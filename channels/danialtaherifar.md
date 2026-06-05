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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
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
<div class="tg-footer">👁️ 254 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 492 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdzQF5CQH9l7hUdcaFXQ3dJtzLRQIzMTUw_jhp54PSYKhse6NYhbPsq3B-PXd7UHEpXC6fOKbROiGzSvpxmieRHUw3eX2qlbsxDwtReUV7Ut1HZq9R7KiyTZWQUSf3xTN4CTfO3ArJ2SyTDidVu36aAxnKU3N2TDhLJW_UtCYsp-tXAjJ7TXGix_vVO2HwMM4q6uBEhl7iucoZEFZ4c75Zzl-3mwTV-Ty3N-xFokbmaUZ4tbFyaUtGApoob7cRcxzy6jQl0sS8jYmjpUwLisn6r9apnxBY4jxImfGTR_EdpltauFYiwP7lqgFBOYCNpbR-XeROKX52TFnirKMH0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 896 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcqHt9HNG8ToQxba_jL7SRt2K2ZG4EHweKkTffWX0z9PndtBjTEeh-wRZClwXy0lfxj2oMwP82VWtEV_YmkSlT23DjLGaiVVKr71wNExrQX2DzgBk9nJ7n2cPUHzNPNLB7O5DrOdjiVWgTA32fw8pfDJCmK_uWcBlU9yS8zbZUWS7ZnRAjJPPA8X1Mf6v3np4ilsXpTa00vW__jUs0x5E0wRadVl7QsrXRtUh7ZGqR-8LVIiKdwwgfwEdkD_sxRytCNj7mibZ5iMDh38vhAIMoGSmLBLJgICrsURB9CObrnKxFgRL3gwDQ1QW7dqRTHN3udpBj96234OiebfJ9GT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTEma_ABqPSMwSNm3ht1wyI0uikMnqB9twfxMOkmFOQOrOSKQeXRoJki1sBzdI4JzqGhIstr2SkuQx8lV9PLDWOtkqcYApJXKRuRHB7xdemiKaJ74lzSqd8edQw2he-d9PZNHZ1gsnMRG-kmq5yoE_Q7vFYIlWPk-_AVL0dWqOdfNcZ4SRfBeBKemFYUT3FFmpRDdiQ0pGHBp1xU04_WlichixfAgRPP3_B1SmzQY9SBcYByXcp9ROHsBRHVw5ZiiVEqff8gNIC5o5Z985EW6IdQVbD1EIJoZ-BEtx4s_Qea1aV3b38c8aYb-KjqF7EEJfeX1dIyzUUBqUuXkDYzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqoax0O2HIM8a51z4O9jNtb50-XPUpBVrL_FAxePcfu3Af0kKZ-Tb7yJd_vFr_TzE2gTCFb2AGkJQb1dCUkrzJYJ_DHXSOsidvI-egQfgfWq0O3XcV3tjQ1SYICMxdvP5fdtYUOSB9FEq3ThME83ZqXp4LF1bwhCNNkS6OTnWiNYFTfSYc3bp6AYexjTpUeRR0qb1-FFrqUu59deu3zKQaggC5EHBinq4HRgJqj3fgPVAX-l5avyoxe6Dwuw7vBg5djS5Ob1aq8e9tgLMuIxuwiiOn1DNJkbjLtrUdyaTeCXXXFacVTowl08tsfwCcXNYBAForjwZ0ozyy8sTKuc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 840 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyXjqCX79ngr0ZBglJssP2XTG-A4U3yGvsRBP5nVhKrH0lXUzAudL49p7omBQg3F37Rwk_S-fGfbagOMJ4RFQ8cwNbArk1Pbp7Sak2nGQ3EC1KBN_-Y5DLjkKYIb_rAtaD5sjbXu7za-9AjUBDQ36JFEyRjZs3_ThTMHPaOcs9tgxXbHRAaTuCItS0zXO9pBcOtvKsHGbItWIl0gueQrhg9JsDTTTtb0GzRcb7-2nogpQspcg-nhRTQ7yeHOmRLtvDyeFZsA_jYsNb8URMtj4zlzlzh017EhikBYSMC-mrf02FZ3ygAD0dJzR3jo-NQM0KlxvrZj6J6YqV2D-_0Ezg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 663 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArQjgvQ7SSNolaAokG5AFX0AOvQhoF7ugo0UryeWh-QDSEKtvRPGOPhzLIkYvP3768F2uiegQiyA6QNNTNcML4zL8u5Shv0NL5yWEO3_ecG2lPjRn1GuCWPeZPPRMF_OrQ74YFBxzfidNvnjzZtLtiHpwCkV95jxpkQkpiA8D7mmvfW11OxcDxSI3QGz3JgiufVEosds82SzNzuBEkzqyd-zA1vETpsTD0oyuJXLtte6uAiZHxhgr6EKhcvDKRgsVUNpyasC78SbAQ59PHi8ZnlsGKqQeT8-E8uQuEyuGqaMTShvoTwJgymuivQOfQ62vdufekmPp8vqB5wiiXvcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW4O1I0RiOp3y2iSeWGUp0JDbZKfS_0nitXMvHcbgU8XtC44LLOAs-F9t4fANzWjLonXV-CQUrisEHIel5-Dg04XBq5DDOEvXhsdG1-f71Cy8mKGQncY-kZYAL-1zad6U3xNAXvM7ZpYyuF6m6EomqhUa52Vyfo2GZexS3qpnV14AuVXcU497xSrG-OIsg0e63PPVOEmi6LmT6t7Fn-g_VUjIoalqEmaTnLWTUKc3vWxZP0L8tY6y-vB1dx8vGHrXkTggw2e2kwmd6WTBgYg4i9KOpiDog9tUbvAw5rk-E8A6NRlSdtMrEzjf7rtI6YNH6Yc5Jk_P6CVva5A8h86eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0VWNCAcIqccfoKZNJLwOwL1zRGr8ylcdWt3icQDTlbCT1wSKOe9ZE3_KgPWVKICnnPKzLh7R3BYmVTO_elY7mt12-wMUpkZlBPtD66SaMCZ4kenddRfcjL9HE5FW_r407O6OHK3-WX_k40mFvTFjacU0-Jou36e80eEEgq4iob-8A-2w9PexP93sW0QGIweKPJax_04vrAIZFJBwIuGxhXmvHI3qlHamNcCItf0Cp4wkUPihXzuzs_-fitjeMkUuVycMcgSWToIk92JOif-MDlHxULfpw18kgYjB1viheD_K0M6RNbNduXvcYbx4UsEHsSoKnqMjwO9Gxh_OM1rxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0C7VhPTInK_yuKhLVXdS5AYOzIPTU9jDm0d_aJOwzik8guCUMpFKTyAwLW7vrFIPddFHXelutEV-n0Ji2kWe9-cp1kM6IxZm5KxSgExZGYy9che3kxedt_C3lPgtTEUE0rJdaNTQbHq48congj6NyA3TP9SRbNAf9aNGoHK0YOfPJvW85p5Pv2OeDGKOa4U3s-KVdwjah8HcwJFAaLDh_6ItxXixmUd0quIzyIRrU3kUVl5LkslOMWz233Zr_hyaHeupsh3nUKRKle6Xp9SZP8wj758P8iA_hyUQKX76mzHOxlNatNUuNr_X9OT_FJrx-g7JdTi6brNOWSnwd-eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPz5DTh6QC9_9Ocq99xKYbOmn-4ZoI81x_66Vt6RKbvj7mRLd30ABdQr6I0uAurpH5sDj3P-rlrhxdB5BS0gwYYWssiVw_7o9Q7EiBJhcjkCtPwr1WidtcseoLG2P8nYyJHWp7Eatvel3EgSraPEbotYoCJ4Q3TN-mx-t6IqIBeBeFilyc8gN45Z1DI9DIj2NIYqSq_B12HUE9LaYFdKWmn-NM3Hb5LDwBudjKXxLWopNW7jpKjLXoqJuVUDR1q7v8XSiLMfBFL7eXeyzUMCQScNTvaa4O7odvJAUYvjIYGo-L9ibLcyd6G6SIQKoMpNrUlomQnfhlJOyotv77lSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbKjAWZsgE38P_86N8Nq2KU-J9CQCqAT0NVKnt02vveXt5Q88Lrm29w9TSiSBEWx5hrDHlAFkDv8zr-p_CjAM6PNY9YUm6N8mHHAVm1mCTy3BvKML9Qgw2J0F7LBtOTgOFp9OY9lS2YjSWAly9iq9JftD7Jz9M0d_6dc9nKH7IGzWvv2ykeRyqE-SGv4OPaCFGP2u-_Xu_tGlKc7JVfsvEd67PKPd82n2ZZFhJy5a6Sy7aW0gvrehXwuahSNOKVBNKYOZFyctz9nm05DuqY3VCx2mohoeAIiOKw9ElM2G1llHv4NtyMn5BEbvToCRS0Sjz3nDjJFg5xXflXCKKgEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5ConuLt3-6qnU62UtgjX6X9KthJu6SmYiKxIjzCkhbF_vYKVTY6wZQ8D62eoZu34qoq82tIpqcd4tlJLiWvhA_UMpcb0ITKxLFujnpbRTpvaD7Zi7vBXQIwQB79NAUe9qlW1_gh-r6V8aFD-CjPvgOeOd62K8wS-rL5EfVOi4VmuMiWKgHNbRvnJbRn_YNK0uYqgJ4qB3fwgrE6FlpKBzpDY5zJt1STSAOCUVh8u25uoXT-wvKhRVygLHMDTT_tLA56Uw5E99gsgP9XXSFVaGtKUJXqE-tf8x9iqbY3bKbbU29G2n34r7ximXAU8LS4bLCK0tNZ9LlbOT_OWfsaGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSdv4d-4wVEL-1MwFmRUOUw6sMh3H7tRFMdNUVi9qt7kuQShCL2TXT3P2gxqy08pPxKvkeZKaEGu542mVk8hgJpLJqxk-VpfoPWsx5rT_sjrvCQt9Ggs4QmFFe8i-bWvh1P0_rsoAAYwTkpOMzACJQfjySzx4IpOh58-TVvYGEZi4CcH46viF2Lz8MiTmyr1gdSMQ-jbGDBiBMIDWhNUxb2jvbHEEOrza0DW_hAMk6qzU86nllq95zg9PFj-uxhUL5PbP5PsjfgeofZeyARLSveeIDFnyfa-SeI1hgyNPuRgdxQFohGLFzzTk8TdplzCX-up_nx-J-BbGy5CAska6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=HzXriMn-Dd4-vdBzSPMrDlXMSm_AdUinH5Jokiv1XbS4kmoEa9AJd3KSKE_vmbvQ3-Myk94Mqlgiwfipg71rXAFydvBgqTn40MNRIF3_5VOxD53kG8MKvNigwA63-mReLiFt_3HGp0eoR9JyC_iJ5Kh3rzIL-u8wS4KvSRk9vtmC5vq2d-jSTD98XaVsK-E52b4QZgKhPDXMhZCLoQCgIvbfQnYBZeIPHP8-7zJ9yT-hX4OiQvuSTyAtpEpXgiQNZqKj-9WW6yf5C_MkuBt49i0ap9qIWfuDwNGmf6b81RTgPQWHj8YUn-JG26GRlKL9m2JNNj1ncsny8B-vsMT-Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=HzXriMn-Dd4-vdBzSPMrDlXMSm_AdUinH5Jokiv1XbS4kmoEa9AJd3KSKE_vmbvQ3-Myk94Mqlgiwfipg71rXAFydvBgqTn40MNRIF3_5VOxD53kG8MKvNigwA63-mReLiFt_3HGp0eoR9JyC_iJ5Kh3rzIL-u8wS4KvSRk9vtmC5vq2d-jSTD98XaVsK-E52b4QZgKhPDXMhZCLoQCgIvbfQnYBZeIPHP8-7zJ9yT-hX4OiQvuSTyAtpEpXgiQNZqKj-9WW6yf5C_MkuBt49i0ap9qIWfuDwNGmf6b81RTgPQWHj8YUn-JG26GRlKL9m2JNNj1ncsny8B-vsMT-Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGPNbxPcjouD0zgLCHDuAYSsOgf4BNdQFuXum73foGctmvd0U7mCrVHAtR8agqIiEgUj7jOlpYikBeibXoLZztJAti6gGOFD34cAVl-KblpS2WvtuOtYi2xk-eCMr1M5LxzGs4TJrbT2qa-bb6Dmf4WVLB5Wh_vHfp2FhkBHAofaYB_rbnSr67m9Bj_rhwkJTqR4v8xfLAAIVZiw6nyhcrhp4DqnJkL1qpmGAmPYNiqYaFGZQZfDTkRgnB-OyUDgxscthiujti-I0k3fdNJ5OB73QPRHSwrOHunEZ5ayny-yuqnMCGs1-qPzonPyzh2V09MClsdcWlYRA08X2EYY6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGxYitDmPrsOFXhClw_ZZbeRwBFFZLe0vVLWG1RXBnJypyN3GwnQkhFr-AAQTWAKoR_lNEusMbjLsXyIk_LOXkWlOqXjYnCl6kH2ovaoEgBzUWEwqEtAT8oPss5tASfJ-QMZeWB7tIWfWt120moCEpMnn81ijXf73me-6Ujl2NakTMdCFFSNNf9tF4z_lYE3rgun4uKBjT7rOSR2LYVc9O0iW-64qJA4AD6gbIBAr32L9nLZrrvelQnhE_ZJYjuNHHzVIn-Z6fHNRqAogEiSBOsvnrVQN6HCP48IccTqR40yIE5dLPApESJZDJZQ586J8Vs5GrYWbI5ld2C_TG2Jxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJkwNh0QApT6RkhVl0Wkktt6mwRwvshq74Tv4XfVInN4g9ZobDatFvOZvjHR_VXU8wdlZbmIEUBgSxsJ8TZESxefZdjUd6WyRZmVnAaJMkG_OpHr2mOrkwafJMAcs90furhb5qemndWezLtxUj6kIUZNVxpMWn9Zoj7LcqT9hociPa3mW1u9uyQzvElqk8Bf3yEwsiGlXOho5m5bc4V2bXKOavAjvcIFfsEMARyDY4Ph-j6UhGF1I2OujBISpeXGEDxt4MXpqT-8kEsnOVD8uPNnhCwlzd9NjIM272mR4KKFEhvr-ZOb3g_wLgbtwKpLiJEy48pxzZhFdSxTnOksiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G22KJRlEAwKxb6ShXE6ZSKsvUh_4sITAlnceTpyA_R_e3AHwA3lT4Js0zbRRV87So5C7JqNoI8zkHqRRFBYfSAWDH7ygYlHiidRylXnlpjtTxoqQ4WEVifoec4Erhq0oYwv6L79DMQMORAwKOOlZjoYkvJl-PGdg-_5nTx1UTPOjCGqkDwmVIehvcJ0H6BO14wjFewtNf9LgrbpjP6XJCytcy9WJTUcNues2eUKpbx1Jcp0anFmfQbTLMTBQ6eQPqse4eNyeWAXPj3a9EoVxnJlgThrRxNvucbQOJvGuJ-8qistH1qO12-qCBOdt1GK3wGuBNfVL8jCQ8P--_f95LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReyoEY8UjT9Gtgh_EdDQTXu_e1M0scPrK5MeALoRA-dYYzbWmZbR61-uNMEkJ6-K3lnlayJyr0NGjuABIPxpIuBdxlHPWokmDJJMQl37mKKwf-ZBMvfiNTJUAesQdJePTXpXa6YnOg5AT4Dmd2ZGB5CKjxZ8vFh_sd8NqdPG6Q9NIcbzlEK9e51E8kmlVUkjZXESjYnGl7qNhe9H4i-EfZHKsqkHyFaeMSMAz7UxlZg7gqpxJIJ34EuKtgoZOzuCOtNX1QwHRohFQw2dgcyqnwnTlN3p1XciI5GNn_L7hHqvdYAg1DIruJD55mEp7HXblSqDwUYk7lWaMPM6BCwfpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7bFgno9OhrQHzsH8PIyoJigg7uI9N2CL8kD7SvgbExu1uI7WY2nY9O3OT7LPvB8VNCAVhhDXpCwDtULLo1Mu8f0q2pFPn8924PYFsnAwBtOyKFokL6OxWNaXS3-pUgU9otl0l12YHX0ly7HFBXQVlGLGsvoQdjiu5G36cRXr6weWver902A7JPMc10EaM1NSXplwTR_xcyz9pBKQ4lCT5WsGceiR1mA6VIPEsjVeubYQVqv-CWKAuDQdy2YVVJApxbWkvCq2XaJ_lv_RMNGfhsCUEAEY4VnoNkyMDESL0Nmlf4_x6iSzLSv46c78FoUYKq8IHGB3wM0b5mReTytGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3nhVtJGFSyY64M7bzwsHIqFM5EN2WuTQq9ITXj_BkAgL4uWvCdCnO-rpIGqVkM5mn3x0hRersxdY10h2CslBixeK-Tff1ZaN30cFXzXduYuB2dlYNTZNMVmCcMNC5Gbq9Yzpg3PiHL0Sp0C5MBMRipI27bxXCnreSIuOWCCDeZJiGOZL9onBjQ496_YkHjq1IHv3OxyYnDoMN6fF2WhVy0YXJKCDr7wrgwSW76qebLKMvkQg88tShryRY_z5HzPfOXfxA7qT408HO5Bd95-wRvsn4v_lDnjted3IezEUInbNmHjv-DOEHfe0YmBjoSzXvyo6WDnHRG_aF_UYUGNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9hqA8eZ8MwHKCxiOBD3I0YXKIo5VkNzjukxW1OS2-93cifG6s3wRXeaZP4f4nl4olBG_Ur6mt2tMX0xWcOa-rDZKS8GQGSPHceD9irBUakkQZ8cJ-hM9GNPMoFRnrggk4XHnv0f-QWKjhSAID2wkFcMDmNgssSSXBANDyNTdF2xsUDbhsNRlJk8AHfkL-16UvWxCsdjJUio_ARuws1LOlzjvO6oFRP7H25qGd8WUoS5iECKXNOD9S3-GDBYHkC8KClUmEHAwtOc6VQiipo2uXg2qsYNp3DDG9E_42kxu4li0ln5g8QkNebGlo5LRp9LcAft_v6Fauu2QoaWhxGQyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUjGH-GjrMhphSnLiJvlNW0My50osLoJF84_7TF1IUcLihWbYMCEMxt30_x2vr-DMDxCBKpiTMZp23RO4srPOFmaBeiohZSs0L4DxcEbhwsRzSbQqqcyhJjUSYYnbhA7qJoEpElgquL-XiHcdUfvmNR40-TKo11bsA_ntYe-g6Bdgj6cLVXL9Gaq0gzTjbK9WnkZoS5_gmVS7TXhMoJg_6kOjcUMdcWxt1yhxcTSh-Ljx8WT4wqKeXmmyrRYU0EQ1aCEfLYMp9zrSFDhKsOixZk3PL2Zp1p0b1DSwxiZWTBD6RlXANXiRjxDRuks2atlvUs7P4vOrncSAUa-jZlfZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvMnX_g5S0FUoxuU5-QF982ZdHfBMKS8QqoYGldv_UJ60vV9ZatzNDbN0Z3rDM7jfSDDUHZDKWcX0P2v5hdzoqL38Y-3hgdKlciS4HEpOum_JFZvf536-oQ3vwBNcqrvlOYdXOKaZiEOVQFnhY7Pyo1EhYbp4x5tvlURwwSfgtVX7Hdk6lpct49m2ctI33dPTNd4dyclFDCGpfLsz4xGfCGSHBGMur4tfhLxAC5k61KmoS6TiFlOeYfWB1dk4Vb1UvsWabxI1nxNaHDLHMvrgpAEr1TMPqe1mlOps1QvNw708zfAB49gqzTBILchzCkU1V7KPlDa1WzNE3VQijPurw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R28pCqzR0hM6iMggBlB_2Hy0PYIdsoVMb1sB7iUgvP8gkcsQxHBE1UnEGXyO4YIV87cTSTG-Pd9uFbHaoqwqhJa9mMxoUFVK42u8SCyFb8SjjsyaKDu3eD_WL_rujFjH1WrxOPgLFlGWjRoBOO8BecqY_CMPTyRHOOnV71VlFMVyQ0Q8izxlPu1X8zLst8ZO55HnDkX1xZwPTUO-IcVR8MXrAdB9jCNs0NozlLZmDn-8GJvPED5fqXqZo9UXaLRCABpfI8n-ySM9XLEyPVPJePPvpZY97lpPL-mjUi1f1gNWR5WNaZq4OAsQXY7r6UH7u69MaBD_lVBMD-Y9DOBylA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrFFDbEuMLys_EhiffcR6QW7ulqDbvyz5gdSTIyhJdNrYx2rmyYJeXNmHJBdv7Sk3g88aDpzTDE9_Son8UEqslUE80Ww9jud2cdwuINBSqtKuzOWo_FzkdPTYYjA6PKLJy3kP3y3ADIVwvc1zUNPxRZ82xq2_o3YSBn_N54eAPIqEs3hF9CrapOgJg0IYfjPmL1ye4X2ZZVs4w2VjFf0Oi8p3UhHYjeYT7Ef8DYYr94xhApjVjF0JkJrUksqEFMkAxTjrqf8QMRKpyLim-uDUW9PWMqYT57rXdrAI495U6OjMDWX0rXK1R_q_T1i2Ai8FmzoUM5NAfQEJPAg14hs6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0bZRodat8_HD40Pkn3hksCNC39_uZfNNioR_aKo36TwwvbCBowao4YoLYoBvSFfPnyS8VnsZEIxP0EhAVy-P7Xb2yopdq9_GGlh2aJZ34zwxFfJHCTvVV_aCx4k1o88z0KpCAWQbhUmsdtBJLchv_K8kNsbEQXXY753UZWoV424840wTsy75LVUxPwcA9fjg7jOwt98YQvlcJhp7lX2lkFs4S0b8w9hd_L1Ha6JPqvvR4hlbaNVO0B9v-u48_-sH-TXiIu2Cd7Bx7dRcdLPGPWp5beMqPTjip2Z5IVgNbu2T8ZzyNrxhEPqnPAE_XjZsM4fk7xDL5Pv28e-ApOxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSQDTkkkaNaiha5v3uCZw7WVHfb8PXGAvPDwBzScb1RaNKyhoVTCg8FYAMeFjp1UbNn69r3IgemXnuHJQlZWmaOONqjAyyv9dWfv4R75FPsjmTz_eB1GEeIXq5OQhFjOBIbMtzFWRC2gNMFD2co5JVQsw_tmX5YHvQXiu9Zyq6xFggUv352pcgaSyrsHK9MMnzfKlkQ3YYAdNmlP8RaoRJAgcsgZ1RPjnRpXTfwTK5tgkEMRiFws8YqPRfba1gm0hcYcAyqZjw8k5B7YB63tHsUeaEeM1JsXoYPbXWECBlcj-E1sBdQ33caxSt6DxlBsKKgQZ1i_ozpEz2-XKzMhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwzAL1C3KwbiF7rjuaUG6Kaj9WZJx2hEwEl6ah1tB8D5WSNBIfKORRB-XQKdRj-eTXjV9teK48becVmCpE0C4yr16L8VRX8BgmZO9b3Y8CmxXZbMDNMQzAWrZHd3Rk8eRdPu-QWLpAtEJjWJmdppxvKiMTiL1a9CEgKyokwCI_5oJBBiDKDFCXf4rHPXmIZoI_H_JXQex3sJBmrt9DXae4B3ldTjs-qJLwuh7E_EF9XQ3ODM7jHYyzg81FzPGdbfuUEp64msABsZ0Oka4frcaJ-bKAZR7m4nlrJfz2svMxRSaW2e-jmQM-sEJEwyx86ZZ8GfCHLkBLkgfI8IhN4lvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1hRtJuKt2TI5c8hRYgktrwLGOu7ENWk-cDx5pR9JdARtgXjG7zFDX5rZSiUEdpGM_mTvvmu8BnY5opm7HfVNpidS31tfkNmyCleQOAvq6ljL64SR2RfV3wE95KbO5zKDCrLlaozEAJRtPcXTFyPhUjNl43CX6nGBc8olH5VjF1FTdO3SCDv5GriURjPeJgU7RTIf4oIZZgpoQM7ofVP0u3jnoGJqUSwZTcryO7bMmoUETpS8vIz1pQpPYT8QHKVRqPFmHoOtgb563CGnphZ0lBwvDfGrQMKSvK1Q9d5AJnHDlhb8EMR-S80gsCvvp4Bgor8wUPU1OQbzFVA-yiV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCp6WWE9pgd-W3JJroFC_7W3q5uDdLquU2M8YggnDjxXJkijQcmCF0Z6yg_aNfOxpSIMlsIqWE0ITRCIJVPmDjIu5EvtjgshDrfNWaRIWY7667_DP4D4A1mq0GtoZQNU1Es1MPNyDB7pNvnQb5sQ1JlKLHKETF1JE5Beb1gh9C9scdrS4L0pRBbbe_nR8Ot0ON3s2e1c3YuvgYv_wVA5aqeZntTUPhKaWdvxab8syVS2ZhnflOUimd3g5YAvHX2w4wwtoBYfUAKiETR4kknBIYO99VmvbgnMlmdb7VIx8HFInzRhm6CkYiOkQqMcRdeIMAPBguZuNwmaGYEkaF4VtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7tRtTBL9Cq1OHchL3IpM4_YAOV0iHdNaOC8_JRHG7keUetUmnbVNnPAoqV6A1FuSP63NavRbwCqTrBM839m38J4EyybVkoKf6jvCSnpVV5oyiv3QETcFEI0XJGsfvzMd3hjeESDAOeRSKmzWPzBoh5Gun6LMbCZHneINmYYa343RaKbZ2AdPZXknes9miljF8XtIuO1F20F59tOO2ImK-ULGR7uFtH3Xl-24WO6vy0Y_bnddXa5F9viD1WaafTH3IV6a-jW_e8xExLKbXLvpD9jKibTvLDpzRh2shZX1HAz7Pp00iki8TM1_1vGN0R86kuh5Q-cL1AXNaFpADy53g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyN3vXMyP753tb4EwOvF4AF5yCWagk1-WNgbokieeiOxjGx8CNQUq9hiEgndIIBrrsmoZG_QG6cyWCzElGqGYZLebTLLyfs5dhyIsWFFVdTIpqpNggu5nXVpdlNv-99jspfMcKpKloqsCvobKJe_b9mKSKXee_mnjbpOBUIlFcdG9QDwZVX6bPP7heQyxcy9f1PEh9QE-c7fmm2OKu1AbEoNAICa52mkl-1b1KotSm8uuqM639f_KPxgbHOo49_bJGOqL0ARbU6tk4pc5wYGDWZT8AnXPNA4gFq6WC0Gi7cvK6Pg2xHy6AAdWDpFuBD1dzIVJO0h5U-I1ShcP_ANoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfzJYuCC9t-hiiHVyBdvM0xWaRWO8BCmdAnu_50eCKXiyae27jGGEvgyhQ1vP_JHA0GGpCbBpv64KP2RowqHFrtJPywypmhn5hrJkAVfOaBD9YX4oNdQGr7BxgnOLdz6nn3mABxNQg4TfHnDl9Jn0IATJkK_fKzyeZS3dp_-r2KfbYGCKuNYpoyzTJqqR52yNFANJz49DivOldiJtaryl47jZ5w7UeE4O88IuMZL0wLseUxWL7aeVKhzPALmfxTs7U2NAO5QQRBW6fifeEBWG-HEBrYN3-VVmnES84nb7X40iwVRJw8VDJxZz5xNO8_U5xnI-vjHsb-CIdl0QeSj7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FetCV1NRwKODjBbYIYId1G4RYq4SzsXv86opknOoRW3TwIlmqnjMoap4uAdTvL4RsG6gZVSMXPNKgL1X6BXdGQlq9_AOJx8s9FHb1j0IRHQz7NM3xJbyelR45eHvW--IQmOQ0seDNpUkBlSnASEJkDDxfaSSPG2aVHvBjr_K_jKgS7nnaUJ7FVJ7JJj1MzL_f9bASGhQdj2sS4cJEPRjv9-z4Xk7ljuoPv-YPFHAxc-gSwBQ-4uDGadoOBLPA4kqs_YBrbeApiCAF3dwLVLPemHe6s0tItY6hSX-CXGlzqFdSLaSpMPVlcYXi-DYdDK3ldfqQwc49j64TIX62mHuFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjxbrDOarn6GxlTJdndIRc566i162OVc5d6QfIzdrN3KbauZvsApE7H9RMc2iuBiBSlIEFpKtjoLShnHKGkSTHH7yAxn3xFVxB9zXESiz0EwulvuEQMwijcqntNF_nn9LhG3nfLPwuB_UCdidyMDACh_l5aLhWoHGft3oPXpv1UA5U2GddZ99atpe_eE_9UB3tIGoh4Mcl7_ZweJoroyZLUz_cjoTKateQcGm9PuTIn0aaAAj75N0vO1UimqLbKl8TrM0gdulXgtfrdC_NDYA5XXZfQw6Nn1Ur-RUnjxFGpJvM85lMYF7tBydfQK6EM1HWne2IgFOMidl580DSsTjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7yyitJI0_ymjblhPXSdm2yEt-dRbHpGaqMX_oprLLhU-a9m-lXT2wf26KyxjtDS4oFxk1Cdh341PjAqRh5a3tYMPRUyks96bz6ryQs4fuHJ-FkVRbyFuPV0gJRN5rEQqbNt91AMrrt-pRh-mPpjeZxbVvFS0LEFvjYge2AwTNY6yXTcNLRW03SSpwRJlFH76jF-Ap6u87xN_9RB8IFL7EH1B5IlbCn6WnRHIXU7OKI470PKd_rqTyRp70xDc6VGWPN4of5jytGpPBMtohNE6nclLbG_oca1HGj6Xf0YuZxqW1zgNeg0ocHzP2pvWihD6MUbB_oeOvl-8WdJN2QIew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXZux9NY1lG8buKwGwge8BHIDAkQV5rZnNARKspH8M96Ni1tcYPuZ-jkDZMM8oSnexVfX-hwlQwlqRbra-DS8RL_hknFXQecRrYPVUcXq-8drRK7fGNcCeVJ8Akxt6CCOmWN6bHueMIb601NgXIBK6VwWNZfX-T-KS4s9kBmWy-JaTZpNXxjwWMAwO9mrC39Tn5DvL6d2K0ltcaWMw2yfHxMzvX9BK7rTHsD3pU_Vf5d1VVwYR6CNvJl6UU1QZLjJoih2qdU_RLeZW5FPrXWWQgyJdOFYC72FTpuTid8n3xg-qWt0NHuEgTweIRHUTzIoz2PbG6yQ8FJCBe_00JyIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGLBcBJEF6C-nWMOPrT0RGaVysNq-TghxBvq5Zx-keRrZvzXQzo8Yecxrxw9BMuOmq5ZA8m5vEjXejXzqxTL1TT_4111ScgHMCiyHuW3RR1ThPx_8a-oEBruNVyvb5DdTpbxKSjZ10H7cGxRGOsbsRqo6BA9E-YFJBjbDEBF0qo84yHBE2noY_rZzEiw-S5DJu0bFDRWbN2cNrq_H50fHlTBMTto6Q7SzoyNPd_61Q5F9AM1dTu9y6d2SNu2g-uIzKGdN_TXbksW0i2HC6gxQiKAsXci1t34H6rSlCPo8DUE1-jZMBgk3jN76uCx_25A0YtmSgrEUFf7Yz7dGSS8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShlArqA4AaPSinWTTgjjKdcEmFf-NPJ510JSDz51FlywjIfnHN8gX7cvrjVCwq91ipNx5PjrVChtianQ_Xasg4C2eckI57LmsigXr237qaSEc2YePCdfGuok5HpWsAOfmb6l7v61jqT87ZuVjfoNejd86BJe25GXlZ3CYCdnWd_s_oDtsBcPvK5zVG8Ai4r4wkIgdZ0C4muZL0v5E3rojYCUk7UqoJgFRqZ36ZWsVSZ0BpJ3j2R1_sQApvIMr6FcYCQzMSBKaXn4Fhgh0FOgm6CvkQsVypmhgV5gQ2ASe3uhRNlAmsiNz2RVXCH_he5FPMNhuAkiKbEd8aCWulRHYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE5X5PtIWIhnV_DAu4rxeEhsJwrXkbv8XoAzHzFA2zMVQd4BMO0ZqkVUPVgvBk6HxrDm_R6ryicub_tOzlt9Z8Y8bnfbuhSvR5tOS8MAJZm34tR25-Qd3VsvYfcslYDSEIxLir-nWoBP-xxi7BwBamoCHRc7MxbAyzqlJgsyXzQf5yvTc9RVWqaZ7J0YEKoWgP41fRyoLf110HRiEZ2HEJGGfxMy_cLmnR1uQgJQCAGAVFQ8gbYnIN_VPF-MG4EQgnmNxVHGX0wDuYBWkM5XKGInlyO_y8oJgXrPuREbchdAlQpDTD28YvJR2O85-WYLviwij3o2AdWZT0yIS-Yg3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_QgJmPWFMhLhlKJoBV2ih08JIaEYih2fiz41N4K3fyJYgY2bdSUFuJQhV2LheoNE2qk5yr7bvZfBBHz5PSvy21I4Xf6_5proNRQBnSAW7xIdcNUX7VW_804PI1yW420hc2kkVr1IQ3UKe-K2Er8BC58D92LVbKkr5CYj_O2cqlbeSKn1Jl--7kB8NLcljw0CMFUtphatPNH1GPlcIqeDAgowsBpDVJ_QqrX-6CFB7XoqDxYsB0ZUuvkkBCfwuwQ3U6cXMJpvv8IwnqgEnvS13Ui1Tx3tqQzLdQkxYACEhLwBROg9it4M5qslWeDDI_8nVrtROSUHOYqOHeur41RaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsMbx45g76CZ5wW2B0t2zJil1gmHYzzF_fhpt7_EUtR5A7EBp6tkH5Dlrzppn6SFpM4PvAUe7dupmpuKei0hKADsrhKlA4kV0FzkhbqUpCK0FaGD4oQX1KuRM4u3qK41_0w78aRpjK1WKNil-Q2takDMmC-djypBeFgu_CNmiVjTmIhxvDIWemhB8K2nzEprv0EDo-B6gzFttuNT1sMVDm9xegR12h2ZjLuLhFTQIWzYyKmUDP3d2fbylxeryaHWrl_3hxbHR62Y5l3ULP-TpmAbDa3uwf5GjrBypx3etBTr5n51LhbNLt_0l3zl-a5AfvrjqYNgEPhrU43a5Ai0-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1mAriLSQh3xGUSGU_VY0HzwQB1d8FwDH1ixYJ7XgSuwsdJUaxcU-vDp22Wv2VyDNH-P0LMh_evkMJRd0n5PdqJIsk_VcXmQgoUFkNNge7SW3SISbAfRub0t_r6q6Eg6VTuaqmCHub7AhL1NMJ5vkHlVtSuBlmlh7lKr9iJyRwHhw_dMBUDTb-npfUtZA_-F7I1qCcXh3AbnXKfGlMYdwJQ_9evGHhfbdBNZ5ytt4O_I49XDrfZhF3Q-InVBsA7lUqzOkdhufOkbWvrreUG2PT-8f34fQOQY3Itt_f9GF8lLQDcer-ihkwC4JPm-AnhAJ-4TeFtFwUJ39B5Tvl_ESA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9QUYpylD16QQmWAZMni9jJC4zEPS-so6ePZnLmZ-gfYA0mKGXn-n3EuCf-LTkFPCwwswKTpyJRW5Bg6e_hnfylowniNws9DXV6v9zJhhhmu0xTRITZh-HMZYJBN4KqHityDxyI0eUO_NDt0tRLJ_RJvChVPy148YaKoqF2Cuxp8oibVSQDHsGcDh4kzOPJc8ach_izCIkBsAv9oKlsMOjl4pydqsOGteBGzmnvIq9Y3cvV8fU7iOxZWSig7cPp08osT3sTiA61aATpeOk7YckArm0_tQv1GNmDghQRbyiDrdT-5waQE5T2TdmZw3C2-562u7BokmpkuupZEXgvvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axz97pndIhiaVB8thUWKWBiUJqVbKtwbYIs3bX7hfYcB4AAa9EIJxrdUOHt8G05zywR4ON2y8Ee6up69a85SO2O2DiT8nStIXSEtV3oJpSTYtW4Xp_Ie3rPwVOmQM29wr4IrRCov80_N5wQ278SWmqYzTYnZ3AvvQWNmi-zZ3cNThBkrQGazPnuQLLcPKS33f4iTmcF4B_MrOyCJVWOAPpmBnFkut2ateR6gypU2jTK8UmWwJ_X3ehnmF7fOAQbuUIMaQvdlxVIZIUEX1QUwlFc_tiykgHR-0TOe8gYJQV4TXmY3HVYAVuMGm9cBxSgyctPgAmMZrp_L_DK_sRT04Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ilvmu6CXD0Sht_Yq94PdaNWLuf6E2ORyM7Q639M_ZKRs6WQ1c3Bj6b97QucXpo1QP7lOyhG8fAQgZJSYdjWR35qVz8dS7WQ438sKnsLa-oONILzo5MpgO48SBo0P8y-yhrGeFf8Sd_an5TThGmaJ2zse02tpP_PHklj_4s0wf0y3UxA6xechB0_ZpIbwLQKOhBI515PbqK839RXLG6QaWYBsQvh4xNa4x_CG9BNOrN-rF4x8qweLnXVjJqLRV829J7ZhNEVn5YCKbY12nhAyNfJiw3jSEGjtFroP1XH-37_vg4KjcjBFluAkHimNyJ9CV4ydHPv1JDPCEve1QgmZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj9BB_9PfaEC46548LzuSni97bheV9BO1uHnLT0m0gQkQrFvMz9wYniYECfsz7s91ZqNN_rjpNEsnnt_dv0GmQEbByU8fPS9pG74Gb7foKIXgCyc1sgRdQO-hjpnr-J7DJjbPUVZJ2JamKnHsqRHLBNYth1cB77ZHy46dmEAMsbiD14XqGN5WrAwXCK_TnLm_LT9TLAqt0xdmJIq7IRjVcp1gm3-n7I0OKAsuolY_KoJDnkrXPfw4BFUBmIcgE9vQL_kMFqw1VW8-T1PFw9_ORtcyatkqilKllCNTwKSCw-Md4GdiWi5kiUtzZIzTqdTKzjm7udQ8fdsRRADzDdqZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXhUdo1kg3nsnA3DXPeSPNtSYbFKITEqBsMuPkz38kPoTBMUbrV1EsEp5rP7OPHsNzPpJvUOLXu5b3VfDlLMHgDdThbWPftybJZKG0sHQ-wGlnJUFe2MOUkO-uOUaIa2Apr0UDPSwGRLTV8xl7F0lNBI2ENWgSpjno4_DEesefgC5mXh3NyJCtXGd3n83AKjUkXEZ45lknBMDRUhSAOn4PO-XYh-Lt6flhF1NEenVp92gcKm3Nby6WLVXj3EjPFfjD8USnE_B-AZdMMC_BPwCg80KFQA_AapxQdxWW8yqSURTBUnj21yrXZaQF11rNHYWPJBhY9j75gqS6lKokTnTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZdTo-rnTg9tb0AJe_ZeAc8CKRgt1o5l-ctCxSqfJ5wu-W93eAu2Ny0TwciuVHhDPz3OUCYd665nk_Wj9rL0tL2TNizG5pnAMjb_2L9KivNUrz8f-B_CyTVirjLyF358B_xJMBczKwz12J4LTYvHYCbxa-gRhn9fhb7PJhXZgJq4vnrolGZ7SJVmbhRWzTmSrM1qokDTsOyppLS2fAE-hPhwW00wX9KX9QYRQnx5g86grxWp0SB6Tq3RnmveUbozUP_0U_vA2Uh2HeFkw-PdB3xTDN-A9Lw4rfeDXFvC1DBqOKesnHoUW0sSpcDBGalb9F_3dx0_Doh8M5wfaJQ23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyfD9v_JySowAT_Pb5FX0dMS8sd56DpPoZgqHoFlX9vVunDXDPq0li-BlbzNjB8oNGRuGPZBO4FjNcuq2XBmU9TWjIKMpRMhgpE3L1PYPfeCC18VsztTz8una9dD-hoUeWN-BvdqZ7LTz0OqPFV1Dn1qlgc3bSDvoHP2ss5DeMMhuY7Cgo35sXv_0ViAARCSYZvs4_sFh-NCdxfHmSiY0O7iWImBGWq82VRuetTVTmpg-FkLH43Bbd0a448rE9UBUmZQmeYgeFayKPAXu5Bju_Rw_V1T_PFPAoxHiyDBq80Hserfq6U4ADY7dtwCZ4_zDCG0Vy-Mb6MAmDHAeaxy7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrSQeblSEum8RgH5aEBGYtTpB6yiYiZIuMXbnbzJ5NAP6uhRzX7P00uqW6-kQueqCgg1SimEubJBq2pykbTYkNdiZSkfwrjM6g7ggT6Fw2zZCvbcN9gJa2qKpDMj-w0XE-OvIXVEuDoY8It6phNySkmf_KPN8rxzDce9Lf3tXO0p9vy2ECkFRP9BEmkIDhuJwdmXxtVSifgTJloTNXrkuIzsTh7KY5pEQAJtT4jTQRuUAyR-R_5cxLpKHvffX1n3iIVPDdmXcL1T2mB6RuogIDrpg29VQGu9vs_x81hTpHYusustAYRzSNmyj1OP-_Tr1RZJnpxgHAh_VqBnSbJo1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcsGY24U4t5Lr5t2bcCJKI_urZykWUl-_dBKcsy2Ry7JIQ20RxUiEcdUIYvMPs9VLHSrKaXK1QgQeSumN0UO48DR04Wc7yVvfjzMy0pVjMhL2XcANHuP5U9kvGsIqnd9MZcuQ_xvXKR_AgIFgA29c9PxI68OWz_rpbwGOAhEgnWL1i7DkmkQ3Zz7oyikbDhxqJJ4FGho-cjEctdql_2_ha0FEdmQgavqT5m9Ut5InWOgPI6Kkj1sPIBZCJtSZTx8Qzlsw0VO621e_DpDH-_3RqG6BG725K-AK_j7Qrdfw3z7KcRNiFmwoi7zzcFSMe2X2EzYLgYo7WU0zJApXG87Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejE69OC6tEtfe_iXdBf2HU5-cdaPhRGOccFe8OWaFsLURO5PJHjTla6tcMrCYsyt-gJJP4OE2errKMxBv68jwkX3bcczLjU3astPGJPwu1eNQV3h41PoyXnnTNo5oSIeXVv0LsKXE8z-aSZq0amedN2yTudskLfsZkM-9v8vlqQS36ali8SjV5swRrSwPGo2tw-qbuTYRHvHPR6JiEbLtsyht3wTrQNw2sM8OL_OhjzfYG0UFVoPNNgaPTXSGsoDeEH7tHByKxcZAO9KRRGPEWWoWaoJoRvwJcU82uJqSeSWaThCVPpBtxA-YsSV0SG1jaI1AODzPjs0zIzZeamRmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CY8jMSSfVOjnvM7G_z8pVUvyKAueTnofkIXZ4ggtKf9EtzK_tsy4hN_9_zj39MXLjwGio-x5VxoO3D56AAxcN1zclN84fjQCwLYXiE6GJidI9rxOqKn3tBilNNqNComLoL_kUnSfXlOjGXm5WT9DLXuUDg6PChFBsPK8z5YN5QnbGCibnpq43fWNOBkv1piqmNrAp21Lm8avX2WYGHE_jq0T0-EtQ40wCs7-VqoFUYarHrd7vNYy9usmlItQ0MOqHgySH8d46otHivsb39If3ri7wHo3KpcyhvZxzXpt-6Ix3US9bGWmmTu3oIzuOaa1FnmeI2PgI4Ym-uk6gLGi6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9jcAfH9gokPK-aMB_j8Pf_oM7uLN_H7S-6OIMlV36PtruQ-ZOA60Rgq0RdM6q8gN17ELPhWTKqAWcZTiqGfvBVQ5t5w6CvzB6z-Qr2YvnR81Mtusi6cpmUii2I606z0Zg9IzL6CEROIifMSKviRr6oeORTbLx3qrnDeS_09Tz6L3LRMRmb9aCiXGnMqImNqPBfw7DfCEL1Y50FG5-OtUCsCDdGQN-doMrGbc60VRgmv4i2CgEV94lCydAc9itlNASHTtB3kUYbZ6-SGV4cfoY0av5IeEzmui-W64ZcI3-zvk3FDvtPKsEQUOpteZjUFLsff14t-2tTun-rF81m4Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpY1SshlB46JifvLhanQeBwO9mFFUUGK3EpZinACPIRIDe9uan75esbzOy0bRs4aVXgG4vczVDQiMVxtI2wYflHM37pdVa3yodPium6TadiALKkh8Wp8mLbIIU4CgBCGEHnDejN4TOuCQCyb7qQUSbnQj9U91O40UwTPF3l72eWrXNmHUEGTVZI8f-N5ITCkmi54ay9P7gig8BoYj0whF1CjuNRDWyxnZMUgzwXeb0K3vxhhgx0JXN0U9gQ9NdLf0IoqQ_K5RFDXrLm6kE_ylqZJmcoXWZ4L72hnB_KNQHNFFjZBv-5WZzden1RYX8EMq6tiOOAe_4_J_vH4y0BPtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALxWdetDxqESNa4L-uI6I5_EeAZIIxJjW0sKG4I_3HN6ZTjj_xNgU_CveeYA1rSsvjFdezJqfIQ4HW_mJ47VerWzVrFfCPLNLJEfWvJnPMd8ML1GOS3LKzVUF6hYAkmkPhGoggMNEhjU5wE_yPaoi7CnprC5KxCnf0VjF96IxOwyeZxmYXObgRPcGF28JGd3iAKGzDBUlQkzpwGX4c_2yyEb5Ec45anL7kAZ_tjOWBCl6SswTMpqoTzYSuFMDXLh0YX_PkmFLYJX3QDN3UiOC6E-b49iuWUy_Wxo3hN17VDf_yoF8PXdkjqj4dkSw9leXKKHKG8-eVkTIItI5HU5Pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO4A35m0peWvsNL54TLdahz_r67Fh8Wj8MLlbd5di4d16KBHIZKVvdLi44rZtotkN_SMJMOzTREtRjhNe_l0Xv8KD-93hPdtX0k7f8kcoIhgz6O1OMSzQ1kweLEXHAgZ2XslKAIQ4-5kNEE-WDUvRUgyZrOCQpkIMb1KxI9V7Joz9kc_XcNo3_ymZpUFC9GpVHjVpVYQG8ZRcOhXsPxEozDhRubvtG62IZoCKCiZCV4yecS4hqKf6EnHBPOXjhkrF9IE_RcvFuyQ07LKd8Z9Mqie35rsb9j6MDOv34nqOyYgdjnJHGm5KYEtb0rFrVSUpQZSTPhjwy780t-JrQtFJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbtEY7bRpa4pkcwwndVXkFbMB-Bcx1yjpSF8BcTRoQ4ftEF-zEjxO9srZLEephog6MXgQdcARDioLZ8GNT6pzm1CbfeJC1h_ALyxUmlREN5xGTaR_lFbBTQzjTCmvPG0IJDmg6mQmPKvyV5nQ-650-ZgmHsaeruKIvASy0Q8uhazSEeJwjnnSaF9HzJ612AT-Kol-FoWT12Zqol338RajdTz50ZpIiieNzWcD_mGVESZOkZncCndIF5fEEiaWQmBvo-u7pxlEBuwraPvw_Cwbswvlc8myW3EIBdEBNAqy0ZyzYZz4C04QC7jfwYRrZoL0FqLr3lqjFWFuHpAD5mbAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=C5YGU_JyW-tFe9-wqkWfLKbDxjYgJ8PVWTz_vD0Cy3vucP3mF6_z7sNuHpronu91m9sdqA8ILVjr277BUd8g75OEfL46yEvcmmtoTY3uNrKSJpdYVPvLFO6pTFuBeGwk9W0xP7i4tV7vY4CaVg2F4Ic6Cj5rVwvnZF5_lrAlp21jNJqizPC1ey7HwYnQ8_seAQzQUT_PbP7QJcqw8lIyu9mKyAr-Lrndi7deo6tNlST4EQYNJ_KcDtsqegcoQNZUHWijuuXPZWPzUAYQPbx8Y_x7FIEIrJTd3d2EMFEtT8gy2TC9dRQ-pQ1HwUwLAwETzB9Anl9NPg-aYbTlx2lCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=C5YGU_JyW-tFe9-wqkWfLKbDxjYgJ8PVWTz_vD0Cy3vucP3mF6_z7sNuHpronu91m9sdqA8ILVjr277BUd8g75OEfL46yEvcmmtoTY3uNrKSJpdYVPvLFO6pTFuBeGwk9W0xP7i4tV7vY4CaVg2F4Ic6Cj5rVwvnZF5_lrAlp21jNJqizPC1ey7HwYnQ8_seAQzQUT_PbP7QJcqw8lIyu9mKyAr-Lrndi7deo6tNlST4EQYNJ_KcDtsqegcoQNZUHWijuuXPZWPzUAYQPbx8Y_x7FIEIrJTd3d2EMFEtT8gy2TC9dRQ-pQ1HwUwLAwETzB9Anl9NPg-aYbTlx2lCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftq9WFvqvLJ8V5QH9l7LN8GsxwKDNol1eZNrt_lWCbrt0a10pKKyQe7T1ylxl3R9my7XdohphpAaaD821-0lldxCe3D3HTmrZSIAhJfdP4ixU_mbHclKt4Q0PjWZE_6fmYUg18in-YoVDdALdgIQrg0SVeord8dc3lf8XLT-M849aFxU51RbF-GpPjUpZjCao5b83mp-py1zp8RFg2UonfL9_fMsclZjif_yLbWQmgVCwBK-8x7J_V4irzQzM2-2XlHUZxv5J1N9VsQW9F2lBEJgFXWECRLCQNbYuFVzKRQs_ll-wUb_bU7R1hrOtzbKvVrNLlUUOHyGnORf7Dup1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll06Q1LxRVMcnZV01fA3eCqqtxIu3LCzoj9wAUD5lJHjgpeQr-Oq0RAEPuj7EFSX5alqYYVqohEqsl4mAjCp3t1QF4hUTwJWWzSaol0j2OF9L9bMtpG8arlpVRqtOQA_14k5w6N7a9uXtqibwms0GmZg2yyKAKlmqKPIJIVCKh-WqN7bePEqSfEj0frZAyUyEsBr93OXYT3wNjnn8T5DUwE_PQvG7dhOIDGKvfSClKceS24PiUTgAgQjrfOxoVb0n-yVozZQgIZzuzePnxiULpuhXH6fRUbRM7Abg-ZbqZHqL0_qQBHHNwP_3tv5Q9OAWAKdYzao6klkTqKkaSw0Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLh-bvixfNHbPOKnXNjWF60vCODX7raEhDOXpdGLSJQfpUYNMntWYGfntVkfFl9le2ddB5oKk66mRvbEjC39V0da6zTfeARKJ6iCjV-rijL3-pDIMoofxqiUYqG4fmBV8fCxf0C6B_IE2XTKa96I50XExjJQW9HBTwC-_C5i07kcUw-YSrhfhRWr_FUF9gc5mNJQDpN48qjXRrgBPvlNPSfktayOFh-KJHp_RTEtJI3jTwFNUfvzJBJGVDCCTJ2DUnyfAhHyApLO2U42nG6SSu8NbcC1E7Grhe6WDtgfpg2lIetO2tkHsF8TMC5gd51lntmiQVpsggSCg_0niOxzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkWqL0-b9p428p9692DDkieWUp2IBaBRTRsWbaBldyHYxnH5WMHDFV1c1iySuJKTZgQfDDckeILQIDiT2xfU7zGzTDgpq0NLAtUpVWR5pS87GDsae7vi_UUU9IJ-WeyYEMrsKy_a0zg5A4ae8a79eYbFlEnmSeel6GV6t8TwY0wIlSadJmGxv-iDeNVGkmu-hGvSxbxtWMncji2MHCUemkH8hipoexemwzJ0cZSyV8m4PvkXK7Mb-24TLQhK20QyKV_zElXVUC4SMcT0J560INMlrXtOULIH_3dH7oSW_iD-bI72HS1-L0lJkj7atyh2tcfYLmAN-Ny_8oTmyARpcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1xlLJBTpvM4O3yfzoXG2S2KxfqjOpZ9G-DbnBFhvb3sBspfLFWa3s7B2zlqNJnICSxRfpF7RQ6QFspbKoer4KuTkoY-ZS-neEY5GHIxAnpCJf0Zr5fHwMA6a3k2x4f6APeff8tBBgZVV5-EH3u9yBg46Af0VatuwwAQj6HczUHm8mjnT6dunRUuJPt1VRGJadpePsDUtyrSJgqt6NbAbBQi9MHBPqN7hrr7F43ThH5sMJgoFWFlou-ibDHXPNBKqQSBcJDS-QPgTOAglmwmju8u_FqGHQN7w0fwwhAH1otobYs9DL1kCsX4tdOVX4kkNLbqlKvCtysOY1z9gewtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeW8_YAZU7N_X5OEofbmGkuTox0gCbK6tsede2W6RVTkr-0g6YlKJOdF2ILDS7TbP0FHEEFTy7qpcdaefGqM6VW3-SysMftMjSpd67w73H7QHJxZNae2XqHgpSx_GcLPcDHbLr7UFh0GZwgw9uEcQDRbVDjVfMu1BqMPUthGraCgHbP3Al-zaWdhUrM9wkLpz6JhHpzg_owlXjSnkPexHef1aFfqiPcWLrF1oGr9vSPZCiC2X5efnwGQlkFKFktWWgEQE-QNEvpB74OSf0YtSG-plnOyqNqKrWDzBYZRcIIV8gId2xNEmS3DXkzz3oNJs0Iv3cw0KJGxrL9ElrG6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCnAfdB4d9fuYsV3IL-kl7MN8hoKOGEf9FmrRzBupxThqaYP64ekAC_CeuYS0qZPOFYtCCUU0tPqqYoTZFBFnmFzVzrquS0EmzXZgSY8TpPCXdqROTdsyaWld4E4Z8mr-kA4dhQTgHkhyUNToqi7HvQbcM32Qd2DGFCEsg2kpX3nAQf-lrJ9LCH83UbUddCJfZz6mWUCoSuVnJwiNEdbvWj_h6I_RG0czvsq86lbj2x7O-xCNlwSldeEFPet8VqVSdsM9tdmcU1LNS3GJaT__mmOXOBHgy7u5YrIilvkWha7PYU13MSb0ghidgOZUE7Md3-jNq212Y90HFFWt_Y8aw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=eREFsqzvsqIVOtUqlO8KI9IJwduB8Q7AIWxvEdXCB_33fScwL-rw27CVF1WjRdHzlI0ssjDKsHXEJ9nMRmgcckrzcwrFpdpoDDI4Jhwt8Zr4Xvloj-ObmuNI4ku4IcL5IEKY6of8k3wQ5WgETFuRhgpnOTJ3z6UQY8Tiv_eVHJm7PJgvCbOGNRPcTqK4UwoULE_DoPBYwmQo0BxiKn--8pn6VsUYDPdZLDkGzIduuEKK15HEa9DZCOCIBeEsE-OZjOoaWeudk0TYx0F3H5XlV-F34qdBoYhXhQhWXs_TxLkIPbGEM8pIi-Q5HPrh4lhOAOPg1AYWu-kEU1RvDAJ0sH4p3EXrFRRvua9mv4Z7-Fu08q0VsxvQ_BAgsxHespvIYIU8J1GEavJlX9Jr4N-9mkVf7dTP1JWWISaHICjpIG4hkO2CJfPJ7a_7A4-kyIDzJs7QSjQAfZCgELn2jwdmGl9AqXuh7jDcm_MqTj2_Ir7tg7wpCRfiVVGfqbOW_eEIQfGVQAdQS4Nq9XVr9s7PE6uAbW7RlC3miTbGIa6OhcUOWMCT6GCxH6RpAahodCdU5xjKHRnL5CK_mqp2jw0WYHcVA3wFkZyVOXdssNo0nNjSPRNhqxqKXKrje72fGgJmGg7y6dvut0nCMvlXkLECamL-LNqPEwTmJ74USlt-vcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=eREFsqzvsqIVOtUqlO8KI9IJwduB8Q7AIWxvEdXCB_33fScwL-rw27CVF1WjRdHzlI0ssjDKsHXEJ9nMRmgcckrzcwrFpdpoDDI4Jhwt8Zr4Xvloj-ObmuNI4ku4IcL5IEKY6of8k3wQ5WgETFuRhgpnOTJ3z6UQY8Tiv_eVHJm7PJgvCbOGNRPcTqK4UwoULE_DoPBYwmQo0BxiKn--8pn6VsUYDPdZLDkGzIduuEKK15HEa9DZCOCIBeEsE-OZjOoaWeudk0TYx0F3H5XlV-F34qdBoYhXhQhWXs_TxLkIPbGEM8pIi-Q5HPrh4lhOAOPg1AYWu-kEU1RvDAJ0sH4p3EXrFRRvua9mv4Z7-Fu08q0VsxvQ_BAgsxHespvIYIU8J1GEavJlX9Jr4N-9mkVf7dTP1JWWISaHICjpIG4hkO2CJfPJ7a_7A4-kyIDzJs7QSjQAfZCgELn2jwdmGl9AqXuh7jDcm_MqTj2_Ir7tg7wpCRfiVVGfqbOW_eEIQfGVQAdQS4Nq9XVr9s7PE6uAbW7RlC3miTbGIa6OhcUOWMCT6GCxH6RpAahodCdU5xjKHRnL5CK_mqp2jw0WYHcVA3wFkZyVOXdssNo0nNjSPRNhqxqKXKrje72fGgJmGg7y6dvut0nCMvlXkLECamL-LNqPEwTmJ74USlt-vcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCUqwGD7HoHcdJ8h_XCFesOwusrwiQ3EYzQqmPNJbaljc6yVbR_I6K-DgOIf5uS-Mf76UGMqe0qVEjASXrUiAquawsYke8sHN-wW_eelTMQMyBiRio-AlfWovQjB06drnbXeCnOK6kMfLTbhtTun12HrjMl7cqQOprpinuKnxy2ha_6GLelrLwemkGh8geOmV6T6YfgmJgK8-pn6vHC78Wt7Z20QApa-rO5EY6QqU0qO6dC-zBBRd_kn7pUmhssFL8E-fzmTE2p99ZEWUu8s9eL2leXC9Bs7Sw9SNbaG0Hjc2joVFY9EUEwNUcbnvbWAqvx9chrtx4sVTHcziNPcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9bJ6Ut3NyKmAheOOxN7d86O9Al9H_J4byddDSDTCUzEUi1KeqQ_BKYoHy-064ZW53A4BUCliHgRkyrEjwzK-AqgWdtRSZfKyTZA8ftp_dquzyxCgvmNtVTV1wYyRw_kwZLBD1OCdafW5vcFsgJNd5zTl-oxMnZr1wAGCxVp6i4OJDY1usReuGeJTRYtkR6XNlJOUtboKS7DqdgHABQbNb34ukqkbSBgd0w51iVwFyYPsLzZXfn5BuPvYrfFJN2iGeuViaW5-U1p8Ybs4qGwjLgJG0s43IGN8ruwCGtI4PdfaxewqypD896hfEevu30U5W2kcDXgp9BTiD_bZTlS2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkIgEVQ7wzig0D_RUpitS9-4jQQdTxeRgFaL0XxllpCiI7euh4Qod-Wl1GA_BRUIcZw5gZzEnTZa82-3vT7yoqFEN8vtqG348mV09cQsH0dnh1_OAh7Ju2F42cy4A8lufngxIDc90TN0_DqozPU4-9zP-OU19WpEal_9GMRwIADHPcwahg4TjtnCrHcr28uYIKW1yj14DiGx8-BNlApfnW1q0iKv5eUiI6CMlBdae02JgVi9qUt0FuAGlz4D0SzR9_aXi9jOhDozjgmd9zvRsCWd_KCCKjmr3IRG1Q2Tpey-xn2daaOdIq6bnf-giMSNrjJ2wJcjJQaPSuWedfRINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smTT4K-J41SV69k5IVtmsa2JUtCFToM1VyR8byYhLyrEBcmPXNp0eYdZ02XrqGi7S3Ox-I-J07G8wtPlFYlBfVg6GNxsE-fGXyBmFqRYV3U1G3bdTx1jG5JZtNbhed-BfTHUa9b0ZfUCjy6vvqo8SrCDL6BgzZxGJOK4nhIYok8Ah5UkmDNU28AYsWc9oN6g4fTTm_4NBFE-MiqiRXaFyKLIN7o8Uu0lK4UMEawNMjax6aavN93LCE6X_K9R81v4ZfWbXAWGe0w2Mc9FiEE5v3kbjGfXwnyz93XIESqOGo0Y0bONCwtnUtdsYjUxNKkQp_7Ms5SYCuk9oQjmq6nbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hARtEnlGHj3I5KmuJRTLH3Cu1OzcxrrSMZd2u06BgN7ElTIbfoHVL3_rVVVdICr2XdSq-h1602EBw3oo7dLNrOo8R_mBWyyzRlKg7EYt9ZhiIjQt2bfs9YnLnbPA3CdLOHC5U5TaYWe0GPZfbJeNz4TddmXCNh6QkAnWouG0nIhmeaktful6X4eUqoJ8Mop0ol43675Ldt7j_2ln_9H0fKg-JZL51GEX8mQbw9s8NsCtFGzRGgljc4iTj3UJSJC1mcF0yNjQ2U8vQ8pkGS0HZoq1hwJR718sczT2PrqDyx2hn-M8daQ9PpVMobcr3MrZMTyu6L74AZkVY3vlesi3Nw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bOuLwVc97VcBjAZSplJ989-YBZreSfytwp3JIy6ofr7X_BSTKoo9OpoESivxYat5ZqVoFqarbu6Cy47JCudocgazfZ1YeZ8zqGCC9BS1hMif6pEEe_87AS8QD0RjeeQfzu2NG4xJBerB4bz9exyTurZ__5Z4pzNIWyS5XQYqdSpG8L9rQFwT6LoZ5qc6QVSVQvJRc8uNgJjDBu2qEvoIVFXo9sDuq8Uw7RhslOGtBaP53CpB2qX94JGK9Ukd0sMjrA1qg_AeuTPfeeZ85MLK-MYuOZLuP6RNMfSCtL1I4CD4DSUPP8IV4P0EU1PLO8SCSr634gQdIZQX0h0vS6-bU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bOuLwVc97VcBjAZSplJ989-YBZreSfytwp3JIy6ofr7X_BSTKoo9OpoESivxYat5ZqVoFqarbu6Cy47JCudocgazfZ1YeZ8zqGCC9BS1hMif6pEEe_87AS8QD0RjeeQfzu2NG4xJBerB4bz9exyTurZ__5Z4pzNIWyS5XQYqdSpG8L9rQFwT6LoZ5qc6QVSVQvJRc8uNgJjDBu2qEvoIVFXo9sDuq8Uw7RhslOGtBaP53CpB2qX94JGK9Ukd0sMjrA1qg_AeuTPfeeZ85MLK-MYuOZLuP6RNMfSCtL1I4CD4DSUPP8IV4P0EU1PLO8SCSr634gQdIZQX0h0vS6-bU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeQwazrEk2QKnIHmE20ZeiCPhKVmEQgXqYJ_k3fisuRBM9yCZrwYtpHWrin-fXUUyI7qHzen_kMHsB3mWeiO0lokkxemsxZ5ZFmdNeDJfDckixjyyiOI_oTKrvFwFBb0NPdjCWOOuOVXqOYB9bXOnFUzOrZ4tSp_uwx_SRBOb96IUzq8hZnI8o9fVSkEdN97Ho6xNwStcPig2sqR21rNor3L1y9OYCq35AI1L8jGgmB1XpB887FmpCWVQpptJmFxSLdM5eSg0hDVMswYnOKKkZyR2jciH-vTiynvph485-ErhseKObfaG5-ALFJ2ubvYL2PRTSxH4sDdT8LOoby3UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2GkPRiGObRhyD2EBiWO7z4aKZbVS0zN0mqD4OiWlUQ8d3n4d7hnix3fgMdQmVvyHFy435CtT7p0j-RXgCcMIWxKIlfy9VVVOZK7LyU7kL2mrHwjoZbAjGc_pMXqcuq6Wg-jpUmG4JmyZYun6hw-GVklGiix9mjN_D79G2F-2wDwFhYuIeRkDyJUC5EIYhIyCCqa_FnFuBuKycn9ofUYgDcjqJXEf2rAy7qnbVY-n83IJLzXbBQPyz55RpsvC13kjE9wcY3ReQ7JmyF_aPtsShqZe_c816LrO2IyGyRHDvjyPCL26r3P_dY5YKVRs3eA2UawTczNQ8yk-1VtJw7v6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVN6nLojcZMhJnGnRUCvprSK_k7lxTIMv2iEq0jdOygntie8NIWzXQrHycclbXbo0Va-ObR581iYNFpKdUwhG_rHrRdAdA9qtXROYztjlFP47-qZ27JplWP9D4HeBPgBtEI-VqpC9-9_rjDbxvnmGBdUS0hKrl0lmVFerwvGKLOfcJqBb0pWM7dBsRE4J80gN-A6WxlSvgFYuQYcX6J34S_tNSxIf-VDsnnEeQI7ggmgNdO5laSNg2POkL10ADH6jWSwR-AKVb3udCUQfIjboglgQPTEyFlqcWg-A0j6TY6VGbL_b2EYrM4tdnwpDfgKKxDJrNVw8RFNXK8cSX9EIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-U_BAdZig4qdKDeESU_issTug0TtY3ytseSSdXNu8Cj923TxY3EXNZWxYKARzlfLZyrA_MBrXmp3BNndfpbk0xQFP2eezNcQ1BG6DG-IOyCdMitNCMa21Mny2GvhzpNY2CcVH0fmTjIK2M5Uko2vsrcP85Ea1B2ZehPwdxzirM9JtX5lUd3Hceo3a9Cr4KHkjJb7V2vtX-8XrBOvu-A-qsO3MUNXwFx_kmqF_nZFcSJKC1rIo5oVZWNkK7SEzxWf3YbQ2uh7g3TPIHHApS9zuPdkd3EzCNw2TCX0ztTWriNQ3nbIq2gVodQMMzUEe5Xz3MNhZIyAnC6i71e-RE_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GN6v7F-bRVnk5hEw1B9QsDd90M6vhjwSaLnzHUyTbvAzmWbQWB6TsLF1IkuyPT9X5BBJIs4Axhbc7Lz0K-G5Swmpx0b1TmDK3LZGmbD0URTr6Gl7A2PUhpJzp1qqMmlhg2dZbpTI5mPNCjNVqNkHEBAyoQgWx1y-X0txpOJYq-vYYmhhGtQ2NNMMhUyu9JVn1uzjOAhS_Ay_J0VSnDdkkNi7sTiW68lL7HihEeA-VUv8V6E1f8SqIMZ4RpMcAuK7MgpEFX51U6aIZzg3pAnuaVhlcLHOUs291_wOegSEOtTR8SVfOqoASE5tThngyhrDVLVlD9RdV1VXQEw6AoWQ0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBmJR0Xml2NE4JsBdlh5Q-t60UOXrM9juMfPp1JoyQgBMee3rG1y2ZkC1y7wHuE2_46TtaCP7a4GK5g_t8Xxrim5B3OoKk7hRLkUcXm1X40McAKm1nmH8qC5LJ7TojlfkSx9nKlV6LjnxNSzX7RtyuAitB03u9hdNzx-jYbAv7rI8wBjzW1byQDrX0WaE_r7vQfnC0JK5RKitD939tqvu7Ks-Jjf_RwhhMhdYW1e3uXG2m1xW9jLpoovXHwHlfXGGbt_P0zO7E70Zm4qPaIVsbi6eJ3R4YGzEDqJIscnPiuH1MwL14BBO_QetAHioRyN1I7PKUU-xRjP3ZpEOI0_DA.jpg" alt="photo" loading="lazy"/></div>
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
