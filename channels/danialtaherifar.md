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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 08:32:57</div>
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
<div class="tg-footer">👁️ 177 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 310 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 539 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 659 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiyacRXJ5VxPYJ0ZFOdvXrt4kFDAl3mc6dUMg7Qb9lh6fMZLV8WUwtLhkC_iN6rGBqNHLWG_HTHGoZOGgfGjJ9Tc1_N9saR1Pw4FKQzdejyZ1dv6s4A3bwqTwDlyBZqzwc3ZMD4asqtWbzJw7GFoMfLl7J6DV9EP0prIPkLYcuuc7Ojn2Eeu_oVEWBgvTq_HvGB38n74ZbZCg3ZJCosk22hclOBBbbe2TG88lvBzs-GEsAXEQt-Gf2ODa0yCKuvl_ieuDBAjvHinzuXRUSSInibfZgfHuVnn4IjX2hoclA6GwgUNFGfhNxrAD6x_IywP5f9yLoTZlby_FmTvpgaOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Elnjd87oMXBYQ0OUqw-cW-6_hKPPQ0ULi0jnH6b18WPA-hl7KvVJODIwNE4B9x1hd3LExvWhJUVL052BTuyZXVFr9cBdf5WoqyH6cRu4goDJPsIeuyMvHpqawXsgYoT2JISpGXH0qgSAnNIJohuFDpGH4N7QalHdet4B9hFYuce9dVLV5xLJbxEaOceg2K1r3_R13mV93oT6VvnRrAirVreGcSIz-0g1kFNJDrJJZIcA-HtKZRQlZOHGUAJxJOfea3-7x4_pDT9JFkiylHpwNL6WkLTu-SgAbeGNEDCcqhWiddYDW6FZ2vmAFXQoafsjuWcF22dAswdwcOWtsSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNZIhNwG5Z8kKCBCvPnrG45_XYXdTFzWCK0jYIG_wFUAqWcEc6GKHPto01b8yYQP4-MlCayBiMVNohsE7NhM4wVRDjkNZfAu9iHg92KRxMqaOjoRYLsWEuI4mIhXn6vPin0ziMLmcPCiXmQBd2TgzYGIw25eHihG8e12j5CmjEYree-kwk_0aGIp3pxfoMX-n0pB7n1bUlI7L3swbRu947b3r7VK9tYjKjMOWk7H7h1TmswZFpPRiMr_qnELs2s8FLy9uzMKnyJXMh1YCqkKWZbZlGC7C_MOycadAfUNNCGPAREXJr6WBZ7D-FAkMtPNlgtm3L41GnWXvsTrBtAnBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYvsbMlsMvaMFykozlx81gDOPDs8FoZEAQnZlDJIHXwWBJdGjop-FlbBmM16i6iHB4Agegfct6wisDFCdeXuixlQfVbzi0j-BKg8GWNlsxJSYCOwv51Doz3FKhNzAEfLmUOiwr-V5HtQ9rcQPkNhxIaErVbdr_FeAhkJYZa-pAVNtlrZX2tAMDaZENo9c6GMqIikuHwuRZUcV5OshanFhWH85UvsXkcEYDCN1piupfy2Vh9O5XJEjGnQxgOw2tD2OYvXe4MFaIVYc3tbBoCw6M8NjmP3cfmqSolMl8SfJk2IalxN5dyWI6g3kNmLzVIt9U85rp8rspzwWnORBoHyfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 911 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObRxaORZum6XWxmc3sBehCZ-ATWs5qgeEqzSrGw7SQVgfAsLhsNoB4OEmcEa__gCRQRrFZKbzrJHnFLhJrElsV2U9KR4Bz9n-5B9ldhB5rMZV0NJgBF8g3VTbcxwyQUqAuyfcnnXBi0SheHcYfZJ_ba825YZOw65WbSo6XZ_-ABDtUWDE_ljvCkI3bZu4BXQs0_4Ym6RfBQskQjJumBQa7eNskOlU9H-enKRvRd45dX7_uUVmZPG3nfP29ZeQpTFQBXOne97mbWfpKm1al4gy9iDySSxgGklRTkAHpmOg2s0dZVEbz9gEnJcz2WlvQx3OSWwwnJn8NbMi_b8MxS3KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDqmybWjCoVbTfU3oTcgkZ_8KdYsRoD5z-7u-71VW6koo_mr-s-LW-SbFb1S89PH4hy5SkyXpPlcbBROno1QG_C910Ui-lakdEv3s9HOP8Xc8tOdySzSGVjqPOKbIycJdlHUGc7LINIkN8J_beSSL0W-dPkdPByaFnJOV6xcgnBMmUJmRCwetb5TE2_9FjfueMhRAY36WcTGZ8YRrXD-0alemSILa67QXbonQ8eUD-3rbZWnA644gq3FjUaVAEsd9DuU0uCp2YnjoiWs_PYL6jh7RuAGT68eYm9xbAbR77EZijyoT99W7DqpNBAwhyB4MoiQCuuvhNZf5vq_fY0DrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjZ8OfC492apqJr0tGJjNxrLl3CIEtt5p28-VLy8UEo2HUbCX3gdatHCwDN0IFwN6Ato72lrWhtd_TmA_awTksCudXuQRu40125FPeGf2nxjAoLv1rvpCE37upzmELuovqfThmg_EIhP8E6M5hzTavqhvBIBCV5-us8FMEcenCH96Cz3bwTSA43mYDpVVBxTg8ECqg8uQ49Uo2sUS--f1WUGmhRCYMfMKeNeJjB1vbDZuFaF_dTTSAelIXUhdH2OkDcrgDkjwhx6hgotpJEKZJhWAWQ3eSJZdBuXgZ0MwLRO8YT9syn4RKLGnUaKO9-n6JpHIZ4rOMJ35YWntuKvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cw4kGmxQTRanCxbLH_MkbFGL43HyO9zIHa-lNEcBE0rUskyJ5P37-o43iI2vo1bKbByVQwg72Qdpf30sXV3HBgzQ1ibAf01zR8BhXeZ2JP_42PUS5G1JWxa0MbXyrwH-_Qxj2m2J5XxI2Zu0pu0MeI_0pjyh8OQHiuX8ZOKzjB28uSEG9izyjXF2a2Tg54lYiG_c-fVK9JPdqfC97pOfmP0crf_TFnva2iovkWqs1dALlFYCKvaFTIH6TPZFLbkETTbocyBBUE_IX067uOdM_gK0nevPgBA7wFoNejwpzTlejU3nFnjDVgRBxlan6FfWXFfkFtZdr-F5z2ZPOPUSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYndpwi2RsyjfbFErb9R66lAI5WEpug40WJQHWpybNsrSnseAq-OYQJ7X3Qd6KkEnXz1E3H_T9i0aPP1tLR0f4YKOe0RRhVlBwMBtjlE5ykb3QVJH0APNI1hsQcmGW3RBu1ofZU8n4l8KFnx5Csa0ryjt8j1PTvqkYL5QB8iuBXFwZOMkIsh_pROYSnLJcoh0OnbBIlKcDrdUNH9vK2RLGLWk4NKWzK63U7aV0kznOJgQR07XtYquejeI7gKlWSW-yG_lpO0YR88Tu3_aBgI5nmCylWCmLz_RlKubfKNS0ZNJ2kplN8AsGC63waKEDNllSbtAoPBMy5mH418Nqa8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbIWQYDOoGdgI9uAdIRx8dy6Xw3ujlJ6hMjSb8Asac-Vs0DiO8d5_CjWLJnZtAIS1KObzq0xHyhV-IJChjBoTw5jjmp-3hdtKtsM314uWlhKBoYONkvO2v3O6iPw2Sr1HAGil4BSnVBRo9nCAAO4qNfZuyte3e3wBPWcSp4TvKiMDGU0fyAZ9eoxEupEWEIqBe23Vj1URqnhRPnaZ-kvlWMrOpIbNfZPDaYBOR2xWRyKwud2nQSyvf1JUrDn-gkVq5O0xIOjgefP8vRpzrUbNWeF2iyZCpIsqaSDs__RHXA4ufMI_4cSKwsS5b6TirqxHx94_hC6z_s8ItqJU5NOiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0BWStJj5SgRftrVlZgiGmDAvqbmmMlPR29wepfRWXz4OBuRyeXYGNs38fLVO6_4F4h2VWxi8rLTKIldJlhoA87qzfEYAiN0D053T-9OTPvE1lk01E1mKZ0OFuRP4-AQGsSsMijAVnk9bJ_slvhUiShHRmHH-BZy2eNi_Bt9yY2FjHg_GcYK6pi_JwpE8lbYOPVKLN9GzzjUcTxWnazClzbq70n2OFk_fayaiyk-Wgq_Yi3AJpYsWsLt_VO2t-UdGcPkZIfwOpq2qTtFzZRHl_N-Q4Q8YauluG7q2FWhrtp7RHtlvyViXju1uQ9tkyjOoqSAdbAJmqq7FA5uJ7Fm1g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=A8b-GgQUtzucalpipYgnWl2vXZAFpE82EvynaNpMw1fDkkTAL0CR_RLhtc9jkSzoLBfNqziG4dYwpu_qwNpQVTTz613Pk8Va6L69A3k9DO0-CbKwewqcC_dM763grh02tnHiIPh9Tiw8KVTEo5glTaD-4eSLqziZyDCyF5SWQ2pzkuLUDN_Mz0ubAPD7acr0kXFdc8rg8jhodGzXCwYSsXykcrjJXv3K1wUdEmTOTDJuD2YlKqkzL6k8OSy77P_NbGz6P3h-GadETNbq-KphH3C1Y9coMgUYh-V0vc3clfR800D7zo2E8vxyaoBVt-CP-_j6DyuWa7WHYshxBwRqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=A8b-GgQUtzucalpipYgnWl2vXZAFpE82EvynaNpMw1fDkkTAL0CR_RLhtc9jkSzoLBfNqziG4dYwpu_qwNpQVTTz613Pk8Va6L69A3k9DO0-CbKwewqcC_dM763grh02tnHiIPh9Tiw8KVTEo5glTaD-4eSLqziZyDCyF5SWQ2pzkuLUDN_Mz0ubAPD7acr0kXFdc8rg8jhodGzXCwYSsXykcrjJXv3K1wUdEmTOTDJuD2YlKqkzL6k8OSy77P_NbGz6P3h-GadETNbq-KphH3C1Y9coMgUYh-V0vc3clfR800D7zo2E8vxyaoBVt-CP-_j6DyuWa7WHYshxBwRqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsuYigxlYXE8dcW3Voh_55Mrdq_sKNI_RUph30lVcLQ5-knY3fJreAEG2HSkyPjSKdbkkEAgR6c5LGEU-5TeND8HbMfEGQbQKmK7zA-_uckPgQAGzJIlJfOt9DDil9M9X3Yy5Z7q0_NNUKht1gaH_YKC3ZxcIl50bJ6zRuKAsYjH5oemlFOlluK7wFpENq0O1PJexRgwV9RFUJPtzhYCoJmr64fGAdbjCd29G7gnrX8pRs70obHGDNNv1nLuO5w7zssN49nR_l5PclD3z6xURNUbsQrFzfu-sy7OV5fCV9EfkHnqQPJMjW_BV1w5tyf0cMAqM-ab8cLI1IZxxcwByw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkfMf3vcVdRSCXeyMmmIU8HhwMA4R7dx7-3h308msPMEK41GlOnmfN4GC89UBoOw43EfG7AXb0v-C1Oy1Z6OORCwERRrOjMMlG6F_rua_AKfslBPzlFB5j6N-h1kf0rYlzJs7Il32e_6-XYqKwG2N9gMI-b0AysmBCA8ms0mckNbRIGXBGHD2Mv5Xwlibn72RrhkBO6LoywrYq_D4nVQZTioPrqpW4GZdsjjneo8fhUE_PN-1mNAL5gFOpQa-ZEQz9N0JcgXDhgbPBL4B-VxkUgLAOSsnMAIKBOMkdINEubGv3DCAoZsqKOXeZLfBhnM_BpSsnRocl-nAaffwSTiLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ6o-68l5-3RxblEiFK6ipEKNVwlFnoWazib9YuFrcx_8uvcg9MwdbmgbPzs4qVuyR4GDCGfGy0F2zpAlnet8qsgtV-HB_lJj8nR7VMaxEDEliK6CWPTtPNmiXwr_Nhdi68KlirnKTLVAr506gwfNCuccZJslS6q2ENzrAoN3B5-uaTVYD924OZC1LJDIVdBXsqvYEIQ96UIhVS903Wrqun-IaUJr6LcDNggAjQN58Efp29z0Ox3N0NzcLr-ExkoWQMUMVZL5g1dIdwo0QLTy3R_GtY2q4ebFYMcfALO2sTYODqQ3msFGa9v5x28J3Q929LAlEZpbzYwSd7KcorIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rC3up2o1nLtuFv1k0EILG02s-EZddBQodQRBQfh_ZFTMR6ylc4aiZbw6OCGbH8B_NdwLZ8MUDrLe_do47C44QQgeCELknlZKIsfh8SOhUNX8v0i68gCuTg_0CI2IToCz-049A3V-09cOeamxFKNAv4Cnd4-VTXPearXwmEDCOqokzho5cnQwkMDJZpSD-UFvbarPoKu_4AYZvnOzdPaGzZGrTWTQx-ANDPtsP7crId4j4zOnIUDxH2t30VHHHqKjOQiB_yLLQO3gWVaZU5VKaoBBpt0polSctuZuTKRbEgsNbchTx8gJ_IIJl3A80QqbIFtK-FAtVxxxhk7zDyKe-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsU9mvjAhgH9yChhI_T1dzmePIGv_TYl_jz6s3hS0t7_Il3fOuwtAJMWKgN3oH2x7e8Ce-9FUZOR0H21UWGx8UTTB59uDXP8oaloThZqczpOc80ImzXa2drWeOSKfaGfxf0hLT8iw_F7pbC-VNGDImuatxry83AGwOTbWLRKyhAEDbyDfiJewytadzrJQvCEq4wVVhGr3R0zuLCv694BCaFXdacKysFcFHjPqP3cPgCHmjBFhSZmROXeNtGxD6O5N6vs941snEPorfhBysvuuqb2zp_QVaGLk1SoDdC8HY2LHM5KjdEFIZGo4PpyYG2imG2CXtLTo6yu1dsVViaT_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-HGSfcB4pvW5WSLeUnyRIqzuybbhW_rdkFnGHO3xASn5ioYcKWGt4JoIccSq1IfBoUFoyYO8ACZGyAotH4QWueNA3rO3NXx77zWe9ie1-RRdLySMdnNuIJAs_Up0D9l5icfoE8wHXNAu5X6U8S3q0eoqa4QWNypO2Yt9uqozZ5TV9T_zw1EMo4Yj_J_vmFHpe9lchU-JbYb9-Uc2QagS_RNY9tl24K5aAl__C2AqniPeu4sk7JG4W_GXwAsNGROdfspeZVTkzOCyOWkFluVGRzryylINrFPmRSWfuCjw3bA5dXyxOQjz_e1ahwDuIiMVob0_VBVoXl7G80NCZK9mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9cDR7RLzDZ7SsBwKt9hOPojRu-sAzGXQfuooDg_k6Xx_p8EePYGhc5jpcTH_XxueVIB-wy8YRmfXfpRbswoUYpQnGdJzMjz3gIwqHo3OrJ3k0TSgCeRaFQj8NhczzfyUi8M432YnVOfQo1diGbkmvxwj4oqJnYWkziFYkwi0B_PNZJldp1jLuKkrIoga0P8Quy7_fByzSVL3hXF_RVPzIoUoLDC_UQAbk4UZwVqUZGYN-MA5lndrcws2KRGgySAIilHXJjNZDxz8ZxATdwz8DrUfzp2cmluur7dMs891iSdtxfRSxD13_UTLieOyhYcW70w3uzmiK2SqafA8Ta9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mP9iYTGGWA28wDR4Us_d0VdKcKQsStvEZfJcpFqegslcUA1NinZi4hrfCvy5AX3CmsmBfSpEsbYEDXtuP79fsruiAlav5vwTZQ8dqQv0yUnVxBDvjui9Hy0SdS1hx-TU1b-3ZWU0bquR-1i13IPqXNTNiS_35VErbHJWOVJkT2hzmuvPBXzram_QSqp4SWfIaH1twQaCugbQ3arypofgYB5lOezkq4hRMTngmI2ZF3gafnkbQlDqUoidQFLGBH4sTUjlUk1tRZtXPsu_tLyZGmlan_yH7JYD15I4Q9uIfjaHIdajz7zWhiMnpxarmBPWwsZI7M-iI027vpu0rpH2zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR6qhYWVPQKyNqx42864LFGKbz4WH_rQqabP5MWUgxMO0VatBTFYnBpeS-XY-RbDcylrt3STqDIr60n6gGTEkszz9oiZSVX7LMbDqFJrBBdj2MbQfLuvY6w6AWmE2vQ8z4eEsCsjuUFeag6RZJeW9ob1M9LI1BRwuYAVAvlkfZOAG2lMQwuUOQOYOCuEoB-bPJ2uIOxQEMcwYLJMjqP2_9HzcYWhLFMCDLIksXV6GuAnmAGCfdSeGdQSx1_aSlRNFE66QesIcf7z8s_hKhPiWDCA7Z4KJu1PWbiLWUEXu6V1jNPDDpihT0l9_uDIVqVX79hphTLJFq-q_DJMuTBLKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufY93I2zRPhy2S8lAcq8YotSBQ_oCpFV5cjX_3jezIGIFjQORZ0Ny1oiV_bUoWe5q31ZG4tqiBFOvCgWHKkqhgez0QkPmHAadjaHVFVtl7RDCHpyihjxowcy9uVsMJUHyfg0V05Y1OtwvcUDnyjqBhd5_EajObst1P3b1djhMNhVNKatVkoYgniqtPg8wCpiNn9w_wTxHDPiKd-upMhm2WmRbEPXXbXPmlMG98NNg-lrS372kInktBVxluYc7dTMsjOJMy0oG07jfFhke18OST5Yjs4HaAI04TkJNnEW8usl-iFioXUuqVyZOVy4AP7hgEfSBvB8wrc8_QGn7_xugw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py9gRPeExiCTve4gSQ0TVFE6y972VpNyu-WchFZklPyvkknIyuSwpDNM483-7rNnknxMIf7PyPXuRQC1lkzAzlWhEnyX2e8XWerGqpvLltBJGTIe5gXyOddowYTjY9AuGGEna1z6shkQFr894-aQdoFjSbe-_zZZ_SkhhY0ocVOv6NjKiYoQCSm9WSWDy7lWlR5hzYVSZSRl0O7424FCOXL2VukfVcEGYCu-jFN78NUnhotlt9WDNmA59Rq62JQS4QOZhGBovDadtdhp7nLlltBr5suuIXr7ck0LlEDEcuMLsJ11QN17srYXC47T3sRAh6f3-L_XHPMbb8rssCep-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLOh_Mg-hg1oJwYFo2LdvLtWWJesuNRSq2JrW6wdq3F0GtIxSeOV-GQAUFvfniQDPku-RM5kuNMr5BYx_y3mTY2n5t2-lmBaEVp1s_m8pLZfRib8-x88JehuFOpbth6uZ-nkN1yDlArUR70Ouyy0rdDLnljfOT8op8OM9WYA_typgaLnAwTtujsi5fPqd55RbTGAfREPJNnS9htMIaec2gMsFSHuAxdwD67OFk_XCHWaI_A5ASanl8YPXu2VA3V98g3HJb8ZdPHpWFF0wiGNCJtDD9yJCd9q-WS_J_pPzt85iPczbfEHiyJFmyGWZLufWemfC1TLpPZlq_6zRCqTOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CknkBbi5k2rvwBuqnA-bx404IkQWnW1E0k_GzNYhJKJ8rOIUGuc14jvskNr_nVwwAtGLz--hkCPNUF1DLxmhdDV5puM8zRJ5kgjTc9xplprO-LlP3LnXE3JPyjsxHRUvznk3hyJD3NCYNC64EYhZykfQPy0ug86-42n0PmeSHY_fA0FHrUR8XKEqJ4S0NCGd1P9W5h8rfojC5aI4AKQTlToc9B4LvnMKbuHCKIwTylivsJF_j-buaXwbXk53jsDjEbnxTxdNx5ScO20Ow6UHfVBMTnYwsybYou3lzzQZmrDtP9WUqAelTCusrAW792QJVEBS8RwdrYyrWqBU6MTWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTImSRUS-d5UtWL1r_f_Ur_Od0wEjF4xCgA62o4TlLHyIOb3NVu3hqTx0u9xB_DU6hUpw4OnDMAe4ihCecx_OOw8ceQDUMLkoWBE05j-OeGjGHfLg0gVEwDzEZQ4nHIczKX_5G-zbmZMz-V2td252ULLDrt-sgOe6hI2VCdFFqruFc4wiNujOgtF6vPncseSf1QEvrpK0jmNH55hfgDzw9J7TnUJ5eEsgjYz5QqH8aEppr-9AC95wvoHZ0X7YwXlz-YkIcPIa6jWOQjDMahanb7t6Ftm4qJtLVJjMUG-pzwa0HGeN4AKndV_UjN2G3zCmgUhk94kBR_MBfHAXm1Qsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiPHdhHg5rmMLvx-g2kIoH0VZcBLmD__8joKrGtyFAgwOhFTGmgF623aHwrvjv8XXQk7LcEh4DavM8oKQPzzbC9W0MiXxTWc00YERSdAoLYLyii88zf5WrjbYq26ybZTp9erIpReT5wsC5awEvjFEYIbuXHq5qrU1PqirRlqqUcoaKxMu2PPo3rz97HltYc20Q_-ZOnpaK4lzjjkdNXa4EEZBW890-fQXv5Eu_vCjCaQeeU-tFJoAYbuS5ophkjAy53ycd6uDGj-L22bl-jD3t99NKGqjgrpBmFK24NaQFt1RD1oBtWhi9-Ad3Oqh-KsZgbJkYuz5WnALAOY0nd5Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbzHpR_hlu6CY_-L5TptSmn7Iz3EXor2MIxYDE95ZsyfJ2i9alZG---v-j7zi3vqCwLUAeoT1dZyZj-52xGnAfWep846qBwxIxD31WzGgtDX8GQPVlQjRGNCm09T4E2-cCHpc-tXy6jdXXQS7wCdHnzL7iVI2lWDH7x8azJc7vRDAahIII5vEiJSYyAOaoI-Enqn5cHzOBcwSFmHoc7x1hIUKdrjp9eXnjh_9_aKReHOXI5vv5P-sEB-rWOntoFPC0mwbTScoxz0NzdcMV3kxBzJClFHzXQnc9kXHYcyQGjizV7a5ewM1L2eBvII9a5SgyHpxgOrJSe0LQrfKGgznA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9miwUKdtJdxX-nw3coehU2FDZdEGhVBb1gFB6fwuBJshiBHs8mqjxf1Afy7Y5kxK25275Tzk40L487qHGfuAaY3-qY9IgTO56iiKR6i7-BD9PPF8YJy540qH-2nAA1O3HntYPmChBAj6kAi-T9HnEt0qeLAU6MSf-4hscgcCvZRtK_wiE0tIS5xGFo7eCLYLYR61Ms3VBWfe_b7mP68IvTSQaGy9uqdriaJqaeuDoYTlWUrMds93hE21WvLjM1reroolF9BdjlOaz2jIxYFFCVsgeNUMnxcpFhu9-rguGvnWEjV6Zs2qxEjUA5hZtEnPI5H_WBCImj4iBfcm-E2jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ-79uIN22p_Y-RLBv1mhZd-ogIel0M3V_Ys2vkoxT1x_WaaCvirHwNvkkfKS_H0xT64BxXunMJFtFGVipjSTZ6G3QOyubFYWU_7RO6mgcmvX2AarUJUGs4AXo72D_nYyK2i18IX6Veg6X31flcOj2q99rRNTZlsIOxDAvJVEnoAhnzwqZj-cz_oj3qGMIgqKRP6cYdSP6atp62DKsNU13hM2_elsY_b3yVIEKETxOyka94biTz6LJetS5d6yVuU71V_CFYq6L5fQ0DqpokAj2E3mrPmUoEl4OKHwNZL5snok5YWYHvqX8F54g2RFXGzfm5l_E-TiR9K9wVwCnIAyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrDMBatKsvmaaXRVglzPf2MP4m0mLOcngngNU0RBSUsurAiTXBUhl3-Abvx9oDdF2b9LTs3awag-58bz5YtqVpjXztRsWnPMI5NWzxTWwCVQtG6fQowZm3tIKOtE1DkmxzDvnmxV-1qd4PUifosMZ1p5pSFERqEUp-Ph_j4L10pxQWlV7nG3PQMnS0hIPdBq61nxIpjBHk5KiqtjB-uG2pr1Sb5Ax0JFJNfNbMsb5lCpAYxZcFOI4L6WIKGD6yn-HdFRQvTix83vRTMdYjU4XTGJFbS1Vk_Uwd5jtrxMdP6uw79BdWM5yHf0tVu-gPq04W0n1xfotit90QbZoUx87A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_BdZdfFcet2Prq2yV6S3sipj9DDkfwCayfPQxfpqQQrTLFyKRIoRT5VAoOkqLqt_gG6Pa9Ukqu4XP9rSRjuhtXKaVElaKieo5yDXgW2D36ocr71GtZrfWU5ok7GP1tpYXfVsCQMaPrbrpWh2UlqWJV-jgYpcLbkACeSG002q1Y1Og5JADBkdeRowLa8Pg5fm4LeTIj_3UJnYWDvTBv9zActigBC33Hr7JbNGNI4UFktID3l734shGSCo8GJP2GUs0D_gkVfNdpI-su8NSb9Ec06V6fBImI59rYfmQ3YBU8mbqNIXdEoIo4aC1LGIDAgMo6ZuXmMa4zqJM0awWLigQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXStPfvx0FUeWG9_Y2BkFi8BRRB36_bZfvibnNf7iZwbtRwXs6eaXB_k6WnUT6ags9rGNYfOxHXXgZg_AJGff-NKFPAPwuO8IbrYvtuqrjD_Vbpz_DrG0TfON14hXZ9RnWu8_VA3MUEHjKfWpOHmOu0Dl3MnHJ2lokeZCGhik6yNekHA9B42GCkNDBiZXAAJGE_wWb-z-Hhf_8LVD5ozXi99Mv6Z9uIqnlD7EBoZT1CflvwAE6zpQmOri62ZIBRavI9Hv4mnltgVJ9Cx24zDmUJdK86KkAt1AU39i_sQY0dXnd31F7ozgkhMNGhfT4tG-aKGp1ZbiKE1pg8WeOu_Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQZe3FXL89uzMVqR2nTeJWsxjK-KmOpoc9Fe8X0_YF9q31VotBkeWF5ItqIWOJKBFaOYdrY96rgZWCJaRNh2CNIEpu4LiHxE7wE4K_VNYWVp9NCffips1NXrzCm0CgIxvyOPjIrIlH3F4wHTjaGdpR9rHiO1mn-XibClTTte9ftGge1sl2ihoTG8eRNDIcPUifKd-7BCVGNrBIKHMbTuE5mBJunrPPM2hsR2sa58raNPITnf1-NXEwQ24I09fho3tgr3xCuJwLAX5Jxokfr7tIhz8PcbansLZ7GtjSAeliKgEtbQdPpbwLK2sdzz5XRssAs9rgsUkkWv-LCEnESAgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxZIHXKwKcezU6h2hL6sqY5X2W4-qblGGXlrcWb5V58DhbWLyx57Vsp7NT67IoDERhT4UCewILPU2Q2nPS1RP0rex-45HrfIVG47OfzKzKY3RpuMwNxbek3tESbwoCr4saxotSkBM0EHar0RCn5CumeZ3boeKDattEF1CUQJFQkeKy7qzKgnUuDxpS_w3XJ_JBXDW1ceh4XXm4PeZXIC9FfDhNV5JZ9wEoeybvbacG5SbvNhUCQxO-MdnAZKlDiuq0QxhePbSC_jvg88fxMh8ImLs4u3WVpot8LIIeU2yYwcHg0nY6HdYro1mT0yIxvFFJqQF_URYSBk1K3fW8UxSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnOKkN5WjXHTkz8IDcBMc7m2aGN2as_AD5aPp52klpGEUHWkiJ4Wus-H6sjyAg8XKmkNJRhXycdtrK6bYagvqQFmUyuODskAKE7DRO6X2p-NGxqPMag3lJ6UNc98JMK8iih8hR2pqlsuWykDnsSaTC6SS287zrgkqMhRjdZR68kjiHSZWgRTEUGfeGyUar1BZScbwcU0wM_U13yAraIjzjPp71lP6zmU6C6jRlcWjXHohjnYM7LwEWFnOB2bL7DaiB4mVMNc5eFiKtdSBZEsHuwT3QuuukUV-FfF4zkU5eY2kMy2J9sPb5HWQIlXFGTNjMWeNJKb5XjJuz2D_n000w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnzeeZzGB5E9jKQ4wpvuI53QvKyDoyNOrHZdjFykkM0AeSrvHHUGCHcu5rMHRAiuWvKyDhz5j1Y1RfZLMK4nSy0sWTeGa9bjzLUY9NLkniolffszeNBCOmKBsTyFv9GOJkoEy6T_wKH_rDF1VmTAvad9A9pfgd3zltACL6uFcNbpx75iWb60TZZIh5HX5UqSbAYWuRsfEVDx_dPEcICSWwYS-Z0x3o_eyv8kb4-RvBDhXJ-p5ZPQz9C3SszVjhKGOVA2CYKpBUAVMBF_C3Oc97lDq4Vn2fR3pEqnO9iJpcTEFI-g5GrGshthhlcGpTrgydc9rlkBN1i9AeTh0upnCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3c2UxZpkdAmgTwjCHWHxkzDxbcEow9umJ0fnit2u1OftDWpwIgenYVDUaSBhyXatojD_3EwjLcvlIAdCRy8ewLLrlFF7SngUegzX9jqxoQxmLkLfkYNlQdPxZz4M8s-t9_d5vU1BnvEzS8ulRsn-dPf9rcI2SNd5oHEwPyI0IbhX5B2s1lCFl5sDp2Eun1e1IawO3RlYWLsOpQX5OmF3fmXSM2CXQKkv9RZmsZkNRnOFkybJhyYIsOjzrs8N7L66J5YgXEV_LRhx3lGoyDJsZ9jH7s3M79kfWx8c8Dn5XqQsbyJ4D5A-AP7Vry-9jKX9a4XRCBaWhjTqepVHMt8zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9fNWSsCuENiPyKBs1RLgZaNUidxrNbr4XkIyMC-aRFoytcpiSwbSIKfTCG2xnsabfT_kqiPukTRxDDh05kQmB2eenO-H4mCDcQ5UuVjBKtJqZAVYc80YnxnPdsHifJWSjX9T0JYgNK-X4qAdKY6ia9UhpVkPGrnvMOTB8bVVBizleYTzmyJP03sOBVkyFkfzz8vgRmF4zovWuUheG8jlYJPbQXHj4YHR5SPS51IVDQtZfbG0RgOsMRNm5_4pmI-MdaCJRh5xklyt2LA21gFjEOfTQMFAp2YJ0AV7WzGtorpPMhEcEAa3qE7bMPZkoyvwX4BO836xDq7U8Y152i27w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLAWIqTXSWAMv46FSb1vDylI0pZ6S8Wyz2RRiXVQGJyE9yhYwUKTS9g90bpuY-DBeEbJ-3n2HA8trLwJKhS-hvtW29ApYWdgDWTBW-p2e4lYmBzcoyNbYYIrPgHD_UqUgcpuM1z4aoWgYP7yLiQ7dpCZVFwAO2xrwLPh1e1cXSOkhCMBxQioNPdkHj9z2JIfP8zMpn7NbEe68nZO0Io6f8N_eWDOogT9ztZskKN922p1fI4nXIZ6lwcekwDEE0-T96R8WfBoSUOQXk79e7gzCGyppHdThkJBxEXYOYte_MU2QvV7z47wtfWOI3nINymh2NMXIvFttLeOMsWO30TOVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVGPZBW65dFrT4UUmoXNUkJo-B8cdSiSHU0b7CRuTaqcQYfYkkaz1HaSZtmKUmbJ-XCikirhvZakdJg5jxtM8UBZrMexTPdPjkR-1cjUxACTQgSNL1Mw6p8IZV7xHxNHKJCCyReawvR9Rg728NCrQTAC7yBWsOlDsFl9ANGjuaGVr_i3y-8sFXh-Yj4h5zrpoDF0A2CvTx5pdhbHlDq5oeUXZU8I60gNv-PgtMILHkMw1TYywBa1ep6Xqx6gFMAPTWymNY1odLYaNetjlU69u3mXAupbazvEWm_201KCHhCMOB0ZbnbU7ukmtpEr2nadfqqXg56bQnLC6uqfsR3Ywg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRsAqney7DN3Ws25a3RqzRYJ1S2KDtRN4yNRqSGU-bAiImQ-SW0hw6VJaPZMI5xAvS3ugFX_M5Q_XQOylNwsUFafb5rG_Gvp0S5Rhp5N4mRqcVY23JfUc_7ehpV3GHz1qjVhv8DT1cgi6lP2tF0uBOZB_RGg_-QEfQHWPcnTFSijsfhPcPiJWyntfLwNhTE3h1Hn3dxQIS601lUrgvXOsxgEMsDcpjPrORvCY_EnMPj8VQyRNjPrm3qwbZReTgPoSTpgDhF8rhO0UK87SS_8oEwjkKHnA4aby0B2VJkOJZ4enB1B3gAexbwWkT1YS3vwM006JtFVH0aYAg06WjRtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbfjZFDc2nmEG2DSvXKH-qwugljpwtFLS3Wqo19kzJb5cH1XSk62aJ1YsTeZIuIyPXb8YxNj2t_WKNAdjUX1h4PDLlKHjB26_-d4kRdSO0dnrtssoijoeOc6QWdZC_6e3p_odDeJaf5rzlCYEcwJAgtqsgQn3_MlPuzIaUMsPtaXlAZuwP7GnMFWg0vzPeJBO_VCMPBn676CvfKqA9NFA1n6EePVaQ3rv7_tYFpz7noC3qXNgmNW1Zm7umipdA-JSr38vnbI5_Fqxr4Yl1YL7StGrhkyzHe4w3Q32UrP33Pv4cWs3L6SGtTJBz4pU0xbhJLaki9UFHfn3Gu8p_qmNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ay0Xlg1UGNsJKMwd58mC3NcbP7UN0_kwqtWFrA9ab6J1e2Y7o11pTbZu8KEnF4sARbMiUAzjP6II19cGmraX1idor1Z7MBTKh8F-nj5KqbCs5RXc46iE_bkoEFV6A6nQPMqJhhzlFWzLPmWgV-_yXc9q4R1y1HrubNhOkCnmoCx0BSQtILGGW7FK3YdFZc5EnSaaBZ8iLqQVR9Op43a2A5ZF6U3nQcPqxRyS82PSE9QvHd7ieW-x-1h7yFOTb3dWHArNU_5sleMJcc9ol001Y8UZwaiF67TYPp2iO816Couizxo5FENQGjK6eWakCPYr0SxWuVUXC2XjfHIrR-walA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5Z6qmzB_eyQasuH0KfWGUBMdCECNitjz6jL-FMuG3lm9A4I8P1-UKETN6DzJhSSdS78qsLIW1O3JYMLiDff4bivP2v_JVerOsJCBvhfO3xbfvkudMWEE-8zG3_1S_Ov7MO3OPxEi9wJr6HBNJR3YfbTPI2xr5___Lji9f9I1vWCQ9IvHFNggsDeekzCSNQZcs8V9DgBveg0EArqQ0k8t5zWbkU7d8gylkPeFG1niN0r-7VoeKgU0HYb_l4UtYXg-RXr-so_Qpr_6_e-FEYqPNJMwBk6tEvHyvv4wISKfOsn93ukW70_VHd9HS645VgnyMNCwlvVL-tzORjzOgGarw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufCuuhnxqJCAhwqJt4GdCjUSfPtZW5SJHmQP0wxVMMs9eQkV5kRXzut99-C1cFRuSUpWyOm0OBtJRAUtXXISFZ_5HVHIQRFNGg8jWK0vrUrTrNYBd0uxmjKIiNALna9UM8mi95LodXa6oZaLDpeBTrGCGNXSA6s_cvkYyXWrZY7OdWFj3FK3EICLJ1owjo2KSO21dPWxx35SlVCM0P6B48STBRw8pykMlpTPqxqf3L2iETf28ucl_AdH2AwkcW-HL06bdw65N1Q8tU8VVa2uHXJfI_rVK1vXr3tV9Iwuq9GP4mLNm_iSdtgfNGBvnyzEkEtuABuWU71r_bKyy38y-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bi3-ynKBYKmb9SGueQCuIRMitRFO__u485eYIeC1cHDwZMAI6f4N9YElaWM_yUc-OQbRzQoIHGVQen3FlDnDZkxiFTt3jMWFC4Q6hFqBMpD6KIWbp4CCoRtZ5l12NEZF_tU3Fxp3Ms9uGdg8kjZ8ReqZjPPQnPLT_rUeVo-alk39tFZNJqbDgGEPyM3FpW4tumTY6wUHpbkvKLKF2yORhYO-4laNhPW48xJp6awYGdXOaAjZ3zOus4XwouFi78OV_2mbAPqvw8m3DoinOAjtcK6j7ebX0okB1yuXzWWXEoJRmrIj2wITqxCsxru7Ft6dXQkjQMbNyjBvtmQgCmwvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umGkpF4UyjxorJXr2tuxa0uflGC8Iv_AKzjjkg-0nP-phM8u43M44QrhZdCSe1MNhG7s9gTU7WY7HHFIy6vFcR0I3fxlZL9mbevkJYrno3TYSbeL8zw1CWuS0bkArWyykTADLgYsuUfIR95JUJDV3FqeFs9N98CXGlNW4lPfhmlrYn6iHv7p_PbwuxqX4WlWm-5Bn8kJvggudFO27Zk2Xv0Ciq8bsi_94pSkN0Ztcv9w31xCZMw8zb2db_RWAlSdOPzikG7le2pSIS7t2QhTrUo-v_PCAA-i81T0dkKwqNeMqEvPCFPOtv92x-Byah5AZpy9y4X6ADI9gdMaLBIRPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-i-Me_s1-a81YumZL9rtehywmKrhhi28hVM85WVpB8q1ClaKgFH0aeT79OqV--NhJ0px8ClxZpgLkOqyP9-s2na0gU8plUBabEkctKOPX0JXmnvCdYY9SrzKm_esHtkDWRzEhMBd8XqevhrIxfdG_IDveGtbrAQhmqzCmnH-DJfDEIuRcFzriCnbdOZCSJC0oe8Fmo5Hq8dO_a-ekCqrX3tptRC1b4Lf4Tx5alQXPpYThvrEluVhsNzK1bdipsF_86nKt3OqU6xOQJn8WXXZdSMjBGK7gU2tbgNMwnhIk9Q9uDtWb-t74qhkq4yauDYPQyBuMc9ifrUbQxLoNkZSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfexfhFS5jjwYmBCSDqBsJxTWf2MtV6P2rHEFPnNX4_4xvNGjnxrP7J_OdINpPyRjgS102AEm2-LPZ4wCKY0nikOMC24pXVQjxqzafp_xdH5X2a_SCjQ9NgTUxkILncdH9niGKxkUNvoyIUHHK2SOX4jGjB70qCOG0KRf51jTgbLnBHfYUWwZD9vZIh8UNKJy2hq1IHEn1igZeN2hgCyDaDXfg0AoZ278IpsDImFLYy3nMjchshwXo1TlJjEvEp-EwB2p-fAU6pjOyHY3KW6nJ1Tk5f03l1oOfJjlPPC_X_n4KiLFQpKuFbTBLG6Ls3reZzfhf8DS6BG2Z9pzEE8GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKwkwCmcv34p8fTCS59Vcc4_KYttsvNVXOBmgM7r68ajbNFOFOv0Aj3-WIBauBUqn4Qby9uGf6Y9hvFQU4KC3k3xU7a3vBJYsWXr5KNr1D1W5pQ7pULOEAXxBuOh-g-6fq7cMOKijlo6Yhjx-4OvKHRuzvr6_yLyOFMkrs7oOJcSp5hTyyCSZRA7-s0rjHBIjXvnyKCDxtT03J56q8Em2JVpkGMCqEaOjIsw1oa1KwfszZmRIAytKmx-6EjfEGMcWEblyA81RDSYZRVB_7IUX3PlD6YAP8D7bqFiPD2rsRDl8mQ51nI-QzLvHFWh6zGqmxL03V7GgAjQtiNlKmbb6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rt6jiv9QHCKJiXpXfdKLgHZmg_96BKSX9-_sK98p2vsuFMmM39xYwvreg7ydbFM-NkTRUfalzFWGUKxhwoTr-dzdsUQCoodO0y7OOj9OZ3uz3zIXE_ukLEWhezSQWXu2_emgTw4RhqvmqY5iTXSwImBPIA4pCIS_GK9VYtuwt3hkHjst1PSybSEYtmGhYhI2NgqjjnRUsqvjNjEC7vz8JdPkLox8VXN1lYi26wWWBH5ZtTygu-87VqoJZ73fH1NfLxRvbxTFmeL6kxoruKnB2H5W3h1yazFcpVt2kvCCexpK94S2tMxASEeXa2Kv2IJj5a614LiwQFZMUGlyWhqN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6vn5kZlZJ5qOeosvLszN7Brn9PF6Sj9ODi2P6lK7F_XZRdLfmfKgGAJf2sOeoFnkpRIZpcaxcV8yPHW7Fxj5YaCyBiX_hAXC0fhBrEzdHhoo2KVEDn089eYBAwFPnp5Iix8WiREigzmbQMWAH7g7tFVSUPz_AdEXSeESvmb9VcZ1LSS53442RkHdDxV9D1d5XeDNRGB1-9ff-bwBdnpYcj8YdgQiRGTq5HO82byaJjrYvPYvzHhh4FqLg6E7pqeWNDhBBpZIz7bCrcBQ6AlqePCT3N50krH2pDfESddUiaEtKthNYzWEly8Zs9NSHYYXolIaISu5s4U8S7fcaSTBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3R4thfDV5uWZ9D36YuRbmrFPjDOu5lNwsNmZFs5hNnAJ1_7kfcvahfex25ixg2SySKbXSWfylh80Beiv74ARCb-Y8l-NzR-iMDR0RVjq0OxgQe9jlWq4JjkdVl4cNWyDNlYXx8ylnr5_gZ6hA9-fR3uTlo46lQb9K65-cEaYfJtKRunWEh_oHGfW1a22SZ9ZranKUimtS9Qw08rV3Rv3wO_tPyGpHt1auA6t3P-TGUVKeFY05kwB3sT3_U2YiHeM9Jshe1tfN8N22Ljj-3UVUELGpCJvwGpg9avebNHaWxl32rZWqaLcIadlYNfdawfOoH8usVgyg1dbKq4Vtx_3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_8Lvwlvff1ZY8r8c6wlUL3or8cwbUdNJGf4NIAy3BRLu_eM9cbeC_6COIt0Cczr9H-3k17sVpL4Tg-oGRUvfsASKwojoVyMNgX3pxbtoq-0de4gJKm1am5rwsWx7XvRt1GZrp6ibCh8EuuSrJHogPk3TuSUtMOIBh4zxTeR-Jv_Vmx1RIy0Pw1EBdVVGD4F3QFBKkmyXTBr1YxexcbdKeIpMKAGCYrFHpTcn3MCf1nhnZsn_-_mVw5Iq7tOHlmD8FVaMtU7GKqeUVe_vglWhYIz1hj3UiWADPyFv2Ivra6Q7VtSwLN8HLX-Fv3wAICHtlSIIokkyR1sUd9sFyEDTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS6CtOyNvljt3I6qbxizCzJ8ELf-3s9XJLR39XXrpTrmn6rqImOCTab3gu22C8k4Ajo49cf115oYYwtO8FNlPhUVW9EaWTMSetPvitpf9OoM2A9tYXqt5OpBpGQwBFChjZoMKWiA6i7v90tI8xboj2jQTyZ_-GOmx1ftemKo1s_7Ye4Mjn3kyKrhoOJvsFpattRTU-yHubQa91O9405ALfK0BBhD7GcLyOm73SbasAIqXRF4pdOuXhqhw-5v_UImts2UwwW7Fih4NWJJoFjoI6o5kvoYeSU0e83QVzMnY6dKtR0PobHgQY1VmH0XfoRuP6yFX6mnSEeOzlS8rfqcxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4yKMZjDGhKdU1d2hU0AsEP3sn6bG-HA6DsCZWPNwKS7gc2vOeVbdgr0NVvYKaSFbejdn7neM4CPSsewRZxPAGrtiwP-iMhBGWy4jc2P5S3POkFOGl1J8Hb_evuyA9wzlxTH_usMdM0rwErDtpEwLM1U8hGaXq_nxNgtzpuTkUt6d2zNVP8BZGDgdOKj9M667fbtJ8P-eKtKkPqE3aRXSHztKbFPG8ztcnCBvQ7Sntul8ecuhLrQ5bUIsMUv4J9UoFQ6kt2FzAQo5Vn33I7VXpnAuHo5TY6aRGmSBmLkZiTw8iTnx6sgUeqZUySUqMwM4Ikc3Xvp6p9fW7rzj2eegw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=snyeo1p_4xG9U3dSIFaKt9jdBcra-qjGc8xfQvVv7IjwFiCiS9T_pVkqIMmiOP655YX9OWJkFemGZvTNcWAbGGUNlMkrHFoqhNBkHy8Y3Zownn2gPxYOerdzYFp2Wlb7s5mduFKUbpMJ7KI6XsvXLx7dMwehrXVnQt9FNw0Xw6CuO7NmTzN_UQuM3ChMlO6sB5inlBwpUxjIgEyEpwdknagz-HGae-qu32Z1Qj8Qnjc0i3rLlx-BeZZsUJJSrzidxpCgKKBUQWhCnNKvgaSqWPloiDsvVSl60mTmX36-CCj5fGx4wX40MpzOAjWm4op-Fe5ZW4uQ0ZRQvafF9NNHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=snyeo1p_4xG9U3dSIFaKt9jdBcra-qjGc8xfQvVv7IjwFiCiS9T_pVkqIMmiOP655YX9OWJkFemGZvTNcWAbGGUNlMkrHFoqhNBkHy8Y3Zownn2gPxYOerdzYFp2Wlb7s5mduFKUbpMJ7KI6XsvXLx7dMwehrXVnQt9FNw0Xw6CuO7NmTzN_UQuM3ChMlO6sB5inlBwpUxjIgEyEpwdknagz-HGae-qu32Z1Qj8Qnjc0i3rLlx-BeZZsUJJSrzidxpCgKKBUQWhCnNKvgaSqWPloiDsvVSl60mTmX36-CCj5fGx4wX40MpzOAjWm4op-Fe5ZW4uQ0ZRQvafF9NNHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I57TwUeiSZq6YMpth03gXNkS-Po_eSEQ7PjqOc7_Uiovvcq8a1LUmToJvdtJi6m3E1xCa9-A6XxAUPBBzb8ZuX6MYABhJAYVfMf3sgLbgosEu4E-hWvoPTRGUz45thHLIuMLMFl8xTT3xo0-9qOvIJ1NkZOf3pLFu7CoyuLrkeBz6jBLIkTz9Tv2lAfObZyD8SUkGTF0prGL5qbIzJ8CBVYTnWzot0e2u5LjTKi9_Yj9GHuMjZ4ltuPYMkO3u_6bNNxFdUHuVeaZ2PWZds2QaL9-6FGGES4-5ypvnYsNjy0oyGRwipWoZcuMGzjWHIQyUr3UJ20ehle_RCl-I9PYcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSpqjubgkwU9sTbQV_GPpr8zSena8BvGb9JwPfmjXpQjJCnendGFPbUI-MEKwkLJjoC814_yJrDIl9GqlC03keoQLIfU4oWDy7B4Z_8V6qwJ640qqw_J6qVZk9CbCJktovMdx_txOOjc2n7m5ng3tOqKshTgYS2oEus_68CoHnGUDE8lTr7cupuswObZGqUvfyjmi1wJmMvQXdg7d0fzJzyWbZeUsSWqZQ4lHjO8CVnaY06BsrQ56HT0pMEGC1P7Zrr2RPcBsENP4w_bMBZcG1Q4deDGrCmOFFcnUAM7-kV3TfVmFQPVclTjU4NIp80wMWF8x-9TEWaEkCVKk_eSSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEHnXGvWXwh9f3vbLbjYyfwpZ1SQxgaBmK1fQG8IxyndGq6cN4ch3cMmXQrY7VslGO-Uo_LljKhMQq8Fmrc7knL0a04alv248ykogzgxHPuvMIhMEDfAIkPEEaTJChElrCcPXs6Q25fZ5A4JKSPYqCzEB2-JUWnl0XdIIoG_CCHAq_soEz0bXnpXzYvCO_2LrlP8HklDDhevCwf765bjeNX3ovZWvMwXIvDAkpglKmlAZ2orqjwPVilL89IWS7sjrZRyzPdiTHD5vGCe_P3Sdq8h2jQjSm6KSWmV0LqIvqGb9bgounnSnkegpJb2JDl_GOAsuk2e45z4AmFptcBxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWtnZY-NHOkU4yx0gR2l1HLFPjozq3V0yfQjAKxZtJsTS585w6Bmn172G8yQcArIP0tFr7Rcqp4Y80_pDJtnWwtpDurexhwtfqYFzJBfDPXTpsBlX2HOOCfg9c6xlQOpIf3JKtoAbG7OCmyYFHv1AeBAJ2vsvjlNijcjFX7Rgkf3IfLbwstUQ1okoy8SPv5N6tLfg60TCgZlKKVOmQ2E33Rsba5CCMki66Lcl5tXG8aJKm5CNoXxUxFgOFVnxaQhZVGF2e7g4tLr8xM_mgHOq76Yxtcfj_1qvWv_m5BXuQnqFAitfbrwxx_CnsqPCuqgSUq7xWiDnWgtHBchpTd7Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-uJ57NTEOulZ5GsIJnslLWXYP4NNC67DN6TLzVgfVfeSTVaGy-q1evyaI0g3mR0w_rjiUaJcJ27rCBw2xnJM9rBLj0jfO4Iajl1GiIMR98N2Rd-ojhP35nAfNNLeXGRuqWWOsQDL-3YjCMEnwbf9jefEn6-4lNJ7IBUGm69W4Dva8QUmS5JL-WDMHPH3luPvzIiBlMYiWc4x_MBKE4X6KuB9P3udprKLib44kr7o0zRf0ZpGLf6An2T6wt51YKz2S5vcHYjGSU_0z6GTVMXPpNpBnSnLz9hsRBf6ZO_j48ohXXI0KvJYmsQ7WyE8TPHFiUArNfzZToEEqPXopp0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muY5-xD-VeoDo370tkraZs0sVdYK2vyAY4KSXSHp8Wpeuvi0TQLNmgce1hHbP7TXrFp-M5owHr5yxTGQmwPfMWy052yCpznl2Sjw7omOyUMGgabcMKxCtW-qwDo7_cXDA84mOxI3vqlKL5wWO7dlP8GRRybn7MAOPQSwhSny3m7mAUV2kScUo1vaiLAoBsG1POUz2H6Y01j1Ubmw4Qmus2ejnBmfB44FVLmgk123iKF6fp-U764wjyK0KS_JdnMbXGW5Wt1aVfANVP_qkyygN9BVJG9SLRxpYLrzr7oyCpmnjTTsVTirIeuXRDp5gIl2KQ3VmQ3hOi1evn0U5X_23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFLFxINrjOVG8WCi3Dv_bsQZ_GCiELYs_qXgx-7FRTIsANqI7pWA7TDafYU3oKXPE2DbiQVp4vkoqtygJPybujN1SiAQpT5LCD8AXmJT1anca05WiZP_L7Zljxr28WZxe5LDEdBt5NY8uqPoEg8Txzy1Wq2ijcPBRi860BNzciO7QkuC-hJvvvB6cTgj7NuoAO3gwexVFDUyARlEk5bQW6fvh0k8961yuqNbPLWMcfCpIQeE0Y9Pi5zS3xYfX8U7fWzO_weKRQ-CSt6EibYWbC15BH2l5BM8G2m2KnHe6548RbFEFpUN_AUT19Ngf2waoN5YgBgB7bYNF3gOdN_wpw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NeMkgB7j98sZ0OI7DFoFQnx4AnZBBV9ACM0AQ9S3rOyMEBsNE80IYlWWJ4EX9w5SxLA8E_cdDu-bw2dTAsTNpY3TOpDNBCNgN_LfjnkdQ3gOKxWHraB6d1GpLKRUWBZCBL8E0kIn_GFuruSXpvUeYLWUztn3TluOoFQfB087rQYpZ4X2VCULIwq9Y8wm4W6v-1TkvkOKYVLHBXx605vAPNQoD0ZXbjzBErtncUz7vYP0eC0lB33FxlIlk6jH9lolgbfHjrPSIh7sqtCMzZo1_NVPQdPPUjclS2z9INMub0VavuDh4YWWFzXIHIezgKInrozplJ0kUP9S1RgeDQLRs2i_G4V8WFUIS8l8r5s57n08oIb-fUJWCSwYyCN6fN9TdYZPkpUc78uHtYQcresXcYlMsBVp0DgUIopVaSQTkqHTZLb7We9TtyztLDdzg0SMCP2kdanA1T_EFcoXkk0_qw6c2hmCYf-Kifs4zvCSRm-QjCdwm7-0k2wtO8VYe-IA_0ZUHD_0rIZvWHXx4JJ-RT_YdM5QVFjLEsrySpC8Q-fU6FJKlkm0Ga_7tO4ecnHEa16hXjvOPRpuIGag9VLwTwzlU355qYmJx5a6RotNbVnCfUXMChrR5basKhVIrWqtfGJh1XZAHUVgrlxuQGf8q-T207Iwm0fYX9oSy9ChEXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NeMkgB7j98sZ0OI7DFoFQnx4AnZBBV9ACM0AQ9S3rOyMEBsNE80IYlWWJ4EX9w5SxLA8E_cdDu-bw2dTAsTNpY3TOpDNBCNgN_LfjnkdQ3gOKxWHraB6d1GpLKRUWBZCBL8E0kIn_GFuruSXpvUeYLWUztn3TluOoFQfB087rQYpZ4X2VCULIwq9Y8wm4W6v-1TkvkOKYVLHBXx605vAPNQoD0ZXbjzBErtncUz7vYP0eC0lB33FxlIlk6jH9lolgbfHjrPSIh7sqtCMzZo1_NVPQdPPUjclS2z9INMub0VavuDh4YWWFzXIHIezgKInrozplJ0kUP9S1RgeDQLRs2i_G4V8WFUIS8l8r5s57n08oIb-fUJWCSwYyCN6fN9TdYZPkpUc78uHtYQcresXcYlMsBVp0DgUIopVaSQTkqHTZLb7We9TtyztLDdzg0SMCP2kdanA1T_EFcoXkk0_qw6c2hmCYf-Kifs4zvCSRm-QjCdwm7-0k2wtO8VYe-IA_0ZUHD_0rIZvWHXx4JJ-RT_YdM5QVFjLEsrySpC8Q-fU6FJKlkm0Ga_7tO4ecnHEa16hXjvOPRpuIGag9VLwTwzlU355qYmJx5a6RotNbVnCfUXMChrR5basKhVIrWqtfGJh1XZAHUVgrlxuQGf8q-T207Iwm0fYX9oSy9ChEXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKQYWo-I4tgpVjt-bXwqptUSWQ-TlFmr7TP5NhxYkIOdH4pQclYe0V6Exa5qWrLypIiP2SbtutYD0bnw4MBkWaHP_UkkDxNnSztvzXNNp9FTS1N3eZ59qhQ-qstf4LSt0NPFSpua9rxPePwq6yYfdnFB7jGeZoQuMuNWfumT-BIvseoN4lwz-SKA5v5IbZeCxuQffsT9zn7BY0xyARxjGQrbmOmBUUtmuXBFQ-tf7Hac-HH5whmwYyKjLENDqhJSKgLBnOTiUHXV8ilp8dCQ4dswcscagIt25mXalN3NQDDOf98kiijsZggxkl5k7vyxcyqgiv1eLvpYwSNuTbrw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiDo3UL7jErguoPyesiAHH6pTQpniQiolZ8JPEUAWe5F14fjY13eqbluHNFRsnceWppA5ylyszZLivZWYtbhCDUoGnliIzUDTIFdYg8_BDkeGqAcC8u7ZfRm_RPET2VIbLD5Lbmh4gl5HlkoHARUeztAMTkWrlew61nho6ka2otpuDLB760tL6eyrZ5Of5T8bWPucHkhYDq_W-Px8uwsVYo6VibJc0TYTzjKC7rn6zIJRX9p1kcQePS_kirGBdHbPVVDSIXiBDNd1ja49JrlVNYBLSD2pAqL6l5wSI1mKqDEr7EaHxxM_NN-aTc8t9Y51cQCL6pKeKUpujRggjB_eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqIOTOnlu4d0gSg_WOIe14yQltnj07Gsl__o3Sa5wV6AR1l9dAvj5O-GB8THQDKGN7Ns_Ps864dNllV0FgZE9mA0HW2Z-mYooczb3voP5Qd8DFgVBdgCwRyCn-IYWMvK-X5ZJ3c0W6U9mwT4BPpwz_rOg7V7kJmB45UbEXUzF4j9Yl3JPpaNkFwn_yPQ8jQgbyOEhFZZ67vNbcDIGr_1m_rnjfkPCUZaDyao3ps77LvGxeVw-3lSM8KyrUN1XkRX6s5epJ0HBvwsbVlUyjd6T_9lme-cozwlbeK_-sSrz-MgCHr7_WGwg44YuK7HwRS7XB3hLt3WA4NbWhxhwUnbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSsXRl8e5m0jC4b-BC-R9nJfgUFsoEishvQh12nDRgSBIkOUU2RaBFvMJcaGX0wsXigUYbczHOy-NoyrZZBkie-JecDf_hZMcPNutSYKYLVT59F4DikSs1i9zUsJjbiXDyaPXhWO8A0q0IbfkzOhOp-ir6RBKV32rbfSgJATv7QLaE2ZctxClu8K9g9iz-BSEi-gGr00olhjBlUw2GKRXFSAnONXOIWwB4NU9Jm90aKu0P2y19Rvo7ya3GGNURPofScEAk9uKnZb8NbjqphQun-lcCZW_XI6nWte1GgioOQP5mfYPghrnbdL5oNRLs_sfI_EmWMyxC2R_n4HpNSs9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SguM4ISimX8pt4UGzLIS1QYorT64J1Mc_sQHNtubFEkhD3ntqTkrEN0P0XvYU1SUwVv1TtehmDHpSbSX6nU_JN6BULJqsCGxysgw3H4ImXUQJ6vkn-c6nNjH-mcEfT99O8r22ae_fzs-MT8umX1gUjBIQKjyuF8gvSTB397Pyh4Xk0QDguJuodJB4Cy6dh4xpUx1S0fE4OBoEY-L4pe0vXJhc3zgJAUM4xB89Fh-8S7dDGGnjzkZCbbFX0VcWVayLvwE8v4qEqKFhEniYuj8gIITCgkvOZCR4Ji8ASvzi4Vi-sv3Qsnusw9FklSkW9_4ZzrfjlxeUiAfnEpbZBUBtQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RZtup-_TjOldtQdn_iCD0CLmInAhr-3b0kDztLcbO7INFhqSJrVul9GEwI1X-yJ5BPAo7TGzG3CE96jmNVTmLLGebI-IrmC1BdnihlYWKxi69UOt2hrsRPKwtK5bfZ2-OSMKwNOQoZtoeL09a7xIGGGVW4XVsxeQ36-AhOyfIEP3QW3AfrzsTdA3OMUBwOwZHudio1Q4LxeIMbhJmh4YpIlHic-YktVjboSvUmyVJl82qG9rpwSBNcPJ_TvuxafmEom9NCx3-dSP4nDlYMJayGhvPDfROQVeNU_a4aorVN_h-Rjyg-kwc-CFsvUWuDBplTRqpCY0Hq_eOiCKfn-wPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RZtup-_TjOldtQdn_iCD0CLmInAhr-3b0kDztLcbO7INFhqSJrVul9GEwI1X-yJ5BPAo7TGzG3CE96jmNVTmLLGebI-IrmC1BdnihlYWKxi69UOt2hrsRPKwtK5bfZ2-OSMKwNOQoZtoeL09a7xIGGGVW4XVsxeQ36-AhOyfIEP3QW3AfrzsTdA3OMUBwOwZHudio1Q4LxeIMbhJmh4YpIlHic-YktVjboSvUmyVJl82qG9rpwSBNcPJ_TvuxafmEom9NCx3-dSP4nDlYMJayGhvPDfROQVeNU_a4aorVN_h-Rjyg-kwc-CFsvUWuDBplTRqpCY0Hq_eOiCKfn-wPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN159RubCTT1WZpe4jIDKPPvI_EJpPyX8bIuWWvuP67eJCAZpuU_cvLVLbS3wt0wOZ6YkSS6OTVw7K_tQTQnPDG1J3NpsOHw-SQk-O-Usqu-vNyOmhgrs6Ps4X__wNsLGcMCggR2jehn03YciA_BR0AoLObLH3czVAB0r_xLEfkY-1Phmgvskjczy3m62UUpTB5ihCzWGbxoewlAn4oCs_46tAFpAU6g2C3mkUzZIJJGwVISpymwS8pGpoqgJK5yevmFIO3eENPbiVpEOV89q6vn-ureLunb5Scdyf-8T0ERqw9iivXlgCD2bdI_e539hfzJpvye7_RVj604i9onhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqinG64JoskIwXgglZL1-q2frFF9ODLFDG1uojijb0oUFxjlCXCeB5KhB7iXDtJq54PvAE9BmZb3ZR4Hv5RApJWrGTJOEU-AQD8NnqdiqvHOqgnpSQDvL2j349JyRCUSy-T95itmMonZLWbqtsDgtpOeK01d0yY2m9olrU8P-BXxmslMyoKI9B-RvFMHdJ6WvGZhtquMtQGK8S3R3HJu0qDE4LaC6vWVrXVkuQswFHqSpBOUtTWitjXFh-wFmEF25rTiS3LeNBUtlUO0-rVBGgGpcMmsi-mVLiWbHRfEIWEnQYjJnCKSMG-RGACHHNUEX8o0c2aV8nBIPlYGm5UmDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDFqCoT__jOUwue1OcoFCVx3WG5PBjmLalYIHQ8Nb1i-v2lMwAz3I4IfX1yDWw7CYh98BI2zQ2nhsCNFIuLPG01wfxmVWu3H1GkJD1jJfFA71evPjBPLGM7aSbPk_C69xDL-NjPXaK2VGv6dRQ2EVgbYFNaUIyRkS8PuIQ0Wqek_Ev4tzk3ZPv633jYEV27sA-AJJgN0z0HfydoRu_CMveyh5WWXx5TFy7akZnbFFA9Uy910MCQxN00URY93QVV1CRDIlMuQkbvK39TLxaQ5L283EuGAOr8JGDjcieOQonRx2Zqqa7_q4p7hozqsS1uki_xi19VCtear8S0ReElZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlgEBQ-xeT_wA21sWAJ74EUf-S1i8-nEQz9WT6qA0IWeM8LrsJGnJsPITcSJQYjM5S3WBY3urbprBtS1poFPT2TKVX5YH_FHcVKFWhg8Ckjt3tsUB16Y977RiOPlL2e_WrVKNKEuRjPJroAILngfXNmOlN4B0ASQSfn9CFTYo2OJTnftx7DxHPUne_k_u7eWPVz-prZ5zERlbl5WsML_5Wi82Ecjx-T3bTyX_iZU5IgGAvJKHouzgb62LtamzE8O0qCqULwMw68yO2WOwjP2a9mWlS32DYot0wy0RQrltv4qmN3qVRrGbZsvUOnit9Yn-m_dPkfHj7EjsdSaK9Fing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwP40mx4NmLwJewfjZdvTWxLIF-9_f8p5hAmilPTinRZMBe3ljRsPCbyqcmbEqpCDmMYmSSaDi2jbUC2kQz32CNENzmyFjtnCDAlv3OuQGKnrBgAmt5i4AUBZFYfN0LowltO_-p73YdfgHeJzD4EVm3AQTrC404LgiuWNZU7R74SMygFwCGFwkKuiDavxIr8zPymkeOij1-xmCJPl8ap6bpG904jiLzeUYPUJXwXAUEWBP3hdimYOTmONUEKLXo4h5YTEcIvAySisAlxxv5gF8hu1FbCuQtPymHg9YM_iJbgTzbQhLNUPriw5uPrvBuPcSSMOL9POgOHHW0Ii6K6fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFkBRDofaJ2WMTPsTQLvGelwpsycYrSHx0gqAKv-DRRQp2etrxzmhKaZVLolo0jPI3lLWtM2kDOzidSWE-jg8XmuP8bcxS9F0casqEhUFL6FeF-30HvG_oURzyZn-Ig3o5FLKIXsMoTBmiTF-PBx01KEVnbDKkJwF1V26X8rjjJGoX3gTFGwf7fKIZnMnqRBpJcKjhBru5IVvHLQE52TSu8o4BLKHjBA9zzlCkVPKvjUyvVcI7X2ki3e3EsUzZ7UBfvaq6gkJu1dthlaWhNWzfCSB_PL1I6Q7ualEJHY1QxRSA0YDJ9h4hvsOj9kjiVLz4WOhHzFclfbxV53uVZmJA.jpg" alt="photo" loading="lazy"/></div>
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
