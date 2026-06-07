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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
<hr>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=Isqp2irUY1giEzGdnt6uuq0MV4usbZwjE8d0Go6FUSrM8vdceR2cBNt2P9bZWFZGlan0yLkZiF4MHYaCTiSZjfj9Y171I3FpLKk62Qm_dzTGqjp39LyzfBDOud81R6dBiHCAj_xXHRnNwCv5qSDpM8bkTye0BPo3e6qTeEIZwpJnNPVuY9A40pursqPP1CrFGGZNg2600118A8l_VKaWuol9kJNqEWLT3WvDJv1J_7JxdnnmJm2IdntYp2568ZjegWkguQUzfnF0x84jfjKD-aXq6BQoYhZw48i6dh6unbHg2axDiVZGCtf0UAiSEBPyRFs4np5PDRBsgfjU9Kcv1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=Isqp2irUY1giEzGdnt6uuq0MV4usbZwjE8d0Go6FUSrM8vdceR2cBNt2P9bZWFZGlan0yLkZiF4MHYaCTiSZjfj9Y171I3FpLKk62Qm_dzTGqjp39LyzfBDOud81R6dBiHCAj_xXHRnNwCv5qSDpM8bkTye0BPo3e6qTeEIZwpJnNPVuY9A40pursqPP1CrFGGZNg2600118A8l_VKaWuol9kJNqEWLT3WvDJv1J_7JxdnnmJm2IdntYp2568ZjegWkguQUzfnF0x84jfjKD-aXq6BQoYhZw48i6dh6unbHg2axDiVZGCtf0UAiSEBPyRFs4np5PDRBsgfjU9Kcv1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 190 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 317 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRQWTjCHVfgpahpd1nfLR3fD2POR6WrsuEY4UtKgvuUUv9yp1RMCLuS9jQ5FKWnvw9Eq0l_yiU6EWj9Xab30ZQXuPykZ8u2CXMNN0b7c4VEfOzRQt88K--fcMmCvigyO36rrWKJxLhr4YDm4bjHsyQedNmqQ5qiA904ZUB7nKmAaBJCZJxX16cDznTr5UYQeICxUlUThhLH8H5vIJ1mfnFvx3u6lR1egJcpmQd7sniyX4KtrifP1-7r7ajpiGH3VvmWuOwAe1PywlBrFh14e0K1Rd8qwAhahf8yTyVEVYbtO-FKzriENgBDOhWC_Qo88MxI9r4WTV_LU-2tfLdLC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfN-uFQ0zE92Ub5oEgdLcJMV8gMRdZOjMN573-xyl1Q7n_MrH7IVlwYJ3yo11Q8aT1no6JbT2tQD2h6gUCbh3shffDgelT7dEQ_A83RlWAdsHsNCdifIK9IIleTUxZjJDOecAURGGIbzSE3XEqhUWpzXq1bdW81PbAwljhLxD8ZBnfSZSBK3DpSQJ8NDenyjyzdcZY-rrU4OXr3vEVhi-npv7Y_6wx_VH-sjEXmgsf2oFiIzqvbThuezRTk8qbUS2R01xJKmsw4EtAAA0sG0ryQtl70Ytz7pOFKHxU5vCbfBifPZG1iqw5CdY2V2nURsGjLgM6v7TvITVsecuKSK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Elnjd87oMXBYQ0OUqw-cW-6_hKPPQ0ULi0jnH6b18WPA-hl7KvVJODIwNE4B9x1hd3LExvWhJUVL052BTuyZXVFr9cBdf5WoqyH6cRu4goDJPsIeuyMvHpqawXsgYoT2JISpGXH0qgSAnNIJohuFDpGH4N7QalHdet4B9hFYuce9dVLV5xLJbxEaOceg2K1r3_R13mV93oT6VvnRrAirVreGcSIz-0g1kFNJDrJJZIcA-HtKZRQlZOHGUAJxJOfea3-7x4_pDT9JFkiylHpwNL6WkLTu-SgAbeGNEDCcqhWiddYDW6FZ2vmAFXQoafsjuWcF22dAswdwcOWtsSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 912 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 916 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1G5mdIOem7At--nyveHR6EJLTwV5bAl0ctUN5ZyRtyj0v889tlLI_ssUdxoAMyUC5X75xB89IQfMQP6_Epf1E2GaP7QlGuml6FQdSW8lL6IsXaPWCvsSytBenKfbpcrBB5xofHlEV3RfAfpnQnbax3hzbphj68khM_NGSGGEtEJvXmjExVVa3p4NchUw5tcpyDDgZBG2WUjXLL_PNVqol3ktFnTILycMlRd_hwwCpb-NRxeazEqrane3uCXOkOtQdBHPJ0GaydZ5rPLZEJhoTYaQ5yixS_nixtRW1C-xR4dnQWRjXSE_-iVR-_3cildG4vSrtlbj6AuR6hQAR7Nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJ34B5pj-U6jcTFHYQfC4CdiWXVgCRiI80bGpb6uFVIhrUOUQNMka2eqez1Xyvq8qNX6njWcWPc-LJR4DsdZNA7ZQAHyCqmlnKOl8zW7f-rJBFOqIIhBn0-3u-69D4WmIQtRX5FPw02BvK5zDR8ftFPmK1kThQumgiGW8BAzI-A6b-EQWqdHczAz_3dEgvZ923TRLgOROVYBggp-TKiEfuh0lyy9X2Yw_4pD6CFMp2C_0xA0BXP8feZJ7b2bI_8FnFX8M9SIVwAfvcDUdP92hJn9WAx52MNEtGJ9pmn1GMvcfV8pwcBy5j3ciSt-b7qbruDyKWc9xXCRyZSrik1tJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfvMYFk33ALLEwnD_Lgtsscd1EgqqjtRiDx3M7YYsQucvhcNy2y3XWgwFirNFJ15wqCgNvbiQWWNxgogXT6AKRlz-5xwdHTRyL6aPNtnK4qOgu_nKtQCh_k0L9bZWCEPZu_XjjPtkLPbCyh9VOaBdmdpyStej8bZa_IDwFZ2PsW6yxzhh7fv2eCn_gjwiWkdBW8DwLCVKKF6RNkkF1D-ztTBtiryz8Plc_2ilN2vrKGDY58qQKGCrjHiHxTbn4mKIwSOOUWU16WmAJGTBqO2WDM6RhyfbRM25s6llBPpQQS33uwoMLPw5mKORUroLngho2sMsGIs84jqIzoTsfHgVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7Bq2SdbGitgsc7-HhJrYfgcTb_yIY_SKLnmS_vFae5nw_7Ar6XbWzaViwU-Kyg2Yieojaka3PVGe-SImtNGn6Wl2F4v1zwGD3mFFWA9eeynJnm2NlVuYckA3FvXDkqccq1PuYR37lxxk9q9F5U9qAQfo2GSPsfYIFEuV7CVFL__FwkQKnBg4M15727R00222CxswBqtGQeg5_0vC-fkk412MRvQQDnSPL0XL9QQOQuUxGQRmhO9rMZNl7fyqv48XvG94-QXQlzaJSxhJ5yB4XfGlMiS4QZp6zUSTZ8DRDyqwM8aASdunM3vDScJWMwdQXF3SenbOD-KR2SxEm0qFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QILzpLODKSmGFHL7NM5wswZndTkK8KKSbPHd0zLVVVulM9CBr9HhmTioFBAHwMLq8IZG3rMSnywGmeBLAoFtg3OUn1WYt8BmgwZGYm0kV14zS4Ddrx-EmEKs2O1rcC8EFquazWDyUFTMb9VmMNVEnK0oOM55Ck55QjiV87FChTXJhr0Nx5Er7yiAvgwWPh8KUaSWcW_EDMHa0iq8ym4twL5sYD4e8PKOprUVNNGB69xAL4gvWC43D4koxJhpgioWARjfDQIiE5_Sw77_r3AAX7CjIGpuJjK1UZplnZIj9kVysPKVjjKTP7ni94_kxh_KQDF4BkfMwRQiUqkJn6z9yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URZaYPWadFNYSly2HtTWxBshtK-1wv1QF6xQxkO3PPqUdyEcSDzalBI4JiO4-OOPyUaMW3drCwY_rQrBCgXrZZuNqaF0IB__cAamsjUPelwfs-5csF5JSXujJNwRdl_fqW78LfwLYV0voXYPw3XJP689x-SM5DKPg7iEr7lgb_2yfCEscpphilJNkPA46tWcsCaNpxER75byFSTEgM-z-twMHlzL97-gqn08Noz3EdmPl1WX7mPA9ILs2Ry9sPDYiZlg4jag8aHQEc-rA12i00oNzoDKp2ffxywRDVSmsXXMiDHNfnKEbAXaZdEphqCru6yfBAZBq81mhnjmX1OAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kB4iXQHX2Gd93chqgemcR5lRqJh3rOPuzn_-xgszrTQdREQCCA1zMgh-u_uGcXz6DxAxFUDKT2NnsNCrEP9vvaLT5LyGIcdwXBs1olOdimrLUCxSt2d4SaVTL-496_w_LGYWSbKVINktZNqUz8PQ-N8kuhQCB-NLsxp8yeLDL2yGe29sqXINswpzTVo3G16X_BhQBj_9L_THsZ0eKXCwTdYa5M0PYiI7-2ftI2d7mjXUTySuPU1xPOzU_px2m0QCV5SaQC9Fai0enKzmX5utgUb_GkibcF-nizQmAY4eUbKNbZSL36NGEnNxoZdNEPpVmLJxg7BB0uXee26DAnGP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sypdsii3EI4Legdv2yG3ephtcFZUWllfwAN1b87PRi_bZlBu3_s3a7xIlRZ45nK-qXJ4TE3ioY61bO1HkziZf3sfPEHY4Xkwj7F_GQMS5XdcwFvFHbRdHzRVnh6xbuE_VVFgtwQVWEvLcipATKvwyK47FEmIOLX8cERAQHEZBV9lOOmdLfpG3a7q0tTWFew8CZqQn6_flYdkJLYbI1B-XDfWU3dpCGn5aZYfPs_sFDCqM3JVdMtQRsexh9PVjH-vbRD4K_-0AvZYRPcTFGkTxPyj1WL-iaAvwwZZNTfr7tgfFQpzOZt45gX9ox5XLZ0kQ4FRqAXa2VpWhn4wG7zASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDVEpN0sODwE0FfV4QlebZeZCjfTPmn8Fut30j91dV9Iuh6QRawJ-o6LC9NbPLDjTruwYi9M5zXzRMm4hQyvLO_9Q3nrMKUs-pIYLLwuOffJV4yAaGYU6bp7aFEbpoA9K4664D4EScYJwUgEfObziauEEjyBcTFjLndCw_uVkYcG4_CBYHf3iOXw_XjUF3iOq1zKqOzu8O7PcJiNdg7g_XGy8u-wmvHjQ0-IylhW_z69R67RP_aEeJpw8L582IfeS63N0aRoDn4x08hyVlutqw77VtboCZNJD7RqeW8dxJwrJ1qSn-rOK80FrFFGh13kbRFEJNCbsrdeZyr6_KTQvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g60H6x6xdMGdYJbBaqZrY68NM-8oCzxZulikC8_MiPP43srMuyhVp3ML5HigKy2Jr8OSUzD5zJYodQEzxa5Wswb4FqyYxrmjWXT9-yZaKuIxpfHSlshiEE7BGJPI7L3QO-AhSwqLuo2wQESilx6Y1nT_iz0SGncoy3fvUzUSfE9VQigM7j_kdxdXxmQtw4jSzXksY8BQX4kP0fYeYovDt07ANJOFVm63rhlAYzpC59Tau9DEdC9z-LdDY3rTW0auSejkt7ZJD8A-zg83vV4kLbCyu_PSApkcApZqcJZlMEDW-OxzpIFx3h7I7Di7lfuteVFI-zQ8AxrGLEllZV7-sw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=dWf1ET3YN5iC3THTFQgY0DXLlpxxAnRltEA_c4TDKB1x5qrdKC-tkGDgUZRwrDrCuBRfy0Wd7PtnpweuDywTbwG3YLVLgpdMeVUb5G9fkttNMb7NWUh2-zTGX8ngHRJFXlpkQTyQAe6lOwvqkJ10DrdATYONQdHY_AeYnd998r7ViZHaZpbXR3rsq3XG4p9g8VrezM66ZRtGRe6SIQbQ0VM5MAZPJdZ1XOPPKg77swQo70AdokLqVN4y0EcixJvAxhn-ppSbCToI7gOTVEAzKdP6URcWrvmTBMblV5z2qPnTwlGxb6VLiCrvAY6ztE-0OBSMeP8IOwfVFDzeiNA5aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=dWf1ET3YN5iC3THTFQgY0DXLlpxxAnRltEA_c4TDKB1x5qrdKC-tkGDgUZRwrDrCuBRfy0Wd7PtnpweuDywTbwG3YLVLgpdMeVUb5G9fkttNMb7NWUh2-zTGX8ngHRJFXlpkQTyQAe6lOwvqkJ10DrdATYONQdHY_AeYnd998r7ViZHaZpbXR3rsq3XG4p9g8VrezM66ZRtGRe6SIQbQ0VM5MAZPJdZ1XOPPKg77swQo70AdokLqVN4y0EcixJvAxhn-ppSbCToI7gOTVEAzKdP6URcWrvmTBMblV5z2qPnTwlGxb6VLiCrvAY6ztE-0OBSMeP8IOwfVFDzeiNA5aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFUQXqFGkwgxv8Zeh8U35y-XNsf6Z8DQGCCvrovF33XJChNafvQcXS31Pkob7-VDtTGAbU1kvCpicbh-Q2K3jIauHJbcdlLopjSFojhBN45iz2t99THgkpXF-TD2as2B15_Tig_SZD3tQsodqgcV96tDnrcvdNzVs63B-zrkSffh_pAIsnnYgcf7NU69D7xQwpPh2J0P0snZn5_N6VDbkzePt27u6cgfgVS4-102vvCTh8zoK_r4e0qyiesyzIUXJPQ9jadiKbwZ_zRV7PiszdhFrxartWf02it8TqS_Y7Bu2pBWCA7yeV3vFReh9FI1XhSB8jDhfZtSdFjBcjA9iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZP5OCLvHj-VoEkP1qjg03brgWUGMQ6-kxZk-wfuaH6roTdErW0v9_7UKdttFfYzauuJgEuxu0hI-UOoVgOPjTw3OMkYwdIAypp_ZN_wNFsgQXHCQfgpFSatiI0o3DDimdoOyjM7hbzmDnY1_Q4GKtpV_obL74ZZvfgJ3d0OeoA0Q_8LhvTXAV894C6L3UKdt-5yTKQzLcgQAF2SZmS8dkPq1WgHSB6T-ckSObQdxf4FLn79DpXCkJrXZyYczBVCLMhpckiqWc21O-4Qwb6nHP67Q6vuttXDLraT57j-Wh7tVXLw038VoXOZftBdbT39-AfudKqngAS6eMtJcN9Lf8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYQiDCXXovBUl8XQGHBi5_2FUXTCDG3J69H3T7-E2GcMXRSuunK0i6JHuEAihtsXb9xyYrxak41HWFVXZcsQoHl6rI9BsilGQUdkveQzDQ5G1PsKM2x_dE-77wsQU8O3Fr05R82BhadbWKRV-uOQdH2ymA4Mn_k2IPYXDh-Vv-rUEoJmzi-76QRWLizngZuzbK_QyP3FGzaerK-XBl2E1zVudWTiZkQ99ccEPWCmZoMBp2po1znKyCnciD1X9CyPQPRiZxKqpqquU6trfFpt7RgEcg7EWmx_-7qR7C_jbkwPSPgxAqFgNP3uZiE5e7KdnZlwC7mcTrxv7vC5NWiMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-GjdIDfgmAkH7kAqLxdE9kO5vs1o7iKMRASdYnBN_k-KXOv0ONtBwofPROMUNy4RIoLhu7t0mpRB60s2XsUlvWoHFQe6m0Tmui48gvtjyqhX-NW6S2f1hKKy46XNdoGITVuOckCVtYfqXLNBHoHsdTYy6WDvsPWjjXBeVbvLMOjCcfYqx5_ZKaHotsPa00FRgYbXo7Qd9cfzqPRHHTnLcbfyRw57BQfckWjRLMoZnqgNCDwwoCPUI_DmJm4j0iRNcI1zgCeh7s8WKIIt0ybB_XCHFWj4iQ59kEbiKhOGhUyqAFxZmvvoqlqfSdZn7noIhiQ4SgA8K-57rN83uDtjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocEIDGdVJLzw4Xn0_Z-qTh-Exh2KUChNpOJAbFbbwOjHzkRihF4ImXQCpQeXO9TGn9UWkXyA8nnaJNmbuUMyKctEoRRITuOBCq2K2onXTHK3ckWRQqhsYWvmQF16jaM-q_ISm6QtkdhKUMs_dijE90Ok_nPxhKmOGQeKD_S3MRz-gVlAbKFoOwfNsmZ-Shvq4fd1_fnXSwQsEa9cy3jjaHGcmmfmlmmzxxZQ8h9d-mZ0maCZv8arCxgK7isrVbG6BNUd-2XUhV5c9SNKkJLEdy4ZCjcq6nxIh9_Dx0RZH3X0FQ1mP_2m12Nh1OmKamROfEFlYPFy-u_uGBORs2uGPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPbJ6B02xDKfzwtOtajn55L4KYvy_B73orzy-n1FtmNYN3DyurBB9U3C409PSUDLwQzl7djEWp6uYYVB0Rk6QKstWi_NXVr3XlslaFvF7Zg9Uvv_8-LglygFZTUjHAmFLt9ezAL-6AK6V5QoKyp0SVa6ra_5WQ2EeYBShwO2kH1llhJ9lHNeUgP5n9nf1NnfFAAbUqcuBwgJnvT8He6jsFivs6w4WANR_FYjHlheLQpAa-al6_fLCS2t5dWiwt1Eg4YrQ85CBfSR2zQNnhUeff-YWSo1--jGO-sAovawK8ASXpWoBt57gnOkMXCzOz42BYGHE2frUuNOJ24PsfkiEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRLe-6bOyOOs2CT3pW1xZIzrzroF-UemPQrpyXXcpFM0IY_jNn3RwrjyAbodUspYf3_U-fMv2tzigo9T6tWKqPQ2Vq1UlHVJ5uv-LBUxBj965C3P8rO5_da--y91d9aqkkOBGExDLLRQ3rGa8gP7Vwoja4UM6o6jZx14hnfXc6xtw0FZWbU1EcC6yge4EbdsJC2bwQksH34D9fTVLl_48AADD-ugU2dTXnyD7VSlh5UQj0DopdNRrNeSUhsQkX4HNaKGAC765q80BWOr3B64zE4UR4VFc-E3SNGYZXwE4_44IdL9QOiSIuNpD0WAuSzyBhOxNn3S-OQYZYnU5RM0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRBY1-UuXRSFeSWX4npeCXvEe2zyhY0wWRE0xHr4J7HmuXkhbV73w4lgwklIM72vtV9UWrh82DXjUWIcFZNmwOeMVxCnCazMibfAy_prkiyV6oWGIXtVtpvx82hcQH1tz8OWotItGI36_eerL8IpX3nZB4R7BFREyICQ7cSC66sHaEcsvYibxiLO9j3bi7XjRtNSOZM-btUcgn7vkQFxut1PRxBUU0U5kL61XW73GkZJC96CSJBghSesliQZMTwcRIwv42JMRcMm1oSQ8uFzWzKMpgPPhpsky3yGSpW6ov14Kc13RMICZTdJqzJsz1TGamX1OFBiKU6gs4mmR76jsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry0FiQZ-UIjwQQRsANYFiNna2rvhb3275_iHtiOFJT1Bqm7GvYCtSntM6gGkusA_KL4pRpJCeGcZmc9t8MEAFLSyQ6wXvX6AQIyjfv1FDlNSOg55DcBUzhdYa7kviZ1eoTWqAKOipZWl-rAnrx5SHgCE6QPzhpTm3pmwcezvMb3I1hUyUccC5wZilhD4OF7Uzy2LqYVs2GWSgCm7emEzwjhTtvJ0anonvvFogRe1SDno9Cylo75lJ4uBgZvIdyQ1lZ-1JNJCgd8izxCeAmnq1Bd43jECIYzau8D0Q0ynzlr0KwLL3t5yYpTHPcDgS4XzshLs9mcASw49ADLhJLm8wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SluGV3YqCp3j_WngCLa3P4ONQT-WwBIgD2JFfUms0U8XwnoGsk03jTWOMwJuucGcqd8Q8s6NaYIVfLjZBVgOyjHSY3oYPD32uF85VAvPAU6cWdvSB4Nhv0WQlD2Mj6GfZAspEcSdO-Ket92dACabgGJE1nZ_ERq1OuyPme8q0EfEsPM3yUBvO2CAxKRrEXwT-Z9mcol1gvVvZ9KPnMahf3UWxGdlGiHoKFozGPX_0xo1JvkVCGO5DR7rnz8v8T9c1W7CXM5gMWvLPDxy9SFqzJJvF-WyYQkSVrKE94_heCtz0hsRmXi37gC5msusRf9fGUcOJ2_uJ75SslXc1ibiqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7npLp0Y8RaE7yarqEwm5GnnHxat_Cmd8lnv2pd9rC3vOVbZKPl8y50cRCpCgsPm3mAdV5GTLPJ9bYyxajzjCi3oso1eb_Xd-YOYZ1nGhXt9RrqvIyr_UjhCpw38RnGlJnMqY2waigYi3p1YmB4hUhGYeqCx9Y1BgzlUd5qch70FK5BHQ_GVNbut9pD2XKNdn4vBa62w3HHaftkWguQAQIWeCpNnKJ3TX9mMnks2MgowQe533npv4T-v7zsot-Nps7Lsxckf2cUfqxP2gL8OD0taxgxXdV3kNAnP9xYSyRoua1fyExpDoSroWMAfL1azent5sIFmsYAmxjnT-AEgrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMtW6Dd_4P5JlxdJf7rcG8fJVzXdiqPVvT2cwkPgOgvuXiLKGVaAitrQNTbBqyKQfyAP6hOWU3_Wcp0m6kHt6EP8ksy1K4NX1ICsk8o8FNcviJLc9pZw-6jCuU_6yuIM36RiAuaIJOddTsGWz6n7ucmv9vBDWQ5-waPZtz99V6348bDd5hY4ytnrbty31zEG67YArnW8343BipoS0QPhEUVjFnwVRqlYFNzBtlkiYO2Td9ViLQkBdo2zmF0kokwB7ePxWnFZdfITbwa5YrI4aN-PgMBmDFd1ydT8rYJimhNFIMCZJR3jJDwOO9XJCOJFoQezTaBzh2e1BqOiwIRqog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqWpUzQQnQfkcqz6521NXaynFrpQDNIHyILgIY7CjOugeZ8QnKYLcqr45_DMzn8B0jmAKiyUTiPlDs60vwzRhmyDM7qADSmTaDsCpTwU65HVPm01VyqRijOJDFOd4722o7CeZ8WU-1YFONa9ltDWYBU8gs-97eP1VDcEUZVTC9ndDw_LkAb4CCH_WqDDX8lca76F8EAyAvBs3TghrQ4MalM2xNdtKF_mxT1NrPsZQnUdSRDTYHwVYO-hhqOKNtbaX5LN1MG9wyctSS-D66sXYdJ5iCeuCOuszYrk19ASc9sAsktOR-IWOHN93RkrbvwShc5Ic2xTbjOVhPIk4hF9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQp2eLMZtsmFGY6b3Sw-YQ61ZxIPHA6SibJjAciBUzAVmj9g0XPO29I2bpFT5UaZhYN8RKbv--2m8EJg_JMZ96m22wwefzRr3RiDFT_LDO2XbaiIxAOA2nMB4v2e1xOumKYPPGzryiB6YCjTRO4PlShZB9FW3XpQuCRFmvThnZ7354GSeBy01XXcuBrsdgvKttpGVhbscUP8xT_P9R5IKKTJ2jzJQpkysZqowT4nQ7J2Q2ZO8KYRKDJq8gfFsQRDHOXnSXqsJgz6evYSlOkTyabSeLlnlCKr17rz7v6IbaLW28YurPR3c1t4vZggaVzQ7LmuOdh2VkCYQWSSpiFriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVtKU7bzVvg3gi0fNeVyxmRD47s1l2-yAATDSAT4TqOxkQp-hvFplt7TOQDnAwnnvSIub0gTDhR9ABonCdJv7hPni_d_L_mD-adK4Vm0jFCaNAF7IagF73hwqluePgnrgcw_VY1ATgbY7z2xmnCqSmF6L1voYmh8BypFLGByp3k-yEnuf_ck3iYlYTZ219PM9QoFKzulTQ24InCniNVH8O5VqrKC7Wi_FC4SA6PYX0gmVucBzrZL-LyvaDx8gHqbwlocmiLTF8LM4GsqX1k641q5G5pta1LTu-M3DuHQapa1G2edSESJ6Dmwa5JvTmzoEb5Bk2hoYtfn13oPa699Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzjgTKxdfRgGSclCjo7N9944eR-2Jl5QtHEkY1J-VBp1r0qHZtOM29GKjJONsan_aupTS1Kx5JYpLIcbD2bDcCjB7UCYz2B4kp9_OrecxLpps5_IxDynsXyvzgEbbgt-bPsNOXMstrXDPBE337voArvU_ZOCHZNPFmkjccGu_e7d7l5AdP6TmYHDQVj_mj8zpvMUh7QFB2eT6fjEEazriLE_BKM339LtOtlCOw4YTI010atjKNeIUa5o51qpxs_DmGUM6nhhU4Hh48753gK2yJXAFjfTk6m902vHjppWWSOCZRbG4J76oIYfmKVlET0u1T7zFFIPEKCZ7kzmhDHwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lp-jg5nxgRw6OEevxv7fD_W8YpUjrnaw1r243mixOtvQ5_cujNxkhetFGnAQIBGrhrTL6SpIoc5f47F9HHEMKGzcDPho74wswORk9j-jw52NSqSReFOBI0RsVBzZoJ7dN66PuVQAagRigpiBaVJqNuPuP_GUw7mdbdE8OJgrEvp8mycUz3f-1WlG-IqA-FtoNGBwTbjqUAxZZGN-qAeRg_tfMNEFYum9OWusVO-iOlEKaVoiKElgETlsro47JxUdCU4whspMG86isecWigmNYfbMG1lU5RMsfoAQQh1UTCKGKwUJ2N8qRoN9m2IB8R3o8S1Sv95tD5_hldat_JmrHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMiCf2WImmkSOK8AiPLvchNPhUZ9yrdmv9oJ5WlMofRsiSE-lSEl0nUgCwSdt50Ojo6B4SPB6m8OuoIEKFwUjeaCJdYZfxgBWCN741OGaRnyfMLBcgdbgVujDEKxZOzDgRupCw470WDC4DJ2p-he-Sd-5vqE6XB3QvU1TEw8Vzt0vHpz1m-00as08mcI12OWh7OESwt2fyG4_7P4YJFs0aUuOg-z6rXqw1RCbbv6G0MWsCeMgVngY73RyYwgUV06aox8dGrXxZbcl5xLj6cFfLBI1FoRdM6pe2Qs14ZZmz2_mLx8YwsqAXzlLJ5TbJOFDgq4qK6zsCrhAkNuBHskoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvNGWSp4p0WlFnKmYH0kTyYczYhyyDH-oM3R_ed7bqfS4KykDA7XVVEugElPctTkDeTBFsrfRCdIt-qNuP-JfjCzTuMqVNTL68-LbA5fsqaZECv7SAP9aZ5JPGjzTx1pPU5B4X5zZqBRYH-QIsnb5GisLBDFliT0znyPVh5V4b_nNIK6XgwOCh3z2Nx00h6XJJHkOqsYfK6epOP6ApBZMMI6XJ0fQbUCPpOZyUHMDXaC-tqkLlTe1Td9vVrv6v-g8l6QKwmUYMYG7KuYIaRYY_VeY6D2qMINrld2_MenM33gxsZ-r0l8wT1FFEFraBEVJG5_n4TKDV6_fz1iuoCM3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV3d-tBgPabZqcWIfPjwiN11RUhZYm4kd5c1PICkT1S3KnzCdYQ21Ea4ybr4QyTXu11hwhED9eBfGv31fTVGCZSv5MY9dLatySp5zVq2mu8-YS2lrvWJQOKbef1qPfooND4jwmZcAG660SJ-y_7gR8UFCMtgsfUmEUBTuXbaINwKxXFsPvx7laFCyJF24wceH4OsbLSNdZGtN_Edaw6e3dQzDloCb_r0wmNqL9qyvGq4w-6szsF80vxzwlUKA_7uD6IOPvuZxErjcpLH-spxTMxNAb6D_Z9NaSGxHWCAilUgbvdbXGfMUYPMY65GkLPmm0g_WNs9QGzYt0awlOFIZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axb4Cfng11ULMjMcVwFOO_vmpBNsqKycs_DjM7TaUwSGoWd5mAn0VIsWnNhqM-BoJEY8_feskNieTxkS-CYGDOB6_ZAL3du2qYqik8f-MR4QjPgh8bC2nDZ1ZgtfYVDpTpPz4p44CgFt4Q1msorvSJ-5GZx74gdFOHOOMKuXso72k9S_j4xO6V3u9yq-Lha2bvKbmHWB6SHqu4tBqYypSPVxNXbY1V6Qz7kjFwXueHvewyKWX_ovf0QdUx6tFey-2eSC8AXPkeY4uJdguvaqICGE38k9-z6jNNEBFaPASXBbBTLM6rzgaH-8FrSmXjtyesKHRX4-2raV-Sq7OyjqWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAxnltg4ZaK5aIdR0DxYw419wv_nTAyYLIry7ixLMMSVyMcRdhXQsTKJdpnsmv-9UxauPDHvtAJJ0cIOLYBilAtVGjqEyoQIlqNhVOT5d-M71MXdrOiYiQjD32vEccWwPnz8CUMY2A7U2QwNnzVkg5dzVU-xqXZ13SPs-B00T50HXGkBy0BdXheMqUh2w5qLZUvDJT3Lb9xKCGv1-u7LpgUvxrs9aTK6zxKku5rEQ70GnYqhTHfDxSMqVr47F9MBqBilL_hvXOYLX1u_ZAm2udmcBbw9v4I1mIK4eWTXJf7q3dsNkP58FwyeKqaeQpfAtgj1RC7Z4eJ-1oUKgqkFLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPCfeVW4boGrjSNTaF6sr83HvN7iCNjfxe3V1keT07IxCDenv2aUKHk5XUysnA-mRJkYTDMHjr8lHj7ltCbhhPXCTq5fy6--Nqr9WCVbt2tnrJSEUnI9g4iYS37ikSgBH44qHdzoXjLwON4Prly923QLwK-u_FHZz4_4Va_8SdPRTzG9Ul3gNRqIrnIUw8htNP03mCljOH_XQDlMBq2zsxu2-HVqUHeOKc84j5aFRDlnR7WAuZROunmqIX_zOh8WgON16qqsahhwyLUniQZMTgiPBZUEbHyD5Uoyiu4c0T83WnqyFPtZ9cXfsWIoB8kRwIz9Y5qudua1y1Dby3K9mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWChGVXJstjJNN0DC63fvsB3KX9aGqKJtGluQWz2xurvN_659jLIUdxsLov0Q90pmpywwRfWm0U3xvSJFXZO0FsDLzQEPUlF5-26jfHOdXg5Mo4qdyi8PPGdwRw9dtvsY6x7xPL6frtQJMLWcZxlDfZyGe7Zsdw1HhoxZok_Vlu0n8XRU_mqgwWBEtK7RUG2F9DFwurjRBuu8xXVNBbbFjV9Oy77lKEjEa-tLsIZuiOIyL60a9iJKgxCC-A3p3VkSFWWnVwF1r7Qts7qG8WgJNoNhM0wEO2VYOTwfjaozfopI_RDuW4IEP1GrIyDHWZ_pVleoF8OjA7fGwC-ASbxhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHGzlCh7eQ9xh8WlCBDFMGhqmbMiMxfWZ4tUkM7WCDFdosJqbnU5cIRtMq7MJeKOoBXkc74qMVI4YUSP65JIh-0sqEzHiaA6fRJhGDsyONFICrdMwRvZdTi1VFH76mXABBFy1j0nZkDM-bQi6G9PCX9lKtmnU1_bfHkB8vmPHV-VcEse9wrNLWJsQ0zOC5_9uvC630YYPORJaY_nN7raEks21o_AyesgVFXw68eLicaL5bklQL3oU19Mxm-aDGcplOW5NWGru_KaWDW4cioNiRvZR6vubY4W0VbaaZ4cclgNVDHN3DINTnhsJv30ATegHyAzGUJHyhkM9RMRwFIakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvg71uo21d097_2mHiVDiDXIvnq_0V4-7yKgsgOLrNrStS_HjZTzwyUBDV-Qtgm6O6AAxi7AteRILxHybk-NJVgYMu1MYO2ayL9y8QnU4lMn1RlBm5SPSydUkne_bcHFmmfhgxzdpixHjGjEhZW1xz8CNrNyjp0fVGPWCVK1vUrX5zrrTKbpDz3YKveQR9HKczqX_0cr9T2SlQBRbf1LN0Dyr-WLW4_96Cc26AYX6UllYv3HA0vij7Rp4Pd42SoMaRNWMT1UDZL61D9FbPqUaOircMNSISMy8DCxaARfRzeFs0Vbw2ms5f0ot9QYMFSyRdARmD8Ynskl-9xsPJYulw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLkigA9tuZj3f7fhvsDnsm9tjpdt2c-VK7rZVrhcU1IhwBhp6NrNaz-q5HOma8HjtLCyDFrKTILthi5kYdFvT49UV5VfYi2Ep3WbRY8VHH9d-TG8OdhFHIgJGn6rjyfJnvl9tJnDWtfUeflQNO9ZB2LKEP0pLufDkxjYnYfvfteycgoJQBrca_l4UVgIc2Y6h9ljcs2uIr5HZrXYCqTgzhU7QptdbolsALnMSD8OtPC1WHAHbGXFQ-01wGpCp_ReK--yxuuGxBK5jUF6Qt4CczAd55a9j0b0nMkwMJmIxiLL7bmyPMUIUGSsabggSHE76rxl-mhwiNHt__wTp40pbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJMNs7asGqc8j9s20MESs_LGnk8zN3e8VCDR05uAI6aMT2N0fmChAcJBSY1banCbnE6ANze7vDodthMnN7460WxF4bX_8W90I-C8R-dpZP_uvDgPUyD0e6sUulx2oNkedJJJ7f-5ZLmj9sjONnYCiKWFFbmOoZ5Q8mVhRqlQUZynuq8r9bJvQYBbxgVjFcQCpBaylva7-S1inPdd-1qkVDfCrWdBayokwRk9B784XVN11dmUaFjNMKw7GLFhEPO2lrpPl8wOxndy_4XcWJOCwmmkkBUo4omGY6lm5J1mPunD0xRUl9SXndl1OuCxsshdxpAs9dLTjJ7sEAe_VWz8Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh3qD7LOQGk2X3RboBrfdCZRVePyl_v9OYmoIei2rtoLF5-c1RnWgOidlY4FHCgW_cOdXdbuaKBKyabYtHvsOGHzFUHpzG6CnlVwPEGHN3nzrcufDgAjTOZw1mXL_kjs4jXEKCZi8B5pGPVYvC6PCYNHbLG0gkdjuanOuffT6fpKlCT7jBx_U4c4EqFXO3gDK76XLDfGGj-F7NUAYzhF675uuLhacyY6oEKHgn9gR0TlLW3n2TbQlIWdd5VM3ilwDyu9df78zefzf6yvgwyi4Dk79NK_ZJfiLQEFygHVJSJcWGnTRXunNtgy8ppCXfUexPEDI45xdzDBWT0TJLf8kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1POlyZesHo1VgUAAG1Tqwi6gA-S2Bc7UOTGJgAjy7NHy4mQex7iUlNcZG8HqbcLBvEXQNP4m22wy4zoMzUuoZzANSyKsp_mghQQOQT4O1rQqsMGqYzY-9BTNF_MSWYjCjYRKPoWF9USMX2IAk_waxJ_NtjUwk3hF8ZxRym1rvMc0kW9Nv_raKRZXOAUS-yuTPythLtnjNHrvNPB2d-xPADlO7lI1QI2wyMRbeW-eh1ghN2hEv2F8cYJ_qAF-nUFpmFRyDZjLUHQeAOG77XqRbeCWNkQr-2sP5TuPNUe7hTHn8dOn1q7DUZNBBGCxUYNtfkGyfnzsB94_Z0oarT-FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7q3G_JRiXekqjfVZY4Y7wfT95tb38pIgSpRzxpsG1-uFw8PdEokNjvTb_5pQEQB4JF67OBGgiDfmJ4VvR0Xbf93eGrmjXYqeiBAOFe8kvyatCQ3XYvDaghOHXmauq4NnLlBiq4Lsi97KngwfqeQU_RQo5S3l8BYnEMypo75TSgblTSkvxtDpwfrsEcZtYmMAz8A7dGYm5OJKPifSV_vmSsOd8NSn62_vgeyCUagXMW_4zsAEmPJ6WrT7ylGLhRgoPD5R_iwHHl1LcvSd7qRnVMV8Uq_Zn-xkiGZV7rZ1CA8t6NTdwTziOUfO58mKSa2HtpvYrx8nlJfBQHb1odZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wf44VWQtMMXtOlQO_4ZfndKaNlCupBD_dPZDJHKWDSB86mdK40J3MGJpy9mwtYXfD9mEzOYoWkLx0GX1_Nw4JVvpaNLmXTMWYtDiX98xGRsCvILxfubbmm1L67wUzdsOcnGi7EDXjWIYg-KDN70P5HUvVDtYlZjPmdwDzBNn1VHkaDCQKqTNMhjM4P2Ar-4tfYBeyVsJcy67K435B8o0ls7Am9dfp9L85Ldb1DkQghkUY8T0-0zFulY01wvg_2hutHf4B3ug1D6jY-dLZJW6aObQYuUxozrnES9GJL8BYHRdmOGh1_9o7JaHR1HGaxxiv4ofbw85W7Xmq-6ZEvKnAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKE3atMddRp1nLRTmmNZEiJNXlnpvxrrbUd_kiQoQMmSdruts1k4jjej7346FiWMd5omuASTnGyXL1vamki5SjLEb6BWWez7HuIE8pcw6J5pGS8WHNXa_xP5CyMPZB_Tea57dwtBXEFjZXWrgIGJt44HgEyHNd1rmvANSJe6IEDEtCQ2zhzQZVgrZkQxLSrOoyKKh0aR23fNT_qN7DsMoiE772DI4gfnNdNbaPOpX4Hh3zuCgM-4SX8REOF0kzoWg32xz-zd5d1Rhn5jf8oYHAB1yz2LL6koJwgxGsu4jpfVG-tUDQ18bbuz-xMQbrKTHetKZmRATVC2LGGWljRFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge4WXyJ2SSHhkxCg0Tb9p4C3yTzApZ50CgQ0c2JhyzwRTE3R04d_6SOJYXb5rGEqF0E6qIf8UAQDnjev0o5nSr2R21PwBE2TQDJs5fJGr8opwOyPdYr8SptWjQhkKUUWzGLaS7TzJs-5NYmTzUimM1mGq1OLKWoMj80k5G6utzu_RkYhcUSWgZdeuwM6EsKeImncJaImMSb5i8VipqA1piOQGaGtb1nv0C83ICgcFrBr4afaUzS9mr6RH-9klMCBtbLQbYKJW1g3sQwZmYYf8rcCEB48skHv30mTrVi05aY9L-_kGOZ8QlO76ls_upHTzHqo69pchwatJJzbdKTw5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWH07QDWJaUKoHA4CULAosNqiG_UybxDc2lREiJHRQiwGgNOMGUPr-Ne5f4JAXL_peVwexhy0vtpPBBiMI8MVj61LLSQOy7rvpgEUj0CEanMqT0yxHUlPH5ieejM5aVk2bT-nkXiGlM1ZmqWg9bFO8Mhacd5Aht8lQBglkPt-ZmrJcRHIH3GlCvYKH3kb6ynEjsxsbepXhDjw1XMmIPYDhIdjAFPJxGvr0-xDW-apn9GQS-doUZyXDRdDydz_7k2Jw-pvjuGNEwVZZbvc-4W9sb4vVubJ4RoVP5JXNuY33w4F642xDHiODx48U3_1zUPwEVABr5vWD3LT_mqoIh2lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voDa_HhDMGlMloPd66LGDqQzQJPZo6d0xGGWqP2l_g9LDO1fDNUZKUAWfJpdF1BhhPxhSQ3YVsqvexiEm-jUYvb5GinXkSre_tdTKyjwsA1YO3mI9Z8WGA39piUljh1o6YFzK2IU_IR22TE2gv7cRcn3hKZJfJIeLTuX6CI3FjvgoABzCUvA6DKXYqwWzruML0ZZLMfsV7LqbrSzU9pakhewtkg3hIjMzki5CvCLrx-Zic-hFNn1rip2gjHnhxFIdMqqja_s3rBgxnJIcwTjJgGEhZ2TZKjhgdP4JDDndNwa8ZGBPXIoz6juOV4X7hRxeWlXSnSHaptiNsS2xcoaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaoldCe51bUdfbr36nesaWjR0bOlYrMbVToEN7Co3lPTgdqKOjWDqe3KTXAWzLGSWmPrfU_PKEMG4gcH0tnUUZWZJLjsVnGZDwKAKLU_xjPR9E2uckF0HorE93IKClCAfh4z7qhp8kEBtLmglwCo8S1vwTifaEfw2dBjceSmYS_Su-QLOiO4diW3X538mAGaPNsjVI949vaVtSYDsNb0_ZIvy2gbaEjwhDkPiIjTSQNVxlypE4porEH_HwFId2azfdHQ9dNOPjKU4ccSWWwc-2hZoxSPGWIjQOafFO_HqgFk2BC-1Kmq8mFCJxXxMxJbH_8QeJ6-8P4YWqtzA_2uwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfGfDZfsVJb2ey3A_DoNjEzGG7NBO2IfLU_UfiP7lpXErqulBkyvqi4UMqwPfuNYwLz1LZ7D5ubLwAe6NWK_VFmgDGYyt5cfa8KIK-SJWJQH_0ejjsN46seNaSDOtxt9Zr3EZNPpMx5SsZH67bXvulOQAD6L6rYh8O0tS-qdh-BHjcVlQTo5BInXhm3wIu-CzPnFXvv012UrXUBQzQDov2e4Ae2fTToTAwEaH-YW_O33p56MlTyN3YSqOcvaJb63mUIVaCodHK_APa7W7YBSxNy26xM1Z3V95lcEEbpD0mMk-H7MTQ7epQ6n1agLYVjyEqNtTWc3XZI8B89JKKZaRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FErGWa8xtw3Kw0AlMWmdW4LIH1GTAxxtPanU_7hhJUYGW-myryP5VML2DNOErJOb6pac2vhTdqjy8E5wir2bwKjYQqCGQZqz1DnXveAVF6u0uTZTS_M6Uyvfqt519iR6NNcORPX0w6gkUiybWA53IA0JHHheex7TE88YyfPgGmvYEJ0L9dnTPrdRYoswN-gnF2ynGY8V53DXdHW1VqR3TFNsBNb4Xr0kAgrOscb22d1oeMHco8CclTDldSlToXizdOkRIR3jKeNvyjSddY4aTq4KERzKCdd1v3Sjm3wv-kI1k9bEu4RZ2XnRouvlqcmZufevmkqTx6gtpwTiD2oqzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHW9FFH3PT6t_FzzMB0ira9Js98-mbhR6WuTly_H1ITzKRxrY3nWi4oDNeabOSFGRFvthpn-yEro_zqRW_WzSvihSkAwMVY4wIomXus_nCT15W9M_f20TfQV01ccwCjzi7-5bzya8hZBH3GK76AW_8iKW_evN4ZGtlgSZAkCpPoS6Tk5yFNJt0hfoYVIS_Seu8K3yif2Xq_DBQI7SA_wJf6I69rFbALySXZlQzd-cJLvMlR4kjGyy7whj48MLw1u6lqmadjEnSCO1B6vPyndGqDt2SysFG9xz7rasVlGmJqZsxLQO-jrce1g_Gq43ERLilE-pxyU1grce-RonzuTzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VT3lWh0y46UfgUz6c1QQ6udBmpJqki_sZTycaK91uTTbKVeTjLy0M1RnVVGud-IoffPNyhvZavlFtW6jv_Yy7CrXQ2B_yOAyFm6dJDhZ1VXDFKgcnrhjWv68C6eb8Bkqdf2qsiPFisQjQc5Ocs97WaOVkN04TxDCKZq07eE7yYVqpEapFcHDALdWMUFkImnkXgDnpa3bQFLMXsh9JkqV7m5C77aHD6aU-H26hjgDFc-h4bqzbhk-yK7rRfzOtTcsnXHwIY4tpnnDCScw7h00PYBj4nEMMEyq_b4PS-n1XU2Po4cuZzwe3HHstl0kuKi39N3Y0NIYHHKaPPjZWiPeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hgvd7ETUOQOsu9Gtn9IDmFYnkBXx01Jce9BVrjZg4rGJtKhx3MhLwnmQFc1yRmsOpVPTzI9-HJ7BCeCtXeZlqEBBfooDOA_uwaaNCrw0SH-l6Q1b_PdcxvK6MLkzQym18SdgCeSlILkll7D00JAkv9XyZy4vviSu5Ut77HdgXVwrv5JpITdU_DtcMdta6UGsAk8mZT3pQPwpur5pQvN3DkRSCoNg0W9ofgpab_uIn6LfnBsD5LVim3Bo-2t9ChvTMdQCi23oHpeLdtNQPbRlcdEGAAM5fAkkRukEeVM2hXZNazlf6JCajznjcCxT1vqErpFXPwfQM3Ve6T51S6mg0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWynB8OG9e18GxAg8Pq_XTbFCXpASG5_-sk8wlBJx75q06nyqrhj0hsFrUf0-W8Rt7E86ROXzXx883L2X05kbfxNCZfuUQAiasxkKfcmnO6zfiR7XLtjGDmegrJcByFjUXad7xsAneeOtv343oUoZyi2SUN2ZQVGnIWGJVwLr1zgbLlNxbukXe8YmEs3wJjPXM6lSUm6RH662VRaC7ywvrjO6qqKGoo08PxQxLLHGcYRilTErBTWC_xr0N92ymqpX6SOTT5nC5bQwjxzeagQWAVYZSUCBS_ofQWkUSVph_H3kV4gCcV_O4rFcx0f75X70jDTZ9wojBdog9wND6BM8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf_emb7inGCE8gBgMivy6qYYrwrTZ5WATCyVrx6HcMKnYDZnXfS_ahfO3lg64sCl-351pTe_82rjhxpcFOQ43_cXc82CbBE_gYF18Souxn2ikFaLrEy6qPdKI_XUwYNVfAjWfGMi_JwFhq9sE3gz_tWrYY518xHH-qrB1LKlP8lXypL3FD3ayPKtQi9m52GmGwp4orpN8qtP-I9xncOgjWrmxnVpgD7VUDWUsV-LRTaypzRmYu3BQUFSXwNQWFBPZ_7tMCwy1Zq7TEh_7N7XG8KOJc7ZvNTHJCuA-GLOoRx8BdyXCDnhQwdPpJLwTC9xA6v4xlEevPqnoSQB0e5PgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhInfktphyXwVzQuVqtOXMy1Tiya1PZOy9P7vskRHNFEk46jt2TpV1umw7lNUtTJ9FQx3zqbmjJItt4j_lsSjDm6ThO8KtasdiCB_HDbZGvMhb6Z9qfKAJxPkPEPzsYwM6eDb0OTpJr6CORyN7CL9Xz1dTTMPd25miqbW1Ci9HGnQ1WfnYnyHLfG2HHO5X3Wy9LByKwLhkbgl0wVGj6nEPMAb1AOtbbMZLBSu86tivistOW2RsTCpyK_iR3KgsO72opG_ZSM0Hn9sNkW9fvEGIr3PO_kEWGkfPw0w_t0Smk3cWNkVAxPBddizAyH9g76HgJEzJrShe2U4ySHO6MsiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkTO8SEMY0JdCTGqnYOU6sE3zfXgnX9GKgAdj1ivB5LoOS6cFFTniSe-Lo4QdRNB_ZxciopqM19MixCW-ntKzX4VpIH4KAUudUVUIWd6otGCEFuC-1UEAvkrLavDPdQ2c7NDVOZ106SGOg6i1l--u_MX3A8I8fCKZr_JgJytvL6mE28mmFtMb8GPKHUUjKJ-t8Ihe8wlAY3G5jIvP4tpVDOHXVaPiU5kmvOGGl8qHQrICP7egzp_gBAVtFDYodQvAKd5NyBU21ruBgV_puIstZKMiwEYnCIX8q3TgXABSNKIKBXOpiQlaoDdvxJ-D3645xNt3HY5ugPSFjBHvZjFTQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sk9M5F2JV4C6Uwl9fAD4cYYQ_qTxbZEgWqRGhyA1m2RynOtADURZFrSWTQwriQRplUT2QSLl6NLme_CWLvsG88F8sm177UM8yV0TwP0s_t3rCAXPfJbL2XYHPjmeaFb58rWmFpqlwCM6r7_5ECbHRs6LNcpmlRyRt-YZ9FKp5mFYMLY8GZgPq_2jKotu_VIAGsyOCIhHQrtnUeeHtEtuO87fLpwofDT9xDUsr0EdUiqF7wKkt-eWTp7jgigkPPFeYyMtRuWFN93LJCGvFoymozpKMFVYMhH0hxk-QgW5yhRQIVsk_tEqyj_tW0mX5bX-wLNVz95eviZ63QFqeMlA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sk9M5F2JV4C6Uwl9fAD4cYYQ_qTxbZEgWqRGhyA1m2RynOtADURZFrSWTQwriQRplUT2QSLl6NLme_CWLvsG88F8sm177UM8yV0TwP0s_t3rCAXPfJbL2XYHPjmeaFb58rWmFpqlwCM6r7_5ECbHRs6LNcpmlRyRt-YZ9FKp5mFYMLY8GZgPq_2jKotu_VIAGsyOCIhHQrtnUeeHtEtuO87fLpwofDT9xDUsr0EdUiqF7wKkt-eWTp7jgigkPPFeYyMtRuWFN93LJCGvFoymozpKMFVYMhH0hxk-QgW5yhRQIVsk_tEqyj_tW0mX5bX-wLNVz95eviZ63QFqeMlA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2hr7c4LJMX06Xs-RrqdOfMUlunc773UGkCulGHsPFyUo-gK952KURAkD9CcFp_9fFx4amHuzKWZTxXdgSIXbx7nT2if3kuE2oEEy9ShwjyquUPTfIEE5INCAvYcJrRDr0b_josjR_YI9vzKHnlRkSrEP_nSatHW_hUPLf_u-xgCcyCHRoypSmGt2MoW0izE9RvtcmeVGmB7awUymQTHafHWYI4bGM6AptBPSzqUYzANYsr5Q5I89giFrjCc4DE6WvQC1WlP4vodtaOebz2yuJesJZHzKjaBma3f_pTuEqqp-w4zewcrfo79JJw0I8OOtq37O4ljatIeeoBBO3O7Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-jqyu2h7pNL8onUtOkgHQjvtcbtaGjCQgePvrf4Lo3buk6dQEvrvsQICk2MD4JklFR9wyOJo6y-BU2YDsm9mIRC2jsJ6gGVS2X6voYHxl4aYBC6eYdDYzuUc8oZgYBYP_uhNSh9f3xA43iHLtxPI3RCux-Ua-IM0csuHxprYdDTpDYJdrzD8GUbHkYvYqAouFHd8cAaQkKx6LxsoPzSD0UAnWVrdfSwtH0TCoPcEj_-8TDkDuSmubomccOcqqOvckCEtOsiyjyv1flg4iSYs8CoSNvN4iFwBW3oENOckPQ-qdMkHfU1DrbfNyu_HvbK1i81UzNVu2x1XfVfjJBdlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCtgSk4UL-rK2a2HBPdNOOAyjWK618Q0U_ML5es-P9WUCV5b2wCFBg_tKqjuBz_3sD6k9LMSIAvmmKQkuCBRe48cAM9Z8vLsKV84BW2knjsx_py6OrlhXYy1ZHoHqNrk_tnCH3vRjlTEyPWMXd2io1NtJ2rEo1g3VHnJGq4KrdgZOOj_hi1iBWKX7nsLEQPFzkDRz5bM3XBKkxIgJ_MvgN3t1qmpV-ZoD8HInEJ6-sGrzhZKeoMZonfzivf9qX2Os6AiI-VA6l_oNdNFVAUDJLsnDu1OtIrvLuplXQPdI6HD2dKxqw9BVVeM1qUidRf1WkdVw3nwP1hyBTY4P3YFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwokgLZ3kzkWEekDNZ08nvn0A9tjiPjWTyCc850aRghyNY9Ti_H8y-WxqKBjLospcuMQjs4wx1lZ5So05CD0pMnctAOKzo_Spm3UX0AidK-dbkQImGtA7LpjU3hvxhjuIsMzy3wtZPKLSq18Ym4ZdkhO5fPdiQwWvfwuXKAje0nUrxuL1SlfLMFl4p0Lfcu8H4laaw0i-BI7KwalqifiNZBTHWy-EeqGIbfopsxGg7q6Ej5x7ewwuh_PgqQYk04Eh_eq4da0nYzuRym50BXImniyQoTVaB3gUYvu70o5ydyiN1YP-3cVmxUyHlPPtS24y6BUYUB8CGt5xttPF7dXWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZtyVeGBynBirK7zIyQgDZQ60OYftvFtzqYxDqyLXyy0KU8k-HA_gbDnhmDo1078BofiwhvIRf4boE1IOFC-AGpO8M_qvF32QovwKDH4wET6lM0tq2-VRNIv8qV0KUnWkWKdAzbsPukXH5aQu3S3GDeGD7FZFPAfsp9xsfV_VDf0qrUAD8_isq2TfHOI560lTrXxWWKQoCO08vNwT4NCJBDEEVfG18XwWTICE2rBcar5sj9X2KN9luJp9oZ5vCXR5mOgwtb8RQDiOtS-4LVRCli22Ug8QHXsZPbNoTehuWPOtbDe1vHbqXoWei6VN1_igiQJQAm4BywwSKs-3vRqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nS-Ha3yks30zmx5gDStDwobagFrJp5v7Ym2CUW0v712-cOFJKFCC_BEd4kbvN3O0wa7hk56c2pQoFxoRYhaa4X9bv0RJcJaIozW1AWSltRok1msjhg7X2XCWhwLy9KIhK56--LsgIA61Lvz_1vC6dnhdz-j0uv-hGhIgIFJ44yxb12nKJuSzkqlcIwJ9NDUo0DBrg_BQli932KL-v3lWCcavujfV6xGxLbzSv0LTCOXDQZ0DiWKxYGGng65yfiSSsYJVwk6lxtX6TLCQk7XNkE1PHQPQOC6H0D6UvY_3kvcfL7k1pmiV05ma8A3e6GUHuHdaUF8xIKMp-G7Nis4zLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnguOw5a6j8BgLUHU7JDBcWMvF-7F14oEGoXJmbLpdNMVfatxDozpsUgP2Spda3eqz5fjcLskSRZeUaJBwu7uxXZpGIuOcyxcP3FeiP0EQyAb_45e7j2g5ORiIeVkNT6SyUORiNvTMGhuzvsfxBhy1WcMsTxkGfNAqnKggNfnktyxBvB5nk2rptKuyD20XwVG-BYfxeyDjeKBXPC6qJCB7jAWF6Ou0fU18dUotlvx8kXdJNMgD_9nFiK6Kly51ajUIdpd0QkXUiQqV8IHuUCfQp71CvfgmQYqjbPRNSnhqTpz_AJTwbOyKjrsl0fWc0Ptc8BWg1_p9ToGZRWje3pdA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Hc3J4JR7aThiKm3xwR3tOeQoFjRgWrkTc1NB5TF1IZmeC5ntz3WGUMlwxaXMh8JRdtD0zRQ73vn_0ColVNirIiOQlcrnndqlMOODDSwJ-PI3iI2To9-4lHpZef9iqBsP1neCwBZWl-Dum-dYpfEuUxmExE2kiDc8pHabG9Q26luOYBeR-Vop5hooPwpwZJ7-BUiw1hV2RPscgV5tYVG1erR1WnXqYH3-DMxr1BFM6FSwFlkey9KHxWMH9kmYeDsKP0_NjNJAtekdWgWyecZi0QhQ1Fbvg3VTAt7kMVgz4LtVeYs8wS4UHOqXD9cInG2wkRovAj2cxE53EMQUgpdm8L5OtEXPKRmQFpvrVCVtWCfc7AghrFNSkxaV3sCH3RP2njQ_mQIYe8noHi9Jn_73r4iN_EygBJs4o9G5rD5eRn5T_iETMQTceWMspfxJTUsLPeO4gadH2JVFtUE74Zbf2lZZ0E9YQ6c7Eve1AZe1aElXG7DTkvISfSUs0UQ8EndkJ8oaiV_JouvhJmOOcd4pV7hoecoDm7GXnrW1MT2zX3kTwDF_K0awhTiZh9Bzk8u_9NEdvsfKPkGLrfw4ohRWyHAKb5O5VFCt3I2bB07SwOgjdZMTYZjJ5LpMmBuaAOT4qkv9bJpqMmqh66ep1fAbwk_8pMslJ0GFPevq4zB5Yis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Hc3J4JR7aThiKm3xwR3tOeQoFjRgWrkTc1NB5TF1IZmeC5ntz3WGUMlwxaXMh8JRdtD0zRQ73vn_0ColVNirIiOQlcrnndqlMOODDSwJ-PI3iI2To9-4lHpZef9iqBsP1neCwBZWl-Dum-dYpfEuUxmExE2kiDc8pHabG9Q26luOYBeR-Vop5hooPwpwZJ7-BUiw1hV2RPscgV5tYVG1erR1WnXqYH3-DMxr1BFM6FSwFlkey9KHxWMH9kmYeDsKP0_NjNJAtekdWgWyecZi0QhQ1Fbvg3VTAt7kMVgz4LtVeYs8wS4UHOqXD9cInG2wkRovAj2cxE53EMQUgpdm8L5OtEXPKRmQFpvrVCVtWCfc7AghrFNSkxaV3sCH3RP2njQ_mQIYe8noHi9Jn_73r4iN_EygBJs4o9G5rD5eRn5T_iETMQTceWMspfxJTUsLPeO4gadH2JVFtUE74Zbf2lZZ0E9YQ6c7Eve1AZe1aElXG7DTkvISfSUs0UQ8EndkJ8oaiV_JouvhJmOOcd4pV7hoecoDm7GXnrW1MT2zX3kTwDF_K0awhTiZh9Bzk8u_9NEdvsfKPkGLrfw4ohRWyHAKb5O5VFCt3I2bB07SwOgjdZMTYZjJ5LpMmBuaAOT4qkv9bJpqMmqh66ep1fAbwk_8pMslJ0GFPevq4zB5Yis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIdABI_2qZcJiIgep4AvVfEuBaEqJ6Wxvs-A5AnGSIjKwfAXiyUEwm--KP9Dxb7A23XmwNZYpu5agg_SrqUcIVtWv4KoM5mvavIlqLYUbgWMQ5uudHP9j1MjTuOb8iN2ijwTSjm5lmBN-MkUlJF6sC619zFHM2FZqZGr3DefUwslrW9LVI5aAG06uVnSDHIgurFnLFrRnsk_5m9VLD4L7h0r2N9I4jvCnCt7QM6M-twpQ-YqkvGiONriLw2AJufAZANGQ8cnBtfdCjOrp_0LL5O8kyleg-B2SBBdWwUEWYaiwOxn-3CJYbVSy0SRZwyplN_mDpNO97kluJxjIqfSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTzlQsU-gNx_85mEXSFc775nDPQYQvXkiZDs6sITiCc3E35M0RSGmXn1Tc8cLDyIgWrciUCYDttv04dUKZLEYHfVh4d1Nkre-c79WQfUGvvgxZJKR3kQzwyhNrLWkmqnPTBbOEuXD3DnFYsML_xvUzoT826pTdSEJFE1q2eEEIznarRUsc4AqQ6plTl6LEIjdL-mQSBN5VRC1xFy_Br4YS2HMXN30e1jwDJbNWGeMsYtoC1pOQGlXKiFszkW8fr-oK3FpIojVHaChcnFdWbl9VfAkHO2H3dsv9NM7R7iHsOcC0VAVd652pWDMXgQgZavDvmsyery7GAuqmZzktKdwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrhH03exNZ29OLUwr9GRxZqsJC5K3KnXcRuUmIZvQa9WGDVzMpSQpPYvaSnOs9dVxpOqtZDuNyEdXYD7a7MEAHnVLJYKHCPgNg9vgFd6jKcJTNXf_Hqiluv-LcRvIjoknKja1iPKj_ZKdnpv4JRKZcFmEoZr9H1kXIvjQqfaDWOfDtift7jCFhEs728IZeb_IDeNfN7h7h6vq5Bc_IRii_8w0M9dX1UwBpAB5xyw3TqtG8f8dzWuowASb8gzpVFTui7x7ztYiUyO2R1tlzVQ3MwCEYAe4foCc-PwVm2tb1gQGDHP_tsKD1RC-KegihvORc3VWlQv5TmnQg7bdmitWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaoG4v2EhxAYKAnqW6YHkqP3lazJmGutoQIccj410vKcGT2kmy_PVwcP0xvOTorvxxz-m0HXZDahLGkufisUO1awu6vUu_O4xL9zkTLqNGKpg3HJd1ZiSKePQwkS7JXVL3ZYDXeUp-hqCDFlnUnodItOnMhBbK_yVGL4sH43UHddItW07UVnnsZeISGYOrnmjlnqbp3EFLJ4rry82opVVsNQHjhjZ2is46tF0WjCWaMxFv5LN0y5_TX_yUReJZwSZ8PlquCa_KbvNXGDpH4cUIRkB90cvvwQ5sD7WYTyCT8ER-DAYEf3eTk92E05Y5F-G1AIGJ3NVp2_ieeHt6Yf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/empWPDx0GrawiriptFtamECchelUmS4o4mZXZh2N-HdQI7cRq74qYQ2kNGpTrpQZVDD4SNurWNY_BEJvwePAO7XoJB86UypfcKBwpaV-fF0gzcD0wbVKVegX23J8x0Bnyyz3yVyGcus1q8TPeAeRd0BDzX549ANxBuHN4A5TPaZ8ii469UJWEhi9OJ9E51KlrcPsXgoYFTcL2EKREP4xvMVMLDvleHjf6zewRXwI8lDIVTd21MNG3V06HcD0A7eMrjjJ6Z_9vJwhlT9rv0FdBdsXv2n5qNmsg4lJTdNPcu7RkFXINpCXVOItLNjDTMtU4t2rdXUkesPuETDA9yW8mw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SB661E7HdrKDhljZ3H9foDaPd5RtvQD0qNaqjJR8Pr-KNQ6iOAcj5yEvvuk2G3RBjWSz7fuwyaBRm3P6miTw9TIVsySPiBMxZ1Qqv4mF6iY1OHkd23oiI-DGNvnRAoL1a-imxoz3CMottRYjKz-3laURXaD6Dqm0AiiuLJ9U8GRAe439ND1WnYfJsoC1MOMoefMSkrntsrcnjXl1G5z8778n-PVAe2mpZENYHyhelRk9Ecw2_qFlPqzX9Dc2mAvz0hFL8wEyhj14HsohA8Oy6Fsf2rljbaujGw1L2ziDyUSaSCDj96lTNipVPemp62VIsE67TsDeIZfZDMeqCp35RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SB661E7HdrKDhljZ3H9foDaPd5RtvQD0qNaqjJR8Pr-KNQ6iOAcj5yEvvuk2G3RBjWSz7fuwyaBRm3P6miTw9TIVsySPiBMxZ1Qqv4mF6iY1OHkd23oiI-DGNvnRAoL1a-imxoz3CMottRYjKz-3laURXaD6Dqm0AiiuLJ9U8GRAe439ND1WnYfJsoC1MOMoefMSkrntsrcnjXl1G5z8778n-PVAe2mpZENYHyhelRk9Ecw2_qFlPqzX9Dc2mAvz0hFL8wEyhj14HsohA8Oy6Fsf2rljbaujGw1L2ziDyUSaSCDj96lTNipVPemp62VIsE67TsDeIZfZDMeqCp35RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7G46faEOdOT0sE0sH-2yidT2HJ9eR0htiFp2PuHHHbJPsQJW5iD1d_ftXUuoJ2hNM_MOd4b_YcDt0s9k4nwO00eIEbcBIL1P5KI3PgNhYZB7E6fTWo0Vuwq5ob0ZNjtNg-rpBAJ4kuuGnouPoeivxud2F5aLyBWEHM7q4esn7Ix7NO1L4v4edsZyp_vmecqcFiX58M6xVIAVhqVbBm3avUTWNrrEzBjQxCDKTRTyK4pzy8A6N2nBMRk0cqYNRamVY9-ES6V9zkk2_3QsFnWSSgrg0QV4G5vTkaKxxeq86d2wg6STeZxGbSOH6jr8OaiwOlVxqqpjRc8lpVqcjmd0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8LOSZl89eZFMgBiyQXq1Wr4z9ZY_muMayMA9yKy4xHHr7wur04NBdJik3uRTXZ6yApixjMUDa6P9UDF68siu3-EPnIyeKxoXVXDbW60IeGo7BIvq8YOfnrZ2a8Doq2fB3HD8owrS7VkRF9eU2rrg3SOCjEhS-WHW6BIfQ9NqBQmrOXdiJ_BPvsA1Otz3LJE3HdgOJzP7KSSbLSzTrlU51qN2Y06muPZFlMoO5C-MQz6hIHOQ8eSZ1MAEnb6LCnCL5pwbB1Ynfs0zBk610TXFHscDuNsc8wfjqXCqt-wquM6LVk9J2MeCqG1QZA1NiYnxPzv-2_Wq1XbPpV4lZkUAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJ5WwA_ZQAurgerOaVybUQzDzmcyCQGfQGabFiwdgsLN-t-JpbkRfCpucKnZoPxWy4bwmuECJwVg1xqv6Q_tN5f4FRZTu3rbff4e2CloDBF8YLm_BZcC8LBEbHztLfRA7XjvqAo873wUmBKvgl7wLZuPLf1YTuXis0cMMCnVSJDdu9y51ZZSaMMrtfMQcbGvtFD434ctMq1e89F95jpZmxzOZERC42K_03RzwH58vsIb_ZCE5dYVi8NuUZZtzdbDMgXa6Gll-QYNYtYzM6DWOJzUyf4qWP074rE48qJZaoSZh21DGFOdPyK9MV2HGiM28JBT_ER0HJAcYvHeUTYVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Us9hSc_V1hT3CdvQFcXeSsNjAgkiOE56skd0Agchkwf_CWi2NaSwgUU37U9FLTwZYANS7q86_eJoZr1QufG1P1DO24e_APWj8quj5ERqqkbidnlZy4zKXY2c8GOLxS7jCPIycLKcaYl86CMi0pJUWeXJHfehV6SyaMAYzKCF61yx2FN9eR3o6qaNgesvZ-ewubGKP5C1VmzL2CzbNmKo1-MPdW36z4psl6_KWseWeP9-3CGEi1ZMoWV9SrxfKirr7ioyisGnqVWwekFaoFpgUHey0iPDIshIse3U0taP999ON3d1YsfLJK8hfsJe41R-e-M90ZUYTI43M57otDk7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Stet6i2h9HRkT_LKOvYUDAezuVvhzNPkJZKK5TkI2qvxzRXk3YpyatbZmERBeNaDgXdBICe7CNJlAjqm-c2yZacObtGOSs7snHlcH9oBFa2AXXVjvLemGeunxO5UMnyuV4jt39Fghn8pq2WSuN-yqT1scfUNAxL4Q3Z-XJiuMVlvljdsYYQzuDPQ2qgB4SBeawngNppLgcnRWCwsjP1IwlKwX6csYJwuZuT-v6jMWBewBeLyPrlHvMeiaykqWq7ygw147v-DoP4brDXPdRoLycc4QdgbIcIaMK8dUVK-s3XyRcCfIUaMmqeJy2KMF8o6rlGXgZXzmRk5R72yp28IUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF6j0vq4UvmgTaCqnZ0KTyGzvW-R6kwBR2ARgi9FmCd3wEES66ZochWgqcemr6fh2yRTD2DG2K7zIZN62o3BrDnUvSRYRzRFkw2FldxVPc6sDhDbBJUH3Us8IQDcNfkAV5mbiy314fey3PO3fyUDfvKIOFazXgDuJN-xp3Q7jlPqNAP5lBtIsI1WbFoeL2SvNsOecNYblcHOEOL4B8n5xBPYgGKqCZRclmCpWn_3cZt0n4IiqGCdhBFwfjhXNQxFUPa_xm4waHLPMhNjYtq9hhwSDhJsKcYzUWUMfCjxSr_FBGkQ8vq9PQuiH6DqLzzNqy6f7XvkwDCzIxbbF_ZHsA.jpg" alt="photo" loading="lazy"/></div>
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
