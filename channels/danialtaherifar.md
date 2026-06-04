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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
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
<div class="tg-footer">👁️ 223 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 476 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBIUP_N05UGkNizqitJ97Il5JOdpb5ojBq7FWPotptCE7bon7zW8z7ezx_P40nZ96o-yg7vP4RMcBpCnlYC5KDYXzLIFEXXVOfrwP3Tpvmnd4LUK1i-kVBJ7NX5-fwMAY2TfDA4Crpk4b8w1v9giDn3IBCvL6M-sGqojkpEllqEgSI8Uh1C7qOdHG619aLWNjzR1djZeJl0y0im8p8IrkElr_RlzfFQydSoOTX8l8VrgbAmkdqXiu4_0FwalRARRWJsbZmEz6WwaQpcV7km5PmiOniN-mXKHA8o0qSCpI3xuWpknxO3uouRGOPcBrou_YGr50I6AkTAeapl1asvy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 737 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLljWbe99BguWC0tpiXOGIHfQr0kqp3xZQeHZgKcQi_ncSfen-nbvgFzVXdyH9lYkvRCkiNgEOHiZh-HbXA3f0ul3P9tn3LIHJZGyym-T-Ch-8GdOctVyYa1tzgY4kxD1QkVrB7j6-np6jPby1JkrD3vkMiB0BLGB3Pzr2plTkAvK4piy9xRb5EnZRnfKbE64KcjNFCmeMqir2COQVQcGHKZJ-Z9hkNoXi2aOwqCd36YzTAWSpw4IBJ28DhEYMGQvf9KAl_zlqQBavNFAANqcZA2ZrussRK--LPsXXSCHFNTe062a_1H0kBj6es8YUyIeRt70cJPz5QMXwKbN399Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGzVuc668Byk3bFRB6ppqrehKCr5Smi4eQKbncgtOzdQuKbL6cCVJhV4OK7U940Edv5U4pYYn8PqdQCsQ_-xAJTNOKmkSQ87fuRbigxonXdyLOiP44UKctTB4Sif43vAgfBya7hEsPEhW75iG5XQq8c_hdAzzPfS2nbia_SauPzO5vQpu7-ETJljMOqSWWrt7r0yeSNXG2XRIAjVBq-40zUeqeBOy8_37LV4S0Z3ggpbEQUefmf_hJO-_ugIVGnEJPKnVoVXSAs13k6HZqDEfwGPJt1dDOM4qtVCcrqbBfAN3YazAXwoJHshuzkYrP6foCOOH2IzOQn1ClkJRtTrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0CC38tcN6sXqzf8RgS_71h6AfIpM6YAIlMPhclBrdgqKDbtBALm2e1XunEVV4ByBUsn30HTQhFiLFq2QYMYiYn_rYwKgAmYsM67fNoXRRqa3rEDcPPwlsl07lTuz0dcYP0UOwAx3VGX3P2HT-n5whCrj4B4vYLb8uVBjBtvO5EbH0Mtqreh1d1EWlAhVgIH481wqgbeFJIgqokV8_IGLk6ueeIGUW5h2EOt1F8KCHJbdmFhEVHep6B1__HFSiqF1CFr9h06MNuE7J32JqSCUuWrTi0MrraMAcYIvcwMXVVj14XmYyLza2DTtRWDdeiIfdAVQKDg3QdElHzl4HPmvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czkayPYveBqQzKnSOgHLAnHUuaQvLhdrPccfQNbZTnNkvKV4ds7o9RS52OAJSGI2oTvqM1qoirsidNozyrEJ_JLRAJ7eTfiKDqmkImESIup7pmnXTGHwVNRe_GKjEcF-gJKVB1Rn1aYv-Hywu9ZbakZMdRvtkDpaJj1BBFS39LbrROWUH7aqfXgvi3tzpKN7l9Ooinawf-CpYWyu1NmIdlv5vpDRlSe7EGos6384ls2B3eMPj0DX93gVqBLn1PpOh92xiIdd8AdE_DjYknR0jr6bnvzwAj5DNCgeWwXwaGw7nW__Ne27ve7RA4J0fQfAKGdT-hRdGbrSGTwlwjajzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlGU4nLYsVlfRmsHAGd4PMWX3T0XVAjcKvOF94dyq937TfLxoEx2uOgEGE0t4_fxNcPxL7XVodU-NLYF0GsV4GRlClYzwkc-NvYXw4oSfwk_rJglvLhXzPqjhKyHCN46vftNScwn-qj5jOuXkydxzR5bR6CuD-ZIbHWIs7OSg_jXnnDR5nsIoCqAG8nDd2N-9oqa3H9WfAOTqR0toLC-14wMwvFwpEAZ79GvdfMFS4mQvNrQBMgktTFDHu_q64q3kbm3mZKGmUyfNhvk3MDqNDY_Oi-sfSc6qSgUnBes-dZcnWT3knpHft1zEx_1Q_YCclWLqoRNT5bEpwkGNgL7ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ9Nfbve_RQaXU7bWorI0qoQgdV8k2mrOP_snICf_5ovlTDgbU5EBeqhbZQ2ZNcHoxq2BPxSYKjfDNnnj5zoPuxlHlko_KxXSDx3J-B7AkWLUeiIyl-7zt0o0a728EsYVfGwwFxQj3XQu7BOUYEWQMSoUCD7b0uuKTXw3mJjSbFRdGpeymktQQCofYztptoCL-MAl3E0Mhp-mZfhu0VB4fmehtC4UiqpJb8IN1yQpYZJMl_Td-BeiTcWEE3ifwcsmwEUmdk9cZNJyx7dLOnAoN2xsWXkrHDmgI6DyzvTdhRLrPpn67Ax-LSGTouuJb4pi7sg7-ux8OITIgyJRmblYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSuqc9cmWIM-khF-Xm5QN2aof-Tf1veemb65sQu8I-KljLyzllLpJt6GpS2c37gat0UZBMQmJL4l7e8NfnE9qhm_FHyKQ_JDblUhOdnw_KTD4bXg70nSrltjR-pvn2-7NLDZlsQ55WxsjLktZiX-9FLU8RuQxwVWp4rDR6a2pzr0kfLWiX2UN-muauRKCAdA_qcomntAbi-AxWV9b_-opLl3bkLxo9lRg1LhF962SK6Bs99cZLJKSbTCR9LYQav6UAfoRgdFerH-Ti-8NO-VRoQzwwcn3yz76Z6rS7rNVvudgjkyFB_CoI-T8BgyXdNS0CNoYRzpilIyANLYsdRYfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqAQyzjwnRayTJ9XSCBgVJroQboytmNzs2-7EIw_3Q0DfbCmngDiImlhH3Yzt4jnN_SoCugIEL0r_xxAlupg3QiL1T2sne0vLX9GD7bisvK9RHgfqgSRFRHadeXZX8wQFd1hMSmR6UsXGYF1gg3jl5nAWU_XrBvd0gx1zdl9iubcYc0XEbLkNdg1yfPsHB4JGjffaA53CRYCNU3MAzvspxIVAkPSiLv7lGDotL0IOkRGczxSclkMrIQCRC3QgK_HVb0kTPPrD0uJM1Adm7ZNUpKu4U7Kf5CG_7X0-CDictklJYXw4U_iTImeqhFgG_lKDindvFpS_pJY43jNmnpbMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brjNkElfPHIEjxiB8PNNx9NrlG0ja7Bu_a4Qlxeu7Qltekn_OTXJfWQ1NpCygjYJOp1iSvJHoQs9PxqpbcK8tgnu43aMWGNRlJYNHh06Ba5xpg-YtkJXXSGD6mtNNbhRyb8KbQP7lxxWDOvrZIs-3xegXJPwBoTJeLAXSyZADBeJVWJUQLfNgzgb7HZOlLBS9wgKg3Graga4EJU2EGb1sjOlzOrVPTMQB7zoy3_UFq6j7TnRG_oPZA-JyT0l3mNu2werTgeqrd_YXrQwI856cNikvZzIGDGHKNVe0oluo_dqBJqHaWhQbpq2RSrlgE6neED9P8zFmmpB3CtvgmLVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc6E-_5xPq6mZsxrGmqBLOgCMjMWeklp6AyBMJ2d5wJWmtvXGxXo_AnZdEhkpoe9zFe8Y_M7FEBqlApJFgtoOVhNyw3Vk5mrwPg7DZ1LReqEIV-TE7URrRNasrNMEt3Or4SwZIcw0e1KR3jWxz7jQAK7viGk8Nhlr-q4MkE5PLWifXoMx-0IUxxOlEayMjR8fL--wkmWLBkplnPQFXaaPobfOkMvUc7u2JKMXrQ8f8EQ2rEHKc4B_9dF2me6mQ43Hht9wRAMXtGSOUoyNtQWcc_bsOcQtJj9GpaegAkNSAr4l0jaRTu3edgSmQtlkB1Fw_9_LPRjjACrG1dbqiIC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMLt8KoRRCV92OmZ_YtBBqwuq6IgiMyOV_ijWIXZgn5lBYyyhVunbuG1OT5U7U5fldoBvvmFu1atmYqyIfg6Bwc-SX9T2ciRLccODbGyjteNNSEL41Qu_rSaQ0vUYAKvPWzQ_zipSby3s9BmCQDxjgqlIxG4hn-q7DRK2KmTdxPhzGT6R-LwQ3TyDUQ46NawVmVOfy5zoQtwtIfo6bNsogl_4CagjZufzpY5TifQQ9DT8q251uG3mRt2OQxdCXq5JdAexa9beK8ye7I3QuHgeidohMPGIL5urRWFTd-CMxiquOFbsANCAz6gciJHVLCl48F289zbLLbNE6-5yp5qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dqo4BCHb-FLYV6nu7ZOhsFTWyNdnd9uw7XMO17-8ooKjFcX-S-UdDcI7bSxEair_vYbPLIxpFvgDzzxrAlPqdTUps8N2P_KPZtYwzP3le7X7ZKbyGRRK0Yf09vWemWCGjuQxbP5de72QgOg09Df90o4Hq2TbJgGS7qSEfF0hi0UTFcVt5RXsPGwg6cl4bungnCJtpXXMESZaZooH1pAkyzdhBNQIRvjnHtsUOdpPA7wi8SOTtPZe3ivQqVRg8fxwy-sPIva8k8tYIqBf0rwDD9GZ0gKNynmJRK67wmVq9NxNi5jVtUdYm4wwKn4FpW2wq6rSpZVVGIvfx1NEW4thcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sks4RWSSgL8V7jkuBBpRK4INnIlfoWlQYjoCIL9agB5tmMjRCd-rAfKLZLkQ3aAxoMa-sMrTr_KWFz2_vLnPVPeUu5kWgopHJZDdfeXznESB9O4kBRRFDJWcxjblLlIB9ZFxrf4GNtzqzGcve8tDooyzdot7z56C5odrmQ1wKFrizAi53CiWuk5MSUbdeB9jp3Q7bxbAznSfpujqxktv-FF9r76MA-SGGREopnA3_ngVEDyzgBkYEftWsv3MPvXT4lpzBlUYnfBMwKqP3l5mgxxc7L1f_JOjM-pHDjni0Wj0oWEV-HpbLJcjLjPzBxalACWONUrCXpEwlroltnpmTg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=IFwQHcXsdqIUL2NFIJIkizWprsmwG5BraQKMCJBnvyF5hAltsvmtrhqT-5bK8Hejvj6_9v4yfzt0KTojgo1GDjDRaSHlOtlwx_HHoOHhpKemoTltFOy9tKY9bFmg2Lgn8g1WxLTaaGj44Gg9V5nBBBvGUm75fgodjmo6kjFxN7mdnR9Iwtr8RomUl-teYztxMyLVpXGbmJ7YK5-8O5gVc7-gl3JOvSkhM1Lsr0mnmVZF5MeMNDmDz7KJ5JUrZf22a4n30-2nFWzI77bMpDwID4y550rgN8ogGnoJbBiiTyOpxG7LpycN4k28skr4h-x8b9dtUQzgFrK8ZzJo6qFyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=IFwQHcXsdqIUL2NFIJIkizWprsmwG5BraQKMCJBnvyF5hAltsvmtrhqT-5bK8Hejvj6_9v4yfzt0KTojgo1GDjDRaSHlOtlwx_HHoOHhpKemoTltFOy9tKY9bFmg2Lgn8g1WxLTaaGj44Gg9V5nBBBvGUm75fgodjmo6kjFxN7mdnR9Iwtr8RomUl-teYztxMyLVpXGbmJ7YK5-8O5gVc7-gl3JOvSkhM1Lsr0mnmVZF5MeMNDmDz7KJ5JUrZf22a4n30-2nFWzI77bMpDwID4y550rgN8ogGnoJbBiiTyOpxG7LpycN4k28skr4h-x8b9dtUQzgFrK8ZzJo6qFyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWGcdzsbntSxwa6QVCMVJ6Zz-6QeVKMB5D635qxp0i2kuU0HDF7L8m35vImEUtZzWDhlZ-jib2c2SKzYQKsszmBgHLiUUlykc1W5FxuV8OMzLhwVnYsc3Z6xdji_4AfrHnxLvd45nxGoK_kDGbScnSb1_wgoGL7PhYeHcq-8oMCgPV1X0E1XahS0mBDdlBNbOiYdHndUMteodkwDPUAzBb71Hx3OX1jGPwgnEKLZFQvA92GI0aef60AklObMoA2v3resyHSGUsg2ex6gJlaUOPVmEDh_6zhc0zD4kXzOgbOn8YJD_W8wP66xzcoYam4zyT_CqN7jKi_2QGWJZ21t9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 924 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltuRBZMts2sgOf6oDQAgsKJTmXHByrP6kI8cucGpO76pcAaeh01Qf24vlv0GsM0h23S0EodPiFyXeElk4wSnpC4Xm0t4gEqBxOCBPnHsZ-F2ZD45YiBZy5fMj1CUTobgndHvWKI18ZYTPLPDTV_3MFRR09wI_7Y_NRlWmjJcK7a6f6xlIC7CRA9-z_hgjvCLA4yCHHpmifA1GY8DYNxCKFHISS92t6aTXY1-eUAwJ3kEDbp1KPZrFqIf9c5K5RDt8fc704EqU-I3AJleJDlwxcMOh9mIvKGYyyDPQsp9rtKZzObFqFkJ-BF-E8DrHzRCQrIpZbLE-uAXU7iB9APnhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYSb2OLuPpajVurxhC8ZR91Fs0P3JyBeZMTHaTW287lCB35b4j-oTyRkK7hI2wZaUZ1KaG653NMwFXvhhlNBzTilrEqrzSltVoegZRJe2_XT_tTtrPBNQDEjoWacQ6uWS4L7ZL7bpKqxu3R2oUptXdEFxucX3SX9OgTEzNjh_y39mg0bXrIXTh3Wox57ET8thPjKL9FG6h0Ox5zrspwc5eF54waAUHmz5SASRHonlb2jJy05JZeyiztovyblD-tZfj_SOc5Cz9GPAbmNg7tZHuEyK3Z_9TsueEwTt0r8GFUY7VdXrfICXqaxFPYi2q0ZLFinXa-40J4_5JLURPq7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_FF73ITnLkB_5tqonqXTT9Ar_8NvF-t-nLJXcyB-dddsYbVHjwRoM5kjseP8i_Z20L39vlha0knPI90rici5wEwCH2jXM3xUl6JFTNQ9undQ9Gkcjdau3Bl8Sbgs-YehYMmvLughOmCCqRtB5KlwQlJOXrWFBzA7vIG96a98dSyPHtYa7ZdTy8ma_zFv1WgG0jyjrYv2DGsGDbTcbGRnyeeUo-L58XNjsDcHSW1CJhujNWYlid0bzY2mbbrlM7aQSKFf_8LdiCIJuC_APZa7QaYlsdFq66JzopE-w7EvukEbbJrgsj8pGAWUah-2srK3KEQDAip2esDu1jx0AkUIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dws6vFxTzjl58-fn8fpR20CUOn6zYc_6W52yUNsLEiGELvs_uEEWwOX-sK6NMEmqxhKIsKJ31zncbJMU63Ek_W96P9jbNph3bZRMIOg7bCCpg0wiTbPYPyawnAjRH2qDYlVWjHBSig5WvhGN8-hdt-h3cJ-6JDEwP-418u2NC4cls9w3XGaYTqpYBbeGKbW6yPXwHrIEGjSxFwzufhr8YC5cO7YzhqBNEyGo4Ghs1WkEeP5H6u-JZqENqsRCCgJN83_tO25_JsaQpcVyPazEjKVqJ5t7kRA_mFFPassLjC8ugMpxEiBv5r9O2wLmymCtjuQTtsB9wCltmqBSyo_xLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKrikMWUzVpBCz4jjsNTDCKV5UIVjTdFk3R4USjS2MxvaUg5p3l3IEXz--netao_l-oOK9NLGVOBkXt6JwgzCJt9L2N9rFWnHH0qkYr9w6Daq6mJc-MU5tRXCtDW5NSFqU4X6oDT7Fu5O9FdZVdwnAWVfYO4O9h-zaFSIyiJZ4E3tFvVRx3uu6ejTZKN61QPa9SA5J-7IGkqHPl5nT38-l6DV6NQf_dmedvxsasvEs0xhupkhZ4siUWC1gJHLodVu0swOWrklxbtXZ3ErVrIaRDAOjNmRLrk26GLG57lH1N0T0ceLgLrXDZwLBAgET6M-W0RwjmJjtEs2T3Qr5cgGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWAjYhv5GB1vcnojanncxWfdxh6BJ9K8ccXQkCzRPBB_2FpvkwVaFEDJLR36Xicw9daQlJrkPVbI315NytFIXidRCK1SwT5xfIduIRIWJVOQnI4VgjAjbC9eBdVunpDMIr7sZq7wJG56C6VlgCmAQ4I0hwYqrPUbYx4VTMCKJj6gjzAV-en9l6bPZ-_jfQ-GGTLuEzRdHwZEkdbzgJkTSTymiooEJ7uaek-kjWWatM818Ww0fWRYz4LNDqoJhNCrMTXK3oh3VoyLhIEL95F-9vmVGSIrCXMpMN-f6vK8vf95anYtQvCVHeuLO633ZzRJYW5Be8-oOVr1iFg_YX9K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABt661voZLIBj9fTMbDwxhdOm3bVrqITBFWzoKC0r42HTiQuMUlmdXNcUO0gE2u0FH9x4RyxmysHhIJPtcFxbjvyKrsQhRDiVZUNhQut8DyPB91vcBBirqEYYFZdmwtNc0cByXuRs8oY4hXb2zywiOOAnjJAqiHEJkcSH1rk9hplkuq4ck5cb3XTdTj9SkeIk6BBwS81DX2czdbY5EEVqrUYdwUFeS-ItRpMGUYAO4cW38f0motIWv-HTl2eirdG46F45gxRMa7lxfxiRgnlzKMhnzDwuumf59-DLuaUw43mj77JtJl8xcwwB8edrzNWu8jIuq0PMcnY-FsvhYBNGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDBk8DZTrb59LWTza_ZBAMqx-yOkEPXp0DcFzrQ96-N4ztT8OGNQJl8CfL5w_hA8ylvh-QBS3N1M8YwraB3WZ7uIFDTveBZAmNiIw-1Dt6VP5f2FexXPRbdKnNcCbSSwrArQ33xgpJDi4EsZ9Mys7JxzUW_-rlAW5n8T211VQIELD8VFCssDRACGIsbEKvoXZdhUV_98ff46WLAVh4I7UA4OLRuduyB29WsnUrBuX5EdbRBf3z2PBNDLzeQPrhRkvhWSky-H3V2N1GDV4bqyNmB4QFUf3ol0YUM5kcDZ4l3XZWI6floHtLQHevj3b85scSlS9TZrKym4GQnLnGvUfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvsm6uivlvKlpjK_tlPs0RZVmeU0pZyR-zNY_ACXd1wDQGonR0XUpl-1J240uR6AaQKBSbOkHo-HtAFyEb7pVTTW6qDfbEiqDzLRwJtElJ8GHTHiHwrQyLfN6gLTAHMrD-kC_ZN69xBNHOAGh0ldU2TzxvrlpOk6SPy4oELI_taP6Le-CMFvy8NOAdH4sb7uXIXkcPoJqeRx3Gs6nRDuwSOhLyHzUkDNVvrYyZsY9eHv-2CiaaFUMR0648OGIMB6y8ZZEi4iNQmxnomTuuxxd-d1aUdh2fnpYBsFDpXx7upSNXlCjMcobc8ltuZg449IL2GHSQljWXuTRveZaLcg9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQki9mvVJqKOTJcNXf1dIjrubVdtX4pebp9lsVheFSLq2zyoaIzd-yOAvuSBDfFnG2jcY0lY-uxScIt-jdzYk6JRulPTQaZoVOKirLrOTeuXsC0-rZImr4dGKclcd3TVQEO4zDjv1Z5RtC_DyylOtaLtukjvKdfn8ky57BqWnVZPSdvsDIWv0LhLMduoTuZek6el4RA6m4P_X1Itg6zsHlz-fEFLlPUvbVMymfV-_cc5vl1n6KhzRzw4O9OMVFrb2j03Xz0mnY9dsvxmCAXiF94Ay6IFzFCt4wIIywGYmOGYW9RHtEtdDHv2DkUITz-aKxEBanC-qI_Ah9ROSFJUrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNXwnBzR1_3f0EVNUTyr5XpdmQAbOT37PmOCsEAr8frZJG37147yGMhF90C_qQNMO7_WZLG1N6NI3mlfcKze2I79nsVrkgmYRip-u3Q_IuzPcsF9Qms-JVA9CMYIxTjXKnb-ZAKfQPJPyp3KY7VJXqw6m0RTbzWa7i-XfA2lRqazmv8WYNCHpnZ-gRxnO90VDznFeeO2S7BGwVbSmeiEZxAW-7AowhWAgYUSVEUEyzuhEtIQOBxH1SK1tOX0sE6NMWQnPgVWzWKE7pncw1bjiF6VShfDfDgzvpTVAPto-Q1rcWhEy2soytqxkRG07fkiiN_CAEEtzdMLtx244nr5Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhBFWQ0rBHOG-CwQc8iyu-z6YarvIt-y3tZ5tVEm2Vtk0fR5bk1F34crBm-8zTnkh_e_98ctwKxCGXVQpAuMA5QP7Kpz2fG1gCzr_D4yCWugCFr44jkbs_FAkcxDByqT2V_9BwEoz63K9HN0emauKjbVI8d_1G9eD6M9vDCdWk6-5xXK_Z-0fSsalQOOvIM1i75iuhxzUPLzAwq3RobTflija7dMtARZSKTknb2N4Wgj3DrHS_y8PTvqqVqn55zzCoTahoc4i7l_-6m-pg8xD4pwKrYdCSismT_62wvokdYgUW2TvSSXrrVNipM0G51ELeAb50H12Q98fOoWt-AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vubzKeYEW86q8WCnMBSLBP8WDXXfg0KlxTmUj24MfYqgS_Fk3LmcMcd-xw3qMIFANT4l2IlhASYUMCJ8dQAh8onMz5emcTAI-eUTj7sg1UTGUroLBawo2SFXOfoOfQWFC-9GkKL0Khq_1-NzLNIsrNEc2yYng_ejiNn1cy9yctvnY0LibjFPWJHcZUXv9_leS2GzmI1goLvlBqo4qv1wWgDDCOYZsIqIdXkB74ai26s9tTG-rqMwH-_tZuzlK8yhwQ7_-sY9uOik1dXQfDPypNxI8vFzl0hhb5fvK09hF9F75D4o2yl9Qpw6yO6eS1UYbqi8ciPyd6HSURfokcHfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjlFFgt4dbITnTi8nvih7WY7Hvr0X3u6kaCnGkY9AA6r_PrCqdIWVAMSb0XCDRiSehmHXW7hCOy-mqu-Vv8NDTowTaEsyaxWk16oECDALNguC_--O30piqBsV4GWXpmoKnQBnS8stkiSDftT15tP2BIjWPncTxBzIMy0diWp50g3AO_5ZINdf6ExUYYaZyZ9Dt8vF9zfqDx-S-2S_pCtrJ6PeqbcQ2fFkDmnsLOn7eYUHyLMyEe-flWzxaVJZ1RjoUy4_j6e897lw5fk1TmNA0O_y-qHief62zIJ5W5-eCj3wiuU-t8MTK78bs1Cz71EcqvbxlK9rZ7_b-RUaCRyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzY-Wr2SDMyPtSTrXEOWMIB9j7HV5-oPHd8qNIh9JO0NnIQDWU08jArBCcoYgU7566QU-N46YpjXBOKh0m_5f2kRfMTjJvinhiqnCoGc-hvjl8npnq4naYm0JcAzM0-uriaSP-P7AeK2QsWytwcANWmAXL2_DrYROAQHpv1J-fbvhaU3ErxNT36En05LdcdWL6p8z4D5W3Xvguz78aFqDQ7lLtKHPYOpakQvmLcnU4UNaYMWPMcUaEo22nY37E2SVXSezzV6w7ZzNC2Ie1WjhjFp1LhSQVOSGeHDcb-wt00rA2GFeY0Hz-gxPeZLgXa0x6V3pFCpgsnBKSijzS5BVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVrk5LrJleii2AngnX70DRT9raqEzgNHfcE_AcoDJepahXfPNZi0HYfx3OS8DBK78vYfE65QXrMDyM3KzmYIrDBtwn7jYKnNCdfrbDN5cTB4jVcnR6VRRWani41bSgVK2p70HEGQvW81m4Ja2iVmYK4eGRg3jfxAootPu2TOkhKys-VDGLUiEWDh9wQS3WVfw86EFfSqUcbNB92xWHa5SqmtbXDxlCivAhGz3ceez0liNnLfVmeICnqoLBXnVJ2dyIVyNc3b43mvQ-YRHvCS-smkwlzMswAhyonaRyvfvn3mdxI3r8YsVvoqJ8QVRo1aIHJM70VZE3D05vMWVJDAGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd8PC3xf8pis_kVFQrbWriePJ3E8-Ij7SdzbuSuiCNRtIGp2ZiQnV-1HWlNyrMNCenW5xFRW2bQcvRwJcMYrRUY-az0C-dMhsw1wg4k3L3GLTW85yui3-Sqw_-AXsj88-5srKyNHR48hOkZtn7Hfkgu7igS0IKfvbwuGT4y5_vdGEFBiJNZHR5z-jtz7lKeW2imbeMFklz7El-TM4uA_JwKulxU5AM2sceDO1nx3kgcDzqAFU6Xp66YzYfWZQlfYH9nLfGdlxX-a2QXzpy73cStKaxq25BrNZgLr4uj6eK2FdBPKgrMYDrUCW0XTv1nyH9Rj1ZzbT2CHKzegNx_n0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR8uEKfp3yuPzhG5TXxvVtgkVWtOuDHwWZGisFZjQrSuJIEeENT1hk2BSjAeAwNqCkas-8HIlqQJRNmA_eOOsNApk-YK3YO8XBQlvrLeWcBCHorBb8qUek6pyKCRFXMzrqSiBMveiWQS4a4BsaX7QsPcToSwWP1rZ5wYoPvrCAbMZa_v3CstBw8n8oRj_OMOTB2fWIDId55OgGnkz-iCHED5Qyy6Zv9hGdLMbc7Y1KpDSRNBiencjTtLklO0yZC_qHj3mjZm6JAfccB4lHPAD0diiLKXhkW4-iAorZU7M6oppAMjihS-BETzoKQJC1R9xEkKFBQPUPTkJrn19zD6Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIY1EZQxf9AHNm_xflUqFFDOCc9HEpjU2dKJ4Xe5JbuoQqPhU1ZF-7IDGZRMA3_pUnK2jV8X-wVb3REcQVjxh4cfZmnDlbAMp-fC0Cl-nUCNv7B5cxP8CQaE75FWDwMokv8QcPOyIVM-38iauB2XNYMlajFaVEDksrAaAWTM6TXMuoWJ21tZP9QYjVYV2YHbIq51xJHCNdfl7D5v-aCT4kSUbNBuFkQQ6OVFtBMsyPacaStU2jcbchk7ThkSTXQQcmXwHb0oB9VSgRgzq3TjkQqyS_nzyerShi-toyh6GvI4xSf05Slyczt6wvkEwgJ9Zbquw9z_R5dvICme53kNqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDSlUGcG_49s28KtxogrpDWfaUTsBDE2oaFjpDby1jNB8c-Ds7DUdVos5Sn5SSIhR4_aVJoH_rkRfvChU5Bsz1t7hJxAhST7NZd6sv5bQ4WqfwIW7TrCHVZ95sF6tpen7ovG5ukWPi5G7w1gSc6E0pZ4jAkF0W8MFVJuVu6gUF6zwDZ236Lg3DW8WyvZiw__cD_XJcYjdfy9Dg8UuQ0KVrWPpsO6PLlCHG8UTkdU8FlnBSYw_CuGb1vkPevxvTHO5b5tZ7og7nb6iHEyyUM1DzNPVU4dHnt3X-BAaZUvNqA9nLhToA6e4LuuMvrvSC5vdHqD3qUPfrUAyNtrV_JXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP4JGBYy2z76O7bfCDIKRfcx2Y5RIEy9qHEAU7-5_QUYrZRukU0UWeGmNpgETIhNSBcHmHVz6W0oMzTH6aeDc1CFeoVH8gqvkmhyaoPprB5SG-0ZlG53sXJ-QwTZ8j5fKsMT3WDu1rj_GgpNYDVr8fmso7UrZ2ZM6xKPHfQwoVrivkGxOInvh16TwH5tVf5A8zml1rQDazfglICr0_YdR3NSzb8qamg9LfJfeiv-eCFJc8vmhqc_uhX9Uutqaw70RRXi0osTJ_OyByX_NenmvsInzzzwMsRZ48KcW_7ydwuOfk5ZlyRviMpNY_p96D8I1qSS3LAH7Ltr731GHo6vgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbzIDUpijjS-GowU9G6RTGLCcVHTIixuHnaY_OVx2hWB2HLvM8y0uBt32nsIkngoZ3Feaoa70yWP5B5DPl7xdVGTk_vaVvuP__xQED9wDaX-cqU2l4ZpHbF64TTeDHVncibg0VfhIE0CVeXkQ0HgL_TDkjnipB7A6wTy1O-AbhBjSf6JFwaYbui1Gn_icCF3qrUS5BxY15VwhN-YiEbE8AuxUeNNklLI6eEhTknsEc0F7lMwLGokQWXx7OFQaUPGX_R1RzCvmiMU-bmrpz5iVPTVVLWwZ8UZ61RYNlPePCVSwHuTMfROCWEiBNICwKBJYZ0KIaUGXqegqaXUHe56gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlja0-xVRzAFalUbxSTkM4bqJQHgRiV1H_HbCotpu1HV3fBhQ0PtTMmmh3deH9C0le4L60tr1HPflv_KI8UVvraqvDWl7kbPYd695b8oyf_-gyQKFZvril-53G6xw-LZUwtrQLX0G7xPPaE30nUSK4fv07xuaFRd-bgfeHKVZQ5PX1HocQs_M4EtnMgAqV0IMFx8_A-ju8-GYzpa9mwJu9r22nXFKbq10UHHn1AElGQEdYymIylIWW2T6qi9Sd2UfbLyr7Gm0JVCwP_GzvDYo86QBzd0hebDgLDm1GyiVtXOrjbLXomOHm3BfEcFT5SIY-Mwm8x2OSkDfuqygYJ9pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZYJvUrS69C3_3N9uVWJSiPESmRYHK_UXSS_KenIYA_KBjtBX9ZqjPjKpYe5hNUl-6HLozP1dlW_Az4FztddZuMpHGhQt5CqOX9IuY2P4Twyw2OUEqwOcVHfy88FIaCIlI7eWsorkLUojVt4IDZwUx2Jy1HixY_QDciyCGgMIggVS0jNgHvBPHmjpKcXJp7Jt5jvjHt8pcPKVvo_gjNvPHLUGOb49EQDtkdD_220nE0PJNcMkIPPAy6-knaPhJDxZbutzykxSURhpQKabLWwl78-0QFPEE3xqCN4Ya-U5q-Iu3Cgel5DQo9OXpDXJWpOxygBAOts8Wo4i6nsuuNDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wd5Q-XSQrMrApDbRkdjZd3VUu3jJZkBRvm74Iu04gYfS-WOuEya2DM7ZmOu9qbqTpyZ9Y6arymB1ZE7IWLr4d21M2JcZoc7C3cRhXppNEJJ5KUwM1rh0GOe0cdVOiGEr0CBwNKM7Jpd39VQEn3V9fe1dN8VZX2PzIaNlZMLVXgAvDlr9VQj-xIIMKnrFKS4EZkE8JrvtSUlMdKqSJCVVZJhxk1QVPwm0SH3N1txUOTF1TxlP_8jO-hEcNU_SmhwYI8P6gt-Y_2NMErV0yX3p5DEHbkbmBEdqEg_kBeqwWwEQK0uZzUicl_VdVz-MhdLgUiKUoY8sqyhmsZpnPZzkOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIPxzBkbIxFzcnWXDruhKjDpZBGHUtIGOTEs5zvipE1k6fHYkfnNBE-K12PfshPd0zsbuVgKfKC5w9-oeVq6iv7Lib4jDUAjgowYNkt7lYGEDkMLOCEtRjupS3Qm4ezIvv2FrXTeauLFEu6o-gDV20UGFUPq2Lo3PzevBclaeRfbiZ7i3IdUGxsy79Zhe_UvFSWt1vMSsVkjDP2QcJDHpxdnIfypo-bMJ5lfYCJw14UKhRxerQB18Tdg-y3OwixCVcJu8u1tCaIHu1sCbJqzOHjP65swmStXr9v8SlsCRqP0eQFmApz9LH1Ne-YhyuPzkvA8WoJ1ysEFJoDTZePhTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMh-V-4c55eDQOUyM7QPywUVbO-im058irNjQ2K4Motj2dT6qaLAqeJxIjOkUiVCFXHGgRRzvoOHzSU7dDEBsXOtWaCJnbuDwoeoJQlH_stphjFi_yNWCfMXTne7cx1A64N02RMLuHMlXsld1apsiOoz3LMzgqYjmwvLkyowluBzFO_smX6gA4-8rCXaRbNd-FWrY6LzV6qAcWCkUSIEZyIVx8TgPlKtgy7EU_c-jj-UUF2blzESbspeq9roUv6_VE7yYPUo6DLcYCROPlg3OaCH1eB_USlG4ALgki0nWoz4C4NVhyFLoeePeCZvF9oIPdYWZYWhp7sz6YtMw-7l6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSh67kCQzjpfPEHaDaK0TrIpZqqibmBIdk_sB4FCb1U9xxpYF_fw58iox0LePXrhO6vQ8EBqgBhn98adTgugX5kkcutRpcqhp5z2Bdzk5MsA-g_19AGuCOjRM2U4vFPiILauYaPPE3p0ECpV4lhW2m1bb-th-lDlYYr5Kxb_uJjj6n8KLNJ-CNmQWLhTKyslo_7aC-unSA79OzaYUPDc-F-Gz-hQXYrTQFku_sZyoJqwpMzh-3n77Db8YubM_HSjiuwJbAQxnZyiawpgGVEcERR2mVUdHQyKyCev5Nx5ZCEsQgveMtZDw-z-j41c43QC1jNR-0-FhBOkOXAy5nspDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meijAyrwqfKnOcx-_Hy7Pvaa8jYWq5fvB4sFYkNitYYS1CbTd5Q2VuhkFdha9KcblH3UactH9RSDoH7zLo-tOeJhyWHTw4oXn9jlfn_RcPIC5OREJo_zjwwNOqkyBc9DwwIuS-qN3dtxH9ZGJYKv2UkwWm4TiC3LYCu8jmLXMc2P9g5N82SGjodlN2uoPtU9wt4mbBkz9p9glP3HirXNSKRe23opsAVjkNZakHEvxx-Y1OpBc7QV0nA9HTMtu2y2Py2xXnhPdSo6NqtvKhFtnbEkh5G1x36OhlEh_2oTKgmawAt8oNZ1uEBdpGBE-m86Fmqfj3Wk7ToTtrc2ai1mhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoja0GJ_FzqYmYcawPI8yuJpeONA7val-YHFK6AqRUZPgq8e-AYxqPF2A0FuA6UNujkFDKitYqtOkyNbR1kc49yCmlioI9GAdF5M2GN6fYXBpgKfSYkBmRFJboXWmo4E_f1zjpF0YdHrPsYEqtoFES3puyX0BIByj0QXL1a69O43SCTFPr6XX7asmMt0YnPIY2YPPci47z6Obn3wrrFpB26CjWvHKzR-gWSP3x-cAt5Wd5sKSDxZyUTpYjfFrvYZN7XS4jWsKLEveaWInQbM-kIgagaWuoFZzfIxVSMqNvoF2Awb9Z_wx466eYKnaLaml6AII8nRzyhzbkhLUQtgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOF-hPPZ4MsDq7rMl9uUOjBWzT8JOPgbPd5ZT2laMJFxO_COg5NhODyP_VsBt8gkz5i18q04o5xt6LMAN_ltwv22ZI71cWCO87bFmExtiWSAsWqTW-NstS_VS903Wun04BccJzoNuX3MTJFILkx3vffR3U87zckC4FOzcn_YWaNoxZWf4PWEDtOe4n-qsc9m3T_lBlADIdhh7jrOHuO5tmkxMCvCwk8_sYnq8Gj1ZsDyXpqqZGSdxem6xwQjk157hUvjcyOCj4RjZA0jACLFRjqilUi18CkjPKGPy2vYV6rSh2eTHIfvXbhfXt9MY3zadDClELoYFJz9anyAmd0S-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQMDNW8k6wiFhEMS5OrBBtgvJLiyLdDVvhauieGQi-q7kP5J9DTKOnVeN-cE3-8XAsTq2ZE38Y41J8Jl-Tv48VFz4rGWqQhrY9j2biraI3GlIuuTBUHbI8mqMCuADmaBLuYMhbiVkIijcTATuQOT9sTWJX06o7Y8y4T-n8Rz91-qfWSbNJX8ACP6pa-woTNLwf99GY5uV52PZ7SG19EEukckHzB5wdECrlVFt2XBub0yt8Zw3gA4Tbj1jT-WNdWMdPXyltsL06YO_lmyvM_xK6ScRHZkHn7X9ERJzmGVaWOiw9uzbEOrhElO2ilDMJk5FuNhXBdnc2HOBtQror3Qww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6IWh5I0jsxj2tFpmuc-V5ynD-vAw52s6DgNQaRttrl8uN8iDfPLV8EjtuA-7_N2eqdbzq7HvrogRrmYu6i4ntTryIWTlziFG1CfxThuGZCLRlI7nzBz48xIiUQ5X_h3iCiA_e9dV40qNQPyDnA9-4J63BLos7EPOAwzJxr8ibbh3O7oE6Pp1DdZX7g2rYi2JvtxfClaXvDzCXzu7JrkHsrnEfc98WucRE6rJDSwk02x0XGkFhHXTAJmAPzK2YC_qkiJ1Q_EqGyk1Xm81VOvABN3jqcR8TopRaXdHkA14h-gmm1B6trEdMye-8llFADFLfNE_wLKbMpo8naTHrjzig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTQ9SOb1ws4nc6uDeApE9QHDLcBZj3Q2E87DJvy3dN287yZfIL7HNrrTkMGIaW3m27Y_ALpD7TahXJie_GPa0ycw888BVyaahgSH6LQRIkuRETF-BJJGzf4CEGyqz4vOEaPeRse0Edk3gzFm2N82KdlsKpHHMJD2-rW5m6nf386cdyHbhFhE3zsOVm0VCbfghIJBiHm8apb9VhECrFENsmDcnbIe7KOnnUsVF1Ul_l1xca45TwIJeJd_CJLiKvVHkgbTJVPV1iO2BbYssmEejxpjz0yl8Smf1qn6o5rHxGT3QQ3-SsIB30uR9nUDAkbE4LyQvfPEw-IBgk500445Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIfPjMAkk2s0Wy077ZKChSmM5EEwRvb2RGFgBLF5cs2n_0YOK0dwG8yrFIpHDN6JDpkI_V5EA9RoWxWbOZF9EP-tsobNNHeZtSEx4T6FIpRcMfjuj4DGUhntgRO28tr-koFrQIBGDw2JoOQ3rdzABL0bCPoILIbyBYx3RxutlMLhccRoGo0HobbLan5l82Kl5zHk3MAtdisIy8lszQj0xYxHGxC5BQ-cSrCUUCPZrz35B5aZU4NZfLPYbuC5eQC98r88kAJaMO0ib8w1ba6GnKwwd8SA_EeKSDflq6zvey62K5yJykM0J4EowHRteIjeh6h4bsutaEmwFJiWiLMUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUTyijfHlYvXfzfWz1elC1iqHiO0SNashjJH8pPa87CpizegdPhkkqt3xN3Cm_KifJZ7ZVo7UTHzEDHsSwGCZ2LCZuBWTIjKkZDhQ6l1A7bGUfTekw5tV813dwFGrQLK-PalWmSLAzj5lQPDtQaWfv225RQ4XdIQ6bRRfJDEpjwctiDOpyIlcwI0FBhPJE8dKLhRVcR1rfZ640t11olQqwmDHK7GwjqzxAncmrC7SNzII51KDfNpJTwjzUT82656K484egMkPQMCX6GFZVYcpw0_3TvLjWNXc8MgymQ5uNlAbw9oRZtfwlkkTwwh5AaTtGhPfFoveFa3-RMsdUt-Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll8wqr-0WKGY77Hh9Sd6d31iKGHc7TjDD_CEXVHnkiuZTInr6RzWDYw4JQtYEXXgpp-jgqEdLL0PgAZaCS4HL4g04QL0EBfXfYBDnVOEc7jyhWcSqj69pRtye5Qlh_kE8TVzcEydGouAdPR0CzKHdoTmeT-lTEheg-zcW7DeakYYaBveMwLIh8rH2pYjVZU49avtES31KlpeOnOymlb6shmYRWK3KiAaR7rF28MbOntweUZEFYVxiV2hmK5lUpWWmvF-zG2YVZylqTEHG8GaTWpY4YPYpfsnAW1xO2e1vNfysmCdE_sCQn1df-Xk1Da1izwOistdtNrkpG2xPTPw-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRu7G8RvQYL9ItW2oQ2eMiepFBHnEHagTU6M_a3DOY2jnGJdw0n7jxTvegYndPWrnSOzva2mO6r3fwGxhxENP7LHWM0djHgPnh1xBDBOjt7s__eVHh3mJKhriEJD-OyKYbhtNhSa8gbkCD0Nsud6wF-vjgZnY93XNModOLsZxk8sMD2QnqwbN_cgTjrGuHXpqk8o7oUKjWq5IYvQ0wp9IgBkY6CIM4EyK3KiCSlcoiws4zCrfDKZ637UoWZw9ftQbcvb24UVDnYywCnU8sDSPOVxQSf3mF9-vkTX35AWtOcQa0lb5zDZTY8pUuk9et8UYOf9cTV43HTESg21C9Mvow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKNU-g5BEFYKh5_NLBd20v4Y783NwnvhUVBL5gFLFp_rnyipeCxwuTy8afGVepajpN5rr2NQqu7Vc8O12gOWYYqud3ft9-fK8vwPcp8OjY_8dH-UvDwgLNW6G6AvP0NGY4Cr0dUl6ZJPyO1fJmu4vEJSQr1CKcqPxjI_sX3iTT0MqDsxOMCWB5uB35p2Z75_bfsrgRoRrASGGtRYhfT_5Nmx2mY0f6buqc1F5O9EkgY3zKlvcKlJz6Ysmh5aRjyJONX7X1Y6Kx__NAblDo8H0PBFQ86wxD045BQMM3xbqsUSO2gMYRAjPDEszj6e-gsikOxpZRckCDz7Lz93lVi2og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tt1egL1wPmFlLbKWvAv8IchCS9tk-fsK_NvXZ3O4DYo9iGI2_zwqQaINgmbBuJ8uA90zcKmuoo2NeKgzMX3sp8JEZX2zykaisIuUtLSg9Bl9d-tjrDzwzTmB68nycOjqrWqco3ESTPRQUrMmfWrxsWLOeDSSXxaVH8SYm484ki1avPUcFVr4az3-dFduTCl7czcUwmf0dE4sGqgxfhX1PwwUlav6vX8v4i1AYnATJyP29xiu_l5NVN5uymApypc1O3ORFX6poydrPjmXftgtXz1PNOm6PXN15jcCmujSV0i5e4UHUiUS-zSAgIM5xKaL4uTfXz5XWCT_bVBSWedSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg_QKFU7d105QoOjH4PM_mwYrL2rS12MUjnlNrP0OiUsRcj4bkLDUQYoYRMFtMm760OSUvM2C1YC-j9WZm82mmYyKWRZyBrriFafRvqr6nFUU2P_HK0MgsTbKVSHTt1C9MBgOTzx8azOYRUx-EUHUW1IefwEsUgyFy9mhv0hBTaDvh0uT1CucmOikwADVO5YN-e5D4bmUTfTGS_iKq9JsdtRQld_X8TM1aLjM-um7E0rrT3OnRBVOKWVXgoUCM7r2nJ_Q9B5gPNELpwcOOHZi0yYBtx9RhgqnuBthZWuiIb6lDhuHyejg0yzore5GbXVNke1Xg1WrcDBXIQDaeHRPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEZ0vqxs9DXa1JKW8F_r2dxEOizBqGft4MmiVRVivt9uC1WCHjGWRa6uvg-RXnlj0tDp5xZeL6H9GToyWtUvwTbOZh1Yuw_DwzXqk8ZirC5Bc_anHObO9fAs1YlTYTStui9qG4lSTV1HsMU_6AnmepzAFjADnJfSHW6_gPfq7UGb5jqsCzzcQ2PdWiqOaOaWtjjI9ON387Z5XizZEPAfl-4JMd7CXzpml71CovJuYMHUACdsu_Kpws9ofjBI0AsyFcOn6ld36_4ZMcwW7seiAyzVmo7v6VtbiRD3S1mT_FrrmPXXCezK34lmhnnQRKTYM2M4FySogcfL4rHnFB2bUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE4zF7Da7okIjFE8FnS1vHz0NBeGckjnbzMji42Ll7G-kTLWjClq7dmh587ISRbj9El7-782e6E6H9z_ylDmQJk8rX58JThupIb1QwRSuRMJhN5s6ZklntKbNRXVAOItalE5qMpV_CZjso5bSUktEJEiEWxB7zU_y_-EjZ_X5ipiLv0vMKXBntxNyERJ1qDrotUT7ardcGL2zfVxVg7ujckRUqEsvKESZlLh6VE911SDSKg1rX_YyCd37sd9-tZwzGdb4k0JpTZfG_9pmZwt_9Xtkqx-DfoN7V7JQxmTOjqIIrtAqMZxZDfjpjYjxUCjlr8EuVPDLRsWscu_xK5Y9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSSLH0z9jeQ_qCOnGl79DH6flV7UFml-6597-ixib6N-oHQAX8CEb-LP3dvKf2TfCt0fqC88Yczjv45VFybGsJLANjNT9MkMOnitoMg3StvQUuAy4N8ex0gdL-RRymyJNb-XR4gkfBN38L2ieCQFdOZrGE5gRPLRhO4R8Q6VHl0Z63my3m-5xMpF6JF7WOCTbAsHRMalaA3sj3UjGH3Yg-wvIACwdU5BkcRiS_O5Y4hANp02FKUt_xCd761juBxlTpus7teLEe_IZ_nirK_7X2PKNObkhf6upMNfgLY-uQWP1LCrlEAcCIU7CLsjm0glBg7J1nLkti19QrAzi_pryA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4W6OSAXMQZhq6qM0xDXueC9DG0iHQ8NUBfPaDGIwOVDEWSRzVl5y4u2mnYPB-zZdIQ3GdQDNDBileaeGZcy_pj4FwimQ4phR0nj1iYIn03CC0HxU1bKJza36EBcsOUxM2GCVJgMBKrBx-Fbof1dBxd9FU9jki9nPykAVZH8t6M25OuJy5dl2QlNV676J3CMAMH_WzQ3XNy0Tm0MoTf2QpgHPW6kL1pqzDk2L0oKt6KrE9lcTHfN0cYUwueKk2uINruCYnPXFzJ5Gl4xKIuGzHYWyaVFD1qbPK9IjSkl-3SV4ThO9-WFEPwf4TQkiBBjU6cyAJAAxrunVqpjvMne1g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EFfkAC22BMTONpalY3PHIkKAWcg0VUwtTGc2PVOA2cKI2UCCDHg7DF6454ZpVEzyJ9KYNMySHFfb4aRJLZ9ND0KXx_wMb1dfhtoyxGtl7xzcHbIps_L4TaFnzpTgWg5GL8xjgwcD-uYmg4FDL730apFg5nltL4QOfydDOCqiyxvCc6DvRXLiffbnCCEKtEKVUdK-VuwcN4FsZ2f-Kk0CHiFHib8EYmmFZJjawtrtsQKuYcOMbAQQDG_iwG29VZd48U4L_Zu_4a9-dyzI4tngWxjn6VdGPxHfs8SnAz7ieQs2CIl0WS6RLkX1a_A4bbKCvxaeUduUMe9REx5K1c8qOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EFfkAC22BMTONpalY3PHIkKAWcg0VUwtTGc2PVOA2cKI2UCCDHg7DF6454ZpVEzyJ9KYNMySHFfb4aRJLZ9ND0KXx_wMb1dfhtoyxGtl7xzcHbIps_L4TaFnzpTgWg5GL8xjgwcD-uYmg4FDL730apFg5nltL4QOfydDOCqiyxvCc6DvRXLiffbnCCEKtEKVUdK-VuwcN4FsZ2f-Kk0CHiFHib8EYmmFZJjawtrtsQKuYcOMbAQQDG_iwG29VZd48U4L_Zu_4a9-dyzI4tngWxjn6VdGPxHfs8SnAz7ieQs2CIl0WS6RLkX1a_A4bbKCvxaeUduUMe9REx5K1c8qOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCnZr8ACkExsI3XaDZkhS8XeLu_hTjvUQllkslfZ6WGWXMWDb0Hnu3S62LXa6AJaouhTor18fiCIWCbcRzqCdJFL8miYZWfRLmRBXBayfkYVERRPGeK0TeHjNAxFzMhaoPBrV8oo2g-Z-JY3tqGyEHBfLu7FtpAb3UQIXk2y4MOXpx1MjTck48vUz5rIbNy6U7z4M7_tX6BvIZCRPyR96Rqit-je8PTklw4IpLNGltLdGwmJfUKzkJFyfrGl4Khy6_jW91WEUrKP2HTs_zdqHI41SG4C9pcDj0P0WZTmTNFZhfKs9mTJU2bbRVwbT6-dx65Uan2TGuKTRcvWCw_-Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU8gaY01RokZVKOVh9aBBmj-TYcXH8RyN4LlJD460t0RF5ePKW1O72DKXXTayhf2vOGl45N6dy5677F1BNx-jz6kY9ZItU8hg_3V3CkUneJfJ9JOFrPF2m3I1C78unwCqDHAGOYtj1fHOl3PpJ4bU8A0n_FM_ETDkjylvcR2U7J1Urnas3BGWBqqyVQJPlJRARfb0c4JusynkQxzFf8EDO83FEYWWg37Aa2vyBx39hrpcliFvWjyGnukSuMd68vSeEhVi8pAa7bIxK9-QXclYo0rEsFIF613kQMuy03cZmnNOpEh9JhZFERObPf1sbS-XB-ITdi7001grVXPGTXftA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zg8os7L4DKDkcJWNTOgwX708gls79KCFy7yMwlq1Bcp4dJ11SG9F6LSTpSx4FpvNaknrFy206T2aNjawZSzLCYkZjVnf-C3dSW-Me7sUOsY9oautVhL_5yDSx_4vG7F-KLvEirG9xNpfE2lyZSwgvhz7g5bYMOI88fSN6Dp_npaACshKe_ulnGok6wZaUB44f7RCtKeRKR6BmxKrfuRRqxQFx90UxGucO5RrHbWRx78D6nZZh-QnZEiesEflbe1CiuQmxfl9JfMVC21E8TovgHLucM_mUmbsvZdJOerOnRK_dAUeqngM4sAFD_XCeIzmBfq2tlcLFUZVq_SUHsVyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9VcewMMRmSSZVW_BWnd34db4uIpPZMVequmVmGmX7LR7mcgARJyt9jGJzJ2Bz6Oqlsqm71t8edZQBxk3Qi0Y3ir814BqKIMl9PHdM7uPeqRJc6XK7WRoRS7rb2m7M5EPMXrThu7T2DT7AsxJrRTAzdgo0bHgomlByN2ADTOOi8P3VLf1NSgZZi8vmEAtZ4i_hzHKBUubriOheamObfztQcXxNhIqh7XQarsuCmMcxScAIDAVALftR6NqDmUEh1yDyvZoxFo7SXQljqc2RjAom8t0j4sKcTvQF8x1WF8dby5OOZd9aNUFAO3t-21dr8q2FHN0N9gn6sQ3WeuJNiLBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC21iu73lXxMnKt28AbCc-i52MWd-3Z-DvrnomEHAR2cxhqDnMcg7NNyWRSAJuDoRlO0PA1oQacuyvac5UEc9D-jXsssc1ki7KcH44sSe4KfiQbGSWSwSr6wiwYIYM3XyGFaqZmOofyHCuI5y4sxrLtGwlFg472AAvK14WV4SzFlzcPzmnVdoMUM2pHPskxaAeZ_7jsd4Ooh-oaO7UCJYslB80urMd531PNC93Y3rSVZDFYJesHqjf03zSXxYgARNsz1XUuMtKWxR8b53PQuX6Z286RmxWp8glhEYu5EeWyaB6a7SwZTmMYAB4RXvi-h_sP9KwQrAtAFpADnPhkQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-yto2_OjD2mX4li5xcrGRp2T4ATqVv9RRJgCrf4WvMo1aOIfKUI0E03NvnGwbHyJ8EYurS37ta6rbWAdOdGX-oYIbkvBBQ9kk97Ubw-24QlP1Mc1dISS0k9c-h28HmF2e5p5TZJObW_9CBCoqiiAs9Ah1O1ixAPGvPS5xc0IDRRJUcpbBmEBVe5rborHP33XePdPRbJVu1gsAKC4MjS-EwL76NRWfv7ZuoS0ouHB89ssEpzpraAcvTczHJQWn8sc2rK_09HSMHkBdQLscnodUQX2HHo9OJcfFk84e0DlOBQNoXoBhdbbBC7qrV5Kaw--hps1IZcUICMvhGPjxkUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vt3s9IspTfDQBFa-FwhnqQq9LK23zd3tH7i66sAFACXroN0mYGQG3pg61-wVQpo7PIalh2In3y5EQ1RfUWwIGnZJRakyGUMpTEgLd4XT9M45HhJvgdB-oxmfjiiDCEnInRYrsmGDUoO4GKY3IuWof5yVYUArxkGBbsMCNVgDD1kQoVcZz8okLt3zzT6Z8z7-kCGWU56ZlDzgaGg4uJxpnbBTWmYEAQkOxBanNuD2lQVAhAiAtZfSc0Kec4u3vCm0NHjSO2lxnmKSEXAWw98rOqA1TBGjl-5eD5W3pgwAIreiW6Y1nY0wo2jgN7_4GHMPK-CjX813ejmZg_rmtAoudQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MLhfBmXT09L3eFFKTwhh3uVJRVp3cLmbF7ktX9O1qULz4e_0-3N8TOWbRoWFFyPyGZXaFpsSFgre0BhBhtgzWpri3KhFopx2f3_K_6orhm72DhAFCTgh5XXmYtG-1Z47ButJK-gKfHFile8c93qR6ziCiHigdEgzAUKSAePAdISp1s3c1hHPGaxsUT9Am6e7bMJHyv4e-tih1bkvi3y_eXr1ctxG7ukg_r3ZpllJzmIPo6_GJXmhX6zYAB9zvk6F1OrcAGCjtYVdxERSISNhwiKYQ63knx7Hh2hnc5iE4OJ72L2sN1W8_L8MA6O4IUH_Prg_G-Px1oD1yIsJtrQDb1QpAIbH1IbuuChWbKK5IAScDM0bmjOZ5_K2IQ7T3Ehz1-AVfdJGRzuxyiSMDv7mj8SYME885Ikh0D0_yj8vMO-Y7c6cn129cl6mxDcdXXe9LRZVXxJ5YGojzZCfvi1ahBqmAICswOnOXCQmXGGqfCH_IYIElngRsWc1L3U-IIMd-VcodxgBqiI6s3sSZF--UbpXJnVFhPtTq8UkZyiEERK7ucFA2Wl5MqvoNzXQw1D6u7k798FLGXooOnKOYLdDQ9Aoz6HnVPNV0k5nmDJZLUMvtLDuMtlVZ_JLc3pha09qR_A1xJLNuhzIlxOWf7E8dQt7NHgay8neIjZrybuX7LI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MLhfBmXT09L3eFFKTwhh3uVJRVp3cLmbF7ktX9O1qULz4e_0-3N8TOWbRoWFFyPyGZXaFpsSFgre0BhBhtgzWpri3KhFopx2f3_K_6orhm72DhAFCTgh5XXmYtG-1Z47ButJK-gKfHFile8c93qR6ziCiHigdEgzAUKSAePAdISp1s3c1hHPGaxsUT9Am6e7bMJHyv4e-tih1bkvi3y_eXr1ctxG7ukg_r3ZpllJzmIPo6_GJXmhX6zYAB9zvk6F1OrcAGCjtYVdxERSISNhwiKYQ63knx7Hh2hnc5iE4OJ72L2sN1W8_L8MA6O4IUH_Prg_G-Px1oD1yIsJtrQDb1QpAIbH1IbuuChWbKK5IAScDM0bmjOZ5_K2IQ7T3Ehz1-AVfdJGRzuxyiSMDv7mj8SYME885Ikh0D0_yj8vMO-Y7c6cn129cl6mxDcdXXe9LRZVXxJ5YGojzZCfvi1ahBqmAICswOnOXCQmXGGqfCH_IYIElngRsWc1L3U-IIMd-VcodxgBqiI6s3sSZF--UbpXJnVFhPtTq8UkZyiEERK7ucFA2Wl5MqvoNzXQw1D6u7k798FLGXooOnKOYLdDQ9Aoz6HnVPNV0k5nmDJZLUMvtLDuMtlVZ_JLc3pha09qR_A1xJLNuhzIlxOWf7E8dQt7NHgay8neIjZrybuX7LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRjge-hA-Qc-cfri3Cod-ERbBbSX14DJFAM0tNXiDNRETdno1EunKLieUj-rTyH0BH5TeZPQpgpHwRB123BhOV1VOEsr3M9zRupNOvUE3DYS8othOdopOxTFj296XMci9zhvvue8w3khILG_snNxzmjlVZDFKj-w70TsC6Esdyh6XfvMxoBfRgPdV8Zp_DcuHnjfl0Ps-HKN6oI7MHLnwTEkjT2fyF-lLPkRdB3Smwkz4Gu__HVXK68lnhfRa7s2OjzEl1cNamipwmJyrWDa03K8pYPknUnpC-MEDDH4cHF6utsrmeda-Wxir3peEaYmHtil1V4tmxXuMbHbuNuqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/drDVh3sircFvuG_joMNuh-b-NFyt3-BYW-dyb_QNPE4P-kAvFr5KQ3CAnv2vTAc6X6cHK0MDp9Q3K4xDAitOchuDRL6CEwo2JCDoF27K1f61nhIz6ia4tkUITED8PP0eYiXnAXDXNrN5Rle5m8yrpWL9vJxoLhHPZqm_46SivQSTMY4s0ioF47P6ACPHBug_CvX6EUC6lY_kIEOUDdg0TX0-ic6HN448Ac5DJleuh6FoUnFRAgRY7w_0tcgU1-BR7Tzrb5XbVu1GfvtgM6CwiZnDXq4uLGhaPrAQzFY_3T0cCRB1D8Je5TWvP8d0g6zkm47wMfASC8jIl3hC9dJoGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSWRfb30jsgamy9Mbk9BWvkF_TBYowMmFMydyjNJHtXvBZFo9LA5C9MhWu3Jt0QkvpL3IBNaKo1FWFELm37PznJjmAAQn5-vAdYLwlOpF6JH__WsQOOMtfvuNPt6ozvDwq-GDQ_Uu-gZqJxhLbY7R38U4nVDWCnxvZ0nuDAgzZgxuZw74Zp3KNCFxNI50r1hfRamY1ETAdQiUQQQinXGCyA54Ckacz886v3KQDp135jp9Wr-V5puLNIK7RNuRHXYEC7bKS8Z-IigLLzK9i0Qag1RD5hFF4Kj_c-EX4g2T3hShXNl00uEanEdYWsM4fIfz3BNhhx1XAXVo9Na2Y83Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7-DtF78jSwkxbxMz_LHZxmi9h3EbP8Y0yAJMsGPTPwGp5e49qzW95pUilTi39objh5_uMOvk3uzWklaHM1CFa4wE84XmL80lI5BNUekL9d_NU4Pzg78ZWoU7yQ8VYaJVrhb_v-_Lnn-J5yx_GZ9K31VnumzKmk3lNEmOelx0tUbV9W59OQSkKBSp51ygxiHtZ2rIspqxTY094DCEPOwpnYhXVRlCrtQQqVCnx_fPHLV4QacWwP6fqRtNVHktf8Jc-h77bnQJbDsza4hUZnM3CfaVl4lhKpsaF5SMcmZqXqpEwCNX9qG-3NXIw0E4NP_wpSBOX0qlAhsgklCl2aBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pfo8mTzRBZR_Mf1D0SURmBhAZ0SVQR0UvghC-tsKfIbMjOogZYj3Ldurxjb9syZmjMWbvy1RAwJgb7X8Gl7iFM0gQYcW3K5gKZoLs10GQSELto8QyfAecrmCwXlLo0_7FxsoFXsNrAzU-rhyQ9ObMhTl7-Bp3Ds2x3yltsWlFUsSQ_SKegQnTtw07BvZ7Ckl9xBFoBpk5jdbt7unwFjmy_EokDdeqb37fCVGFMYeablWdtCdm70zfVLvUQjerVBbM2xfGPJHRp_EfJ9T16H92JTlU5JzbiILSWhKHec2syHPNcMshw4PRj7eQKPXfVshIlJcifqGM753foi8n58sIw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SvA9Dm_wCvmgaXEZMblIqcqY6xwXaG2FJ8KfaRTsjNkRN4qP3QLjg2gaccwwV8m0UnBymC-a50say7RTx211ZI0ErSC6_oOqtmu5U_sUrVVf39WRs5x8Z5IFhemmTQQJ233iv6gIWyEyfgWWPR4FVo-iQRNeTyUD6qXgONnbKORRSRISOz0O5Lf6bqN_uO4peIMMrzI01-C36pKyIPWOYK0wzQsuA6YAkrr2tR11ey7x9NovUlUVD6EYMgiUtyfcMH8H6to7fQpzv_1RcqXbdkstQxIS_JLSCteIqPOHsnz6sS_JwJHqaHqiFLeBnNizX2jUjdQM7o-loGegWYeEss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SvA9Dm_wCvmgaXEZMblIqcqY6xwXaG2FJ8KfaRTsjNkRN4qP3QLjg2gaccwwV8m0UnBymC-a50say7RTx211ZI0ErSC6_oOqtmu5U_sUrVVf39WRs5x8Z5IFhemmTQQJ233iv6gIWyEyfgWWPR4FVo-iQRNeTyUD6qXgONnbKORRSRISOz0O5Lf6bqN_uO4peIMMrzI01-C36pKyIPWOYK0wzQsuA6YAkrr2tR11ey7x9NovUlUVD6EYMgiUtyfcMH8H6to7fQpzv_1RcqXbdkstQxIS_JLSCteIqPOHsnz6sS_JwJHqaHqiFLeBnNizX2jUjdQM7o-loGegWYeEss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRs8O3-o92b9MqBw2t_pUTnnjXt--rl7xFrmmi2Z4daltPUn1Zm9mKWDwB9UeEd7N61tKUhNFXSXHqC11HeSyEau1of6vE5yprBZHrmLmZLhXCshoOyRe-g18itJp3fSq2cGyoG2W1yc9MH6O12M8zfZwCYlZwbitEe7utCA5e40ANvroaINzd04u86AZGKvo5byL9hCo-W5Qcn7aMC8bK8PhsxcD64YQ6exGbkKgMeZ_Ujtqb73jb0twgSQFdoXwbgdASA1G03APNasarWQPQZ1awHkCyg25G5CaB9XDzXCJu3P9j2IoIAKcQbkTUqVRL-95StmqQechWCi3smbKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIxoHUhCSG3KWVyF56VK6xiaNv6MHORY0gD_IgASdpPNHMsQdj0OQ2_Dl1QFosbZfhX9b4WQJcLxAjF6WvFgl1TNyXZbBiRnhNB637eDd1TvZRkbLfO6-vxU17-xLustztnVA6Y99O80oMwAGb09-PKJ1f5zTsRMDYAgnSdCEknw8pdQDzFRkQAsJJuVOLX2TM-PchQD-rHiXsxtAvHNetjZklIN9GUjATjLsTB7sT-aXblDlE4y1NQ3_uccpCzb1nUiU_kXIntMXF6wkQjNu1zv45npjS_dE-8qlnIS9slb5E2twlFIOXDsHtdKXGn6JSMVF9Wrwadjd3xLctwOtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYzlGeO70zTPFOgWq0nb0t2PiE8I4qEvBmysJ9GxfRipiZBhQ3pdvF_O1m3lEfrZbMfa5uppDB7JpF2FlkBrlkxUpwsW83fLPBZiESXB-M5wkL1cwYPNTG2q4evcuzfvAt5VqRJEOIxalyaigiZG3KqvmE3rj5wHAa1UCsHide0lnB-oUcPoKHdRZcOqA_hGHYtczwKdA2RkO_98HVS2fDAfgqQydvw8tjT5-8mj5RWnr5LlwgaEoQz57169m1hXDutx3vlOORIymHEiengiD0tl0bjiGckXQUCwYIWrIJs2oYDhDvigqAaL6sVjpwFw9gqJD4HNcqhqnyPKx4N_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhoRAVBG4CJgzysK0SXRD7lCbbfCvh1FLpseDIcIq4selT1ejGR01e1YqaOVAcD_RfLTyFaQqerzAlOmPQM_Nbh6I7_DlbvIS3d_2cmby86wAMRVf_3UzTufzG3uVP2AD8ceD-FsWAgoEmSadoF_Cpwak2aKKtOU5tygnIRxTUnE_hb94Ke2mY3gJUb3r-BKD1DPiGI99imiLPSc-MNmBLyJoOElElkQkdrq60IaqUprx4rEgV63nLH5Kb2asPabEWBknajYt6er3HvddYNtHRQ-LEVX7WgifjvRB5IydB_tkq0hC-MLGf7z8wxw9_eEix9Lxs0ADzsJOqyGOnYNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ajj8rYFKVONlX6BXWur_5OA-rx1NMcZDQPOo2Jfvtb2ITgm7_oAmhIFRHwDF5zzy2ytvbV9O-ywF8ixVgemIwhyfihmJhembP3o5XXKFUiVdYuMarnhxYpRg4zy514bRfD8ntNHLE9yUIEBI4rDfTzOVpuQV5YQqaozKBzprZiZIbY8Wx60ON4eJSY2QsHmO5P0l6m87mqf4c_VJVsa0A41EcWLXuD-TAnp4u5mKEtCDn01B0zZmsd1t_OfBiCsQweIxqUqPB7yKxAgSEljG5v1ifrKj20FM6ODWWe4LM4aCfnTIZ4FsWBNaNBF6nZk2TH3kJoUCgpinLy0H15jz6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBfvkPVZrf4YfDAQLwDajZp_G4bcweeHGIAWE9ApEXt96kh9wz_iiI9HCV08Z4eDPILwTI5XH8nmpfNgrZTV-eTeKX6w9veB_iNEk-ethw8TB9Dkv-oDjPE3be0gc9nFxciP5d4wi4Ye2xbOxi4FOY92PSSU2rvF8t20_CMeOs5AhBnkliYp1JrlTgZBWzY_rqWk_tlX9QjPquQPJmhcAxmpub8PmN-i5zGYrJ6Eu0AbBzJLK8zlNvc6fUrEBX9El1GydZfp_GRGoLVJG-Pm66ZCxJDYcM9i5v424sd19l4Fw93UJXmkcJJ1BTdOoFKKtoacT4UfnnQ1uiUFKipKdQ.jpg" alt="photo" loading="lazy"/></div>
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
