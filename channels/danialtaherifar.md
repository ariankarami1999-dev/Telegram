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
<img src="https://cdn4.telesco.pe/file/omteJZgMNAQ0wUIjb9roDQU8K9IreoTITjSO_Db3z7vXxPc1iaZwJXpGe08Si0gyIubBgNR6PNcUKpbGi53R0O41NJdnh58WadAqT1xsTM6Fn8NVtXatRc1w42y91iSO7YQB-9klnsDbSLVg3b-t2-F21KB1cvW485tmgqHtkn7NynCU85uTV9dtNmpSL9wGZ0xxQcEqaeIgRPub8DXTL9piuMBPBQc4QnyA5lZtr7iYmHILGPVdm-uuxBWFG33BotnZZF2MqBBRTkF3ozx-VfeiC22q49XGEbCy9qsPg2XZQQFLVZT6DaduaMzoSZQkkzUQjQnIqG_I-qjWqDKdQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAB3Ok_j3iAKUWB7nHGduetCH5z73Yq_JrTAmH4aOU6vY2vUSNeRS7T_XvlkzjehprjrMKRUdNa5o4IpN0kXUCcKL7EOLGkjs8GGJ-ntEWi9uZj5TPG2A27aANMk6C8Xs1SGAHVoC9yjZdj45_1p5QCq8VEBxHGTya7kKJb7wF0lzIiGiM7oqqddrvJjx2wdZSJsT3T1ThRcX8q11YF5T96YmzsSPn4RgeTO1DyeDQd6es47-PncmLz5TZdYVF4-iLAShSqUcK8d3mxhH4YfNYMTyYP-I_WaRajj1IugSSloJOiWYaOoqgTFQL_OvIOxdYEV5JXI2-LEmwCidpyeww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 241 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 486 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdzQF5CQH9l7hUdcaFXQ3dJtzLRQIzMTUw_jhp54PSYKhse6NYhbPsq3B-PXd7UHEpXC6fOKbROiGzSvpxmieRHUw3eX2qlbsxDwtReUV7Ut1HZq9R7KiyTZWQUSf3xTN4CTfO3ArJ2SyTDidVu36aAxnKU3N2TDhLJW_UtCYsp-tXAjJ7TXGix_vVO2HwMM4q6uBEhl7iucoZEFZ4c75Zzl-3mwTV-Ty3N-xFokbmaUZ4tbFyaUtGApoob7cRcxzy6jQl0sS8jYmjpUwLisn6r9apnxBY4jxImfGTR_EdpltauFYiwP7lqgFBOYCNpbR-XeROKX52TFnirKMH0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 893 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcqHt9HNG8ToQxba_jL7SRt2K2ZG4EHweKkTffWX0z9PndtBjTEeh-wRZClwXy0lfxj2oMwP82VWtEV_YmkSlT23DjLGaiVVKr71wNExrQX2DzgBk9nJ7n2cPUHzNPNLB7O5DrOdjiVWgTA32fw8pfDJCmK_uWcBlU9yS8zbZUWS7ZnRAjJPPA8X1Mf6v3np4ilsXpTa00vW__jUs0x5E0wRadVl7QsrXRtUh7ZGqR-8LVIiKdwwgfwEdkD_sxRytCNj7mibZ5iMDh38vhAIMoGSmLBLJgICrsURB9CObrnKxFgRL3gwDQ1QW7dqRTHN3udpBj96234OiebfJ9GT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 845 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P74be_yNV08gGkVN6-BquEnQLPeD6q_VoGTu-seqgGBpv2BUOovctuhRujHMXgeALDMV-RDpUIXCDAQqb46TSAkHcM4FMYzopJkRWU27iIYAEImCDuFIqWkuk80BBgOgB96p4nQJPGBpFdyLfLJPeY-HYdRjIrmYa0HeT9rGH7p4HHaFA5hW53i5NB8oxgh16SikgWid9aWTnn4CEJCr0F9jUzLEob6PaLYh3RR2h8qq1_AVK3jsgrBiEjC4PwXCyFfo8_iGfllzJNf-R0g5qyWdLnrBt3H8JtYeof20tbf1lPk1xj0GxC2Fs3SpPGWyQmoE5fIe8c7M4wgW4AKWMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 940 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNdAxeWg9kvFwADXSPOFZbMySit-v-fCSrXCva65UEuC2hnKTd4X0i2TncCunOM2HX5wGCG7xa3w-nr29gvM4cK38f9dr9_0n8n3YuiofzgnM6LgrHu45ONRV5uic5xSCS_W3GQHWQ1RWH5oz5OejS8vyNoz8KCvoGD2rjC97sQWoelkju-KZ76Yn4Z2nTIYdm4HCb35wCZiqecGiBhLDvYKT8L_O4D9_PENLnSyxGwOXTgemw8TkpNhe7ywrj_NOHt5fIvOR-xKx6dNEN8Uq83RT6WHTdfjpbU85D9Njki9Zt4EHGMEDYVko4vcPrjpIZzA54ls3rKfEgKAi9NFGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1ouNIwuqSc7z2a6JiYKMx5UHyO4LpmE4AOitu_fqsKNLvABMXJ_wS2mvlPWShi23HDkj1o0btp_-yZ9obBRHAi1j5cnAyZFvnsA1OQ26xnjlufp-vejzMbyPdjiMiC-4bIyxR-ZTC_tTPxEb7TmIQP7DFenmYQdhhysHyvYHUYUdbQK04A0QBwhZt0Jzqf-JrTguGhv_g25YFkAa0Ee-pKam_UoV0dv6miXPy07xKHTxbujlZUFOa2e9MdF4NhdVR8ycJ1_juNRvKlrU2pX2dbhl1LyxSAkBtjj-L3U5_Enj8bX6qdLsK8UKN_fyqIbdBSRW_mpa1MIGT_OXJXKiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3qowhacuqap-R33OXJXU7cbeGehgLtSTkzSmTbKQpYL4wgW_1WVeLp5AhH7DbljbeTV4YFSZbz4ZfAh6VvQ9hNGBldqSjbi5Yf6qb0vKp0WJOUARv0UHhKkVpD9v_55HqhNoPut-xO5qnDXtWtm9krWUGJ3OIXFiF3DqspfUjRm2RTOHFP6EBeoeGzLGpNbNt8v6y3c7dwlw9_kF0zeFQYRQMtJFTOt_xcCrYVyuyX78SqOfu9Aa9pTTQFUdWtmunkFaRRJdtvJSSNRk1Y_2Yk_1Hqy3VKnEmPuJ1euM9B3YT83De4jKBpz1QLVPxk-6_3vo2hDDykGqgjPpLhd6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpIhiUJ3YfzX_n-1wuTe0iF8ixnV64V-hhH1iG9rZ_5dstguWQA7zXMAiQmeWCn21TCvBhK8wyQeVwE5IemkbVl29ILNXVFHnUjjIsX3mbjvvw-3XpkJwUuGYR1EwiLkVTH1uRyrnCQEAmmTXzrgqMdT-ltgXH7y68_JVWputJ3kFxomN_edcvhUH54jqBzBgyliGJrYTCLhh3FReNfaredp4BeD4oxRqIDRArS3qnnKLyt-ueJSA7hkhGqlmf6NDaSa6yXI5nM-AY_gPXlrGAQmsoOmm8ZoQzx79fvTomxl033-BItYUPIGq9kKi41VDl1j7vRmu__eqETWhDdRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLFp8s2tbmohTnslUiMKH0-eKIxo1M-eeYnRz-FDFPq2aHsobmMzb7t8g7dnSU2sg6n9_kE9u97WCHbetGUpuyj40SGB1BJINQ-7ssq-h3YD4x1X-oHUu6gubxtlb68J93i58S9wxISpLFFybZB1dHf2loPkLtXzob_HiohkUYpR-tTMmWlZdRkO0t6voJGV4DMBoZ1FVFq7-Uo2C_V5wTvSzq53JryEjQnE33vrYtebE6DUqP3Q3ikTqMkcP-Bk9PZVr6Y9Jke1flwsJW6ojgBSdLZ08KXtgX3ATZs-e6txUA9TyUi34ShyPjAUPZc9L-uQ-qbI75Pf5oMLpLpWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aczK74pLyxMOdYRy-ZUolCZrXQKHvqZpkQsCK_qjeC3KiHef8qNK0BhIA0fwmU2Y9NWvWA4uv-YjNL2C7WNW4iX2APMGWs7viKk5vTjDaOR438NvPCg_sXRHcM5w4XYEDmBCvSqQr5OycOJV3H_8Fq6VBVUA_oH8niuyrpNrEaakyu9Ew80BdvYNaRR_C0bwAD8qt2zWmD4QCaCPiCM1ubJBW0_5NRj0hPEQZcy0nwQcXDkMCUWWK6FFdXGf3Us5AGeEx6jeaaYkTwuIvJsHqYOkzb0flmkXHKQiUx8lElFnlZvSeGEV7oY86B4-6B28DiJe0IodXIv3ly-bld5yDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz1oqZmlUMRmNRd1mHz-Jxd-hZEC-pL71yZxeHjnZiyqkedcbJl_1AS-NNCig3cPXyZZNrRaanMrhCNOYl-n5HKnMNba0fiBc-tuBDIhKusUJI44aLeszARGTG7KT1lG8F9iuM7o_tnuFfoko2lT6Uj326a1ms1CbWC7VlkBoeKpgaJsoWzVvaJZUniD7_lMhipb3QwqNxBuZmSEKTtq1_YqnWDtmpy2D45mseHX-BElcok1bK2zVYW_Ez6eDJVr21oxUbb74DyfuIvznu33XIY4j928MhUBAYtb75ehPDRniSswPibdO4HxL0m-a7M6AmYb3-l-NqEPNwTTUPHkjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPZkmX3N5l9PfxeIaNVKWWlxOEhfNv0vj0iAYROw3x0dyhJBfi8w55lsbvFHbItV9I0uNU21uYtY1xbKdQr_FMl_5Z3Q0qIiMs7bU9_l4qwxcpmXos1a9bqsGABBQQoXwnrOsnNoGnkwQAA8S9EyGCQ0Dzk-5qmpJucSrisFPe5mFRYKq9-Ew45Fmae2PNilwnpqnQcIAQkRm2hoVPbE4n7_9AzGOcyxwSKD75hux77XgtPKFkWuaFld1IoR3N6K-snUY1YPg02k7wG2R_QGm272FI2r32kPbGGQxUlxsYHrFxbn3Z8ZyCEXPq0Wmror7MnbcXlX5s8kihz_iob1yA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=bkdbx-OCGpj280NiXnPWjL8PTSbgFv_dYgo7Gj-rfUE8oG1OfJhbtAal5cxbSayerEZ_-HjGn4qqdMHUi4_FYJSdKb9Ppqu763uAGaysrr6GWbaQVsjvkAaGS21dqTGJFyU5ilcNh1O9kh7qY5rLOJfIYLjwSj7-74LoUD_SEi7MECBGtoHhexwtKso2z32X-neMpg1Mszw0sSAgZARM_NpHkH2xzWlpDP5D3iMhZiiCuAcAdSzyvMb1Yneqsy5p4-iJdWDTPAbxLzRXBurpCF1Vll4OTlvz7peiE9jCW9OKznZ3UFXa0TfU8w6EorGDtkIYrKYI2UA-4YXp0YkpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=bkdbx-OCGpj280NiXnPWjL8PTSbgFv_dYgo7Gj-rfUE8oG1OfJhbtAal5cxbSayerEZ_-HjGn4qqdMHUi4_FYJSdKb9Ppqu763uAGaysrr6GWbaQVsjvkAaGS21dqTGJFyU5ilcNh1O9kh7qY5rLOJfIYLjwSj7-74LoUD_SEi7MECBGtoHhexwtKso2z32X-neMpg1Mszw0sSAgZARM_NpHkH2xzWlpDP5D3iMhZiiCuAcAdSzyvMb1Yneqsy5p4-iJdWDTPAbxLzRXBurpCF1Vll4OTlvz7peiE9jCW9OKznZ3UFXa0TfU8w6EorGDtkIYrKYI2UA-4YXp0YkpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxG1-VdBx4XLQX824dkEfiH7vqANqXZQ0bn9XdUQLqOr60POfdc0Gf94mHbVoScQrSn82AV-0aWZD-Wd4-UDkn_xiIH9QU4cYCzNoFaY7vhm5rSYv-QOHsc7yMp4IPq-5wdRe-l72g0ZT6nsRRNmS9C4ZLoRBzU655qMq8RzzJ2kUX5TUv6iTthpwR_hV2GMqh8DKmKpE4tHYYZbQQxbci-8mqU_vmJHKBmh3Bwf1UnTL7Vk4FxSJG7hY-pvOp1MGzbDipQ4HMT-CIrf2KXFgmdc76fbb5UN5N6XbfYMA3liSv6OAVx_-JxZ1mZiUb3EdiPhpMQDnPHQrb7G-qJpMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix9AnEmqT-uzrOqFnr-SlIIhs3Tysiaeg4CvLCUorKHECt34g2MueSAHIId0ExQpv819MVYNgNgVJlhySPSrHf7-kUHjNI_V5KGfuEjKh82N0E_NHeyoR3K39hXIdQU9qEpvL1P8c3xJJ6xxO_TBREnA2Wy1LaZTkHOnzkCv7G5TTIyltGgYH-xweM6mwNM093zrL3-_Uw4DbP-RlbHVx2YO3EK2fTDHdtSlDpDqRCC2EeP-i1zeaGaIOTB7L_nEAH5RmzsaWKgZBP20hBnqL6twqvXDBCPN7LJNbZP7G80oqfDpdYRBaOGePgvjX44_HREAvlq_OOeLmxHOzWF6KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVumsJdthPXpDYGI7k9y2VMTRutwc_QTrbyIb31IcC-zYHrpOXBLlpNeQcI0OB7Q9p-83wLirYJ2yVN4peCtpwKdfBpMGaCPMQSHUY4pvRguuON6EKVXZzFvAXqtp8PrX8gM-V3PMQa24SdNiIQXrBb2OkQmfjRTeOgKSN-HfKHEm_--HSIRZ_wruKtYjG04GDfwbTrK8nm_nmYFw0tu2ZtTUj3LppWogGcWeHRBHhmspH2vA9zNYrhtWm_TJLx2oSoxv8eVzQZ1ZoM6Uv2AM2TLE0CDmGXhsPU2o-q1GFKNGxPuThBDqqqHcxWnzPJDKUPuwPEbevYN53SBaJ6sSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJIViCelCiBB6m6KNN9DotdYQfQHHhGzlclPC_FbTOIhm5rgLmw8nJUgESCbT3C3Fen-WRy8k-eof5O1R1Chmix-K7c697oL0CzEhmqohmgQvl4kgisYKuIEMl3XUVxqMtRJd3B4la314PTWxjGkZpg2nSdy5Ffhl0ZV9rY31_qlw0_e1gpPTKJ9d5eGA9v3zEXrFjH-VVmok-jsj4mgweL5IbFCgAFoiaSyHrCEaNryMGp7--Xu2sb0bgBF5cfsSUgfpzFc9DKQGvFgKA30o3meaMnygpznIbtV6KnnBFNk2x0dAFhS7DTdI3nl3TjEF_APoxuGaLtr_lKL9eDpzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr1Ht5_3HyFbuHymRkgUyOoAC3DgySJbb72iqKoazGyM5zti1Y1Owe16oRqpl9iXyjhTpdplV7OBBCWnUGm3nr-cjblOK3__m23Vu2kRkWv8OG2T_3cOjyhG59SRTxXnz3GJE9BBm3FU8BGXjkXkolp0lkkbBitZhGHv2zzZ0ctNGFIPFYU6HGOPp7q-nQDzJdZBn-M3i8gIK-w5lRxbyYkAZwYGZnHTgzxJs_f5Q7KD9rI8e3WhfwimjCxQ4MGjQ4ibncwY6ZfS3TbLJeVAZZIYIZ4K69meAyLmULsQbpAGkdx8WszJOMMQc3hF7-s6SD1n-v4AGDJonzIinhsQuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9YIFntE_qFjLvPYVK0sKkEncEsj7W3iEMzE2MkCjRJpEK2wyAEyLbotXI5r_05fBH8UO6aoRH4rQHTEkt1Bn-7XaXD-U-A8ktTZsxOB6K_DB6DMd17gTIhCMIfbIMzRgZxRooHOgFKDNMvlEnU1dF1ay5CwJhkihoNj74KkTlUHawO1xc5Kht9nk3pRes5md7kj3GPWvrlHKWwyBrEo6Eh4y_HUL7pTJ6ApoSAWDXnGBYnaoYLhGqT76kArlo6uPFFWlbunlFalCqTdqiP1zoWBztXqRqOCx70FLFeeCM9FjYmKnHdQkv0ct9f-1KKJk61XendF_w_XV0RRJwlzIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9QjkxlIr4jgb8zPwB92L9WLlmhv8r5iGjkwCcDpRMDmW6P09mOGrwmrga2iW7GNsnDjfq32I5u1TbQMW2CxTd3-ZoOJi3wlYZIauojl6fwkPUNE-ptyK1eRLpBneJZdYTTrkVz9SImCZhbB25CegqIUPHz_dMTdJ4xVKOCk7neQ_omUmkYPEoJPLUUIaU4bQDg8yrh1xdwW_uMeAc0_ktpEnib_zlEDubmgb3yAgwvytho9UN10syyguzcvUwCMgZPEVo_RtmYJxqICeX0R9zpEqOrwxBF9ilFCF8M21Z4FU7_61PiUFJoZ3tbCga1N555rbj3UnQHMHnzeYtXEUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIKWS2tCynsu4Y0gMv_O7Zg1b6GNTcavBj_xYqh8muK582MLaO_LcjZj-wzn1gh0ftSy_XvK52lJzUIJkbXI7wz4OL25zz9pY1x41fvEpzVF3UZc2o4Qo1mjdCABoImy47e62JKWjtAKtvvkPrOubCglNPC6R0DcZKaWfdfeLv98NBQGufaBSOQ-ERX8_fnMLx3Lz1m8UW5ILz3QpUP5tp3v5NXnDHRg8rkv-_Yvr0bin5-oIpSJrz3rEkrUq2NK7aL9DubALvFLKDLh64JYyjwrnTiPQvYDtan-AMQoERdefcVcPgwzOLTypjtryj8G9cXMkSObrf8G939n0fW0yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2aN7VgF9d7Jno_i3XzSjOIQQxzPhnr69zP1NJ8TYaiPbsqSTncltNc1a5vrCyX05sIRVIcastxA-JwptEs-JMAa9y0GEVubJczI7oSVmkVYqwlK2ND1BYzASabIm6Y2dzXj235b52u0XrP5BM5QHmOYIGbxvXptQjd6MQy7jnOcJjeMIFhK6bS0U-AJiSGyoTAXNJSvr502GfZCYdwgWjrReDl6KpZXB0jhdD27c3ueQwMpbTYGuxbkpbXDiqZq2oKyAV2KVuAPrGJ35VggnGjCNf6yd3f7FVsO6O8lMOVm9yW3H2CNV8vQVtdPqyjPzVA68iSklNq-3IckoZzSUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6vJwU0VeyXsK6MMlR07DoeM7mxzQgleLM7gYQYf-eyKvMakMjly_QrKSJJWHGNTjcc8MglPywz7T_Dl0WsbeQcjoakBT3MAh9Q3cuPc344Q6pMiHPj-wlXIlo9Sa4G8tHT-VSIZor3O5IHZ21mGEAYc-Vqz9a0MJL_Absn89IevVshI-ln8TDBfqQrVyoUZeFPuWSvVgcqHtvY25ozO-hHAStTpyXGnnruEdqefTKhZ5zHeB7bCBR43uB3ZAFqDQXOr8CTvd-g7vagYhCphW3ga7usbid3rZcCEpGYticQ7w-iEWptLhQFn3TOY53mlmlnr44JzKDQy0DS1b0Tajw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv0du9Mms5kc51btbKf0pbIuoelDNOwM04EcsEn5mMFBEnX-LqJ9RERUZ1_D9BWBPE5IDpwZ-wZHbW_YbGPAqK970NCIthlJ03lkm-MBfarOFp_dzddsZF6rZu_alTXSNZL9_OOnBGi_DYcXIqQ6VAOzu78Erz4NLL6osIw_cul3KxV3I6wPC0mwy2_GLa2shaFU8UmVOChoy9JNjvaztJq8ac9bggSoqYCAeK3K4o2hiDb_albGCO_3BbR25gA76R7_9eFKIB-xsxzyPY7Q8P-s1boJNDfM5Ab3-Swg4QkhSUILLBvd-QZxdI5gYgpTzYTyCwguEapQ6Lizk9FdYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp1KzhS3dbv4fwyhXX3cY-YCFv1Herym8S2Y-FECSE7lEBLpXuMsYQ0r0KSe_ujoB72NAFWWMi0_QG4QVjp0k9F_q04uMpZcWKAOMDNsWZPOxNp0VOikEI4wcNabJgR3eI94bMdj1o_5pEnVtgWDf_Z75oH_n1qbOwcgr-YRcf3LDTtBvZng90sMPPNpR50mwnHXuRTGK43WSn60j_lnbeY2L8divddjJ844EdEL_ZNbN6Qb0MQc5lA7U5diCHY15H5nuI-wGliVapQkjByQGZyjZjziowVjZfwHviLKbUONGdBOz91H9F8FGpQcmhYEX_dPEgckNjRNCSuqLEw9cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-lcqYact_MDMpXKIVrlOBaNkUoxOQgt22VEEkOnlJfGFxOQetGZuYdr7b39Ar9Y5Yx0qanYw9z2HcLFL_NV75uvHi4rHwkuIXfRDS8RZADycUtTtofV_7DtKn0zNXhWcR_JbqLb5jsLQgLnE96yeuvkwY5H22p1u81FBF9ZZJXWbgYYMgq2DOvYEJJs1y5VHPlQPeqIZyz9e0n2edi_8P-7al_bEPsBXpu22jv7BsLjj3WnZ3_CcIYd9OVvgijVRwJNR7LBQ3DD0DpjblewYEjymiuEWd0ly9iDeoS-11yMXDG55xWu2v794767fwzeV-5iTR4HOZd_gMUoH1zjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsS15lSI4F6g76d3v4egMVJ6FafC7lUXMO887Bj4WPb_MrBColTxUTfR2swV0wchL6TyEX_vVqxSsaQapaRkA1LwPb7kQTgqrgDSXxCy_iMq10eolwVmFghMLOlPA_0eFIPBCV9_-3g6ZhcbiqRbU4jtXbF72Fb-PNHIKtoV9fs-Wc4ewUF7L-sSlR2Z_x6Pv9Ayvtnj_drVxlBKdIv37pVIAO3PdeLTsjpmppwvH5XrKHwgPeoZOvBGHh5M7oncZYKJNmGT2k0Fz02EraGwfyPRWbRgayif2z_97QDGRiHpIi1GfEIJCURn5nZbf7CTub_vGnd9GtdMR1qgPaR5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9t5Woks3QOEFEW4ZDKRxhrR92z-Amgem6N0T19vTrOtFc7o5z2CTrMgWoK2u-hdyFkTbIyNGDSsaDyrccV3sOk58snR5F4eS414NU9ALe1frMlV5rG4srW7m-5LIecWocgqK_Lfx055wWticYX3cHGD7gGWHBVf398X-eIvA9AIjAWpqE70_1frjmAyuU1N9Nu_o2rr-CXmeHFhkRLu4gTrmQ-5BPtt5VwQacQ69RecPHs6c2YmNSwvkvurYSy3Yp9Mu6Za7U6TV6zR6ZEEpsRV213D3o8J5S3imjNJ0UtZ1V4KlNOGBplsHmYpWdmL9IFI783leiek3RNuDFK2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJH5FsWPdRZeFTVIVtDW8pZQmSci0oVrv1Sznzj3tDQ-0KHVNcgTPhBV5FU8zz16_GYqDYrmFkXuWijY4cmyrMqUCsIV3cS0-HOus_kUL-qlPqg7vcjB4gLe8ehJAgeSWjSI04AFFLphEH87t3M5ADhMIS_w-XAvqyN4Gg1w6ptXaszF-o2vnmnCgV6dfjTrqhxdVJIWVGTKqitGu4cX6JTA4Hn6PjVemaCu4anQMkAPDO1w6PgGYo6Y0KZmWgg7IlLlyUuwCKuQ-rLP5WU3jUpyiQFoHfQ02Uz7u5_-S8i4CtJXYyeI5qSAauEcL-q5vmDeWrSCo0En1xNIxU5_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jjffs_AdubgknO3aHhQv4d1craqLP1f_FCyhfcaAKf2t-V4KcUtV3Rc6O4jkCGtN0kG9RBfkMVHYmTwOXtpk8YVHk5GhSGTBWpfXWmugOrFvHjQ5Nvd0mJOW5PqjQ8DmqgSMUozMApQ1bk8dwk5OnVfL_DKAw8psZoEETv9FsZKz7Lx9zDIz87wknU_XsqTLHTznq1V6x-2tkzBLkpWUIkjCQJJop7Bj0UmMCZvG12An3GSwy_4B19WdsVZrdxQw3bmPNNTNV0MKTdR-hxrNEsAlWRXgWA3T97JgK7eqKBtfLkION671cOm5J7tyVcoSYta_XQS4-0SOcyUMcrby-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntSXiUOYhEnLhfb6055XM_FrECvdjQh11MtHDfwPlWTuCVbGw4-fanZD8kfQtcpIoDcyxyFTCJnxosWPpwc5IwNPprvEbOSRyGERRntZ5Nhvmi9upeLTvwXImnPWzHi3zV1SwHuwBXm-U1S-OZuitvkuFG-M19sCVCDcBYsr_nEpE1IG49vh_5_6ZAm2P40KSAF2TGcA1MulVKu7eGYlveA1z3AcpepaESqvaEGt7-0O3vR5hyrshXi2FcjRM79TMiIdjun6ebtN-7Bg5lsep1_0T7E3_D0rjeCAAa-g2_yjNapwhkHHwxZSAv0Zm8y8JW4izKdSF95R-aHE2-ckCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6K3VnIctEPM65LuB3t_WT58J9FF-tCmkcCzCKAFLaGzL6-e0psVhJm6eD7iPcY4yTUrNeirQWQKmzyoEG4oGeceH7lrj_5zxgT708IUd_o95u2R6GbKVa0EmLuRzQBhlOjBhnmB_odARsyIxqcvvvtSl7JfeuuU72ffm8oC5bxrTpoDS2seAoNQCwVmiJcbI1imVo83FQl2YSkcPbc3Y623Q0NBJzAuy7VLtoEP0yOSb4Fwh0EJdYMbKXiEBPxoWyyU6rPLR62_-df20Rm-jS4-X16vT6ndtxqFBO-5zYbRf319jVvTTiQ5C1u2TKDmNN36aTVnWDRskBv5DdBg0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcLRf98hKpCeWCap0KYpBmyE_oLR-HNp6aL81j-H23EGbhbvdwXivTUp78DMrhIaCG2w5isEW1OgV-5e1Cs6nZLX4xidBBZZeNDsoPrA-LbnvZvJqk8ZDCFo-EWz9rc3FrpXv6BX6ix_MFn4WZmFmAIPpyhcjuKU3xeISJFHl9g15XUIFHrmebBEAlYV-7u1-5E6QpqvIhMZOACCsdhWAKQgfi2G9rmVLrLvLUGY-e3fA4o0KI0eECjMzEjzSYoX4n7y7w0ykYGme-ewWHOCwKFO6ys_Kk28YmZR5ZWolEeQI8T1Zr-JsmDdGAdVmqpydFnpbbqarOhxpbfVCYU5Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foufL2QUhMQo8C1W0B8OmVVq7yEbXBaO0O2Ms6jtu_rvHNboV00e7iH6z3LujVlbQS_f_CmtBYUhdGbrfMtfiZP5jP-bF_8jZaperiPpYqkGIjjh3ATDlzlOB_Cjnh3Ho9wGH0oEPYwaTvNCFIpUqwI7rbotTqZ5S1lnOCMee0AIKU-NBdaJAZimy2r6iA1F-bPSLdeZ29orwTu7c7zPyNLMclK5T-PkvwamWseqr9G6HFGqCA-JQeJiq32i07WSh0mU-mxvf9-OhJUeAXeWMcNDGIklKjdmg7DFYN1v2Nxn8PNXWhSPVD43Si3nhq-Z32wbt1Ckm5_IuQNpQxOYyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcbygBIA8mCGUMbn3gxYGzlPJ4kBcKdSjfldQgEZ3mmc4WnyscyNO76L6RAnWNr6hbbmU8YRSzS8vyhmt731vgQKE5DGKu7aqLX1Rrz1aYeT_KYjTUB84VYAvWBMaNoLy8JsIKKc_jlbThbK7RE0ReAmtfGJ_39QUlxg-Wkow8FeB_4adpRAVeFIywTyeZR1PlK95mo_ynVJlRDPwtluFQzdiDisHJyPviO5v_zvlhqRCtO_gAIg-tCvtFDfuB8v-Njmu7Ee6_hnqxPaab3Fp0O19k7WMAqYVCfwATEbmGhFEBnwz7jTvYb_x3nLzMRQXWZM8Wo2yPqEu-W4Qplryg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOE0LWWZ1SD2H_p0IqR5lUbu9FdqeJi2kHqcf6_RMMZoXap1BxoeU-82evD-j6T1He5kj6OgcNbdTKCFt9PGA-53JLLNEYKwaxl1dGUE8k94hMsdk-FlAOC_ni0VLk7ZO4x6RECE592z53WxNbK-uRW4wdtR4NF3txatDFAI67NZzRm3cSxIIgcoTzkjJ95Dk3567UZIoiWH1aVvtHV490eQTk_VyBAI39v7TEvvmcgD5w9jrv5DHhghNexYQf5cXnKKTYU3fQjP4CsD536ulrWkahO0m_uNqtuuUgbYcvagTV8a1Um4344kXcfIQFm8mOExOFpn8VlNpAE05-ipcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz4X-V2zZ3gVAeG_NdFJoNO51qhXN8t2dz-dhsOeaVPW588PnPsRyhV5w-GmwpNKdy17lh72sJhEsJEzM1L4FMZHi3zIeRXdwJtov8djWqZrD7d_tHwKgf6QIf2CEIWFJ6g0GCpBws4ayLBOKTl7PeJYsSV39Imi8LqstsCorsevODGf81uty0tU_Q-ConXtibowFuI66Ag6Yr5WzPwLzMOBaWF9vsV_nuIF318a2OCmFCr9cjZpIM7K5BPP4YFOmGh-qxAeLyQn0_YN43RVtm6MxSmbfZlQZiQ46b_XrVaYD8w2tE_pUs5RGwqYbjdwqfm2WL_NGtdFXbfcr8jlfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf082ARRdtIauVTocR2VcVh3l8l9bl5dj5_A9GspzQEWz36wTOR9KAN6Rumb-_Nm-6f6fHPVQmA8MgiDygJpsMRy3-EEmojA-Cw3Cs8Mn5ALwafmjM8MszpyQB_4msEO8BPYaiNoonDXXRWggPeqE0AoTLV-fQhKiJemxgXBKSBmPcAIdhGGYl3JQjLt3vojJQyzolKmlJwey1MEdGap6PxgpIrtJPEXgZV0oBqbQF1KmvFyPxpc1u1wJdtKmjAXWShpgHthdGjh4V_eZ8yjRmZuMDwQGtlzrfqBw8pJpYQ3RDRirHxnXk9VNpm7Pns7sdA9kqh6vJ3tYlYt1_sRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJ1CuImNFLmNqrN_rsPSKlYIsje8Az5ktzedq3tmwGXOupcGlw5T85gBGzebPNz_roCgQwQuUa_a_74AY7Y4vgxTBGTAG9tpJX4daQG_dzQ7kVnzrZL31JR1wi6_7_YaqUFy-jgJCKJCyyTLucfTnqInVLRwbqUvSr_XTHckLGAEW4bgMhRyr-H25PGLPKqW1fbO8qO2G8qF8g-sNAGfpdEKPMhoWyG86Vdg71DUUWO51XPqKrnyrcsCnLwkM2zGzgmGqDwyewVo-2M-_sqyv9MMecf_7oiAyzMMHRPK4zMNbQCegyiTGW6KeTs1AnfhHneyyHJeq1FUv0Eji925IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFp00NhzZxARsGvI6MuzunOshdU7J-2M-Uhy9lvyDdSNI2seQP3XPP6_Az87RI5FNbrIkSC9gZn4mXg4QRHpiGks7Nck2L-XoA9167ieJrT1o-Bd5uOqcTXRfVs-gMqQuX1dbuHWTmNf6fYOR9Ac60koYzy3q1HLc0z8U4eA21g89yJnP6YO3TVEPc9F6FNWujoOGQx5MX5uLq3rEnxAhuZOl4P_gNK-CSZbJ9O-ZlG9ovc6UVqPNRXijm5N3QHWespoh_d2-Xyny2yHBfbbJ0T3gAoLnfeCLhjL5L5WkT5z6XjkLgvV7bJHF-m57NLxeES4ufok53Sxynw34GcRNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR6lbgTKvvTdi9PNjAqZYMNPoeLXYosnu1yZ3WFghHx-29Y3ZcWV9aN8-khzbdPHucB7S3H6qQk910qWHFzdvqR_Wc-ouRqrp-l9bUjvsFQTE4_ZD4DZCEHTf8fXYx1QeLB2ksrzRXiA-qnVLTQAhdOtXLwKXLfwuRNl8gkxK5NmwQC8ALBz8Pq15WEY0o7rJKOY-iVUsA4krB3bwrrIQ5ChkPwsWQ-3QccYBv7UGCnF_eUhtX0tfQGiE3vwohPpnNZqjJ4yKXuWTOGmhxPfy2rxACjlG4IX4Lf_IPpGkJNWvydXSVunDb4pSFnQhZq_ciChCRqVz7JNgMWoyuUdqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxlflcS00WoyIurdkenRCic1kOMmX-lFrO0ibFnoqtl6-C5tCj44_xFA58Wik0p6xz5vtg2UuaQc4rAoINbvGzZ3iLu5ztwnBHVqM6XDHSW8q7TxMA5jMaCnlWFZC4CfjD5CKuiiS7KiO6Bywi6cSAkkERuL0IoymG9aHmLkuSKj1joWXf8x5Ea0tMLOsKJnb7bgorMA2uPwR55F5ponaAf0hZ6kK9ctVqKluI50TEtzEuriFX8g1ubc6rE2G6NkIc7M8EIYcChUb3viFd-tyAxc2KiIKntJWr9ISKSpAe3oLXazKA87OAh8lBK327zDpvbMj6S37Wk6mm2liTgeCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV3r332PmUOyhJjg02_r7EiOz2hED_pbM5j3sDh8URAEa-_6MWig6nn2Hetd4J3yz3vJWSKVQ6xEL7WIMayVDi56C50ALdlu8Sxo0tub4CmdMe9wTomgGFyeKQYo0QgXDSKOvBSQJY2xG-YqaPUF9TY6rxVOpZMqZp6sRyqCx10-1RhLaNjr2vxWdn05-LxwC1IrKY4nJop8fztC3dbM7_d6PaIHHxS_irUN9sPDp804LjJUsWxL2AdSu63rhv7wpc84MfWPRux13Yv9Y76YlhY2LAQujNK0y0uS8Frd1ZRSIiMXKL-JifheCLXAGUIpZqsquyLZgYI-HoOuLkkOkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rlllx9lqJ-xW9WAg_eDIQKz3zcMhZvpYlDPEKylQGk77VBUFdPJpSA-WSZUMy_mKUzvumAjlBuU1ayy_ypOJgQEEzLrZPdyltdqw5tviHn5PdO6Ry-yiqE3jsIV-dTk7JJt4Y2YYpA0cdR97dAiTMmHwrlY8lvMXM3xtfdvQXwDP6o4pB9SaGMfe08EXKvdJKcm359aS3FaqQBSj6huOn-HurJ9cG_rmpxDFaPRY7wlrWnbBqmVTutA2o3hNFmdLYwg_dAs54uxaLlpehO5amwFWAqxD9jJycQx4ewZtbHJfcQRdy8Hr71c0cz1j8GFN7d8iJqkDpbujP7IxVMUUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRPHoDJKwD4zeLXksaZyaCnGSaoWzZebn97-JLtWyY27WL3GtKD2h3o7zD51uY3e9mUpI4JfgAUEfdsSCCriibxzey_XbmxLgWNN2K-FR0ZttN_-2Ouw57Wi4K3NvqQ71XPHedFAblZJIOs20Loy2btPXIYSnZrxq3jwHgMaZ0UkC6cWmsRQobCsnOh9d4xGmhLNZ830LaoY5Ojh1L1iPzHSqEs8FO-ZnU5KNL0_L1D-QrTOvEE9kGluWSQw4wmTDVAkuiKB888buxAG_Ee5ZYsh93nKUQiu1pFQrm24NBGi5o5OuAgiDP_cuZKscByUmdmIyh-vl-evuAE5n0r4Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuwLkGGoBju2Vk5-DS392rsqLQhPpVTvIRvrF8er32gNmd3WTWNCBUD3gHbSDhXiAhERNDieDYMU_Ly3vxf9_HTDNxJhSQNdwjhp__COAwrQdPEysXuUwP-jV9lnPcOKu44slNh9UIio3ZCXqfadoPMsv4pAN-74Zq_y5O4BzqrkAj_kU0d8Bk0uxXyR-F6VqS5dWZ4oNcDTTvjD_aO-u8tMSJVVLGywEMukiCEp_0HHH_ISl7FJ6QSe5i1QtEuq_osDkVlH0eBPg9vAvjqwfd2VXlpb3Mnx75CzE8_m2sdyoOPL3uovrHAqWGwzU4Mx_Q5nCZYGPbYbllj4iBl_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJ6-muhM92UdjhDEzhWZjk5Wc9kEyGFTfbzXWSVxZEavD-6ycZs9OKG3Dm_b2h8qamR0S4o8AZTF9jptG_8_XCaTSDK1UCFsn08i3MeMsCSxlLMdSQMIbP4B2FaKLJYB8oK1XPBLfdx5nPbLATmunbhYsUxil2LiYe3LPESBnbhWLbQU8nCo3Fa4-KeFR1RBTwDMgL_qP8Sgglwx_Rc1gpnvjsYamhEPsezHow1QuryhacnDwRn4779RHH8UGRalruVLDkVBUbKvhVgSvggcjJXqujNTbcAqZvmOPuGILjNFlpyEapkvGPqZMYYq1H1oFuC5MVOJ0u2nuP62_a17Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-sukiHj8QtkSGf-BH3D_iDMHnqgGWyzoicdtxRCuYCevyKrnSn2d7w7npIGLXdE5nWyYsSLcNIhfjH4tg0SYCe810wtkqvF8n1PQIlSzCdEY8vo3r-pBkD-gm5njGNjEusBWBLIVg2hY0J0OrPH4_Uns8ev8UMd0LAPMK8AVGLzsD4ctSkalRGZ0PGDiC4nmLLkAgViTzR8-KVVNmzD541oWXap5V8stA_-1MlKP4Q3MQfQs3ULox95AAc9HKgHV_gbv6YOJOFuVW66ptIwfpQBFWkTT17XLMBI78AhN5W5NVDAOIhqWsebyvXHNakKp2fQVRroqPP1q38NtfZBGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7V35LzIviiwRK-h8Z1z0-gBdBy-f9HUZCGGK6KHq94uKO3s5nJrRIgHStZs69jtLTYlevn9ONbQS1eFQerwbEUYFG4rCzv9QxejggGfDiPrTm-MVnLiGRzj_zUqmGHwT5L0OfuDWvdZbeGTxsMF9ghrtpiD8RyHGrfEPB4zHmvn2JAmW6TzWwFEQE_soNB7MddQmSOYK3oFES35Xzl4kfoArxwbX6HkIW26N73e602euXUDO8UDcjEedcTK6mLl24JFwtOQlNkfBSIx_MPxKy3mD29dRNPrGh43UfX_OTJguDWsmak6ESQAHD7B99o8RR4oMePLO7eM27YJZuAJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmG9_D4KwnQMT18tYbxnAK-HpzwyvT-nwqzW7oztm857cJabWioDY5Z_mdjp5VJoaPClF6htzgawHHjOqwnKkeXXHFi5IbxbX1fT5iY3nGWzxfwqNQjlCxy9jtjtQXZb6CMWuylxFAM1y2mLlSSwILgCt_DffMYReGhh2zotCpwHuAAecZukh9_iYBMj6z_hTdTxN7sJ3A8EAqrEZm7yEyv5_4dNjsKg7HvCvk_sFud4pil77kk6TN3KJT2V0nNmdYGIqYuINdCEzjOeJKHQipYZ2s4jSEWeZE1W7r7J18lEGQIO5gm2V_jrzJww_OohlbnvAn0QmAoa8eVxUGVhdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgDbHjoCtQC9VZX7Rq-r2EZUFNqytJNZY7ZQDGPEK4f2TjhLXEM0EcehnXVmB6AYAFlUav9X953PDQqk88GVgWxS3zJb8vHmzriLqlkvqFADVfC70PwNZP1LTvDcrs-iKKdW5TcP0EMm1d2d_5i8_W2l3UrkRL4Ihk14d5woOr5bj9mBCPTjEeDQQXjVTcDPy3mMlSWDaN_uag52G0hAK1dUJ8x-dvWlIa6qqcqRMs3bqBX2rpZT8-uTzY1RHID2SwtZvFwX66jE3egFglGw2P6mQVAPzijLSo0i6FKjJgH8jPbR3oAhScYPKrBB27W2sOYmUiVET-kd6xRxlkl8rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgEF7Mip61TQ8bEc4b2EuRXzLH46_YD0iCec8g4CAR-gC-HcLJD7TQr259u52GXvdmzGfyD-L30qhXBX5NFhPETzOS4zbbtay82WILTS5Kdtcbl9cssySIIgXhElvL1lY6HQQxndujDROsn328_aMB9RloUfe1t3BqLHQevqr73hd7_JOi-qN86JJHryay3_TKNgbPwdTotizbHitqLOa77HG5XGXUz4CPTUWqQKjD3QNmpn3jog52nbmphVWjzIcgMe84AWmsx_73vSA3_1i2XTp_Q4G0M2nS6vZxgfmDSLVIw8f0xbUsMZyPvYWQOO-S4L6CS6ZTpQtPQJv8JAgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCf6naK5vMuDD-8cIOM1e9Rlk6x-eHSNGWTNTQZc0YxYRA05dO1Zb97FiV3RTD-9XTtl4I3SY634zEnc8PACjI6CXiIr-Cp7P6n0wo9U7XQPm_VAxIY2UNp8CF7VR4gMikEx1B7NTIpldWy61pbp0-tx0_ox3toSrPXX8TUqSPuTTOtsMzA_Y1G9SYiiCYElQPr00239lA0LZN6Cz-lH1svzAF_hUj0P9KqSlX5zXw3J19nJ-oEeEDbjtgIfkS2oXmvnIFVwfkNTpFUTFb2fXRfCiKDBegWD7Me7Edk8Ovq4MmCHoqhh3fCPuA4O6WI9028qc5PKNLv1cd1ArSrzmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugX29Vv5d7cS4HhKCATyZtfTi_sCueK5v3DJNm3bOdMk8a23XyTjTy3gcaroDMxfE90Xv6mG7iGdsa0-al8M4pGrdb_GcU8CzvD1sPlCbDfFsa8LPEf9qbkRclqiGxt4tZsKAB2Rq6alhbCs4PjuRqHJ5ER0wxgwMiJ-NvR2_6P3qaT8oArfZAtHuIMGjN2RrJX-PTjjAqlwy74phhD2l2vfU1mwIGrhr6moMLAU6yCpvSITAPcymkHN7fefKj5TQ67rKKMrnFazEevsPMjrAVzL_cYO8C3a0mXBdvAjLuHY7iY0CNA22BaJH7lEQvLNaz5wghJkowmmoB4nJXGqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbrFQeSg3Em63w0EFKqmjwHjJFrEuH7Q0yLwRj0inRPc0c2efD0VIvPPHlALfjNwUEh2Szu64FAWGMLVffPW1K6XzDisQqLzilUAOi25pW42Emg2WaVEa-39OE7PvsfD2HttTwKR3Ivdwh6tbkmPzEA33u75FtfeYfVLqU_NbYgpfj9ztU5LPNM5gHL-ZP07ODJoyvVhsoTjDy2tSgMeyVw6JM-v9isFQk-YdsLf5gK6AJtgfkjwo6dEZ6XGqAwObK86AjlVolKw4t1QZi39vugY10FQcRgvqyxTiA5EgP2jTrEE3TtH6EgKY83CIKbWsKU5e5gbuyEflL89BGmh3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW6Zd_Hsmp7jljm5ECW10JxlVDVo1ary2YdNa31FkrbKHEltDvYlM85FTzN5PUiTBhPW7-njp0ykR5BwmwFpjdm9upwQJqLO69CpkLi7cD_VJD0N3CHMuNR0R3xIQTgbsgHICiVen7pO9Bp8IzFsUwgVPcfJy4D8VTcQoJgM6xS-k4FsQJT4BFy5xgeiGzdMcYXm5kEKiIw606FX81IxeVzaXpYH6deKRokunNK_qSBhOpENta3OqoEbOTR3wFmODWNJ8JzIqZfvH3p1C33JOiZFTFxv_NKdfxowjmiTB8W_LSDwePh4BJsu7vQCp9ucZ1XCJ0umPuo13meFTCDwIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwtRxuJW_M1a6K-HMx_txdgpsnZI_-d81jp6G4Hv6ivD44560AHkaiXN-DVo1dFTisX2Fik5cIoLqv3nNHXzZQRafLNqy7kQjxSDQEty97wZOEyRymaYLAHmmy5S0j4yCFstALwq9tk_yvQarR98zCWuNAEHxV3by_nM3b5KeRBk4906Zky8mIFzCzQT3k_Y6bc-_kSmev9uOU-7KF9bG5dggcZAs4Fiz3OHzpxPuyuBs42IqMoJ7kouDOLiCX_Jod4zt5s1S4JSrXqMQ6H2_V-4LcDmBDmWEjlwFrov8Tl8pkrPqY-mqCOz8qrDUUvURGMabicqg3yHNHZeUS62fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOWax-d1pYJngxUVJ2wGp3Wz5idjTbXyw7r1c47-kCkANl4nCuNz9bCufRDy_Si6s7d_ohi8AsuKcChKEGNlOun-KcZwyiCJMNKgRx_xnN3DVbsxVFH5Gajf7T4Fxd8Lj4zGSL9Nm3jgacMvNgcv3d-U8p5bl19ccXBIVCihW0K1pRLAfOy5OpGThz0NlLYPi4ijPX2mn42D3pqtDOuWHcN_zFvbcKQA5JGFtScussd1qj-j6mrcMijsgF0p6TFY8WSx8WQEBFlepc-NWl890X4kYEF3J3kr6Scx59taYFDrMBg0kOTB4gb3kaNF1tVs0PkaoTov9Nmwlowp00pdUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcRHy_La299sEHev7Xw-KSt6v2U0s983WiQA1BHfO5zzuNcguVgZXmUNyVRtQ_DI0_R55lC-KxfGR-hx_PgNpA5o4vxhBLOL3dMYaUo9xLgbTwrHhlTv0wvJfa0exro9KHPud7ejjGf5bj6nt9eWTKDEepXkJmgm9aW3uq0Op8o8xr3wyFH9Pvs_-sYbMkm_9XXtwL4mCMYA28xkZsE436bFNpTaPylUjP4iDp2H34UC5LK_uuE_gdT0HMf_sSZhm0f6CsrePgNExFQL4HSsU55TQzUG5SIRZhmMuhUB8oUQVE6KI4DJQofkJbXiZSK3k5jHTHqum2TdEGC6aqEVBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=TqBZBlRo26qSY32F1WBD2E2Glec5fuDc0onP8YXa2prlyM6sBVRu-yQfCPP_e0lqwi8rBtdLk-2peJoItuGsSyxC-FWXoV89EpWGMEuwepqCV4zm74smkbfJls0GylZr_Z-Yr7uyWKx3p42W6bZIMDJr-89prcxr19Z35UorJzPa-X0dPs3LU21zr8CHFVDocccGM9TnnFmLpmyur57F3Wh85qS7M4TqzlnAEkF4CmgCHPKX2b-iT5NkidNm-6UiNLIqkEorfNe-VJ3bUeR5pPfQZU0dGWEUH5DoGAc8QJGQu21InxFlpHFNkZB2BkcR36w5Oi6TgOM_o9-jzae8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=TqBZBlRo26qSY32F1WBD2E2Glec5fuDc0onP8YXa2prlyM6sBVRu-yQfCPP_e0lqwi8rBtdLk-2peJoItuGsSyxC-FWXoV89EpWGMEuwepqCV4zm74smkbfJls0GylZr_Z-Yr7uyWKx3p42W6bZIMDJr-89prcxr19Z35UorJzPa-X0dPs3LU21zr8CHFVDocccGM9TnnFmLpmyur57F3Wh85qS7M4TqzlnAEkF4CmgCHPKX2b-iT5NkidNm-6UiNLIqkEorfNe-VJ3bUeR5pPfQZU0dGWEUH5DoGAc8QJGQu21InxFlpHFNkZB2BkcR36w5Oi6TgOM_o9-jzae8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDw39iFUNj1Ptc7VT23EClK2rFUfzGar7xanbGSsHHjfM6eMxnCa1XAfRDT26uzyhkIfJJhl9qeXr9uNuARpEKSw1zwA5DdX3ehMHRzQWDczJ69J8lKf_XcXbPRwdMOFHBPClNKmVVnaePGOKYhacXDlcAvebvHfWnLbpxQNfXozLMo0qq7OKkU3XPP8jQNAz2IOb0ARjinKOyBxMLkJaWypfeOOE41ulmEKisRlMNZKj0kMfw96uW_X6ppNTzSzm5PXU5VfwUtQtVv-cR-gNvTstggF5wo3hbz9y9FR-qGjnlB8PtbC6g3zJnRCU_bmOEQEXqe3QLe38V1YocWj-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqHZtDB4blZvXCAE_r4xyi-air_SO4IZ3nucYqmkMtRJVigAAE1aAY_FxJPaVPPdbD8Pj7ksh_YmneFTxwTUEtDmWe56twhW2jKP-e1o0BUbAiHCOx8_YMjUP2TnE7XpzijczgySftM2AJ9C2xa6VLQrfAtgDWjkt_z2sLU1U19XPMG5NM-e0qTRyD_5XZaCgtgWD_YMY0f8Qw6hocu878O5Bc4mlDvMS-qxtsYCVtJtnORXlxvX-9s_5H48ZDBsL07VSFc913oOt4buwYxX8qv8QQbqYeHeCTuO1pyo095a4m-7bInlQ2TMOtlcr2DvMc3oaRrgcs5ZIrynUWEY2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDP-kj1ilvh0PE3MKPPm1YzxBcfb0uoWBuxxja9a9x3ZkkUvL9_NC4Ki063_a9s_SvYrHqel5Ek0HiSr90kA5UGRaHwkFVyx8KLkPplk6b4iz19JIg813noA2msRvUuPJgvT27xyctxqDLl1KTb0KAbOP6yF5a5ugNw_wGrCAozJUW9iR40GXy7XIZckUeotMqutYazW0iz8qET1qgTbaeAxN4pIq8W97H5QyfTdBRn1vqCNdZpvsQ_Pd2hLUWPko7q7GxAFa8Ue-Ffvsxa2JcSop3nctB7BK5vcf18-8MPF4_xAn6GPA9xNv91vEcm8aXHCr02Ae5-J-vihMC9axQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0pL7ThMbmG7V0K65GW5D8bNBmxEAKyYprtETC2eTJaJ_GOv3gOeeX0F5zd3Z03iVV-yYJLIuA-pqhYzdbqQKrA1wrb6lxQsQhuZLVLHKc4THNGtJvWYWa1VJwtkiS77ro8k0nPxreWHTuzQJB2SxSwWDcamsUI0zkNEsL3-jhhuzNq9Lb7rO7p_PpLemKapnzLvcbnEja_SQ6WJjfxT7wsIl05duJ-74DpoU7LIo1tEYJ-_Tswr_CQWjirdcRouwZvRDlAlhQeq2BO6G4X7KQbgxKAQwlNcVglb0uXv3F3hRAwvXaq_Ge7bhdXjA4aKf1oIlNXLSPuz5EKws6yFtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R58dM_7NTjN1wKRqglY7l7bhamGS_Yc3K64ws8Iy93yHIQ2gZM05I5zCFRZd3wWRNtHb31-jHPc4HcPsTCAeQmbNeYDYUZsbnANTSLGb7gAegZF4rb6deQNKx2Um7jTQ8eHTTWuh2esat_0UfzlITiissBX9pc_KbyvwQYt18meCRBrNtT-OqdxBobeeJXdOFcfwcsMsgoMrZ_KxDp-zZyGjx9c48Qd92nveAIPqE-4hcrWYFNbW9n3LyoAwWLGhKPaYTq1oS3uYCYL2qf_QeYq1I3WTnq8DTnDVS3sJji6hypyUwXrbcHhBn0-10sQiQrJb3SbWtj3J84LrjBB2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbRLe8AykFaFxLLgwr5dRIVJ2DkYaUWk0cM3kvZaytSzYYVtqnZWI_PLxZgLdVX8baA-5I-jz3wuUZ3G34l0eDdaWvGf9zzD2Om-rfKKjWyYjamrqN--kQm91I7xn3jnhr_K4ZB2OolrIQrckcGv2anUiTjFvoAIdDarm9oQfdLQUzFugVY27I79X8WFzAf7oBVbuaMX-hf0l835M1DPZcVBAXz77JTIgnR44u3CFU0MgdZAiehb3YxAsIc6FV2_s2dFEH_jG522-2n1pkoQKwqTejtu9eZB_bwNn6FJwrsvEDmr0QbMmXjKRyITHPLqxpEyjh8FSTEIBtmZjJer5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELwSWeB4lxrjCUSHl1VwSVCIlN0viRaADj4M1PtATMF4G-WWUvqGs8qaiCDaia58QUn1hnq2ZjXIpSB1C0bd_MIsobVJnPFzVdSgaPqXxCtzrqGerfUg87MdxsUDVMdz49XjcP6XICt2qjEl75slO6QmZ8ThbQ5NAH7W2i04z8oNc211abfCinFFprujoBLS2-juRBuS4NEWSZ96C3tE7zWzW06NzdX-e1DIOsScOCgQP2I3QXfFlIA978qdi3eCVZN0h_8RzYymJll0PnsFcjrVLfqdCT9t1pRBxWiAarmakG9uj4YxPUtmje8pOdDA0VYaFer1UUiCJI4wIhlOFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=hUaAQ6vkNFjvlb0zftG-NFnaUTJe5QcP6ksQIG5n_frk8IDSZePmKYtukrHGBtdIqqfuw4YbmLVBuc9S3HAjUqav3wTbcGuqp2BzzVCxwbkOg3hZgSBdrOHV_zUAwbO1Z8X24HN4fBmaSbv9-owu6iP-Yg_E7Ki4a60qvdPsVlRGrNK5mXcrvKjKuJPCG0PqmpWY0trtzNt90DSCDnKSz0d3Ds8qa1l_bBMx4ZTF_e2A-li1Z2Rz9UCQdpKWnt9lmKF7AQjIVfi_RtNKJDXfSmKdmtyZ8jAyV2U_oQMAhpiy_R7aLzxHWrtlbd6NJtuymojor9MTjdi2kVyC5VQZ6jTY2FhOsXx3eg3BDsyay9EV-OZIlsimnMNa4de_XBrzdZFAm7bx_dZstsn9M_n1B7OlVSuBJQnKwkz7Z1w4ATS2jAGrX6DEswh0uDY5Cp-daY5lTq5r-WQkbPnRbUdS61M2gGTcDfn8n3xFqogs712iDa0jsCpt8cPdK4e8PDSpiarNRRfaGRA4lVJ5C9lH6s14gMmSOIjoIr12n3uHoJkweiwuctbbIVIvSJ56w7Hh6fRLACxoQ7NgsBYEItw3NIDTemNVPRrU6RBs5v67ZkhIR1gyo5M55OrGkwzPAQQ0wfXEy2GStyMwg4sMgssNO4eX22qI20xmddH1QUqBLAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=hUaAQ6vkNFjvlb0zftG-NFnaUTJe5QcP6ksQIG5n_frk8IDSZePmKYtukrHGBtdIqqfuw4YbmLVBuc9S3HAjUqav3wTbcGuqp2BzzVCxwbkOg3hZgSBdrOHV_zUAwbO1Z8X24HN4fBmaSbv9-owu6iP-Yg_E7Ki4a60qvdPsVlRGrNK5mXcrvKjKuJPCG0PqmpWY0trtzNt90DSCDnKSz0d3Ds8qa1l_bBMx4ZTF_e2A-li1Z2Rz9UCQdpKWnt9lmKF7AQjIVfi_RtNKJDXfSmKdmtyZ8jAyV2U_oQMAhpiy_R7aLzxHWrtlbd6NJtuymojor9MTjdi2kVyC5VQZ6jTY2FhOsXx3eg3BDsyay9EV-OZIlsimnMNa4de_XBrzdZFAm7bx_dZstsn9M_n1B7OlVSuBJQnKwkz7Z1w4ATS2jAGrX6DEswh0uDY5Cp-daY5lTq5r-WQkbPnRbUdS61M2gGTcDfn8n3xFqogs712iDa0jsCpt8cPdK4e8PDSpiarNRRfaGRA4lVJ5C9lH6s14gMmSOIjoIr12n3uHoJkweiwuctbbIVIvSJ56w7Hh6fRLACxoQ7NgsBYEItw3NIDTemNVPRrU6RBs5v67ZkhIR1gyo5M55OrGkwzPAQQ0wfXEy2GStyMwg4sMgssNO4eX22qI20xmddH1QUqBLAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cltvj1GX-zZTf8W33Zp4NVNBjj-_izQ77cK4o94k5rz2cOpy9T_O4ObX9xNobjMvWd9pJewISHjZ2Mt0_BcAsOR6nupzSE7Q-1OZxa7TDQHQuLo8GW6jPTOX9oFzOJc9869JYosW1FkU4R3BN5movgAihyZ9QEj1sZyHXEN5NnSnAjInBnV2zwUnroUiJNuXTPQNJjshfWQkdLSCm_DRjv9KllPmBmL9D4J4p7ZkuSpu2HeQ2FEIPOJJH-Kj1Z2KWQeFpJyhtRd_qojevtEeVCtoJK5Ek3VpNDXZF16orgwSXzB3-NmOPH3JnBcDC_oVB2DT9BnY-SDti8LsG5LGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKoeW6Tw43XQG1h-1LeGSoRoVaQSIsCEnm4KEBZDX_Y9OVIQe-APGx1e-bFGzuQ5Ns1pdt1m_Vcn-V_6WfuEuh-Rp6p00iq2H6hIsCpcL8Jm4JHEV16icg_I_NF4fe5RVXa9yJFsgyxVZXuegAJHliaq80L122V4nZqh7BrQZ19MpxlVwE2HA9QUgSMAEzBTwdUdaJvT0ty9bBRICPntrN0z-ILn-6IsFdE9MTAPcXzWqQW64n4dfycDDPVA9a6o4KbDiE9NBCqqdkZnjPn7vBi4EXN2t_cV1O3jAYrReu8sgA8DWKf1SDVRC3Qw5Km7oMzCMRgZng-hqh_BtYLv3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gd0zzv4P08KbX9q-eGZ_2KJ942Q_0rWkbfZaE9iL-ouE1W1GxMIcHP560LbvY3ljCCvwTaVFvU7MgXWSIBJF_T1UtziCYKGWi2KpXUBHCnZl6wewTAlRWOikIhjVlA_MVZNDBXBVcHyDxQQ-P_vnN5kiLTno4hlKV61s7z4i_hzKTkWaTfFm1AIAuxuutI8nOenzJ3CQZj3NEnLSZFz3wscc-F63tVB63RwwikBrABgfuI58Jaysvx4Pz76rCtR6zOp8m3bZ5b_1Nzkj7M8PG4iiBIkOpJ2fLPn5ZYeikjyUgEjCSH1d_Q9vbliAvR3y3GTAegDbH4R66zuGbXJAJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O80PChg9zEHBhKHbpeqOI6eoMn-03IZZVZ2vNWDaU4g0y_AMpXiS-WsQhevyLVyPmNc8XP0l6y5f-mvEQrD04c1fTHttbmnH8YlKT7Qstqa3cFfK88PO2etITeeHp66jWvbb9T3f3WpdH9LROVn2tzlBXmej4rJYOLAL0II9gjHd9HreFePheuALTsjsCLWlFTBGSSkwz-N7cF2OhOL4RbI2iYE5srxnJw4llliIZa4362FBF8ABDQ3K9Dd2ylzEsmpIbYt31MVsVSbPFwT_Qn-V_d5m-I4rMH6mSrg6GdgkE9D91AxI0ytSPj9qZdO4gX0uIxZeJluNQNZG0cqa6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnP2yfoUjWcnIUr4LiNYxpJVTqLxVkGRZevKGqW-u9zWCdUMDtxFksGSKKwSKTl4RMLuV-b55bMCJkxBdWVz7RMsybUP5RTHIeAIvGMngPc9WrTCpah5EOFc8gin6O-kk66gAs2jmrHoGXmrUepeYyXgSSMXbBJLlW9-I3tN2esQRPI1aPGGqrgw7yJXt4FHBL7zVID-CZ2eH7yUsd_BEyQq0-b4AF05GiVKVWs-Yhxhlsl18akhkSc-Z1QlJOK6v2pYF5B83CZcNP1N-npEn8bo1JNSm5bJsBrni59qkrL1vUJojKtW2jO2KFZEQk3qJmyUu68PRY2Yzqw6CiVRbw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Tp-8csw09vSTKVFiMgVCR7qWBQgweCuyPDwwpcwQK3Ez93YctcVsJQJeu0QU6AxUIIrpciBP8jTqgR2n_1utIPtUpeetrMOCMeU1RrpgOh_uE-CJyOrcro6dGvPyofTvSmLBe3vtK5_s8Son12u380qK-tWXtekozJuVHj4nCKer4RwmiCY4ua-4BGYq0GrtZvKu-dDXI-Oe-Fqm3zgPq7hWusHukYKcsrnRuUEtN4-_FL0c_FIOYu5Zwk9E0lXXflnanozGazghkZIE8YVCiDXePOLAvwchVpshEOVUJulQOiR0dU_iOp5Ysb6rJWfJj284yPh1-PtOtdRF_wmWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Tp-8csw09vSTKVFiMgVCR7qWBQgweCuyPDwwpcwQK3Ez93YctcVsJQJeu0QU6AxUIIrpciBP8jTqgR2n_1utIPtUpeetrMOCMeU1RrpgOh_uE-CJyOrcro6dGvPyofTvSmLBe3vtK5_s8Son12u380qK-tWXtekozJuVHj4nCKer4RwmiCY4ua-4BGYq0GrtZvKu-dDXI-Oe-Fqm3zgPq7hWusHukYKcsrnRuUEtN4-_FL0c_FIOYu5Zwk9E0lXXflnanozGazghkZIE8YVCiDXePOLAvwchVpshEOVUJulQOiR0dU_iOp5Ysb6rJWfJj284yPh1-PtOtdRF_wmWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxpS8ct8HnTgMacd4LBKY4fjjhA1M9VCYDx0iEdoLNvS3pulFomgIy_Yyfk_yOIaDYJlGO1CHIy3PB_adqPRf_160wJYF0RgxoATYA-pI8HNBkIDRG-zYVBLceRy4hlM3hLirK5lr4dngE-GwwjqnU3TSVRoYZKmRCYW23avuS6m7RE4NsEVcqyjj8NGsJfEzfuDZWcw6wy1VU5PPZb1n0A-bxFqoL7O_9xiG0Kz4gXz_UU_7mNSyGK5YT21d5xwUGvTMwYBuvyntUWDHF56l7FZP5tswP8FUa-hRZjqAGkaBKz6kL4ti2ZA-bdw7v-dy8cvPgwLoLiUfBn47bKhHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrHbsSsgULwlO90y2ER09hzMj-5JO9zASuccL6rkkqjqaW96ZlvXF6VgWE-vbduMn8h9jkzQ88mWapApGr3oJ-5C7LdIlEkBsmCPpxlsTcEmS0M95vneKsBDazzmKR6EO2XyqunLHpYwnu8TSiVwdG6dFjgz3eM4tQpwgjDaMvJV3x_zuEphWFKHOVwZ-9XV_Te_t0Z6CfdJVkfrwDB_e0jFHoCFykr42H7lWqql23KjJPsF-B5g0G-MEAmV539o4v1FdYpfeOA70d-KKv3b9kmY0ZRQMPGbl7IYnVLrltyiMHH_AwvVVeGoL3J6Nxxz4-lwXXU7We6puNgBGZl82A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDeE2JAngJMMkLvQwynwiAl_8VwzB6ETDbcF6IGP1W1tjk30al9TGNaY8R-Z8S4i7Iw6mypDVqLrMeds9Obl7-RA6Gm2geI2e0J_ddxzqVNMsMsvgK4kf94kXzY23YBnAjO5aIczNhQhIoazRMucNNH9C3hQCPWt-qcYaM12TWeDZsJ6-vxNk4wFDbXv6PCXxugU4RI4g9i5SJG5Or8agQqATSHxlx0WjNKhu-LwgK_WNii_VQhW3zycvp27XFiVcbaWf5GUS-7wtahUGfdkH9VbdVk_Hp37pUFoiGJJSMzYi6MWDSm6qLAuAuCd_iezUUU_3JO1lOt6tbE_iJHTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvXhwa35Ug1fRFFa06ccDKJqmKrgmvHNM5dObePYOXm30kbfK6zxgqT2PPBW1WVZGuPAlBy_2wRUD5PqLR3TgOHuI-IPb1gwMb1pAOZMA6x8l8x9W0y_lB3W2CllxECBJ9DWRfDB8nRxX3VBWDiROvJPkNNQPMgyyXlMcETTi6NJAYs4PGYXxm8c6oeb2sEEIwcOIFEBiRt36bjkaiJGay_FuQeNvgXf5JvN5vk_lkp-c2tkN5j97lC5LvwOssQf4TS0liskSWL56ZS-lA_nkSPhEYJip8Sys4mKWsG8f9CDU-YklcTx6nU-9LjPw77VWCFpZZi73eErMbMvd-C4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQEIInsmp59PDPkjlIikXHN4_mX_zxc68flh4e9fP3a-GpawSeWwY7s49AK9pTQ_AjlC5C8AVX4Z1QoWy-s5KQKxVXIk8M-PAV-Rb4rngnuJpZp0WFnQyM3Z7_tsMvduvpn2FAXz3PnA4sj8jAUFodycrGZWQX1t0PEm6xuDdWW4jaUGJs6OvPXHL9ZJ-FFPEq_F-PpOEzxgCoQzVnoG93qw12q6P5zm6eG_GEDZdhMHttFBHr7GHwgElcDySnS2KOnCNFaJFPOQxtYWKWrNItEEEv-0kHDQMImrDMn9uZd-ReHFGS9dYoXK8DTYL21cZ5v6J_Opk6LelK6gmpV8Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl88gKFoELtBSr05R5zvqVo8ZNpfzRTzyfwHJrYaZFE4_CISe7atFQk-D4v0qpDVqzBxw6Krg3D4qYrJXpdrqzUoNgvsWbo5I0QiRCFkSPr_rjll8C6GCVFmD8-6asr9i9-psEzupzf8D48IHNZtbIIW4wwJAKJlILLC68iL05xUnOm35BsXA3spaC4A7kEgAsz8sY-PT65k99cgzEPD7BVRFpWTCem4pAEA2CUG1F59HKnmWJvZ19l8qLvfVDJJlwv3wfkGXqH_bk8N3WUEW3dVboUM6XcLQVd4XNaWgBez7Fz95XdOnv--P_-SSwWoO8epsKmRvHjb74bq8WZ2bA.jpg" alt="photo" loading="lazy"/></div>
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
