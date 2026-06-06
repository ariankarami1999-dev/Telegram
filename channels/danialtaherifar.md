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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 09:36:20</div>
<hr>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 259 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 495 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 622 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 724 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdzQF5CQH9l7hUdcaFXQ3dJtzLRQIzMTUw_jhp54PSYKhse6NYhbPsq3B-PXd7UHEpXC6fOKbROiGzSvpxmieRHUw3eX2qlbsxDwtReUV7Ut1HZq9R7KiyTZWQUSf3xTN4CTfO3ArJ2SyTDidVu36aAxnKU3N2TDhLJW_UtCYsp-tXAjJ7TXGix_vVO2HwMM4q6uBEhl7iucoZEFZ4c75Zzl-3mwTV-Ty3N-xFokbmaUZ4tbFyaUtGApoob7cRcxzy6jQl0sS8jYmjpUwLisn6r9apnxBY4jxImfGTR_EdpltauFYiwP7lqgFBOYCNpbR-XeROKX52TFnirKMH0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 748 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkT999FlytuneSgRVf9h17QZGW8JP-8V6x7DjvxRs3_HCeij3O7GnN3sUEzngkLmIjr8jNf4fgE1SxaPA7Xf1aeZa0n7BYNIw7BTGqGTKxHtYTq2wAWXKopE91as-uZBVXPyebJn7jaycWhHY0vxtCgqfl5wZStoBMFIQs-_wsaOGkbo0_SvjwKnVnQ3zGLarLRQM5mjguPNLlICWxknllotinqDg-zRuFwYQ6d41Lmo8Va-qMepH0QmsqjlJwqbyePqfpxFmnV5xfb4pnWPk_SgVfh0oru7orBbdJl6B1l_3dflLLmc5PQUramcjG_nhglrwkHzqhnBie6aVQ4VUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULRRrpH-9qV3Tuicknb9OdtYok5CWTn6wEqnSRZ-47_YkxhdpizCo3jd-WGFaXbbimFidtMqRNhsfuYLv-yisdtycp7Sh9h84jgHtlK8IRqUyvDXILwnpdOM-L296azlKmm_kqIw4JGsaoBfoNfgBJDYV4EbjLwBIdfqXAZLsTpTru3-ZM5vhP2sKNPdJPt-oGlcUGZBSJHkgxY2_SV8KJJl9qwslku1OG2laJet8mcHbF0wxAx6UKX0AQBldDcUgXga7hwapz1UxETSNwKVmpVVLGX4nXh83PqdBSzENV6ItxfY6iwCxPmaU4DAWtVeHZSWcISPIs6fdYm0pEwBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE5eY-CheYiVLUdpkXCo2nczCNzWr519IRtsi_W9X8d4U-9r_IGxxIX2jpKWnP8QTMyeN37LQZcG9LCiea4_oxqqkSjnZvzDRFbLDdARRf27NxC3r9MFepi8iCIO6DW7sAQy24AQ1qywrvwoP2k6VhZG86KWmLz5R26GH-tfAFUSYa0VezdRsgEZLtFY1vMFx2SOtSpN-q5V2jJ9HT3h0mIWP2-X8qyIGcux3smE3tPqhumrlMnsRSpicEMAJj2jYIJ5czIU76VcBRQM9v6Oo7BDC8JKZY2Pp3h5YyOw0Bk4um2vRWozBj_aWrrquNoX4mpEnw02GVJRGnzgBCGEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLv6_7MrtGMAox8vbCDmXzaUZPuiRweXx7m_WvowG5gtPQH_I2F3F50zZqWIhPlWin9chh0sfTHwwViDUdhqn53I6fwUr2s3NekxaznJWB4KhB_KP2x3aIbp-N4KYBroqeA7ZnxqqdTzWKxh6FFpEhPLnI_CeOPJVfHrZ6k87Xi1kUrCmSwSGxIbUt9vAydBqit0EzE4tO55fB_ontTB_G3NxuAWNW_SaPytiXYS-lY8zUfBXk1S2hosbiWNsYi6IOB8U0ke7ZYL2ABC6BvBArhmqavHKyEUSqXPGRKUZQ2OLRVaLC7bI-N2InUmzAa5q9GYY3bup-SkfueglRgkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjzrDuvupEk0jcEteYpKXaFi707DDqm0sThRvM3W4Sw24gfmRuaLbsqLBC3Zk7yDQDjBBGIZjaQUntEMvQ41sDQEuxH0NL0yQBaGL47SJrNsG7uLKELDHpjb_V_e8p-run6c3FmCidHj2V7V36zRJcWhg0-u1t-Ef1q04uIG-p6Hvpy_JXx4teSyAzTMO_FPci4gJh-iHVF8Dq-ja6g33o8_zZDZ71XK5DhAc0tAjfFXig15UHnKWy6T0DCCCd3agzsmTqPB_r8xQVrujv6mxhLN-xLAWXxNPgspzZXnPMzu23fSK0uT7folhL9i6Z-Ombk0yeLMZRPr4CsaxwJTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uj3ns-sJatMIK_r2SsZjrNzpnmElqqOPMq-0yUWd2RVYX55LeJkmbtxnj2KIA8uWSZZ-C2puhGvCO0XcPzrJNx_C3YiQ0iCCK4X0NrM35IcRyjCt5OXqmrVab9iJoLkprWAOBKRQCrA1IIR_MUZPYx_4SHWiPVUKf_72zWEMDjg6QI3sY2_RNntZLtBo_gcIkvvV2zEC1CtTIuJn8TnMVt58_ifRbY_x90s8NfWz0CB3gTwoFoGvHMbzcB4nIHXN315fhczDxKID0TTgH_wrt3eE6wJxMDZgzCMP2pSXvrt1iS--YvHKGqnAebz8aWcB0QlY4XfjcN9tpHom1kjKMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDsvQ_Sj9XcwcBSStIYIWLMAcTCnOQjC_nKN68FGwVzINq8kHMgOuKGZoZmE0tCsTbn5vVLMyN3gVAf7PoYhhxqzOPq1XGlJoc_wjslY7EP05_D96Ktihd_R2WAxMTjKQZfvOoNFRxqv4DSXe5fsVatMu8pmGmbyqGALHh5jHoY56g54k5wXpFcrrcHbl889nAqMV9Ytcn9ND4v2LnO8HbwyI4OKOUMIm3sfB2CpT3lq1UPTA9HM0wjK74KFJlW9KopOO6v6UxMeiaVJQ5f2dlNqZ1VCMYK_zz6KAHx3-C1H58c7zgHcCEtGmiPYpz5_l4_q5rKjDgcFEcScKPBY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOxmodH1L9fZWEkdkA2CnJqQmHt8eDM9SFu2Y974L06UyELD2S0pqlYzbiH5nG2ix2soZHVtKHOCjLeIS06k9sRT2E9ly-9_oFDvlIxLsRem7Ac-hUs_mRC-xqs89dzPZi2EQun1LUhaxInJ7ausDOzid2bbA_9UcfaV2Plc6SKzXjJbZP_xKiH5-Bvrh_M2DVkQq_mQFUirhe0VAN6Xh87OlCnnTZ7ihTLDVBUIu2m26vLFiqrBRbN2zGibU-7nBXKXiaR5G2oWD-pcdW469IZ-IL5KP0nSEATSihQkT9tCWthWQYxOnzGa3QIRZDxN5nl1lWvOkHsmu1VRCgziow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU6fTDhUxFNLv91b9H8JiYag4cOo6rykKe7ssRLupCIuG5wygNd5u8Rtije05lNzldzz0ImY8yE4LnLejWybxepxxmRy3jeK-ahIuN3OcIjftnvauXpcS-I6FvSmtIN6jIv-_PFbk4aUZipIgI_atK8lwBmJi1BJW6uzZWrZRvr3dSUX9UlxDf_nORFWMLmpAM3_iTjlFEzYAO-31_k5ku8S2XvxHheA4XD0Hqc4sPA0LryWiWP0sSThShRqmdXgiSrS2sVExuq8IB2EM3jHACsd47ZoEScCNhj5IfTrmLc010B8sPJ9NDVMKs--8dZZox5eW7nftAznzVov89fCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tL99AEkdlQ-IpHY8Ayb_iwJDLGIpHoJE2CO8lm1XzBTviWEe-LSjEDFDjbBZ-4l5ihYOPFyw82DUQRUStidnbw4wYUjsCVRULlavt8WbJ6Urqxfg-SjQGScIcDsNwFTsflIeVMVgWvX3qkL8SsTVP7jK0EO6OgpJHQcjnxviABYd5sq58An8fdKfjdohZEqSRCipPi_s-BdUz7pkH1MoVyGWQyEbkors5LNkHmnBd_StgjPRvfYi7XNwCyNhgArIOUyU9blTAgR3qcQudA-GPDY9V4dpdmeyuMPpbMg-ov7-IiLNzJGcCGQXVUoet4h5P9l2uaZRhC4GtM87PQnw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c65Ys_SF3cTRkdlJa4-VeNity8byu6VVrOtgWZ08ZAlrlYj8CHQZ2gwAR60e5nzeK6H5TWAeJcQj37gNoEYmev1jZHLtpi2ASMQLP9r7LcsU6llZ2I0kH4P74oXMwL5Fb1Yp4hEyDi6g9cjIM3kemCsbaYeipvpzs396iU5WhdFKWIn6ZwpcvmpTbJkoQXFeot_0gspwuIfu1Z61pMMZOTOc49SJ1VTEDm-icZcRoRNmMI8fnXBXD2DC68rOU4841azD8uaRo4SUQAjGXHToQPN7KN4L3Dx-gWaueMfkJLPzszSRiDRZME2zJN_8T-XxGcMya-WSVyHGc-aiAvFohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pr1Jz6iBxEd_Z9-3bPFYGjcbNS1bLGkMFoJ-BpTA-dwrAzpLtrvsRP5i55Gcx0QRxlWL3sh3lABik0XnlAwT-tQhW11Yiy9smggWNHNuapca_Oe8_rpQS0o1IJSdf_s6pFQ7HcwhHtco8szy7VN9DsaYzTjiyFOBUeA1KS7VXFg6p7qix0hhWNuuAWmszykGuXlg5G1XNxWoMd1sG91KgRYBFau0L4OyCdB1xsilHmIZ3_8pcTTQ6CgeYqHgqNblAOddMyC4zpgI5BmVThvNcmpQKSxBO3r3WHdsoLbp4tIERIdHknYD7l575yM0-WEC8k8zVO3BDUvAWBoLSrVQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vk5RVtmiK459ZC_8Gmgn7WEjH-MISZouIofBSTIxRZpTTPETFdXfuxEWHC5UOIHcK0fFPGkHps9TYGI7FlNbx7bO1FYsK2da-sL8aCgu_XQhRrgu47vRVW7VciMFJ5jb6zQoutau7Huw9zSYG3IKp0LZkVvVFrwqv64x3WvbGDNNzJdbLcTXK2dr72E5nKsX7gGOnb-r6khamG_hX6vDsKLBJsnYfWTAfp-WUh0hVp_qtTPh2rm_Yu4UIr3JcAvBrUCettL4YAGOXQ_CMq0XI___trryuho5r_mm6Rvb8gJQYEIHpL-NtZQskvjh50NKKMc7ncX-X8NskXMMdIqoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grRP6cytM00M9KdEpjSzRj8SpheCMWhOU_zaOAqXoa9v6U5t91PBy6ywdAWeY3o-e9DbFBBYCr6_kIdSCvYsGrO4TBFxA9OFULBHAWM7TnYh5jsJQDXsc6sHh99IwfIZwNVsRVJT0NIHcRc_BDNOzvuenKf6W48vFPVyPoHS6tNjquzWquQ96C-XVzXClgW3LdhhGX2w3JdfT_dQAGT8BrKAW3SiuyCnscKc1_pvgFihrGam-awcCVtm4-W7TOQTaIohmYTQPiqkKs_Otu7jJuiiab5VcotVP4udoVAj5WgiZoR2sDXU50ZNU8FiymWDVV-aLGPK1mvLlK-eaOiwMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUpRe-DMIyHZboRWI_PpdcfeTqsA7qqzSvN7s-VaYga8fW7YriU9a_VmOMZSgQ2fofcwRBTQVALsegi1geezBMCmoqo6uQq7BQtxpUcM2OSGphfPLWx-yXt5sfcsK3G7arGLi7MTVOLoNIiHgTWZod0xubVwTOQB-aFFFV7r678WHzrmS-rwU42YsnAcG3kw5IKptivGh5wy1h_wFpCF7IcnbcX0ApUqAIkhDBX25qQBMVYgH2SfSZk51PRczIeIjS6cadUgQ7yLivSX0YzzGe7S_0P055rLUYvJj1X1CqYNL2ZqPN5lLt4mSGs_DcBH13VaubNbhXM-ugr8qJX-HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=dAkYxHI4qHZQSqHa2BoaMT5d-GoessnSGuFDumGSsEBG0TjAL30Zjn_uYUSwoS60icfA332QYLc0o_kB696O-piJLJ6wVDRedLOEGRwh0txQGPE0w-YZ3SniaJ9EflTTBcIdsJooP-_fLvgodJEwQYr1rj7VfxfxNFO04V-ucw1e3G37kieZLAdonCaDEeCMsxN6cnFb8kX-f4fS_7peXjnv2nuiE4N-omTUKnG1Rk__w0j1DLdsAdaP02KkpekCL09iBvCCpGXaahxnH-OcnMgj1xjRrsAbWg38dtLoUWilN16NiLE9XVkuMPTvHoLAMlutKlbNkGiq8DhpaRMK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=dAkYxHI4qHZQSqHa2BoaMT5d-GoessnSGuFDumGSsEBG0TjAL30Zjn_uYUSwoS60icfA332QYLc0o_kB696O-piJLJ6wVDRedLOEGRwh0txQGPE0w-YZ3SniaJ9EflTTBcIdsJooP-_fLvgodJEwQYr1rj7VfxfxNFO04V-ucw1e3G37kieZLAdonCaDEeCMsxN6cnFb8kX-f4fS_7peXjnv2nuiE4N-omTUKnG1Rk__w0j1DLdsAdaP02KkpekCL09iBvCCpGXaahxnH-OcnMgj1xjRrsAbWg38dtLoUWilN16NiLE9XVkuMPTvHoLAMlutKlbNkGiq8DhpaRMK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8S9O9u3qoFqXbMUSUlgX4_I108HdbyJHCw09LNd7h0sIqQeGiMHEunuI6YHGxFU348diBA29KhpEDCD9qWVDahsLgkCDxN5tPBGzlHH9XFwIWIumEnZe699dAGJtIPtl8uMwzDVRnvazwmllRzAxUvJxTTgT2IDNevyoNrdTD9Kwc4OXVD6iOmAK_2rE7Qn0eHkkukOBO5LBec5oyvH-jrCbh8oHbmMm7UkmSFMQ2gWI7vTUfPJmFlcZP22WaCJb8iQo-9II4Ynxi7CpxFI5UoNiobyIKRDamk_4j5XAa_xIovZUIq3U0rOvbsYlTDnlZyqXjr3RFC6xrxeqhjp9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFzGtnmH1nKYT5XJlL2OnAN0LFtmT4CehaeRLMadRo5Ked7yOP8nl3FGsYaZKYU9SyqCYqmzDP2quzlNY2tuYMIImsXvx3crhkXNb5nNJxCnxOy5p8JQ9u0zFrU7yCt7uAokrjMJS9mB40ku8AWEDhtXazMSvm7K5UTybQVShaHxxLbLgfOKbzwLjQjarRfPWieKKILew2KhKcEmRSc426sgXxCPK502n5cIWPSRQ3Oaom9ClxcKx31u1ZbnlRZyHLNnhvfT5ofArpK4E_BBDDH0LCgPYibcSfaTybOOc4XYLEWtOp_ELw3Rx5czz64ZmfTmqc_xJTndcYg9YEanyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHG8g7p1FjiIexlQRtjjXco_Er8rjZATsXIe-5LFrvtB0P94ngTq__lZF7MZmxOBadtpXbzNq6q8W3Unc1EWot-7mJh5wLzGueehdarRyWUYhkZZHceRbAZJDpYaBd85y48tV8MMDfNPoWtE7NOFimHWwcFCRodkPJJxO1zlteXkRU0cQNLhEMzuv69R00uYvOWv9ucsTPtFZh8Lzx-yLRBFuuo1ViIUAF_DEIwkQZqi0VjY7I2h7epOVTMxTX7wxTjxUWCgn_mLcRL9sTuWfR6mDZcICd5L3fnGeOF1vAdU_9_jdH24Gkz9wEfh_fYuXn6uFZc22_it9KHlk-uy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_OCfh3CYzIro1RSHqPDW6bjYUREd67LwcrmmkDI_pTVow62ETv_Plx_cmob5neLDvG659Wmq8f53nBlS5bSV9uDpRt4P1fcVLHLyysgwiqhOJyqf63aPdQMncy7jXaL_lA0ekyOgQlsamr9ZU5AMVkVFbuM902IT9tTYxxTx7EwiZOC89WJ6Zh6i0eHXpE9vyHpBKZQTpDK4CRCj5MbbEAMGKURRTotofALO1TnBlsQcEwSiFfVYjXbWlAJEyZJZqV7I5K2Zg4zF_5ZO2r0GnQIo_wFbqmbKvZ7x8mw0GzSkXiC2UrB0t8MmTjycKn4IF6pQdAQm4iUn3ymTy4ROQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfZdqnK5vPlzUEen8e2L1tly77BnodTBDdsmMHN35e1Pu0uU1EjZrHK0wdxlTMbHrFhNJPwB0dtBD_9b7sFqWOguP9qRmTPbCcr_8YOOCmhdAYOmnvvNiULiDHCWEthJNUp_Flr4iA79uGO9vlkiAI0WxYsSvVEqsocDo5HkR3IODHFmzo-da-55RQEh9_fcYo2vlBSnKzTOyvdsGXYxzkzwvnid-sjJVBhZfmwgEfILcwU6zl2aQBZTZXeufc0Ok_PVHQ2MrriHzlpddCpQAueBOyNHd71NatD30yxMcr-00oRsw-dLeUHHpV5UO_tdM22PWUsOyzL1EKNWXpRjgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZl04oOPcKD5hkVnr6d0YUX0nYKhihXin6t6_8VBkVrYafqGVIvyeSQUDYqyndoH-WDTqGg4lAhY4We6_gcvidVZE4v5MMNHZvwd8D5jaIZIjtZlNn1kSTeQady61AZjGlOD091Upjx8m9dSLbtIiN9dtCMFWTz-oaYlNXRxuqE54x73Hl5YbxGl1_X-Atrio1-vZWGhMuavtCHfE01Id6NuITbI85nAgXm_-tCJdOkVPLXDvXyRqnF6bfFHMZmWDHuRysfCSggDeQsBHRmwh1MUywkBoV27m30md_OloTNKvFx70XdcTMfsrxXmeeBiZk8GRTUqvkK4e9oqnlbbrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rScBfjWc_P6U-VNANLPE5ZDsX_krBN57R3oQJVE4inGH32gSKBO_AAseGkDTEQLLkui1Uxynk4rd2ue5FqEIV7qDxy_sLCM0abSpwPFghQVjFx3FzPxnxspwzyPchbXKIa6kHJoGhYF2sPig5StOBeqR6fXSjiyx4HBoXqMYq-gN_9_i0Ub32DcBV16SD-Qgb2PcCViheD9DBql9KmleXuVhhxZ0W07kpcEAM5WnbT1g3tNLVFuby1kzlcDb_nW5I_S7EBEvz5WkqNsy2Ia5-JHcd2lYVPlhcOZzw_4RFSsKjOZ-oyZ-xFAm-pKKT-pAuheKK_-wIFLvvcvnAPAeJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcZO66VhuXRU8wDomc7n5b9asQexZ3OeJUg21tF4DsYyqYc5xSjSvyGntXJ_9jRRwecp1zR08rHnr7_jx-wRN07dluR5ZP6fkUdQ-39QizLz5BrRVe_0kVr45sKu2yphlDL3ZrOwg-aCMdMLW5e9HJeIGdBYFmNrI5RLMN3dZemW6ql_W1nKDZSFiQqfm1pAIW_B9RsL_EunPU-zqSy--g5bQyxK7OWxSSZhaKYIi8_i4zmXf6m5EvYhCmKI-x7yRJGcBWTaYmG-fIdX0iUQMnovoae_SBsBdC2XvU8WXTYFO4PHhvq0TGJc5I-pKdzp0Rx2kdLuB8ifmNHkk-H9Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZ7_FM6Yd_fMpD8TgCo7R-1QnH__JfKgOjVEjzaq30So45W6WcziaXs7qGIyB2sgOfMAmEQp7A0YN4Z-hWjPeF4255BukHAgGmyVvaD9_MGhWB7_6F1WOUDxI_fLZ4YMs5h2cInDdF8boSdltJBig1r6ggwiauHBQiKq2oPD6YQXm5XbONOwZqjxfH82Ip3bo2-pWnwuK83XBT25oFOBJP3STs5enS7O_ekfoiB4wGGtJs1HIRARY3B8vHEKP3pauHz9HgyVwhukhfY_yqrAbXRTqXltB400T99iuNhzMHX0txixeVtcpflmkQzIMJzvJp8dZgRay-F9CrajVTKjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 659 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO07Z9iXlXur8jd1IyXov4mrBxWc8NLAkZnEM5JK7vUQCXhC5lsUYcg9HSzAxWVNuFTgeXcJXjujsjOlfmhjZUUIrPcB2v5b7zFOB7FtZMD7zJQVJZJ_6Xzv1pTmMeNThFlN_49R3DEVQUuC_2WPqWczDyfjZe2N4Hhq-pR8J5dMRin8zIHftIMA9ZfT8LsYy1VeG4TZrPe_Wp9_NglD-uYm-auBlcdZNvoJNIWZg10-mlNXOPDxPvi320vvtOR3h3LbI4pRm-CZ420ppKUtBsEQeZa9RqyZCMbE7sOhG5VZdpXUPX05wKFMUem0oRRFq_nXlKWgbZAkW5azXnlLdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH7qbjMq0quwLYE3qeFHN4DPkqaMsaMZOwfG6k7A6_nXeORnrrj1y_WGUEfriHo24fGlTFjUn8L3ucF64QGa0RAdrPOrwnpKwQiYeLkorZifcW9vDSnVPhsMpTeh5wy7Fq8NM9u8ogioX7N3CqVeuOHCT0JTk_KqahOM3yvan7Vfm67teeKj2i1LU-VVyC2BN0r4LE-Z7_E0_LMPvpWGGKP0oKLGwigb1kghFve04C5S3ajotolNY5GLXsFpHsrBUtdj-jq-p6vVS0_E2iHqxPxthpM2XwKGFyuwYZ5_IcO-cUCWopYEH_fOoK5PTRa5hldkvBE_E28s7D0REKxbrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wdc4F0hcpJO5MLVTK3ChpBU98CNxgptyopTu8F5CF26hoYxwIAm5wijJh-HQN0vtX7qLptrfEy9vWmJJf06xewzyyc7O2TpPHhaVwS864fe6LWoVmd5_VsadijMgSyyPM_MPtA7MOgCpQHEU_KVOkAxmCtUUkafUmw4yTklubXpt329txyNj-LklkwiYRc3-ibPFNDVW2XbcVuog9U0ZXyDXPjMsp8W7Q3CaEvP8xk46AwA2XeNioGUetxaydiNy3yX_60JodPkUT8USHkGo2aatklB4W8NTmpmUQK_-gpuqiBtoHMVrjrYwxk0VVRyNWql5kGX14O4Mfgjb5uVepA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QT2KPrlzxGiRPUUmE2grly2LJ9KsCVquL-XiSQm3Ydm2a48CwGnQFVbAc6yrRHEtjQqd8VkAKx222VgLYNWvex3RjKDq_k33t5RFs4yRShMN59OMMLGgr2vAdcZmwKx5i-saWHNg9ku5AguybYLlFK5VDoiU8xknPGgggEvlsPVQB7Rl3UHEWNfcpB0HdVFhi0dStwua-0yp5LUsUSWJ7Gq_DSC4aWh5fiBbzkrWM9FHGCOWypzup0lwgrt9v1cNu9cNTNPkD141sYk4qXBb0XuLqUFWQMTyf9d4n7BdLqY0jnq0UVhz5yRKgu4nqeJx16ZczRaXiWaZk5bsmcJG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFALDkJjW-rG9s9EJ8bPOpGabgxyTNnzLlka8comW58AsKGBVn8oHtRvi52nyXJFlh-Z9FZV21dLY-BxnI31gBcqkmbfyXDVtpQGFxSp0eTa7IgDbRqLHK1L7-iWe4onyk2qnJp1SthpdwcC_cMb7CVAYfRg0KCJOe0eKYqWwqHru0R7p416OkpRzVzCSfI4Ctee1FUwlR4kRydEb-gai22k8bY2NE4YO3yHOc3zJGiLRiPhI4MChIh2Y9x0MbS5aLjEAQYBm310Yn_z5uoEkC4hPbuDnPlOgfKEFO375icTK-SRK29AI_YwbkQCXnlvDWs2SRGwCyE3WPgIJCGPdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKEeYl-5BQqLu1OR8PEr_YkrBPFwh2cGF65pPwztLSPKQqKbvw7jHz-5LIwebEexYzWYj6EPG7TpGzlTMQBPCMsxjG86X4fW30IT6i8h4xmA-EKFOTmYuusaNYKVcGGaIW7SYW7yfjfNnJw8dPeZhD6GDPIom-O2W8VKLoLBqSF49XFhdbrZzJe2hsH8CZBC627QlMlf1j7hgtNYWjsd28q9MhOQBDu0gY71RO-K09lqrPEfpfxbxzRr8_NKd08cdNldtdrP4bcmL89RmD4LvC65RzVkDbrFBm3lKloPZMr0IqFE1f60lmTdKPdlnkI4npiYZQ603jIFcYSDhDFsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufVqSRdapEKCqWg3UU_GIRnaEC1xI_c9b7hlE0s0YzQKsc3NS8k83t-RfE8E5a_7dkkGp6a4w1cIBe3Q8DR3BLezCr46_u4GmmiS2xRJchpRKjCCWuwaPtb7yV_6PL77zWA4ZNBXKvHi2YXrcrlirX6MJVEUZsxTFeTCNbAjlvhbMcLwMVsa7lsadkrXNrnIlHsSysnmtu50Qd_Pc4Ag1Nqrne2VmPJU1Bm6t44wU15y-Ne5o1kDfbuSOqSukAjREA_D3UlvC3jHG1OiL1mcBZH8o8tbSA9EKiFbNwWYTIe72jkr1IgyCh9ufPkA9ycm23YjQL0-Y2rSF7b-FhD9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzmxGPhFdxypGBukPwryaMJgAo1oNPRW1aKOs9sa5R_YMsyiVL4TR2j3FIZVjxs8MLJ8BWKjKM9o0otnZxm1Pg2Vb0T2Tn-mLn9joJFNS0EC3ff8pNc1w04Ohc0uVKHO1bGKvwE1Tt7_GWppQcXCTG4A6Z0if8dA0lJfj-pB1ErVa7w650NI4_isAEYvJE_5VsY_x58SOJhZ0is6fD_CONfnSrm90-6vBGJzca7cCQbjsW4MKd1WZI_rYpJir4mnfOm9HXEZX8xNukf17lkuVKJui892YtSwIUHFOxftDMbKNfwsC5gUoGywdBoXa-EqVdtq3FTSSXmKEU9Lle2hAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSLpE7x-CIdhJCc689mXLfdvYsTKxf40zekaAnjGDvNhHNRjNvDCt1YAg5ifm3xX175mEl6B_aOpB2S4RD5Z_yXnV1k4_v4ujWciZFeVAvJ5ouaqb5DD8buB1boM5bwMbFQj3QZYP8t2YG6dJPGFIvsiCEYjSpLJxDiDZxqUKZuTOJiblHNvZ4AK3zJdNX42qqdwsRNzLSxyfY4Q_eaUA2QgOw15Q8H3tTZWjYwrsY84yT935PXzLMTsR5_SpoGEWW5UAGuuUSqKnRCHB9oAf5DLrUHy5kZyD8PFsY8x-IGwBXomqrf7wyxCbSS90aah5qBoNOQCkMbUmzJ84MRxWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkuGCoH0WkTtf8PhnIpn-CcLLtLpRxKiLaEe5n1vZmRCJQ1oNhjy-8bzaVaWwyK0X-DdGvhc8oJKapsLeiXh2zZFjNIROZYJ1Bpz885ifRJpdctytpvSEf8UiWKprYJfgwzPOIJtTVUnfq9g6rdBDCRdYHcnix_XZMUIweU5XnRP-647zKQjDrJCh46SCgZ6pZQPDU7WDWJsFbQC_XXnPZ-MsNUaE92mkZCrdUxvRv97z01S-gy9F4-e2w3qIB5WZ3xRi8eXysOh5QORNP7CxFMZ70c2aTACOcmLpzyUgNrrMtqCWaPwzJut_BIK8g7sdDCSXzYOx-LGbkQbZOcGRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faieZdD97T_WLr0SPyzowOmLX5HaGXpfjih2-_C5bTME16CJwSZEYzi46syc6OuQdMS09V_RShJPYgpnXFtN4XPzw_IykUjE0XBpuZXGvABQa-AAa6UjrJ6NcsHg0VKwi27dsJ4NOEwKeu5Lomj40OX-vikSX_6In0sV367T8TmSQgTsZ1jdcp7DL3Hk4SLJusK0YE_ON1N7SGjTXA5Pd5--hmMRon78BUCVFDna32wb0BF6wPfZS7LER14dl-rJJ6a_T21ZSBD4Pi7X9DWimVUBkA0IWnpXrbnAtPSPOyTjumUdYiY1WeG_LXFzlz3GBaVf4BVK959fRVy42HcsCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuFcGKtZ_X79cylZoWONSjuRDuPYMtxSvhCR9y7hp3i7FCrjZljIOZANYuRME-0SbY6e2sFwCYcxgb50F9cARSC_dfLXsdtoOOAXJqlhmyoTAhd7KDO1QcghVEczA2NxV0EZ8w1MTFTGxM3LsDxu_6MEekbf78vm2pzVJmqIfn5_8CsZF7iBtgfnImR-iYDCez-uX8hjSz5aG67Xw0P6xS5OIOR_LMQ4oINNa_nVqSepLlwTbH_6N4N7R0306QGgvJIebQPHI34nBJE-ltHEyd5OobxXPRuVWENEZO4sksRqXrau5ZSJp_xWow-iHgrn1YQRhYABsZ8BiuKiuLnV0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO0Cux9_bdIwcv9UpIWOtTGsHR6x5qayRR60mYAAq-60fSSpFCZP63M12vOFWndSNizwuP_74gJPbMD-ghxGZflefRLObH4SLrXE1JHsfTzDaNSwI1H8GJEcwKKSlqSatH3liIbRurmCvxQ9-gHDTpmi0GRjKd-aucre8eS2bwu5RO2lIvcJCJIIaXeIWWVX_8djW5_01qx5cyLht-JOcWUvJ4js0vX6E87O5Z-vn3jSU0dOgPHcrxtu6G7z5hxvyAqdyq7g-Z4xN-8ea3zHnW8cKSi_d2VfXW0qKSPUnhqPllhFMnhPV3QGNvzuRtQQvvtaygFCniGaFH273etUIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSe7-ihTpn1jngNARR5CeOTisWt4AGQO6aaAeLtENafjV0L4rm9ZOYvtCO2HYrdiddo8mqZLwv0kfW_ITKJul_H-OU_1cHT9mfWdZHKQVv8bjIu4U6Kj-4a-rgEpIwXXz6q8k8g65uXQkT3n7fKx3iw68pwwf7KFGWyqFMn-_Vbn1W3ATyUJFfnb9gF4lTqnY3E7kDWxTXyYgsgtxKgtui_9hd_ICGRulQyuaE0pV-VmmqMM4NUDUtpDhYdQgF-bLM-XwzilWMog9W9N2WQ4bHEA0bVCngyNpUDS6UEYiMMxVX30JM7--PyibLp_GCL3SVNSV3HBhI-PKCBqQfmqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnBdRzsCY__u7aYzZoaX_vtAMs4I-Q1lDuiKFJTrCf-v-Xy93Jc4BuN-8mDbFzftT0Pto6qnvpi5sTIiHNJXeJ1sO40MSq46C5z3LzLWPEod-Ukho-WLnyAlkl_Y7asL1_l9Yz0_LUory-46m5_inCYMfboXRyK3in6veU8fGl_omEc9XE7r4c4C5kqcrA8rGn45G9DhkaPJJ8XMd7KMkRKWlpfsVRH5dHAj7EqVGUZcztjavJxxHJWYdCNrLIif1mQjUI9XCwZrK7eEMwHSBHY04vjeZovkXhEJjd_oUOlKmxfc2KY7kdC_24kc-kfy9gW-I2NZTXZRJ37jEBT0aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRGfKiMXwUBXdoJfcuk0wzjfZo96In2CRYUFeEEivwGQynmtY44zdc1G4UXYNZmILxpyooKucprHSVC5wm2sQRFcVjLxCb75p0jNx9kuN3l_fj8fzaBcWIFB9RR1RwdazJFPsDwFM60YOt1TCSdH1AI_jEPcpBuXiNUCzASy4RX4nJ251_i8pGjWNgB9L2f_S7IYXgpGMR47VH1vzuaogpO6ZnZ3-c7GBhevlgzIOXz5VdaLDBSDS2MaJ8fWbFP40TumEPedqnt5yO5OkZeJO9NojQgUH6QzRFTPZOcgmxceOIkYCUwRDzp6M-OtxqfZMBxtOx3zMyPO_8pMZ_ze8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNCGf5AAF-5DwRrTpGRA6pnHLrev2KnIURuOx8x88UAyu46I5fRTk8suLX3JmpUj532M5IIPaDt1IAUi2uu2IXb0X6Zw6qzU9rOhLUOWTR8kQqqbibXGatP0nyD9hLXrJbnm2OLXkT3BJQIOVy7QQV37ydA1T0GQpbB3S8LHtYf9JlAnxPeyVOyxHN3ToeI0TMEbAIlutUPFkbYdFs02e4G0VZDzVQsZPTbRTznbXksdkKBJ-_mFpG2IvNdiGL8CYmZ2wZKyhqWeH7507Z167IejPkC3yEvV558w3jR6cy9_ElPmous6HNMiqIMU6whThVim2bzt3bRT4fQqUpEcGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLo8DQ67HnNmJFfHWvg2aYHAjF9XqlZW27tCVQiLghsTSI_r6Ulb4Vhd8nwyuEg9Opfvi9HLBNqaYOtLhiT5wRrFFFtKXKGNHppUikcdIZ5smQCUrNzeC3bO111Z_U4L1ytRQvJgh2aZHcdmUyGlMdoNnLlh8nb6CIndwgYdCElyIXWVl30VFBxWlV_0TL22BOTTMIbmFM_z1h9UuaRkeTO0-X4v4m3CGqCVyJeICEdiUkuU4JP0mF2TTZoyoj9KtbEUkcgYAA1c4t2RywJEQ85SciBfft8RdbgBQA1YAmYqC2oneqiofbnaJf4Y6BRzgPMHXEBL1xTHIXxDvgCnQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqwIFx9WYTtT6jveTS9FAXV0ctn8BYNLxsYf5NP7jEfdV6vWRx5MZBojAua2jDj0QcKuu2ZexA-iC3GlWFO5FYNcF--WZVY_ZeY9sCU7N5KX23PQoG7wZ1mLjIR977XR2zB5oagC1ERGqxqL1rhCIFoMeYLSTuDjS9ELYK28gK5Jkk7lN2axB_1vIAKJ3Ywa34OeMm7JyMoUHOXS8Ni4iZO8HXZrQG_hPS-xUEEVFSgGR013pH1SFsC8epEOo1qJb9DoxiuDINvowph9t8vMuEMVGMvSBy3KCBKvhmHH9SrapVhEET5fX7tUj2sAZ9Wd0IMFqRuYIVra8ImwQS0rcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHaCq-9Z1Jx4I4QGM9np-qwZDgPvAhBejvNSoOpjliAMf73ZzGyHqKRix4SD3G5CtZjaf8IE1Ehjr6zca3HATPVA2BwbSVDHIgnYKpjO9niq25A--qp-8vWdrRKmOhbRJQjssd7_VWmZXsrOjKTQCZvr4KqULe7KWLNjE36LgIFBf3wvaas7bprckgL5AXADNfcgT16arSO4ciEycuCIqeI6JTVGufnKmgzobFeoFCMiaizvOQblq6CogD6Y5nLp4fsQa5nzDDEJdfQlYS9uhPB0SHBLl2CQJJEOuHKBPDSNWxPJD6_YhhdQODNYLC3aQuwjQ1G_8DZZArMcgpaSIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTEAN1NvERha9yRt9MPlP7Hgy69tAbuZBplVvt614-L_euqQHoQHXM7bN96Wb2KMJxOH-e8Uv34DO660M_Nfq0HFbqLxyrP4tjhIHFTbzmfOVzmjUzM8JSazvkixaVlX64d9JHEhtenMH52Y7vd3x-chMTOb_OGfY_oGj3pSu-Uc1uV_4C6aPr1VzXb-9_8tvG4op7sdUaVB2MIjA913OYSbdq3T0P_76S9EIR35p9kzc70pWDTy9tHDDJ7xKzBU7qLYR4jJWvCsI9bTqYDMzBQ6eje1mKXUMIGJ34LqGIl2JpywG04YLe7JRxD3kJBBM2c8OnYY1r4zZFiHdE2GGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1tY_SprlGQqHSkXyZV-RCpiCwlDBJlXrE2Kew8MX7FsARJu0nuzAXD0O_UZqjnFuaglvsrDXBI6vGFBArz6tsuceoR5Qvow3e_9YGZXL1K3HL-I4rsIwJrKhc6hVMaGbmaRt6TgZJRNu1kwj6dkl23D9LtTnioVAca7hiuiqmYUyW7tDcbyH8Er9D_0aGB9Sb6Ze88TVDZzQAyo77lAFpSfx3zfClzTBGTz8pVubw91Otopb4namyEijQ6KuoYPhUrVOwqoebazZ7-mUutBViTCaYiaJ0acVQWkwNl2t8liEuKM7jnfDAMddVJzBogKClwnU8_1wmuMFTtwlV9y2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZOkfbLcZx0Xm08G4tzfcoMml5uECXMMQg4mqTE7mxQzREyswSzW4s-wo_LyWtLcE-sTujwefdOmfmxRUN1bcbwa63kW3YinlzrFle3rswL9JhWsLvX3lte-wv2fyttqgW8Kv6MG98odmTXSp9LPNRkbwslQv3KPtt_bRoZdV0W2it5Is3sz8X7Z7tS0k9ymhTKS_40iTyywoOuZy6DR68wjQpfac6FUDRtkuLzizyMbp75o_4e_pR-iFBHZbU8mO-kGZ7uXKCdKemEJBJDmOZjsDEau1eHw-5_Z1IF3l1XnI2c3-i4syeJJ7BTy562MmlXa8Dq-gF25-sYMdAT1LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev7n7B14N8zKApqXlUqKcVJKCZ5FqUFAZZs72DrAgmPwp6YuaPIkzRGKBrJa1gV8c24ztoVivYRbOjXwFT8sS_baqk4GTWihOGk96ZYXG-DJEtEIx0sFxXOQKZZPxCfItpNeW8K7xddlzxMEmsEqtX_MmbWZjwfU2ERqh8buRLlyLc5TIhv5JuFpmSkCxM463KzmkNE-CX0zqqh1ZFwE_vKoYVfjirVvv86OET77fM7rJOUbzSoV3HlX3UXDqPHzS8fMJJyImWc60USmX1P9CmvC4JkP_6FSheyBz3Gf9JAhnnw94UIOcbE2Qu4-AGwAgQSjmoxP448F6DpY5BiQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDVtgqqQO-hgthViJ0fg5wqcBFkiOZk5bxRdEnozNOq34ZZXYIlQIqvNG0qOFcPC1KpWtWmSUd-WY8DKk408HOPgdy6YG_Gf3Doot0JpEwuVHkdYeuIWpbvHE8fmkO5ATUwTBPs0YI1AyUCohgDumYWy_Xn9TO0xD2B318UbqhVU5q7oOgVp2C41fVCJtgS6qs8uY5RcY56y89jRuTWtlVfj-VN-2OlOMpQDc3FYRbHif1kOe5G5-sEla-vSD19vPrZYcuUxhOayRro_E5NY08D-ZS1BJJ21QwnbPJIP92gFxqvWVYZhFKWiP94G7J5gtuZUhtOisE3ubiNNicb7Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehcLf-3N8MvwrnjDlDRHXhovpmKXQxRAlS-WDZDgMilmBJhnD7W_B7cBM4CfYQ6gEj-RdqlPY0R6EFIBzwmSh-llvDwSUXFXe0IUBEH-7rPmaaLBQrJRWGiicqTTmhlB4Kr5uzf5fV7TbdmhazxK_fxzlhlAUEY-3hSpvVTO8CrcnAbEVQsOEIknRes3V_FEmUtKocbeMXl1BCuy7on9p3vQrPMQ-qqGcmpmJbNT90V-X_Dsoj2pDAIW9vu_cpEMI6xbMOn1-n4oFoVz4N6qjbxn8d2w-CqswRxuv-nqkmBN-J9mePY946jRKYiX-_sg3tHMHuIw1ssWh_e6QT1y4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4S7aMX4uyoTnVUos4J_szaQ0QdpfGOmKIPDEL9oujLdVdeieV6_SIY23C6H1U-sAa1ZwddnNg5hamx8FDuNPHbrm5z4xOpx1E7ZRwFNaCnPDI9O4my2-3NXfk71ZuVBufQhbyiHR57uYk59ksZrMKnG_ApKXvnIUgcFqiTU6rzEfGQdJLycuYh59Sb_KM3-IjZp6UebHOgpr6yttnaA2bQJpe4IJQyfkdTh__MMT6dawhpXnPTaqCoEXUsWevFlUhTWSB4H41n7u6dX6qVLN_OAH9_kAwieNrhTzaTuRHvLLVthWI0mhMm_KrufWWxY9LJHNnMUVaEqt-jCZXW4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6hY9UbLpGr-dSXcuhhsduQW_qnl6DgZIWGewi9QK7kZhizMr2nGpR0GxGomNEoGRHscpUNccZ57-71oq7hGRy65yBqKRdOWMYhLo3uCilrkW4bweZUJv-Ac51p1AFtkmKfHmxUHX9HUyINS3Z7sOSyO41Jx3Yk4B0e3jmjNLwaggZU_2vn_9yNhaXdesn19tLoKNb0SM-DKuxTDGmLaHFLA7F_sI3ihy5h5se3MsDf0UXsdq-olcFejQ4eXnyJp5gZKx30mJ9W32iZtsLhOm6n2e87fcl0H1y0Jtugbz-BTQmI_uo_vOALexG2EyWmxjxucpJDZvK2IhgWGtJ0_dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suJRSPKa_rQ7bu2Tv-YyBG2Z_09hTTBjowic2pm1ylQ81RbASnnOqwC-tgC5xrPRbYkQCJuK8UJKGaD2Oocn3m5qedaffSrsVuUuK137ucc37oiowhA2B4EBHzfWHb3T35vMBeyZrH3pJXheFvVfpkK_ZHcWHrYxOJLGmI17IxJohazGkEgzMFMila_484UjJ3JWJDSmA1jeyl1xX2SHed04x_eiL7n5QhdX66Hfayecpvt-a7FSxmanjWilVx-WLoP2g1DgfoTYekLrF58qLO5_uPL28q8N5Gmz1A1he_6WXTSpFHkeBXmFBB4X7dQRx_sZuweBPsjqWQ52GC4yZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqyj4KZUUtN0NPAgjdAWsbxDlZsNcarPeIWCd0bKb3Td4dXLhY1sdDY16ElZIw28QDJTbzyjrAo_HRKRfQgloHsuWQzSL8y0u__Spmsrcf7FTsBPo_gZL_eCH8z3PhZRodf1x2o3HB4VyRAO3GgeTqvCoOQNpWlhL3pvwzmw6aS-jj833pzgQSnDVq3SCi02H7V2SxKC3Vft7rHLC_Ibpr2w6SfEI5zmD6jJ81ZoelEoeok4SOF-JaC-EBIWMVVQujEM7TW4GqNSW8pdKxLW2K8Um4GdQwJYIEYK5KSUboq2P0pNiaat8X84hdx6vN2PlBI0vEZ_6oC9yOhFD7mYnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSez1lDDlfR_SH4PjBc7_4-dRlP561-VnR8cxQrhe1Vd5qoR_lXTVS4ZP_Px3-52TB28mGGsV-vM7vBZPuBP7zJNzbh93ceKjpxEXzCKV915ZiVNc082YmLNHuPXlK2BsnFsXIhvok1fNLO68ETcoyTK2i_pAo6Qc8Nv4tKF_yGSa-uGAFFoaCnxvT3r4kWDgwKO2lhHDtVrK9J9B_ahaPhUnhuK_YUVwz30dfzII8Wh812w-U3mYF2X9m9mSCfV_shOOkeEDf3syj3HRE5RSlXxXoaC8yzJfnutEA8AtC5niVzSrjYsyRDd-_4szUvhSyrF_px8-zDW3s5cUnzpPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ayDWHVTMk5zhQZD-UOqRLYNFzMLTIRKf5R1JxTi-X4CSFlFsuBDZXjhXfAp2yQzW9ssxHY_2U5jNu1flpyQ_baEvFEyWcEj0FLVpQOHn8HLVnTdB6PGLVP6OwEIQ_zlYQhp2DPA1ZToc0EUgk9DUYnDiMG4_KZh6s08wX7mza6jo3VH45bVP63Sg_q3qhMHJ3zuIDt8ngwev23B3GGMKToFIPHDOrVoJHWtZz62YfnCGM9Buue_d_qkjA1zBwldwPkDy_Az73vNQYb4G8U2xdwvOibzmgAgfMwZ3R5XTVJMfxqqZef0M2MopJI1dLtO30cP2pGk5hJ-6lanZmNRoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX1qfv6H2-nABD5GFVk6VI_1Xh8sh06sg8TG1mjAObuyU_CFVwmIQm07n2sO3sgcPP7wsznxmtCl4DkgG7Ysj_x__yACfm3Sb_CNMGoxLYFTsEsB11yVJATW1hku4Y0PLgXtZZznru29atIJiSc6oR5rVZBXC2OMAUt7x3s-c0ic_zEPvaHXShVLcUDsBclhhq9XPQHAaSHjgTFO6pwRav-iyrTcqCOco1w2OHzDr7kUe6kXM3NyrrE-yq0GtKodN5LXr5AKLXOv80yfMP9kP-7WZMsiYK1uHT2d9Op3u-N_RMUX0JEKildBj-P97aIAnGtwhR2uJb5nfLiqubqILw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxx0HNwQohWRbs5XnRl1ygjTUuGP47cEDTIGVaP_Ha8P3Zv5OS9r01T6lGsB07BrG_frBnleBXrfH0OsWCLRzffAE2dc_W7OqTVsE5U3_tyhcBLZ7rwfh0iSCciDc6pTY9Xw-0Lfyulb-WOiOzddUa4xk376ezRcJxoOAmwIFBylAyzN6dJIh67ryZ2Y8y1RhK6ZaJpIM9i3XC3IejTUoJz_arLfcbcHm6iuGU3eQBLsr3TZyxtsKOVbGaQMvbYvPH5M8TDHmIO0cozYne3PqOvMQa0qX_NmhZwlxzbMx4sICfNLqjm5Qaa2v6BtoJS-rN_tnJfim_dLKo1Q6uHL5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLhyeHPRot_oNBfid1nv5mtLH9JElF4hIEJVTvtZgYQ9wLeVck5_lC5_uxAlMaVv7F9ykWHrmhQTh2OxXal-AU2JRrEvazQicNACd_QN_GB1TbzWJXuf5ewdw7cJHcNuJuRZQilbpc_AJLYv2_JEQxJaPGJ7iYqUhH5sA_Ich4h2e4QiDkPTbAMAyGvBCHZYMD0BSN9wHLupdPEE8xavV4EbyoljmPx9GYpyn0uEzRUMSAi7NHerlSp-n6pu0-zBe-yzt7IECq8wGyMPfit0vsO2UwE0X_Bk_XvtA_bMe8UAQ5QOBZ8VIHU-ulGucJR5Bfifhavgkd5Tf3OmppYAiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi4N9CQX9MGU6-XRL_kLsr2QwoblhIML08p0rdSydabYjjyQCmso5F7MP6UDH-ppzpftf3_UnRdZbb14xraM3SZkhNSNlrRolnwP5jAK26GGkVQCpvm3k-Xz9Im5PWS8QxZWFnuszOzbadE7xmJNZ68WCBkn5_GIdUsLnq-ZAJXMQZcBMFSu7OFZV5p6b3xFc8_neBfRs3ZVT1Ff-PwnQbZrOAHpyjYexYG8bIOy-i3WLX4NLNC3Xn34F90mq3rwepVet3Mn-WU8LIvDLpq5SnYo5dNgFaJjM8hsn2ihaqfA1vdz_pccmSZOhM2oajvZKAo8g-hidFaNcSaTj4s1JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbvx8cBsMK55OjlRAKQEiJYSoA7xq3_Lgt1vGczSuZ134XAeumfGexCIJpH0DlnWafzKy5BYnIR_DR6kwsGYPzdy8Pn0-a-ffMya0dkJCTUezzBMjZKKLTYuoZ4VB3v7rmB8MXvcHtRxKit72C2IUCt-Qu4xHN76ua5XxvZ3-vG8QikReN2irM3bPzLaoemDJ5RyF05bm41t-aFn6AsCcllDykzVCbNNAUwtKDlhXWenllYEN0GdM-G7n2vHvjD5GhVb7FIJXnjAYee-53r2N1vF-C6gJ8KdTpSL5QreNOEzvPPQ_QATmxvcYSKN4o5UM4gTljTHXwIX4VJklfuoNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dsHcHHByR_o3qGsuTl9aEu4KL3IXOT67A_P9eYQYDlUGYFV1iTE0BC3n_VhJkU1aSVbYv68ABzpTAMQoEcbF2XFGNkjJN3PMvugTZ1cryjWetIsGP5SJrLD1XbLWrdfpKulcGrFDPFFXhCYioWTUnrElOx6VlDmUGm9pmgCnK9nhESQWySIO7e8lNlRikXz5Mt1uaTpJ22HW7spiyObJES4zK1E2ElXo-1ytSiKrPqMryoPeQ6VjFu7FbBZIErFzdAga3R54KSkfhYcp4IrBs6wJMrY9un8Oi1V5iDy76mo94I6DVjSihY4gzDHy8EtowQuBRFc0NXhadTIguo-96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dsHcHHByR_o3qGsuTl9aEu4KL3IXOT67A_P9eYQYDlUGYFV1iTE0BC3n_VhJkU1aSVbYv68ABzpTAMQoEcbF2XFGNkjJN3PMvugTZ1cryjWetIsGP5SJrLD1XbLWrdfpKulcGrFDPFFXhCYioWTUnrElOx6VlDmUGm9pmgCnK9nhESQWySIO7e8lNlRikXz5Mt1uaTpJ22HW7spiyObJES4zK1E2ElXo-1ytSiKrPqMryoPeQ6VjFu7FbBZIErFzdAga3R54KSkfhYcp4IrBs6wJMrY9un8Oi1V5iDy76mo94I6DVjSihY4gzDHy8EtowQuBRFc0NXhadTIguo-96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt4eognCP96Pc3lOd4neGlVkurmZMKQ49IkM0R_lWt5jIuD5NX0_aLnCAtaqm7pcwpQFgQv5cUyMxrj3jXtbdY5C5cJFNVpBnshoT2mXJF6eNK0-tMv_RUPjKYWwDoU5JDFbED8jmEXRBDq6AJMmS26LZ7CCwYecjSEYOVbX-0aamG5LO9909ju8M63caaTLP8sy0D8S_azepzl7bRka_dmUDm5HiXIU-le35zSIE2YpR-0a3gA2UlK7Cz8L6tgfk9bWnktVuYg0i4d6ciRfrU-mDEWfqBEob0gGexRNKIqQwTRMPCP7lR9Q3w4WPwHVq-hzWOo4MMgX63MU_3q81w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6bBFhN7YfVmaSwKTezezZGPNNZVaVfHFJC54EkDjNu1B64yhQIn8iIGCZQMZdGCkaJgccvOhZWHio7OlxenenTpxHQJ7EMwGdrhy1HsWoCFlt4G9ES2aeBDAzZ9Bw1NJ9oHoTpSCnN_FmLpDgnbZTI5exSiqr7mMG2vtsNciI_r9QewkPyqb3CS8iBuV-pYF4FdZlLvMV9l-cVEEOMqiax_R2zcLmUXFr0ENeDv3GrpmwK_XHMi-KL4SLas6lfkrQyKiZQqU316FIwz-cgA7jKJU7Z4SyKU3QgdS6KX0LFKKa3w00gGPCWBTLYpgHF7wqKHqAiKsyFNVtN1s7fGXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDSifNNUlf_2-hLx4SdzNjM8GHXipTgpp1--s0tveXdKtN0vIdjNcNSO0UbLiQsQoFJHaFvD4LkD6au67I3i9mNAwAZtUJgc_L8FAVwHlquaqtCRQDG9KeqCEpRj8eSpcq_lrQoOhTgmjjhIuhRSrkOBiNP4QXTCYBCMxXefrPHki2ZddQyTgOl2axgzf2AEUt0TFxKxRqlFCvcuKiSjRVXyE5GL9xJdT1NQ4cQBN-i9nOlL0gD-eIdco8aj8a47eFX0KOcy8jqsaUZ6qbkW424ApfN0_5FRtScW5q_OLfYQuDD5UqpIcwmy2voiw4QurJDdbwPj0wZq4KHErrAm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjQ4Ds7d60QJEsfpyhFTpHYED9hCD4046FjUmHcdUXLHK2ZSaEtuww3bm-2vA0j_mcOQVAm1fANDYDRwKMAuvR9bAPf3unyv6bBQAZ27sMN4iPpG4ge3ue4xTclXrdN-4qTY8z6Y8m9G5i7JE943ONrBrXuZI0IojW6vhYKAb-QL5-ea9J6fufb8cKpCRBVeysYibottv1OfBUlAvtsGPNjIhrM4OtmsLO5-BDLt3OawejkWy3v1DzizY7sGSvvwBHRUOGhZl7IPV0wgeboT1blD7h2UQbVQ_YCQut6jjirKqPCWWBVByrWTQa_Q9WIpolZ3j6NfZrH2FMukKB8p7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCFcf2HklO9NFpKYEWh2WfGCOJFx4_xJnhOCfC_ljlj8e9ZC1z4G7bBUkbefT1dqvs5cnpmtdtatSh1zWtEZ5LZqRvpRwza7ToxoxjvftAvqaH87x0sg98GL8bKNdSjpZG7hyZeQy_hm2QESG7VHaQ7nhXHXH63UI6JZC3frzg5iN22vSe-miu9eBN9SKtQwLX_pu4b6N3dL-ZkHvKnNeEQh7BNKHNcbt_R5hPxIbPb4jsNd9h8FqHdVRb65v83gzgGaZuQp6YZcDtNSrzHq5dEBMgFP8LHTCI_QN7s71XSQGuWNxC2DxauktNISpkNBu5nFje7JINaJXdbjV5z-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/piItp7SzZqYHiKBI4riPdKMad-Qa7UVpSW6HuThupWrl0A9ksbIlBqEaLG5UntqYlCxZ2PhkOTA87U54LSLTg-6TcrS-AFHzacbhKW2e8f7qnA9ENcEVGURS9qntAU8w5QvwLxTW8pe9-07AvfR2fqHvGZAdqf00jjbCJxFtlhPHxB7oVzK8WpePurMXPFAyVaVuxkiNcZjTf3Xvlyy6EsHximJOrcv16RTy1YKExeFLL3-lVwts-4SKfNXGvYy4oTwexF1lNEqgLH_7kOFxIHYQ8iOyfiSXwperui9_-FfaFc3UQdmLJN0Wsev_iUQvT3x2XRAm-kvYyEd4QYaGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/putRxRAMV9xcKg5UReKm-5IfeEBWZYtY3h4Q5SIQuzky1NdE9HvdqtmnwBy-ePB2sMBCBnY2gnRLCO5yHLPDkIYjeXgvF2c-oN7AloRP4l98DSXUeI-xYLHPB5d2oGX-x47-N4Gvi8YeOUVN5QVzR7zVHM75B7cwGy3ekvSYhs_7NdKcMPT7g_n-Ctljia1euc0AgHwngDbfAWP5W1lkggmQwKt7gBU6MuBoMmZIBy4GJIza_PXHXOx4GhuXr5Ny9iWVHijK1wJcagtBfygzcjDyCf-z77rIvTZFQ-ZEdYiBcsraaxzSjUHOPzwoVpq3cCZgUO3sKjUOhWFPfRXUlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=dG81FvaNRmKE3n0uUi56mX7WdhousN3ORoY4e4V08jVPGJNJqgDwVX5tzJH1o8PxfKkQ6jRh2d1q_oc3C-1d-FAYvORBahfZIn0G1cuAWBO4mVlPVshR76fYn_I1nVPt3aKoPKPuuOjO8gVCPxfNHM0_o4bPKYHeAwLhuRH6brwALTZeACpYaDfhDTLmtfwfjjPGSzy6HJ7rM9-LSqYn2swAicq-KGKRZlqTZM4ngwaC_XTZuiVf9HpguBZN3i1ST_bUGEr8hJhvpMVwH9KPUegSo6jlYfXK1U-ek6GEmzoYghgjZmUUMCSMLoXH2YhVfaOBO-KwwEJQ4hx1TdXqK6YFPUvd4xpT6AFzXMlvW5MJ23SI3zePYp9ojyqKF830KKo971AIh5FzwjKq31eeXp2Ee4kIDD243sjCCHEk5icXcQ3dp028T6CKIGAsQIES-yTGIZItXehwrdmjAODNJ9Htby2GFUMWj-l1wvbTX5pJvT51KUNhTm2qfLlqJGEg6dVlOb_ZSdjLop4G5dzIICEvtcwTNO2Rtn6-61ScS2eKkVT1_Vpb6o4TxU8jayIKKwJsYRhwOZT4jbDAxC7rGwTVo-WBO5Lz_0NGPwhDqows45J0bQ1vuHAeL6fH9hQGtPq-d9CaLjAyriF3R9vHj1kTSqpRI2Eq-cJyPHJQjEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=dG81FvaNRmKE3n0uUi56mX7WdhousN3ORoY4e4V08jVPGJNJqgDwVX5tzJH1o8PxfKkQ6jRh2d1q_oc3C-1d-FAYvORBahfZIn0G1cuAWBO4mVlPVshR76fYn_I1nVPt3aKoPKPuuOjO8gVCPxfNHM0_o4bPKYHeAwLhuRH6brwALTZeACpYaDfhDTLmtfwfjjPGSzy6HJ7rM9-LSqYn2swAicq-KGKRZlqTZM4ngwaC_XTZuiVf9HpguBZN3i1ST_bUGEr8hJhvpMVwH9KPUegSo6jlYfXK1U-ek6GEmzoYghgjZmUUMCSMLoXH2YhVfaOBO-KwwEJQ4hx1TdXqK6YFPUvd4xpT6AFzXMlvW5MJ23SI3zePYp9ojyqKF830KKo971AIh5FzwjKq31eeXp2Ee4kIDD243sjCCHEk5icXcQ3dp028T6CKIGAsQIES-yTGIZItXehwrdmjAODNJ9Htby2GFUMWj-l1wvbTX5pJvT51KUNhTm2qfLlqJGEg6dVlOb_ZSdjLop4G5dzIICEvtcwTNO2Rtn6-61ScS2eKkVT1_Vpb6o4TxU8jayIKKwJsYRhwOZT4jbDAxC7rGwTVo-WBO5Lz_0NGPwhDqows45J0bQ1vuHAeL6fH9hQGtPq-d9CaLjAyriF3R9vHj1kTSqpRI2Eq-cJyPHJQjEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUTh7EJ-vcHnRs6hPP3XHjtxXBfswFpsOcPXnAs1eBgb2JAEHX1cnIhUxEcKGgi17j6b_MfsRrGQsXYLQemO8ZLPZqLNmuiHhbm8WZPsrAnSGF8uSyLR0Cnv2fJy-DO-P0mzyI5jYyE6yQIMVw60zeQ_kG031x-p53QoiNo4IiWviQ3Uv-mtY69BKnDLxEAtWlrinXkd7_0X24rXVw0l0hQqgQ4IriOm_dMnXcziSoPUng9dosB_XbIDUEvELpQ5KvZfcvTDg1RVRuWwACfgeaPplJrNVxYaunoJwoXG9BZ4PuwRxZsuuvpwdMKajWAUdqOQ9RAjGtj0qXz6HD2L4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmBITYVHy-ExVDwG8Bxb-xIvgU6EOiWxoAnKM4Qips9Puda9FWEY7FGjLKTwXtQOWmpvYUfhtbrtVHunAl3SxaMCYJOos-zvh8KY9cA67ldNrlRiJ_R44j13gNlEKrgz0Eq4YySzTFo818O7KE1jHZlmJztUpbPhAdD4SZErQXV8fk3MZLFoxprNdvYEHV66Y8dEENvioVJa-58MTbgbpA3kBaEDgVeIN3p0ZAgsDguqKh-VymbypYdOcUHpakqbRNpQfBIEtBGbE1sDUaMch5DSWdDirLiaim4PtPZm2p5XHyFaFdnMA9AYzNwcfq54RdvtgOWS0Mz6hCH5Ro1oAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcED6VLlsLuQs4j5tehzcjMntjElPIKnnnC7oQqmTZR4QnKGINoRKH78duC3-kzo6VhUMt9wd6Dax8rNFKrHlleYIqP8vmWMv-0O4Kwaz3LzOIEaqlHtaDqFErcxXLReCCgFejlf39Zweflk4jDWPNyD2iVKJTjqpSAjJVyXYZrjIJ9n7xj88TUZULCkdr1d97F82Gg5BYAeQ5fQ81WB8Dk1XtDe-F5QX2bFE79jP8IJMI5d5ZHoR4_88R1sVBrp42xRrZQ886n4bjEt3Y3Ncfp-_ZlFNhQviAQjKMQSXGIG5Z5CmMDAjgTSzuhqAorYkmPBI_toQienOXVPG6RQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dytDnBwrK8i13AaCVAXk99IKqPqMDHqLFSHvLpj5hQQhwANz_t_rYU8-B58MxsgOjWs701nMmcKaFWm8yoPjqAh8f9NBaJoBHIaNDcIhQdzNXpDu5LvFzhHQiOzhBkTv1GiI10eDcZxvPAvZCAyaODgKTrscQLUc9iGEFWFHTheNsciddxip6CDl4YrWel3_miL0PcVsGuK8oQQ9TKvrY0saBUi_VxusUS6HYJNBi_kU0PtSlQS22fvRen4ppRn9piUeHegx33AcIRxnk4l_-f--9begMkNMwUNVhTNcm9NXGnUhRLp6Cds-pObsFY-ycmceRFiYRGr0vOotN3AUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PpAc-AXvpCjyS1h20p6bOr73YFwF9BJQeViZBFPsQ2l0DHAoP7uVd9xmah0R0eR4oVeXTZe-Cs9vsvlvSrek9SAlnZGEdU4HqfkgEaf-rIhB7Q1spGK7CvoyMtM1mv3gYOP5C_hb_esM4qgYByb6WGXOdF6gQtsOR4mEEUsJWMrs8TL4O4S8x6CSyikYBgHSCr8NVpoFk9HXkqNSQhwSx7mGU8nFkReP2lMaGrAiHgo-zLQBHlylSnnBkRGgMp5b_Tnw1NH_ZrFdIy1c8QYt7xha7twcg0ObA2eN3NQ7Gr8m3hPN6b9rGMJbUS_Tp_YJ_QWofz9TUmA44FOnxF_bSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZeDBzzwRPwXrgnPWn-csU2nlTtFb9uhA5oqcF06wnPGfb_aNrw0ZKZsPjcicjP0WGDkvOvJY_HQBAPlyQ6uNbJI9wYV7PYMz38EBVs3T6SHfy7U-gNUTj9t96vjEkrK8Hid4szO5u0aCvoGZC5oD6xssvO0SFuCI14rpHLaSMJHY6Nj2bwnW-2Oouv_6hnpSaeFOVVfc9TlxLdCshJY5agw5NtE0uEHhCPDgHaU4zO0Obeq-c2z7fPTHH2HnfQEYwfkDB1KknUaTFIQaLMRls5MzEINt4VF6Lj6HjldjfY-xoYl1WPAo7UnxCnpnSP3eEIF1fRNfkKY89zCleHQNBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZeDBzzwRPwXrgnPWn-csU2nlTtFb9uhA5oqcF06wnPGfb_aNrw0ZKZsPjcicjP0WGDkvOvJY_HQBAPlyQ6uNbJI9wYV7PYMz38EBVs3T6SHfy7U-gNUTj9t96vjEkrK8Hid4szO5u0aCvoGZC5oD6xssvO0SFuCI14rpHLaSMJHY6Nj2bwnW-2Oouv_6hnpSaeFOVVfc9TlxLdCshJY5agw5NtE0uEHhCPDgHaU4zO0Obeq-c2z7fPTHH2HnfQEYwfkDB1KknUaTFIQaLMRls5MzEINt4VF6Lj6HjldjfY-xoYl1WPAo7UnxCnpnSP3eEIF1fRNfkKY89zCleHQNBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgZf85Z-e3j46bmbvy_PzV73Y1vVnzzbuH2rnQY2oDIxvkVL8miZwXm0xPIF1VPfieGW665YrM6jooMI6OlwtD6dNN4r4hjz7vg3pjM6tFkqqpL7zfz1-SnIMEYMmqERwtXfud2kWXNJx-bbJCxewFUrPM0dSF_UbxKiBXUxJ3grV6rHalngkXWY0lLU5fOHWu1w5cWiRQEzAqmcNGLYMs_KZv8iGtlcMcXxl1VAiO-SPe7oOMQ3UY9cU0SGUH22oyEqB3Xk8LAXRn4JLr2ZviadvS_XARdKCH2V7Ru9ZldgelItgPd8YYk9mvHAwgUPFR0SwqXdLgLS2a6cC2Fvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5zJhg62-YDiVrJp6V-bd3UZNtz6pWjQHZ2WV5yhi5oTIIgwdawxmHsbg5viE_1VKMlmn5xGE3fn0P3yQGA1Bmwg0MPu8vr2LzWz3QCtj76S5SmhdJxnD_Wo5jIzPMUygKAjjVvoANYeN-toROEQ-EFiOjsRqjTsGMjUzO9-xlQyldvFV-8dPnnAuenv8MXi3sRIUHaU2Ra70rPX0W2xvASlWwKtKkEVls1mD3aoaWp-nAufkDucv8vVT7l85Thu6aXrOSq2NWXmVEphTzsZU1T__967h2yE_xVkRgsHzQV1vPqzUphxiiOkn19XNzpeo48-4vcgCkRT_Z0OlhUYXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk3cBfbya_Y-S7fyFCeGaUwkBA-KSZ3OzcApuPwseWj2_j4KJOKDXeIsp9PWNQ6_Tnf0XrTCfR8rqQITWxmdRCMwO6ZDL1_sC0fmEcLoA2l-T15lUBN2lUEabEDZe91P3YDly1SmEeJ_xXsFKJYPpUlmN2a7Ux5dVZUxtn5fs99B3ppznTozXZglx8Tomzk95hxCNfIvTwW2lmro53d5_x2FGpW95UlslPdCN3lzfwPoJ90DahN5XZJeCIlVFlIDW-w7pjdYg5RZZxyHF1gFBhrnexaYbQXQamlMDmJ2b6dCanfV4zd72adMDmpg1iZj6CUQOdYw57fYcgDNusCHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXkhpsiP6ptRH0_OzjQjBmWDOipSCtJAMpQpwoFFhcmzhJcmUdCnxcmDO5BNbmB92AK1Y2W2_s5vGvexOqARghhK0Z_iT-wwWKsxp8CvYGsl_HT-ynhEv48I523U3gORhEo67JWEhY1CcP-Oy9-Y6-l5Gh5rjHQq-VThh_OhMhaMblmWj67MAN6LUws37dl0vYS1vB9otcTnPnhyu-DW8OY8twR3s8YfNb2UYo10xT0PQPugLrjxvcneK-QxUb90y6QJkQt3pFue-rMDClJyp5aAgzRF7-E9dVplV_dZLGXZsvScVmIN4ndk98E4wZbLAnkvyAMcMNOz2FeExBg0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxA-QGl6-x7l94aoeKvaTZIx1nwp8HB6QqU-YBwvxwgrpMEC1QW1jsiUg6z4LuHUqD2_vtBG0hAM85Wa1N5wQgNg51ID08pFxMgO_m6c61Y4xkL1dxC44pAEOC-P4ZfEK3JsKuFGVt0C04PM-K6x8D5k18bQf4TfE1lrmkOTj1Rfd2EsuFTe_-um7DK71iuqxxwDM0RvXH0iuWsMlIyZQorRHStT3dTsiOVsGjiOFpqEO15eODBbaVaWPy6jVrC8cLWJU4u7z3SZ2LZzMJuY-Cdlz0gqiCMmRMuOpxDT485vV0XPVzKHtOTYYcgCiudRGOPlSW4NbS2gUFDXXQMPgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPOWiTOdVxHyoaia7yqIhSsRAVPu_x59-TXC63VCRto5BGZSgTA4L7dWBdI48rxYs6MoUMWWigu8e1N5V4WBNMedrUPuZqVm2OuZXW3SloZtKC1-APC6npjH28sCi8En4o1Sv7mtk8mDuY240uJembdTrmV5bkkV9Nfs6qth6FL72Mu1wTxvXxM2soBLOVvnopPUAhwJz8gMWoZR5FMgyJJ4_V97S9wCxBY7c2ZAteEg7BB30jxBhqBbkcny0_KljzyT14XCjDVlm1hye-KYFRLk5O4SSNr1EKgpj1cfX0TzQU1qK4EwvggjdX2F0c7mYuJTIvd76uO__JL3TY4NJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">elementor-pro-3.12.2.zip</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/danialtaherifar/802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه صفحه ساز المنتور پرو
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/danialtaherifar/802" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
