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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 05:08:07</div>
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
<div class="tg-footer">👁️ 197 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 325 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 548 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 978 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Elnjd87oMXBYQ0OUqw-cW-6_hKPPQ0ULi0jnH6b18WPA-hl7KvVJODIwNE4B9x1hd3LExvWhJUVL052BTuyZXVFr9cBdf5WoqyH6cRu4goDJPsIeuyMvHpqawXsgYoT2JISpGXH0qgSAnNIJohuFDpGH4N7QalHdet4B9hFYuce9dVLV5xLJbxEaOceg2K1r3_R13mV93oT6VvnRrAirVreGcSIz-0g1kFNJDrJJZIcA-HtKZRQlZOHGUAJxJOfea3-7x4_pDT9JFkiylHpwNL6WkLTu-SgAbeGNEDCcqhWiddYDW6FZ2vmAFXQoafsjuWcF22dAswdwcOWtsSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp2pwvxCSzPzM60_vDtAw8lgpxWvKmgmMBYHzdrO_3uS2n8QXqEwwXdMBuyC-V8jk6JJy9gBOXxIUyczK-UM1EMRWOOhYi9hbVD54CyB8rBmGQF3KytpEHogGbcOJnEt8nyfHW6AWFsm5SrYvFU2pkoWO9tlCeQ8rEnA-2yaUREcVzwETSAXHg-uH6O54wW7nFu_j5SX2XVr_mPbxvq3SrJIVaaF_HIgaCPkRKncJu48Oohlvs0SBm1qFRx3SfQgnJd4nrg97Ssrzi1S6L9PMzVBx22Pysr-kDNpahRBLSQkv94C_bz7vdYmUsDofhp0WvegyHYgCV8wgUVscx5bsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6WTKUgRSTNeoXfXVJhXCyjhxbBFkENelNPyYrHxvzoQ0YE9kG8qc13rBl_tR_ylUbFiunNJkOyzApH9p7VqG3YRaPhLX1yjSlig5KtqpabHBsjzM8B-plwzGWyy6y_I6m7KSTxfiT8C92GHEVhMoeyJPPqFtLPcFPLFyQkZ7RqSQaWfObJEBqumF5ndH2MZau6rv1p4VZVuxf9c7zMnJKz5wggw1oUZmaFcm6CSkdKovJ2P0tTwT2AguTKmC9bXObxFmG6o5c6UV5qIiwZ02mbbmNcLH7ocm9BnacxW_RnHMKNfNtW0LdoL8ArVWOv49aFTJicM_1b54cAD8VZboQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgYRM_z4dtuqes7BoPGNicfxNweh4wZf-gXMuDpZ1v_KMIpSkbq4jzKLzm_VxY9Yxc6fMztPrDK0LdbWfOG8h5NkRNVNltN4PQA178i-IDemmfntW-SdivWBqgNtoCDp1rGfYdDtn0HtWBVQk8f3Y3gV7zxszFWS7OJ_rs3kPD_cbnjgXca89XpKP5_eS5MbOdUpoXXIjp_q76-MAiDqOZkm4bhXi7t1W9bgohruKpDOHHdub9WpalJMN2vUlCMLDGlw711cxY_51eyAl7f5fDlF5XCpuwLkXTdk6y4sGP0XVF-SYEeXppj0IUcg7BJD9pRIl7XCjBpaqG_W8L3yDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFkkanLgI5eGzQGthvtHUM4KJlkfzb1SSmX3bivot-KTYhrSCalFZAwb4Di9egJ9Xl_z3qiQ7Vaxhcyriuv3C394YNxMtFe4Qmpf370j_wc-aZDZz6y7UXrTljZKL-OwDQ-8C0t-qV5cj4mkE0lqsNTsvT_jizHF1JUKiOMSXRxCG5__jSsG8v8bK6y0dUVlS0KUW3qyhKfDG02VAgeNHZJ8DEWaC5dvPjBJIUWpHPygLk23OMpmLGN7Zp-3EnU4oUy7ZVPL8HXclgp-c9m8MjTsC_nYkrTEELF2p9Qr6evA_H9ETpc432a0kJLAvM0ihoWpyT6rIEjn0Mr5Da8kBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra7Egd_V9W5wlD8fc0mc3InSoyBzLoqE7ZaB21zQRLXyUIfpnOk-E5tYALK6a1IBzpsCIt0sIm2kxxkYn9Fi-yPzSRy9RsYv1Z07yVsCduRKHObyop_1txs0QLGemLHV7d01-8iYIj5HgzOqnSQWlKFolFmc0uAqELsRcvQvVoRFRyKYUDHU7ewE1gCOBaL-g-nrsEO36BKvPUMil1uzmRgoMsPN3ij3RsHuwoVHdA9BM42beKoGPoatZrTVPULufWZEg1qVBX2aObtoCFi_MwFaiGUbxTnpnaCXyzjggbDq-5cPLnpVOgsK9BtFfzqSNSZ7lttvCGeTkIoKNLp63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHu6GEBBqz0qWLLGozPNYxl8ECkNgEUQyCEHiThHxEeF3eOec0p_xHEFy7HtDRqTR236hUBlnwL430Ipv-P1WMQL0p1DXjHj_d0gT8WjtglK_xw42aR8HkoMnqmpuhz79p_pa5wKRXn2tZ8Zq6oca929ZtP76C9Ari5yl52IWk9lpxDDh6521GFnztoEHorJSNGlZ9ozzvuBDNx0GSdhuPeY272MvKOXvnieD3gpr5yBS9hPP6WFJ-tNk5S6ygAU8HgTmVpPqujE0cIcyJsICdte6WyHfdikc6aRYkh0nt7ypQEHNGLtZu9ojK85lUH6piR8_wLD24-8-KNsuFUiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gY5vuCo_9r0_oNyg7k0hdLoDP38nQcwvCVUn-XM6fuOK9cTn-Iw1iGjjcDqAsCFHc1tXsZPXlCNlHAYgW8rKfVn82BSuTIUamz-cMwl1sbLIDAe1EdgVx8fQsKPWw18fHorAULEBYu_7ptli6GDWVsNUswSXL8kEqWQv1AVSvZf21pE3eH3xxRVYSS6U_cSryw4bk7O2ATq0JqY7kfrb7EFVWQE6dlpHyWnIU9JvC5ln1fXUz2AijTPH7a9n9upiW_-hoC1FTzsyCvfWf00mGXV4UCRfcz51JZFhQBrsdTRkF3hM-GBE9GyM_XUi1x1J026E3vQTBMLM8GqZDxhOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfYUQGpKM0nsDkJBguEYkSKEuhJuoJNAjiXv5zKJt4Nkhs9Nodn4PtyLt-UsHQC544NWyDySgmBb-Ib3Z5mNN64QT_hlS358-OwvE5ckO_DY4G9V44rMFL_jLWJ_iLQPh622sSFIIF8gZ2iAuteWJcskmyBtPnWL4SHaRitocYmkPOvsvz1Rp08eyi7cle20HNc1f0wPKhWDj_3EUBhUt-cBJj64xSGkIL-pQmcPoGAVKDhmFfAtOReKmP-CTksQ8fL6WD5rjosPDR37Ak_yycztAItpussMgSUx8-vIYp8BSPaRbdk4GSYfG9MsLaQYwsCc3nTib6nA7_SvSp3Hrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFmMQecBMnSferg0ec9gj9cJ8P3XE3rI_KaeAWSUEYt4LhK_XTuXw8F3CXCkJ2RU_ebQCFzdOmUn18SjGJeGJmkw_fQvbNKw5k_e2PYibw8639O6yzwlPcrqzmL0peGqjx3GV16PM0RtDZRnSOs_PWbJQKbkQG6Bphl8JFOXeZ5QA11SGRXcX5lO49pYA1XZ42ogArbIJ3z5vpqTnVrG6pzilh0i4r1Y0y1Ad5gyQBSB9KgrXFmK_LEc8hfjm2LD00ZZp2zZci3nSy6zmqAeiYc-G8hCjhRL45HK899e5n2BgfLSJ8CeqVCJ8xvW6Da7ZxK-1Z4vIkILdyA3LUJDrA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=FHxMktn2z5nPjTkI8gb3s5Xs1Ubfs0Jit7l-yw0_eGoTYVkUhUZJ1ES-TfsrQUyDQEsYxgTaj7GWPT-7GlLj3IaUmLiD2fvr_pxVezM2PvYiocFb--7NF9zGI-qHn9Z66QYvzLijfFFeQUurP3bi7QdmJk0E4m1aEzFA_ZvunhXNbz5HoPd_L-4kzshtl4KNGsoo1HNHnmqvg_upJO5T4W3Kz0XMJ3Pt2XqPzHhAgOhjybFIYhVpWfgCaPt9MqxWCdwPQWhEBu9KBFeCJpW0ZkIKwdmTEEsCLowMNS1uvHqkOhwrQou1529JQ27NA4MV6sZmYAJx5HK6Yc4n-rnmEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=FHxMktn2z5nPjTkI8gb3s5Xs1Ubfs0Jit7l-yw0_eGoTYVkUhUZJ1ES-TfsrQUyDQEsYxgTaj7GWPT-7GlLj3IaUmLiD2fvr_pxVezM2PvYiocFb--7NF9zGI-qHn9Z66QYvzLijfFFeQUurP3bi7QdmJk0E4m1aEzFA_ZvunhXNbz5HoPd_L-4kzshtl4KNGsoo1HNHnmqvg_upJO5T4W3Kz0XMJ3Pt2XqPzHhAgOhjybFIYhVpWfgCaPt9MqxWCdwPQWhEBu9KBFeCJpW0ZkIKwdmTEEsCLowMNS1uvHqkOhwrQou1529JQ27NA4MV6sZmYAJx5HK6Yc4n-rnmEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSbMZz_e8363mljNwnn_pv5FxmiokKghV6QwCKDf0TYAro1qLS60zlTRx7VTiir0pERWSUQ1ZouGNNIRx8DWcQyij1wWKb7dPGb1DuFtd9lRyfOsu5IIfLeWEn3FWq6-sYvH6r7Bwf9RuC2bJKrPebVMbwHitZEIXYWtdDGEqV3whuvhkwQdUGJB6GKzSqdfsF8CdOHwPFVtVvG6tsba9st6d3rPD_l1aUdiYnF8kQQwIYZiqncYv3FrSpLP7vWDTNPlyUFbL9-AU35B8K_5rexYGeDcGvvnxmj_4N7VgxFIpyH9Z8Nvy7ijWLy8ipG1xLaFWQUc0gQL7qaUISZmNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTRQ-ilv9b_yXYATkifWjmWsYm7-hsM4ASuF4Kk-22HrsWBtmS9rGFYVDG48MmZej7KWEzvSKAyQxDrBbNbQ3dilUKO8ItNqkZZVVf8kzTSw10oBEHaXiW0nKm732RbwxdFpjPay1TzTxtNT_TqYs-dCVTzgeQbO4Wy9Y0mzGvcbjT6AnwPqXaneNQIwGt1-vTx2yrNWdOS87Doxfox2_UX2FxO6MMSc3Vy2c8qosa3AMOurWjkR9JEpOeINYNKe9O6RcvOyuYJUA_xLILmNN99bwOMbmTeVDnziRzpRLu5nAn-ra0bDUlymct7GWZoKDfj2rPD8X4HuGwxd5iQcTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Adx1KBtJkX5wa2q7YPxQZMs-_Ego92Hcnqe1f3rAyPL_tjQFfywC62-AJ2FXSTZCIgEC8mjT5JsSlz6Y1_5TYKxmqyINdwyGKyrtM_FUiEGKP34DRfN2xHTy9rIbNjRYAL1Z9Ya3xEX4zSAnbEYAZj7S51UogElzUR3dsSsbA4LN4qx3B9jwRSyKQNVQlnGwceix-uHaS0ypPJoVhVvXGsOZF7KBc4STKH_iogRGDUH0NgkBBsm0xvEWCH8KlGXhsRAT-9niVGY6PJktJru65GFhkQlritjZNNlbqr1nhvqHooLn5ZrYImz2a_uL0_8CW8uDlRftvw9hze5YIFo0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBS5qleXkwnPo8KyjBDhgP0bPiTEH-V0K_0aLsvR2zOtkTcEpYRsQRDv4klyRjTY30F081w9lwASnvZm_MWIslauEcbYUcHdK1O-PgbaMfnWL8VtVYG91g3I-kg9SyJXQTKJCrYXjyHxd_7lxPsd3-cInw6DyoMl6vip-ryC9HpqvC7CtfPlyNtyq-knml49b1ht5JHoL5KgHpDkHM4-_SuxuCsCxwHKB2BsjLSQFHhFXnOnNEX8wjYmI7KiMmi92Rr8F3hSp25ee_0__NVini7OgyElk4nA4BvC3BM8lHHKvDYb2GBQLk1cbfencneoc1Ec6-gzOTVI9pN2BzUJGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-lLCZ8nm8Qy0mzRHPdr45EJtMSZnOB2rB3UXytcY0nmOZBXpJlS1kBl0cfRrrKLnFfScQe9HCAeWL-wPHey-nQ7sLZ30PdyJYOQUqIrxa1OEvYMigqL03VRTBJDno4FbLOSqG-a0x4Q7Cd1NPx_igWC0hZdG2-CrCvv48eYIBAJrjrXIVGV__lcNjAOhmqiSfH7xxHWsRzCfKIN7Vx6PGsrZ79zo2xedA4I7bDBFiJwmIyaZ3v6HWzsZ8OhzcDKis1iut7blGNzqbWAXJrTUO-PtixkYn8t0HO5rkrYZQ2bf1A0e-kK3gp25V8qCTyRwBA8RGDfLh_xkV6bJc-Dnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPtP_JZyyJ9ydlrsAdD1TloHNL3zozRORBCTFnher514YjwZ-aYI70Da0yiaUD94wfThamezyf5nhYIqK97Ixr8x57e2V_1DR0bwj8o1IidHza2j8I4KKgNYGLNfEwFoaRyeI2LquMKjdkyrbRU6i5zEirEiHIae0nsTKE1DlomlTdGwvA9Du8nknAEOJa3gTqB3hBe8frgwi1H9erB-piDwxjc_PKtuySO-OCx7blicAD0pX0x-lKPrGqtkX6dPT-cNqUrr6SGqkCVW2uzoJSG9ehqDN4aDOKFZp3Ogx5ywqDeseWDKbMbw7L9yvQNmKfYQvF8YfXFMrvhNjjrWsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_CvVBsAbqGn9E22CqaT_PwF9tCTcZsbuW-Ql_Cd1lG6AE445NXcOvg0Gocdv6ehA-bn6t1AsdrordrAJ-mpFLjdlS57BGuxmdhgRUxKlXgbtN84NoMwzdmap0aNDPbVsFGKlyuAktBFSlZWXtyDo6SPT9icCUaDMAzcIzu1zwY8ukwpxq7eSkyvSqzXM7PIqYgOqkO_GWrQFuyiqjzQi7vQuDxDAls8084f9hRObDG4_IWT3dM7xMbINwJKxA0GMsASvueOBlQu4SQBergBRXqpkmYzpoF62E4PCvI19954tNF5CeTdQ4N7kNsc9Zo8b3eokoD2Z3Eh-pfpnKvWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StjFzgZgxgQtTUHPyntRJ3pdo_kT-eawHQ742JQR1F0slltUdPRP6ES1L8UckLLmWmoXh1uM3ekm_qnrnCUiXhnxFs2v8_QM9kKOBE5We7VU0iiwSSgBu7_m339oPegCM_OKqDYqmgJPIdHlz3YKXGamK4xrs5jSc6WLV9EWOlVi-6A7nJbpIca8ogo6C8ZjuAge8ceeDBFO7K89yi_LpulG3E0TAJbPP3OAsrnBPKB4tKJJJOl7TDbxQ2TWk8y6RTKmbemRbViggKk2DuiKbyh_iutIkMxNq6FBOwUu1TJNuugTdC4lfEpYW9wE30xdtymAJjaW96r1LC_P894Qrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lds-8hcDjSBjKIhW9mMM7THES0OlmEtjMdZQnIAti1R660Br8gRZHywcYhVsOlVQWvaMwuLjqK6FtjNJ5mEOdvYFfyfg7mgVObG7M0n5Cem3Emdaq253lj9KNPrZuhyEP9xbY4YrncB1yBOAhdmSnBj0LSBX0nGzfd4OqdupclPA367GAg4r4ZVMIh981X62UYBizMLEm-JClMmzQ-G_XiTw9IvXxWiyiVjfyLi-neGVpX8V6uXPvVaWDaWh_oOTIbu5GfrOgFYp3ZGchMLcZcGuFF-k_RnT7ZzcCSQJkU0XFj2nwWCW_Bq8042Z_pEBPUVxSWagdhw42Re9jfDndQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj-K9s80iHZ0gUesflyIj4BuxrdN2V9UhNya_HtASaVfE4miAmpkpYhuOXmuOLZU6iAkd4bVH_iMNTNQ4xhX5VkA45nCEUoZgyzNsu41hcyJwCb22zUY45oaq5k5CszwvmeGlIWCGFUgkzMsxEaQckr8wisYiwDrZ2bKtn4gYVMfjEyOmdmaCHr66eDhEyxABCLfVuBqtx6bAU1W5WPmULx_9Nm6_duh0QSaKoU7gpeK5hKntQUaDmGt4MoHTYGG3kG1CliMAuZJ2tznI-XTCdW6FugK02Yel7PIVE-wiPlDzP6mfIRBWit4eOhf7oPqwrAKxjlwFVEIaJTeYBLTEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_Et0jDULhm2n1jh4MhP8ZDU06CW0LtrFlr8yFM9cIdv91O7AD0-DLw9GuglsmeD0PXfzsMGBJZT6hBjl5ja7OdqFW6i5S6CtSg72zo9ksVdVsotq_KdGN_6GuKaV1GAFa4mkMYlRTbMx6q50XwOwRCOR2MOsfi7pZpg_ms-YHR5_Kfk2zG2HrrPKIK-c_h0XCznYajwYgSjhvMTe4c3vxYl8S0S5lCIYthbhOFFSqh4goWCOxiEaCcMmKYiPEh0YqVhahUJNW5AULwPHOA84y3qXXra4zU5M6T8cCPQluQxv3Rh1eiONQph2O1lJ2hLpZuQf08LsNuqfvQkcgr-xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGNB4RXqYnZ-45NmxZuqOwNo2SrlQSmbShcEWWDrtersNLyl4jpkZJn2zYnRQ40PLPMVVcPRz3UEdgUpWt89ZST_vKPQuayIrO58QI5XQoaLay8anuFjgUoHs9QSx4Dh2FEUYtcYpQ5ux_UpciTjmCHi1y_90dJNWIHETNb1ON2eSvFt1NAsXLjlNeDncDKogtkG_Mw3EgACmZjvSS7JOmcmeaE3IVTa4YUqtrvKL6b069PuG9T1OHy0zggPI23YO_rptV_mQMQTNISfli0defiodui6L6I92T7Qu9qFUM-T-C_9EoVwrYWmhckmjgJhLT4sX0evvn06ZeqBx-46Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFcPWc9x7lbMDI5Ccw2qR3qXJMuSx6_813d8eTNoB6FMBpdWVciLiVYfjyahTQYELAr_k5rEF-7tRN3JUpAUQKfwhTPrDpsiFvyc8vDcqrrgfFnsL9YDGyLJCwe9sBSPsfrUuFHbv4Nfewa3vDDntv_oP_fOJQYDT_PI1lsmLJhyu016U0_aFEx3gQkG4lvKJicqvYsalCkeU_oKAIgF8vt_c4iHmne7lNWQIWF5CDVkpNwPu-pLvzZUAFePbdBvwp58cR0y3aRBxcOCg9rUUHLPsKXB6kbvfC0CIRTh8Qkmg2vM5PBJzQnphMZummLw4GP2ABqNe2eKXB9SyBUM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjKoFZ3z4nkKzJrcIHnkOVVr-8AvFAHjli5pZcfHGIo-FDhDQDGtp6-v9FHn9WTk-nmVuwuTQoS7lfv0Xwy7glIim0jaRkFtaKOJmuFoITTCcKsCxNQkuccCGU_kLzEOWzfRnFDDbELpRbpK7EaDxChFox8nIkJp2SRprtJrW4d-addq5o1CDbG5PI2ngO6dyoQPMvz-0nSROr7X7TFyJulmo9o5E_ha9u3ZnBHnaGExuUsPyN5AkVSq3WagTGJ2PSYtvl1jbkcT_EfvBRRpt2PPLwjHOOKUnRB1u00uPOES9Pn-arEC_nUs8gynBIeDkRmNmg1GqE7eHz14J-xsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2Dts56qUmqiFP5L0SxteJWCxVr3iXfnw-aHWHTLbz_fYGWp4Cv8iBEWXV_uq83lneCCZm2z7DU-m6VcoksQWl_XsBboWF4OCRVJ25k6a-j4yONy21aBbV_EorGxsUBr8fuo-kqir64ZM4AZXqA1njJhG4-sDH2O6mwTMaqX_zkVqQ1TXP553AopGqIOG2_e9uHFQy7lbI_1DqD9GxCYCjvfkr2K-RaX-kMouwLd85eo02k5CVETpBvhpGRtU376AcnMoy5b_oD-wD1lWpwpe7lRslNErPqCTt-8BZ4tuLtlLzPF-H5Fb8c2RtrYNi0aFe3yt7K6iwhxH4JkS0lpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2KRLpwuy6viGH-X-ldWr2HiKjoun35jHkVh9rtvC1JK-PGUhIs6yNWCM2yZJo3SZhS6sGRLMMk2cAqvO6bTa5Hd_xu70NVjeiia9R0ITZi6E-ibcWupY0r4D0zgqmg1WnC10h4Qr-ligLr50sUTBkhmjIaFVq47qreft3iQ2JfEnD_1IjgW8IKsK97WUstGkZSWimmi5BIOfFeSnM14w1zT1ZS5mRLyYONlKTvArEOTEeqfP6sxqAzpGTKOHqrJein4DncNEKLrR7CbVTdF8ipwguH_ogSdQGl8wuXn8csUjecX8HUd1x0lJdcQNbsagFsUvMLyZy4ML-PMYIu7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1hxrPXpz3HAEr3sL5Rc5vIynwXcyyT1dpqNviL4JcBnip-rRPazZB0kX8m_mb0AHTVl-xZGXZOHtixYu1ltWmyczwKbjhNFBFyOITUV0Z5xYbwSbkavahWNHkjEdsG4suLhjvjYYURcuo4F5XgnUgzcFI-KwaIfOr0SZlWyLlLDL_AXy1CUnnu5gfnpuuCKo_P0TlCusTc_BHjohWNWjfbdnsmzX5DiPlKbi-Hc7R8Vy-KlIjFfWMVP40iKNHVBBOrVAb-N7bTtpl0N6y_ft8MAJf_TdtvSDN5c2z_8WNdWj_BjrFJw5ZPeM2e-sdeavYMU22ROtsD42uf6CQZwHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0TqIICi5WfrsoyTvt4Lh1PYWAcjtlfcbl6a9YlljuynIa2_SSMUkSy2cyQ2946GqUyheQ1cGSEWoCuWhVINSX6or8oASsl8cASdzKcXe_xSlOBCZfrGuDgtuwlo9rd-mmGhJSqGymr7aW4QBsiQO5ug4o6UyTkXCwkTPn-NZya6ewUmfL5_yq5qcyppmds8EPlUH8oePWz5p7kEoTUuKumnVHWWUtt8KCakeFPGwd6LEhKmlHTzbJIlYu2ny76R_ECdq_qg0ER-B8gfQnLu9hirh2JL8IgnLfc9Heyp0DJksHp5WoRPCUAAKPXMwvxHC5ykHpuObmeY6pOY3pa2Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N45w6_vEb5nxYcisQFYWNiOYEUeYHZj6KihRnR228lDADRcQgYyPIQC3rY9rcizHli_4XDDFsDhFUgHhvipcvvg9O1hMwqXtLqxLoRTY2pgeytYGzmkaP91Qt4wGpN6E0FtsX-72CstVV4OBeRF-QS3JvWeEbQRQ5UkmmF5Oi_AwIyx-O8HXZFstC1EOPnitpHvR1V8zklSCfgBYe12WaLexX0wX33VNDHFKBOq2T7O1PEUL5F0U5fnWMFr41m9pNhp7oMzcz9Dmc9T2kdZPyg99FA_XY_xcEAvtsDDQU7O6_GyXNwA_E8pjKkS5oXKCM7y2BnGSrW35ec9aIaV3kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYAGLA-yD7Wd_ED1AOoO6MVxtklzrPnIWA-j5QLmGG-RKuY3ddKsgk41Ozc6XlSrtjYVuGRPciAazl0ZWkpACiz7qpxwPHMcO9IMKxyoGHAWKOSM5DtnlNQAoICeOOqhnstgB8r8gTcLH88vrTDMB5v8mOg-ZKUEUdLhNkrRh0zOi8gMyJnK9uxEZuXLnDhMMC3lbxfV2u7S387lwqxsbq0VnX-A_JBhHsgm_qY8wBB5DWbI7EChOSM3IWIXuh_q69YXiWo4SnhymkNygyHQ54sw3e8eAnRgZQxlPCoLMOClt9Y9lLDVTLefSfPsXJR9MWxCfZllBVRK5vVP9COgAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYYWW0nvhfvgWdYiMwS4E5arbpkZ_pDkd5x062nIEDnb5oUfQCn3pe_t3kJ-hp-YAd3JfjDcrkCza9caE64yC87Tu8DKK1cf9sMWmkZz6qvt3FW8766qoq3HXEnfNq4aan2SvE9w55hQMpX4fYp2QHgVz5_4eJpuDXeSHivJBpDWTSpOodRClDjN-WjWT5fsY_OKU0XjQkLV2Z_bONDfm2TJQkGY8wujBFtt8cFpkhVcxruWVnmspPEtrsU942Pt4RVXDeNB5S-UgZsKbJCz26o3D6M8iUgXvAz4JicpbDbkgF7T06-eHVumfUY2WglEJhBwrrxSTGxORBo-mr8l7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z21dr-5oKXe7npGjA33Au2_ty5jLfrw0Yicn6wYyY5Xr0mPFRst8XFjFDYT8GWLWZeaVIQJ0gxnOZohMeEtlB9YDvfTHxt-bmevk28vKdWBkWEwzfbu7ieB5MOKwX3i1rgJdmTkFsV0VLxNVhvqsPyuWjkQSq408I82p--9tKB7x40RxNxpF_m_wg5uLS23vB2aCx0QIUhSWxKkrHWEY7572xZb1o5zDPtnt-4g2GGKJBO58uJ9vCwMhMxUFJvpKi_h_1YvvNUEiam6tyTqJUQU6Id0c7jcTjGWPAbrBOhHAfO4Cn2hT8puGJWtkrMi-WXlLou-OFQelOVw37yuLbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AppK1BhD2hENE6axeiPZX0srp8vKxOeNJb9HK74iNUyRMfnQMyYd6-MGBwJIADxTbihBy0mriAqJP5qG7qc2SFRa4DNMQ-6KE_5a_JTuP2qUD_x7oPbjNLuWjbkf8mgd7gHY-rcHZVEBHSFDjoKiYQCGfaIDFpjXXqDPc8XQX8M_VdKM5utPsDF8-v32wLUdnN1-ivF1XLQjlWMpDqp9Mjneb-oDTpXGu1QsvqMlXg2sCeqx9-xQY1y6a9ftWoRFzv6B5QyQ2AbwqxP61hBe8WcebuAEbeWbkyba3OhN_F1JfCkNeIXaXrART9PoT_KncyaZ0AiivDugP-pNpP5i5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQTwmHeQLPbRXohZDV05IsckcE6OlCKXp7iERJKxow4kLr7o2EWdSIHC3TP890zA3heWQhIHJkjp9sJp9FNt1_95SB-FbwWZPCvjBPFGF8Pp6RRqom0gm7OqcAgNtmwqfVAmpkD7byNiwhM0TbtVIcTcNR2jdD17TjUlRVVhyMfy-IyDpnnLI7UKq61iVJLiYrlL-7_5aNGhFlhZ3-qzKg7CcUr-ciZ91G1wVP5UX-DcFxccoFm4EijRkzF_VhfecVLOHTDWfE-WGjPrZRX-YuL7Z5MMHyKNQhyskYPSnjUYZHX7dvakDPJ2l7Tcg65bk-PhBmqouiqjqvYZPMfn8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlLZanp-x_nLXiHfVPwQPbkolEQkp6m5cQPtvXtghnjmPY1jK5zpbep9mqZnq0wfjDxXpANmKZS6uVVhjHSPJ125GqpwBLRznellzQ1rCZAtDbq9DuVwToUmSvwl36YcHash6NCrmnKkdMn-03XH7El9dypNZ6nv2lHHgUvxjXKXhTK3g_C0t-wxLhgQfJ-XoXol7sJQ_w0YvrlHrOKzKEeM9-jDUbLNGkodO-I_SQ22t8qvILKap27_piJv1KiNbLBRaKcHtNqOcJ0gTL8891zCoMagE1-wt60yvTXoPmtaQ6Cf3lqEoqxaz6uAGaihAe6zv5TKsSfaZhifjmyRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_OhfYiw3tyW4agCkDx5MYhtKfQAnLBdBNDdZntZ_nD5mozquXoOH9RP6-Uj4MoUjfCIaQ0GjSevD3HNlRNdxUR0EDJgAyZbkmep4O9zfHhezGxuN8UUP9YiAfb-oB3fQcW-nm6h6HYkkNDBcbE3vKok4sQIi4QUnyOh92J_S0Ynf9WPdVSJN3KImV7UtxkaVNVEln0_XfCr1cOJAnSYcRiFxU_aBPgFoy1ngN7bQOomH3aC9YdCvS6DGpgHLGsn9IMCzOmtQgu1Q5u4hJq61raqcLpYfusNvLkfN1sWNDXi74Vu8ZTTYNmgFEnkDt8fI2qu0FndnvRYoej83aZ5tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5vM1KymWghLTp6q9QmMusOmvNMTbhUlmDKQ3GnWHDhAOa5pkdP5feEUEKNQGPmLskKp7o19ujp3al1eG7-yHLQ_Hz84zlhcKWmbF0_3d-q2FCOA40xdJeDzabJgd044vFvl4fUfFMBUR7zsEPJGsqiTLLWPjVWn9YQKx5rqnkQ5n16cdxSyHvWMbhb-YcXO6niNp1dAHzuAH-PguHRPMtomR8h7yYy08GFI4J_RdoJABYyct5jkJJZI90O5q3MXGvkD3Y56ams8ERqx_BRXQ7cq34ndoniXb1zTAbgI5MQQn6PqRHnOasi9bB6I4zhetUaeFV-5QMyYKKFNkvAwCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMl9P4LFfY1L4eFBD_TdIKZGj787WtboVB4uCQ0SbOLeDwvIiWZ5HFU0E5d5CFshxxWRK7W2yNJpsyN8t4ZmZuFZbXV_xxSL9fiXSnlETNkeNyDn5GQOyITibXKjkFpZnN8qdDiB8URKol9fyjiuqKD1NOUkH2WXa0S_drzebeDiRcW0Rng0UQPiGx8o8BKjKUeM5BUUecBI4j9l3mMTbFU_RQuBYY3nF5Ic_TX-RldgP9_yFhgKZ_v2scHG1VR8LaweD5CGrTB0uJA_bSmxuFPs-g-FA9kUDG_YtAUMuUHniMuBDrP43YLEG1ZsYHeNg2LF-Fd_5O9ywtKZBcz6xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-xDUzmpBrO88Gc3YDC8MdI9X3YtEX8AFHbN8GK-46bC6Mbxj6TGoHUxBYtIEdwKF79I7k4Tu8L2PWOxIPuFfWcvstnVapyDyv0cnDFEprBjn8VZovzMdN_eaAeWoXjOQNI2b4Z6sBQXEpLzWwaqpw80ryVEV65hntQ800784Y5gw_902xG5BR0x_WHnyr6jP4aUTwbtbEszECPrrh-xt8A08A3IIQAfTNIGIye4gvCuy4Z7Kp-XUy17kU1mMYhFf8Ry3Ci3bRXvh5wqjjisndecLPxtrDI8vukAKtjTNJxiLeSmlygipb7XWOgh7oFQJnHvC_IpbLC2qnBrs_FAWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4wTXb7j3nR8J4e0RXesuR-9vMmADyObbSszcYIBGC3RxoFlFaviJYq0e8xitJ2gOo2qwZPJvPOB_NWwL9BixVoqICgoGVhIlcb_hiQaFw2437_HiqI08O6srJlTDwP2N1wVaZ1amY_lE_TM2vkqN3fxSvdzToNkcFrBv9fXlsSTZHUaDmD4_EXBYIrrQYpXjaVIaEzbVtcCPOrUGOtgEMvncoyKQSKITFkLlk3JxeMfM0ahX63cIweRM5VLLloh2ndRVzjCjhErK_kInN0fEy0ZuNqlme0eWUHFD_mUYNCV1zpyIGoXI3Mt0H4IqwWW2VkhXNE6yxLbJ6g4g_od7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJJbVV0mDCaSmYp1XLWvP-9PVCFAw5U41gdHIBKuYNJUUGnLFg9yrTkboaoeR6D8sk_QUldQipKSvL__Pxj-CBrIurzEETO2PP8qdQREOlesPrl5g2-mZ70qtIOf7Ey4vUkmSZ6DpFvYZkjs2O5nBrmxmOW2K6z7liV7BS75vtol3CkoA0CDM-hot9Ozel_L7xOtiNO0N5BhubDDMGCRA9Ek_pY320c_I8IHufgT0WfDwTcHXLq8st34MjyTJZlRapYWQ82IhBQN5271Op2ntXtSv8TQH_HZ3Itc5y5CIbE-KlHSCohp8wARNSB_WWL_LkKWS2dC17oYE9yBAOJE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbV8dbCdhgnqmK_A9QX6ptg7h1xTjVcMaSzP9IubNxlXD-jKKcuHznKrALFyS-M62se3ZPl2V4QXIoBbmatsp_eyl7cJ8sH7B1iztFHqqPCTn-z68FEN4cB0HL9XERXRX8Cz-MS68gXPjDSaZCCguPpdhTSzMwtIIgpL1TJIYvPMLEBRUw_E6WhbFxcywe9WQx-ZlzR2H6IBGVBvjJ0BITsEhfskSXZWGuZPR7WRzznjTDPKzD4-jE1Pf5eR1T6REgRcbja2XlnNRefZFo1HWSD5gCeun1xXEoEdB0QRz1ya2qE9B_kejOLQhwXbmDTuu2wmusmNsiEru-VFNoRI_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcK_HANdbFb2n0dj--9-IQQaI9MhYHsTm6VqtwRf5mZdM12Nqpn6Z1U24klXUu-_A40P8O5AW9kxWf5b9ZSxjuO3DkFK341-RfPDvxXgKfc_-lL4EOPZu5FgQMr6t9K26b-DOB2NHkSWGhWgFOVj1zBaLZqq8Ve94m3tpp7CfD17TwUKbNtvR2c2jnqAl28BWrvGs6p8t1ySeC6qAFZY3HwCGKRo7_u5Z49xQ5a8QKHexTYAdgEuy5JDPrsygmCnkmVGewx2zLOBZBw0rusNCGr0h693hFhzqnwTX1KCtESdJ-LrThsNpc-JbA_LA-SMDKiWPBtC7NSj9Xv8GPaGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCJzwKeuhljtSxtxLDml_d4lUNf76cXpIBQsjp67SIjbxtiiSdnKE1jg_Uy5hI2IYjwit5s6MrXxVDawHBC8uzJBCW5U6ZBNfvr8HZ8mTx-LcO7onJhH0H7BWQsS4RwCBpWXHC3gLz3qMcffS6mc0wRh3EI9XOStiF_1_TptyYSJ148DILqfRtKcuAV3bgMx0Eqgrom0-ASYOYvyqbPeJxi5IPF-0RXuenmfKy91heqU_vDgj3sr-JyxASOKvZb6s43l_oB_HT-JECWuKRBVPvZTtqMaEOejx9Ys2IIFIkD2UtyWcXZNgw7u5oEXsuBPgfYYJtroAoJkXCbxHtS2Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCngf-3LN6IFcgB8y6N5ou8nUPEn9asi3mIPYIz4Mozev5dv15kEOVWkgI0mHUkw2EJD6qOZn9geNn5BWIc_Yjm3yqtI7WqMC-9HIRsrC2etDGJBjy4tjxdCtIdRb4H_5S5BwSaYpjuXEYdCLA0deameYwS3aM_xAcdXgJ3vPUVmO1rw3fo_o5n_rRgW9ng9KA6rfoICyXjQb3bZkKiigGsvhZBqU6hy9vdkrF0f3gmqDFH59ZZDVJe4olR0bEFYYRTlWaycBnW4CUyu3eS6sBvaS-Nqh_mxCXeWZ_0LvClxtwVt4mf6bUQ6W4WeOOA3tor9XWAI9-WNMzc0eujuvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwzQ74-FD1IiguWX5cp9qgJyEpH0LWVsAz5ztXm_hD2hbeTfvSUGU1uteXJ5B3zERAl6hC-GCt8A5dUp0A9IV5GUhTiFF5-SiLPn_THNuvsHZuIh_OYIFE2_GDVfXH21Lsd85rDbJW1RkNC16L0TLHKH2O3T2hpf462HIBmS3WvjYwoFYV9Lk_j-vn86MWGAvgK8m4dH6swNwvzJoG9fMzxZvVvYTTAMeJ3GRSKNOWeKUYrwiUpeU00SCwciZBy9x-qcUhNFknd3ZSKeetD3EbFxrIHhA3J6IhJGFCE2UyP9kdHckLdgEqdHPbr9JFVGUs4xSoqpHaYd3Aot48zddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krJHZe3VLmXtunXEbIIhPrxa6PkwslFWa5ATPMVGKmh2-k_bRObDmTzrkapXKK5KPUvIkOMTGUDRgCTisbDAtlAMTpHbPz6lh__FYIdPAq9jRadnd9fg6Lu2pHz28H3QYLEplrHRLM7m4Xk_C0w-ROv-J-8AbWU29fdbFyyoVFzeBvHLhrdeoamMJyOakHlormikojyuLHvc2F_kKaBRIAnZQBxSBJVZO1NKKYYg4qYaUXcetezSRiHTp2gE2wD82WjH693U35-sg9RH_fNO-rP7dGhYRTNMCpERUavAgCuxeZEj4CRRAuu2MTQXuXrb7kVF3CaJ6bvH3lEldeHixw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3v2D2YtD_eoDOiYSsF_WJliuj_yWnjI9T-2ocxTKpSoGXMI0i3M41SRkp3ugZM5D_J7LAXSSiIWn7VOBAjfHdkmHEwI-mY3v22h5LXCWi0bX5BgZmmP_00O8WshZ2L9oJQ0gX2sf5sA4iUCznhW2wLCPErwM2TJOHDv-PPnO49VzM56dUN2mBHguabArMWt2Crn644GIAywjRH0nSAe_O5K4nUuDOlEtOM78WDKUfnHHrcMP2yqLgZg-bmdqlYt35c6NwcHhac0OFPU_QiFgNVs9BjQJIOvzxlkZMcmpb3LA_8m22LsLYDKc3TErz5egos12e1dcP5qn-a2O7POUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH3McI-CCYcbV-GhF2fDqJYFez-hHLuWr7Vj3n3aoKwOl0_w-4XNVGMJbaeT9exnL4e0h19gSpwx7GTZ4GaLFvvhaD12EEUZyC4ZUPbmyQpIUTwuzcVoa0JWUyjq_mZWCNMxGwijneyIyk2YR_eLNOewM3XVnGAb8hEsgoY-JsipvpYA7CoG0_z8ICpQ9kUu5T7YWwTFeR0i3PH2w7AlQoXdxv688_sHw3s19njH8aXthVsva2wREo5a0FrahIOozCcaur3lmojc-svdaIWmqRl-LCjMFCO1ozCWsP2rVje4zaKuN3B6Qcmtl-HeRsmOHAKus7LbvFNdq-MBsjpTXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM-0TtC_MW8Uk-VwRbDxEgRam0oDh7GXXE7uJrQ8DykCIFirF-66K72LnKlCIGhw3RgXggbS8lPlvRIxiDW3zCbPfCme4dq1HRfvSXcP28_oApySZ7uavU8QhYyI87Vs3Dm5TuqC0YIqI15gvwI_Bn272EyNZSz33Woz7V5tSsJJ8yD4rdEEHrAC4jBxBn9csj78mOx570EsN0Sq1XBJAKRm5FLv-XM9rJm7lK9aL-SwxN6EAQpnlKfbxevtFbwBIcruEdLbW38XGBRE4-oFttY6DzcC_DYeHzRO9F9krUdVozPPFp4Ud9fWaQkYWelGFxc_7wf_UuCMWerIYvfL0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITp0aDoHK5hkVMlJHOQVjsSlNeztr-YoF8DibXpjSERf3mZkUhSIZUeai222Jz1l4g6dCxQ-LPITG852CWzauQhRC6qPwu2F-tA37CS0az_IAbwtElhMiGiI2-zgl3O7OXX4EXUy1x5NqmNxoTp5RL1AR2z4lYa92vkqiZH4zJPf0ftOsKWJzmzzk14Q5QynkbpE2CL516cFJlREBeox582D6U0dJIjdpMtPPaBJ85xqPzoL7xUP3idoVQFO6wfV1B6ugexOmo4bEK4yS7KODg2QNouWTUgHW4_WzQpVCd2opA5j6XUDpI9uGGymIZU1alRTTsyDG2LVdpsAvs4aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km0DAClO3rjwf9SfkSwc2T5PPY_jS_g9by5CqZ8fxQk5jLbKJjkr3Ayg_Kiry97--2QLkSmbHK2WWejW_GrfGnsKKeoxOcCkKq1xFVkm6bSzpC5F0qc7VA4VcHz-rbxfpkgVbFkgn2Z44ipCg4q-s0fS6hHlTVVL206-WqPuG3n3PrSWcFs4sZ1p8ciwihR0im1wrhB6rlc80Fd1eT7i_gyRKV6IJF4ukq2ZEDh0U2Q_Wulx72QAUD5Bc2DWq5SAoJ1oKvrt-Rt2KhEtYY5Zk830ixQTEysG_B2NPHjvJVIjylzUMkcQF8WaXyBsR9jnKTAji1IlZcqW93FYcUDqzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzldT9BbZNoAfv5ooLLMjhnZkB-Sl8E0Htb7lFY0WSy5qVya6OgQmBCr7pWCEmy68S-N2HVyJCJnmPXq8cgJFNZBOaeGTXEZpLZp1lh8_bELtHBmW333dJubQm9rA7N_9iYzsZqGLCcXW9Ri-Kr5gwVCclJNdzdJ1ewDic25tsPyyf4qdgwoXfVpJCbmDg-NAd7TlX0pM3X-I6m6w2Xrk8IhC_bV-5pja7LDIkbVS63f0eorW2Y65CAbBVXm01l3Ud2S1JwRn1G218MJaZteupwGa_BWa04H7S_Sgi8MmDVA0iNvlu_UFyyogYnnYTIEMg34jUqXVLv606bXrGCElw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvdIRgzJeQLAiUkaSWz1Q1xPpJQGa3mfXPPCygUb8Ht6QgFRZWOaHCFR7wUm0g3SQs41gJby5OP517hYc4-pIoMEUNJTodBqGEOiED1NQoJ_qIqrqivNB6Ph1tGYFx6FgRZm-rJLR_siuaTTECtHXrE514uzB7vK0me6_yH1dIT5EpryxVxGsfzCV6Cluqef5qGE6RivZfk--hVSt8f-IOyL8qnUEY7Tk5vMf4iuBVY6lI0uRst2k5mPRY9z3CCr5bR51BP4LB7tx0XFPjktfiQ1rWeZzb5NZJCdInC8Q2P8NAn3AUecfDvZb6FsPRihcmaalq9D148OB8-tsgVJ3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDIAr1k7Ia9rns2VEIhi0-GLuiH1RHUOLc8bwsPAn0HQbRjshBZ8NbBdv18gITv98Xr75Cecy37I9zRCK93fz3SVzqv2uZmT_-ywXdM7Qc0BUucwNbEEgqGlGcoSCqH8jfXtr8U0D4T_1SohEcWqrlIzUwyHX8MFdLdunHF1Id0jsyN2zc9ahReCoZl1Zun4QYbSDnciE_Bfz22iFi0_f2cGu3oRwgRY0G9FsBTP4Nbhjn3mqpS7xpdDOKWzCz70Pc2gbcmUhWa36iFYrk3mOH2Iu5Aq3l2t_S78UUHw8--xWEhlXuOzaU5znhObHOv6P5pBSQWcANlGwyomw-wkYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_2JhMXKxF4ZHJGPAqPUtz01ulekZdYKrbxIMbJbFueXN4euXhNuaURPferjHoIk1U3ICP61VyFLbk0r84TgfIAsRqdMcO24x50Zy3qpHx2Kdy8RKl85fujgSC3lXiIdNg1z-4xf0caIqVWmJRL4nT2SHJgrCLOtkwUlo76UV7C_PWAi6Xzt5LRQqv7Cimn2_bL389_m9tI9T1vxpnwRMeoIA6_y0Wab2Vu1rMlbsIK-ELpXBcdfvIJlRIwkf2jjDY7RWbGcXGdFhPyUZU4c6FD_EjhsXZYlc_sb-JDNMkK7TKVk-nF0deO5cxJUsdxry7GOU-8h59a681orgoo4nQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=vMpe7yHJfc7m5QUpdVrAO_DozN11Dd1iR6ICvJ2QUhEsOk9wWGxfE7MkxKy9Ir3SsY1Fv9rBePf6UHc4jCW_-Zyo0c_YDm_DWwC5fUYWq2i7clpRPYmoFluDOQtouXBlio2zPRkevyZuTkFZMI_zxrDrkIQ9Om9fcvGLhjLRIiJt_z9FeiPqzFf28TWBmLM7P1p0WzswikOtMXi8WUrMcZ5I5mris4_Qudu2j_Nx05BcrJ2b_5zHiHXUwpsBJT5ql5c9rp7dfza3-bH6NpeQEz_dmLzL0iGV46oJFc-k1EJpWNQhH_K6_61CnQMik6HfE_CVTOc7FR6IR504FLWuIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=vMpe7yHJfc7m5QUpdVrAO_DozN11Dd1iR6ICvJ2QUhEsOk9wWGxfE7MkxKy9Ir3SsY1Fv9rBePf6UHc4jCW_-Zyo0c_YDm_DWwC5fUYWq2i7clpRPYmoFluDOQtouXBlio2zPRkevyZuTkFZMI_zxrDrkIQ9Om9fcvGLhjLRIiJt_z9FeiPqzFf28TWBmLM7P1p0WzswikOtMXi8WUrMcZ5I5mris4_Qudu2j_Nx05BcrJ2b_5zHiHXUwpsBJT5ql5c9rp7dfza3-bH6NpeQEz_dmLzL0iGV46oJFc-k1EJpWNQhH_K6_61CnQMik6HfE_CVTOc7FR6IR504FLWuIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKK1NV37zw6MP9_iMBcnaE5VvCvTHPt86Z1uyP1hVOfyBs7Z4fmHURaWA2CtbzAuNENUQxK2I5ap-xIBT5eODPTUPEWAfCgPpd-DCA-uYPEDA0AMo-O9jTI5FKqqxXf7_g88RAwrHou3fZVH52auD0EXbkDa6JR75mLcjnPIOufkErXRbYwY8GTd8XpCTFqzz3iHnDJiEPvbagCcQu_IZfPyxYdB2xRn1Q1LlRRT-_Lk8_AOIDqOh1qikV3p-KqFOg80kL5wTkFt7nfz197VMzl-0S22t6vaz0MpVTSw_4zQf_sPIV6HK5MBKnXIyqBm-2e_et0XitZFusFb1LaIMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhl9n-wB_O3jql_bLNEugjLS3moqVpx0mF45TsvRz7WEkGiVoIUw8tPU7kUxOHkYsRDJ69NFfkVOU1BzoSDry6sGxnkKjEml8aWLOg-QP_DBEwwPNVXMkb_b_Yv3a6FA5IwDUdvFvJV8o5K2s2kHvd-XR9E3vLQe0EDo1rZbqU82PATZmLIJzsYOKY_Z0U6mWq04mRSJUxbnkcsbyrlgRhKogriUtiwdp1KT8GT24D4JhJi3egkq6m5sDIdxbu8qgLdmKe_OoKWTzwG2uYx9AyBSqitKRoSbeFu1QuG7FPq65kkNMKXonWkj2uEISxeiU95UOHCWvmFjzVYnm2TPpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUW22w2h0iEOGoSWUe4WWaab-puygqNeWqEkcE78s0J-d1WRoWaK86wHYQkSEAb5zOzFUxM3bruEMya1jKEjH7XwpZBOSdDLeP6PQnvZBgay5CwzKNQhhk62l0G2sbcX0tXU4upqO0L8pfQwdd4qy3hNhn23Z_V5NhVEsR70HFsQya-zZkftn0h7A1kh40KEaxMiZ9xRfC3uSwaDoTapTA_1qSYBndBca6xSDhpO4YFPYm17uLWw_XAwKyhhW34faPzcfeuXKTNwMELzMUNuZ1NLL57x3YL68UZ4vM_1WI8o8HlXJPcXmNHNrFJHnSX-sNrROxjik9PEMPUQEab48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HO7P20N77HutNs_PuQsJOQxFk0nW_XRjyG6cpCTp8USO5jiFOtTFyQJXNYUoHadvFFD2AgpmdYqA1StXYyybwVjDxRXUmh3cPM4QPBq9J6v3Dode38-VIFNe-uTa3JLx7ipacQZiEC671YP3aYFEtI6tX3Vpxgr9X9BAl4iiI1b9zRrGP78cxFG672scn2OKlM4ltjNX7MOkOhciAm_TGqpkrQHGDfqfDr4IvMzOE7ofGtSetBYHKaPC3184oz5GoL4oE4NDwr0icwB5B8kwY-dLxGPS0j1XY206c_4PH4WunZQCMqGUsFSP56JftI7C2XvfsV7c-TNq7SKwp_VaeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km63b2y84wdhRJWQnToQLmkBSk4sbODCRLXEZzqzLazLvFXr3sY7iPdo6zHrX82CG3DDOfyzcVMLX7Ecj3GRVJrEp29gXkSa3k45ND1ncJxtba_qo2hlk0ZHfA4_QtwGd0a49PqrlzohM0nxwc6vbdmnOOQNDOLxYE4GDxT3lhU4o_YpJ90tLgTZ70c7NWYuTe7RiOvRXcsod9JtOvDuk8Ldw5NlWXnXYI9Z0GTwchgZ9O9fkM21lB_0f1K0-8N8oO9hy6xXHQbrrXOOwspCJZLz1edoapTSnNg4Brsrn6JCskdfSO_WsoEAUXUbVRoTspn5pLSGureTsIXWTCBwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQC7NqMPTgAn2XF6RpKgmpFZrF7OyqGbeYKs0aLiB3A_wAyqccS5ksHTPUdRnn2T5cX5MiaoJLHcZpMUqIgxxxSk5WBUZ0mNOGKjAMHkf87Teu8HoldEDDzjGbVB052wlF7TnWdjynYwbv53JL1XNoCIf64kHrZj-n4XghX96g8wqjrek7MpflXvh-5A6oFpiRYjDvH-gm2dX2kiyIKeo5CF0yA9wDxh8XekRenJgPf2FpSyaR68-N2zrNluKG8FBJi9w1o-B-dPGQBqgWE4rHix6RRPmzv_LAm7UOyG-ED8cz-YUEevm8qr6M-F7_2zmItUdgQqEviDwyYRscM7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpoHg_R9Rz4ZT-Wt_yg6Zu9km6sDDcnC8c_wXeyR9KgvGP-i0il15AtLZz58029JbEoiPp1D6HzjZgBh8CiPg1bhdxuIglOhS10Upj7V0ydtpE8gzW8GLVuVo63N4yC59lG4ZhetSOCJcJZtbnnpkkuCXeu0IVrEwOzLRS7j7BL9OmTBbkcuFsDaJ3-FZ0K6cMB-wsPKjrZ6C8B0P5FYLs8AE1HXG5uF1mH6yYjNbhNGZsKqW4B6_XTMWA82aYKhhpFlQ4GN82hOpnJj20EzGS39vH0bkmm51ZJBsXbyVZ8P2SBCTyF587j3tsKWfuIiJ150K14yG_mnKQRW-HDPgw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=WwGIpnBvBeNkuQbCjKdMszfb6xxbVMjqfc_sfgmZh4MIaYAW9LhulTrkjVUmAeTGE4D_jmeV0jTVYcqRWucvF_iLKbCX4IxrO9y_-xs_pcMRu2kYONn83DUl_65DfZydVzT2bocQ2gClMypILrQMopXeC3xBklQICLpHD-b9TRc-V7PQpHH6nXF4Gu5sAHqzxpAPODH9RE-uwGJDxyoCDClQ-qUc-T5uthZbdMSRi1cwovPFj4Yz9m3IAyF9l6RKlwabatXX8nC6rpUeI2OEeKSGN0Z285_WJ9yiM63vP9UE8lBJsYWNyAphJW107zbqaYckHVVM-ZrdDhJ5JeULvY5szAP6b_g3lgra0xkm5SqCqCES_InOfrgKSmiPbti36GaA4rOVRur8GNi6QMz2yG3Y1i80lymp6laRG02vey0ItIb67B0y7sG-tLi8_tgx3Lv5i1O1ky5M8TZlgA6wIeKpwQiWpOvb6QPRYZkeXcNRXQ6RZtwaGTc33PFhEg_LbEm1rjOeANDomD108L2QKeU332QKAEvfPBcN4DvxhSyNQFO1WZl5Sg08ZAFs_20BWiIwjMYHQU131qNExwR4gsNU2UtcnYcetEPJ9IJvH4IwOPIVBLIEXSvzENhhFQ16G-etXkmEhaacW8t9qTJu5JfEIJ4o0nuy_3gPFDGdm30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=WwGIpnBvBeNkuQbCjKdMszfb6xxbVMjqfc_sfgmZh4MIaYAW9LhulTrkjVUmAeTGE4D_jmeV0jTVYcqRWucvF_iLKbCX4IxrO9y_-xs_pcMRu2kYONn83DUl_65DfZydVzT2bocQ2gClMypILrQMopXeC3xBklQICLpHD-b9TRc-V7PQpHH6nXF4Gu5sAHqzxpAPODH9RE-uwGJDxyoCDClQ-qUc-T5uthZbdMSRi1cwovPFj4Yz9m3IAyF9l6RKlwabatXX8nC6rpUeI2OEeKSGN0Z285_WJ9yiM63vP9UE8lBJsYWNyAphJW107zbqaYckHVVM-ZrdDhJ5JeULvY5szAP6b_g3lgra0xkm5SqCqCES_InOfrgKSmiPbti36GaA4rOVRur8GNi6QMz2yG3Y1i80lymp6laRG02vey0ItIb67B0y7sG-tLi8_tgx3Lv5i1O1ky5M8TZlgA6wIeKpwQiWpOvb6QPRYZkeXcNRXQ6RZtwaGTc33PFhEg_LbEm1rjOeANDomD108L2QKeU332QKAEvfPBcN4DvxhSyNQFO1WZl5Sg08ZAFs_20BWiIwjMYHQU131qNExwR4gsNU2UtcnYcetEPJ9IJvH4IwOPIVBLIEXSvzENhhFQ16G-etXkmEhaacW8t9qTJu5JfEIJ4o0nuy_3gPFDGdm30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgoG65nigmOnB1u9oPSGXYuUDdDyF9iwyAwfhdi4j2p6z4IHodpsCzvPvR-MC9y8KvFoCAEBD6zIc2HmwW6SXWmt-o80vVOAJnz8uxHcaQjssoGIEfqIcGkMkb_eLovXOxhtyRHr0Mva2Z65q9N3X06khpiCB3uHLrIRn-5YFZGdy2HF7lNrMmTDzfwlYPWPGxoNtZ-yAbAilqcn4tOzVVu3BxjCktqHJsCOXeYNLa2dC-SrwSKcuL050zpnocjKRp5ZHJ2rGm67BG6g6G7612gU9rxpXiXaikWyMuo8ZfVDcxD50LPOBaw7dPkxsVFbmg3zYVNTKyNRPbrTUxDMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSB3Gx4OVOCUgAb6K3_0Mgicx_sZn0ZOf5QwkK0YvFkHLoTxAZMrvYhMZijaj7Al38RohZFux_cxxNwyaiqMzq4bg4qWA1L5kCiLo6D1PS06UzVlHfLzOBoT2zg74glgu_9v_jiV13f7XxaNyHUh03l9zxrMfvIzwpno25ZW0l1BSzLtkfwk27ehi_5JdjRl2fBsZBVu6UVEI-f9ZuxJP2HGQ6EbDG4xjjDN4Zlyqj2M3yPspDgdh9s5MBLI2N4-BIpSzu5w-d2sCyowOptSafGdOrSCfxh3w3dpUty58-ZuPmhplxrSEN4ypuT280gCli51ZxYqE1GlWdUTNzTybw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwSABesAsAIoo7OfM2LyzpyqyaCnOElYEFJExnxVxtpt5Xlin50PQ5QChzbpfm4jYFS8Dru-W8CjAjAeiTLbblalIKzsM_YdG5bWR4THcGew_luYs--Gw_RfqSON_SH9YuOGKFHSqcE6uVCLkyM1Wn1BSOxn4ZqdDxUQ2NZjAa0_hwFCdN9psEZ7EKxaapUT0f6MDuTdJf-vHqs_3WoDjh_cA2NrmSSsF3F7qZ2RRMi8uPbYPevevL_UpQz75HPBJCn8uQazfuuLo3bAdBvKfHmibwm2KjpVmrimnrCqx4_v6JdDwo60Heax0evu6yAY7SUSzdROEkpsUtI3fa_l6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avJI3KsYGLzLkRfsKMMZnr2t5-mQD-8R4oxWjm3LiKUTBLWYzPeI7hNdYgQn87khUvn7cqXTIUaSGfeS2EJdr_N1rA4TcQ-Dwkw0roP9t-Z7u1PqpULTpZad_2xaN5deqPfeaxHcltb5iYTLEm2xtM9-YUCYiY58W06_6xGjHkxf0hCHyr5au9hIn5RkSP0PWrfFA6wGRUmv7PGmrS9psuAEMdYwIBJcxST_W7oUdyxCJeSDlxbZNz26pNFnn2NhggUoZoXN8fQY8lP0csMQE68Hr5kFlgFyXEqoon-ySWrmaBQeh8tE80HiRPMWK5rfpoIBpTdz94Ho-XiGTpFZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm0sNfZomJNyVkaxH7D_Jg729wS81ejl3ro2Y9Mo4LZy-ADrdow8iSP1cxZ88zG6KTPRGPCBNeeF9TDTYeBvcgT-FuRpYqGbtuC1XtFNNLi-CLxIklKamVn76N3vZhWtsmVAF20F27AktaC4sWZwV0OpIvzI9nEV9fOsF-WCTd0XT0SrFoftVBmsEjKfty8cnNdMWUoACtpBptoDhUhRouC5VXkEFdsUfT80jMmJ3Prqiq0XjAE3snlO3yyH_3TkYVb_dK9HFzypQSn_YK_m9HlVGQVeH2IQsEBmcA6cYE1vj16C671BKowmLOc0h8ORqlF-4ED6L0GLoKtmdKlHhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0T5PkGHbG1qxgfBMYZiQ2Hw4uJmwhUHT5HyRpnL-y_TLfsFiq_YQDlFong0m4YRs7NQEX-s1Tp3rP73POI2GfmKqFN1sCGlK4tdSN4_7jWbD2SN-b3o9BgsnU-8Yzsi3xp9qtR1pXiwKSRLoQWjxodrdoF2FKNo6MQDqElHH0Ho8kjX0l4Q9H_xHpmPytRETK2vbyEpQeKNHaUoC4yyMFkmLrflMe_-vytKkbQOdb0I4ED0XHNl0YJrcjg26Vv4luKmja2EKdQ4J6YcsBdc7rJ81ilqyZwcJdYMGHnAL4TBoYLV1RTWGrEd2XVEW8sNzHoFtHbQn-_5xzlhOs826XNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0T5PkGHbG1qxgfBMYZiQ2Hw4uJmwhUHT5HyRpnL-y_TLfsFiq_YQDlFong0m4YRs7NQEX-s1Tp3rP73POI2GfmKqFN1sCGlK4tdSN4_7jWbD2SN-b3o9BgsnU-8Yzsi3xp9qtR1pXiwKSRLoQWjxodrdoF2FKNo6MQDqElHH0Ho8kjX0l4Q9H_xHpmPytRETK2vbyEpQeKNHaUoC4yyMFkmLrflMe_-vytKkbQOdb0I4ED0XHNl0YJrcjg26Vv4luKmja2EKdQ4J6YcsBdc7rJ81ilqyZwcJdYMGHnAL4TBoYLV1RTWGrEd2XVEW8sNzHoFtHbQn-_5xzlhOs826XNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNQT9bP0QtNoS4x8364PiSB4a4WHFwtggag7CQ4g49OIECKXh4JMH8-zW2VHquNlHqlMmW3MuhYEaXlKO85OTGgSX7Oj3FOz3fH96BbbFWTtXpTlZx6q_Rt-4fdyjSGm4e15LLPJnQwkToVHarUiIhNPgoKumGDotBYSQxGZ9NpKSD1Ca6VZUYL0qOlab37fvknnT1ORhRWsfnmzVl6IVDs4B8M23i94yLjpn7BBtJwpXi8D0WIdIeWdlWyowZqRNv8uC-og3CsWp9XTpE-2GG2c9tBlrNPW8DqmuhgIS375YeAWVN8MIhNOrJC6HISB_iMouvlFPtvO-VGbgQfNQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPaMbXaNIOZ9Z7UbIBKQ08I4jrJie7XNWt_DcnSeTO2GaZLVZkpRbv7UDESWouJe1mYigGODHhP4sC0wiQIWrzmBp1E5IeqpVB6hquH8MwUyxQvfM8ouxnJSazCv3sZPW0-m2wyYNxo2rUDX7d_Odnk2QSdBsTVUk5z4f5nwFOXLuN5yGbqjXWHK0_HErod3paWL_cdwwcWARzIvlJnigip-BuNu4Wcq8V_l5meEXXTH80HHrEY5LfRH85BKoh0639K_ljKj-JucVje_iUvFWLPjPVJi1sMJ6XjI0WJ5qxlmdqY9iQYRxkdtn6aXrZavxTt381VdZ-IAbVTge_UvWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0lAYvKvivA4EvN1n6yak0u4xDaPcmIqFXza563sUeLxgLz2sYodhxtdfTs4UyfpOuu65AJXjyj5QO2NJKUCW4LEgZb9iQ_uhIljLRNQXq4Zz8zcNvauoQTgjQuR1iq7oXS7SaJtlJkPbtJk6NITL83wTz-6tkuHCZZcyakcWVNyMewZ4ebewbRHIMcvT3p4LavQazQebQshahM8TC4EIXpUP15Ma5oR0FwiSG-FdCcgpZr4fE-CfwlDzUcXCkyJViG_HHy7BQbubbob3SNmHJKhgx2UPWPOZbP0C8_ppi19LgzdC4BuzLljvUu6kIQ62OyrBRXInG39LfgmPnpjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVoSSPXZNb72gLcS6NWDKOXh7fvRJDiSGj95fTDiw1W2-HVBP2wczEy-0w0j2USko71dO6Uq-Wexk5orW_WWnlBWEbZYHSHkPnsTHW6VXYShprBxm84XN-AJd0UCikYyzmsJDFsAa8GerPQZw8uxQ2vwE4-ErXuv7lv99tsi59TM-OQby2bUaGX3NGeK3imvRbt1gVPlS5d9fNRk4BYQmjic-rp5VMszmOXbMVOXk8zRybdIXwoMrs4TSmaFWAr24Iii1L_wju7zALQas3cXQFTT5Gckw38qry7M1Sgdbnn2jsgBKRfiAL_KdHVAnjtjxFD103YPmcwpP9tFywKcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7oDwjNPIJHLP5_Mftt2hOnzROiwMwhRH_TdCHkBoffsIy8Cl2DXRC7AJ3z5pn_PA3kWdjuNt5mbyWfJ1R4Bte0Gg79RQKiTrOolv4xqe2_DfLjmXwmOwhmLPvwzjR3U2k2MNnfpmi9JQXOO110BLebq6oOECUMklM47Ok-2PiDPbJh5qbA-HFqqfjhB4yA0sArZkYq26pGTLQMs-xViMAnoom978WLGIi2xvbP5yNH8YM5CWodDe3FwjpetqQXkEsidCzow6MHKV7L5yJRb8EFkjBOz39Ebm8hhefHYnIEJ9CdUcMy5xw-BjdRxmbxWOX6PnTU8QakjP1eXLTuXlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHSIlOdudzza6jgjmU1Tz6c00SXMYfzNsBInO_rKL0PkhHa5B8SzX-m0s0kRrPrP1Sga2qaYTGexAWYmwXOqHvggW-7JBK4veEqJY6HCYq-iWO7Oq3lEA-J97Dj2rOSveXFgfEhjtjp4ZglgFeD7eZL07gEnW-65hthaFORj3ShkUSXjm60rnojX9Po8P82OEksZLg4oAdH5cVlGEtBco2R34kT1GXh0ryEwfoZtg6ox_ZX2-c2nkIx2uJsdXHlmvCr5LqEkigE5H5N0tKQJQY67KHs0Ggu-8Tf1seGd9Mej783np6F6m30h_mPcz0JgiK3QoAFwvJrLKhaH7P5jDQ.jpg" alt="photo" loading="lazy"/></div>
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
