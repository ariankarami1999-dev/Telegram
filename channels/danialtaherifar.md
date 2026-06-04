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
<img src="https://cdn4.telesco.pe/file/Bma80hOPrPLpPp6SsjPJAxqgKyQ_1s-f2PAXbvNiGvJcsUWKsoMJvg4Kl4Tr1JaJbDaVy7pyKVm4vR6Oevd46hbj6RtOpvrXZeWWgo8EraL-Wy7z8Azwp7HfbeyIeE5BjyexTbXL70C0ZlnUYLvoFHWtl_PF_pX6VM4p9FheYwMaw48IUIhTb3EQ9AtjH_IZ_NdSQTjTjoMDcr_ZtVydGny9xnAA2wPNFF0CZRzeEcdXVbA6ohbRZkXvWy3miMh4PtHOkCmgVu6MMTpclyaPVHDpcCKcUtd2S3edLTG_F5-OG7gbx91hAHuGyw3DKSZSzx-XVjJPlQnwtl34aKZcaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX5JBKndKknEQUMEuMjQciZYCxovOkDSV6ZM4Et3Mxwj8q0md9nfFuJOR2Q3ETyI6TGvoK4oxGK_G9-vaZQWlfkOpd5d4aYW6rJ0USIGh0T5MXhBbvy3yGmJqIOeePX3oa5DXHYPx-wfVgsAtBTOV5mlQjJIdsjnJRTANQl2emB26-Ll8QL4D6Ya9VRuTaOuNktqQ_vzhhvDzgwUTDZK3iDWwDiBM7VQ6HYKuqxtehm65dGX4VhDLcgERcbFozr3rM5fZgtko2pMHvwDBHAVPhuV9RO5ilE5R6sbF3DeNjqK5Jgq7NFT2TxD0E3l4k_GyQV68UhmjnHN91VsmOrPSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 190 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 461 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1h-LL1R2dxLgZ7YaDla0DAaFeC2D3LuVPtwt7ZWug1UKr-d7wTDuFtdW6Tz04vhmM43epWBNUf6bvMaFYIvp8kmp6fFxofqQnyEWlSvDruHpjI1ZBireK2XcyRePCTVIBAJYCzb-ks2TMZuVZrLcvncoCbVnKAXxmWqVM3fl0aUzql6qiveuh3aDzXL0_3GWKyULr0G25At8MHUWjbqeD159eCyf8PNtMaoDpIpZ8a_hsfhvkYXRDos3Z08b_MH6YUY6z08TxS9vgbRPQkkk8PZN86KDa8QMqT4WJnq5bsGbmcTOTTdizLzuqbhmIqt0jwl7R-GOdyFPnX5WipMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axEO6d_R280I1cAFfz-HsDQCZaIBR2gGKoEXkAlBoXTV1t-alpkjtaHkxH15PhcUZl1qbRNX-I2VsByzss8wD3TziR0kR5TYpfmyQijgTfDB0bO_Y2assgMTQjNcxMSPyQubTld4jdnfPBY7lWfFpg0RXdtbQmYoOheWTgwrqe931rA22GF7Ey-nGJaJTZavKxaA10vhu1kC402Jq27G65qOVg6JsXFIBsdvvHveNG0nyVs3bH3lB1Y1cP9q2pexn465MP0Xq7RcMcFaBKENv1pkMrxxfZT7_NvbKlcpgYnGgkNWk3kyDQxk8Foim5MM-YddmDqJmc5RUhZ-TaoOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGzVuc668Byk3bFRB6ppqrehKCr5Smi4eQKbncgtOzdQuKbL6cCVJhV4OK7U940Edv5U4pYYn8PqdQCsQ_-xAJTNOKmkSQ87fuRbigxonXdyLOiP44UKctTB4Sif43vAgfBya7hEsPEhW75iG5XQq8c_hdAzzPfS2nbia_SauPzO5vQpu7-ETJljMOqSWWrt7r0yeSNXG2XRIAjVBq-40zUeqeBOy8_37LV4S0Z3ggpbEQUefmf_hJO-_ugIVGnEJPKnVoVXSAs13k6HZqDEfwGPJt1dDOM4qtVCcrqbBfAN3YazAXwoJHshuzkYrP6foCOOH2IzOQn1ClkJRtTrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeTbegrt1wtIil3XfVhu5rv9l8-HQL5_It7nw_1eOLjhn-T55rLfVzwt77klWlNvLgkEoVgAqDX_PP4p2xcJzaVsoF0L4fdwZX26gBa0ZBhMYAbhOe3l_O_Q2M0pkhnR9uzQsmv7XXMuIzn_I9R7A9ktnX4oAI9vXU52LzM0tdR00FOLZeNa4Ev5bIDeKyB_UykVuFSOiMvcI7uJJZBGtf2xP4Nfr1G9RuCTIXHZ2DcmLDNoEiwJMgF7zeUjDHpN7IS0cwZpJfBf0Tw90mDBFTPqG-5W0PCRWmKaZHeZuPDsOg5etgIITkY7PQzxBHyGgWrObIZBEkA3bjVElpUDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxc57f_IklPEgTB-xCe7CGjeK--mIL__3sN0tYQ6SAXzQEGkrRVEP7P_T035ZnjZhekqDDFOwdcvOIajWhJtrZZbSEpnj41Umgbj7lrGX78URrw4CKPNl_8qCIMPnuQP4UFxy1CyP1bgH-Ja0kK5wdmmQk-n5hvpfFyhRZPNrctDN1HDF2XwYN9h-DxTO-KzZ0f6Krug0DC_C_N1uisaK3Gjy9A0Mau64hKhETtQo7Oyd1T_4u4mebzP1q8kRp8-wdMy5u_YDntZeKafeeM1OSQplAXb2zU3IBSyeAYwUVXqtybZ6UKpJrWJRLPOCaSV6iCjrNWF8VhXNK-cnIhynA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbg5s4j77ELOTP6_NeoQg8g8tLe0f-mTfGKnRvHboB5heNGmHO3WFpcAo_CEOPGCWsOVwaTTjuRAYC1MNSKgrQdDwiEmJ3rktk7h-lJic3pThZxulhNkYQh0rA4YDE_auUG9UGKFNkaKO6Iza_PYbZpT8H38dT7pO_i8KNcyE44gYEaO1lpuF4fZYqXSSx7l2GxYz8rZbqgGnx8q3IMFZPCg3LHtAXGzaYiVJTE1PvroC29u5ZMlnehY3SGJqydAF78xChW3ebO4qAOt6LhDtqbNi81FtAtdiBLdV9X7j9B9kzwtCmrMCOx20MxPp_QX2Jpo4U3hS5d0adviLSXa8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKnzTXk2fV-K-fmc3CbzrlP7tT8bV6e0l2kNv0ngEX8JW2ag45_Qrc06EH3VJwtsIzh3iiz-KJxO-Hq9qbGg6WrC7TiSEPslhQ2i36_eEqGrMtilsR2xT8uOvfML0ouFcdYA1GBdnc-9sMmMIHBb8b5kGi0eAoBpm8V4SZtR9wlxh7f3sTZGRegWprjZpb6T-XKMBcEXcqrq848d5ugIISbbfGzPPpuFqMqTevABSX-yMcQQNZQgcen8riYt_UJa0gFpU_RV-SvtJSM6LdDT8NpfeEcOxbE7IumHK_wmkRfHYNev94YKy1KKR5nDTEDyh8dNWJYrSeBiiWeW_i_79A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZH5bpKgB3CXCi2JYljsvOK655pJVUIgPWcQgQ6jKCHkxrJKD_sZN27lnR2xM9WjoXZaElRYq4TkH9tx3QgOdN7F35566ZnbAprQ_96sQBJvI65FHfWmQbmON8kf-5e5_Kyv1EpB9N-ofVlxHTP4OJw4nf1gCI2zWcA8ZVsC8XkMXKKBK7NHSdyFIsfZJ7cdVJwK4B6V5VyBjS7YzP7LGxoPFDZYTi98zwfT8Xm5zk_A0bnUwY4fa26VuxzhDcSYItHcHM2p7S3oiQ2Wx1XTNeLzTWtQeByZADYvL5b-E-bxSCeZm41mBiQ_h7a-k9v9gXFa4JqQ_sQC1h7ADvgSDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaHpKjqjUZIAcqISvSuBi8EHdBIKXBNYfCBmUSigPg4XH9T0WZ84qTn0aWmaXPHHw7IsjPfwqMF5ZDPb_VE9MF3TmpxTfl_K5k6WhkIj2MPaMHC3G2BlRrDhRPC_ej-uNXetAioV7SJLd85M7wpEebpdcHfs6aP09raj8kkdPIJHyIM9-oCD-a1rZC2FgqXsncXcT3Ua7E0Kim6w5vFG-EYR7OBK8eDs54r-gTgOi1iqrFkl-t7ena-KAJmWTkndz7zVbovtcD_8Fq3eFi8kTfLeRiN6bv4-cG8TsqeMTMAlyjQNRSGcxmrlR4bnG-KN9VRxymkg_8TYPiPmiYNQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpHEmXK9rjo8ugCrigtUYC6DLqVsTzEndobNfQtVKHE7LD57d3ubMy2k-IQGkMm8eGpu4EVGurU-hnrsSP4DYBk_c47qGAELi-gREb5e1f53J2zDbwwZc7XhNE47aEvSq_L3EVFUiXBZVtMWLsqwitubSXAT40DxBAZ-LKrueDud5vZWNa9K38yWRPdP6gXyi6IzEqkJaPxiL4crZCmipvkKlPsmdFZ9Cg2owYztQ6jvBWymlyrG-H-ifZwOsZG09PF5gUb7dVvMR0V1ICcFmlRwmbgaH_ccDp0Wb9eV-RVe9kO5gAjIn-nVslDEe5UyGsZ7vEjSJNdxkQjCYA7TDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8mrYBPDrblqsiFuVhhrZYcMFO8ybRH4yGkH35g04_AcEr1kJctfjshzakEJgeKuaJGmk9U8ZGLSo3-XR1NtdQGL3J63IMvBvfrR4TbRgEuaNZEIaK-v3rkpKgs0Z30nHBrLMIpoKEsByXivVsRPy1GYyB2U2K8XHIUTshuh8Z9z0P64-aMx0Q9AivP6pQ7MP_vQrjyo5Syyz-CGaA4OyfYiyHykoD1Sd3lol1LVMJ7zLToKERLP5ilnQgymexCBtvE1AxQkSMfA9AzabX29ER5lBw38f5hFoOuAE9Fw2fdG8n1_V859SgWuvk7Qx4knHIZe4Qxidcwjx3OUcA1MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxijZlKOdEdrLhZLO36vQ3whETOUr-rur8txbgxNKW0ujsIJHwySb2HnB1PiJbXhuexKrGFLy6UX1SkiFuo8AAN1bsigYfztJ3EZ1KHvnICb_gLpq79alZ8e44eg49YwSp9PioV-uYq-L0LFXump8MKCA8_Uq3P7cpA8w_y_IU8EqiNGoUjeZBlxBainrdcTyiAa4JxQ6RpewI4zruSCK7E_xWMql2eXEupbdzDFBRduGjRmYqM7R1vi0BhSyjyqnlR0-JLvteydGAG_v4l7h5pOSFe_KRE4qX_tcFe6lKAg1sh4iysXiycopo6KKyn7Kb_N0vSbqecswcEE0KJoXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhv90ilpgjoaMfe5holyJc2LaNr8sDYta-R2kPNODzpqdWyJAtpNcMlXB35yUQQOi9JTLoFhwLrCOkrdA8PoUvb2NWh9gYsd5to5-VHYT8thrZzVT2_bGjsXktNZ_q_kt3SN5ViKLffSIJ-6Zm0ImrSaWgtSwR_rf8etvUPbcYd6fZpP33XY6_0mn8S5u6kKR6ZGKSeTExkBTeIynRVyn09oYRcXw742g2oXUchfHvTEex1hz1IyoK10cMo0RTLSgh2CZqzgM5vjXzAVNufM7QID6DqPdNn18uYdZcWhNIlhTmfbf9rNpwTUJ6U3KfQ7aE0cTVojuftIiz_hJX5wcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq_Bs-vbdMBql80TBZtN-kA2140q6ktuqpIp5NVprRyeDPpP1ZvkatpyPrjZ_9AfQmt0yOw2gsj4T6aZmfb22xPkI96d72COriTZbuLDT9SYw_EhUT4Nb3t4d6v1il1O_l1QdviyCl-jaKN7SFmf7PoEFhEz7LTuXlX3Fozg3M3IkTL2GrzGLhyArdyf5h1uTZBUWw2y_OqKGI2KwsTJ0D9YaoDm7hbjifARXMAMlU2E3F8ln6qk-jjxmgX6SFfLJq_lVeyxJoHWum525XvlRByxBhLPdscJRh-KJAXCoJf62dySuWBK3TGSmc7JXec16M9gH4dc-mlqAnxNR_chcg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=b0v0CdZsJIofpJKmA1eRboRVC3sj__t2XjRttX2PrYsha_AP9NivRTJiegxEMNCH8CkWWKxRfjXeTkrkZ6xdgwvPcTwjmLvBllNibJpJGAAaxrMugHFmtzre_WjPTy0MS-rV0zpL8RgRJZ-KQga0X_DNul_yrxTddQj63goursvLZ2fRm5CG9HBbRcUDxzmIz6N3zVcO1dYYxOF8L4LK2b2QJbqu9bn-8uMwE3yqY9TEy1IeZ0_oIBFIhrtkaAqE_BurozHe4akcd0eavWpOCrrQzs43KN6MGg3o-mowm8xDcyziCWUdZfuk9l4pwewbi5f8SpGxSetkh6Gsw2GbJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=b0v0CdZsJIofpJKmA1eRboRVC3sj__t2XjRttX2PrYsha_AP9NivRTJiegxEMNCH8CkWWKxRfjXeTkrkZ6xdgwvPcTwjmLvBllNibJpJGAAaxrMugHFmtzre_WjPTy0MS-rV0zpL8RgRJZ-KQga0X_DNul_yrxTddQj63goursvLZ2fRm5CG9HBbRcUDxzmIz6N3zVcO1dYYxOF8L4LK2b2QJbqu9bn-8uMwE3yqY9TEy1IeZ0_oIBFIhrtkaAqE_BurozHe4akcd0eavWpOCrrQzs43KN6MGg3o-mowm8xDcyziCWUdZfuk9l4pwewbi5f8SpGxSetkh6Gsw2GbJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rna66F4f6aZggfELXKKoQnjqdhOmU2hVkoJ-vFMHv5LGsRNjbkHdhX330B_Q3NdheBxQCZKyHxhJtmvHIieWoQ1ouVmUSmXruriYmdMcpc0W0WvhYfk_hvZD0dUpPpvNXSQG5gof1W2Sx_swwrWNTzhjkP2a8b7Una2XPOAgajaKQ1Pp9efKTVRwBCau8lThfefxYjDwIi8-UyTkOcossRs9KP8HswUS_84iAzfvGkn92rrvQQCsNrvMbHjsA3JIRnrTICKSU9aX0muwqJ9KIic60h_8AkG7NioAxZUNFoVGOU42SgcfVdC-SPfe8GFER9eqMCYvHDPICJtltWhmow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFCEdbdB0DGyt7KRZOopkQpThajKZ9runi6KscghX_rFcVujFV_qjgq6VXvd3nmQzdfjNChtrtYzYKqe44FmkmyQdeN36DGBdTyjwj6O5cErPvlx9z4Tjsgh7Y4KhkPVbEpNKdG966G75mzCbMJGVds879-qXoqT018vhORybEhPTGNug2_hfmbijumAT0aluwXDU37VPMUuhMXzWE36vbMVtlov10C8geFuuBD8DWX0F75tkKlMf9nOmioYv4v8ZW2aGdbuAd9EO1h28LOquj4Z1xXfjWEHRjOMUo1KHLrqmcI60KmHiFnglm_MjDiDICRamsCwOid4oQl31t7q6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t53X1As5kamiy9VKWSuFJ_ZzxID9ICGs44Al1Rf5B2hs_h62RPAkFYMP50c1DriNjT3XYrXk2QO7Rf9vw7G3HiHYiAqP6VOIsx2eZEhvKj4DqgvC4NY5UEP8DpBK_XL90-3K806QK24pzgu0ZB3tjzE0xc-acdwn4AIKkPzHErFAiJaX6GQkcDmaSvPI1tr5q-1x11faa_g22__6UVd21maBylBSt1uQXsymiwPAV539rcEZjrlTF5ZAF7sQTA8k8Y9ehjTnY7h7j3ps5KuHCn00DZ18A3uJCmtVKqVt7c7hEMzLzi1cGpdtqs8wLMeiQf5XbJNHTeB3VdLlZxhhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pm5eVcRam6mtSoiWPiUPw_Sl9_hdOIpirSntIxYeHkglsgAe3wqfgmz_JOHfFaWUg13lJRXDllicQX2yR-hxzDWWogwARaD0RPuT1WD8t0Gja3kZKwY2lIhfCcZWZQFhB_jMAiOxL5xX2J3mOD_M89yaVI4CcOMicYfjEHCDRtOlxY-U8bKtCODOuOFDLqkfLFSlCpfy7KF3W9Nxo5BQ8vrRVSCervVwnadUp9pv9k2iRv1pLDz2fg0KFSS339phqy2bhLdJPEBZDi4j8DA8gkrURW3dYArgRCdjSCtNe3J_80WQ8XTOlHmUqa9-kZw21q31dY90Rv1ztswGQ1AufQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K25gu5c5dYrlLRKjxr5wR1gqPbAI3XP73Wt32gV3sHucwDR2YVxeSvPYaw9jIFZghVO4z6-p1sokTSytM6cVumYO12TcEJHBKoiZ2Tv0HL2z7bf8N8P4mRzcPyRc4Fmu6C7IElaX4e_-tkENc1UmMvuGN4k67zXAtIJUT0Av5eEtig_WNfCKRT0i1Bo8h6LLGN4VdthwVe9eODHA1dZ0FwQjqSUfhbYXK3M5G5sqnvGjPxW-WsPdK6VLSDqB_m1f3kegAahHb8SMk7Rdh2tZ6U8kLbO0FNAJCRVYdfsJbaZPs260_6Hb6wL-G8FpgHmvzeqmAt2o-XP7SKVJdoALYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYcmsLlEM-_CCGNmLfDA0hqAEJmIg36FFaOEgMKEiemfzOfKZ6h9AE8QJsW1gXLBbp5O7w3VwD6wk5CKlckCXg7nN-BK7F7L4TFKfHSNWHQLo_trr0y2kQWNmADjue1gYaiDJ7xB9TilX3zNMmB-knCM0j0ZDoVTfTjidIA0nYDNzMmQ_ZDwJFoABLEr9XYSCrB8OT3uTwsqGeoXxyAiJ7Ufe-SQeEVQ1wXavwjV4TBimLGUqcQi0SVrT1TDsVEGL7L8A7piD76cXERyB4Mawx9lVjjGdHyp_aq_mdODB163LVAuBFr31YMY3SjMiaj83K_n9YrDdc5dQz257gINsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m49OV9VAsgmtOWtdKyeTAfbucmbZf9lY3wEbOIyDwWyVJZJX36TQAvrznVlrMtWUGqU7kK7G1CzlZVJ6o5bd0qi_q3R61KnzlH1AMQBzpz7o0zAf1QKnbbb-m-gdr5HhHAzgPheZtkgUNcCtpeRE9atAXG4wuiFDro9d7M-JW6HQt8HURJeViw3E1crgfaRqReaQxUOAGsHO6FJ8hYfInNezWK2EN0vDIm4aKR9kjCW10L0ff206-6AS97I4t3I2avgRmEpZwdOrQ_Lr4LYkUSgtDOCHRsATcVhJVB74llhnqPi9zpCSsCqJ6H-AWRnQ8pZ20Db6EYcqfMbhl8suNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPudt1dYuNSBQ3pacHp4QmGd17VKm0qWpbCBvrHC8cQwYvB7bVijhsM3tsx74EGFowjrysE3TQlwhTcZKIV8pG-ubrprzG-SUmjWeV6iEAQSOmxD1B_bwfiDdL_CFpXygrB8JZGpun4-SThUx1MM02eu2wbebVRQubNflZFNW8tpecEFzOzzH7J8IGF6jEXjsJyc_DgTppnxLwbvo7-Ha5YxSNQCi9VgSVmKlfiHDjoOXdXzsiQQHzJECDcTR1U5TJuNOFLNUyvMb2uf_tJd5Jz5nWHLqdkTNvKpzH834cXx0LzpgPi72kxyTBlZtxQIzaCngpKgt8-_BSnGv8DGCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Odle0ZDDSCihusxOrkOoO7rv5iShnOc1vp8O-D7XRwf-8WLJIdoC_VNPOE5voxrGzoFcy00GmtRSC1ypOectA7HWucsrGYGtG6p0hXzNyX2eqZnf3iGMKpgOPcKE6-0Tt88fxwysKxT0OCxlO4KVj-JnBinx1FyaecRNG6k6TBQ7w1gZjyvVWQ4hK9ufhxiCoFrk3pKuSvrU5UWaud5EWYeQqZHvC9WmVOWxXQZ6uVwuQyS-EbijAYgo06xA9eik8x-W6oPgRjF0tshDWdAzLrnHU1IptecyELcWS11qwfAs5VF5XEuK3m0KeElkX6-n6cZkxU8ltx__xb0mgOS_LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS6aSWhy6_k3EA-uj4NpgsGojRGQO6jHU-Rrpv0NfQS9vaRpKiEHVFJYrFFd-aUNkcIPF2uWfcXIJ6A58DRlVorD3TfH-ZRhZALiTj1EfNU8AB9twg-zcSxLVsKwKH5ahrNwyx-U9B2OIC1d1wQjPIwPrf1q2U4llqIzFGA_xKqouvb54H4LK-GutEhz5q5kI4kGa0KBjpkknjPX3iKr0YvsK3ELmKXhVLIgPC1KE8szMVcqXRw_-tvONU0gt8y-ObRHnXRSf5TSV63nWDZYDckGKCZFi6a23ho9a8rQhsrGaZCzigA1GuI76S1Hk-BRULd6_Dbm8pKpao_B6C_F5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODjlneNq7F_di3WO0OMeedRhCLNYB2sHMoLiVoQFfCl25LsX1Y3DgD1bgB3UQjZi-ImfPro0aZDyruw-ZFJtyBmtMVyIGOc5Wv8s3WZyQcGcTm4N4Iajoxuf7LkhhPUpsMS2I6ufv92E0iESYYvNqdezDN3iKbz-MtYCVcuwhnnV8AQJgPu_-c4qV6hBunLV6-CjLoN8wlfCwCSPcWfcmL7TE4-MhFCez3Bm6d107NMfEgTjKktlplJQMi1vBQhM8VFllI7gsHou0Daf6M7mvbBxcVh8Kg4SFxdC2SGcXa7DN-eB-rtjn1Y7-v9hbMTpsSUTbNLQsgATQfpBbl0xzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBS1drClkoXUaZL6sGnyiv1PzQrRWJ93dHOezCzDPn4Fcs6ZOEHDEaBwzzzKzcK4rYvbZ_TnFgxxfI9H104nC4WBhy3_F5mssE5U_Z6c67dqVX4_HaU8g0D4wweWMH427pVTu_9-hFrxnAsQRVVIJU_MKVIsSg8BZj6xa3_NeLXo2lnkNbi3_NXDj8rSUPg-CNcw_Q8ZWci4yUaGW7biFjaA2TXcpzGCn73p3fubcOx0sEHFMjuKhQ8Sd40UsOKX6x2RPuy1HA_KZD0vW83lQkpm_sKcblMQJS7F_D_y4EzH5UNiV-foitUZaaT07BtVcDPhnot0zg7O_uw3AWBqNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Az-tEeC5vIM7zWbhTX7GLD2DE4zbe3XhpD6H5-o4L5esubRi7Z3Cbl5PaCk9oUHnyrp6xRpxdzXhLA54G710bfRa6_4mHTpl79_GC8Zzt2Ex-gGmpMYFjUw2UXb6BDa_ahalXjOgEMXNd1Yy0ZKw2Yt4_Rhv9ACLuFaKN_aDqkPp73x0GQ5QD6ljw9PccqMFApGDNY2ScUbYVKwyt0WmeAt4biZUW-8s9-MNKnuh765LZfdRCgiKO75wttsN-EWGyUzhLia77VcLYTXp-Vx0VmuL5zVy4eRXOq55vsRWb4Yt8a3Z6taX8Di_65l-6lkeqbU3x6DvG2Z8g_CmKQ8ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSIPxidpzuHxP2dvTu6wYLjYEyvSrAzY9_lLfCW5G8g1HLQ9deLbR08BZqnS2kCCIXNcX3PlghqOPbBv0ZrVsKYs_h7dkbGGqz58BiepNIt1K5deG0BTK5OsqI2pwW7nhSuj3Lt0P5abDePpx_I7r91SAR3lsUjCCpc22afxqRA5XSgq5vbscFw1YrZjKP4L-S65UN_cBbjxrgMYZ2pOhTIVIGktfBDF7lUai4Kwe6jCKRs8XVsqexLyObsLvEPRVisQtBw9gLVwPz9vc_aLUWdazvGKykD49p7wMx2o9vLqOXidLGoYc7bgYuV3_djv0KIxYdiiZoALPq_6_0kd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAHayFW8IcVYEDivs9taKjAf-2BGdHbd2g5rKCtwnkFz7LAtXo31q2PKaeYhEpmo3OxXjBfQXRjpIAfVOx9sUcCTo_kHd0QcvymA2z0uKLVakRUFJnIs7MmrUNfKKWn4DBCYLKURgY7evsbc1Kgy_CMmneqW5-OR2SZyPM_Sn8TeCX0QskGsFmiyFwBVlfkV4E_n-egfXeefq6BeawaaKdTsJcmDCm3ESlNJvM8vSlrgoWmN_e9Ro6kcR-yv6Ily46x2E-qVGqu8oU9GyvbPQQSBwNTAzQcWJmH-kDbkjrQrvJ2qmHqrRV46tar9ItVtv6EV-4SNVhinxMF2KpkTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utdVPq-M8zR21rG7CvgS7OoNOoFI72LB5QPwc2UgOIwySGO-pkm-FK72ufUCE7gzxhbBGWnXoC0RrbaFqM2z-9DRkTxIPqWL-jFBFIIAcyGPkNcHihM_OF6-4arQXNq_oR-rtYSF8qmnB26RZScqgDVGCCO1IpESiJnPVFuIVUu3Ye79MMHICOks5qjaaF4LzJFBRYe5VkVuWc48rZgUznpnw6HZj6CpVeueZbeiRXT-dl1uCwedZRKKxHxO1qJ88oUgJHmsuqLOP6EHd9F98cmUCw1fa0K18s_JS2JrnBLJnMOKZ1c0H7yuOVJAEPqnY5SxG14vq85rAmiW20521g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIAQrgrr-mrr10f2x0PQaKxJBzfjmKmR9b9w8M0r_tkPjxR-od2nWm5LIxolOmNPVG7hChkuSvhnRs-nquoBMb189MO2CSPlMkOtSkRsACs1vbmgHD6M5FbI6en2l2OuHSml-rpDeCEzfQDwomgr_EUx2qAgQdq-ZlfrCHPnV2L7WyYhbLbUcRJC3Ui86dT3B1ZqsHTuFXtQqcyQxxRR9UYOkjOEMcveUmmr7Z6bOE1IKpyt31QtqCiJZDCBRCrinRd8hay49fgOxFdeDc81X43rQ9bak-WKin9UcvLAovD3mc-8zQ0JX1w1kRvytzpoD-Cts5SY6hhT2NdoNFcdgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIijQe4tCkDeXvV89HSUGSJS7AjZWL9E-gRRkFSe05Nee3MiV1ciUW9kVzoCwNHaG4_FaJe1ZOWbrI9mZWZ86JWw8OmCUH2mvmyBQLJXT7w2DQ9shb92I-au8NrJw1xocw-ev2Kby_o2EXi0pjbBojS0n94IALpp0F8h1SVkdjl0bG3KRXrnLPfDepsZEDRGPkJQrFoWC_F1K0PuOpa3uXsPWsTrEvFLfyxcNQn46rGjyM3CAOBVZjR4-rmXlcWHChbxgvJMfQjMasfHMX8Ud6zaijR3hZMqrn0fgg-HrYDMQFP6CnSwKAmHndFYSo7rpcWIkttixxypwra2lI84pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izqRfcXE7jq1MUdNbuAj5ZdfplChl1C-errQqHOxT1LBE6Od_ObfAjkC3gth6HPOsvn8tChcxfRVXDDvKvUUZ9ZfXMpZ6xDDIqS8k5EmTWLorp7HbE5IRJsgJ7-lQ3j3FSYXn49Nd8c4GoIbNijNJL6WokKVQBSB1GZL9BikrybdGvYMy_4730ArHmuoNcp8FnuI7B4IQmqtndgjABxc2UQ0AA1UHOj9NlMDxyUb9roDCfAq5b64aR-9vpUkmh8lt-k9gpK7Z2kMZp1RdYIvndY0Y6sripA9HN1GWGw1ObJP-K6BZ1xGfQmsXKcVDgN2AVT-NhrTg1vuGMCh4jeetw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 587 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq7A-GpMfotWRrfWxHVQhxxmubWsStKBSjDnMoZNOYESt9PbCCuhRKfZjGdOp-6dfKZecnQBBLErEakhgRnlwMyBcZ_4z90JGHYxjgvNVTCrLr_1OdvhvYF4I-Z88BDxO-EX5Ywkt3gbPi1146WkOoF1dA18BCUdpZv27IR49H-q42EVqp-oG2-UINI4ytQLwb0AJBI0dG0hmtBqF13I8_Ad5JCHj-z9dBB5MNJTfLdrPkBx4MhuKJvv83XpBt1TfgBFBSeKqkmCOd2b3cRRCJtBNzTf7hGKd3wrX1nVQ2wMRH1hxGqIexUfKr01JuRDXLKToBCEKar6PvilpRjBbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 696 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPAbhEe4IyHQRKbwNDAljJfXmh3srKgcMm32_GuZ1xtncABjMDTJzWEqMoEuqqbU3OfzLifWxQFArwf2g82xdN3MYcen6ahyInk4JpkDiSvTc84bGzCS_Af3m2ybKrSPTih1zlcEDlCBF3bc-6P97zA_ipEbxqY-xhD-x8puuYkqBeozXRqxI6d3ezXWdAT5iHwHc9NZoOivinD2oZzIV5bTarUzQNZPv7en1AxOxtfmlCglVv2U7LYG_SiiLubqJ48COJXX6fXjAkVq-tOUuSM-j2s12-eMiU8wEcqYnB7_TRsmzT1Jx5Ka2f7XBTcAzQHMr7VhkwPqo8IVn4z9GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrAs0rANsHBgruoIUid7OmPMvtZmcS3zE7f0tjOaNr0GDvA5J_CZpAfUeeBL5ekHbig8-xMTnttHqqkOEYLcrgt3b4jiaUFPUunNlL546VxrT4dYo7MTeIbPvIuUDIC1T-_hxt26N5c7kyEvp9THiALzOV9PMFzSOA09omSb0M5-yu5WpDWDDL8MJ5Cgm3DItiJMbaHCboouPhuzy1WznoS5WpfKKtaKAhlm_fuTaWWHkBBRdIKs_kWFT4HCivLMbJ24HtB8h08YvF7VL_Flli8Kus4Xj4aZjJ3N3ky8c6cIZfr55Ml7YnCncYTYEyeVuFe1oyGGytqcXUuKHPxz7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 710 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8oPsxakdCH19Sdwtaqf3M_TI-a5UY1BF6C_cM73kfDh6ZezLFfW5zz0K0KPFBkhNbNHddUyEphV9GkH0SO2plwtSNwrMg6hR55aCwENOhDWtqGxoHUbEG2NZXUkMRQtyFAbb141VCXBPJA3ZNrgASvwmwzbAkIW1UsSdi8Us82J-KWXyQcNBBaDRrVx4lHoBP2qn4Pss9PAfupEIVNmEYFaJ-0FnYTxIWr4bugNbrsD2ZAJuZPhegdCMYxkkvs_FTTBxi6dQbOt2hCBmgjWXPuX0exg9YWtm-5lpSMVV5dIgXCkhJTgpaM2oioFYm2-9IxSjE4R8iQxG3sdst_J1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWxobgv9lDEELPnuqcZ5QRXv_UOMmIhbmIa_dNRWpcYO1uMT55-fh4sK7M4-bpViSqnVWV_ftJOeMNLPkV9c1wocjYeOxSSRLWnb2D2UK3bHAJVM-cFMslHO0p3iioOBlCm6RNHpSBF_0h7J6ZjSaxOJd8hmdLKlk_OJSfhObE8tc88a1zh8sH6Yj8yF4H7iZOfU-ByzFzI2Jl4hjRuI4vlAhiuFdpygaEAmEyp9WG5y3WWQO_A80sWsgVqUqbizn4VP5Gb3P50WR3bDFDaEVK8YSNnTJYFDAgEIFspKAIZrRMBb_xQKben3fR4bOTrwyM3o_1w9jNQ4y9keutd1NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTXRI6C66Eb5kh6jzLqm3fAU_HvsaZ5n8MGA5bIagU-KOqWSMEwoqo6-VPwVGh540RRbxft4w59KtaCF5j_uk1RMgdAfwvV54Pzjh5azbE6-uh2Mac843HGMmgByfERJ5NVIO7Q14EmQf4RIGdonG8rqOtbOOJz8RQxzsDNZf1RvHInsHvgBa1cjsEO7TIRgbmPGyISIU6pYUGKpLLgIKlv5fRH0PexuI3xcbB-unXMo7qjluzaCS_FNIjodD9VR9NyzMxSrI7YY_BlSdSEksEn1UzBrP4ZHGNpwh1OPamvAqmWF45i-KvW4cvktrK_sp-5lNBKhTqFszq7wCqgaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0taOHjTKOHinqrO_hvz7eZiRDayurzYRTWv1G98SYkiaSvguItxuS2eC_GVxzCfRcyD9diTRa574kDZNdfh3DOw0pYP8_xHKsDyoFM3p4g8gyxYoOHeuW7q0kanLdtwayqcUtSiq4VtkPAENyTzQ_x1LH4ZJniOpf6A58olUS552eEeKLx7nkD9Q7VX1wCjgFwCrH69XybKKFxC1wXirxnGAUzaFFmm0ZE0_v6hYePD53Fo4HoPf6aP308tTGzWU30GJUG2O79Dtz-gj73FMHnDYz6EBC-zgz9qFW2l9M523LbO57GWG7D-1y49QRo57BZEa6hbW6kt8bwCo3_dSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvmbXaLOoF4JBsk8BwioR89l9MaezXDmg3sx_BrCnRrUOEsl7HQX3RIM_uBExYCMolg84bjy3uU7kX_r7tqYTQrtnVHoEwTFIS90tMyTE4mqhmjfE8x-O1CGibibGN8B98EAg7IBSJq302gCpZjz00Z08ol97PXetdtCJTIx06usWpV8qH26ya8JEFL_e4p_710oJ-hLJj63Kpg_HTbjcZHWKF-Z77kdWLWwm2FWSt_wVHLeTrB7mBYz85U72zdulMYkTQvZksmQzXHsqDwmGCI1JgvraABHTB_jpwubW5yLaxGlWWcs6rjjpKEDSCie8NisCEg55AsEMf3eRpBUWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0aV_XcJQqiJdRgtFgmvXAEA4xCJGl6924WC9UraTxe2Y0LHLk31tAdKvQQkH98_0HikiJrv8bcPVcZtxOUH2sgBrRh3LkPNIjSIJuwaZQKuoeU70AtxQRJg1IR5ZlweNYpIjzp2j0anXTreDFM8435lX_Tkd8dX34Tepl6kYh4DQbeN2LwF010f9AkzV0fGIPxVfNn2yiR_bHGqz2w_QqCqcYYXcT7NL7BFSRQ1OG85HLQPWm_IbL1Hc2DLLNextvC8xYFgZkdQBK9bTI7ETdZYoaQu0UktVWwqpkfWKnYmBEpXLdkv2bCmtGKw69A7LBubZ-IcPv53cUWvfOv4QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcE1V83yaqtrM_887J0AxS0Wd-cbwYhq7xq4uZMaCFp0v1-SvJ1Kj_O9m2wj4QP-BVzc_JRvTBA37IPDtl3Mtl5fZSsNi8cycskNzbIBef2w4op6Xqe_EwvjEJZeWa-9Yc0vegHDEeRt_7N7pBEEwHufaU7yQt8xsu0sm6CV75ok2E6SdCMtHj-GDtl1WMRM086eimt_Pw6imIK6RyN6XFkgl1YxyTwJxrA1hCGAD19HGDzapHGVh_be_Icr3QCFv9w8XRjURRZpYcvRqv-phvzvA0yYozNWTaKetZiSUxCx6yzbeYof4x9KFSLFeYYPS3rvygfZ0MwAxk-nZEY9aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAeyY8FNjQQEfK7XATHng05-oCG_HQW-AdsBsbmph_uYmn9bsJDMIsiPlTLOfjbUgFXK7AnIv4PTPxMyyXJu6g6H91J_quml63CEg-vUmL-7PruCnJ4ZGE-bg9EYWb2b6yxLYpl3yMpxcK-gW_KIKM3MrBWhNIDQBzxvHuNpuxU9iwRBl-rUy7UqAfqXNf74QohxCDMVYSsjHAZbNdclFeYDCJaL9HP6kn92_FncGkcW-bUgWx_bgdXmhEDAYmH5sivjqVxKuPKGjtxBxo9t99EQBMxRSONH_hqe4qsABooFgmeK1m1GSGu_z9GVY6thvvJeZmgO7fimmsPNhRiLLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUepHjoI7Rr9HyFDxtKVZYR_yq3Bulr3PXZVgXZGG_S1tQfUUJfD1nwD6VYfjE4EpSItiWCW-5l8WFMZC6we1gwOOUMrLucsUHaq1zJd-4COqGI5pb6zqu1IndJF-o2idkDXaEP20QBL9qsQmYpGL_jihtynAfFLGhLW_pgdlNhIdD7r5nxfBagKdH5LqwmmMafjdAJ1dCUcIBUo-WW8yGv4rdZAarL0GPIEQjXUy-eKDcPRTbNfYfeJda4unRUn51B8R7OzSoxCsPNuqkwpCx-R0JEoVtXyvFriRO1C4OzLBE6L6kx-126_0inpbtMYlHf6gPjZV1r0-8DYUhSQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZ8PMUkvpOYMjGSJ1hPiZxqfTFtbmdR91kkIyM86HeTA95tVKcb8nGoVE8iH4oS4KiyBZiCo8bIfviNo-8UE_Gb549epaiMq6NglyafQWGVWQA4XTQh-RDRp_0SVvKwytDSjG_XJvq_m4FR9xb99srtZtAKpXanMg0biqR_8cZsTWZa4BzZqaHn_iyoKLYz522qk601BUP-IIhTWTb35MXxSTAJ0b8_shmyhTzXFDv9BOtW6ZYLeb8xyS4v8ahXduxbmwyOvUtdpSEu0IcNg7OprZRUC6MQ_iFqOvwBheep86jf49lMtPnK2lB2tWDTV-FlXTIGpsICuL3c4r08n4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyPAx23S3lrHxjB-a2W9lCZT3wPQ4QkyCGaM8JH4UajJB05xeN-ORxy513tEuUDkQ9ZGTqAVXhFrrs25SscBrP77SC_hnEpgp_3rgR3tn735-URA7ZIAqL9HfgNSsKeIh8cuTeImFmNNnTxA66hlgC92U8Z70NPbKal3Ika6L62oB00ZPUqCyXXoUGbgUHamxe6-Hp4Y0i4pZrXgz49KB0iPLq16LXaa2ilm6pHVjhpcd7Ay2zRsIT6hvgc4AotbKCISjN3UMdRRxmOXxsoFV_tD65xIBupJBgYeTPazyUthgME7PZI3wBMtRwGB1v75r2SYNjdLQ0J1F6m8PqSwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdKLlK5eYLlFvXEscwpNcKvJclwH9ot53yvRLhD7qT6Kkd_NtZ-2fQW1mOgJ2lvVuHbfnFUyE914aqeGcqKupjQRdZRt-z38ZFThScirKnhDEvPzxmaJMV1-RhaKd_XztYmvNW93-AorAPSInmeslGiDjd3rE95_Btu4Nnj7rKAL7Q-3vV5RRo_4nTdPYnHfswlns5xaMVYaAU0bRRahAB5MoaRdMOAfYH4j1cnZQ8T7GRyqmlMKpC50P9NBGIDA7df8POAbfdlWz6_bMcCcHisaExD8tjeUloG4Y4jGvNlZXa1reb84E6sx8VopdU9wbVVk5TXzXJxHsFBxGS7uDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYHq1VRXNYDFyd23p9TxMIy-5RI6zYnfCI9Vm2AYezuCDrHVDACBUEF7OvLvvLrtYsbnkTjrGzFRDwk1K_6bv37hPc9VbPVrSjNgMjL2WgAnVk6rKBFvVLDiLbxoy6SWQLTPu_zqTTL6wcQGWJZXzCPp7otRthbS11RBKhtOQHeOXBGDLCehB7m2gw1ryfYn2v03cpOPg8HtpVar-5-4uMWFhMfP6M6uEQYYENvcTDj_Ib8EWuLsosc9ySBsT8dbuMP1eLjEzNJFvM9Smo2uPw7iIR9V-Q_dbJPCgRb-zeUuZNTbQ4hP9VvsYfBbsDemGXnCvA3mRLEwpeMKrlJyaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLCwoDbHyLIOKirABqIwwSHUXVgwUMqN9OPyM6dcl9dD4nl1S7Dqqc11INKyGCv9ZceaYt4r_ZKIzjguTJ5IDhs_OXdDcRGWghm4ZTUlD6nHEv1hOmy7QBVBH6J9Q7IdcwbfnAnMWQuRX4Zmywv5z7cU9zmpPg-GKsZCThdY24aZjItJ3Cm65JSIUlI0KXqQ4-xI9oTwzjW7hoeImnBVRZP7uVYZywDROxCfB1zAWnbtxU7iCTQgMr_am3v_ZTnJCRFIcmqZ58kLaSyliaKlCXcOC2KOZtef1OVJowcVwMm_NVONXPCrD0NKYUBumIo1D3lNZOk9lEobjygtZh-Ylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ucd7yhAy8Q7LimoZXAqObzhDAcTRNB9Yl5Yur6hTurR2zbtOLnmWTum-R8KMznR2rb1AV5mErLVJ5zX4bA7YThMva3vnmRYQloTIUqIivGQ3mA3uReA4oTpBGIFQF--vU47Tg0sKypGjyr2YF2CJ9Wiw83YPNmWafLhNzf-_bttHwgTZpm7Hf7inzc50XS7pvo_JwwV6-fBYO6Dj8GVTeTDvbSw1ZFdwc3jj9DCa_T62eJFlVb2Het8tfH65w5aOrX01HBi1fA_cZMnJfocKc2-a0V4x-TOHtWlIxj0auEu9DkkGnRDNlCR4fbZLp4mjPtPEjI5uZDJ8JPgKHGuCpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGZbLQUJ8Q448pvCphzP3PDCi4Qib13G0BkxjKZUdoSjlGqqVHTLSFOgxWqlD41wPqjail9fw6h7uYOvXM303mNdpwp-qMcLZEXysLepWEHjZ8umClMZ2Cab3aKdK5IQ7ontVqzAsBuO7F9pzo-YMyQmvSnETa0Zdp2CMYA6tRtoQeHySKbpQ5jn9iNuaay8JzezLOYl31rLqaYWBTm7STCltB4K6BvK7E2apVD2Ew25WxETAdG4A-liFQM2GVX3xu8ke51aeQ0-O1yi4ajPbCLQqaFYvSKQI4imHwwbqmge9KMvnLuuCFdp9eiEsP-PuubEXuBOkGU1Jq6btXbG3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeWZeCDUeDLc3gq9QGE6ZAxhVWUbyTh2azeRGPx7LRDwpRTouc2YD4q919GROTQPnQzMPeZN87odzfWyTThv6ls6dahIiTJNABLOusywItsVCzGl1Ddr2VNEtIew9oYMwAl7p08L9y13KrsMZKkOdR5kGf02L4dWa_P3ijzeE2X4Va5mTYhzsyD5u4ipfCJ5MwbIJCPIDbUaalfMhw5ynY2Q7OObLydx6rC61gA4_VUHB95TYBgdZfZgqpSIXKR6zlmE3Fb3zZQAtgt3h7jznEylvRaVhV7QM0Z-sjAWj_blWZO3sE9MZmu7fS42BfwDyRHWrQeWhs7tgWx6TZg14Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyoysujFwe-7nGq4Vi1jptrjYqF_GTegud-XnwdhX8k2pQFDkHzBpc4k8_fC7VJQ1LiBnbWXX1seTBy2qoeXe5Z1_HnXBc05ZtQ-cIiug8R7JKaVFwhHjd5YRMa4mG0ZBCYoAu-LFFzDcncNF2PD6VVlW6dyZSm7QXTMWymyJCWVlUPAsi779bGPH-vSSaaNq5KV-4WeYlVaHciKxMRzroe_CiRfWSUvtqB8uporviOcMm5ddfpxtFgIqxVWH890KpHyiNz4wTXV2FQ00t0HspAie9Y1kSxAauuTKjgPCpbwCxSizBTFJZjX-QAMdHAh4vHL2uSw1ND16pdpoZXtGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aO6MwOOh6HEEcZEB4RonBtSRncHaYQ6Z6ggUam28ENgL-U7qTts7RPQ1XaccWELJ-dLQ8ywO-fCIi1HZgLbJiybVDqP_H3rlnW4K2RQY231RPToGoG1Gpv2WM88SkjuYLaWSnAg5AWLCFlh43EN2dhrrQezIi19cTQhgl5OaRLw6oEhRUddDs2wh9Ctw7hRH7xs1Ot4Ga6GwyfWtaLQcmiY9_R8t03lccZfy3NxfYgKk6BEGOJhcNfutYPo_htzX2T0Vs5jMNltR_2jfBWpssR0rp58kRPJS2QfZzzUbog1y7iB6WsVSQa-84WSQdbCnvJNNulVbAAgd76kSVcBPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwe-p6QS6TNNXcHi2W09wybn0oRifPhMKmjK-ejA_I0oqPE8RgfgPSAEdB5nvyKFDWaV5HzkrD1xDnFc__fozYzxVk7dncx5YF4yUBjXnGDjwGvBn_qn6L4KmXPq6lH3vC04BVNnBMo0w40BZju1Z-0d2wPvxBXgkfcHUlhTmQ66AQWRgyMHTN6uqfi4pPTtDjPslRwfxbOt2iAYNjydZ05AdcSlm51_XLeGeYTlBatw4gCn8LOuTAi-01Wz8w4L5XH-R5zOKRBFro_LbCoDf2bf0bFVjuK2V1VArpYt4Oo3Xhy4UTRxRWGdGzCEBpT3kX7g3fynvxrDAg7vMij02Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZUXLybM5HXlHI4MNxxhUClifd6gUbNgcmsatRq4-1spDrrMpwX3uXrkcXtrdkjpDF9ljsKI-XyWnMquJt1JgSbjr9EzTDR3x0S7BJbipvs-gOi_-ThUnZw8fMQVPRJgK4IcpO-OtRudpJBXN5L9xm5L6YPgtuM-gY6BOMXqUoux-c6ryf-nyLWTHDft880FaKI6uWXd9QuW-TghFmD3x7nzk2bUiV-Ml9Y0_tNX86VBHIumTWgiTnV4aHnnysFApvGap-8tLjBp4xk4zUbfdbF1IAyI-2cUxZiqvqtYOQlaGI23QNeJEGg17OtFQagkeunBQEZvO2Saux2hx6vsRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Ifu-XWnd-91senykx78A8eFdC0PhInU8siClYAu9pNCsBGg9RIqGiCQHIWsRIDogtMESNtX60BgLQLxZvuTnkTrQos9fVBxcHu10z5MONFwrnd2JmzW6TZpgQ6Vl3TSd5j9niSdo809pKEG_d83dDesuZEjGAS6hjc-NFHfoXClNRXqThYFwoiSesFgbKEskBLdAAvixFT4FLun155xSAtg3xyDJ5xW3Rnft-4AYrvuSZYZEA4lGTBm6cJYb0TYxXcIoRSpSo9p6tlPkgmUzaMZAwf1a7Wjef5JGG_j1NZcltj7Pnc5J_7UQPMLeLEks98_ad0WXsp2wk1i5RrLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5137H4OXXvyfkfdm_vUvJcphNwc2JOJhH69T7xucPHn2nblYVUl-avSD43Pl6mQloeM6T1kKUzvu4ZtZh-YVG4xOqm5pxoWE-AQ8G81GOE9vPf1NWABaXEqlzmnw0d_JNVZ5DiedIIG47v1HuvFNAaR76lNbwJk0HLYpRZg-ugCODf0LUK0kbBo5TgXjvuaobF4GurltChruhWRK04Q4HyLQ-6VwXj3_oq2f4_taV4lIZngjmR6epDtITrBsSxfvXsqSaVNQNM4Qm6tZ57V4xZc0vzJQu8K0FzUiNoyFZA8MUk6r0fZz7ZZ9k72LSy9LV2Gvl-YhOGw_y1ludE_hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMYWykvtA7HLPGr_zvysp16ohR53UUt6ErDD3U49c6Nx2h-8tuBfdzLj_yLodMrYQRa5ZakCNHf-H2YiH5Tfl7xHZy-2Io0jWjbErQ14FdMmdVpNwARAcZd_NBgtue3q3yoyWLXyNAIFus6ZsqBIjPzPjFsCtOp_Sl2OQC1yUIl97wqe0DbrnnMjov1YTtUXEyr3JHj8WfOFO0l6kvxWeKsxLyMTIk6VynANXR4_-K3gsuBEqy_BlqDwcRljtjTEmAnKfAG7xHENytB2vKVwoYrFoPb0gDzTVs3kpY7F17ArTZBPnGQjgEYr4IhLQNDt65wx4K2CW4se6QUylZn6Lw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=kRcDef6To2dZzAe97We5ZICZGey7G0XxaakYBdslq9T_32pv1z-udPEFNdBTFjUguXTMKwxrZnJmmI_QvGf4MCbasW216ueCJopSBZqms4QipjpcNcDExfHBbaiMGQaGk_KyEDauUzMVjATXJxIiHzX8zRtp5zoTTE45DFYA8GYOXI5DuZvuBiurQHH5w0qZAlN0w9Ab1J4NSPKE2LPYrAnd32_2UK2XIK8yLah7DPlrvpOkjae95Gl497WK6xDIfuyZGbYvkgTwuXZwv-kC5Iz6xfpWYvl9sQEOXMdoLDIwNBxGlRgaKklcXd34ZiPI8KqczdDe7eqMNwLVsZSSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=kRcDef6To2dZzAe97We5ZICZGey7G0XxaakYBdslq9T_32pv1z-udPEFNdBTFjUguXTMKwxrZnJmmI_QvGf4MCbasW216ueCJopSBZqms4QipjpcNcDExfHBbaiMGQaGk_KyEDauUzMVjATXJxIiHzX8zRtp5zoTTE45DFYA8GYOXI5DuZvuBiurQHH5w0qZAlN0w9Ab1J4NSPKE2LPYrAnd32_2UK2XIK8yLah7DPlrvpOkjae95Gl497WK6xDIfuyZGbYvkgTwuXZwv-kC5Iz6xfpWYvl9sQEOXMdoLDIwNBxGlRgaKklcXd34ZiPI8KqczdDe7eqMNwLVsZSSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkB0NNtVRxOWJYclkctmIHE_llqSH9_QaS7dFqGFZ7y0Murd704zt_uPOIKwQ7M2Tr7w65ryEwCxSFX7nHKko3fQBlwjE1F0CUa8OSDLI9RmBWSdiHQdeBtP0U7FjV8ANY2ueq2JgFlaL-gaOjU901BFtg8fYD8-Li31rzatk7FPSkXfphwI3V-IaBD08pxGSNP_dEXbfCv6TpYwyT1LQmG_URAEWb_m4HAMkEVxpAFelZDm0uaFiczg26YvHzBnid0JLBn6X8PO7bGnZXIg4SDc-CpLCUCAyetDmP4R4_jreOUR4CgosyHLbKUwArNGlDfI2qlLLvLLL7B1-dCUlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf4ZXBJTcBfegh1YKE6exiaiXisY3UlfB03iJfRcaEOKTN8-BxYses1owyHQn1VvxW4tXOuk02GSNRkN21KWEMPcT0m8f1ZNKVkUgAWQVmEpp9cESsSqVeMAkF9fQmOWISwqgiGcaNl-w6GQbZgTLJT4MBg8io3SsNIZmTG58kptBfDRq8uiqFSpzU6hZrrXVARTmxtSLZpEW4pb5WVcKQTFmv15WkL78EckHsBmF_5hQSWJEPURu6Uk9fFE6tA3rO54IH2EUm9d1qpTV4Gc5guFFtTy_NWpi6iLj3_doXLJxBgdvZ8VhSsVKMWttwDyI0Ekkv6rOfmwcyIgVwv69g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiicqyelXHlZp-O9JPBAk1komDJpZx4bqnaK-95-2goVdGv1nvrSfBGNakFtZplYJgcjifa1M3ccL9itE_cRk0FJT50Bb5itcEAmdOc8wi50rl6VpOwgD3NB_EWjSIo4yM3lRH9ph9W-5XwFLKCsIk9yp_-nfFR6-KEX9phC_4CeKWFQ2uc8HVQ4XAGnfpJ5jS3lFU4NYW0qe9eSp4JCmZeUblBiPYVvCyhb7_bg77Vw8BSbki3pvcVqAxWcqqdFHTRH5p4m1OeVqPVLj0hE83cyTfg3XJiaNXD8CxnKVGoF6nEFJ24pyFqOCl2LC7LG36UUDDj-CMzopOcHI4QuRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMtHWhdOTeeIRQ_LNlcYUZy4rDoWXWyQMzsTD-rCD17HZZsdnhQnQpYjC2byv1FLS__tSwpOv-tA4xWLH_-7TQf2HU6oIEM2HS_yfYN16UFBcoQRgTiUshq0IaUiFus66l1TqVY6MH96l1pP-yvofCvDTpo72t6HIu9El274P2K8rhEKMyX96Epf-M03M5Emkd6HV7kp8gnm1niIgu1alDBc6eTGprq8F-fKXp6LmZNaeVPusBUDpjUx-KrUAnCTSTahh6Sijf7KU2W4XkIH-o7QwpJI9eJEEyAZRzU7GyvaopZiOXiUhFueWJsvVOd9Ufv63eMYm6dmbRqqpIzy_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZOV76nYbj1sZ70VyNj1S1N0vAVGQJ3ktJ3TkRdQjqXiWrNLFQ5OK-wBuKKL3udrZgNKR7qEmRB9VZ5tvrJw5DTuCvwvgyvLngQ-p97BQEQb5sRxB6TJ_iwhFfWhP9lzTjRLpeF_BnwSsX326B757IYhwO-vU2KHLatJ-65UIoSUOtm33y6e8vnF8e4WhoHYLXn2qOtNYAAPBCzpyh6K00Rz_YgOMirfW0kMKpDn1g6rnHmFGK8UQIozAPL_OfHYBT3QYn4RXydtpoznPdQ5gsvqc5W57wFMX05RZCDDyaPTZ6imxVoAtf_6LqzdBgkmaGaiLoVX43APRAEAaYpGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FB0fuXZQasqTR2tykT1eZhys2LtxGHaD3H8OZ4kqRRPrIbO8ZRHQ6VolCZ6xL1YVm5QDRSwW6i-0-xHcJ6Czk1QpNMliw1II3FvDb3V4qZHCiVvNa5vv0emuQNXhEVuZoJZ70SSdwrukRfJ21HrV_FVbRhvogpIaiBa4EOhYX4hAFeVNq8XLeh4sOC_XKIu-FFi3cKkvDXjxwbVZoaqpYAK0GlQlbFZbS0OxAkMvY8s8Q2WyXSaaU88gWvsY2cOQEu3x1qsmq5oRQbaEEXLty_020ZitwCK0cWccg1ggQLRJ3MH0mZT2dwablr2IEMwG2wZIVXqddARQLmipxRM4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9CSfPhP_2TrwI48fPxo1gwSklQytRemR6caporf1aCE3r53XV1GExJX0aZDW2YXEI1jaViuOkWDhpBsiBxHl4KU0RtAy7WRIOSDa4IBZuPDrTiOtlVdC3UBTryy-ceyM4DHT6ULOgRcJWs_VfMmhbQQev6kx7b5Xv8qX44Owkg4VMNJ6E0XecNv9VBiOZHiWKSA_jDStpjaBASBkv9EeufhY3d1q4u3MYcXqGq43E263GjthJaKZKGPGE1RuJm7JoyuYvOI2e-PYoymJmu8z1FC_G3HFeP47pslLPZ8UOTfEGUnTMtsC1NK7_LYRi_u4TgVdGSTapWOocXU5uMRCw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=JeY061RIIhNowFxwaH-ZLH7_XndzwROZoMMC5lA00j0ahnmMXhuo4fbwo4pzLmSGmTjpJ8R816FjTytw7mfxeULgJqKT1tLm1ltx9u5EpTX2A17Gsx4_yB4qCWqBo6pqOI6X4THqjUk6NnaQDwIJDqOnM7ixHSoLbpZrA_WGiOQAYLjL96TWNSFRAYUlL8m_2_gNNAP3pK3lmKTwAcQW5lfJGimk0fPyZn8z9x6hlDj_IehBujLjpndpy7XSkB1Yb9ADB6qXJDeZZKyt6ec_OLzL9CAHGL8xzjwZpxtPTYaBmbbq90ciKGzCidcxMdMPaoRnj6WRu-FV9cBbbuSSXH3Tm72D-zJwEObOVIfeCWP-ItGJnVoY-crxpDmKSChe1DpYR9M8ZjMMjALZ_rtq5tIohH7-gsR6jU8b4g9drODMDKfFNZM_MLkODv3n340kM_V0Dp6eUq-PAy7oh3T-2VteendnqWXLW3BAJoxfkGLwY72H6G8j26fEz4W7KQsrgttxZGetOijdCakl4swjCsxMidWiGzOMSyi0Fssi9bGZx-z-YwPJiA30rtIHvXyW3adUW6hggcVDCOXw3vvkyl8NHsY0gZ1m5ub-TYAB3QnaGlz-mwshal_zjSBd2LRtO67MFyOUfp7EC3c-Lc5xBughk-5Q2QgypM6WmqVfjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=JeY061RIIhNowFxwaH-ZLH7_XndzwROZoMMC5lA00j0ahnmMXhuo4fbwo4pzLmSGmTjpJ8R816FjTytw7mfxeULgJqKT1tLm1ltx9u5EpTX2A17Gsx4_yB4qCWqBo6pqOI6X4THqjUk6NnaQDwIJDqOnM7ixHSoLbpZrA_WGiOQAYLjL96TWNSFRAYUlL8m_2_gNNAP3pK3lmKTwAcQW5lfJGimk0fPyZn8z9x6hlDj_IehBujLjpndpy7XSkB1Yb9ADB6qXJDeZZKyt6ec_OLzL9CAHGL8xzjwZpxtPTYaBmbbq90ciKGzCidcxMdMPaoRnj6WRu-FV9cBbbuSSXH3Tm72D-zJwEObOVIfeCWP-ItGJnVoY-crxpDmKSChe1DpYR9M8ZjMMjALZ_rtq5tIohH7-gsR6jU8b4g9drODMDKfFNZM_MLkODv3n340kM_V0Dp6eUq-PAy7oh3T-2VteendnqWXLW3BAJoxfkGLwY72H6G8j26fEz4W7KQsrgttxZGetOijdCakl4swjCsxMidWiGzOMSyi0Fssi9bGZx-z-YwPJiA30rtIHvXyW3adUW6hggcVDCOXw3vvkyl8NHsY0gZ1m5ub-TYAB3QnaGlz-mwshal_zjSBd2LRtO67MFyOUfp7EC3c-Lc5xBughk-5Q2QgypM6WmqVfjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcECWdTFBard8kYMknLE_slm8Igc-KKAHL0MmipELAJ76PhO7cAh413XYxpaqOR-LYJUhGRIRJhX9qV3Kugqh0DDBdW5LVn_b1dgsqPmR9JNtdbAlfds_K86ar_toGK1wL2jI41ZyjMWea1TX5_SVBmLQ0ankwa66fAwfQXTEzqxR8_CO9KycrhAGJRKyYfsNPijYPFQYzG7XIJ5fqMRL5GVjsCrLFM477FCTnNSNwyMvVQSKjTFBuWoJ0XRXJ12v7UbsNaC0nXcDkmfI_q6wr5V3jmGt_2gI0TWpOgWtNzDivVXSvT36WvdNTulLEn3ixjbczPw2jIzKD-RIeFCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYkFbfwcXVpjZnHK4bCg1N7UDhAPVKf0KaiisglJDhVKicfDj0D-vAsfya4GDr0Vh7j7LLpIyc05yLW_-6KwxAwBzBlFExEMMnG-gKN4fEFiuRJuDwIW6bHEQD8XqHYE1L6S9cdlNGxQ6cNy_jAAhWzgG6WJcrdI93r4men-fMlcpuI7-GbUDGU4qeOmLIMARgaNe-7PZePTLVXCw5O0so_JZmTS4plUQJmuGpQMFZUGX93EXQuD8hNd7owk86fju2O5r5NCqgRNl4YARS_Iqg458ClVgJtpg6vqjz_qH0OK3BRsKh5nqD9QXalYy-jDITufok_XzG5xq9Nsm51VCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2PQVHa4gkX2VEhANxmYVqYZDonLwUbpFkhWVGAKQLJE0oFUyD3korYMPeto7vvwjZDxzaBm66W5r0D2Q_Wj9OMkBStH5aZ0CT46-p4q2A4GvJ4q3uBygzRDhvXs0wMxUPixbi0_gXwJ3_y0bwyGBsiFbUOYJ81-6-DMjshO2-Mv4jCWIqYIjvQ7OZXnlt5Og8N_baIbE_rNyeSlLSK-CBCamU0lucKmts6X8QnXdEeacJC2nxTXahXBZnHqOPQVDaWoBCWbnEA6Cw5llpCbDV1rJ11ULUqgtA1yRs-SIQ7L3CaBrazBhUnp4lfNt4aCGIcJS1ZcZrciB4Jgk6Fkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtLXFzcUZaLPw5oLA2yTuSTwKH0VIkw4xx-RfeuAGZCku0zrP-OPMnm8ZcZzZ5tbZGwSXthVbY9SMm1NzZWlLuBnAdCj-l7vwVJ5lhjNXx8iu1GD1P5pFdbuGlMsx-3-07G2-trJaKalK8IN30OvJGqbX64mJyVyUCgu24YbcqCOQj1D0yBGpgtHqk2I4CuOn4fEvLGNjUW1hO_5j_pyh50Ppw8jr6Z-trw3M6y3F9rjqeDx1voL8jRe1-xxrPt671XXhg8rBw62Jflku81n2l0YVs_4yPyqSHO-1JMl0OL6QFRkmO2gk1bfoSygw9_HK8xIKeu-gCq-AhpmZcScxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBWRaHff5CgudjKOzUeMn4BHMityMAdUBeG2nhBXzM18FZy4LBb3e_zPzGQLtMfusLaaWGG_XYVmNQJ9OBuiOMIcSsDjuciIP9-KsUtB-J_nmK93mQNsv0FihnArrmphMXo7G2PHLLm3zn59JGwPwTOGNgI2UJptXMVkK10VWQvyZjd2K9PqDQXoedwnfJgQAidTGfDY3A_4M8fQY0iZfqKf7lMWhDB-4ZzS0r2i1CK2xpg9XzpRTcMYM3R2fnFqWa5o7U7yq6JzBIS2i2sWgHW1Nkj7Bh5piJiFSaMCj3xI5qfyDA8zkIoB8uWx9OKYYmVJ3tOWJi8d12OLDEaZ0A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m2lWq0au0lba92W-TqW16beTASV2zY2pq8OpqzdI026Qf5PLQsfpvd0PW7TFHgGuET2ulAlRlTe2eit8fUNj4RTqT8CcBox63jtD6EwND7xatEULjV83q0YG7JnAj4F1nrw9wFavS9qqkI5FPDyOCMSh7Z0xKi5MpDG6eeeqB-_fhkIM3VAfJfNyETMVABewl3-h3tixwSnZfLe8lseBnvUV99q_I60GYPN4u1HeK-VHmTv45GOURpz8lDHuOLdusA9keYQSlnDnFgvD18KuI0E1yk0JMdSc0lT3bv_RdvnMvFwXPp_odbdVqtNUyyAiiWYisE7ge7hCPmd-nixsbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m2lWq0au0lba92W-TqW16beTASV2zY2pq8OpqzdI026Qf5PLQsfpvd0PW7TFHgGuET2ulAlRlTe2eit8fUNj4RTqT8CcBox63jtD6EwND7xatEULjV83q0YG7JnAj4F1nrw9wFavS9qqkI5FPDyOCMSh7Z0xKi5MpDG6eeeqB-_fhkIM3VAfJfNyETMVABewl3-h3tixwSnZfLe8lseBnvUV99q_I60GYPN4u1HeK-VHmTv45GOURpz8lDHuOLdusA9keYQSlnDnFgvD18KuI0E1yk0JMdSc0lT3bv_RdvnMvFwXPp_odbdVqtNUyyAiiWYisE7ge7hCPmd-nixsbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ-m7U0hKeaDqtGflKLurj-7pe0aH9bs-UX-m85ZvtuA4ebvAZVQKWMbFXhoFc3UjHmj5xGpizdlLMvw3_eIR_IsSdPoeX_Q1orUr-Q_hx8l2gbVGDzp8BplRwrKhw3LYRFMCh_2_yFiwCsbgdqqXU4Kub757ZnOMOGhjNo87wAb1m2oXbqPH29SQVtmm7ywoxmtP47BC_qSkOCVpWXwghdp3oH8d_LnipoGS6GZMZCEJdXWAwfIJIJBUbE8vp9fnaco1lPGXIJU792DV9fNIYtvkYk0gxqAG9GKUvZHvr5HmQrtxkQ7bu1Rmsz_7FC4XI5qcISy6fqzgfqSvATZKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaAzLuakHy4tfE0wOBfbGbQTIt2nU-ArM5FK3e3tYIW_P7vdYGAKVgexG2hkYTciduVfa97sjWMWd1O2EkyrrOM92cw1g37gKY9tnoXBwZmuX_A9LXhBtYyInJS36Z81Qg0jtKkFd4RhtAk0VJMwRC7RspLK_L_mNtaM1Dmcvp7uCN4n_Mn1skUcy2-8IE07S3xdQMvWvl1w7xu-FU4mXlANx7fYwPEdnH4me7tG8zqIzfI_nxNDG1VTVIF7QIaIB4Aq4Bs6O4BZ2UCK9S-9Oc6VsAYLlhIO4UVMgSkZ2rEUacU3D2ETIPLcvHShD3MkCnyRbu5ADkfyRGgwq_-jPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePftKAWnEyp_sI4zg_eHtaCj5c_8ly1pJA1SO4ZjfZR4F1H8KXqW8dj-ZkGkTqrl9LLvvhFmg2LxpflfBXovXTeBsEPU2lvexm7MmMFftapA6Utsz6Lk-_40DYEG6upA1LmbhpJ-u7KidXlIUALELa67k2PozgAuNiWfa2TJbjeIFWSMgllcofk-a0APoR0BJPeGkbwFuqbgeOQn7uP4Th_8Gir6gg6_52kemmotNA6mTLK0hjeQ8UCK2etP3VrdYboWFeau1LjcuLYgB8DV4XQo5lHjc2dJeY_jez3o886nS8Qr-hAa038Woavobsth1gAkHCY0Nlaz-Z1qZRkdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVDc3uKrPZ4jsQlBEFVCWcx-3jxlcE9K4oyoj-HNjqTmB5g26WNjLo5C3F0hvgqaQVl0eGTZF3SVyNF72rEuEAgFUvZzeAd8u9sKHhThpQuDD_8xDoX6jqKxk2-7c937z2qk0Sdx5MXFPab1DJlFyWINjeuESZd0NTTqWPr5YBPs39J7WWDdS90iAre2TB2q9O-fkydYm3ai5kpcz-j3cUA8o7ESycobRqxdjdmiy4jn-KhqBlEYYe8LiLeJW5--ZzZsOJAG-Z0iIvVXp0WGzs357chmY355UBBxmgMhPy2Qze8EOgHTrqydaT8jjVQCeLGSQCuK6ZTZI4tucJMKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1nlghwMEgIFtN6k1rUvesS0KBNzpKOnq9hAXS-EzVOCoxt46Ec3tFuwUShWL45kpY4RhlJIcvio6gsBThJqvp9YIOZqIuxKf3Wn2Xm9vJlqokvscDUTFh430j-msRimUhwDwWWL41thFfckRKIF2Px-95WUxko1skW0-vGXGK0hCg5ZajsGHZRIm4-KAmmPsNE8z9s-r1Dfzt2vYXTAya7XxwR5B6wAYOndCCL3yt5-My-BKu2fInKg4_qKrVOgAkUiNiZ6oqU92qPaQKw4NSZ2MMDsYA0VnSW8W8vurJH9cL9XdsEtVfxX3EAx4WgyTsB-3eWbFS3YCU9WWVIuGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seSj6jt5Fdq_HSDWRvxgBLiUCyTCD9KVDc9ElVAJl-3cC-qgwcFaq3MU6l9Dy4OISmmKJvSQkJ4skjDMAgciJ7QlosdVT5RXop6f8pTc_8jmhiT0LCvSWrMMEgvQb7KdcBfGFso4FVzozOqFwzqDwubDIgQ_wBNxO-80sN_xj4UOn5nGnhtlgqY_CZIhrkH0Q59smMk9RyDonAj_nbS0EauxSaEkFK70R1ECy9FikCtt1UUSvBj2c-Is_6-ritwlFrrhUPHLLusAt5xGFdOIVqh8RHUzNWFxuBLTTg7Kw6seO-_N8l-diOS0LKcdGPRT-LeAGP3gCjn0hc3L1DnZXg.jpg" alt="photo" loading="lazy"/></div>
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
