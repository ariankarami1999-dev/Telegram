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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
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
<div class="tg-footer">👁️ 240 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 485 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdzQF5CQH9l7hUdcaFXQ3dJtzLRQIzMTUw_jhp54PSYKhse6NYhbPsq3B-PXd7UHEpXC6fOKbROiGzSvpxmieRHUw3eX2qlbsxDwtReUV7Ut1HZq9R7KiyTZWQUSf3xTN4CTfO3ArJ2SyTDidVu36aAxnKU3N2TDhLJW_UtCYsp-tXAjJ7TXGix_vVO2HwMM4q6uBEhl7iucoZEFZ4c75Zzl-3mwTV-Ty3N-xFokbmaUZ4tbFyaUtGApoob7cRcxzy6jQl0sS8jYmjpUwLisn6r9apnxBY4jxImfGTR_EdpltauFYiwP7lqgFBOYCNpbR-XeROKX52TFnirKMH0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLljWbe99BguWC0tpiXOGIHfQr0kqp3xZQeHZgKcQi_ncSfen-nbvgFzVXdyH9lYkvRCkiNgEOHiZh-HbXA3f0ul3P9tn3LIHJZGyym-T-Ch-8GdOctVyYa1tzgY4kxD1QkVrB7j6-np6jPby1JkrD3vkMiB0BLGB3Pzr2plTkAvK4piy9xRb5EnZRnfKbE64KcjNFCmeMqir2COQVQcGHKZJ-Z9hkNoXi2aOwqCd36YzTAWSpw4IBJ28DhEYMGQvf9KAl_zlqQBavNFAANqcZA2ZrussRK--LPsXXSCHFNTe062a_1H0kBj6es8YUyIeRt70cJPz5QMXwKbN399Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GfpztfjPklk34vqnl4nxUzT3Y8UPAi6byC09exlgdpump8S91qWaikoNBFfuuWvWIcSJ9j_69u69uZTcGiLS9eDkLZOzSi7bOsIy151BQjhQKWtKZZAZ8e2L93qEDO4_0jYjwFijWHjrfZkTrH8KYQDf5EI_NHlukJXzJRs7LgIxj1egUBQBd9kBEikO3Vxw-CKeOQtj6O_l6M_HU6DUXEVg2xXmi2VOwB1uxns09bWZlNjrRzCv8cUk5aMGEX5DyPB-zKPcA7UP4TIBXGlVGuihqjdJV2uFAUAQilWUURsJsdUYkecvmwxhw0nLaU8nnjHXySGYckGBZ5ed1n8YJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMyMbCT0de6zLrXoDvVNitEZl2KeVXyR7XD5DaLM-F0rgk1crWMIRCdYnzrUTleDCt5AaX5BImwaEwo-4O3yI7pGDhKObNwowbnQUZfXAyM-cdO0YFE5BrLiLVQxLpwE--4Zzk0BdprOtRFNjJf7mdGaU7pDuGOI6SEifxZMNY5dROLI_B5s8-zh7eXfFH5ghIsBJW9L4gwPAcsqJ81IVDJCWcwJ8iIgj54t0Kda8fvhh1uqm4lLYoOJiagopj-H4FoBRM93e5rINQyvo8Mko3BnICc87GA1JcfEVevx0EaglA0-HFpvzOfW3lrPAmpK0WB0zM59brk7P0sN0DJDPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrTLj9Q-RtjzhpCzQMLeF_P_uekxLRIYHsUT9zHoxo17ALO3cJeekiHy7cOzEP5N3edUofQkXprOJ934BHnNbSkAL49srMQqmjRG_09swnoGB4Dn7ZSwrh1lqMLjvPNvxp7rvbrI5TxdvVHXSgE_InxN2xfqbutShMQpkLg8pWfTbKTBl0-8mZEKEgmcZz4Enc4nsXr6ni-rGMyKUunO1TmkrkHisCSx2r_tHoTCxmHQfsXY2HeVDmb96jx_j4Z25azhvX00rqOQPZIqqy27ptshn0Bbz33bcvdnnD9Xwum8Ztp_lbDsGf7ABxhBfoD9jVm-AMzG_ox4PMOc46n6vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6UU1h5dun87JPaHP95avAuJ0qA6fw9WT78AA1tC-d2yfSNRWdjQ4nOYs11XBt2CCOA2DB5EgJfFcH1N-rUP_MHqliJQVPHbrkBlLbsytlvxA7zpUWNqZ-GNIZJbFQnayXW3J4hMzBhns_JloUF_sNiyr6SaZ_4qROZrzhKu-Jc1yYP8anjfbxzKBkabOqk2OdxxjIPGNuR9t100IRL3rR4AI4djdcZDSuWItT7OfPexJ3q53c9buU5BX1VVqNY5G2GzpQ9scKzaFUbAhIgvjTLv3Xroa6J-dhIYkn6TUW33A3gK024Cx38cAiB81vo_W9jbyaCjxTkpOnQWmy01Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdJZmeGSc3OPbRtP8aSw22Rc5e8plxrCIgYG5FjHbzxJWKAlDcrjihUocpxSUMYcrq11jyOMNmp4Vs5qGuTmhppZakh_mD1P-n4bDMQcJ3BId4J1RbFuImqZ0GWs1xD2nrrPXqizYTUOCQuotakhbQUIWxvGf0-43qITab73OlRyQLpnfewS-rMrKsoTtNR5G1WvRCGkkSH2OvyWybGSaT15aEAk1FHhaPLtPOJGtTv8Uc-cBO34xIPewgAWv868-3khl2jdhJZQoYyd0nWP7L_MhsHxzlErLcTHHuaxX14DNipBDCxVDCC-lhBcgGSdIG9wa5aA-iMoqXg7E6AzrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-lrR36qAYP3ojw_kFL6U_wJ_xc_03BSaGrbDzl8bSyCfd_eO0Bu3iHFPWiWdsduR8MsSBNv0mpCKUT1sWnhxNQaY1gx4Hxq11pKNYjNlwOqxUtrbaEqXCX8BOlfpK04q_8ZFQ0Ir45Yv_6aYYZiDaD5B8i3ZBsepgTORLDTRTlKsZIJRnYVY54XDXh1CiLZ428fKxbey9zxx9AMYNXc2fEdysI_9u5Fe3BxLjvleuTjiQ90wAZ_0jCw7HodBd2uF0oylwW7VbsfSfADLoB-QmCZay0orCc61pjExfwOC2WsHgvQxYVfBU5cCp1hOTbhrw-fw6daHnFtT3Q8AeYxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVEi8EjCvTYQmboo7R-zEhQy46XDIQgf7Pep5fFJBvKgQKAGk6mFFjYm3vMaCCqrRTBEW8O-xdrYX4WULNCrpSeR6sRSLCpEDD9u-zFetcG__2pBBgr0OtqrVlrrQyyhgzkmAj5idlMDUK-JcUxS_mpb0H71iRAnTkPkwLMiwEctdFpgpwJaBg0AQ-kFOJv2RIUCRXg-f2tQSqD1-cbgRSBH1Yiau01kTZcmmWpweF8t6bnucfsKEEE4Oti-ODfXpJ9t2ukJgL45uGtuTt1NdOYPNV9v_v4yegGg7hq5xmkKLmffUbX9i-NgO37e8ca-SPMb4scjgfL9weZ_9LWnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC6RnLQEMJLotYbf5-EyMQCDG5XFw4jA7t3G8z-CJU1MOG7_xZBDlrXv-JHdGpGtwizUaSi6Dug_cXUHKiw7oTvDfz2rmy6bTghraaVgHW05oMw45UgYR0BqFnvfa-DgxeGhlxjyzagUiFyAtWQH4SxFoGVIeQ4tAxQ9tf0o5UUsDSlQ1hDC-2F3zIBj4IZPqoB0wWagpW_h37j_pYlDiIi_rvOu3N9GqCtRHTXORVoe09ERsB7NS91WHA7Q6GY2aL0759g25FfBZF2H2K-Aon8B3D_Yg-7IOxZvULQEYdftmLfzWgEwhGKDaEtsIXXXeqLLTaBCkKJBSMBQBMcv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivj2APAXlhuiZ6jpwEFhA5KUBfYgf9JdYu8uJjLzc0w1DxeZCn4I_m5bw3x1LW09Bdya7JPo4EPzVgHUNe2qXfq909TzcuKYsN9wfVE-Gi18g-TlbLLHntY3ZX3W1aMZJ_1vnlGnMM1sEMRKWo0ViZtDXpqZgviQNjZwe7WbKUSOLjUBl1KxaX0gxgp-EapH9qd9f55XagfxzPxPH64lTzD1YvE8QXGgkauXbE92q-OjxcK5Spoi4PABqKy5Y31C2XGpo6C2Lweo4AWeBfcoAbtqjEZq-NpIJCg9mzMupCOiRfYbwWJ-0xjVRknK2Glr3XGv6NiLIVsLjgFABFX64g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqDi6SYMuqm7cwbB6lWF3wHG46L8TifZ2jBm7qXgzLYyMOnjgE2mFSJgVhWR-8pSAyJfqg54lXE0g8nRHelOKTmTqCjn2NZCj_P7-AoXimRuerZnXKCN8okP_EQtTATCji5bS4HXyWVwOXKG-_Z9lMKXLcnalJNZ9YFnpJ2fMQSwshT8EDpiNba3q3CHdcAk4SzCXZo_VTcbSEAa7X2jWBKkomSYiyh7PAI_JDpLRxUlG6TTeY9G3fD_nJ3M86WfEMejFIuWAn6RgNu6Gea6E4TfZJhpo_3WtPeNTBU9Qf7VFPLHjWiXArX0QHHY5dm44BCWMuOFkUfz2j-k2Ilmjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=v1rwCFzN4qpNBVUjCR4nnY1m9UO438UGQYzLs8xrPrdNU3Cpv5U9PiCFJXz2J3spLSJUaaID2U-Xc-Hi0B5BKyMoPT6JkGOhhj-L7NCzGmoWjuzE-IogHxR1eTS0kPR0UQ4-qWA9cYHC8YxI1sYHd-Y7ID6bmbA95j-lo0XutwZuSi8r9V02Fgd7Y4Z2NEEnFEr9rYP7Lxcnsqc-78ymUrb_yg6VHYVFuBTzDQ7-tzCLho2ARX3P9CkAWgRNKd4XZKWVE2jWP0_tdV8iaBLdHyMk9Qe2p96DF15M7C-_7m7bsk1gQRQiFZqBaihfh7Ignpid-x8Z0s5NLeitYmdgqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=v1rwCFzN4qpNBVUjCR4nnY1m9UO438UGQYzLs8xrPrdNU3Cpv5U9PiCFJXz2J3spLSJUaaID2U-Xc-Hi0B5BKyMoPT6JkGOhhj-L7NCzGmoWjuzE-IogHxR1eTS0kPR0UQ4-qWA9cYHC8YxI1sYHd-Y7ID6bmbA95j-lo0XutwZuSi8r9V02Fgd7Y4Z2NEEnFEr9rYP7Lxcnsqc-78ymUrb_yg6VHYVFuBTzDQ7-tzCLho2ARX3P9CkAWgRNKd4XZKWVE2jWP0_tdV8iaBLdHyMk9Qe2p96DF15M7C-_7m7bsk1gQRQiFZqBaihfh7Ignpid-x8Z0s5NLeitYmdgqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWUGHCYx6fnAXGDOlTZzUnGLf4UHHqolsoJcZ26S-bzTdzwizK3Du9_oBTG3hk3jD2ZLyWPMP5SeZpM95yN0Ug8ooKTw-hWNgnfpN0-wFhESLsXf8N12oTlcf2-JRYyenEealkGSkH7h316j0LSizalOW980bYZv_pTh7kY3BAnAC-KJ4nWidzp8c428mXypojBkiv6gUIg4EuYw451840-5mBkvajTbvWwf83wxq6YCVmFSZ0Z2usCQ3AVmfFgtzh9IrYnUDtbR_mCYKeMFhZcvajY5du2FwEwnsFJ2uua_KDWiQffy9GP10m-hs_Fv9eNHC61-kJOmC5aNXiMSHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgJeSl3Qw7I64LAgrvhfzQjJQEVJLjF33YzTF7IVybKGidu-gqvQATwvlxwsAM6zwJfq4l9SUnmc_VWzw4uANWEKiDGfrAQ1cO7YzSpSapgfMaPhDpBpQgCcfcrMPEFYPwwS1KWdWON1-YzUfAxEptJgDiXosCBeOgkt_RMKvPL6VSH7f4YqMxKNSVxSA2G9cz6EJf8L8mCviDH7V5f30WBVpbB-YtuvXA0B10Mh04xMGKjfCqGHlGiXU6dLmY7JzS1tUu7j88jqY977ci6as-5DNPts7LOS7OkyZIJbH8Tq4J4O1ElfFTUFRQnTciNgTKQbVLZ5rRTNjo-OIobSrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEJHIDbnsEKnq9NoCKF0cKk7k9uLfdyLTTyhjY9T6_8Sto8HwrVWlOFxs05E3CirFZ_3HSd1Vo2apMA9h0ZCn2BltRCr6yUJHExAze_2sltzyxc98_sPeDOTDN0yqaWgGuioLevVcrAp5JtOwpib9AEM4r6QE6BGOEMpdwmlkyHL7PsQlBRV6crK-wlCllA9-N6GbFM7z-PDGkxftB5PzRs0rEgJ7nF_1S2CeHVQfbRBbA5VrZbAX7ZNsGFcR0w5b2Oe8pg_1LEfUbWYCzICEUJyhu0fi_UNe-o6gCvtYsm7lNNnSIDltTB3Zsa7YbXP4NF3034f-65PaMoLqIVNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HB8WoCe67vIOVv7r_YpXPY7CRC2Pqft0liHBdMpQMD9teuvafHfPFkCdQUjq9fFCIFZWlxRKBfexlAVvPV327yOdyC7OwecNK30yzwd46zFfCYh1M8AtR9CdEJ-BonCukNnWUqHIOyT94vErjRngKZ6l7drjfx14cs5aqO4wyjQyuwO4tjCv0Gy3q5aRHpGCkPVWephc9d-Pr9Y8fwFHyRbhP6mZAnw7L-WnH3fkufraepvasMcPTafJGEAfb9r57I0_9W257BvdRgTnRCOEUi6v7MvMDb0DRWLggbUK4tktiwP1QYwUiTf3CqJjMmFMm5NbBApzkXwGNciUVDi0qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI4osgL-ePcNWwvTbzBDoVERGwGz1QvG7bZ-lu7YmxVD2Ds5_EqTWvp4nCtL99MFWetHU74C1mWMelm7-jxYARjxK4h_67FOn2SX-5pvDKydnaY7BCEKxCih5umFxnYaDnvVhgiPUHpgXR_4fMrEIytqpqWn9lfQnTuSXINsvCVmT5V3Y_o2AB5f-66V7hEV8MLit16mTpoR5gcyZ67yBLMcQ8nPbJQX8pco4oB3Aq7cQvN1kz3oxdey8ZRTlx6l4NGhnKyMcTWjt4DvhEIyJ8riQu9kIuY3vOc7emAqZF2OYWStnWl8FQsb23CNAkmFc7Ey6EVhUsi99MgrrFsXvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmVLjvA1W53c9zKBHPy33Y7bS3y88ejJmKS_EBiMPxuXarY07RpATaT-GCf77qq1DLj1dgZdQS405LV1K2glqS9fNqPBtp2MezBbYKiG-ZMcvDzSA5FpcDiUgdp5fEFAKk6Erktsknp19OR0rGrltRp0_DWJPT5_yb1oqWqbsxBZLSIwhKxbLwmKrk0nW3dldCT666Ux9rXywXI0vuc4LPNet4Rfn48qRqG70aC7F9Ol8VX2omgX5eUbmhoo37RYZnBKQSsT3CvbWciDFRjCj0peZGpYD3JPTx6s5FsjOixNkScTeShXpYo1lHM776U-yIQrJjuCUv-4uN3VWjxPFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQWWt7I33hBGujpBC3hQBw5YjV8jKRng4C0ZuaHLdPx3_VVSRfgdQ3Ncj-01Qo-QDAqc0dPaQXFMH9jE4mEQhbNA-dAzsmTk2F6BSiUhvB0kK5gBQ2eHLbPLU9kxqWX0tQyPqgYXovcaikrrPeZ7ZJX2AXcmQBYijgDvLfa2ngwyZ5AmC-gBe4epmJbbv-9r_QsbYrqpCOOzeXKJ5jBlTjQiL-JzERaNJRD6sHsQPLT8QvYSLq088Sb7VWP9JC56nMipLWoKiPROji7fH-ACmE5JjYdNg2iLt24P7RjJFdTaAK0O8hLkgekQKvJ87793pz7Tky0JPHIeHPzNLz8syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBoChFznGRbGvqGWyE4UNvDd7QpYwYQQVEiVfJ0A1Gt0n5Y8Xr_xaC3B6Yihs3fEP2dgPv2yEO6K2NafTR_nBhrZqSYLlrzTmUBhzk38lvh6LUwCUK_vHGo8IWW1t-5QpiHtQ-x9YT7FMBvBtZHZbZ6iW7HAfnS3Hb-n8AGrDpSZFrJFBHVInlf6-id-aF37wJ6nnoMmptwQoVcewKJjEWQgyQym5Cmr1DeDVc4FxAxVCIqvgZV2P5ZAnuY0jtbg-LkWyk40o1pS3qrZtP8nEKxJAHIi6KsjsvETq3m5t-qyfed0wee87KPbaewEfaP2aLmMunuJJahLvC_8MT8p0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G84kUP9ZZ93Zh-hQeBu63iY9_YPMjB93NyaZ1ZSK48lOQczv6jGJebu9E95mWy6IRd-F2PbuN5lneRIlQFMpTpbdte5W3Juq-qYld59J_biAanB_P9Df3jF4u6Q9fwClXx08a7d0h3HWDCLj3yeBkqraZBH7AjhbZ2-ctQY8KD43bMTjymUssmc_o4r9DBfrRNrFNHULVfNiekeAhmpWlb1T8remFiSIFMDtIWPa2HYEI9gb38pD0PNeDrPEeGpjdZSZcxlxHhAeGUXik24-JGhphL6hdHBsKfYhCfsDIXzhPJFiBtXrcsgaaftMBR5JYJep6qIqXBmzOFanPEEsSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTdSqw73Xg5CFxz3FAzFoPwfNk0dCZyoTH2_t6DUQKwKlrm99Wttj0t_2S9wceG08SUiSuCz73ZSwJrkfLNiJ7u7ZJ7F0Y4Cj8oyg43j5YLA9MlyWUnhkK08Ve5LzAz_Q28iBjbcZWG9EJXAb1G7eLzW9AP_r6BVl9uSHpXICrsU7jaNRIoTIvYc4fegM1wndpMmZ5ii3PKKeo-894M724sRJBC1KfzOmdWSnsPi2Hqnh6QWlxK_vmefHr5G71b2R_97y3oyGtuTr5EDAnUYjspbqC4he_veStaaOyhSjnKI__qCW-h9Zwk-FyhS8EgpJUiEaM4zcVdAhXG3swu_2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umid6Yud01lDyhudC3o5HrRD-TXEo5Ve9fvXRQ-OIEfLQvfaHKPswiAKqPswLWjYQmnJo_W5gaeVmAZ8Q5TkOE9xIq6-ZChpok3FvaIrhrPoKRL_cShpyfB7UIqwiETg1n2N4rMfjhYDq-eS7i8bTTWbLeJBDuAHc4wGjr5r9ivTAJuL08pcJ_dXuaO8ARkfX3jIZhogdzmZ_gVmD7dTCjVj7XGblFM6jCn6BhYuM3sk0c1ICRhmiODick7hwlYJZeeHjJFiAosx8MU7KdNd3nMTDZGX088u39uITKBxe5SKhPGXqvyR0UFA9I6uJhjK9Z3FI_RMIWJb4X6Pz3LkEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRwLeKEhKl6WDBuNfIGhxFrc7FF9C4EdZXgqxhaONS0DOdA8L2lf9bfn-SqXu9kLNSHgJZO3VHyYF8ZGnXxvJF0e-i74LMo0NdcoYc2kXGdv3Jt632Prmvm3b_8Lz0Q3WsmkAwvkFS10ABbpitt-8D2eG08ofoMIJPWiXMWD0VejCi8ms4eizESqAsGf_Iys4YTXsG_D4soiDKprRe6D0zEZDK8Xo4iTmTQDO_lpToKc2BjjBCo6Y9T5PZBzj_ip9_4i0mxC2hKezB_Y0j78g_wZRmQFfleazwm0x_qr37v_Xw-gDarQtG6H1jkEBLGM5eVW57INC4B5K_CAmK56yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgPd1nWpDkvDTa556y5IoKFmzwhO4TAAyIrj0V4kE0jvzuoGIWTf_tfhFcm7dXzQ4Wgm66YYJS229jUyFDn0mjyk0hAMpmVwH7nhEiA1cC211V7SdcwCGjM0WzimqphynZrhVbMe2nAQKiFCRM1OnoYxkKjPPOq11ObCZkWH5R0jb7i25fE5Eg5JGriZQqieVhUL-XoNX0QzLwfWek0kFtI6djpNkOvKz7MxWP5adfvrh2g3WNm1F6SxeVtsjD_cHqJOMODaFLm1rHVgxdGAyw49eAYfOAUQRjJm71xLYGnGJjuMd-PVsHlRqDS4Qm-wOnavwGlMg_26Q9zZsmaGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wA2b5WWB9WPWOA0_iqwklNL_YT8-yamRDgJZaIny-JJc5DTIJQ578NuBsaWo4fWYOifvjVybcEww4VoUBKS3E10OWn-6MAknGZKqvjW5_pBTVl9OtIq4NT5nbjm0Ix3Bo1qTGwK3vCdmgu7ok4_fvRbxwkIWWWNZeXoq97NJlR_FLQ8mDpw2zj9a5l9HqIf8C7KL5cez8zPYFNEZ6OQ2KMUTispaPelsYurWmerOT7kOELgWhRyOekvEo2irv6YMtR7bYrqvc2bxFsOoVUbWTLtNff6oU8zK70hlYBOlXLUKwVPa-rdUjb8wLTcwagQZusJBbEkUK1ZMQzJNfgVsFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9aqwsLgZKwsFV8dHdtEnR5OLWcRzkW6NPJd1mjFN-fCcgEuE9Zop3D95vtlI_t50UVYmAxUTjjXR_TIhWSEsnVkh2YpquBrS-350LadNGCasqUGWuH75DpWlrUsyqRHKzNdceAXXaARSDSirYIkFKd_n1bDrQ1EfoVTKEbqVtY9Jr5Mbv8J3AgC4NaBbejIfrqaRjYYDz5GbxntiLbFgEvuK06htVIZpSjSmdEvNjf8h0uvM0-BWwbnLxi5S9NK3mb4_lZjRquDhpcBK0qwTSvwdgvuchpM0zgXVtQ5De05MTurTfSri6-wfqwLHrW8qnGbO1Q4z0UFImEHp274IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP_8MABFQFa7yabHoIlXlxpOo1qLYcFi28kbAB-nNomLBOERZz-ZRAFmwcpZWFxC3KIK3UeTILF85AeJgsAIYYK_b7Vvlt3KKD_06aoNOvKuh6KrprVtpuJhc0pqwcnpQAGX0X9VeZ3Fmpdz9M-gcLEi7hVMiIMVGtqagpkdyU3B5i_8Erhb8Od-LDS9Kpndcyz3MLyBw3ui10EfGaFCXIvmNGazvWVSBifhlkg0d8Lf62XmdxOOjJzM_pi3Hr_mHJn5QkfTnwA4Stv119waf8AhYsi2l28nfks0lZ80XP7BoIMXXkZKLgB0kV_dP9p9juaJMX-OcrhN7n8FrMn95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_YpsV-JHClgDnPK8hyUp8zCKAkGEnuEgml1p5gKfeZxnZofAiKZIRoAcOXnYoxujFq9GFtwXZM7GrxfAxsH-G-io9yZU6zRVj536uHDALsccImnOuFx_tBHgc5lyzK-zaws-o__TlnVqktzchh92XDM4SopALL0mNxI2ofeeitoX2ZSclBB6FjCm9pHc87CQiqFBbvhJiLwAi3sAGCREu_spi7rirDPilzkUGFgOsm7zBF3kRhbMwDWEW3tRs5AMY38qwyO05hKtg1XTbwm6M6q-gTbKIlnoI9KMmLnMGeKzPVeFKr8nGfiI-G8wSVGaw_HaWJVNddKTFxgKS6dlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx5R2fn2RZ8qT-Tvp7cqWm0y7egRjsMmDB1ihJoMOvB6qabg5RAEm6xK-mDpIYR_xoDdmkeSjO511T6SZqPGTP1bfDxIu7DAuvmzLeJucBm5VtqQ9tGRhQL7esxoIj5pGyi_98wjs1SiJneyrBOnBDUNpTkVygdCYLGUNeAsreOkPa61q3lZxvBOpiUerTJ0On6cTKVR2BO9HrAMdRdVEj4gB6fKx0K7_GExyNQjXk5PvztM8ib3KdTSq942u5VMUe-QbEC95tHB1FHFMnHmf8SEuE_HkMAZe2lx0aSebAfKUgAGBMw-voU8a4oltjYAj-IQj-crrE-1CIPsb7soPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjagnaXxjuuxtj0dnjFjjICDtSlL_m_JDnScip4w8_yBwQjrzt003smhajOiZXlCvpBZhUH5DLvr0iN-YM2D2h_XgiCQXTqQyf5nllzRuiLTGRakKYml1cbYhNDQmbWrSIK5_ybpzNpGe7lrjSmHTQ5UcEAEBp42O7EvZD0VHh4NNOxgt7mOLVMUWIRDAX_d6HyWNCtjM1Cn3DdfW-Pmwzf_F7PZ8dne-or-Rs7ZWOvA29YPrtRSoaiuwprmEFPi4yVLOMqo9pI_rmXCySq2uqIsapci_SamUii9UTpxPsSiMwdlVF-sjYRS8jCd-NKbBpKHVrCBbiODdz3mv6cHFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcpqN7DzTAk9a7voHhNK1XgUfO5Ozl0zF4PSHwHHDCkXxZAMGmSNqY3Oz99oqS_pL5CjyT3s_c1qOPG7oy5fHpjLdZeljD3nY3U_-Hu9M5wP2i7Kqf23w3r_pIdqKS6ks4My61Uk2iyUF1qpR_NKtED7XAs-H-44jY2ZxBix3Qrn0UNbdFR11ekcyvX-nUAER5bcD7vrsHAm6hHHk4SZdOlvQNkPj7A89H6IkVem6_QSn2HR1jpwNWP5lVrkkgJPjQlNgX_OTTk4c3v9wVCNC8uuX-KqR4c57RafS7J3yUeSMxToKUQuFm4_oNN75IeEreoeZAfz_ATqF0u5vQN64Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSRnBGsj13s779gDJGnFLOigbGOPmwh_1Ly0epaM5MAhzJIww1z1iFd5Ak-5eueRnp-uulDoGMM5VXtd6HGR7rb2FMYupKqIe1jA7svtf-wLhPqsJ_9zQdW6ypzLNWv6a1-udZTlZDQLERzPIC0rGOeM87vFDaFfPsIEx_o9GSYw46QMCJOvuaL19XI_j1_2ofnh_jB9aHYQAICYazMPN3cSuD0JDQOev8WY78rcp_DeojJLQTFMzILUr7s0uNgJthPHIQ2L9RctFpXYB8E5TZkttrTW47NA084Z7z1yecGanNBQ2T_MgxYJdLyugb9jrkS3-TX-pQEr0RRI9Bdk0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViYudRYW-5jEx4Q4Ut7C7A6nqCKvTHSnZ5nblSB9KFQuOrPlz4E_2dYJV8I7cbOVcP6CcU12aFuH-ryPg_FLxr0ugKy0rv5MI4tsxnTqQEcS890u1Oasns766Ts65TwaQvWYX9z9iBFZkw7hkh-uSk8L-MujlQ8mVxEDijnXr8fXp8CKq0BmHflp6NZfCi7xdAabQfavHsAazpxiW1NL6WhkDSRRL1UoFyMNc1Izg-KPN17p0YTLgzQbGweeeLcYGlWkBnerVWSffZjH8CRtPS374zLHv6lyjWIY6Qu-VZthixSu6qN2QguJx9NLzKR-OevNNRZO0AoZAyYJJNKJRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STBYGHOKwgBfffbKiJas_v7mz2R6xrFDW15E3vSrZjc2p3_CKySFZB8zmURgmsDlsFGnfSQKaYhiReLNXPRcmM07JRv6-p9U7RXVqisTptE8yAtLjfa5gTa17SriWANie2RcQZSgZxzu_Iay0qOOVgH6X2_YK1InpZofdevTBWQz8hT56FEdrHLstPltNsWxDobHYQ8_8Ng8YaXiUKRKIC-AS-ajSAExrtPy_EepRe4WIWf_vpjW90D1JmbePuBpU894KQL804WIFvvX6dGPpLj--xChdvwekjp0uAyoAxYzm2LdrrkSOSqIU0PbWiMomyMlydVEwaWPIR7a2iVtMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwwmUasNxZAWkDNBjvdieadoxyyPnKfBpAmCw9YTXqvd9mRc0dzQxWULgRGXgw9Q3QXyojb9FcVHQwd-T9sYMG_jRhRJFun8nZyJx21gRLB2NBgUha6jrZVRfgWGKJ9lNAo4VXS5V5Po0SVUiMKpPO275tDYuHbuUAMBVe1xW1La5hsDLQtcIfIxE4vZXHlDkK04gxGq5iSO7fUvk_kZMDWr4adkMmqTnN6hDfP6htlTmamMg2YM1RAyf8JPUyjbHqYAtvKy7i0B7S1f67BpVXtJnfyyXiOOjqNXeWbD7QP4sB6EoRThZ2TDI8bb9VHXRKD7FmX5mrWVrMJAj-vHOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBveqcO1n1aHSWNQsFRa-CO-96Yg5LAa7r_T7_Un4xMkGk5NnsjNo6hQLlEXfAqbuW8iVawn27vtgqMT2op0HeAjMSUQ07FLiM7mHwAsM9ka1ZnWi17VNjPdcxwggss976nDIGYAchcYxChx6BP-liqf3NqbNhmJKYptU2vR6-nJMTRPkVkS43gAOT8DpTlL6qPGCADzWAKIXcx1vGy48oNFqdwNgEJkJ9h5uVm-0epBmPdJ_-oSGBu4r8anal8oQHFaYmao4O3yT46OEp4009wHsZ1hUorC5YiTv5icfQX2-M_GCyK6rzEJ6-8prQUSaNLdlvXi1W18A3qXnXY6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLi7IIqiQB6VRjc_CzlG5XIfwQAslXTGXzMt_b5UL6HubJz8rsOaLu049JGO2B6OEan9JwoeIuodOdasJFOzy2hfKWATmdPNj_2fnrtf16LN3-Ep8dqPpBroyMjhka_g6jCWqMsOuzjZzepiS2CS1muoXiYyctzckxbxxaaA078X9kwH0pJhqFDnn7NHedjufi4ZD7idloYGNER1xShEW860nnv_TT5RCOEpaDbze44L3ZeCPglDMHayxl0vFLM9Qw2aF-owuNU4JkVyKNvSU4H0IO9jf9Jo6dVgxpoaV8Hw54bi3KgKAz_TR8KPfvXm9MUjpJYIWTeBX-iKHuOYBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZQHs99k0drnUenFTB9MYg7sDI6hqFq0k4DncR-_P_NL3N7Znl2qsZBLpneXQAt83gKkMCcozR6NiWKh9vjHaI56Jts9V-3u3VI4AoFirTx2IBLXdKNbJa5hU5stRwE4AxHFPIE1X-Bx6__H6Ri4KB0Y52v8bV6aVVRIaVrjj_t3JO3innK7J5_7hL-U1J7rsVt5A9BPcX2X79kBrrMEdG14I6KBwyanHTLVv3Th6slBbnEwOJpk6Zffu5XpZIbsN50DGdDC7f5KKT0EhEekQkSKGZsm901Os9e1THcwSy99nilk-qU_iag6h99rqwD94z2IMPLUasQ7FeVUDLNxfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewe-TXL1gY162JsaP-Bqlsi-_HNzpCYkfbsJStebafc1yL2itil779y6PDo9tdXAnCSVDYV5x-jNW3zxufTqKIhokjocfLmb7UrMshfaWR68Rfkd61Js-BCmPv-xvpuHLgflzW48l1g8MKjyKR7u-rsAx-9JkIhfybVuKyoCVqtrr6lTCHnrdx0YX-ZUTJHS8icxBfjCOju9gRjpIFl3uNHB5egV244wNx2XAPwaefc0Qeoq7X57JC5Z-PvSrlnMDkMY_X_3z6OpxnZm8jPb2kB8qtRPCblJkBb9t8xN2Jr3EytUacJSb1Q7QALMShSR7tqxoE3mLOfH1tDRbiGD5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjC7DJtxPC0yBXMw8Mlm1ahriWO2MwE8N6MvOdjtNa2jGumhAfpDbT4kjUtFBq_ABCfWPSz_LPlNoMN1edCzhghZzRGm0dGN0jzXBESbyDPqJlVN3hzZ7i_RS5-K_nr4h6CZfLNxR6mQakWoEZV6rwpInE_FvbUbAvtxZtaa7cRl_eRh6GQdQbxyKFJyjTi6XSqpXzH3RqTMMsL5LC67A2BIQmc1MzYBgDO8vY1shAtwMlS-u3tqLDoCRTvu8g5hlIYROfKyictax5mWXRRv9PlGXNX3CthAXafFine47P6unsg5Zgc1q9ul_d1iRqDeKMdQnZpJ9ZcGCBIToW-4Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onvPNHWfoOK4Rp7FwjP74ObR_9U-7u-WoyfBYxHnYmd0Z4ml9t0TsUwVejsLhazE5sqyBR6OYqG6z5jQwHS9LTmbQkZNqd6q1FoVbu66hbe6jxqK8_qijm-56S7Tn3Q8g4das6EyVAM5-V9qVUNfLUTRMIrjdo5WRFIcRLSAWcZPfuKDL2ewfvoc3I3-y2AzSZU252C32Fgas_UD9I-uFYogatQsj1a2M6d5n5Pp7VgKgLy4uNBxENtn7-BaUsatl50SbLvwYYqBBEVkjVaVsO9qhxKzgGDmeB1WvUh18Zx5s93hL0H3KBe6yeY3yfVZFtkpViZlvPiba6xAxEw8iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESQ8HLzAaQo37NWOmQiH_mc0f7ccqCG56oIGAwiuUa4_QrL9Jt-oqSMOWb-5JcPieb1l9deqOobpRji7MksVzuKpdocEpZnMX1vrV08vX9wSrnG8OXOvzPjzAUh6PgldHwWwrC5-P09IDdOZesmOJhBYdJYGDBJ8uZml7cd-9cOmZAkcBl8N5jR1sAlKcoFQZ9jHe7vLljAv1hHAUgJFdhV5pikcJcG63jBRGgniPxVYqLRc8nLBJ17TRQ_MGW3OSeMU-S21YD4J9Gw1VB05MioG5-Hh4244gP3r0NiaXdcpRcAbieWS5AzA2wfvrtTKiLjKvOEeKykjhA7JiOkgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4OMoxfVbcexDvsp3yfOxuBOmJI0omVypElFsvc1yV6232VsrDiQh0ZbRbdjVlBcZZBRCgmjCmb-UPkNRzMhaiTLPEFTuZ9ltOW8a9HPySdVrTVLDsex1zxepISOjIDAKmUFTGFiSJuU_jvYW-6Q-KZTmYKc2ufrMM_stjRY13KE5d6SddV7_LIFTSVa8rMw2NXkdGYCZJYit01vOoDTDv49HcozbID4B9N0TLv6ASRwGowm7pOYTuz_Za9VcCZQNiQdR8tUJb9l8Pi2JvwB3rVW2i5tN_s7RRVI9gCVVzY01PxnRT5RQdbcUxGsfFE9BUcnUgPJzIuuMf8M9eLsJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPW_ShSmpXp6qpr-TyhpZCWC9HqbCqsK1q6Rb3yvKeQIix41PecFSbwVBGWSMQBC8xXV7Jxae0uMIpwrSlGMt5gzu0H6KA1ylFM90Y-RO3RQnpo-ur-CkwcQdCv6icm0ChJqM_Un5VWJDY_Dx0comD7J6Tzphcq_a7HSjC59K2AWNuW3OgwOxU6QAwRbYS00pBsVO_jSnvOjrYmG2zG7sj_ylBc4BN8G_2KlOrXcZV8457QOJtPzNSeS_e_006gT6puRL6ggNYuKTyRHP3Sw5IL4GTxqsmTn-7CDu3i4aqoPel7WytO0rPUaoB9taBCjc0pIc3KBFQcTJGMRaxCZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBVOgA3MTLERXEXVeScxDRJ46Pvo4eKaaVGjmv6DCwNJ_tTIWfrQdfFIgo3iZKjRmf-dtdr4mASo9DCCHQR3DNeyCQPyjrXYOT0RIMXP6dC2Dx0vGO03Fc5Mh5aQoFT-CbkeIECqUs-LOYsXrQVXeiHxLwId00u6aje2NDi9PNxyUq3zI0qOBjv-PijQZlXVQ79P_tiltEi2J8HNRM0ZiBprk8vz28UyFhU6vfsoPcVgVoB-lAnc4ArYu0F6HjwJBTijbcopT3HgOYnC2DbCjIXFtPtPKAXUaPDs7dFd_Pyya9Mr5YfI4bynCUO2J5TU6KD0BXn2VLAp0uQIU-nMBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9Iiv6LZgbWiG5d4D2bXsn2OkkSHNRWSA0-_G-ws0rTTm7OCSoaGIN_nP7zII0Bhp_Y5xIDlfWccBIW0khMPfrFAknl0OpNMU4UJVs0NtjeNI5PFeJASAFtbc39gWROXUn4CpHG1D_pLPsSqBpa0ItRKUocHaWUQcFPudL2W_iIQzYgboEsKRtqYT35Kf7iAlS1DyViP7P_olBXstcayP9c0q35iFB3TE9oKcUOPfja__rTvTYRoZ3Akrej-3K7BVKFgwnuZvjM1xWtZ27G16AfcGDCxpljfws9MyLl2TeLabSJqwKsVAi0frIHRvovDvsyRQW5WQfirhjxR5LCJoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbSPJSnxkyXi-yO60MyvHzsRSZuiSEiYaHbspWtUrvmfOTTtOtw6a-WstmtoQV0bmkaJCi5eEsx3-U1pfOKk3dIC2tnE_46aC2RY1JQ79bpvRGMNg_tH-HeKWvT94SyxRNsOxPwlEv-_Av31ZLzibA4FveoqKGgSz_U2VqInzmeoxMTzoOqRE8c3VndHWJOMbnHK146VeljBoviqrIrToNN9K9TY6pIoDItCJnYkQV6q7C5CMyA5ac2A0_Ltco10QLBRPkqdErD-NbzzNENpcksKUUoRa7Ik0A57qcD4B74DEuNVab-4CWWiSIUCuscfa5vKV1UMSFZOYZVY3GKoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4GLfiXZTKqGV3lxWvNKJEdj6JmQjBqUi7o_g2Kax8LFv57WB1nDa1RGjvJinSryBOIA7kGa6hM9L0fn5tGFNBAKKTgF_Ody27pvBuRkRSm0UrwCnbIsZ_YaVJjixLBVKORpZjrgCO3GFxwPfVZ4KykFr4DShQLcVQyoifKfvYVN_DXkNFfkvU_8rAVxApc4s8P779LeervgWsMg73GewZPwDvDeZ4DTIKqgn5hcrIVMHbKsgNdaxYIMJNTdSIdv07HySqpy4N9NdN_5--rlxZsijanB-WpnphztjQqoHKt4reruZyEgdCOitvmrxNpjfOrj4rT6VroGIo-WyBGpAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KawOCCAM80Kzp20c2i-nqlCCOBTH14eCOHhAIg9bx78hjT3wdKTwPKVstcuYWvHzZ2RWvS2Pq9ziDlkn1nVZFC5C1JPEaLDz_12LLwW-NQLNe37SgfokvrtTlwId6R8ABeMUE0BTOqBPuF_Ev2Kl7r6Btmx7CknIn-D5XUo4AD-EXF1ubnKgI8Wyt_2KkKikUzzzwJZoK-FQLoD3IUwHZp8NmQ_Tgs4ut_UqFA0rye-D_U9ZeXcY9ZUKG41hoFimnu2zVInkeCk20WzwWY4TmJyDnnSZ0hvhw028a5VMTFxxWfsEhKZbLrx2E_p9fUVfSuo1DVqxp-X6hSAaXUrAsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgyUMp4R7vb2NmhysbElodn3zvcDjwibBokjs333QzbNILp5DLDt_EIBJdMnq8rcqhbbnx_Vkokjd9tJF5-KkTLjqixECn0L67tbpKIzghMTe5KtL1mSjXxy_zbRnz6z2GiIr6D1Z3Uh61c5IFyGfMytRLpvLq1xbDNBTBUfyOe7P4gp2UW5ZVHcT-1dnWyh4W3o8q-JjBFhYe4dhGfcAfJxS-NDNLhIcLWO9UFe9U0RZjPqnj_5FusJ-u5ibLE3peJuVVvU7VAeYMqpaR-cxcfOWceF6ZyjqB7sqCZpB-ykdCm-SgP3dzpvzdp4GUfm-Sjekvw3mfGLM4kjetVJGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8yYt3AuG9dRhvASxox6iip-rqWrQAK6UqF2Tre-PqzKKpmEqAYZ_p-y-J1_8lBnMopiCCMz_TpeASM0B71IMHAXK-ZiX9GmySfns0NM_fADlOxcSgq_4dmnjWFeIJPvgi7CtidxzfLX7fW1y0tmrBCFyPvTOKaOjxyvpcaylfhBBPlU7H2gMgIBV3SoVkyqZ6Nh5tgHJV3ixGxVcSWkT4BhT-PolJBmAGR7GgX9eBQW1Mm3_oZRxcScwYsZ7K5Vf3ZGEdb8Ftjtg_i_4slVgKwDDvjlFV2o_zR1JY5hyj_4ApCi25jsZmuV-Dv2iB_yOGT53NdTCiN19pnGGEL6EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IGKQ8S-9TPZS7IyALah6k5k9eE0R_TaqPG3zWtgW1-4Ktq3DamYm5WJSRaYa566e_e7vJ7MRHvDbLY2pR6jH7fFPLcZs6ZzkcZUgM36v-RyH36UgcoOtUCcsUIZjl8Y5sYn2TqpGtG6y5mX4FgMI1m7X2ND4VhmhEIvCbWz-ydV2bmxNHf8aHdwG0BhNB4uF3aM7IWPgkS9NGn9_LLYAZiWvDLpNpmxsks0lWNQaq0HCIIYIVXo03OmhVngyJ97AZNI6amg0mv0PA-oHHR9jjst-T6_5bJQobP9cDDZQ7XMZdAO6VbQ9e1TerDM-enTPhx_IA5ahbpeXrMTQxDLNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4zNkIg1JVEUe5ARRmJUmmCBm_kMN_g8pl9P4oWHeLRlN3pHhf_TW9YvZbvioQnTC2d1spTLLeg8ucRGz9SXX9LU6BOvyzxg7ZHwfYe-csfwFZfJP647hHnjbgYeGYNymz9bUGzFwFAbDwgNzJy3NxdcdFbYCAcTbsD3xCwgeowRmN-hNUEEE55YRaXofJy0czk3RD5pUpFg0pJv36yebJ7G4lmJC05p8CGDN0--ywKmF9lor0l7WrTC8k-6KahOx8yNYLu6jCDmjNMxZ3PnbjUAf09EMI1C_th7rjHfNGTMM57e5V9nelBk9VT4q6vHzQ5S5IDqcwKNXjdmYYrLSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZWodZ6VXIt7L2hj7u2T-2bbZgMzR7nvIIB_4iqa209f7P1m_rVavdKpRnO8EiRQm4sAZiH4Zr8giH1AZSBrM4w2y2RO1ldMin43ojVcQmqdBX8yo_owFC1kcQMt7IJbp0btNi4Wg1qtisIleJpWriPhwxtmy_kIl38Pn8XY8_OWuQFqwXB-60GsDlnEuxZNwdXqsyldBQkAupVwKh6Bt3Ompg0AjIvllR4kY_rC7M38Z-gtGUFSiI4r2-nsHx_nwZg8BazzxuBpoZc-8gy76RmuIi--gij9vgmjBaY2jIryEPpnmw-KrDrl1wm9v_3K0NHKQZ3NRyJEbWgh5vtjZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGn3NNpz8XD_R3Ca5om-raqkuvrRSMJzlgOg-LSZeTud-7Qiojg8_YYS6tSrOJ1IceJEpjJ_wJKTbUQLykTwSNN6FSP71pJHu7jMSA_OmGpflNjLKNrMWe4iHcsi2qxHLh7CnrBfZ2LJt196ZmRduEn48-jvRFrnS_xh5-8nrqZKgN17FHc6_k_L26VbiVRwptiSFFk1YQUOm_-gxwsxchnvaPrNjQp4y3u5TCVq2G6yQsRkzqIaNS8peXFHB7J5AqrgIyN0AmGxDvkNsG-eNi8M5wLcnOVKqyDV_duRuy36Tp3j1sqD229HTWAX5eRwn2NjXRFHNHI-4aYalwMZeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFlv0qkLFG2kV9tsTNOjViMQdOO6mnmV5k0GDE2R5QtIxp90qXx7sRlCJukHK25LOPyGn3vxa7xYnKQtXgDrEKqxF6o3zkVh3epN5FAdPK8Ngw2oFlibJ4SSH5HU5zeHqDg2nxa7fzP5-0eZPtoonajTflZCIvXo8B2W4zQrcoN_un2_L1CoXisv3ioGW9qCRA50qtEvSwpngYImY9De8lF-Rgkx7BrW_mLiVO6D_SMFZX0umZSjgjLNEJDpBQMqVur0LQ5QViBCPFuAo-Ya8N0yzpz6KxffzWwgvJLmlq8fWo3ZFzT7tr0lsoIZrLPwQp7AQcBHm5iZmKRhXGYxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcOcFeRXOT_vEudZekAgcwdCV5765L-rPZUAYqPYWhvx6_P5cJwlyBCHqq411E5BdbPvb5A4OcHXB38O5-Zv7EgzaEH3gw_a3-VAqSo4fSc7DXpeMPYkS0VaokzzAITGcXOz0HH2Fy-IWLvtMsd0FouvZr0_UKmf1csggAPxmaD5qdqBjBTT2z_oSpxC4YDuFHHEGir3aZpR4mkkp0Xi1nkNsbyqZH-nR_4ZanhkIp3FbOoxR19Xb-0Ng9m4IOVjbmfhWJ1SVM4c5mjZa0TZwnVJoPRbsvjfS_3f_f6Ztrk5rD7_TMnBGtDDAP-Rk8q8fpTLPEqxZ7YkMMh4zGRCJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ZbEadxfPS9P8aFO1sk9oX2K_Js6NPzvyObk64IrKNipmC90Y8WFCASlwV9h-tvZ48C5L8QajVPxyV2jh7lXLTBoLIuSnFIsgHL5XWZL8elsMWureyOvY4PbEKzhetIXgZGJ3NR__DNTrdlMda9TQzQg_DsOOekisML2JWs6Swblo57-jaKhch_8_sT7ZLBESovqI3nbW3nOX5B1G1pa_WWIvRBfXImYtm_CIZIW43PDb6z7mlG9Sh5-f7K2ARqRW9ZE5KItk1H6fLT3ydVx-YjS2YjVODKcL7mvyF11pCtyAaioNT440qkHkICFUTfacmHC2hozda8bjEPtaE-8B3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ZbEadxfPS9P8aFO1sk9oX2K_Js6NPzvyObk64IrKNipmC90Y8WFCASlwV9h-tvZ48C5L8QajVPxyV2jh7lXLTBoLIuSnFIsgHL5XWZL8elsMWureyOvY4PbEKzhetIXgZGJ3NR__DNTrdlMda9TQzQg_DsOOekisML2JWs6Swblo57-jaKhch_8_sT7ZLBESovqI3nbW3nOX5B1G1pa_WWIvRBfXImYtm_CIZIW43PDb6z7mlG9Sh5-f7K2ARqRW9ZE5KItk1H6fLT3ydVx-YjS2YjVODKcL7mvyF11pCtyAaioNT440qkHkICFUTfacmHC2hozda8bjEPtaE-8B3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwXeVjtgisYs2qLs9J1EUsAktDNsGZzoYsb_SOd8dFD3bKnePPstndQlfvc9JNzxG7eLWmEC4Zht2EQIGM3vKYKxQc3o05lvB4oP0f5GTv5YWqKP8tJe1QS3MZ73LrY7_BhS97b2vpM-T0LGoU71QiQx9CA6SwBr7NkAvaIX-mE3ztiobxpvnUOqRfxl2MtdMaKSiDZapsQN6Qm8J5qEQaHTBuajrlFYTxh8jkiohyplw4lU7-Esz25CFj8tF3J28e3cCncolfZGxp2fj5T7KzLkf_9szAd0YoVjK6nNDfGI7oC7A9JOO2XjdtIDNcmLioIKaW53Nsg-mKHQCLLq6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8Aq9xjKFW-PyTHuU6WkDXsjdj9vIW2Za9g7qSSGGLgq_CrUpvWN5JsMCotbBdL0w-8C2F_RAVWnxIlIDuc74y_mqLuo4jtYzmwmSREOs92LGhoPVFnUFxkHbewi2OziUCO01Qi6S8VdKj_OsX-17XEE_Lj3NdQVvTsyXRO20_XU3rY8_OCgAnXjvlC1aKu8ldQtk5WLZzcuSv35BmY0rjJx_x8nfdCId69LUrFPpsMHUpGT_FLcEZHhkp9f17BxW-e43C2g5k4UO39UijfDkrXvZIVyOWqfL6CGO_eq6Jdk3ByHZjTF9pmS1N3KhAjxXJiDtTk1L2yUqhtTG2hPqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jibE6XicK66Cj2BqmY6S-b8jkZocM9q2Kc3qIEkhUDLEmQK8sg8ABX8Zp-Brw50zI0mHWDhE5Fomy6nPD45KFMKgipZ7wX93yFrgq3uHH9eBkKmTfE5Amq0HWvLw3iRR68UMPj1cDm7at9LvDpS84_6rRsYT4Lp_RjeC2ME8QpbzIT9xr147ok_Hl61LFJuhmB3Hg7gcIx3n_jQD7F5rHZkL366o8t00J1hwuRkbuCEo1M6PAfOvlWUbO5dvHfkO_VR2kQsx6NufR8xVF5JBF9xl0MGSStnXB1ns0ORuP0Z_CalrFbHV4bNwoDJ9MbvossoZodpiKZSMtWomrJwV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UotQqVhmvUiXXKHNrnSGuQOGSglU1ISKuJ0umB7DCZSbVBCFdt8moYB_SV3-2JvZND-umLKCANjmDDslG0nFwSF5k-_t15LnQRkC03trHUkEnhQigRMsKF_fxjBhhty0VTnle1Wshlt4wQ8yP8BefpsWqamabKTLVtEi57IyrDIbACy-T2c5ddHFAvJgIGfXQh6EBbDepMiMqgA1_46eNKU__xaEujpynKFEPnNYPxFf1B2xALp2lZCL13H__b7Kg676bLeX5OWlk3rkCB3ySKEsYDzHk94u0Am0XkMuFy_7971Yfxqo6ryqabccOeDzFh8egFO8rUOOkcv9SFHHfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpNV6iKx85wUPq0aDy2qxX8hFkOfld-FepDoNOGUU_rS6irvldkC_Mh39luK_NY068HXngn9jeYRd1fyWn7AeT6rsubQAhqg9Neuh-38CZbFWOPLx6wz18CkEqe9lCvIyuWsJIiYFxGZpOOjlx8J4nhdHs49Udw5R0fvD4VK6jF0-BVxRMZcxmlzTwIREChrEBztd6rJqgd9eMAW2Gj13wgf5P7mwd9idQBzIcSymhOXrneY8HOumSPmSxVw-JZE6Y1Z95M3BIeoKARzfJyABz6hHwtq4VBdkjP-cqfm9YVsrYWReQh2M5eTGS2PlCap65fUTs34k3iUOAEiA4yF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRfeYG6-djPHYDPuOf7Uwizs6ZyCE78SXY6CnFyGUuwPZCuZCdfOWIPaLc6B3wmpXQTiiRJBh7YJLO65zfOpqQPhw5yLJn9PP2-aqOjokGD4HgMSKJsar9l1bG9itn5MRZpo6c8aDfLhjyYoTcruBS4IrOmUaKvdoduFph6UThhlIbOny6EWDl1ZcEu3I0Egmh351UD3m7tsr-acw8UT0gW_YJu0i-sebkatpN3tlMvlt-0A_5rj-r5vjVOTKOhlvIDDqwYNQiXHJi9GoKxZDK-YE5HdDlKRewJRRewwVuf3Q1RVYKeeaLBHt2Py18wVv6qyCyQo2nzKcSwvPHDnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFENBQjvWK-kXpWHx4SfAgyFsdDwRf6pPrdAQpAX9uTykoRLT3h1g2Hhg_J62Bsr3VsJFdNnvQAyQ6K_m8yFgJCBs_Yyv4aas0Sb0PK4oUN_Jbp7fWk3DYBAZjn96AVtIFFXgzg02E_zQVTFqCeDfADiqZPmrgT6AhFcJgoVd6Ir5tJs_cGqC3qKskw_Jqege91OduRBnbWbZtq6yRV-Eu8zAjZO6sZoNJgo3pEv2lEmSuuJbKV2FBhR8ag78nT8Av4YC8z-sJ-DF2ZuZD3JfY_aC7jqgA9qiJTVTIjMUorQXfd8IgCuY7q_tbWiSE-ASaneZqXEKg9jti_pQSvPIg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=qzQME_Tyine7eUZ7m-tEx_h6eEtjkDypwhf4Qwlz81Q5YUkwtQoRpC0tIxVkbfx762nesttZLGWNCUuUnw6yDKWOAeckx_f8pYfVOlf4E6CSBAhkuG8kBa9b-bXfLB9Hj5Kg4tMrETraarLRxbEaVj2axzE0aK2tJmQWmUoejKJ8OyVhivzDFJjq5heJ4YdACV4e6IwKrImnZFabf4wOWtJ3KNyh-ZvxUBVlHoq8YXrxN3E4E99iqwEQbPWxBUhqEc25DdD3Sq_9hMd_KkCxVSGl-k7O4y3C_fAkfHyjNCOPRO3HeRtG-6v2565NokFXj4feRYDx5f2ROIAlFjxpJFRlwBgKgDiO5rF9c9PEoL4nj_dhmviJqZ1VRFx7SZj3pEZ9lsP0EfTE3BV_G1ORS0dIMfajiGW2Dnv92zSEMySK21mvknnKVpccKf20rr3B1ds5Hoa28alX3n7cZMM6POI5wUde9CI9SfMG4Xocy3ECfOO9wLyp-q6tNx7MrDxASGqJNMpP59Mtx32bHOkqQER7W6YRNA8QRFo1sQLgLxCn5GAFAgTdzfjvdQoC6qqyvvqc3Bpr0WA6Wv83_z4srGyiP8TXaf4SIZydCzoffbFXuSsPXAaGy42dFkPuYs1hIRlI33pvrUG9_mLEwKc9pif7-gsx83vR7GxvWGGtRac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=qzQME_Tyine7eUZ7m-tEx_h6eEtjkDypwhf4Qwlz81Q5YUkwtQoRpC0tIxVkbfx762nesttZLGWNCUuUnw6yDKWOAeckx_f8pYfVOlf4E6CSBAhkuG8kBa9b-bXfLB9Hj5Kg4tMrETraarLRxbEaVj2axzE0aK2tJmQWmUoejKJ8OyVhivzDFJjq5heJ4YdACV4e6IwKrImnZFabf4wOWtJ3KNyh-ZvxUBVlHoq8YXrxN3E4E99iqwEQbPWxBUhqEc25DdD3Sq_9hMd_KkCxVSGl-k7O4y3C_fAkfHyjNCOPRO3HeRtG-6v2565NokFXj4feRYDx5f2ROIAlFjxpJFRlwBgKgDiO5rF9c9PEoL4nj_dhmviJqZ1VRFx7SZj3pEZ9lsP0EfTE3BV_G1ORS0dIMfajiGW2Dnv92zSEMySK21mvknnKVpccKf20rr3B1ds5Hoa28alX3n7cZMM6POI5wUde9CI9SfMG4Xocy3ECfOO9wLyp-q6tNx7MrDxASGqJNMpP59Mtx32bHOkqQER7W6YRNA8QRFo1sQLgLxCn5GAFAgTdzfjvdQoC6qqyvvqc3Bpr0WA6Wv83_z4srGyiP8TXaf4SIZydCzoffbFXuSsPXAaGy42dFkPuYs1hIRlI33pvrUG9_mLEwKc9pif7-gsx83vR7GxvWGGtRac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/girEOF2iF7fxzTOEGfGeQ94WIpL8H7SWWENhnu9uTA3OSWmC-lW5uIusvZq8TY7V-7dyQPAoAEmqATHbyOVPbSRgd4eOjBUZJwvQ-g7fEdQWEenIaz_qVRXX1dWu__bqI1pXh4IEAb6B-n9rh0w67oaK_TAB8FeoF4rWcKTcJSxOyoAy7JvQ-iN8AzDiI9bVXdfkTCvlqVKyxwenCqpnKHp2JEULxPXusY2gwNH14ysVYZrhyrG3aNq91-SGhxGI59bMSmQwQUEdgRp9_2mBakul78vhmdKPti-mcXln0jsv6gZV7bUsZq-YYH2IjknMqH9FEBQhO0nL_rv4Le7nsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ewu5c0ygIzB4rBHm7GCPxYJvgk63viTzGPgRrJ3L41NOPioUsOHlwioZfcpl_NC12t61xqpitYWbvanohITluqb387T-czgcuznx0Jy_Eg2f0GOreUPLoh0ON3B6nYf3VwUZPQOv-DoWIWePStrgMZ1Z-rt_4TVwoU_R6YnO8XvxDwEJ_FAKeyjfX8uTg45i2WAA5N0aGhFC91DZLiwZpxjqHX4588yL0nfyHVoQUrSsUxvvHhR0cDa8dMenXm94R7Bs4vl9IbRhBE3vjuTiLtmvdTLn8PUO96YNXqdu48pshAUA0AH8MX968psS8jedBmM_F-4CDBqAcZYlp_XSQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S17seJlyA0BCCcz7hvTeqw2K-qy_NLm1_XF0mvMZf04Ozv6HioVaQJXbrsUiyA37ZgyszIppLcpUYGvH71E19UTmhJNhF2twAcjhh9N99FntcQChNzORJZxSePaveQVCih3spMYgPJZfJliVy41R4-SZT8PSZ9HA3W3sPUcgyAqzxMSJD9eP0PSQz_gu90qLtkGzFS2BId1QggKOX1ok28TFvGz0Eb-kV9M-awYObvxq-q5lfsYC_O9wvy90EzyD8kXEC1_JjGnX00h1xipkh0OeKpskGLctb7RCVXfD2ox0tNZtzd6HTfpAS2dmw-N_KBFXRXWMUaKMHn71D3fbgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bs_RVkLQPBMbvguuXc-zeW1WYUC6D7P_IsCAYYS7qKO7JH8ZuBJ9BCUvTazMMeQAG4XVx16UQMxc3A6KZStUqZjuBKILFiU5C0CS_81CfwN9kUYC7LnR7z2Tl4fyEbvihPwSFXZmd2Als37u2uYMOeF8hCJYsoexuj9yP2HmoW8wu_NAQ7OU93anlSigp7UllJcPRTO2rCjXs77GFEutqFNqPY9mYDMcBOhbp5-8eOWtuiS_achBoov5typwzlW5gM-9-a3gl84a-wfZhFCF8ajr6VI_XCILcW_PkaptSXOBliI_xfKIq0k8pul-c4nRU16CqAG63YVpGLExAGny1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwvTiBI5sRbgZxX5EGRCIrysE9owzG71OOL_fRwIvTrtCwzaw8A4HQAxOOSduUZ_POc4PHKLYkP4GXk8yWk24hoLSExVUbVuKUbjp_2C-SC6jg-GHzxM8NSiyU61zul_1VOfUW874VnBhFxi6FIvcBTo9ZDf1q1LgpEAgwFV8jx9GBMjkdxLvzco_9ZMSYQND5JXhJJxOl7V1G942U0JyTjItV0v0t243ttAXnsJq2PdgzRF1FmcMBGXQtzoaCT8m9tc66wBFsPzYZT_qbYQyz8hgmbOjBkCvyk54-vg3cJrOZrg6VleL3Ri_hSsIj1F2cU5snbwzFxV_HxCA8UOXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0VlVEGVK-UmCH5qQX7w2sRHk2Lq0pLRqOtmiVGpvR4NSZng_6yavqBKAPuu18FIdjpypr-m3GMieroWWvI03FLwstJ1X1V0KuYd9wwTno6PcYv_ATaEoGTWu7SOkh9gdbyZuKGw9_uMl94VDGZ5ywsPp3I43H6mYSiFdufYoJ9LfONCrPCERIepEqzCEmrHtyebLYv9zFmdyZblCXO420Fmano5Lh1yLgIAE5-KJRFxa5ExXrn2YV2itTo6RwVhqKacOp3fwL3gpIeByoFkE-aGRONm_yrFdmzfDb39s5IoDBO282k4qcn4LCZiKyYZ_NP-QBcCmh40EVhYUzaGdSdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0VlVEGVK-UmCH5qQX7w2sRHk2Lq0pLRqOtmiVGpvR4NSZng_6yavqBKAPuu18FIdjpypr-m3GMieroWWvI03FLwstJ1X1V0KuYd9wwTno6PcYv_ATaEoGTWu7SOkh9gdbyZuKGw9_uMl94VDGZ5ywsPp3I43H6mYSiFdufYoJ9LfONCrPCERIepEqzCEmrHtyebLYv9zFmdyZblCXO420Fmano5Lh1yLgIAE5-KJRFxa5ExXrn2YV2itTo6RwVhqKacOp3fwL3gpIeByoFkE-aGRONm_yrFdmzfDb39s5IoDBO282k4qcn4LCZiKyYZ_NP-QBcCmh40EVhYUzaGdSdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR6yaApKkNPwyqMi3Off3zRMuhoQVjOrcBOZa0BkY5NCWub0cOslpFftoiOG7EgK8bFJiaZ6TpVHkSmGC12VgsEFiQXcGEPMEZgb75NzA8DoGrL3bR9u0UEQY7lbKP0HqNrLV5HYvLUCAbPHJPOBrdJ_yvXlXPacjvIEKa9s5pNcCaVavfgF-1DaA_5LdjXOX7yuKhmlWcciWkBn8Mx8T5bEOp7TWgLkrVYigxgBWsseTMBwGzfmdxYeyrikCZJbY19CkJgTH4ICmDRxdzTMDPd2PkHn5J_E5cRjZ_aBrjgGak_3Puqd6zgfFRk_r_3ThgovIg4mnK7clpVCdrZvYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRGFQ2EJab3j2QuU39Nhxy2V52ifIMNKdLAy2tHBtv6aSafNogUawkykDmEqHonBoa_C60IyCGrq6keDHjxJurSbwLOtW8Ws1Kkwxle524NBV4QekHDbocsMfPgKAegQxiUXcBh9Lx1YclgiHfibsz87e9sWXEgsYolLZAS0n3UZTcuVZo5B7w8acr1xgkmEwzSUUvwbvuKXES3AKVSKS3uMA3OpRXfnGKZGh1V6oW2oZKIrbkvZnQVSXhGBscf1drnkI1Y4fywHhPMvsaCpNshbg2_SSEnSCXRI8dv-Xp9RjJJMP3dg-Ft0ggPU8eH2PMaT09-oeM2uxBTLi9Hsbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5-qPv2_ic7fd6hzEML8XeL5LdQsXNPTCtcQTzil6dAIeb6r4_-MDBsjybKsue5hak_Z2vWd9pthGvZkjFOh3ROji9nMXUzLzS_TNOnEhTHjo5CpSprKiS_T7IuYCl9D58YUsIRxomO3aoX_P3z9nxjV73qGPSMN-WIe2KI14Qr6tttPFX8KG_JnW1SNK52JSc2USVwcg52MfvNp4iCdoAC7zxdp40i0nrN6V2C98r0mhDR4B0N18QbyUboDMGjSLW8TJ1DtGSCozCkzBWXmbC8njwL4xG2tgpMAVG8SNH4HIqogwRtu0c__Bpzjs0G1ar2F25chZpnzhsev-zsiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICG5c6cNnCh2hVVzwvQ2jaHOxKw6n1aKWssMtPRF5H10rr-1Vzkpr1rIslnv_vRm8e9o_cpC_85FxUB7K9RdGNUH8GZxoQlcaNWZQRzXGl2ghxV29udtGSz4jLARxNuA3DEOf1-FfK53E44l_MRgL2oLoxzmk9jxEYmDa-iDMUtGW07AId-9ZIP9vSVzlWFSxmwaQXpSLeTnY3plk3k8xtsQDG4xTl6qNzYgS1loeMbdIy9EYtrmxxKmADoKIVuFunFaxMn4mRaubzBMdve4mJ7aKuDZSStsGGpxAPtC9fRbH5NpLnmsrK3S_7yoe1OUoA-G-X1ifEPTEO7av6GBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuw5fY9JfbuebSj91-y2NrOEajFyK-Ugf1oSEq_WpQGtDH5TwolAwZXStvTIZxw778xqnhZaGQZ3LVuAC6gS0I0ACScs84p0YIBZQGaR-R6gZ-Ljf139VDLSV9st03DRdo-Bd24HYeDd_BXsx-2i3wqcHS09uJNZrP9nMBUWZucZZGh91D1ZxAke1usBWrfV6g8zRHTfn-bqKYr8JNbL8ZBXH9w0adzNfE5_XfJuAwEUX0k9atxPS7DMglSZ-v-bDvsmpJ4ThHdRMGx0DbL76mBGEdY1dbSRFlgfe6gnsOAGFBcJZGPt2J47ja61eAIpNAtRUvxl8e6s6RM1Bdo5mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjXtc6d-33TS4G1m-3U9rXUtIvAKjcXOINhp0L8lX04stG2L9a8BR8dYBm435jcwgDuFm-3bjKTFvJCsG8B_gMZp-FCfOuJ6KvNR4eJJyJMKEuZoYaMzLF0hwjm0NCGrYU18PmIPh4KHomMfw8UXWi5RGKwJlelAuQd9D1xYWgOsV9JZY-IPe-ZAwJ1RDSz5p8u2x3A8O6n3Yb-mKgTICemnBhzGa1EJnrX3H-K3_tUXqOdRQ5-1udzqY9qWqw7l_z4KfvYsjLCL-ruwLpTYT8pj2Tb20ThNYDqIQaTOy-FfNnRN_iAlUcjsQavQ0DpWYkwmYhGQAHjrr7owVftIBw.jpg" alt="photo" loading="lazy"/></div>
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
