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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
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
<div class="tg-footer">👁️ 232 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 482 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBIUP_N05UGkNizqitJ97Il5JOdpb5ojBq7FWPotptCE7bon7zW8z7ezx_P40nZ96o-yg7vP4RMcBpCnlYC5KDYXzLIFEXXVOfrwP3Tpvmnd4LUK1i-kVBJ7NX5-fwMAY2TfDA4Crpk4b8w1v9giDn3IBCvL6M-sGqojkpEllqEgSI8Uh1C7qOdHG619aLWNjzR1djZeJl0y0im8p8IrkElr_RlzfFQydSoOTX8l8VrgbAmkdqXiu4_0FwalRARRWJsbZmEz6WwaQpcV7km5PmiOniN-mXKHA8o0qSCpI3xuWpknxO3uouRGOPcBrou_YGr50I6AkTAeapl1asvy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 998 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLljWbe99BguWC0tpiXOGIHfQr0kqp3xZQeHZgKcQi_ncSfen-nbvgFzVXdyH9lYkvRCkiNgEOHiZh-HbXA3f0ul3P9tn3LIHJZGyym-T-Ch-8GdOctVyYa1tzgY4kxD1QkVrB7j6-np6jPby1JkrD3vkMiB0BLGB3Pzr2plTkAvK4piy9xRb5EnZRnfKbE64KcjNFCmeMqir2COQVQcGHKZJ-Z9hkNoXi2aOwqCd36YzTAWSpw4IBJ28DhEYMGQvf9KAl_zlqQBavNFAANqcZA2ZrussRK--LPsXXSCHFNTe062a_1H0kBj6es8YUyIeRt70cJPz5QMXwKbN399Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGzVuc668Byk3bFRB6ppqrehKCr5Smi4eQKbncgtOzdQuKbL6cCVJhV4OK7U940Edv5U4pYYn8PqdQCsQ_-xAJTNOKmkSQ87fuRbigxonXdyLOiP44UKctTB4Sif43vAgfBya7hEsPEhW75iG5XQq8c_hdAzzPfS2nbia_SauPzO5vQpu7-ETJljMOqSWWrt7r0yeSNXG2XRIAjVBq-40zUeqeBOy8_37LV4S0Z3ggpbEQUefmf_hJO-_ugIVGnEJPKnVoVXSAs13k6HZqDEfwGPJt1dDOM4qtVCcrqbBfAN3YazAXwoJHshuzkYrP6foCOOH2IzOQn1ClkJRtTrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 837 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwIrUhRdJ0zvGnWfUtGIwzngyRByHDwlIpVmRls0WphVX93ATaFzmbm29JXl20hcGaIB-22Wj851tUFmk58AGBx8lW6L97IspZDXcNX48jBMz7jNC-UG_Ufo7u5TakS3tzWMmXNtuFxcUbjoKMrChqWHvkJrxiauDpIreAenqOtlb3DuODl1N2RnYYMvoQtq7GDjgOKDLVGxlhHp0JUUpZSsekmFgsy4HFgPI97rjwDczPp-PTg73vDr1nGakb9jSzX94JzN8Kdr3CTFucwTrHrYBj7HMwmDrjcSSG0jwwbZxMKfNSvt0x6Za1bmeXqHSqCj1I7Vy9xmOXK87t_qow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6WeY6MqN0QLp47j-d08LJf7vScs_NE0dP1_buXGt_VZnwWwXsEA2liN78kW-yzO8G-mZcmkGl3XSLi2t2N5HIsjbDUmzSPpjGNQJO_NMHAyRb9j6AnSwwA_sSsRMTzx1ri_YWt-gFMOJduhTxxN70CyzrFIeENgfVa09KqI3y-Dqy8TdXWi_fMG9qKH8cTPQvUA0_ZbvXPjcrXtpN_BJnlPIDPv9cFr31muT5ga6VTw7tZZjhqfL7i-buFAw6fHGXDl88f9mV8P5aIgIfQZGfz7LmWg-VfVrN5_ra2t8KDpabpxJhPFFa68NpZQcNYC4PXxvPn030fLCWa8nvQxyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKwiwvO0V897p5ZjAUB-lQjcAwEanKa1Pp0jY1Uq_S2nFtOO0HJIbnrAEA8ajFsWffqmXecRYreantPXqwYFpQCM6OTVay2pa1JqS6T9Lbmw-GB0vIu9VO3RFYBtP_UKk7d7hiWNpiPVUbXN0-BC6w7D6LI2FfrAL-70wDt2Lm0I4jiTA3rAKiEWg-UGxQV6VzbcuwdnEHD4KITCmUMJDSkkKyWv7HNWiL-x41Pv3mcwzyLFkpLVcZEQ11oks9FzPiP-M9c41n0ajQ4YHqahVH8cSIC2OuMS8m0sEakBFSjXHaSj7nWNVWQGDcY_goeMkl_Tk9-eOfth2mzJTD_jIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXDQrLofSwo-8JE7eN_AAyT4jgKZtjwMw6z0kIGUn0M93GLU4nYBuLRWPR2UE1Q7Iup0yoXuf1MG3YWv_5RFk3oEm5py2PETh1vvt3xFuHamVZuQZXSuwJmyS6McGCk_DDOihM_ThRh2LLyWJkEpvNy8PLCD4cx6OZxfqH--suGyi_XXNp9uj7-vmO77K-_JPdA2KmxzAiodhdUueC2WWFZnxS80jxRASF6N6q1bVNPSPXT9U7T9AYbFmGv32RNjjGoNm2DCve0-wIRt-x0WYJ3yO1lEOBHGKjCdpkq0Fp_eNQQoYVQe4NHiQduEoz7GUteCJAg8JLPi4j6pk7iQZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRwXgeVUVsSDRWdfBlgYc_aJ4jBa7UPqXpzTSs0fgRC4Z1jxZqp72j8ztDD_GRiyMCyNNCXS479Qh21zJQN9-OUzyAToG-z2tD4PBUe1_Qf9JJvwPEJ5s9NLZvporbUV4LhJBAtG4zDlogjugoonS9l8yEDS2opdW1xiBv6pLP_kCrjNPuz7U-7f3D4e15QabAP0FhnaXz-opYDHUx1b5h6t-PLAn7tzg4Mx9utNPq1H1whGDcj7jBQ1qQzQkiVJAXU_LU6g-dPb9f9FPrdZwgiebhlTTUNBPLk9BQImplyz5QpJR86tRB2SZXiOKgQS-EzZR4_fz0cpbF5MKkGkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tISrb7TUH1KKc2o44XBcxSHrR7io5y2XDSRhi382UfJOWw7LTN15-_vjryBms3G2YBmcCvV86NyosF3sZYNac9dt417FcwQ6acKXD9QJk3e4Ut_tw5VpoHAsECsFO3PTx-6AXga08vUzQYbjWwSfCo6GujLsnjtKKOM67LmaZDSI4n9OQyKchJvg0CBFhSNR9az4dOd2bpYg-qfya3kPnLA-Fnisao2DLIfrKSWdQgHU3PTvFQ0Bz2o3ILJHEWmOddG5GbDPSG52TgN-tHdvcKCX7vO57Pz0DkfodSjfSbrkmoacToDZYB6239B_PtCjJ5aDCKtPo72saTdX_ARfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmX5U-09Ojsz4PfolGnoYkUiMX7nfFu5OZUL8gYPe3A_yhtczGGUHva-Sq8Kqx7upL2dCFKCz3_qHQ-D1MH6k4mlVCEirKrR09FxnPO64EFE0rrEnt6f-_PfO2GBveLFQ3Fwn3uBZAi4nqn5-t2UxB8_BTfnqy_oqlA9XVzSYAbH8XsNxYIClGFJgEIScAzIpoQ4UtL-VuOmpQfmzUPs8kYxdgcS2Bs4R4mt6kC220MdWIq3j7OPg94j6vPr3GuZh9TxkkkqoYJlKMyI5lh_S9Nw8csWKBAChl7K_k_2UXCfHKl_1BjG3gsT-jglM3xk1pGSD_ikZAdCraLIZii1Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5_JglfBRdEpcVcJZ9YULm6TGI6jPHWbsiVh0-4j_Z4K4p9ieS0ZfYVtFhCRQmM0umVu0k5ECVI5usAfIb_OnWGlFYJxYeruytjJTv_IAw5kRSFe39HS-K93BOMPBlPrOakawufh8iW75tc4bLN8E7tieEM68oI_rHTXIu5QUELySzcpW9n8cKMIb5pHUfvCkDCGlM4ciqc2MRPaeC-ozviF2snjD4sbFljPp_tNNsCLve3UnfpbLHB_G9K3PC-FY95GQmS9QBN6vynF9avudAI1SrQFZ7AUtoW64_lWRs4kWmreKS_t2AERO4S39Oo2cVXYYGIfPQDA5UQ8ajNpkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=bFIQJGor0QlFwyg9hdrQDNjNKFQHDqbMMQNXDgYgmVttnFKpePEuPVLjfdgIoK9UGHuuFXWlPGA43sYODwAtDyb1Ih23J7dzJwxELl3HzwBuQz8c13T8WjpA-jVRFjso96hmCV3oGIw6JAdPeJKxMpoKD1FsVzTV0bMzvk1lO2T8dCNsueNTdOxOgyN2GE3FjlidG3842BSFz4B2LMesgtF64eTohucaSE_OFZ0ylZqehGZTNrF_HW04x4yqbcZV8yjHYQjFLonZJVd7s_8r1XYVrR0D10cho8JdCtzf5hPkTIXjUHPmJXJZEwZnzG-0vBEw8oxIP3byeT-d1IE86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=bFIQJGor0QlFwyg9hdrQDNjNKFQHDqbMMQNXDgYgmVttnFKpePEuPVLjfdgIoK9UGHuuFXWlPGA43sYODwAtDyb1Ih23J7dzJwxELl3HzwBuQz8c13T8WjpA-jVRFjso96hmCV3oGIw6JAdPeJKxMpoKD1FsVzTV0bMzvk1lO2T8dCNsueNTdOxOgyN2GE3FjlidG3842BSFz4B2LMesgtF64eTohucaSE_OFZ0ylZqehGZTNrF_HW04x4yqbcZV8yjHYQjFLonZJVd7s_8r1XYVrR0D10cho8JdCtzf5hPkTIXjUHPmJXJZEwZnzG-0vBEw8oxIP3byeT-d1IE86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvt_s8LPx66dnqAEqQ4vV-ImZrxr10wdRPi57GVJ5g0etipGZaoLdnKX3osoxEJ70laJK_OuI8tqbpAtPDZtQlgz-xaMlUltoCjIHzCDk34IdJHg-fCFq4Ysh4eIV7qOJNVryWHHl7AX7citpYw2L_-bXHDgv-m_l7r1t8jwz3yJ50aMfIXTu-zxhsYkvoDORxnpGBPcqTD0HohipvM9WTD_eEUknO5TYfVfExXHqT5RGLVw873S8dZ-IEAWGyEOoAByy_UH-0Fx6BaGOlhbqBq6b95jZkQMdjSomFu84xvMVYGthcSjxXVg-Z4xbp9YFto1kKSyp9XzoiBlIJFvuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEAzvwPgIZhO5uaQBO7RIzC59oWUEn_ZFCurlxwNFCPjWOty0WsUsZoNIGk7seN6f1Lxa_KpXlybnaiVy8-CTEMSWcBgCoCvTV2GKc4VIy8Juw2BAnetAhutlLw2JTrOKh-pLdZAmwC52cFkhirtD6mgY1djTL2YRwubpLzE17uOFjYCM7Rzp5zuT7pGI5M9U2mRH31bcrGkM_FpjQhyrF9yrOAJk20taNtBybn1i1_wm5csr9OxBe7-wc8GUZqVNS-3XqFyoEbX8B-ZL9xPPOyo2Gfja07aE4EC5m05UAzGbb6XPQ-iHQx-72bGhr2ow5OMULfoA16soB_UqTbiuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m5A1-xI4l7bKz5CwYfSzmBW7cPVhKqmbyfXqCtQM5SprEd-r6Vn8lxfIzm0UO-UnxvTc0y6z8kKZR2RQOBLs42LSU41PdZ7W7fpuCkUOwnO07fVcuSHzxUnn1aCQJWw5OdqIOY0QkOHLGpxfngFIMiNeirH4jhreOhGwAZSLi7tdwEFSuueC7QKkMQ3DNkmC9NSu7yfF0k5bmsr1pz8TU-izrt4t-kW8w8zVpPJLpxnt4PMlD1L5KyXAK5WW6C4n5FsKom9VNmFUmfZTxzYWywInHC7fHx57PJZPREHDI5wzWTC8OzDzSqO2gKqVaDQ_Q7GQ_HHgdUjDF0sy1pZzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn9MaKgVKNglQPwjdjUUP85JWGNR-b-ZFCC1E6mIucWlpyGQdwfGJ_bKdAauVOsf2Xpg5JjVv_L6hTf7NYu07tvl6oNe_ofzMft7DJJGaIWWhjpHyQRVd7Y3zpQ8X7OdXbIgmlg7H_Nguuk9Wqj0Zg9anVmNWOvNZSRjuqyeHKtQVPHKfJNhaC804qL4KwaDOxwJGPGo0f6cuPayMIG9QEjYC3YGyEPf-IMcVes5B9e7vjaHoKlY-GMVut4N1XHXvU3C6dDgMYb0jjshKQ1g9DmkhM22336PUZYP7VRsw9Efne9mtcs0jFJyB-YLTj1Y8-Z3avrBUslH1tQcBe3GRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPshk_BbglYFGugIV_HtgP_c1yV_Vpq5_9ecqN9xKbsm07LnPSM4j2ilCN0vwOFGaqnQV4tk3zHSEWVgLlH_UpSnZM4q3zI1318CO1sigxl4t1ZFUYtbFyglvF-_Na-t66azt2b0UCwgD6WFihFUTpomG9srwx3EPuzyYYg1mWTI5W37sblZOJgRp23LERhlxpS0M0Rzp-GXzj6YsOFBO5F0xK42AEVhIjGgcDbL9BEO8RAzitaXuZBqp7PWrGFVY-47le4aENexl3TbgW4_XAuA6HwwuI53N8SADjwimirPNQXaCIWg4XNPwm5VOBbwseF3Is4_0tLCsdBbu9BkiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee7PZWn7QgRhnOh5M6gsKDbeau-GxmmF6eakp5T6PUerzSB6doVBhgagLV26iJGTIv1EuRuUS2yB1C-OMIIyOkYKHofzz6jWcEXWzo6mzCyGqB7HP6C1OJypsXHyokQJQJ_uYU2NX3MvmNf8CGi9ekiJJY9gPB0CcWaLntrPPTmiKtmQ9li-SA5U1SKMd-zPkqb6tUl6GypB6q6R1DDAJYq4pg0p6We4p1UyTNpR89eq_V7xrgnhsygOuCtvlStZSHE_QyDf7sVuEaVKZ3iDykIXaVc2TKD4w48GMDYZdbc6YGmwcDIL8xda7uxphofJum61-kAPBRISKApYKN054w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clBrErepBRZG6e2Vre8ggOA6nSVrytLZcDldFiQ7jIN-z66sjdxXP4vzM2Enku3JDwvyhDo1Vn620tnMwgRR75GtaPuyRb-jNxGaNXsjSAX091xolK8crBBMID6SGQauAXbq8BmD2Ox9eBuC86rTaILyWGVyH8YQWboFbKxFS_6QiAfDszCGVPtersO4nQ19L0NdrBh6Yc49m3b0Gw4FOZPSYd0vzOg_dhzerrOBZscZNOGJB-wKeK9V9vyRw6iqu7GTVfCFQUN_lPdB88ygNaK1yHPbKwZACVkPl_AsQXGsrUeEJ5N_ktN03FMzA4SHOoogb7qmIkHKhvhCni1yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pakq8T19jcUVW0zV2nZB3a8ovn7_2OekOUoGfsJyWhV5RyT8xNyBVDeDLkdBBJBryqc-D8Wl2-Zz0L3s8pZcR5z7s3Li_2dU_IohLqKKFncCR99rPjmgmrpaXIEph1ynuzM_QsfMJx2CsXqV2QZAG4A6Zz9m-JaCQ6KDeUmkj0-kcNIpvmYp298OKTH0x0iP674gupqS7gV1a6YFIMzgpnxQt37aVkpxI6hFgTs27TTrfmt3i9m26AV5FwlvWz8OEvFz_fLDG3leH_-M59ZMnl7WHD9wvAuJlAhWcqqEuPAewKAjfrHhtnsCpw1oPC4pI-ybvsfbqncKcpNNkNgZpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1Ys___YPaup2dY3x2Pqqk8N29usCT7frHsttkV1Amjgi3nHHg_3hfK3D30A77uv7pgWGFaRwC7uT20en1XyYGsu2wqiC_X3IOtfNKDkh7OfdTfK2PmTCrFZeBDd6Pqxa5SyLljtJ_SLy0x3dhiyznPSxnDGB9ji8ZfGKBsvZbwwZyize8F3QX9jGMyUkxbuElogFv37UHojvZ4eKh8ZZzbvZMJ90kT_bv3U_iYMR3QYgH7iArrrC3u9QbYWSefca1n7NEYeO5XPTwdWODZivfGDtibS99Pi54OI-1gHdLbNydKHOFRIunekNZb65Y_XdeXjYY96uF12M4TfZHmV_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh449CPU7QziTNlEZK020-tnqnqNJp3S4J-7PQAJOSRe97LnfO2lz_Urmpt_WFn_1tjsRDpPKoCZn8u_H9BjMIWjmLLuNn65AtZ1kErzjc8k4hQ5TXEzusnivxWhBpkmTK-6ZpWyTlB1y1BniSDDrAN1tHO2_ojW7ZwETYZS_v0YeR8zmrOREdFrNTawnnU2jpR-H6-tnne08Q8uG7M2ds0Aefm_BgTFmSXdwzKT5UooizjdKNElgP-kUEmxw0KRGsHHflba-mRdHsD5o3L2YMrne2t7MBTqan8roYvHhNP6TLqHRvtU7qb4SDFZAviFWVnpQ7w4-T2t9ynIptZ5eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLqsoOHPPlnzO9zZOoZMsLOXxSnoOcMY8lWN4GO753OpBb3t4vnCAA3X8lrWdoOA7-9XKj7vJM4gUqDiunDzbVL4riTBb5HiS0laOqHyD8mg_8OADlceTZU-nAC7qoErKJPKg8oW-0_I-Q4HmpCZ9VGPcOs-HOmdhWKyeNscKSHByAbMDIaewPiUryZOrBdwXVxS1SAKKlR43hLyXcg8KAGSLo-kbR7hZ5ElmUcfXXmmViPkm5BST_Je5nMZkNe8OwW-1EQ20a9IhE-9Wd4PQ5LzGK7e6PyT_H8DIpekxBA9WnHyu4ko9fSib8wDJVebFANygC3J4SjJgl5aqOcT-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5d39F5pyCX93aHcoUpiwykbQPodGsUTOuHSQqdjMV8-8nyPQXdV-GGdbLCn7GQNmzB8aHUsY6crDZbCecyEq24TUFLAY0a3DPgGY8LLdOTkFv_YTyCS5RUYxtLEzlovH-4l5yTRh_ZO9d1oaGFwp4T2cTOdn9NXfKrkVdCskjABQLkujkZorBxstTUtg4HNiBJkVryGlrSBkYYyw_uUuav8fip9MVlqOE1l79u8TMKAL7xlriCK-AvcIi8BNtZFyqIAwPJ1R52zalckK40ptwx4Fd8Ns7_rKPfSz90IQ1V_OFcP2sM2WZ4cAJIUrDDwNsXWz_qTq8HO738qAIQNjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3l6OGsDhtskhTGD4S879d8TjnCDpqpQHPblWcd1ogFUAPUR3vcdcVdZXVKgmwtXGEAMserULg-JR_d8NVxgbm-OWObGfPN9lieUTSeZqKcSDNS9fnzdAihjxve46JGK9Vh2Pg0EJuG0CiRftXocHXIZyeJsQ7zns4LqdVS06mSeMhs6bEmXxOKJH4vE5pFdB1uspgYomvNri9chmwGriHeFSb_yuYQ58ZlY-NJPgBj84JXrF5mWwgY4Ye6YDkT5UsFOxcgRamePdfofPwtQuA1FTEDMwkEyrKfGS2ND4bn8jPQN1YLBz5Chy7DuHW7WyYwJKRSh3sk5w-fjKy4_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgtrYSziy7Mv3cHb4BBIczj1K7N2KvWkIbO5PA_1Gdbft6ynCy14zOFrze91UEf0T-iEv24W-CCyZOoL0VB-5QAk841A21U8ylW6iZEU3nEhQ8O1cjIxX1JTf1cDKydbDPkElg9m6i8ymwXpyWckVzGQcbMlAm2vPCOsY0WRVNKRcDZVclJOqd9j_lQRUWUv-j5aRHI4Gq1KHxP1f6G0lIzwfA2IT5-7xGqRpW-lnAxTeGrBO3cDVqn34WVLpLCT1UO69HXEnX-spE1_WzsdFRa3xHfnBSwg4PY1o2dvRcpiH-ZAdNor8zR6d16Lb_aPDaNvxRctrboZKNLB4Tr3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udMAWOHfUq1nzHrlSwt6m4pMh4RQ2WNcxlV1g7CPLn2GFbL-8ONnXH46jFgdGRSpIdznaNUijhX4Z-Fz27q0x2rYUH8q8sVrlkTaNevsR7rHpuXfv7Ezg5KXEPFeUGhK8eFcmiARE_HfXkx8I0Z-bkT4zdA12uWUDlSaQCNNrMUWS5iLQ5XhbrSvj2cEAUuJOm-IuGeZW4M5eHOXq-uah9PXxe29OKJ1qooZfqJvXg9luoj6xLvnc8surmMUlGHqadzCNKQGTZNO0xKzgMWdI-mR1BJtIugXYyo_OyYuka6_afXXBQaoygchZx50HDeEW3wEQJIbJmzpz-qH2J_7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXrZqTRzlhJKhQsyU0ERUgdVDB1M5QcXir0WL2Ql_1MoOntdzogn1Kic0W5b9QfhK1AUHSzTTorXHCeCIufGGdywlwyWrX2_snqN5WidAYsUDlphY5iMqtcej-y746uvcfZEkOTmJwtwDI6jQ7SQXVV9q9UYL0XvN8CBeJP3twND8d0qiiiN-vdefV5VGSrB0VBu6DT_89FzWg_ioYUf9v6BBfJFTUgRg-MfAgUFNL4_aQQe1QufuitBhd-b3wlc8IhClV9tmTCszn3ItngGH6qz9f2bZ65WUJLpsZ5eQ-0xlIbQHDdLUq-gOWrSZLgt6n0iKI2SJM9NH0LY-ki5tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dissxsoGgBnPUXly2ihO8lXh76pmET8b6_AgUa20lRDOy2zAYyrE4-2Dnb_1A7n4Zdabt7X2IPNKpuSRq6Z9gU64uIc-XtfO4bUXVxQ2dX8a-Gi5Hop3bcEK9VgJsRJAEQ3f0Fl-5h7MdrpAVghnevNeqUCJqhR8UzbxoCCzh3qEbBwbZyIRd7QNVWuHSaa7XSn5UyeTRd0Mx01_Nb3lL07jNxNz0mhg0At-sj8-8d_XGtBzmwStVvCssrxqPANBBE_y333avIh_uZrGbRpJgLiknXSheKo36EB3MJyIr0av5BdArDZNv4UBL16heB2DxRHjP2yUnUb1JrwqR1CNRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRx1xOLFNLkAImdT22Msh1uR3B484ODhyf3N1dyZf3bJZg7PFaNmKEiohpwDba0oBVf5eSxDzKxvS_Kqnhtdf5i8YcbHJssWSS9MhJf7cZ2DHHgnEp0cLVG1SNoBKxyCved0k9_foen1OBhgU9U9nxs6gSG_J4Io9s9zyq2LoYRxlffY8vjyaqb_vIaSQmb4bTg98-yV_PeWlRbikiwtdkzNQmkYNOKi6YqQ6Vr2bk5SNR4GYd9qrOeFmE9O0PVSSlhJy2JyDeS8dPg1Ouzkyd3wqTx5yUu5M6Cpxpkpgwh268adeMG8U-67TgWnlxe3jCCxVnzumhKTDBbORJ280Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRXqhtnEA_VTM3qz26z07IYoSl87LmpxMEgsQQqfitnnrCZq7o4WZEreIqhKON-DLoCHTtn9chefIgIgOwkG2Ddhb9Qnd63CDL4JRkSjs6jlsoe64msA7fyrYf279nPUnRmeFFqyjyrV8p4KBfYUIfnW9HCcqpoYQYeaJSP_NmZdBn9mY_Frm3ps26HLRd_tjZUKs6c1XPrnoOlKVyzlSqLsyghvuLTUXy8oZeU1dj0mDmXelxSQJCufD_RpjoSjmT6SPocSClVhGyvrh3q-wCS6cyPW-qaLh3DwQ8Xs0DaDn1AMyn9wa6JDXs2O0grNa2p-NeiZJQvAIinY3wZ-LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6xTBofypF0UxarPw-q_kNH6iM4U0uB86ZpM_Cyk2qDYwpY4YBNRrk3PDI730yW1sx0UpzUrcH79S2hLHvNeGhD6g8weYH5Re_eVST7wEW6nmwsGmhAAbdOP8ljiP-gQSZ5AldqQEAf9B7KYYzbnPeB5VkqqxMrq22_SwvuNcfXFTfBdMfhbYeXI4SbWGsDk5h1KzR2BX8Fj2BJGQ4Jp8bbH-kmOzPueldXcEuYwrFrt-VEDN4ZHFAwmNypFu7g9dGt5aUAlvkXdbMNDM22_FFrcmIc4KhwKrjVOpj40YYb-yoiFpG7k4oE69H8mHc93fpqKeBbFjecCrQESptQSwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibsiTHJVuoCjnLVV30QaTOUYAXx_RYuvqqtUhH8y0jMKUFBdLMQtu-HG14LAFBRcvXd35Sb0on7AwxbN2MwTxNo8Rsx0U92W2oQuLCAOB1pmETePXJMBA4gFG0XDae87hnY5ocm2TENQUPQU-gp1JwUGqzzohPIDeWZon9WBB54vlPa_nLxRHxCRDbXMChTNH1moTCCvn1jWh4uWK4UwPW_8YX9oU6Ahm8xkWj6-tqlOUVGhVCVPp9-SA8a06j2P0Kh5KNQbjFuJtmkSchgcbU1uCjfnenT1gTTOCJwbDLihT5UVq9Bh65IfKJVpEyOsFk-Y_p6CAZusAY8MP96Z-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_uRCTlbPfCDxohQHZHSD0GD4CRMN-BlJGN2fZRxnMAsVP40f1ep9qhimgPEKTTL_NfNWItavX0Rq5tLL9iDuGjUgZGFE-cBz_22rFJxCfIZWM3Q8gbysXKGTXTppNJn-Pv6NPqooxWDjCJ9sEOOO4CPRL8s1Ko8eSfkcXBTXL7FXTHElHH0ckql9Bw6jjiDWZbwFJIaoQg0IdM7eJgVAggF996PNFFc0onFwVlyBxg79Q4XUPzynV1QBHv3oamBnwazyvZfIAvQbLfS4C8ADhB4WL6arg08CCjC27nUvLRL-6E92OVLW_C94LMcMloaHLUQqldPV5LPG_ISzAtU5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7gKrys3K6Xaaq4yybb_-wWxyKG8SgRROUrFhdVlB693YXhqK2MDb3LftumLu2_h9nEm8gIbC9misp5l2nl5HkKyp4OPL_N1tQQgy6U1IFz9iipWhzXQpapf5zNcIBuDC6GzvsPy5-XocfPcJJYrkB40joYaEmYHSV9vfmSSWTKFouCZfoVAYEcXJ3gfpaVDSR96skoy3Ww-Hc2nzygxR7ZfH32_JolATsTAt_sq3XdixXAZPnfHfVQcXS987vpXnpEQzAcYJ7a4SuvZib4yogEv_aBv3ATxEiJuEu5kTs26U16I8D3LpRSnnY3h3eKliS7DL0oampQej65RVcgvYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oh6a5KIi-MBXwzvHohG91nhImIXCtWSsNskyBSDPGUMC9k15tig0NlqZZpqDfVDrugRww65v9b7sntNeY-AtCyTGHfG9UCIknpnalRCbYa7VGuliEBqJpZLk7KfyA9o4p2Nq1I9K659U-S1cRMOFymfExc_5hriz-E37rnBKB2Yv5DTN54-tf1Vb6pfrqCseeISoSB-smOchznGTEs0tlh7HIBJHlregINECyz9yez8sP_cGr1_eQ2rJuLpaoezoDT3QaVFl9_JPybAFScKnQuCX2GZNHL8B_dzjxBHbnDIAUUOqLi1ucSEAmVGAonP1jDQzWurcT40inHgVYutCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmh3zPtRz_XzCrR7ZeURbqUHN-_IL4T-OCn7ARHObjQ4c3MXOCXLzhQXBgbCLxBcI_Hx4tTSNMBCORuod2cKtDBHiimwPenHX_03NyMe8B90X3JuWqKZlMr2Wfy-C9fEsazpYyXFQcdbTp5MgyB1_IZ_mZaGii--YSl3MuP5_-zLRz6X4rakjKPfP71fs22Col9TMXndOGc_wDkCMRX6YWFUtMWNGv40tjAR_z-b95e3S5vTp_o-R76yxX1x8i1LlsmvCDPG2YzklEVUuy5yHYFDs-AdRoQRPWEHwUsLbtZ11i8rbYfeNmDmmHHd6iPSjojAgh79qiW1446FI6jQhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaO-QWmjp-tDh2434ZTBaIpci07YspoO_ft0Rws41dFJRlFv73Q0kkM_NrMzMPEqf66-uESf-EtO8vNBNem5Ojps9WpAyKhMkUWvPBdcjfzd4YsUoUTf8FZt-8av2-UoU-kz4-hX0DhXVCpQrXZYcrS_IxYUyR736t_OB0CxgxNv2X4FRYbDe2stJFAnHoItx53_JOb6w6pQbBbDHWaDUAVAwnkV4AN8s0Pc3RSbkhAz7jBbBBD8YSzakx3txrSYRCNMvaJDF2H_v_32LP--NG9kcFd0FfB46pIJcyJ2QeAwJVZDiFXeDRMcz5UsMTQePqJSND5ybLntAy9GMXcJvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQBkb54qpIi9_kOLcfjevBzKiNtlFdYjQqoBZbUo_lRz8BL-gn1s4W7k6XTh9F-fLf7156OCJ9Mnnt4iWPUB14SMJXQwiGCskjUJ71JEnB5oiFGG5q_TXu1SoBmVIedGaHr355RVFILR8Pz_g3tpmPpW-6ww7W6HdmsyhpxdzUpxaPRlbig87V5mWjcZX2EatLsDaY1HJRBUMx8T4oSzc_WPhLbIeh46NwY_lxatT_L_aZWSnNktybfa87qYhjmMJbg3IVc4jn_f844jcv-C6DenTZfyL7gr5wCVYLD763PxmiHfRXQQvheFMMe-waSY6jrZcl1Uad7bWeZlWNdsVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjICdVs98Esopo5JZC9-xPKm3azfVw8hTV4-Yc5ZzLbnwwfRmYBGaEwtF33QKE9v-jMLJs7LDZQwFZqIJsmm8eotqECW4WnfHmBB9aDcFUd9RQwomEinlEMk3wI1w6yWrMBXmbdmGG0Z360UxRP_Sv0_9Fd8qSb7cCNef92mW3Rb9fi7nJ-OOCMsc6S2TKqVuFW9O8k6cZE8oMDq7kifZfRYHB5tdAJ0D4uT7EWjc6wz37293gXHms08DEFHFshGXRbpt0znKklqI8LGMOce4scXd3VEu_thRcXhx_DPF-3vn7dC922ohsQelf1SBXC3M0a1-SZQLdSQqPrqVG25-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLzG04QrpniHspqZYEWjLlpcG9zpnW61AA2Ljmfw3Grhr475CNQzXZ7YBiL-6AS6IYHyD6Hv_c_KarIOePT2DlHLqYZW1-clErP1ws87UD9kAwvslBsZ01djdsJIWNV-h7ge6PbwTtyTZhUcAE_zfHJzzwwYXDOFMxfcjAWb985QImmtSV4U_Ho488Lcqpq3z06RJjmeKijhTsgOmlNwLhzRlYEP6GnUiLv_Rq4wUcdILMBxjlxqZqjQdo1T0yyi3oStoAQztv30xkFK7pk0yBEzeME-7FJDYr8oKm6EEhv-1dXlOgtqRCvXIhW8wm98atJT5pl5S62cL15I_BOoTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNcp3WCZoG6BtML0Q1TbmuxxzDpVC_nsmaxiGcLuQBpV-YrfIormaESdMJngZNKZihTYx0MzfnDsKM_C1iShe7Q1AKokfVIV0Lp0kc42_hkLJc0F8gd2MMJZQAuQX0XFOdWcuoUki8-0ioomFEkWI23_2k9wYj--30yQ7YG0A0cUDDAoKjmoVR78W51tXIkwhNHaS6v_25Y0LkfOTI-7g1lS9H7TmzmlxwBrqcrbkMs11OUqM-tScsRxTddEgNg6kPvePhNtll6rlEauxj8o1gLcEpuftEHXM0oPlbJTKVIaGTjiOYzpByyrsPr4obM3Do2D7Junp5DoWXDO6954CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjslgEgfuzuBASLshwQKL5RdtmBr3oIzLZjJ1ZKO4yOq9w-dsKicudJyPCeBdzsDEnUlZ1FUrhzHbenRtD-jOr3WXi253GAd5ZXTck_Cg_q5qq6giJRcGArXuHgS09BtOrIozoS0p8t1eYHGcUk_JTopBInXJ9mRYfnnmEhLg34Jby4pl0UqK4invJkWJEOX4vROBCtqy-cpLkFbmZx0ngadxF4yKnKQ6kr2x-UhinIZl-KF-ikHScjpihmXCfZV92nGTyOxCUqYB8zI4XixiBFecRqJrfmv8DYSVfUs1PdNKULxzyUV0M2Y4rrRFosJMEkL4-Q33dgJV80-mJc3nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBAuCJHq5M4fzzgV9ctWhqFH_w_b8wt3YN3VFgOUwYlggbwd4zo9IXKVdVcShN3q3JuGsbw9V7My-lPst8rOq48RXbRW2cSB7bIz3b_V18vKnNTWCqJMuffVhpbXxQvtNmNPLFEJUA00JAkhKk8RbUv5d_vV-BcAm0bJB0DASSIT65DaLvCjiUjyN7iu7BgII2un1ylKptwsF2tEaXXQPEwzLk9OYQ-T6vA-jaJ_gAG5mP6A2-2Q-PepZVQK8XMfxJSmvoY12iOQnMRVvVa3cri_agdIRe8oXVzQq0FMtg7c9idlUh0c0njtLTT60e-qcbsajuC8tha1XtXyJNEnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXJ6U7eolufAlCaF1KKinzVpkYVThStycv5m73uklmNCIgdUsV4UaSVvegAk47vD7tzQ2c07Inc_Y5YSDB-v2sdl4ZLEFY5PV7nt9FyN0dsMFDysKfY9HLHmZiQSV6R6_NJg-9tnBYjuupw-Mdo8Mp22th1DuyqFxwMFdtwxCfsiJvfap3u_x_JWgcby5NmfRXz5pgJZVN4pc6sb1qjzGM8js5CGzAj-j-cMz7pmlVEu74Vv5fk29yDgrnRlPaM-yDc_Bvxx40t4RX0DIC_ln6pQAk-h_u-lesjYAgutE7-natS6NHe_iL6cfItilxBYtE5DkW6fXfAPE41HCCWLqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps-V_MZYTCmyj_gtyGPB_JdDlodQbhVA4V2PXd_9WGzkNsrsbXc-ZSpAbdLtluieRTWfXOcIcTyQMWYvBo6e004sNPdoExQHgXcOVyi-EvECmqjyzXjUkhVYy2r4mFzqWV6v6pueQrT9QOmUITTtn2nRYU0Vb0NNr9qzLikIr4eATq6ffmdx8YXU27Z2z1gz0xn03pi9bpJTxjuwfaNpHaihXmNNbGcTlGl6Idg38MkNmhgb6c6F98-UVS4c0r2znHNVACP7m0ayhXutTRoStvYfH63oqFvxQzRXaDBm8SrHSnjQr7F2Ed-50fbXPXiV5JAAtaCuOlKYHWSsq27kkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMppkT2zJu52BQIHQz-I7FKZIkN8I2Zt28R21lYRehfgfevQqTxCNrvdFcUpu3iMynLljf0w4JhTK0-uha-UjTW41wSH5aaZxA4Ikd6JYx5yvGe0MlbyIOxPfK2T9mXPZKptHmA_hRNvl2b48YSmodeNQkNGCb1D16wbpaHi74y1qyUMSc2HXK1IQxlBFvw1lAC1ZZ3teq00q46yV6bdw92zp2gpL4niDOQ6jJ7L3z0WKFlxEZZGVk711rWDVxzKIOxzbXRfJhtxYbAU879lZVUYmdddcbetPMk1Te4rByv17SK-KOCIrHsitZTmXOj-ZjA_mk2pP_J_B9KTN3M74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1bYP8YTTkJyKgFlXZ0dxEko1ovUq8mDfziYDh2L3Bx4x7VnCeNxl0EhgOVxZJQJ8txpXVPshSgro9pt7mEHnL6zz1I7rQZi4YIdtgBELtbRLgQJZX_RR3nedKRAgx09bSOdtJMDAfBe77qF9gvg9Gl_omiALrcS45aFSrhvrAMMGCPHwhIQebkjV0HWsItMG17NbnuML2k5it7suYl5kHYF7EtBq_wmSgD7iReSI0INfit3Z-jYWWQ16ThhCK_z2NwvC2y_NDT4HSzQhIiHQxZCMXF7V-EdaXAfhrkp17Zxq8YTPSu_5Dl8dqHn6uDMQMIw2pbg8e1aW_lOaWbC5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY062c4QRv1aFZ7oJ-FOWDtpBETO2j6eqZtE7AYDNlfer4KdUo48-DidaviV5TleNGZ3G_3KvdgT8j7Wp5cIBD9nlYx4utvw6z-5ZAMPBcpjcwr_56-4qllufBRqiQ9DKMUtEx02tUK8WtrX025I8TgkGCLjD2k8tUzXv1NrB2mIl8-CD30eSshN-pEE9di0fvgKw21stJRKmZQjS2ycVciCzFRLiawar8IK_cnYCwAbG0hlb0Mc4dqAijOZtv-oCtWeaMoJrFjOMcxT3EGsK6QSfNSbMAeUmEYSQIFGSHk_7ofkAbKMMpmb4OCGezkruy-c9lwIG-rf46q9SJbbMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfBTLT6JDGm-uj61JeFkOU_R5krIslI6x9mwWJMQjFDfYxWA-39ECmUf9lxaPqi8e7j7AZxrEY58WQHDnp_O59A3unCaAVjwvsqu63Y7UpYz-tKs4X452_JbTRnMLZJkl8_15GGI5YGorTZ7RP5W-bhVqgXI3JDIjpUxKNsXo_1OVUfXaxBMcoViBWca8nasmgjj8Xq9AJN-kvVTc-h-q7M7k-Q5lw2O3Is1bQDe94ji0Ntg8n7io7tCeqvYIcYFwpJ1tTLLBGspxD7kHlJ6VyO2dLPP9_Vhh8cfBVAhwFMUyOHPdMVMSyz1liMYDf_ABE2I93lePMEP5PByBYzK3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICBIUoeIO7tTJOu4ApBfCvipsSklcy63oMFITHyvG6wi8XqISGetjkgj2Y0u5YNZVY1wBAGp2JD0y7po2ZWVtuKq5ypmzeLlesq18Pfab-C6LZP6uS2dPaIW8WttlQYCP11DQiP8zqTVCkAfk70U08aejWxTOmq4YCUsflrt6lQQ2M2BuU1axY_NcPS0BU7gWFQVRqTs09M4tXKg_ZGVGkBbzSz4p0_MPX03nHHmpd5q30rx4bYwPO6JQAeHm3TTbPRmyByC2QWSUHNv4d8-Dt_jswGyvoZiRV5rXvUP2ZruffJSQD2sSO4H_TNykUOYjGMxNi7ZzC1URE5xsZWzwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idJt6aXXYm0uNJW8QAtH6vQI2mNXYVxkp32k_AJ6AqTsKKkWSXKWjQk7_rbQJ36mW3SjoOOccubNsapFmYbEnyeoby0cQGaT2PHXlVAeOzqMg5N7jHctCEyxqU1IImlujO_GzNYUxnPEyTvAGdaruYTvj6raU-LD5ut5STVXHH8KkmvW2Bu8SX-yRcAu_gpazLQQm3U6k4uZpZWgGLwmG23CkftZczQGI4OjXzile8XcLoto-ipnkA67GtgkcAxAnfSDtiOH9iAS6kjUfJ63WxadSo54Eir-5nnIvhBxaDMl_FKAgjHGoTt30tjvQhSig4eANhQsZ02iWBwTFlSqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzC0Wyaax7qCnW72uTEPXDYrvjNkAz7h3_p3QKi7QR7CBUEub_m_Ktub6rmaRnhpz4wJGlGXSC_FWPckD14fnOAODlQm7ZgfMh6CKtEkJ7DyC9QZfqSrgC54It7uPzot1gTzvL6UKJFJm1LP6JNxSTxBBpkuBJiP0HjOvA2JLW0u0SjEgPfpRZ8VcB5yG6w6vX3PaNQeWg2-H1d8FI8fRs0KI6xcjjZrpJd25pIIA6npFFeGTstpa111Qpa2MaNha1O2BdRC_kYRIl7TOR-pe9WgfZ8p9rmddx5YCa-iIh4zXwoUn_5Ere4slBDBAWJvTUKCcgiTACYuSFHsolAy5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWxiBp4JJwshVlPbsBudsykQEzr1K1wrz3o1ZvBK-C5WBYkEYS9wzMGri9LJX-L_6bLs3HXKO0mrP2xzMWSUf5A4asdnJnV-0D98BUSetjaAJPAWvb2UXazanM7AwNqKHqT_IIvBSFCNqLPBYOhVKsXzxK6gkhoEu6NHnur3h2uqDSyAXuc9eK-lFu1bIyhauKkiA9P_vbdvSsRALrhm8dyLU9aXRyhq5t13pPo6JLuEv4fG8Lo1rGaqGQ5kS6ffAKCY4QIf1DCIMx_mLQyEHPdCnV91Cwl4OKnDN_23OEPApDw_ujBYlTE16vICc2cKau03RlWqyCHILGFPbShkNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeLAP69K9NyAdT4_v46pBam68YrMt6iywtLnr6LRy48oMFT7HTG8cLuzo_zwZz9wzjHHo962QHde4-VOVKuDlfRtmJgsQuF1cXgx3-uTD9ruEblKYIupUO3eKwDbmgWFDbs0Y-U1WgkLJkXiRRUAVL3gTvVZ9nYbB4yvgPB-V58aPwEHXBeXbU2xx4ld8BwY329HvFbUY9veyrrIqzUFvGsBg4js5cA_vxj8C9VV5YH9HIKYz8MIfZHq-uwNFUZSenJVUHIofoow_Pm16bE28Wv_13xFxR-9iuR_2wMbC2CUEYVeH5FI93cCNWOcVdc37Np_akvD4BLj5ywMpAH97w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UED6xEimosNDBuPSUmnfP6drHSjdiMEkz5wsKK6DhgGfKbHXUHbFOCUp4ovqY9p5Ula0UX8rGZDsTt0XzcxwG4VLOjuFyYZykexPNoGkuaMnitRNxBlcTzXSWAg6iDZqyx-EB9L-ZZouJZewNuzbGiAifb5RiKXMsVaq0-vgx5T4pcmeCUFzb1LpTuYMnbUQ0w0ezpztoH9BwpyWu_QpPl8c4lVl6Ys9QsP_k7rWzPILunYIOGzhM87exfHZOevdxt3ALOtRLhpU4ooeyXQqbHd0Pgf6KffrBgNkCOEyJBCNyIPyHLzA6pfzc6RnLXSyz2AJ4OywlJRp9TCWX-6KLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knyAGb13g31MMMp9J4iJ33kt6XORfQ6zpK4lF80w3PcDxDnz3Lyb2-Cf2M4nEokKxpGSXGUrOPVdzMkZwuITmAxiOHO59cIfIOMwUQcqqLr0ocCZqv6bbzRc1hzKhLbkilraTAhDir0QTeKXk5qVy_yiwTEj4AKkZ0BuhRQ1cmGR_r0nkenTIzgNfwyyXeNGoyxp9omfBH3ZAHiloIDZRO5TfRqWMh63ikN1RjkQCuyUishG9D74aAzAF9rcrd47yENgoXi9q1roghYEllDAHH3z6D7q_revOjkY8juFY43VH6isHNFS5ylSrA8mbIiSUEa9z_BhUU-_uHPxbpTkaw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=uTRQVTfY20ZzLI7mAPji2ILtqxlh-4QE-M--fvlE3sDMt2O4m9cb3TaR6vmjbuDD2mB1dFiWaBL6FML5TnoCbMTfxsTJH9qhn_uWuYwKnvC5C_j_9XKxHfjZhKJDpFrMvddjoKeJzF58BKj84y_fjmcGk2WrGo1bwQzZe1qnz3TI_28wK8yUb3hdw71tScQrejWMFHOEiYkecNJxRQP41URGV-NwdW-T8ibOt2yLGaA0szOlgO1lSUIquhmgxpMiU8k4q01MBO8gRvj4JRzii3HZjV-YdU1ZktzUa6Sgcf7iPsiTVMVtO2jvrjauyIqQUZnm-4ytF4xVAvXHPcetPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=uTRQVTfY20ZzLI7mAPji2ILtqxlh-4QE-M--fvlE3sDMt2O4m9cb3TaR6vmjbuDD2mB1dFiWaBL6FML5TnoCbMTfxsTJH9qhn_uWuYwKnvC5C_j_9XKxHfjZhKJDpFrMvddjoKeJzF58BKj84y_fjmcGk2WrGo1bwQzZe1qnz3TI_28wK8yUb3hdw71tScQrejWMFHOEiYkecNJxRQP41URGV-NwdW-T8ibOt2yLGaA0szOlgO1lSUIquhmgxpMiU8k4q01MBO8gRvj4JRzii3HZjV-YdU1ZktzUa6Sgcf7iPsiTVMVtO2jvrjauyIqQUZnm-4ytF4xVAvXHPcetPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F23QZHx1L_keuHU41babaCn5f0S4AsN8z1A-c8aoxrrsEVAA6WTkPRt4YHOEnlzfehb2kSxftjcWCHSB_aGexa9M73QL-alEZ9-n9yCayAZp0sZPHG-K70v7qQNlnbOlXp4V7HmDxkxZ0yUQiUttfs0M_1nAgWZ6cG0BFqVEbf8ImWFvnXlZLTQEkAge8yINH4o98B8oDVUETD5PAxA1oMrSgNus-Gbc4i2WR8KFX68d8bbHVdpKyCoZ8syI44CrjqfNtmR-YZB31RcRQwiTzxmrre9MkWXwE1RWqC2X8O9nIQS97K7HaTN8kTMaoxcgUQ9PErUdrGpi581dFCK_8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7bjP8W_KaLCIMASC8z5LeTYkan7ohmjvPBZnRVjv3ot7zc_m_sDyh72Zo5HKdrimmFII_BxO56BDjzD-VLTbAdlkCN-C5DmnGN1Eu4LmjxD6zOV6jNrT2AC06u87ktJsB0GHulBlQeYQMP2QOv4s9Wj9e70KlLi21CC5W9BscT3TEl8QA3gm0Rlzjqi9QNzu6zQwG1cSQA3ykshpqrCGig-4mgHvzNw3p7iSVrhHHW4uPjlLwmx3b8tfK5u2S_yC63ulY7wX7w0oRFq5g-MzHg9edm0CxQZ5vHH7KrIStZmYowxAYcH_J6qr4RTpY-n-NGr915FL8u_vJ20-b59yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnQddRj0qjJxK2IjWuGWfT_-2HHhCayvFH5kugbJtVbHRfV8eyri-6K77uQp0ZGRIdnf9g5zsGt8qRY3PLRkfe0zQJtlWf2bEXsYttyiJh5OYZkWuMSEkPCCMs1SSfAc140JgPb69kWkw-6KiMYw4u6PnEOi-1AA5U6MVz8n9OIuiYgHWg-nx8resYJsGX-DVujjUkNiSUl1IopJO2DV29G-vAfzdmD6REhdTGj92LETYBfM4YJs_mNfp4jvm1CRSwgRzknm9_j8EmDL0N6Repl-_OAGcz-4jvV_OHdrW4v_FjCG9kiPRWvxIMp-hdnJDekmkeI4uHN2VO5Ob_Rr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1jQhO924WOPtEOb0JhiYyiwyzDm96azoIQNjAcR-sYExUnCtJ4lZZrkpQGmECeP1vRLJxHluJcaJVUXWeMXvWKPpWXhJlIif9bbhg7hf82uMwPoBqeeSNMebrfqZOsbOStLN-JW8iVjsOmBbMvUqrSsVG9HdOfFsz9z0TM1WkSys7I6sg2ZYN3XMkInCaTr5dCgveky8VRiwYg0YocfPx7pfzOVisvw55E10-u1ERt9gBX8S5iRa1m60xZJD8GSVj80rAdMhGt0tSHr1XDMasbMHQGK2qxxfaBY6U0u0SdNAl5FROVZ8njknd1D4XFxAPhXP_ed7riuqElN5CGfOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eus2YQ83b-7LB-RsUFZAtfxTjEDafis3bYx5lBZJhcU_nZOqaXyAiFxB8uYLz4ejLzNDvnk7hfnfRUW-tA2oi0J3rmkRCO0pENXdmw1l3JRDvHbri1rA-pD2W2ADS2vFgTvWhJp_dIp4EBOqhSleTl0XCC_2IAjzWASW-PkyLX1VvMlNm93yELtxw5-xeQhH9OLMHMfodhagNzSkHe0dJnPpvPm_WlyxuuMMl9lT-vJPk6BFMt_u4fZZy2QCp39FFP_lzbyD9iBdJ1VtikEsxxaaFDnh4ipJiF7pPTPqS2ni1_qsCB1m8-DrWfgTz7UuNtDP67R1Tmy9FrHCLfMyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlWuo3hc-MHvBd7tvWT_0GRe84edUCmg7RAOY0D8zhJRpKS0pqSSkKvyX0qobqZrgRXYzytqLNGpCm7GgBK68BULerAZLfaEfoBQWbMMvv3ipVM-dCGsbCHjDhXNR80x1GuZORTZby-hjt8EdvlCXoX-HFsD5tskJotf3RE8XNCfK-FRhron3ujiGFCBTBYDR70sR_ZNfeBWTTbEDUIWiFaKci2bQscpB2I607GTLjwPxoz0xABkni8JE3FjS4bRipNj5Gof9MwZYkPmx5wUn2K0UzpcQ5ggfvlCjTMyoyOlDoYGYJ0JkHdOTBYIDBnpySKCUZAPtJ7eF7EI76BnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKLFxxqbPO_hU_JzO-Hugd099HUoSwfZdYXxKg6Pm7w83ikqEcWq-flxBC4AwMwo9Bb-DGVWejIy4c6ZepE14QEE6eAIOIda8lKykzYrwEP_sqWFibhXXyzfBWLMH2YfWyBT9Pz-mUL6BQFJGIWA1odQ2DkzPK_07cZ2Fi1nOLyjKEGcKYP9EdyN3be81e7nikxaVulFFT67XmVuPUs6GCBlHH10_aYTSxcuzW7gYX7sFVjcVsaN24qRm66I-AhCic3KsIemGwQMUV1RUbbumMRZs51qe7CnGKu4OwOc2ONPDmYbgd3YUqBYeUc436DC8_QDKn9n8HNA9d-8_xj0WQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=SS3sASm-1hgpfSUB3LOPdxqqGYxhoIVebB3Zlo5V4x9tC9B-MTEWGAXi6FK_htnp0G0xFSqZDQvbXuLAduRYmAPoQUo9_4PdBFwWdI1FB-x55Ts0jmYbVXOLtgzpY2AFYcgMXNxZt2A4FMSd_ToFFs7roy2ZkAdQdPta5EbF0voyJUiuLqZ5J8-zCTi-jUmYoUJvAyE75ogT9UnynookGwWpcbINYXnOnYbSXpxX3vWJljsAmGdE0OfnDJhk1NNr-Ku9FgKlJIf8qRTSaaUEL2CNBQlR6wICsnciXl53nbpQubXy4qHWPQELdhDhHHsPQ7WvseG2ivJNjX4pzJ1C15SlMclZpBuW9OjYpbadZTKsM_XajoZEKTZIp8iIwixBMFFUWuhbrB26Pmi5Lzw_oadDIPbn_DRAjqLcTUA2Cx5CfE-ZEvZRQqN1CwcKJi0-CqV07eaXS_7UVTr9sb6FOpO73y0ffe3VyPNigXyzUkWJZV-RalakfzlU75JcIhYyRgs_rCC76QlCKhIQP5cJHY79xhSu0GvA_GXcp92Y_MNwVoatc-8pluZkL9No13j2fSLsjd1RFMaztNfmE99PsWVK98gAMgvKZa73PmrwkHb0cdsNz-y6XHepr1IYX_BCaKy4q2YIUdYykYPDI1anc02zNcxLwZbdLXq92VAaJZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=SS3sASm-1hgpfSUB3LOPdxqqGYxhoIVebB3Zlo5V4x9tC9B-MTEWGAXi6FK_htnp0G0xFSqZDQvbXuLAduRYmAPoQUo9_4PdBFwWdI1FB-x55Ts0jmYbVXOLtgzpY2AFYcgMXNxZt2A4FMSd_ToFFs7roy2ZkAdQdPta5EbF0voyJUiuLqZ5J8-zCTi-jUmYoUJvAyE75ogT9UnynookGwWpcbINYXnOnYbSXpxX3vWJljsAmGdE0OfnDJhk1NNr-Ku9FgKlJIf8qRTSaaUEL2CNBQlR6wICsnciXl53nbpQubXy4qHWPQELdhDhHHsPQ7WvseG2ivJNjX4pzJ1C15SlMclZpBuW9OjYpbadZTKsM_XajoZEKTZIp8iIwixBMFFUWuhbrB26Pmi5Lzw_oadDIPbn_DRAjqLcTUA2Cx5CfE-ZEvZRQqN1CwcKJi0-CqV07eaXS_7UVTr9sb6FOpO73y0ffe3VyPNigXyzUkWJZV-RalakfzlU75JcIhYyRgs_rCC76QlCKhIQP5cJHY79xhSu0GvA_GXcp92Y_MNwVoatc-8pluZkL9No13j2fSLsjd1RFMaztNfmE99PsWVK98gAMgvKZa73PmrwkHb0cdsNz-y6XHepr1IYX_BCaKy4q2YIUdYykYPDI1anc02zNcxLwZbdLXq92VAaJZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQJ0BlfnOG9JhrL3NqpZmmQVK1BGd5QgHHcJwBoWQDpcIMYR17a4AKljdJza2PwZ2dbGIH_WqudjOVLJefK_GVx_8VPo1_djfw-WoOWMzRzqJIKhwoOEIFuvmmiOPUHkv7xE3kEc81NhsDsIgFssPc6G_M_HCop7kSwcB6i-RrTJgajrBtiTCUCTac1n78Y16538dSg45fm5Lv3o-hY103LwK_Iu84znw7Jg1fziis1BFInJuZAFT089J8yyh6bCjXwtNxKAmI55SvorfsZzb5_nSwH4KdOJcPsXK8llVoTzmm2qHFAxUWUKCUmu_sQADVJjyitL-wS65F6NZmBmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xt8dGxOCDh79IfCxRqxUZsAWzo3gWrN3ZTqKcJNdCfjPQ8aH7Ld1aXn4i0Vh-hL0pXIDGHVz1l3ajDm4NWN-COJjczlYSDLtttvA500BUhOhQdFh0m98W8HpuAwDhXBYI44hqaHPejd0kGOurWh4_OU33XY41_r0WuF87E4zVZPmYDh5wN1nvjInuxdF4J2mPf0PCmdXlB3OtEyovAkBy6qWgAYXybjcAfWA_vwPMA74R0EUPgFFpVcsT_dKQdg3otx8XFrHgraAdiXOHODpj2Wsz3Ymi_xfYqQB3YD3WemWoEnOh85DuYm8vQQykhM2GFmN_GsHjBJjseqT3mq86w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Go-FCH0U4EXVpIKWZoGJqej0MvAibs5u4Vc4DNI3HvJmXsTIPSi8uONZ8VoW9iiyBlarAlF98Vzrc6Cthi0OQC_XNvCfHnWPCoBZ3skb-imIVl1ZSpfeyVk3LiRCOBOKaVcjWi1aSW_2yjc-R9Gj5HYbQrVPa39PupFrAaKp5MXRrR1g26L_m9S2UhYAiH2YeqEoI3_xMumoqfjVdGFZkJftNj1CVOw-U2NPjlIunk_3cQi5s7sEphRKx0QK0SuDZlKC_sWJiP1jJcmsT_PpKAXJN427EGa7ZmcC253uOKHjbiT5YJ5xw6hRZhVFVfZqq0fM4YwMOFbFv3zBatfWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZcoMori6XL7cKX0KX362SbXK1DZ_NjjSmv3b9O_N13lDh-SN0dYvQOoQ9i2b576BTCOlXY789D_LF77Ba6E540iyV8KHpFX8OClOt-mWTFcwTa7-ebd_XbJ19QK8m5EMaEvOshvEExDq1BxOTAczsfQZB3Eoh_PuFzzcRKSO5Zn6d4OYH_bD_-Q8_GB08DkOviSffwKfgwhmx9xF47vTwg09ST3h5TEMYJTjopyMkY82p9w3LpgMjAyB-_uGivixcAO3XL-u8Wqz4xvq3UdXpaF9ptHs1A9Ab2jCFxbznNCY1C6LnPdDszJvVZKixd0WGwJw7xc_jF5xgDTCH7qBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4GzXtlSUjg0m7wy79wUJeDHX0q7S6-g4UhhQXeOYAO3QI1x9cTKjKV3jxVDmoykpIgRNC9M41druFgoHmLJHgBaMbLzndU8fCtepylznmPLRpQMZ7b3xfN7JxTylIdVpW3_tiNrE_PtP2TZ2vAiOxXKJDEy5u5szqQY-pK8Nc2BFgOHaPquj_0-CkZ1XrGmpARzCAj880JpRxyAMB9Yk-JR0azR7mQ4RfJkT_3djcyAAWj1v7vSi7jmxaUQkDTAhn5bg-mJWtDsB0jYgFedVdsUg6mvrnqh839LsmwXvroFnD6yD_lqkzW7UmDQS7Ewoy_XpALZQSfh9eF74QANqA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bk0i0P9tR39yvxpA7DG5FiUJffy54U-DXXsd4ScyZLBqy8veM0z2Ge8PAU0zNEP2Gq7BvAtrngeZRhWusNN9u-xp2M7GCmKF_9k4jTu3Fuz0zJOExjqcMQrkE4PV47soDoGVp6Pd-g9jzuwvMdSiIEBZRrLRS9D-XkZxmZJXSPe2wMN4_A0zsR0JNrv5KIup25oLv_Jsc6-FEsuTMvxo3pwAM8LH9IlQo5vp10RG5_wLZy8sUd3xUk6G8N7TYFZOy6xyOrmiAjHw6kj6W5dZPeGzuuoP3jpVvHxcQz1o2ETzLZ4DwrWm8S_IGKRK2Kf2ejo90ap1be2FMt8bYnhb7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0bk0i0P9tR39yvxpA7DG5FiUJffy54U-DXXsd4ScyZLBqy8veM0z2Ge8PAU0zNEP2Gq7BvAtrngeZRhWusNN9u-xp2M7GCmKF_9k4jTu3Fuz0zJOExjqcMQrkE4PV47soDoGVp6Pd-g9jzuwvMdSiIEBZRrLRS9D-XkZxmZJXSPe2wMN4_A0zsR0JNrv5KIup25oLv_Jsc6-FEsuTMvxo3pwAM8LH9IlQo5vp10RG5_wLZy8sUd3xUk6G8N7TYFZOy6xyOrmiAjHw6kj6W5dZPeGzuuoP3jpVvHxcQz1o2ETzLZ4DwrWm8S_IGKRK2Kf2ejo90ap1be2FMt8bYnhb7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_PVv4QPz3sj9BMzUKQVm9PfDsP69D9bhv5u042Mz8gc4HC6PCj05FzQ1ekgODT1E51GZdRlTVE7wrXiD1XCVbjQoAyY_2S6r37JWWFL9YANfSrL6MNshav1WvuysDMvzd3KGywrwoicfloEiU4tDQf3c7O-0Y4gQqB4pz8YJEPUVK14Uap4wDiPHZqkEpGQyH5dOcIIKmrKn5IIiRu7OwnZFGVLgr_m8WqSw1J3pBbihL05Qv3v1opnCATz_iPLn3LSDjg4JaRTiN6zH1q6aurhSaBjrHycczeJdGKUvs59Tbm25Fr8cPaRJwwmtb9EW-mqrMazcSxhIesQWy9Hvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsl04otKpqOIlJEctJB8iPiBGmDUbqwMf15ZcDnyYRZTToB2x9Xl2iaUWR-agLtOhHVghkOEXWi3tWc2pu6-mCO6kf1-eDXu9GxA6M7A1PWbzENmKxU8rrVyNoZFcMWsXjdi07k-jj8NE2tNHmW6uFnla3QsRzhszMJheBMQvS-zXHxE0AiQ-pWGfhfb5JWM0PaxSNnCwL1tjA2hu5sHPetSsLJxVWudcxdkruQetWPUUC28Jh_4G13UsAQM7oVuJC7qndh4oO7SldIz3g0b4FsRuddMnfx2kiUv9vi-i-HN3kNJJEX0E64aQtWyY6NWTztAqM_NxSgHKabG_c-icA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipc6Hseo20I6T9ef_KgvQFdaglSzrSigWCYbtpfNxePWJM8Y7eNspXlrSeqrXcIdooV13Mo-V2FOGJ_QnuBGDG7_400k7V6jxt6d0DxYa8G3XzTZF6XXzQ8J62q9ZXAnE8jEaemNGOnC4NqJWN1m-SkozzN3Fj2f9njEF8TKModsQXlVRWOWWPC6JO4x3yKe3NToZigL7ltRZK9wjOd3zgTvTBx6sgqdWvX6eSpRaD8XWJCLJ_Du9SvEZ4UGBAbkLW3HtjGICqE4se2jaWVHXWPbtkSDne5TW62tSDhKI0goDkcDtl3602uicdLbXvTLrhIJtchoXIop7NlGWi5wBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJZWd0MSkFDmsRehHmfBoRRwnJ5KZo_ptlDfZ6MAWFreX0nz2A_zg29NA1cObER71QAcPr1zYc6MbIDpwa5CabF86UeIuebMjr5PWhYY2JTxnfR3ufyTcCPXEDWUd2CvUe3s4Jtr5oR8jMa1GxXFwPwK7LCyq_ZcTKfKHY8nI2kF9IUJGqgo75c58TDq5CEcNSanSNRHrzwv4r0j_PTbtdEVoAvUQSpqVF9LJGdQ2lolxRNKeXOpdQtDvd0JukRI4jxeChCXQchDuHZ0oTgV1emCKqP5WEFpf7gO6ML6fRKJrUDfLvma45Jh8yNw6a9is1HTIZ-048msDEDNwK2Fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOCSxqFpMniS6Q2eALQCAWcqj3vk4MKflcTt13RdUYDfeYwB_ocuYCQHbeoxdK6VnXlxYYEcKjrlPdTpeydC5pv39Me4wSC7S3xJr8_Br9Kh2C0RFPWk-o6ZvbAy-w74iMlmiTPUzyk3T_2ans9xxSSa9Sh9dSiWOCac88Lhd-TIfod9gKh_l712ABwQHMeOdke2t2jCxg9OpOq0lhUi1MuC9MDhE1T2c4KI_6A68E2NdqIDq8-eOyrHDBOpdYaw8ljzXTkSNhFPPzvnjwZrw-fQc3AudEcWQ4ZHfXNOZx4WhHIDiRp22OYqQz6Eav0NPvQoJ2P56Q5mZ8cUDcFTHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnibPg5eXX01U-1v6lQTLwpy_j986ACoXx2KFPe1kRAJT1rB3Gz2dBDnJGfS0KRgoPLCOkpOxRhXxxx3kJmHXvmOf7UtYaka11mP4p8uWjRN3WYqgEid9AUfPRCgtiL1ha8lDw6WJAXun4sIF4AdbMDq9oe_mITGdIERprGEK-WOs59OHiQfUBgzbXYg-5pdQVze6Bj1KtCkc6p0EATtJnF4MkwNPqIq71WreeNX-NzozZnrxIqbt9iJ4DdTNQd19GdF1Z-edSrIAG9QmAnDDPs4mHUCK1duM0shVCXlqUlDLBjzKv2Zb7_bSVKJmnL6BCXtWmb9ybe5Zp-23LRqVw.jpg" alt="photo" loading="lazy"/></div>
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
