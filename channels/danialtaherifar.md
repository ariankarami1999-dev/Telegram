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
<img src="https://cdn4.telesco.pe/file/Sz23KVtTVXotEPb4QFZMNk5g97-Lgi03a478I0RpPYSu0LQj4QuCruoLgjWh6vQkvbixXz7cr8jAovn5kcTQjubUSEaiOr7bEjprpdEcpT9N7qs-0I_qJU1keZmUcFjsN_72jl7PYAL22ogRg07B-veMTYCQCIfN_Jy5BhNbYXtgAblxtONaFCZ14K6awQSJZpb6QYboiA459dAWGH3tXx2iF4H7Apsm2w1LX0-sRWjOjAa3OdaMLIlEvuQYisTFGQItuUiDBXWfk_trTewGKdkRdF0gckDEKj4Xzs434WzrE2IB42CvI8gxNPWdg_RpYcBakj3d_fqmTvBYslqgQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 21:15:03</div>
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
<div class="tg-footer">👁️ 196 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 321 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 547 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRQWTjCHVfgpahpd1nfLR3fD2POR6WrsuEY4UtKgvuUUv9yp1RMCLuS9jQ5FKWnvw9Eq0l_yiU6EWj9Xab30ZQXuPykZ8u2CXMNN0b7c4VEfOzRQt88K--fcMmCvigyO36rrWKJxLhr4YDm4bjHsyQedNmqQ5qiA904ZUB7nKmAaBJCZJxX16cDznTr5UYQeICxUlUThhLH8H5vIJ1mfnFvx3u6lR1egJcpmQd7sniyX4KtrifP1-7r7ajpiGH3VvmWuOwAe1PywlBrFh14e0K1Rd8qwAhahf8yTyVEVYbtO-FKzriENgBDOhWC_Qo88MxI9r4WTV_LU-2tfLdLC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Elnjd87oMXBYQ0OUqw-cW-6_hKPPQ0ULi0jnH6b18WPA-hl7KvVJODIwNE4B9x1hd3LExvWhJUVL052BTuyZXVFr9cBdf5WoqyH6cRu4goDJPsIeuyMvHpqawXsgYoT2JISpGXH0qgSAnNIJohuFDpGH4N7QalHdet4B9hFYuce9dVLV5xLJbxEaOceg2K1r3_R13mV93oT6VvnRrAirVreGcSIz-0g1kFNJDrJJZIcA-HtKZRQlZOHGUAJxJOfea3-7x4_pDT9JFkiylHpwNL6WkLTu-SgAbeGNEDCcqhWiddYDW6FZ2vmAFXQoafsjuWcF22dAswdwcOWtsSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I124eKBKrtkU-mC5gXuG15xuwW1IHTXUZYUsAhumeaH8PVV8_gxWACJnVrxbsn6OegqQEbtESBlHCAlebZQ1K3fycwDGyVL6q4XLMJ7UHk0N2FCF5P62pP8ZSlXeWMPUWpRDdW5s7xC2_bGKGHiVIpONGB1I16M0tiArHeHGOt-bDC3FnrhQYfdFwUWKYomO9P2RD9q38Ttknr0fKhGTL0QNkRwXaXK0NcfBnEzjPtNaIFLSWQAfUAhRaKgc_efdAF3QEOTPn3DJhqPTR4Q7RprSSC_5SmGVEuNDvkB79wk1qx4hvtQ6RQ1R0h1VDeBMHHycd8UtdNI9QHkz6930lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwdzvhSbCFc-bUm87hHClVhMJCh9sV1xp9pxetTo3vGjWuqESA4CjF8KdnA-qDImspSs2relxMHc1jsPE4RTHq76YPtLkhDeW92wwJTgnBEJ8SD30ftjUOwZ3JfguhvXxyQ_1NGsSNLuBjfL3K7cwu197J-MyL-OBi3UP1qqfS8WjHH09I0WpuCqLSnDO-h45Bq9hnuD1iUPTBc9nYZGhzdKMeHPTuR0QUNxr6-lSUTEPd42ubUOlbZzzYzRCltrLy5z4yzl97YBIvRFUVDVH9ZXvZjdD2bkleve3w_FGe6NoS7u6WE3m3F0ScLjwk393Tq1qCJvpVJobMOoQ-rOJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN8IvJoiufw82umMiG9rG2e5cYuRKpzwbbwILrB5RFibQApFlMHoOXtnlQ1vmLBCfxEj7ClwfQb6yH7tQlLYRAelg2Ag5EfG42uX9RnltL8ZpJMNd5ZRJXiJ5snpAM2Ofy5T8XqX3ZNZXhHjGfqvCso5i8-9d1_dj5sL0XWxR0kHwGTSkNikZ1veiQTbcNNrwtLKem3sssvTorfqRNFh2niZ-nIj-HQkLah72kzmjzmMmiwG08Tcbg8xRnZ1_Aag9ZxVkgFASZvu7a5hLJnC-TGaHYxkQ-L36JSJxkvS5ZdCAlveK8l10R5UgO3nygn8He3mjQCK6KE60aLuQy6NNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUNnNwPdpZUN2pBwqiiaLsmRBLn1svEvRNxJNQ8y5AxloJfy97rtiEsEt0OxSH3e_IyUyJBSX8_-qUeN9Ji7wO6TryptfDp86vjqB9cSko-7YUKeLrPWo7UlXBRighsGGFpDzU8EoJUKe42qw2kCPfDIdKwDp6qgl1Lc197TlM8jgxjYe-WEGU3uCGUzc10j4XJQH5Nb0GPhhZtW1s_z9-QKVRL8Rv7ZFAbt3IR2i-Bbn1tNLt2hUblpcETVorJktZMn3Z50Zao2Oiq3lhgYX1wb0JBvFLP0i_1uoTwyOuUVo_T18IESnMIWi70OpB04QJ3whP61b_3fpLk0LhgRPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncsUk1ePVmZhaiCjcL42q2LuJ2tvNFPWc79mAT86gyP2SKELsOj2Yy4m_tzjtrPXK8fwmGXOX23hrBYKG8mZtVeWUh3tlPK1qQuC48mftVwPvxjpSVRgdTV1nH0oqBEebY-YMcSW56Mx0T_7ctvCVRJFgTxZ6yRwYvqy0Uy-7Odx7phcTHZCdmq303MlpOwWfbSADjVeQp3o2LMwPrP60czptag-oMwRPdxxZviJflHV4DINHnoXFAGeCvHXfxPRDY_XaAjCRF3igEcsg5GAr65wIF-jF19IEVml6fX9yWz_MI2Ho4rYP5Mj_aUrk929bLF1S5UFYJJSfxYd9UUzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAYKLHjjJ0pe5fiT8p1J0L7gIye6G5oDdqInhoI1z-pzFXG45lL-VVyvE3cq9sDuP1UVb7rPmk5UVIv4eduqyS7Qys_fRFZSCfsJtfi9qKtf53_Yyxk7yPGSOsY0CdmJrumHyMOfMGF-25NHhJ7j2KZcYQnAmfYNRhy-1oUI-9dWbmyGnGKERc63pE2MkPHR-KO9rZO2dWdw83xrWNBUOAGZw_3rtxb6c0f1OFrj4zYlAd5ix_Ha8KO22cc9XQ5pMNg7KDWnyDYRmRo7VTmxm9O-qqOEho2hCqKhjKb8Yy4NQ0Hgi9id5l7yFuM_9n6B_pSdij7I479Jx8978cBL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPy1ydy5NYY0hcTVPT9cP5E_VcZrEcsSKhP-2LFDuXSxWdhmoJ4GlLgBVDJ-ZIY7b78y3KfaSGPQk0iBCL1kR-ys9hxtFZYYRLJ-XiXdDoEoQTjymIyZL3uQvCAn9K03_zA3rbQOucxCDPXwJxnjlpY_MhzBU5I4tQLpNWCS92H5oJa2yiTiR1XrKHNp3pslNLf3Qj8xS-YFMogc9S7S9T5MPn5wiDN_PU_cB9y-Zk9PEV26hkqAmVTYhh1ZBFYy6s9rHNkQBAWrLXuMiVa4pkIZWLkpewK4L1kinK3epMKgdLCD0aMglAirWSrLuVa2cii-RSBE7khmBamCRNxCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJE2Uqw2sDC_LXyDc-kDmIwCfDuFGJ3WWYmFZTOn7HkiSdAU8TFCMQyTW0yusZSYch6pdEiVlU82x3iSsjtfjhVOkQuaL-wU5RM3ITQ61ycsZxVtz65HScBc93rJjSJNaSRXkA7DNIhgdZR1euR0HCiODOwoPQac7uo8yiIZeJp0tiL1Tjh-u6825B21LXtCPYfCXz25il7PEv9jn9dEtA_Hd1BebcZFCbtlKhBLoRVt2t529DABXNB1BaNY3YF9P-zJXP8vzKwc0AVOaPErDjv0-mM_xUbH9vuy6Mx6lzJTZD6m2r7VZdIP3Dzw22LeGF2wDDfWbgbsjqtq8B8TYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn7wZ99WQ1R3BXDe4c8JSKD-k7nQJBy5yIyiaeHNcvrFJLbRhnJSTCoXhf-2QBy6rNJHLjpz0rPXyuHyoSpovrS5tz58ln6xRD5eqCV9lmB4sKp8OshGivvC-SlN0s_ybYWBKZs-LovMcBX1lebfWibfj6h49XHLgn7ZKc9by3_pRfB0O5hvbk655sgkxpLg7WJCiJUqgLEnvDnSAH4ZO5xPVY7INnuZPWuqz6mDe0pIw-uVeoi-nE9kHzLYZIyT29HPe-iYoxevgTGMKodB16nMPYC0OPjTWuDKJbvisi_zc8kXwzGGDSM9XfWc5YSSPUfaHxFoSun7crX92CGe6g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=QXDsojv8HnyOSl_YgTTNxQGxsNqaHcMMarqr8dST6NPX1QnSi3rRoifH8_UmAKvvHhBzAXLUnabpDzCIkrrl0TZps8_JcJ7EFh3qChESOXk2RBhhptqjGJoPU9WGIznlb_TygD_L3kxza5RT7m4YG933CPPCK1gb-RAFh3au1LntnzeeDRN9qKJBpOOIwRf0Awp536sCgwfTnPTZzMUaJDa8bWAUnPKtQHy_WBdegmBpYXS61zerduTftiETSsgt8q4aDQOHKHhK4xParP5bdYtrB6y2kitrsU57DnCrgMmzXA1-JFKi9WS34o-iLaCTPBb4fEvcuu-1XV8HMMzLbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=QXDsojv8HnyOSl_YgTTNxQGxsNqaHcMMarqr8dST6NPX1QnSi3rRoifH8_UmAKvvHhBzAXLUnabpDzCIkrrl0TZps8_JcJ7EFh3qChESOXk2RBhhptqjGJoPU9WGIznlb_TygD_L3kxza5RT7m4YG933CPPCK1gb-RAFh3au1LntnzeeDRN9qKJBpOOIwRf0Awp536sCgwfTnPTZzMUaJDa8bWAUnPKtQHy_WBdegmBpYXS61zerduTftiETSsgt8q4aDQOHKHhK4xParP5bdYtrB6y2kitrsU57DnCrgMmzXA1-JFKi9WS34o-iLaCTPBb4fEvcuu-1XV8HMMzLbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9BJ9-UtF5XXXWmFHHsKWrogOvhHWMrmC2M_wsdtSbNut9bM-ehgABpxshQK-bStKPvkhcnylWLJWAcazK8R59gtLKGWOWgsbphWCbsAldoJi3U7F37VSvOasyOR8thPgk5tK2VNEhm2_sYW-TTBK5smQOUA9mffxavqE1muTcqkuZpy0dV6T8ZwpkMqJGWn5D3Hd6kRhEhgkbiE-dGwprsGPZ2-HSYtLPQyX6dms0OjZSd7g3YST8CbMWOoWzjlSCCV9EkIh9xDr8IKweBGK0GkZPc8pUTyz9jqLkjITcuhtoF6WI7F9-s1qJgVLisvPqGtzJ9-EExvVCthK85I2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4SrDxnlYKbyYtCgsnibnMKOaU8ZXtXDX3ykPyRHeoChuq9fylc4C1Cfm7t2_4Z64EIFuof7dWDF10tIrpFdvs1jgpTkZtxI1lQPI5zD0VeRBSk32gUiieWzSkcLYv4kRQo64rLsO2wPfv_ZBTlz5zMZycyz5oWivuCbZQf0cSIH6haeUfzl7f3eAYBHFsYai51V-HHqOLWU59FYcS97VgmcZvx4yLF_6ZttlmIkWZTRtX7txWBmSUWpddlRNl9hlLRrB4QiJp9c_6wa6tqj9sHZZGS2vakfGW0Y7LMdzFTtsfjtdf5LCDcPus-zBdJyieeFytEWo5wOJDNHe8mupg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TH9at4eMGKSg1VOvCq14W-kcofw97UF1-P7i3lERILR1vSN3HMglE1n2-Ts-oRQH-HiJoIxYCANt7TEMwSo8Dk7A88QYhADFNfX-xFVd_zXZ4Fm3YqRrcV6fwCBInIPN7p9VwULG9Vx8yAwAssVv8wOXaeX4pJmZWjJYWf-puTEcq9XQdjGZ1w230UceJj__AQZz2xrubt78OMr__T-96qfcrx0uDlpxWIQC2t279ti4H-n49VMRnhccP-aw6zYyr3Q2QkGHaZDBX3cCxzAKgMgIs76MUFXN_u7Ghl41BjWoaTb6p7JndjOCCUMxrI5yIllAEsLC-ILKn9oW28FsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXjR9dazvOrUeCU9anjIWHCXPFy-mghBR4zV197ipgynS3EdaKJRQgtotUaEcfOKdbhZOZ38QDOADjn88QdLa_y6TvwngYl1sOMoA50S74sViIx7zBbj6dqy9WNoaWZfvjCZq4GgZpTTyYt8dp4FHCo0VnCJjPAqzhszdxHqwaf-03ZiQV1upC52OQTAiIuteHvtmxGB3BOZPmCOk-lC2A0ja4TqCJGCE6nIMzupOBMPwgeTiyGIZruILC0xcsHV3xva0DEuhXTfaAlrWTKTGaGeeJVrd0eTVFSwe9ik7N_zhuBYsjigcq5d4HgETFktP_ZlftTfpczUnN5X7NTofw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN_fPtpIiZn68IpJ9K2gYi_E0cmuq0YKwrTZNshFVVA1q3OlEUi3PWzfgV1J9okRNCt4nbiY69mmWgMmw7P90AD2fdkGzqxTenIX8syk-oq-ikcYNFyiSHbD1vOSCtDPXtgGqE_9wDigDiHeAksdQlNrINScyezwcxo9i5oV5mV52-Yw6-wUv92kVIijAHJsUH8sfQthQluBYi4qhNnBAO7vl7Gb-mhdEoNgGWXhZ6wp9Aiv3dl4ReegW30M5ysUQlrptS2SbwZHAbFtZOl41kJRzt7MElXjtpptY4xvRxxp6cuLOt_WEdFl8aG7hVcU4MNfWCZylCPzhyLikwDEnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDtLBSS0ZcLLcnZWtFc2fcGMzhJ_4QoCKdIkFFHeagjhY6id9wUw-hzNtzpFkeJWdzo3wsSwepZRMAuPg3V-yx444VM_aNvItrkIxJ90z0gxijjoo9B0KI_mddU0QS4bpL__diiF4yo8XykIv3qo_lQ9TP_NBxvQwAf1XHD-OS6CZqYqAk-DC1FH5Qey-kg9uaBnniavQ2twIJQPG46NuiDH6S36-BQ6HX93rwoVVMgN1TkXELr84QxeyF99W3H_Aglw0SxPx3fWetbZOBJHcAFndkxlb-Fij1NntW_K8Xfb2Mbo7BclFbblUymHT1mZAsZuoeayeZ3uSJTSyzW9EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULNHfoH_o01OMhSuSLRlvzoF5j3Hq8KHEl_E3KVDqeUwxUTzGfxG4Z3Vo2CUuJ6L3brA_IATB-79dzsaeNy1qAQfpzvyCL7MfL4jxb2_lVNfK54TXm4FPuVdsEQBKQI5bd0pIAsGImCqXQvoSPD7I8TM2--GvNltubq5TPzSKWF8W8XRrRMVxMYlo8MLS09gdWKL2zm1vndik7Ip03lrr5wgToqI9MhRu-dcDfZ4oE-zpwacFrelSAyBDadPERS-gPYaXV9FDO8VjnfbM2O9O-Ya3raVGEqWfB0DnvdyyjOKPgRFUgRzQxix7dnRxpzZJ96LEoNlo939TpX4rk_XyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf6DdHFgR8snuyUmNNE270odoSK27vB-yZcnbAwkVozkOajIag0XxU3ZcvcJ7gsqZlBNCJksXL4zbbIQBJhGvkYVrft3dyyA4LsHIBL5I1Fd6roW-rWE-R_xf0tQ3gvcPM9zReIdi8xgTofvSX5R5sCg5dD1pNGkaFLHjSz-oTTXtxlX4qUsTXLWks7B8atP81_0S3-YN5mCldXrjLMElsPloDZt0rY8IzSejqfSp9wslykryWM1r2_TBUezTLnGr5PHZzdUwUQwPwVWZgqUKKtKXpXzI9X62uO9C9Y0OH-HrDdrK1E-7xT05pt80w83LToqRd010w6NnYpJK5ddsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSNEmRufEVXH2BmJ_TzAEjzrv6Bk8vtKpRcWj8kdS1JlRo50bEKXaUUiKwtOwZD6knFXZXfiFK-08rQjoPaVWFBQ6lE_rtPUKwVee3LN-WbR-hNUjRjqmTo5NhkUo5ZQomW7BOSTkY6dnq7jGCZj1_eVGaEWZsQVPj_nWkXXFYs1juBNQXdAVHSzs-qW0v-pPLe8ga1VoP_DRHWpfHWtVgDjiq_VHGzTX2qm2N-JoIOsUOlvV8gDCZeqspXLLbUxqYcBijlnfaOWmvP1xKi_kWXghEHIXyW1JjNwHIa7Mb67ydT5SXQ9LraxhWfxuyQxwvxWRkmJ0ORGgm8i8rwFNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/or1H98VTmVXn1B2eZaiCqNeJHTioe-s3j1i_Wa_UJV9ELAQ9IDxaM63l5KnGpvEE0-QnYAIP75qt44gN2CKExr5PHLLb3no1bDdyWGQvVbMFY7nmnN6t207tu-9-1YP1o8qraTXLuw2WqR8C1yjmxLS0gEoa1ZdwJdT_yKWyNMzhhArhT8Lnxq00I9zKIFvzPm31JBzuadQ8Zh1mMOEDXderOLCOAzPyM0OSUAUhhUCyApn7-bGd2pzxso0c9gVv-v9c_QMCDerS0yHSyShx3nygFstklcJdUCCuKPgUxzLFA0ToToAGZ90Z3PkPB_RuiGbRAnvyc9xol70N7MxAbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgbP0qIrL1RtRh_2lFaTeo6MlOh_JkoiDOc6gFh5F6S0OTkzsknL75S4lpLueBx_aH55V-cbtZVyHG7slQ2Y8N7oWznOIJ3IbRhmhBHfnpOTmKbgx4CsK8vThK4k4YcCD5OJOa5ISxVUXdXWg4ofh9JadlCGOuAQburH_8xgFLb-d4sA3-S4cxrR7k_Z0kF8ChlK1FHFT77RsGURbYbAB81cB-maocgOgbpSkR8bJftI71A3Ctz0QSoyhayQSGxdHGb3xjOzLb78JEZlO0jJpw9mXk8qNjpjjjy3yXRcraitIQwO3bow9VOav4COfVeRbnR9LO_5LGspjrWv-zHNhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uco_JHakHzav3IR-Y4lJsrIOS-OS52duAId6EBhxBL2l9JLZlLtr9hSVzLNtekGRQU031_JdPW9TZafxisa52ZwPlGQzyp40_t-o62-e4Tk1ve6VJo57mRgBqJCAIOfV33iFN75cEVSfsalgWx66ImUEqCMUF3mQDRnvrm2XfRgAk2QTpenVLKGOre3aBdivem0P_CJmJsOzrOYwKnCUNagoRfxAQCpZewk74Et--3LJwe2JDC6nOOIVMTS71XLXpRqF5CW15SjpN-XUCyltQU1im_ZWK1SjGbfW5_448zmYBQuZJvFRZWNYbqMA2iCbi3HrTpMngpXann8Sen8bXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzjdmgUjVb9fciKcBDtaa9v7J_m-zR62PZos0FdKsw4MTRv5xJ4MMtLyE3MpapYMoY8TAyo5xWqScKwpB-mr3a2Q8SZECdh9tkGVafUOQ_FspuPpHjTLfnPKte-30wi_kmSfvDLmGjjdbAQc4F2O5uAVpsz_VY9v1zEinkT6VlD0tI_bdeY0QpUA91EYk91WtQJuT7eD1NLXVwWRuEiWztD0Z3qoefQCMi60umn4WmcEswuu1VW38h6GDTBPlZhdk66-8b2BGltBerXPgfnYYR0mAGojg7owcyYri8LtxqPemi1XoANayh6M8irjhuhvcI0r3KrLDMqUkRLyOjs8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckqCYb0XESODza6wBZIGNYbZobyBWvnh7-QHIXgC4rXwNVaeSC6cecqj12UqiUHRz5140kvsIJK1mP9x-yu0sfJUZTUFfSWBBc8pQYerEyQBOY-we9aXQLoTXKUA2C2vTbxlHjzSUnSoeqx1gf67DCKcNtca48yKxAF0_cJNzYG1Tfil9Nozagz2Nf9CckPPTyEo1L1R5wR6UpEGYJ9jUnsSzJekTvHDnX79HF2ppmSSxFcb9hw2wn90ozArf5kOsd0JA3bOPGZX2O9HTqcQ_zPwJlV5h5LL8ehECjEHbbua3HKiOeNDwOJBa9zPNzF5667zYrCzAV5ei6mjSbnUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6HqCrYMdqBk1Kui4DTEYiC9A_DrlMSThrhH4BtBB80XytWn0hQw9YMiegLkJZCIUAZ3GRsW0I72dlWARIxsxKp8W0tuNkHzWGX1hGo74JV-0l69bwsQclJ5q0L5qTmYfNlSh_NHkL4hAcCSjTpNumZRjIlSdieSyxGxmSV62NXXFc_mTyHxFUIJ5K8g2boObB7DfVzAs7bgtNcKfqlAoMj0br6RYRDBMx92Htm1na4LrccPBhMK3RANF46r6U0Jjc7Zh2J-KDQyEpB8TGF6Fm9TrfPfs7GjfMTuPuf6DMOXtnsbr6RiTVxxFPvUeDBFzUB2sOXse5dss59tktXNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smGQA7o38c0sHPP9_73AsjaEbdY_mgKGlzidCdblrnadfH0ENN5PPcnmLR7k-Yj5NQ6Uuy1pE4sLwJKtd2CZ-pBx7k1qfYqiMXF77mKsGJ2zy4fJIIm6JOvcZuTLMCWezUTmuE5HSsuHr2BdmQEQ27VYYZ1MQK-P0pUdKzBvCvrwosKQ8ZWDyR7LGIl-BoGPKfeK10M_XN-WknuXNXhCMeIiguD_yoPcY4GR3rYPydbpmRBLT1IGK9wZ4PNMfFL9cpowij1xvnyE0HwumerEfz9Fiu4QT3wYB3HHC6pPdrkNpyiixJu841Vz6CjnhiTNZqv4qTkbdGz20kWmX3i1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUOBdEU9yDz2_jkIz3MlquwgOVn7WRleM0VwlFig7E4ekn7caeDXdsX4_x3K23bbtnZtF7d9egbmY3jrDNem99FXOciunEwaDdffCotnvymaEqz0-OGfB_oJVh0kKWnOVUBBteTV7-Qnkdi47NTX1_3Xh7RKMTUcnoKZZb3kG3G4NOSlRbiv2H0zPINGvh_czvWSe6IBnTj-m-h9QWX1G_9nMiHV4Zo5I2N8WcL7DJWSPSF6nm3ojn6V-q2JkaCYerRtFzK4ROUip74Q-gh7w8Y_zH3WPJQ7UwBTT7RLEB2klWOaHKlw7u9nJcxtxwd6n4KEZ5C77LCRFX2b5_sgNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQU0h3M8ey_BHf78gN02ZmUzgH45i5gVS80R_pLhsHNzDw6rR4l6vQd9m_6eL8yumab1Paxw-kk9ns1YOUdBRs3Wo3tETUiAaX_mwbg6R8I5lpcaxeCJP2A4R-rJWuAEyrWr55-v8H4emwV7m8OS7EiSo78JnAMRhzpGfycokC03AJoezdE8K0hOdZXfrqZNsktvwy40If2oJirzTj3OegdlseJZOzgjvRgSwB0aYDuqof5ZHakyVeEaqPDgwzPs_xr9xX-XGe_zFum4EiAb7gSk2L7LnVOy-dJ6ybkE-k8HZpGjN16Z9Zsj6xE21zJ8ax5QX2fUHN_5hOtojiTzhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2G70kKHSHfW7uTtecURALdXB6S2WxRhS--t2vvsjzNMKOIfhU-siUogwzv6igwPfhcosJps5bYb-Ow2hTdQpVLbAtW_ayXgwxYPt9jZOx-cDe3YSGAOnk1eLjTlG_Ug_TjlvTHiWg7gGbVne1G9SoiHS7hBNZGqDZ9jHC3DwBUA7gVb4EM8MMPK92w8ao55_yS_07v39XSPadPW0oxXV49eNr-NZU9kDuRSnZd20IBVmrD36hTmsQ1rYxVmWTRpyqThMlvwxX5BAdz8nu1ao_d1rx5hiChQCX4H8t_I-_uUY7ARCG_7GWIUYrELotngsurWNeDN_iReS5hJGzbyrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYrZrHgtESqhMSjrFruMEDt9CPdVEO0AwjJ6QHdCc6A_NarhE0DwpsI34ZIHxX4pDL_QiWAL74tU2jnJFLvKv4Ir9FOXNlX8MK7QVumG-XbLm1xXZ1GGusHt5f6Zt5pjIu2JMGV5mI2idIg2J4nm6IQpGXdf84tkbN2ns674KJmDdMzl4fA82cGzGWBypxeLZGhkWXTcTmJKXiZZYqMJtoz3pLvJKRf1084A268xyGmhBtxu_Dvn-ZsYi5LxCxK0UpB0U1wJAu2f8kKIvrteyVmpbmund1ORksXwwR02geRld3EuEkSqwW4n7z7sXIVJNBVDcyrmqFyS4XtCDX9lig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a65BXbjKzjIhfahAKkLsrr4e0HX7ak44Kl1PvMnijBQdU8aKcv5ym8pXzyS9A5PaAvVXbIyErudbczVCFzX3-AgETldMzrCXS1Pm7qhMUtfCmQmG0qH8E3lpCMtb1CvELjOvAUO-dIFostxXtcpvmEiy9kAeXdCc1j5_hvBosMShDMW4b_o8coyawBwUpl2Wqee2wjuTW0pIsoftOSD1tqeP55ATo6LGpo4-Cq78LoL7H5hYjV2hR8v8TsJyFvjfmClnjTcYBmoIeJdk9zNJUg6ZKa4tobhgyJeraA4ZcTN4yTLksDOzzwXwdR3SUyJtDawWSFPgCUNfpx_OgMzQfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ79AxHcbt2Bk4fuxHA1jP_6YlTZDgmrUTTEA3pwOCEMALorxAngpGMOT51T6Sin0CYWXdhrzcHFb5jG8Ds8Lvy-43VWxwyJ68AT411q6KL9EmnBEhrDAnnHreGQBEnNfjK2CTDI9Bkjgel1gjkpv__78U1mflhlo4ZRf0InwAf-CGBpUXR6c8nX1EaLnv5JxsfGmGcZ84hV_RFN-mE0M2McqKCdsGvUMXnjiqSKG5RiBxXoSzVlWbfPlVk-qBNd7GBu7M5kEK-fUFQ84jGqUYK8g_HmtX8ST7P1gK3d_TBQ-h2SslozA-LnOl1SlC5CfcRMD_XSmbnD26VoUL8yyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shwfYJRwqfjh8oX7QxcXMuQzkqpOWAMRmrTIS_gG7i28gaF4a7z6hzUUffEWG6tblDPNP64ynJbXYu9DRuODoTp1akcZ549LK_p5uJerzODa1lN_rhcqwLTEGyzIvGNWo28dIl2_lTjeSimvzQhaUbZGhofa7wRZV-JPiOh_gE_2-cptjpHKjuNKhSl6NLNYjGr50hO1Et2tCoGcGlCC4jNnJoa_nTB0r0LxpNgF43OEcKL-XBL7bH9MWs3ds1AXl5E9qbUAcEC7NnBnBIK61BkaXM0lC5PtkWozj-ej55uRzKzMt7HywPFu29ugxujHrXj62BBs5_vIMbd_jMBuMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYMdY6ftG6Z6oeuNCtru2zO8Qia7B603e-MGP9lELzomGZd6zEyq9JAv0_kvOJFYIsFlDSEWboKDD-IHLktQDeJNP0LtGZYt1ucUZuNz2JlkdLRYRUbQsWVz_lPF6b-zClsjWEBirSQ3lToeb5iCdr-GQkqOfFY3-GBUsuTj9zIZpmBVJr94MRKwBhHrP-sl1j6wuZ46nzK5w4sFQgPuhKesU6BPCT2kVoBG7hiG_GQUZxEKiSW1--hmewN6etTKzws2sfc4DQ7al9tm2lr7BzQERm982_YmJon-9LMCUAd7PxPBWal0xewJaopy63kVQF-Blu2wDst_Zia8EEQ3_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cALGpug-FrtzzwUxR5TG-86B8KrZOLTSNqohyjletCyEPd6FTI-d5xrx8BoS0gm3Qu98YdhfnGEjh8ElmbtmyrbxhuCp8FFWaaeHsFFKR32aCq1cS0KtYBhOWV55QM2w09rLurRKKn-hCOIIaIVEJbD2WU1i9mVhI6lVtMvGhfqbN-1ZY1DBgx9dRyqsWGc-x_oo2RjLM5BoQTuyCD3ikM887G1ey2NZ_4Srfha9loi9GPgH_vsEa8FCUo7P4CrypwD0UShtDyKwoW4gztidUAOphjlTvmbJA86KC2aPQfBq1G3ySU9Hu9LCjeP6K6FoyG3cAgBTrguZ8nLqX-Rn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaQxbaWfHz_MvmYTcMUP3gBFsie_4rz_2rzV1mGTuhkKcXu_QXbYH_hipCqRVd6MSKOYzrF-h2axSViJ5MUEKZwilmhJyD1u_q7kQ0cJ_9_Wqm9CHv5Adge1XA2tevkGq5wsDBHAoDG8cbfwzyhONFPwxk33fes8RJdvhjJa9OdzHlg9FB7Ifh5kBMMaPTRX2adUZKxlW20FDqn-e6uTnnfzpXy777ZKg_zJmv3rm4OGk2Me3UxjcxIwQOGBQ4DdI4fK6lKXdhYiSx8md_qVY5tEHKzjBfz6RpY6lzSHntw1rcBF_VmvhaKdkM7qGzmjOvCIWfUZOjnHVfhs5WNTUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9VDUxYUFFgBV52qOn_hVkfZKtw9KuWzsdSEJKcLamx9cS3XyCwOW5_tXX8fkV7o3HhnoFMSo_OtXXV7UgNTEvOQsgWT3k3oKEprRA7yiLyAgPyVg1F-BPCSerOLB_VdhV3qy-acV8tgIDuJXndIPq_pa8nD7Q__AJ8_ktsUDzadr087R92DgBxiN1KBMp9wpVE-oSlLo6pJQxrPa0Cb35u6U4YH8UClO4MFEDH3IwiIjOYzArLmDWEDuw3ObWBYGnEpm-tT6KGLRz8ZBZWednXMbwbRek9Ud3wdf1qYRzHAyU38Shlqa0a1nNwXo_U8aasoo-YpNT_biXGKSyb-2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFzLSTHWG3dZLWPvnyRncQ7vT67g866i9xAmC3O0FnldMSUKRGQl-Azc2bvqKyfZrR5SNZrnELfbN9KZl879bICVO6aNvOzwM3obclEVL-qYYQQ_TPPoggblJNcHCH_XkeUihghDE1xVGHahLdFxjknyKZd7OLtc3gzWW_FVhHpz5UXDnI9DgSGi3CvJATsqhrKedKDN_WFvNdud8oc-eDUSz2VqOTCKL6W5ycxFnnD1rl6ZZOCumpfGQUsE33O7p_BqGxGhBFp8Bos153BeoNVVwxxMtvA6G46G9b4xg-3sX7V8nPCYqSbwTNldo8Ct9kaPKKSA1HfNW81zH2u3Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL6Yu0q2C0jl_DfQyQeru9Ggtf2dnzXA2AONEI19OzTFFNKk9IkDokA_iA2j0fhP_m2YNJ7kFAIn2J0XagiFrwvQ-Iz8ySnm7DMY62BV4UZu7PEAFN8vqWzu81jxAZhE06SR7DqSXkKy2Tu6QxLQM9n_B5UZc4GQoamQXoy67giYJ9F0X6tN7-QpFGOOKHo_UNh2Yh9Gzx64unU-hI8KSDMjWMOfWffXPmvN48GtSTKaMHuptKeHSKFSz19lfBsOV1ubss7rl-g2yDjLf9p0DdyeWEhWQzFIWH2z-WQA4Cmciq4SYauZvv9_iyXnHYQtLVC1Iw0dQRwLmcQo0zbS7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgE4Ju0gud1hT-3cj0U7WoNFY-EFg-mRpy1Qg1hKNSdtM11oiKApun4YU849YjfHv6rBgnoQPbs7Lo__mtLWMMjxrF3X1J1ijIkMJqbZVClOCQff4LcsrJg5AVSnK7sRIYaabEBv1Zul90jxbFXl4hVs7_xYZZuQDaFm5pVAmXOnxZ7JfvhCPlvznkaUQmNGTgRGxmmFcj1awLNKOaVPGjGi_YWpi-NQVEvtt_VK8Ac2wQ0m45n-n63ChMdYFOIXf2KOYXnKm-rNVNTD6Hi80biS3Iy3eycm2NjcBhXZsceaQ66sn-JtXhYCaPfjCSCWYHs8Hp2IWkpee5TSQpo8Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSzd9CuJo9QUi3zSR0o2j4eURHEyYz6PmsUV12jm8yNSRtsQc9oiAlojhkQz9RFk6PK_KZv4LGj6fu0uFWPqNvxtfKjROfD0oe7_Sb5rzDW3yDZZ36I95IJQy7ugTs60fO8zmVVeEDu_gsrw8qgbLbmAK6zSqc28IRqEEVOMpBw03PHJb5VI60RztlHaY7Q6ZYeYk55h3m2vJZ_dNh9a6RE7lidz2hcZL60TDGFlTQ9Hw59v-K0_JUwayDcUrIFtiw37CVFGMes3zTyV18nHa5e09oM43TMovnOh35nNVWkiuggg_uUMwRKnxY2OEh0NMb8K8bbsbzUD_tsYeI5hvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY4fEYIhONi4Lsq05DINhW5kmtaBom2kbumCRwor2EMADoDVSA2QjjQogaKUBMb-eC-UKXoY6-tHQ5KHiXHg3np2kVebUUziYdsWGFnFHTxw1T6HpFE0lP_C0f9lSn1vmLziDRb4Zyqz5BijVkQcM3yu5tNaUZp5CjmY14Y9x2DdRUjbjV7eXcfwTw9vdrb0N1G4MzJr-G-Cfbucw7G9CEtJyIxe_Ia8Du6hpbjAMvH_Quz4uw8kGBHWxdxQ6OMRn2b_PhR9OLBAYFDxmgCUyvsJHZTTxHOUr-qWsrppbprsKYReSQOGO6tR07Yw0uO51tvArALjqjW6H3azSYmbsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FijK8lxhjd24PqozlIH00HQPXS9cF6rD0UETXrQd-on93ZeJChheuRHvFrsVcJ5CCiOAXqUdmBorxplamBL_fGzXsZkPFjq-WMOdRBAH61oPdOG2thXmidA_58S5eTKyGiVq0P45DMwWEK-XzTVIRm0HQlabhNLFuu0wqZSWmQDUx05-fsRYM6Wx5HIDa7OzDSgUOvdZtrUo5hc5RXFQzYhS_sIfrgSRJSzCEvZocEsV-7lE-iUtht1JKuUC_uyyhljKwwcG0sQZzemqsdk8WSz-i0OEaWuJGD1kYBGp6w4YZmM4wQWudLiFkSu-0p_k0wnWAx3m6lqoOidjbbcUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIPtrz3ihrlyvquGMTuqvzBpHEb_EWJn3snbFEAmSKg6_X7P2Ww6bm65rvT52vLrJNDvOnzGqIOCHNRRjxr7sR8SesVbzUSz0dekB-usyM_hFh5VmUjIO_cHbm9B4N4WNsBBbwgEWb42X_t9etKeNbQexSV13z1QEgl3xGBXN4aeebJBB9QaE5JIdq3noqIL0_g6FaZLlFJabhNK_bOpX6kNHONP-zbnxJqQohAepIpuj1SqbH6NxxeWklNTwxbAi9z-4vespfHYdmziAA8Ty5s623_bwvXoSsIAI1cCfOb7oBI4tMxZ9A2y3oTtqFjfy-kydvEeaOsaMZdphjy8iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCWHGRVkycVy8ht1E3qszJx_WJ0p93mkaAhSih7PVWFjMPu1GAioJZWDLV9QQGSXLFo4Zdn-i84-ClitYnQNJ89R7B7YA0QdNBLstTZBsfJgAu1TwrVcmJC3SZR23jJtjJIuPvJ2aOfOyOZo_FOE277JdsZwHrbutaqheH1AEog8UUJQV6aqrzS7TBidhB5qZ2c0gdk7mbES6ysxOyo0Mx36MFI3Ioil3PMKvTTJjWpXUGGdUgq2E5AyrTYRSe8SnlZ4o66eH9nfh92LQ4eZsDo5UViscA-4o66lpW-TIvY0Rc2oHEHTrJi468JaL1CarIoga5hS1wMYkOAyHBQQQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueTjhvFba7IuY03CM4EULPfcOqTIXEG1qlxl_R27O1zqhA4SahMxJBSSMiNHbCH6NxK_-U_UyK3kdG6zQ7qCnaBctXJCqMxqCbJ3bX8yyz8KXVhHT5vm3m0DckHFGXVC1uBqFvbzczHXfN-RVAB4AFTkVoLqpT3jdESwljqdc2th5AVcTuPO8NL90Im_JO-HhfIikGip9UATgRVF2znxYbVR0d49SRQt5RL_EMUWVQ9Q-lG-nEK05fuvhjsIbQMXDdGPoeELUrprbQsMRJgVzwR7bNXxzWre1gqaGaVCT8Jzpj0e-G4FZlgTGOyfNvu_TqkDgC77AULOoVC2tHiEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwivGfzyHE84-GYOrq3wkBtsYoC7iAT3tNgi4RX_nEfcAuy1bFUPDMS19msrCsZsK_oPz8dpzFHmeeUEOiY9Sp1cJepsv1f5gneiedRQbMah8FctuiDT93l99XOPC2uMOqT29qcI2KS6Rjqk1H5ujQZ3yGidWWyY2e71-jVYt1ryINuREtZUCiUk5gtS5Aj6_TrR9za9D6vJ7-coFV7BjfOrthJ9cAyEU5FC5skTCu7jDcpniBQVykSmI2vkai0pb_16Ov4JoGTzWB933Wtbgw3mfOqUO-uHiWKYeR1WV2C6_aGtEmImZAXIFbmOcAL-jZh1fEqQac1nIK44MrWPdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qic56m550GZWI4OclEMQb8zOjx5RLwCMw5wv86kbeqZbab1C5cFJZv1yqymLBWIr-jdvwaTxdXhoOtlbwVQAQRa60JS6DVA_eSyke-A7YFpHDMxAy84JAJQL-LkK-hZ8SRzMyfLF-kUWrT0KOikNHBtjfTRVc96Q5xp0ZTed_b4g1suwIOD0JFfLGMG3VglEda140r-KQKX_sMUPcR0sR59wYOBA5IdyTztPJo5NYM4a52MAy93H1oIWdriRafND53NQcOG4aB4_esk--0ULsP-OGxcK0RHP2gBfSbLm4HCyYP2_Y1WX-mKjUKHjvCnUsHqhBqeRQr9VUHhk_VI08w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ-PLWwa607pPF_cuell2D7gFC4oNJWHkTjUZ1fFsAlRAViajpet1nJcNcM0LwaKBN1oQYD1JEXuUXCsXhJkkSjePz_cckoNUH0_C1iGt-HPhBx9KQoxDxRS9zjlICaXt2bXxT05ZAFGRcjPyT_CzkTGFU42hxzyXvZxonu-EjH1C2eobJS3GfZpkETfPghrBP9bSV6zebd41VqrG0eSgWyf6Y6ppbyC-BI3lzDRLAxByUM3T0OUQjfKJEeXFy85AB5HhE0JgO9nL-xo2xPL16My5BSUUg-hvyFwVbYaFnt-E4p64fxiEfYgZRn_5S7Cf37ntmseAYlnC2nPx_GIvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_OXjVfUeLOvJcqaw4Xw9oTGa66hcXDVWcQnaprJq-26LoL6Q4CurmWZBOneiZra52Zq1CK9kIeGYyyzQPkVj26KE6aZytg5y3stWOX3q75qJruK3BkZPsczgGzCRpWV0gnc3YlIqkV2sPVEyXfO4SK4k3KVMUjwDEmIE5EiMrL4m9NjNgqfx7nBY3Yy9TLxqTtkKbQy64Y2kX-FKDf0UYKRWznxkrLIR-7hjeWY4zLT0GC4pcxRL-NqFYodt49TJpG2XLBifUxLKgjzX8JhY77O0RjqVSGZjaYYVwY45P-h9v0gPBXJTWRKwru1bVWawXARkZnL4-XBqrygogmJBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5hjh2av133uE_N5GttxYaP52vuO0jpXHYg8YWmt3oMTBhQYMJMDf0vX55Vksix35DsYOWvCfRbGq_rJ_6LVvN3JbsSkUNqf_LyYsZmjgVUu7WibCBUNVM4W4pJHtWPLlTp6FJ_6_UdGEu-ldCqXG05PXHzq6GsBI-7T8m-dUFQXSTB2K8vi4d_7_XaX0QF_Q5mTfalvvQ45ZBWHM6tP6DeP6F1zc-9k76rmMDPMxhIBLfLyT49-L9LrpsyPfc3HWHNTJp2fpEb3jD7XttCU-j-EDc2BuFX6I2JRA5zK0ALdKhp_Br25CGBkTxJNosxli1dT-IaBiVVPhrAUp1D-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqCR8vRc-wFjvLRwsPfu5J76jl3gofj9rFxd8s66EjC0MUJtGoSEPYLJDcTiXb0NMU4XIZvH7W3UchUuBdj91ZDzr50f0hFlruHdrocllZXtheTtkz-DfD9I4zKtjAnavrCGrX0TkzDOlCkoUJtbHa9WEWWwtXkg1BSW_8cxRFAxxq1-X9jaz7Rdp3Lfc0IjY1Fqb2hiiyvqlfoKDSfLxeDsZ4oaoqxxErX1squEoveMwud2LDkMj9cz5EoUhNIRC7V5kpKMxmrNFd8WXIJEI-r-rQNdb7KK7sQ71SY6BiGhlns4e2KEPN6UAngWh3C4vvl33G_FvuJRKE8AwgafqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqIEnRM3c5mz590meoyj9W1XcFP7osKojbHpWjWb_TI-n1BxHuAzA9M3Z9ddY2zCacIz0asXeHmZwKcYwfcv1Dd_Cc09xK9uR9oqrQx-cJTvI2RmwfKsyszaepy4hLsFyfelecghNQahYOm9s_2geLkIz4LPM7ntT48OojoQDf-B-t9AE0EhCPiyYCr4A_8oW5Qm8vKFHxcKQ3R_KshDov9K8M-JVCRR_np05wuO9-eOuO3ZdS7PUlQFchUGcK4g5CjQjNVIjkO4ynnsHV1W_rrQtqkhmYm4eZ5xrq7wmm8sgRaygxKN1n5DOdJfyjlrj5EWzFpOE-gOPuoxFk7V0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOU9a-I5Dahz9M9hrWzmGu02mVtKe5rYSDZCNJPiY1hHAkeOJcpk1ZyqBbpn7ZWdd4HlNvqzLx_71wr6CoElGZbUWt6fzCic7IR1_fClX23NyIwUdqCNvfd2d8GrEMbNqRwYqPtg4cvgIFykV3yClwOyijz4mh_674R1W1m4vfwFbzuOFZN-9R9eNatVef-guLV5DB29eK_ylCTL3WZ14E4c1PEkr3shqgE6opXAQJfv8x0rsayuk50NoVCGXUO78d_JmlrUAK8guMLfhzWHVrNnr4ND9FPAfTsP-Erk9D26H3NLEARosIlhFXEEzDwfDRrreJfVsQjqI4_zXOrjiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvVU4z4h8rF_wjvffw3bdiwNbA5awnwdLZAfJfKRqzw8fqi9gxlQcTewZmTsoACue7dGNDir1cT8bjYWUsaNmfAeBdIKqFolO4VCFEVikfZ8vO5MpNeR_ZVS3RohkLHgzz6iJRd2P7ca7bqkMie2qbh7rBAB73D0X4WNIPzN6HDvPBdTkQObe1eRekHUXgjuKrzFXxd-pAstZQEvPBe3sVVpHq2tJ6GNJuecvMmDV0lhHign_Mjx658lWxWx-WlN2TbOymIfuXifu4_bxhKozRtRPwrsLVLSidd4ZYensLxtf2CkLEDBc7zfv9wKWk4hyMQaG5SC9C6KfnY1ONxppw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0duaZ1w9pF2kATs7x6PWnGM4uNDKcKAXun66K50kyjBvzIR1VtCGGqRsKd-xZnZugxjPQ80hglmdgzy-ZfscCAhj8re6kGQsTNqAsMij_jfI3sfWHK3H5L1n2ULnYcjZBmKn7KL7UH11Ckx1QIJ7pXerE24RKv-m78Hyk7LHfPdrR77FeY_bEInRWtzQKkUSsEr1dofFyLWST5FmeBDPWIlwiKf2KlYbzsU6t6x3LSWFOjte3VOWvoV9xJqkW8Fz4Io9extfeoFaEGAvnZE4OxMHgx7S0rL77SKRV2dehytwHvVzbtzQAk-20AM30wqtuuYoD0FDhL5lAYHTe_elg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Wey6lpT0qWyG4s7peKCBenAj7ppzftCYMepUvEUFhk54GExwJTcGrQbAMh5Wgm0KTCcvq5hdOugWlR2kvDBJtVYY9yfwcR7dr4-MiuSxiXSaoQ6vR1xlC8cT8v0nYM5P2SC_oa7VUlF5MNCSYfifylQOTlg-tZCEmBI79cYq0NAZ3tGE9JWQGuXZreV-130SIvZQs0j9_lE1NekSaA591cLOq80tXYvZNHU22mqUCMKyHsteoGRQJ-Pq8-np1cBtNyxdR-ZzB3bMiNERPvUf_B_YoM6CNu3H6tXwi8q4bnkCF5R-qLjXj6vscOu0swJygfMULqbVEz1h7CTIvjeaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Wey6lpT0qWyG4s7peKCBenAj7ppzftCYMepUvEUFhk54GExwJTcGrQbAMh5Wgm0KTCcvq5hdOugWlR2kvDBJtVYY9yfwcR7dr4-MiuSxiXSaoQ6vR1xlC8cT8v0nYM5P2SC_oa7VUlF5MNCSYfifylQOTlg-tZCEmBI79cYq0NAZ3tGE9JWQGuXZreV-130SIvZQs0j9_lE1NekSaA591cLOq80tXYvZNHU22mqUCMKyHsteoGRQJ-Pq8-np1cBtNyxdR-ZzB3bMiNERPvUf_B_YoM6CNu3H6tXwi8q4bnkCF5R-qLjXj6vscOu0swJygfMULqbVEz1h7CTIvjeaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEstT-IsxNZXNuIKPJq9ljrqZRBQr8YFZ1EjBUFIutSqu7rdthuN1tkcp-BpitvAMHHkTtF8fXpxab4mu2uzLrWYnP9qt7xd2XT6nWFEwBoSA9AY5UY_MTZk7gP02YBAslNJ0nl6YFlN6RMT4DIbYlRZ2PEmpjZmCBltwY9RIzc_EjHvkJoIcFbo0opCB7CAJ1GUVeyr5fFmLd5IeLUxjSEucZOFH-sz3rVZpiPeEuc_3n0AyXRSPTYf70klO8Jtk9DpXPTuQ1VIkt3OISuOZV0MCGYQ_Mx-yhrI1fOEvd_hCVcyfF5VS-qVxvPxH4B-iVl_FJ4uWu4aFHoU3wVTzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBRSsT5gGEKRpKFUq6ZRwAiJf09myLQG8b0IbbiQ-f9rmuqd7pMOiPe2J_MJSD6LwtF08-bJQiBjJqdp3wCj-S5tGyrd-2mF5bzotrQ9PVCcyKdEFpn7w7WHAvkNUJvJ-bh3jcYFD2F5ZVrVKyTT-V-Mx-Oj8QTpsXEnSnMIy3M02M_t1pyi7huLnMnzmWVvo_BkQ9v0oRBGgmJa-vpA90gKtu0Hel4hZ8687aoaI5ERHefhsS55iaUWmcw4IBkmixTlSnGuK380JRZyRxBH-mxnuBB77nIY0nHbrXDmBGYS2YI7N6oz4uTDJpr2gZq65s5nlvbuhSIZ65SWyS06vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMWuYZONa_HdVh1Z0tsSCNQaKpXnnP4W-49S62kat0scfwgXdUapdOyt9-XZ3GigCTkPFMdx3wdDn0jea5mrF5TrfM5VE1pptLErnq_54gmH9pScgiQwcXxQ7RX7ykSIm2gr9j_Rere3YcGc5BsS1hwlNyehgx0lPizTG06xUc4K6jhZwXSX06YlT5mWqBl93Bolc6gDqVIv9DC1yyY2rSPqUiDwnRgz9S6zc31muXu5hKJP2LFsb6w2hXx-BoPDZS9frnXAUndb9ausvW2pMWWQLl7EVvz1jDY_6XxGEeTwf42j4hu0EH59LlhW_VuVEc-W0MaY0subROzUG421sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pi_xn91NzjOsC4qoRvdUa4BXXepe9NbBJ9P5osolMnxaMj7gSsHoNoD20i-DNCxKueGtGhS4MrHiKcNSuKZwwsmOYyK7vnkDqsMlwGktmishAR37rvLuw5mqDc3iAWNqn3bN22txXmb8W07c3SZazQqkRqSEkyVUKur6URgIXKjmfPdvWkUyitpDztyn33q1IqTGITogg4d7S2pW_OESbnLDDJxHD69ajXxafGfjsxYTHNIixy7t8909-RusUlI7-eNzQtQUZa-SUAa9oPp7wJDQT5eV0tsWv1COQ6HK9d1aC6Cd9Fk0tpk2_c6cNHwCQ-rxIapYbTOOinkrzYY0Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9SAV_KjxUS8A7-o08U7RUerHbeV9OfSQAlUOTudO5eO0UqKkBlOULdgWFAYiMufexOiiFv3JO4xWno1n3bnmHf6I2kzY2fZ8yzDXBDu127z9FYu87MOfnYJqaHFi5amwG7Q1PiIwK2DdxWOTuDXLrM7GaPK0JQn686MvJdM-8TJAzGKY8N9vEFe-TDfoezvDmto44QKVy2_4Ev_7LUZ8_SvBndhzHrFEeF1Ps3YBCGi1Xi2wCNMhdftJDiSWPFjvU0qIQy8bY2yBoqtEwM0nzeTvedHVhZvTehd0ytTXmI172yVxieTwpdtXDM893MbIMbapHVsP_jYPZ-Q1xYrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVtN3PJWP9InbUOkPa0r3rH_Zg3QpbJpSSWIo2D3OKGUxvPdgrRKQsw_swcUDe0jrRCcXndmjRbADa1t-Nug4oN31tUaTBB_aw7bBQyR1o8qrJkesYITDpW3_1Q6Gmo7Q5Ldw9rC2uyNXUZhYO57dnOq6X1s_I3LIAIf_anO7akrWbIG72fZGomNsID0G0HdTbWo6YBqQHvafSb4VBJKwkWFPwMMOelnTsDJ2a0OqIcL7adhC3vAzgmOCeEwqCv3ipKFygRAuUIJ_6En4l2m1iVzXCadoN2nEboPN4wxxctHBKV0krswFwIwpOF2UKRTxbhe0Q_MlCkRzDJuowbxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGnBGTeN_pMZqmqwqLiIQI7r89S3zbfA4j_Z1AkCyGBOs0wF0iSOH_PufYZvs-4ILhIW3s-NRs1lz2uatb2CbMDsiyHvY1zQ-qYVNYBYRd6SSyYbppKVlCxXLTiqYVrtQKOGqIn0XtvJO6HoGZkSVvopwODIDPfJQLUIpZ1mRAF8HJcCrCoUQUxUu8d9-6JptK5pw24cyrbuSl4nwyYWkLDl6-nJWkvglCgUqJoD2m0cI0rZjVJYOUiZzIQGMj_5UITi8WDV9bzV8KDQtIWNGvpMrS6fmZwHTcYiwJIVwy0Fa8_FUTzDO7x6nWWoXCWrM1elQARga-msovlDpr5mKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Mnf6vra8YR1wp0fL-bCLkjkLOBj1NLD_FFL8EYeO4RkCitvB12HYxME_3OucotEZ8U4w6PObYV14UO3PdBz0UffpYId4LjOIF_YXtmI39I1csZNUwkITnTLzw2zUOI5lLx7vf-fqD0YStvq0FFqqI6UNNpFvDfAwreOzjAkpkcNjfp1nVqUWQXv9nLfsWw3iFigU5-J1h-BAyH3eKJctqTenl-KQcJUl8PA3tKkiqe0OtavsOcS8xNCbvT5BCarIjdFMPpLgep4mQvCKqrlijK7jKAy8rkeizPewDVlb7X5gWeinhCMozZ6zLy_ANW4LeSpoL-nU1LdAJyurPJukEkrYXsg6PuuQyhR4xsLmwInjy8ZqO481IGGzgMxH95CWlNBqcBLsrPvOqOzN8uoL6W3ocFu0T9mXBA3vOJP9srtOWlge6X0H_vRVo7KPZA_rhYo_bwNSKygN5VXOCQpaP7jds__1brr8Qual3jlIjPtbEHX9zuroS_dpEX0jrWdEYGFEFa0VgO_hofUcE5rvUxdqRpNxDENqix3uX3QKtzZ2qIbpP2Sdz8BUGelTWvkKKkWzrLpfvXRHQ3GE6buQp_RWyZG0YsIv7zhK7b3s4DVXcrIpx9GpSx2VC8LzRF7r4LImyl-XLHptDsNlbu3p7bt4RauQ331-rx2maNZd9Jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Mnf6vra8YR1wp0fL-bCLkjkLOBj1NLD_FFL8EYeO4RkCitvB12HYxME_3OucotEZ8U4w6PObYV14UO3PdBz0UffpYId4LjOIF_YXtmI39I1csZNUwkITnTLzw2zUOI5lLx7vf-fqD0YStvq0FFqqI6UNNpFvDfAwreOzjAkpkcNjfp1nVqUWQXv9nLfsWw3iFigU5-J1h-BAyH3eKJctqTenl-KQcJUl8PA3tKkiqe0OtavsOcS8xNCbvT5BCarIjdFMPpLgep4mQvCKqrlijK7jKAy8rkeizPewDVlb7X5gWeinhCMozZ6zLy_ANW4LeSpoL-nU1LdAJyurPJukEkrYXsg6PuuQyhR4xsLmwInjy8ZqO481IGGzgMxH95CWlNBqcBLsrPvOqOzN8uoL6W3ocFu0T9mXBA3vOJP9srtOWlge6X0H_vRVo7KPZA_rhYo_bwNSKygN5VXOCQpaP7jds__1brr8Qual3jlIjPtbEHX9zuroS_dpEX0jrWdEYGFEFa0VgO_hofUcE5rvUxdqRpNxDENqix3uX3QKtzZ2qIbpP2Sdz8BUGelTWvkKKkWzrLpfvXRHQ3GE6buQp_RWyZG0YsIv7zhK7b3s4DVXcrIpx9GpSx2VC8LzRF7r4LImyl-XLHptDsNlbu3p7bt4RauQ331-rx2maNZd9Jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avPFh0yJEhDNkhdHYL7JNZXU12is6jREyQq47mh9AT1WBFblQeOJ9lagkrSQpAofwONGTAYtVx5uDaybsr0EftXfvjMeUFZQo9CXoxBUKzgTQramgmfV2Nr1XNMEw2D1dMnT3xaguXBzgZ0xBBdCZ_DcfdkQox5dhXQizBNIWdyS0Z-N0zRi619t0SkkkKw-m36AGOSI5E9fUx2eMclooBCSJzxNzdhxq8jDe44bQWvK5zJb2qNR8sFJQDv3W2gPB0THxNbnlBgoJQMErHZ8e4R_c3gyOWiPdcUHhq_vBFLKwjJZUleTRT7eepDosSLpF8VLTFqoUHjqJ_hG-NxDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/md4tk9PeHRz6ZpHPlp1lJ7tweBKaAq0xwgWvDG0TlOe5u75fF0ArP3EOC0TOU854RONUQlTePTYpiGUkSyK7qDQFx6chsHWZabTpct-BNrOM7g-wIyl-q_UCA73vEK2DJ7dHFdUkOzmAZfVODuUGQ2RzEWcfa34Y6PJGK5Efz3rrXA1vXycmezzUhLk5bwOKeZMQYkLEAn_Bi63NMet0njZUFN3Qrax4Lf_Hck9txvwHpbywgNRrbrsDmmnr2hzeXlUOZYFVfFk3vp3Y-nEFk5ISGqoYrNPT_MLCx2SDGYSkd5N7Lva1ykT-cVqSh2b973WQwdUWmPyxwF2hF3yKJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiVWs_3nElR_VfhYq5FF9URB909_4IkiUWxHyGeAezNMbN_2L2t9k7HDk2uGqEdjkFi57-why9u8TDh_uhyuPIRBOMIslOx670ON29dZegyGFGvaxcKS-8BZ5tG3j75_LCzOUDd8fkI_fERBhb8SLdGKuAssM_wjUR37LsHe6XbF-wF2A6eZXrKJEi_B5S_9z0eakpiRNR6YKPav6WX9PvuYu6g2vWLNeQkfBuuZD6FO7tyaROh56xdVGTG4gi8GBlBZ86HqtoP5gqth6H1-70pw46TTHbsLjkil8jAuOb4WzO_mHDNTkWuc8v9KSAR7TZ7qyLLaAVcFwn9yod9T2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imO5hQDzJyxk802Fx-0jgmWCNlbgtPu7AEOlsALPNzWMwR1ThdizoatP_UDVqGhe4VEidpfddqErv-cLNgbmF5yDwjXN-vAv-RMpkvnVt4FbsrFdrAQv7u32hy7kZD0fc_HFW7s1nI9pKaG4E4N_k7yyhASt37D4AnxFmB1zO_04oaJCLB0gXYg8Bd6166ru-yKt8-FpafYcZSlYomNS0UecBKmPYCkvnC9s9migTFQtXv5-xeTbRLE_Q2N1AkloVXMJoWIYdzg7N1_iVJj3rqw-ZkmRAjlrl5eij7NqRjwa0uMcyB_DYaZzDAmQ4wuz6a1Bi_84b4LO24xbpoFB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmOxR4Si70lpYPBcHmZfhe7EsF0M5NBRk3TdHA2aWAwIX03mDgcwoXBjg7XK5ygut79wGcjAaa7r5QDfn8mXS0Z9P7rEvJl4-6VSHHSsgrdHPD6vTMacXgzjHJaM06yHEA3FbZJQjMfNf66g1t-O--V0ekxCuI9wx8AAUhVKOkESw99Vcsp2kRdV73OdRuf4PmSQrA8X0QTfbafFcFt_C3DeDrMlPU85JoV1Pnae-EpWuEjfqN-wkSUEHJwp0TLqPyVzsZbsXN85Lc9NcL1VVKMPlUrzWDgUrpaDeqb6L505o46VH85B7OQpU7Kgzgm5xQH-41vRK78mlf8hfQIL6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RBjTL5Fw5vck87eNLc-ObPg-qEUYYpzRvPuiV0ljeZnJ9_vkBASl7NxQRxsapHV0dJHpgV6qtlmzbJzP9uy8bgVvGwBUD7t2OV6pYs7oCYvkv5Q5bQsiF8xdprhYYCHdI-eRhSzAkSyO23kqI9cGgI44OEWoXKv6SSStHSrxHF6ThCZDpknUX80SDVZnMpwTdBt2lM5XFx6fXTkRsuwCOkE13cj82URkcIKAhV6bq2xWiGzSamIlv63oIuuaXNSuvIYcDD5zh9uBedpfbkEucE3RxC57VrTv_LpHs89Xq7Qw10SEW__LHLHrl5YKM1l0ry2rlJmEpCgSnkd7Ox7v2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RBjTL5Fw5vck87eNLc-ObPg-qEUYYpzRvPuiV0ljeZnJ9_vkBASl7NxQRxsapHV0dJHpgV6qtlmzbJzP9uy8bgVvGwBUD7t2OV6pYs7oCYvkv5Q5bQsiF8xdprhYYCHdI-eRhSzAkSyO23kqI9cGgI44OEWoXKv6SSStHSrxHF6ThCZDpknUX80SDVZnMpwTdBt2lM5XFx6fXTkRsuwCOkE13cj82URkcIKAhV6bq2xWiGzSamIlv63oIuuaXNSuvIYcDD5zh9uBedpfbkEucE3RxC57VrTv_LpHs89Xq7Qw10SEW__LHLHrl5YKM1l0ry2rlJmEpCgSnkd7Ox7v2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsV2DEI6HfP_M-N_dBZM5MmkXyJ9J4_5fWuvM5yfLCxUdbgGFMadtUAZpxIWFdPmF3SxKsgILI9Lq2pcfFsmbgZAbQATw85fdVDwLlR4tZrKv7zwJsZvl3cWwhqNppFWloETXQuBrD2PPqIqldmlxOn_ESWhXUsBtFNNR0NNsitV7l_Iy1B_bod5Q8GprqHh0A_emDZnUFNlL4qCXLSRpDMTYnPP5Z-ZjiGWVOIXLA6lpWaL_gaURY-vpDAzXXTkR5pXo3W8QROYyQPf2sNzSUbg-ciOAo25DzcGP0GhEl6KAlij83gRWTCQ7ccTBEWsJIhreP0bw4q52BtQblX4Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAAxB-cvXvzV0qw7r77j2QnjznEGKaCA66YSrJ8T8azGQ3CxzAP7LvpxCfRs4jScpgjDyvSOs5UqZTI__N77gO_ZUSc0lc9CKaeqUr8logyo4EGU06ZzD2ANnL_b8jeXBx9Uvqdt7D2U-P9tA_BXBFqFWwia8BNlassVkqNQkl4n4L4j4w5QBPpES0U28G60aqUE3iqO8j6wAyl_TlJEdx3svcyOtmfS6NdXEb3io6AKb6H1BZ_nt7BV3bVcutB_gSI86qTF_dFFMC5VuwHf_AQKSnQoH8EUPE1oZFZUWDCoi61rB3YvoapA8e_i9P8-ALN2lMTl71evd6YN4yIiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4a8_HTrGEPJSWoN4Tf66yJ2Qq1OyQhPVU5NqskQu3tMe6RMM7h-09w-3oEeJ8YVN73nC1R9xyb5ZCWYutpv8_FnBfJINt_vPJHNb7XKqXs266i7ul6vC5taAHqI7PHcKCdAbA8JwLgnWm7rMnOMMSBy_QtHDve4U-vH22YZX6vQ0U2mlQFEngm0ZDMUBIT8F697ddn1_d_cQ5NZ6VOY7rb61wE536h0K1S9nSzztfsZOvWBnP6lFH-9Topv5apa2kM47mHW4pJ4Ofpoqrsw-W439ykkKB0FSVp4_0tPBRCB3A_rvoOltIzCCpGDUGzHdT7-T-zzxpvnaNv0isLe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUzyKtrlf_Z-1wGrha_7tYl8u4SQ6Iesi38ArlHYkXvig-cv5Xk4LEbdi1KBx-uEpIffP_-L4yF0xo49P3FCy-RMXjhugNOIvu0mkKB9gMZG7xzA-2E0GpMsK2RhmKCt8cV-OdQkyHqd-TygoHJZu7ttksTeptrvTbRXpCXG1vnLinxSYi1UzRkQihLxx8a-WTrzo370VRYhYFBbmrYZbgewIGCGR2pAEL92JyZlcbisJ_MXE3dSfkaw6spRBXYJsNuPPyGzU80YloHylhgZ4uBg6qdLZCIUhWmjdM0x9o0OF_0MUEblEdIWaE_gG5zoQ7z6eU-_m-UvMglAbxDXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z93Ahm7rge-e_rxbblWGCTvN8FUYnt2S49pOm7LQoNIGciqW4rayzRpDMUtiuIFPjqShr5JLME_0tLmvBf3TqhqDA67bzCLVP0Wngen7gh4FmlGbblt0fK0j1hQdw4yvbDZW-hYtQdNCWxC8M754g1OaMEPWv0dZjmGwkyPvoilHIANJ8jNVhNR8XE77exPFN1qGbioU63byecodUDfnp6E3Uw_aRddpxef_7cByUZy309ddROIYEV5zO8JIFsWgEkVaK6CWSaQyzMuVqWTL40lxnokl4-QAzBc3j_3l38dlU13mu2gVZ_w-TizmuXQiMMQ3eNfzqtK5DF2CqGHSRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-w3cg5-VOoh0epsBvTZMeF8xwHNXtIb3akNNWSkaAWunfNZpe5CIioBZv7dFPnKm4ejv6o5dorKjw3xPdWIh4AvCFH9lVuGqEJ-ojkei7nnhK0zVan73g8LjcFN0a4tlxGrOjMKuOi_D3OChW4cZGD8vRJCCzzvp9NylAQmqZcdgLWLHAcmtfedVgTq1_bd0sbqVDndsnHXnY8JK3eiYGrySKDVZ9RF261A-3xHDLfTudcqFxYzE-3Jroc3r9PLYKranYB0tKgS0Xtiw9hAU54CCR6tiDgwz4Whs5y2hgjt5PPvv8cw_bCOXEl4RY7J5eGAdmaxpIOPFymLM8ODOA.jpg" alt="photo" loading="lazy"/></div>
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
