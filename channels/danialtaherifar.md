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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 02:28:56</div>
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
<div class="tg-footer">👁️ 162 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 450 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 592 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1h-LL1R2dxLgZ7YaDla0DAaFeC2D3LuVPtwt7ZWug1UKr-d7wTDuFtdW6Tz04vhmM43epWBNUf6bvMaFYIvp8kmp6fFxofqQnyEWlSvDruHpjI1ZBireK2XcyRePCTVIBAJYCzb-ks2TMZuVZrLcvncoCbVnKAXxmWqVM3fl0aUzql6qiveuh3aDzXL0_3GWKyULr0G25At8MHUWjbqeD159eCyf8PNtMaoDpIpZ8a_hsfhvkYXRDos3Z08b_MH6YUY6z08TxS9vgbRPQkkk8PZN86KDa8QMqT4WJnq5bsGbmcTOTTdizLzuqbhmIqt0jwl7R-GOdyFPnX5WipMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axEO6d_R280I1cAFfz-HsDQCZaIBR2gGKoEXkAlBoXTV1t-alpkjtaHkxH15PhcUZl1qbRNX-I2VsByzss8wD3TziR0kR5TYpfmyQijgTfDB0bO_Y2assgMTQjNcxMSPyQubTld4jdnfPBY7lWfFpg0RXdtbQmYoOheWTgwrqe931rA22GF7Ey-nGJaJTZavKxaA10vhu1kC402Jq27G65qOVg6JsXFIBsdvvHveNG0nyVs3bH3lB1Y1cP9q2pexn465MP0Xq7RcMcFaBKENv1pkMrxxfZT7_NvbKlcpgYnGgkNWk3kyDQxk8Foim5MM-YddmDqJmc5RUhZ-TaoOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEUEDfazZ0W4EH6SglRzCDmy1HmOKf1xS8bdoEdmD5lvx89_OmzHayJCntX4p4C_aPp3VuY0O6EDB4NyIIWxV3vqpm3RYQ82YaFjo2R8WSrsgxwY_as38cSu43tJpVDTpOlQQd2aKljKiI5fU44215lUdSSbznq3SBVolKbly2Ak8Ta_ZS5Ri8f3R3ArS8WjcUGkpQi4grc5OqUG_GVKfL69x-5QCtHp61DCeOLeOOlKmXo9a7QPt6KT9dmH2Op96oO7_faK457tAsmMbZxt8xHDMaPYJX2konMP3MWFSsjJXoVyRiN6NkMJEnD_anbhsliLjapNkLrkyWLyrGvSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 959 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm6PGYcJzDd39x8-SsMlkeNpapAluiHTORqV0HHKdYJhzkwYkgNhhfSi1mPP8VZ4pQhR4lHQFxoUtZeomLNB6xwse7NasA12YZzSLoFW6yef0Gz8NrjP5-_AoOyKFFtDVy_1D7PB70ixAlny5M3NzMD-chY77n4w8YPGz7AS8lNW4O-pYfwd_84zqC0zqKwLCAGYWhLukNf6tcrDhD_3-hJ0BU-gP6xbNb8b_LBNcvSoW5ogDUB_GcDGTTIctmTMQsz3Rx4NOwSBCZ_hUB3417DJt77cr-WByrvHR2QRRCM9TDOEBInItzIcwBKEb-EReXRG-2bAzGBwW5fwdFiF0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 829 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9zUTauF1Tp-k95EtBzznE1bMeO7o03IPyiZxm4ZWBHi9Aiddt80-f2uOrEpDtqQ4BqE1fKaCKx9CVHVEAv8gdzEugiNX74EAONbpFeuKWwFyl9tWc4cRhast9R7MA52yoqvVHIG6gWnnw6AHrfD_nBG_i_gK4vkDrZAQlqwM7AUY78P6NPvL6P1NLyQByz6dq-CLk4_Ybjv6vNFyBIDr2XPrCsd6lNWDCjYuB2FDFZJG0PPIcnvTnocI-AZPoEelHe_Idi_KD-CA_Jyj7GjOCV_KVMxZx1g1W2zNCHfvyBzLYfcUJZ-iT3OlegaEP1ELAjPofLWaTNEwiMBs-x1Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxgEOaaqGngQZRBI0-RkSA1GqDJcGOKQQtXPSNfUjU86pjBKOZUJ8RGqTfqRgEqRh1lSdMF2k3UiUNbhtEo4Jqz3_IndHETG9bYnFOI1HrrFXgcJmFFjdi5xUi2fcGeDNYz3RpzHn78Dr768TXuUTiBu8OUP4VUs2Ad8S-PEbs67Cpt20LxflN7rRiT9a7ekzUu0U24TaMdkraRQUtixDk4FvIIgrVQsmR8_MYf0KobhLI8oz2O8sEcvSrwnt_j22m0omL7urQNooqaiCzFE7HYwAfCZ0NoYXd9Ml6Ka2MSIHK6a0DSaOkTqqSbzHBHq5uge7hgfwsGXOPXBIf9Qzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVbBljkNJAMh7q7jtVHKKbDR7cakaRZWi9An0kleL87sXULgvV7ufusP9MI1giUXjf4irmyhPlkLc-_SK9IM7SPOHsBz9eF3H5ClvDP-yLVzyhqt_Y5nUvx_Zf-JUfrjIVYRHfpmWNhEttvmPtrXRdpQtzk5P-Cd7dCvczkIMHLC7BBJB8XOA0BKfQqVCODw2IpYv8kR7J5GMCHx1pa3SKxyQILdrzGoKZpo8F-DCb9YIw2LUQLTvWcpRDDVDg1gPH4ZS0fK8pBTFv-_TvrOOn7g2Cd7BRuVSR1lPIClf35D0GGE16qWduPmMrwA993ZOFAUKDzNGn5eULb7rpK_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJANaXxlxay-6g0fWsIirc6w7qbn9JzRXJmA-DAjbf4WXaUpKyZF89PJ8NQeXhBMbZoJbkl0k4bZMnJNyPt34DSRYyqnySiuu-hzSjBtQwMVioYuJcGxGCFzH3tgEB0ymIIFxrR47l7qKrZoAHAxskWJzMhfVVWMC8S0g_KM5D2V_vsVnedZKumyqXFQDZbePjrOs2Nh-SLVDpYYzvIjkTN01kfT92DaHRVq3y2E_hymWxzaMzjM0J5g1DZGYoKby_qF_u14BDN83c7xzy1CyZ98NNiy91T5ebMdNkbcrd92r41DUVsYwx2I9kI6loO82dUXrX1qSxhuNX4pHFQp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4yJti2-hPq1lVWXEIQxjhlGLkmrC_cDJv9ZSkLH1N-2azdBTqj1_b4jz_NPbD3FIpRecJQnlWG-203wXWXj1Uts5XqKf7GaEDyyFbLheaxCEEi49q8rh2o080y1DUL_UbHPOwwvWwPYGeeg4sRCiiaqUmc-wHVM4R_HilGqkwDCzU_R9gmI39Mbm9ONFjLn508Gcd_HG1oULKjWA9blW8OU5U4sHtKHNLjLPWLMxRtCG-lQagIzGCp6MgHScfF-569o_PELzE7tYXhV6VPKTaddYEiPHLgab0jBnBlwKmJKuQVp51kpCk4xNeGwEQsuQtb85dM4Pm-67EIAA1Ch_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anSGfVgA9CZWwWPDjwj20ONU6wOPKgDRH6zh2RLcjzC2Kyb4SWuqwFm4Z-zPSBt1Ro_wlk6ybGGv95sI248GYIRUTUkqREzVWGO1aGTM7jpEcMLACL7gHnqMbtC2UophdgFQ7BLPNaO2Ogkafxwi6mOG1Y_xl0Wje8N7blfuU-dYNEb_4NG4XuM_uNK84yhrklcJyCK9zYniPSJgWz2U91HnBdLTovxK_54CKORE7yaG6ZHv8GJWedFcKgDW5qHAjJsVgFv9i37DizbC5rWwhRlTsNenrmqLtGIyxPNnva3jwhiMpngOpv_6D9kqZAKxgWpDrGUFwmJTkH93WC8W-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSXf2cUMpyKi7bc4-ig-Z5-ehARp__mYDWfQTn9MUr1gCuQShnwJUQDtuK9FvZ3qiQy54znS47uvzw7WXwfr9iVuBmCdJpCJqDxLPSGj-6Zbel3hk8MTmJO7IxKfn1T3V6cu1X4Me8CpOSJPybsMpKvAUbAykDh2RjsrB_D_6Kv9VGgipkeZc2p9DOp4wNV4ViuhfLb5jQzaxvmcJUmjzT7Bz8ohGWPBHLTmuMjIoelFb-N38BnX906bN_gxlDW5afz1SqtksJVhl-W1L54hH3bYuQF4jVvBabwn59fv8lDDc2AcTU2MfNzzgZNK5VbLxNium6c_aPiY4CDsjbfenA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=lCkWy7MCL5VFADDl_fA9lVBkdLjn-ibHm3Ta_i-pWxmniIBNP7ARQec3Q6APPZ2IIqk70Va9PN8OrCZtLiKR5ZCg-ir60QATKsxbFL0qS1O0b6z7BuiQEJuPca0ha282U5l0nxQzb_SZS46Q8zmsllA-wOTfD-_0WswVxlSKILPq-FbL0Qdms9q-qBSZUydzcfUOKf7v5ev-XuQy1zfm2_yoQT2iPmffSZXLgog8j2OXGsCKNvkG1c5PLltvJhtMw02Jz_wrjoh7cYSxN1pZKlPpP56E_PNzUj46DHmBwKhHLPo_1VhvdG7Hm6ZBidYOMk26X82jRbTsPVPSLfw_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=lCkWy7MCL5VFADDl_fA9lVBkdLjn-ibHm3Ta_i-pWxmniIBNP7ARQec3Q6APPZ2IIqk70Va9PN8OrCZtLiKR5ZCg-ir60QATKsxbFL0qS1O0b6z7BuiQEJuPca0ha282U5l0nxQzb_SZS46Q8zmsllA-wOTfD-_0WswVxlSKILPq-FbL0Qdms9q-qBSZUydzcfUOKf7v5ev-XuQy1zfm2_yoQT2iPmffSZXLgog8j2OXGsCKNvkG1c5PLltvJhtMw02Jz_wrjoh7cYSxN1pZKlPpP56E_PNzUj46DHmBwKhHLPo_1VhvdG7Hm6ZBidYOMk26X82jRbTsPVPSLfw_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFZ4Qs3aMJW-qu4QcoNWKuSCm31On_WdLDAFYQ6Pz7AeXRhecddbF3DUNvfCCWpbO29Kuznekjd1vic2PYlIkrQzAWHoPsGmnsYuTegJhyldqQZVh8xub39k1HikZzrJzzb7fIOaTs9TU8OWSFaT60ZuIwvTqcU_SrDQl7f7ST1mfLWyqcyl85xCAKUJSZvTtEXP9di38Lkr8cpDjsF2xUzZAGXCGf5f5BwdDn22LuWJB9W8ndU8mC7tvvGaEj1bz7TDQXXTzWaLD9N802w1THesU6dspek3UHHiCGm5lddTrov1jj-JSmOIqIp3t7DKR4pkz77AnOrTW4jUUaBmdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPokK-AjdMIEsmoNBLvlnI0GTrFGbst-UPGSujOaw2T_76q26uNyYxG0E9_guCfTMDoL86sQeheUdBlwQi0VVBQk80DWlh9Ox8baFrT9MHCjIGg8oESrtmgtoXQior0OVThEjby6aXoIlWGppc9z_KrGzyhhJ-WfN8VeXEWnfv2IMo1cT-L2Moh_65ClUTuGHYZvn4VrJJj_6DYOjEMWnigxuHKBY-r5sPH8_a8_vnBakS9VnR2a3wXPOCLBo_jNJs3amtNnSA3VEfIXrlVF-AmeexjVyfISNvLJxUQ7tK8Xa6gvKGdgSIXF8VwiITeQFTHrKR2SMAicYt6cMUpjiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Td6hnsQb3GwR2sNkiCXKa6WQPZ7cWQ3VjljW6iNPxuuBm0rWlkvuBiNtNm7PJhUHial9RLrcSLANViPfV0kCVuI4p60uC4B41iggKiRKQZVSJ23b3blHp9dROVjDm_7GdbCKjSX6_I38CNegjmR_E9p7PNaVE5LCOg-JDV1DA2iPlJOO42mwmsS84tSOMq01JyI1N7DVOiE5NZ6gdiGyK1PKxK2lHjCXdZyzJ6CzrhoxnevcdRjC1emoSoYmFueHZSIL-Cs01QJU_tmfByyLZGqGdaMjkOc3qrLW_l44Zux--r_V4ojjbX_dP-vYZGvNEpzwhNL1wleu_bJuMocdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZV0x7WzQ5cCsCnQsd4-fpPryFp40vPEj_ju5mRGnhStMgJUZo6Xurpvj3xSNOyxQhkfl-y8x3W43_tymuHc6rOiaQQ4GJQYV87ORwGe1FvWzWGMwsgIfEiERkymhKq_b0KGP04ZWXq60IDeU1Vhd7-iQU7_e18cobmGblqpGLcgY6hr5rF5RMbbdA1t_P5lR6J1G8cfIJAI2rPvqECPe9Y8iWlUJMxxyR77s7BTbhnVAsSdFdBByaJnJ-cnjeYPeqNGiPUKDPCjBIcqGlp-UT9PQwymw-gcFPcHPn3ihVKuBpuiuo3-tFptM-awsdVAI_zlidUaFuLxrLQ8RxyX1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wng9WUlAm0urt1bE9PYIKve3vpw9dtrm9yXlx9sUW4yS5fUwfNDhpBSj9FDHVSzTya-A35U65A8-ibceq1XHnnqV3ZK13_NNxrKiJGvE0H6RhuEoy7wY6BYRVMUK1fvoOGAkw-86bzjt-NrWIW48twIAR3N08G5BcsaH_E_9_Py9vLPZmD_hFJvTqEwb1JWLFVxhWy03hxmeehAAEiI8V-MOMEDc2tEqRhZyDKd_S7nTXmGP1JU5Q89h_w9cKunbd_yiOqqqiIATcwuZV9tGXYyj1UVVATaUeHY5-B0lcUpH1ozRp0twZYHq5ru1K5XdOnXj-VysbLpcdggpWX7MTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmCYt9T3Av8Jm1HtJf5Lh6tVMQvGZQzH1F1czYPydMAECOWtANQuMHHJLRe1ZEIQ9e8I0W74KGzHKf7TzEvXVYgS6319__jM4URpz-mEOSrsHoEtvF5qZHrhrVo27kje4d2WzI7mH-u5kyyhFTw_70DZUPBS6oOUV4WBQN4nAXuf_6950fkEKTzpp5Bt2i5GUt8v3mHif4Fn9DHFRhbTWqukIIbgVapl6PmsaP5lYRn2bgfO47u0K2ISmltR4JEQ7TSN7kL2AIm3bxOleSP32MkAWnRCLZS51R2BttcUHGidu-FMFYRl0e8s4S5nEZO68CNLcVM7wjst2oUq-AZGhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj0CEfdWgwIPRhKtz_8cKVNRMC8T7BRwhTYGE-GXVc0dsu9s3gl9hqEH9KAz4GFcKrfe_N8dGmMiuwsJO2sz2dsqobmZARGUnjx3F1GONTwO-z3GP_RNKkmm8qOCNbTdX_ko1xesrEXAVEnKxfI8K_d7XDQNMFSDA41GIm6X7XJ-fQyLFHg3ZDexmOT_yWKZ2RHx2F3EKFeDXL9nKFyNps92ahvLf-OnFbUlHabk_Y3HWPREfduq-2jqBH66UbnwK9J40o1Bf-vJUEtruezNX9EeEKa09QC4-FfHeDP7NImmD2Nld36TqBEWypIhB7f9pPhtCiJJ9fj76RC5JpPpJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMXnI8JPniLRX0LozUq_u9fVSf9y20MjZLyc9P9w30kKWTBSi9OOM5IsKL6Y3cyxryRoApZjhzYWviBz86HyM_dd4bY9THKbwJumzgyExOswpkaWPtIY2euP3sPaOhi6NRbykrBUseWuyeYPRAMK8UAzVQGJFbj6abH1iIBtv23vUjK6lmW2Vc5Sgh-8CjVVEZlLoc8kuT7EtPFgEZedP9bEx3WQSNE_QZemc6ozgBVOMaZgyCO6E1c99psoSpxvG_zOay4ybQZEoMZUcdf-KbojvR_i6zvzohUaLEowF25UoyhVPQT9kZ_KU2SVgTv9q_fd5Y9uJXMNVDfgOB5qBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9q_HYwnNYjmJeNBUSFn9vfAxf7OxQgOpMP3Jz_OfDTvweeYyu70UmH3D5sgVKmt_fBZoCvyTxyidYZjwWhQXJg3ihpRPQE7BfSAggMBMrL8hPBS9OJ17UicT4hU6GENZLSoxlQRXtfpdvhF1Ev4-qYw1sJfEsBcvtMkqZd4wKw_tLbYItEf3E-mua9pvYDEvmtnllrDu9TJA4oj2WLXow3QDGgiuqbJAHszjSQxr3ojNWopn7V4kymTaGzXTxtY2a1X9Mp_hlsFwSsQ7VTAbNOgkUhVyv3zsHN916Uk6Vng5MtAVMBxktYtQqtJT3GgVqCfphFYv7wGTNKe8P7XaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeBp-IOeuQdKwVnurLzMntGIn9bLWOurJYOQVLR0B4nGmZL53MwZUDI7p4ama2HNrf7KcJlCkJAItsmSFIxdrtov89bxgbfE-es7d-j5xh6YlqAxWoPtEBfQI5NU1FguLM4yFvFe170_ryWc05AzvI5gMuxJUmcvNUivTYpdvOaMJcFZ_3o2crZUnRTzJ7tKy5yPtJiVpZ0OG2UNEg4m6H54HvBVblQTvAFq8Si52bSZSYl6RRnBZ8vnuL3YXvvjjDBML0c46V6sSTnquuVyzkxP8WmbI0GgqQVcf3w52XLamIJeDpKRwRFfIBEEkwd-L-WfC7FrwWYzSfUL0C6uRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMk5t6Z77YALDlv56Pa9J6_iF3WC8dhEaqHAmLdTeDyZ5BHjeykSmzz0A0RbM8bNRG2x-R_uIXbPo09yaSNOahxJBNK20D1D76yfi3RYa40KQL4F9F9RoSvovXsMYv2iNw3Rx8nRDaY7uE1rfhdkdausQ0IMwuRnqr5JndD2TzMzg5QqPD4kW6fM-mQXPvu1ym7olPv7gYn1QUiwrSC141Sc0NK-l1QEEeDRRag1CAljL6py3T_8wYG37vgqJlXPd7MtYrCpePrlWSm5gQUW3r0PG0RRjuorJKIVlMWvqbSWyOIa3moySCJwsZl9L_9bUy-0LGy_XiOyLfi6iD80vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2OG_3D93Mzl6Bxf-nQMZQU1rD7aUVmJwD8Jp7--b4GaA6zaUbpfo9hJsLHEyRcvMXz-Fm1O8-RaENbOtrUT0Srh_DI-F-fB4uQujUKcwxcKTUtxt_FiJd8QGCT1Ioae40n1ZAXBniL1MTBnS8tpzYeLAQhtCQmH40zQCjs1Ab1ZLE-k7afnlv4Qvo2-XiiPUNn3AO8xxwK1L05qRV0I9EA40KgbiQp88JCTPdvQCFxafCT6CPtsB-S_GbgmeQva9ViJ-yJ3zJ0AbaTiy_bBjXjM-wdidOarvSMld2D-rk4CtvxtUwJZVGMNhqpWS8A1z7a_5Sahiquwetud9odGkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THhGxSJLP8kjdkkrY6s7Q-Adr-oW3rfeODFcd8bJk_pPQONJCfZHVzUQlHcg8hmh9CSMF-lhMaB3ub0utNk4ho_s7C1KmyO6aWms7G4pBdLMTMKPi5Ef9eD_qZQoY8iosORvE3b19tE9L1lcl_85uBfiP1JV0mnwoVHH3o8eE2wbnIYjaHB3d0WUPy6bXEzrKLRJ-bVdxizxj4WklGgkvG8wgTZmKNnuwbfhldpLXb2glNTC5S10TxZWddM8sATmAA8l6LN3ajNR1wFYGJee1nEjKDhnH3_5RZ5ZRjdugGJxQ4nqHWMLrLK7WOwdznamrUPV3mnwY6E60OfOueVwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRifqLX12_x9rNpi11oYZVxlGaGHfB8AHdXUwBiQ7aJ9WhHV70AJ3Tx5Idd4sQUm1KOF0lkxvU7vk-bCBYA5LWj9NlI7Kfire70TzhQa3G0bP6qsw6Z1J9Nqkk0p6z4dngJxPsJicNOwvIGbwkfHZsSXv7ETEJ3EHQzk3zC2gnAFFz5Id_tsAo-qghSWNpoCWGiCjyeT6M91kjuafBkFRB2fGHZG6FI6F-YOWrmkD-4xyr6z9J0DtnSFqf5mPkb3adAxYY07_TcTigIgFtEIMVTW8fzOAA3_RHsTn_70aZ9sxUB33SZmBxeLjIXfzRT3t6CWOo-kCupJP0_6vVXrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0OsaWjEnvDfgbXJRz_zCvi4ROwlbuVykwOTEr7ESvMO59L0zjLVkxEGRf2LbgWEEJ2k_0lF5NM3iLhq8kAr48NsVvTsoFAjxk-zK5UF-c-ct4eva6W7lcjmeZ9ismxZUvIykorVzbrG2jLbPGpCTxg-pSOezOoMSKkGvnf_QRAOw7hvd_PAspwukHjBh6a5VkcwksS34cgtMx_yW4HpZU1yj-K-Ayg_Ru1iW8uormkovm6I4NUxXkE7DPRXe9vtQHoE9eKMf1WlLpVYMeqA5akv-i5csFYSLDeaJiFSF0U389mxY4PzVXRD0mKW88HaOEuAb_2znjnfREPJcLc0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbnRmPXudnQ2UNa_LR-NfmUUQaMxbm_nzJz3GNdpqsdjXdv4-KbJIO2ehzi9gWmqGihaji_cNnboavvtAxFUjK6wN6gcgFVs-crerCNOfzvJj4f1XSvMDRqqAShpcZuR_RU0zmDkWovemHHsXTCYTS5zR-0geQAewkOFjqEGukABWlwQk4CoBK_esHSt25aP3uLM7XbVYhE1zPU9rsK43taOv2CfzXRwTHYmz6wQAWsiKHH17ez2lPBcXziFp3lkpEBbkkF8omAAYxb6vR_XsDWPclb5fwg_aXmOK3DSm2Eei1rNyBrSuOylxtOan26id3NCwrsk9OCR5GKoGM-tKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1RHHiC4AJBQvefl4k7QSSHjYUomh8NVHb1_HTYehMHiNxTmJF7W56Hm7JYLKXd56kdoIGADCrDDzJxcF1ZolL2UGBcVw4Yd-89yHgCXk6bg2oDKPhHs-CrfBV0PcudfPjOl_OD2ks-BucS-vFAtbbSZ-GdIb7uY2d9VDHnyh4g7y9Bm6zbju1Hbdg4latOKa3rm21tviMPW-y2Tz5QHO3po1rTV1uQFzf4xkI8jMHD-KoZGpujgF7n4x1zXLamVeGb9WUKHXl-07YjwrDuP5-pVcA-MDTIzWH6H6IpYKeWx_ajfWZF8UTprHdcN7ih3gLA1afmJxHMm2UGuNQY9nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkV1vI_hQL1HVtLkbXoNwPnoJJAY4rUlL101yKfK6FZD01ynkJYbwnDZp8VMe7tqAJkfZ0_UPxQTQpjh7GMNyPw-eJd1_xH3q3dI1FR24BirJlyB1qswPJKyGsYMXfJjJUQzYVU5bcrXAWxpcSsZnMfKFqqjfGVbgdnUR2Ewr7dVGGKRslsel2F43pkcUi9YmNAg8C-9kN_u6yIXg8L9z7GLAzRCtSgUz6WVFisEsdtQqkEdNcBPOzeulki1g4rcCryyPYMP3ZE7A8-T8Fz4_37Edwa6TPtJgxmZWjkLJ621I8DdTLE7fsVKRQhBm8P7n5oXYkP6iU-kPIDbsoo5dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljPEb3k1Kjy9GgDvF0HLXLgdiRk-5IASE2WThlpyDn8ic3YXamQdBFpeLB-EwV6_P8tx3AE-q3SzL8V_i3QKvzgqnmhUp63d3yowRMgVuCOVmVvQjsLgWpzh-cmxXxWheCSYqK8O1eQo-1TmEFw3wiYwR4_Nk9KX6TDu7InzudcSHvzkROC-HK13YTZ3Vm3pqJKo_hWPq8AN0M9aIO-V7cuZZJmeE8s9YgzndKIa5-gulr_nGqwK0ns03gubVsfZY-BYa9QV8eu2ufu7Lmvf7mcOoPfIZH7cx2AptVw-4KUtsJoPo2g-tYV04B_WO1TUNDuRt9sfHmjpmoznQee-9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwxzusgqEFRu9mu04I5FG6yo-hBc8wsZn4PS_Qb7JnlMI9TWqWZ4Opnq-iBeRL9OWsLdSBR0LU9vqDtq_CboU0RMxHC-J_Ln4QV_7VaDmSxhXpAFtpKpBW3DtB3Xk9zyp2zFd1zVSscH8YjJJMd7BLkoj-pY71YR_pYCjtW5DbayHzC3wPCIyqGGUD1Udglm1ezkd0mJo-qMYaK_K1R6gpmfNAiq_HUDwNFwY6y8Ov_w8nzmKPNsuXL_EJm0CPFwVg1eRrRSvk64s1wCr1IR3NuKCR9qRFud9OpCPHVRCZLnhzGmxce365drohcyCYpTJybIZLFSUdWu_xjuas9OXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 695 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Je0ghul8epNWdivKyye3_PCdKEWTw6HRMG4ziSfMqxoKDu9mlw_pkeL6L10nPjF-zu3O92QnlDO6DWzwCHB_iNCUi_TTy0gyLQra78LUYQNAxzVLFDv5iVs36vebvTtKVkQBWPQfmtvIScQ6u30PiSh5yott2U9S2lGjL-Ll3WBu2QGt5ndNuy5r7JNGi3q4jDTd19ZyS6JRq1RMrhyjTAmvgGQxUvJq40u-9f6mYe78zyZlaJ0H4NYNRfEjac20C7xFAwW1OEcPtbG6jQWO_9bOXGtEjXDDKbyXWCNopORIHezVrppJ8sMvvXhBxWjx2ijdsuZS51Xfz5EcZWEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQxcAAgtDsu8N9rHsXRx7asCgg1oDjZ4DoIU0UzZw9S1wUCiK8LF36Zfp9_CFZcTVy7SgBrRs4zQyBxN60Gy1uaudnIfNjildt_BIA8trlFwmNZ3hZMCaqL-W5W17aqkpLQMJWkOYPbfJYexHHStnle3Q6ZqV8hJZ1YbG4MqpuXZxODmYVWsrnjqss5ZRhpAxKDvIOsYKGujtnIZGNStwq7nUyIyW74jZ3MVfWIsEuYSmpHiNumkMfXjDgTfgyarLfzZz8YjjbfmqmGibVgmKfl_LyZ7IH4TNcgrzeRzwVXeJY--eSXvhwZx8740Uo2XGPRDnTtKLs_7ziwdRwnJqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhFtswgqnYYwWJ-feUyn1rpCjyMzWquXQ4B1mU0CHykk1bCadVqQgS2TSXMyGuKlhEsWuoQYhgP6y9yr_w2BlkJWrb_hSpwpZOqPUEhK-D2e3aUkzKxNQTsg4fWkX0T1Cr3gwwPUqVveZa2LrBV6gE_Lrr4QtCH-DV4sy1YlssRZuQejCA8ldY_UTRlflpFnTYqcDhRvRBw1x6FNBgTcAJRMcVZYpxORyz_IQkjl_BmPjGi3v3vUcUhbi0J-VbdfTny6LirjkmAQ5YZfg6f0MRh354NTTfaU6kNRL6qzvIIjrNcCFnBHViCZx2fEQMVVlcy2g--8WWVHjGyGBkUpOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6e_wnCji3VWxA40PS054fWxvJ1LqlAXglr3JmWpy7dBFiEroaJUoFqnqLVPoGcOZ2faEGwTXlaIef60I5sr_yyDzFZuceqQwC3gx8zdmXVjtaaFGPKH_JULAJrS5J_Cv3mL5a1jr0ZfOGRFElCOcLFEIh1ryc8z9W4EGo6hmCelMJfsieIw6DD0ZfJgz-IWUfT2JzjTlotHqeBwncO34GClEOooi0xAEJJ9d5w0XUuLMFR3iVJy0zPUMDvK0tfUBf877DCFBf-VgA8RJPgK-XprU2z2QGegzX2wd1OYYQV_E1o1J3hf0BE0q3vwUsdmOaP5mDgRy_qSCP1MJQ2HRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsQ_jdMUdMIyQv17kKVWP1gABh5Bt5E04u6k3Y3HFC-uPcqZaCGWLB9SIj10Nsin4jiwd9SCzfxqw3DlnTmh7GoiAd1VKGm6ZiA0WjyOIKtmd8TUmRKBY0SDgZ126tIq0g7kKGFKw1esFM7o_RIsFOk-wvxCCTf7bRyReFj7XzwBD8Fb8pWmqtozdGzY8YqAdy7TICob3nyOnDOjUFf_aT9vLw8uVnMxgTmCcZo9M0ZBm7pHYh8FP6Klx_voCxcorLnZbpt68yWa9prcUK_3JEB-_b9QfwRDhyK9sshiF5UPbjrV1ptKs109jtJT84JSKT_A9mwUhf5Ph2bD-kPx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlTplDSQCDC9Qm5CLg8A1XgADTqVDk-VwEOxTSqiMFvyPpPSm-HkdkxAudEU-cNKuy3ZIrdLZYvqrTUiKaieE8Ano1XdqRsKfUIWRsX141JYg8143XH98RsNwOKAlcSxJcAiHH1fOJ4dkMEK20QSvFfCTv6wE7DHxOrkq_wenclj_eW-AAgFKGXPmLE4W6LCJre22q60p5x8BsW1MzwB8AFw93odDnHp44DJedqI96ivkudUIDTO2KkyOfADNkevJHa4N-CxdXZHQQbBq9vllYfBEEHMSszCwoUwsg6WgKbkl6PVTaut6gkXKjNuoitVUIEN1hQ7_g8o3J6r9Yicsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhJMaiHYG9CJHcjhBw266jwNvM-9DfcxDcqocoJK04-M5mZJzixMveTOD3psAgNANQOcW3BFRlAsHMz6bzBn3qydHG-LtXxjU1HkNkiGf5BDzdWfdM0W-D-u-auuUX0WmWg9lozF6qwynADLGKlAPP4ZhdoaB9wyXHLouqsaa3K5kOky0nlkuTj4JmqpOgirVkLDJ7KN4sRkn1k67HZa30D-FBokd-aWelXWz9mSQaQ-qMqF03cwsyER-QNpD8w-92Sz3kyt4YSJS-kL3FaKhencXN6DQ0Iz2vMdm1LLamNdHhRotDeykUCkDXefI-x_bHRsMA10QKV4m2LGLQLgiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFVTM9I2cuplu5OwegUb36Jdo4so1wzl2it3QrSYS3ZEHywx0FBZ0cqnpEQH9Xzn_ZhDT8VEhtU2-jo4f8hSKcuYTuLbCe5YvrTxThZPSNwQ6EG0xzOGuyBHh5coQiOXFX4b_g53xyqeLQLyp7E5WsGlPhW9t6wbi65omIwfgUeqEmwlr4WiOdH0YTYKgEH0ESNXI0eU2Y2WisISJoRnTJWj-dWrO-bsAQYGNMhXhq_yVtdfknHYkULT3u10kd8vgDtH0g_kIuoCLozj0thfmMhjNFm0hpdorXBZ411SVgEI_FkFh95Yz2jTJgcNw9xmnarx64gq41WcxwhKrySZSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-ddnU8GlGXKlgj6uDQp7vZ_fX_F0q8YbNF9jtdBsOw2Y8AB-J62w9Jd2rMa6HSIDlwd2I5Xe38sKRQxbn40IlZJrEy0BfOBbAXykRYDjIcA5Pm_2o5cXYMAXpAiM_b1r4CTisO93aogs_SedrkfxC20DB-SccIOlZSGYmzAKoUUTbNaRM9R_8jRM-RpUMsyGWjAZeWgsNxaM9Ncb4bJydolJFKD6YAXE7-cYqoFPvDmuf0s09iq6BerXZxsMjKtuKWSKXOg2m27aEGba3N3-2zzxiXT4EekuXjU2B3RTn0XYd99FapZdXHOk4xXpSIE9j4MwtX_YeV-kbRk1l730A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ury7jp8uZNGRFDzgV5Nnspfof_escX4ckjBYiHOdiv1oofa-9SlhGUvi-IeRd1GRPXmpJYEnZDHoKgZ1fULGz1Q5lMsnzO9CkuXyIK-Un3-ErYGTj4rfaLth8M9nO6d1i5SCvOgYeLuv5j1j535duq7xTlm1kAaCQLyBLrxoxorRn-qCpGrZI2Fs0IcOkIXsJ06HTyAqivHA_lbNnhuUhWsJMEVXi1EP509SOeFgq16mg6ZMNGA7AXU8TwMvt09I7MKgzgNkv3Zvd_N563kznewFpOuLfz3A8UOd5O_SQxIwNkvbUkS44PYjtwP6VKSRDsl2RNHzmTVwJMbSfErjGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPqyX-aJccN-C2sRBgC8J4eLge_Mlg-VfV_Iz8QhY7RJpmDovnDuUqhhTHqbISqDN3UJtBTvuxow-lMbUsrbRNOVn6Ca3BeuQEvLWJ7TFNCiWzaINNa718bsZbYLeiiM556d-2LYKvYkV8T5KyY8vJk3T0JtUp5GCuew5cW9s3YlsH6ixASxAVbEwoLltKSVj8e4CiFNBbN0jwtMNRtUNwuSX9enC96WyIjcGMilPoRcEKjTopc2W3UGvTfK1s0ZJlD1DT0QsQ6LiYPVKsb0P53-SeSDk4J8wNCaO8OOTmKqiP91OE3oCVw9EtbFgqXCVT9LMx9jpjJobk2rRLQPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqDiHYO5Ou6JHFZwp0Rdz_jPjkdlcqyBF4mp-IOm-VwXD7W8uhEAh65j-YTu1sew7UUE7QjQCHbMmbv-nzRJ4yHDAolOos_IdGMXxJe27gjc4LknYx7L5MiWU8Pc71Su-ntRw8g6rX01JLUfCp0nBOMmWS7uvTJP69dKcjMJagy8hpD4Jr-A4Q0DQq9hE8t7jCGq6KMpEraRhGZWIyCtaC8Va59jofi3-df7pgPjIu7gZEHjYfSRqcnKtDluSe4CIaCsnOE80dJK_JDD5JBnr99RYX3jqFzNtDbP7MvusQ3VruRvcbnPqMfT6ibDauwZ6JlWMJ_C6riiTfNpiPXWKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hi-fKNWDEnGaCS2Mn2A3HD2A7qlZBUrAjuJg0FYJTKeaKo72FDnd3HOxnswBcbce7N9Eae0fgRf4A1asIVpAXVeZBSJHN_vqVEJdR3mqRk40-WpqhhJrCrFsc1VyZS3pyLPBhO4u8785DaTkPLSxRO8piey96x33mlmotfTerLyx7zdmdLNlk2aptaz8V3-ybM7-eJvOBOZAtFbhZlb1RvLqOh1YoJRz9iqcVsgJg9zA5b1Q43sAodZY4oHQEcF_5FlsD2uGKPi3p4wPaR9GC0_6yEzhZOC9iuzf2lGNKdTo4empKa0VeCLZTU4M2WccPKLMC6AfK0VERF04s4W2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-cKXRN2iGYl7YCmzjsa362OksLPwaT-r76F3okvXsPxGDw4AE7EV7nSb1A6KSq4sKYnwlJT2JI_S70_qjjCfQHcSE2qatcUi6byTht-eQaEoiX_cDQOT-iEEcgef-TmfQxYqihRVCFA3d_CefjgagPdMPZ7YjdVpeC3ZkhKuXxqzsy6WGQ8bMb0xzARxOihs9HRBszo6JdkcDKbF4Ud4aY_momYQ8pVLqyUV0B78J5nYD-9uEZ8rV4Mwj9gWFP35yyuQT6MtlhZxiYBWOtyfV1Q6jxeHiPr04ayMfIBWOcOASv-1s2mgfgOu0_F94E1ugX5HovJRE0UjgN8Flqzvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLcJugmxMfl2oSxPCURv51CH40X9X8S3X-R_FHChY8wbcN76-Mpzvj7MZ-O1RdjlebNxTGG9xPRqhkDJSHpmsL1hDSsUYAEyWTxfbUXmjOEoT3nwBTer83Nk5z32Vs0thXQxLLc3TbIk_9SdUIafpiLexosEhyfHmpPBRpqqcxuUNuKtbK45FH7MuS2aASk4gVt6WULh4NeS4TJfQVGW8hAqvweEYomCebK1vC_5W95_SWVARzH7Z_V8bPfJSmM_g9UPrklqfvaYIDJwOM2yBEPJu7B5mTsDvSlu-0V38iLYSM4vCpQIlufBo1Z1acHPVhfCBs36sfqypwy5kgxfjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
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
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hc_S3AAEpy8liBsg0_poeHhclQaoU_CmeuyvrQwzIeonwFpmYbk9LZvu99xeTPJPZs6vdSLb1ROmUCGwSB80NSCDvvJOJzu5P8Nb_-4zTf2hzpeh8JtPr_GLMwqVVPqZdJuyKD19MJZrzOreWV6LL-lbDvcxmZGfqkxNQLtL2_szvkvjoI_z8tmXtAcflFcXdyAzeHIH1Txk-ZKz6ns9kzkndzSwoFc7c4VIvtSKZvXIivI5R34xqiGayVoKeFPqDO2Xq9-rMi3D6pqOmJozgrRxcdqjAEv9QM0XfXAQ6wLus8_v3n3gz26pkZLOQ8BACREaWwoaIfMS2LFfME92tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMpAYBpqluCxiDXApieOujFHsS2WrMYFodMNVRf75XaCIHtVnK5pa-66KNw6vtNEWbZPk_sYvjpZLRE1MzyNngEyZ_giJw4tB37w8sgtTmaNYlN9PSLY-9mhzcA-rgoimqsVGbiZa4kbKtN7EPP6Z6hCWDaxyQuJYUtw9O23bL-Ts1ZJ6dG2f4NEJF3wXiuV1yPFs0Zn7-3X149C4hYsbHPcjZTKcZvmiS67fYUuOUxZiyAKgUPjb8zkqrzYAYw0gOEOzc9cJnjttNsZf-_Y8ua4eHZ6BYNGWRdKvnvaIp8lwFIbmpOWyxXqzBaYZyavRMR5XtQZ8FP7cUM7Ef-mDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9ONcr1ONaCLHBlDefUAOo7xurNzJZ85PEFhi0_h67SBYzAcgWj4NI3R0rBJDZMgqdPiXkAsbmBIp7ryFqJ2vG_bHVz0GBgycUe9mULUdw8DAZw3dXPtVKaD9uoQvJnNwzW4pVXGZDOiNMlIxUrUO_FIveagHYoaigQJ0B1UzCsZwORdDAypzaFR0zWgbWkRiDprddEgBRWf8gq3jiJqWsJg3PA5tSO73qdVmDLCF8mvgQRI2AE5It_QXUe2w-i1Pt4DJpKqW32_C5t2x9L-PDs65qSP_SmgYdhNdE-wu-4k-mGlptjl4PN9tNgSCNgtMplpcvJB1o33fh_cKgscqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID3W-LDZYQTQqpWRFSviQr1t9OMXwp3rfsQHPA61hTFSQiyfzT5rY2bKYZAMqNiDJ5FYj2jNT32Hxgizk9qxuFF_bPxjQwSiof3lTyrDAbyA12wzQUz1sWJkLCs8NWwCqidOxBPZrDrdAOyHJsSEqZVcXxUY3jGQSoWEPaTZ418mR7rvkAy7OfbGxbJOhHy716HJC51N_xrXvXOV4wVVP7UZQMlnXQgi2mMquCjhfPna1xlLqPCH1TusDrbYzxri9ZK7zEksF_6RAFZQ83fcrSpoF3Ed5nf_q9uMmRGx89r24JVxmmsEVbbYzO-nhZBGC-z23F7mI9lROi1_7fp2yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmFTRXmk_JFxxJDdIyV8toXnSZdFDpyRX4J70fyf0iqEtJZ6li33m1mGr1ZoxJpp9cfXzDPh4mp2Q7q6DBnMEMVNV8vYOR_XwMEv1avr5Yr0Ps2gsqeOA4Lp3jrxG2JD6WlAWaUAQ9So98Qq4AAnMzklA98S5SxlfM3eFhhoOrocpXzyomPdjVIo4SCi1uvEe8qujwksh7oLzZrh8i9lByWo97s659XoWvJr6pbfWHH9RJSYT8nARW2opHb8k4fRCG2e5vrH0Q1dBvsHMuWwUaF_q5mxXH0Uzy26wvH6DS1jR8lz80B1cMaJyAwHz6o2_IGVPWNzcjOl8FO3BOt7pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HS_EGMh4XY1llTeYyUaVNJ3lfAguHs3osH71rPfvLuSHk5TCY4JIBQAGbywazPTgtDVKvDQTN21A5I2Y5NJd3525AmKQNnWazhuLRFwHRD0T3nDy0mosUU4_p7vTYNzdYK-sJ6dPj3B7sGtxuYkS9ehB29yEH-6B5eIA5vo1is83FRoJ61CC0gU-ZcarE5HKwZn8yPo6ND_lh0sEvXB0FtCFmNmv4I89VSZsyPB8m3E2AiOPnlwwVAYluODxH00eFWOITv9O17K7EA7vEzfnoSLW0jKjfnGyJr3_xnSB4XFAAgd0bTHi-I8ZmVg-AIPbhXizuYTSRftNPbs8MkxoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mpj1ekfxXBi6loIOgtcJh-cF7am60ZM1X6ndiwZS--b0U6jMHdHgM2O8mUBm5SF0F4yFeQUohB6Ak5By-vziJRkFNVJj54AAZppTk1jXXGZzObUoXFU6xOs41dCYNn8PUJ7wBkTFjsC2v2siP9DA6OsorCvmRXhaSkKSpU6pT0jWxE6VJqgeS7hcTjSUBl6p_my9r0U7eKQXHlVa4U5yHkDVnzHJJTlNQr-rX0-umSvZMp_jcjQrOt1B1dbBnAOkVi9WpckoY4OL8WjxDloJTHTj_JR0nR9mPXT4nMzsj9pvSpwUe5POn1CYwTJ9qrwsip74jERJl8UXV_ULo9L-cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppjZy_U1xDoK_7FiCL57DD8moQBB0_9SU_xqDsDPRBDbgXCKGCF15FkZE83eNp3GaD0Dz4_sNqd9lQ9pRgT6vrsO5CLrFBEiS5DHZpwqAhKxl7DgRRVvEWVtTXdqXJGnL-QURkwmeHS-anP2UtOLAnynZlLiSXNO-kwCocJvSXeXh8TccpF_GzZ8rZrDr2yrBOkCZslBwgnqbRmLE071PkbGaP8vEZaRwVmPXMTxOTss2AH3C9pF7xoDPJ8m9D2PU1YtCoFGAXXbZT4eLcgm0Jr4MVTQvvWAT1e6yT882_-3Uu6jdXQ6iZJqio9tN6dHM6bwTfY5EZ98doLm-i4SsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO-j4vrO6DLi2jyCXeT-MZfA4_ANblosZyg7_8rzKRAvS-AdJDfZKkgPntpt3pjyAl1g3oUVxWE0zvZFlY-0zjY8KXqD4HxWqR7YPaXgGCUmTR362GwKc51zzqAhoVX4MwVJj4kFgWqfWi7Z9bn3gyG7ORwAkfC9zm-y-jfd6992NjetjESxsLLCEmxPBVMKgZuLPixP_r1gbYT6EI_1Xo_fz6afDwI5UelU9wroPqFpE95IVVcnFT2hKAoO2two4dZqZJZNzjqYGuKcKRISXndd-401megwM7sCiFJlRxLzXl9M-piKwFy2HrD2_e9nAd3v1jwYRjzCDk2MTgE8mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci8BS60netGNTfZrQLA8ppndiyGxhj7vUVARIuzSJMTytqxx2qJsio1dqhTJjKXQQWORfw0_6FPWymvFWP1v_XQXy7FTw8tBpmb_e2PdELHx7JXHBkEYVFpuUhTdRF2e3YEQy4vbPO4WzbG7k-AY3xVQjKXF0n6GWjRESXxfCL0l2y_8W9fKmR-ge2zQRlV7Km-9IZqHZ8JalWDL6dIXx5-OXaoywK0X9v6YfstnHZiuHcOUvQ-lTbq_HJSnnxkZZppXLVP8t0rCIdXvuAbux2I6Q7bptjqauioGm4RUnvghMcFkrySscPlGUUuHo4RtyO8dmmWG_iHHhtO5_yLfRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbu9s6kVzIWxjzH-a-7PnoHzW5fv-2rR-V3g-OzuwND5YIO5oxn-NSgPe-xpUyEZC4y3jze0Q_KnpatjSFrDcjWH-ZttV3tXSh4tESNxrog4U050ng5ah35xyDBnAG7Fv7LrhyvZjV9shYdMP5q_USGB_SAsDAtVXFQWLn8TCjQS5TyP1nj2vB3WXnD6wFyltos5TvEEgVWv--qjekbK4qFgjNlm0vUmQQ-jitZm4h9IoklAUd1qWqa9rm1P5a38mtYheyU3Erm-tscFJk3RKGq-b3gUnOTmgOrhm7DsnMiMf4epXTdGx1PObYiKsKmmOWgA4rZG3wBzeLOoTuClvg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=pA3o-oeM-NZ_jHkNzL1sXIf9BfEl6XuCBAIsVPYDvn0YUcXJrDKCfgzZWFmX1AHtsZyGyesIwwsn3CaO1xKS33K9xNb8w-4vpx5pHRHBN61VIr_4N_v_rLqyP3V8CYBeWgKX1Unm2WSp6GaFZUW--BjdZB0znKtC-VeMFfdHAiAtDVXX7qftUbqiZaRuk4PawwbFNKMv1HYVNm1GGWnD1l2UgCtszIsPEJW5HTZ4KymTUof9irnRWqW8kyXv7s_Gl81BInteyoOT-VYVxiLrIy-Sjbaa2BlJrXMUY5tXme9iv5OHo3E9oQnon-geiUhz_QC_GHLnaFDMKlAZL-xn0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=pA3o-oeM-NZ_jHkNzL1sXIf9BfEl6XuCBAIsVPYDvn0YUcXJrDKCfgzZWFmX1AHtsZyGyesIwwsn3CaO1xKS33K9xNb8w-4vpx5pHRHBN61VIr_4N_v_rLqyP3V8CYBeWgKX1Unm2WSp6GaFZUW--BjdZB0znKtC-VeMFfdHAiAtDVXX7qftUbqiZaRuk4PawwbFNKMv1HYVNm1GGWnD1l2UgCtszIsPEJW5HTZ4KymTUof9irnRWqW8kyXv7s_Gl81BInteyoOT-VYVxiLrIy-Sjbaa2BlJrXMUY5tXme9iv5OHo3E9oQnon-geiUhz_QC_GHLnaFDMKlAZL-xn0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YayhUk6VCEk80PPxeDs4i9__NIUzD80VP-4kmBib4sTT43KrnHgG8Xvpwn_tlsi_dbHjuXwDqJ6sk3t99DpIWJ-RDP-8Rw56WmPcSGLJhOHxdPIfJJV4OfSi11CWYUNUA3ThfeSDW68Nvh_z5qazprOr7ocu2K6ZEnt4FRfI8P0pGsNunMHyCSeC7Itc5t32QwjVWRyGyOd6f-6d7mUyM1G0ORd0bQ4XFtTRCPsqVEATrJab4jUkfPsPyro5Fjyk4kU8trb5bjU8sIDGSqWMjp6ejcZ4WiDSwWaZ_S1L_lmEVXlmUhTeckAA3hu56siNK5nolgUEgV6naWVPXSlNwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKUDxpd7nvZhk6NguIwGvKD8xoCTyjGlcvu7qbLYcxG3pGmDbbXyfkpX0_h6ZM9ow2GjrCE9sXBAG5ZLpLkBttrcjqLxhlE5-aGNktg2pS0qAhC_ExQO2KU38yew76tfv8lTlit_vqd1IWGPGqVGcT0xJ2zaUhE6Ri-VtMUTuzJ6nvCLDGoFdkZ65NDyqdhczCIyDkgTcB60NgYrpMsIa1GuxxT_PULOH569NcEatByAkdwbcFi79bUZYTrAqciXgrfkCeK6jOx6YkVsXLui1X3ELYvM853J7Y0ie5nMrm_5tOqMyD1q5kw33Oz5L31FPhQkD2SlkVhM7PxvWSzgNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRsHKs-M15-pRalEGGtPTYpVDO_te_LyQreRARWhxh3qHZz0gr3rdngAwYR_xa1lXQgK_yPtkCMA_yaeWSFt_HELxw-4xLBU9-VFCL6OiJsTKvngxfHp6z_CVIOLqrxAuZZrA-Ve_SPdr16JQNBEme8jgI5gYS0429Yz9XThT0pBiiOpVJFmdVyf6KP7w-XxI9crkVsiFAbHbX46CotRit5p81gWYxlbKcFKwuNwjf0-MX5aX1BJRqn3x88W-uycOKhgWg2y0nATU6b7esqB0gVsaNKyP0VU0pmDfHh5AcU1OO9thYcGtxucspvzUMUXd9V7WqloKt4J5tvxkqZBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8e4qhWhObLy07nt7Sv5blhZU2dC3kM8YI4lZ-yUQ0-WiCZcFxqvl6sSgctJP2hFi3ViOTIVAwv9fBbk7Wy0_5Nhi2gKBPDI0bv6b_ep8odzIX4UM0_VHvSX0qxebOK1XltcUUEr2lcX3CJU9UYjequmb2T3GHwiJtVlapcbCIc5KRR6lNc5dRjLU3xRmU7Ly_gdPE9rYtX3A_C9-0wWYqcKBDLB96VbQ_BqKxUS_-g-IIUVL3L1aXGiSFbcOJMFvN7I9dcChN1mdAS5lXnc2VnvvbGHhapqM81Fi4kiNEklsX3z1e9GR7piU_4ldbJSQFZMEfKRLkXVZ6FWZNR_kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htc2JAfz-GqSKoZo9jRg4tpn80MUQF1LQDCl8CsCb6so4beg2fiuQqYuEV6Z59a7cTUSiz6spypgCeTyWZWS4MOElh6b5fFULhihsPFqFs99FWcjX243JBoe4NlVdAMLLx_X1hNjtfbY4POPF229Dr9VuQA4p-nxW_hkteydKYDCPj9692kt35JmcHWN7KDOgMXzcEU8pH-dNWAaZDiE_Rmk5k0yajBPHihYfZ58sFgASmKTf96RCFMqzwkgyKpSPUUf1rGuT5B1_NDuSDKclXxhAEPXEVtHK34G9jYMt4MpXGcl3jJKDZFo0A2Ej2jyVf2290C_Q0_Kv8fdipe4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDrx_8NkmYC-UJPcI7LhquMrGhtEfh34bbr2O39KOkYXsthYbY2GJkD2aBDzuU33B-Y96T-EXKx8QU6AQ7fAu6XUpA-aj_lcWB5uancACY_sgTnXFiq-AK-Gum5s-VGXd_pSI48LUYVevUdR9fOYXOCqzrLRaUr8dpVDBBnVYmD5exicztrAaXtrE_uRvpUWOluZmu79HHd3FRhHrDi1F_GStek0hGXEdi2e39T2WQrYAVFvHgwyPU8-b_VdXLa1llALrFCJWP9SaxxjwKl2Q6Rcf3iGUkgnw7nxeODGLkAPHoG5w16750FJToiIatcIDazEjxh2t001tAcJc01vhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN7L1lRxc2zE63IpYOGZOYluC3QV53hmoP9W_F5NP6ma-67ZUud1dVT5VS1NQzoJ0ejXWMsopHYDv_cSHOf_qSXyjKr1Pv5qnWoEIpEeqfAvX7z19kQxK7-9W2BcQ8tQVyWMwVRs8kMUZwPsaFOACrrWNd4PQoUblVJLyeprgwZCy-O63_oqcDvex3TdksWwLlEtjJxaCH8vARizd_eCEXuHws4AJQPVlfnkqQclklp6RvZeP9h4M7517r21Ial58Egaminv7kp8TPqEyj-8H7DrMf7ilN3q2CbZaFmxteT6cvHyqrwD8JDBaa6gYamCyNdLcCE-KksUKFsKgflj4w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=OrYSER_EZ1WDMoWXmHf7yZrEWkMB6sOjPipu-f-ZrMwlOvZ0z6gxspnoOCI9rm7Fe_EPZESQ5Wz61IcK6NFCTgNOrBH-ERmsWoI58y0PBYTcJ5oFaGFQ6UeDTWhBykpiu8diide8gevnsfd3CxjwuZ_kyxCeGREfo4RT5L2ePGIPJNX7oHd1rH2aFIW0QSpNND7K1nh2JN6X9bysUZ1YB-wpW8oXdqfRb7EvvOjwO_E7UujKNWGdQqDZUZQbRyoRE8AsgsLRf0NHgkdMhIRztiCF7FGCc0xBvzBjhQMtUMFOzNgVf-IZpC1Rho2w0RdjTnVr5vBsJjKiRf4e2UByHACLT4WE2YRozUzvcbga8mb2OKwKt90wfAmXR430JvXFR5kt8jlTSkkSeHULB29hsSR7mxV_xZ2b-CtjX0dZ2iOFuZ7TSZaiO0cvWRIq9bSYWk3NrNxabHF0Lqy4T2BFFVkghmuiwbkY1Z-kIupNX1xNBrHu2PPoKLQnpY_c_eLTCl1mzST1TR-crkTzCAsx-ww8F3GcmsQlA3JQRZ-lz5BwnSxirdkLAEc1hFp73T-wXQABeoWh2JMqm3cH4leeId2XTSN99OoVqCzt_h13bSoLIN0XyvhBFX2Bv5KXoHFnNW_0BSAET58be_PetDrOs3y_UjKImNzsiNJkxNYqHU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=OrYSER_EZ1WDMoWXmHf7yZrEWkMB6sOjPipu-f-ZrMwlOvZ0z6gxspnoOCI9rm7Fe_EPZESQ5Wz61IcK6NFCTgNOrBH-ERmsWoI58y0PBYTcJ5oFaGFQ6UeDTWhBykpiu8diide8gevnsfd3CxjwuZ_kyxCeGREfo4RT5L2ePGIPJNX7oHd1rH2aFIW0QSpNND7K1nh2JN6X9bysUZ1YB-wpW8oXdqfRb7EvvOjwO_E7UujKNWGdQqDZUZQbRyoRE8AsgsLRf0NHgkdMhIRztiCF7FGCc0xBvzBjhQMtUMFOzNgVf-IZpC1Rho2w0RdjTnVr5vBsJjKiRf4e2UByHACLT4WE2YRozUzvcbga8mb2OKwKt90wfAmXR430JvXFR5kt8jlTSkkSeHULB29hsSR7mxV_xZ2b-CtjX0dZ2iOFuZ7TSZaiO0cvWRIq9bSYWk3NrNxabHF0Lqy4T2BFFVkghmuiwbkY1Z-kIupNX1xNBrHu2PPoKLQnpY_c_eLTCl1mzST1TR-crkTzCAsx-ww8F3GcmsQlA3JQRZ-lz5BwnSxirdkLAEc1hFp73T-wXQABeoWh2JMqm3cH4leeId2XTSN99OoVqCzt_h13bSoLIN0XyvhBFX2Bv5KXoHFnNW_0BSAET58be_PetDrOs3y_UjKImNzsiNJkxNYqHU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKOhiwhN3I2t-XCtl0HDkx4ntRkWKTfXuCI-bUuP2iio3Rvs0ZNQuw_eUAH_Luj_-oJ0nwlI07QLi3sEErEaKIZOXD7vxWGGKanPV1YVrlroMu5nDohFT6M1mzxDk1oO6odzdLDRG-fWu9nvEN4ERNmdW3bhYlpc5CGa4Mc5X1-7VFV7jzi5aoLPkiKnDi8dxjngl5Vn5qy_ThI_1XHD2JqlZWPteWfLtP1j1YQ29hQbr3umPHzlu97itpTjssZ4dFz2bjuxFfgJjS7PHzPUAGHKUdMEbNVu6fX6AlieCZ0o9dVd4O71Cl5_-SDYSRvkPVV9ZmUqy-aHne6SVbSy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwkHX9x394FlciunUHEt29DRI0qcqRE66V4wGsOk137KpmHbvJ6_uNSP6wSv9aBq4tbpKdCwuKRhBL7Js2wRi75ba4fKkZNvtJLChbq3q445U-ZZXSoc9Ab66wWeYduBfskEGffcCm_zK5JIY4rOwQmi8HoP1BEoTLELFOioNaVZUpfJPzSDHV5J7QRrHnavkQuTO_hl-6JiETANnosoLjmNJkKWlm3DRQwCsraGFIEfcCYHjVZJe1K9-XzwWo55jkUeAF8vC4YveICj2_DskU9_kQcWHSYqz-oCY9-v0IxhZ-BTcjWxwPBf5dN7roxOUc3POm623DQ_nL_RuaP6QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_kHRxwOItnujYdzvv36lf1VjXD7HA861Zg_HKNCiTpWWdzH1lRXo6ibUGHBTxjYBY39I2PH_1AxO1ajKkW4QARB2Se_AHIWq1u_OHcPZAoIzkIUWuog1Ap2gGVSZIPUpF2-_-V2BsS2Cc_-OYOCKSE0SB6sljCtSTGwsUekDBLGofHRIjrIV1ZsrjeqihaycWL0thwZUeiZ7vEDoIqa_qT-f6d6XC5ZOs6C32ivSLWXmXlUpwN6KzysI3mpQLxS8S8fXzjFr4NwFAnHksCWrE4hLRdhwlhQoACxnHxCaGygGW71WZ5-R49QOW6Eoz1NRi6_5K8B7Z-BL4QZ-m_2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3j6_7P-cwHOqJsl9u7IMv-0mNGICFWQYF34IWdb38HCRm9CAli-GBfqW-6RGxY-a08A1CCEXgHbPf13itQ1zdfV-wntHptX63iEQ9saE-fUeU35bGAuafCyM2WCLppa81VM21HQdPW-_1S5pa_EnDyvT1kBWU-fPhiOOudwv2fl-67c1SUNoYR-qrDSEOtE5OUO9ovJFVQElXXPKqgBuP1EJLlq8g3lTyfihvDMJXZFslfL04PiMPV5X4tJHi5CtLjAheh1a9NPWGvisfWs0wdxEX5zM0GjXiIKvf05UgAHUmUDSAOC9MeM9HzbQzCBVNAbuBzxm9huC1ihGhneCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnsKyA2SQhL-UcqInIed-CkRP3YI4Ci4_VawYPWqaLUeKHQf5myrUdLCT2wCeiPvH64OYRtJtdDjv3KZDwaopPT1EaQpGenfvvpm067Iqh-T0iIf-qksXlXPHgsP4LzR7-5DtUtotn67j2YeQ_Ulx0oFAU9SaGxBFbKDgD_8KR0iUnz5bDucBQ-YpjKlPxS9yisEFJr-LkYiO8dZTUHlSPnBameo1zVjl_PBAbKzC6UlrZ_7GOW95aDYkVUs4KN_rKvEBhi9B2x6f72K8Rnw6PS5vbwSsDbAHEQBVE_wyGztRviBmOZ0SeuWPSVP-MlqJ_vbSS3mtNR_9wSOCoVSsQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3pYawCTR843oDupa60A73azz-7V69IAlMRZkWSRy3AFKfbwzfobI63YtnP6JeB7XAmq3TESKG0bNjMyBmcGyQtETxYdvANjy2C4v1LbyTy1uKJgzv0iqV1usEu4ImnxEwUlhuj93Md3tuq6eZetREYsjY05_yIe5EGBNw6XOJEjl16_P84V60iRg2oAX7MhY54FaTxKiTSwQKfUzbX-267YI0Qqcur2JhDuZLbtUVVmqFEaL5rKUGyAUFk92rYuHaxzYCTZr1MN0XhUeCLK8zZkxeL9rAcHY3oumQ1VDPhmE_u2_G_tgOmUjfxWm9DOEASIrPWCWeyDimd_HKsTaAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3pYawCTR843oDupa60A73azz-7V69IAlMRZkWSRy3AFKfbwzfobI63YtnP6JeB7XAmq3TESKG0bNjMyBmcGyQtETxYdvANjy2C4v1LbyTy1uKJgzv0iqV1usEu4ImnxEwUlhuj93Md3tuq6eZetREYsjY05_yIe5EGBNw6XOJEjl16_P84V60iRg2oAX7MhY54FaTxKiTSwQKfUzbX-267YI0Qqcur2JhDuZLbtUVVmqFEaL5rKUGyAUFk92rYuHaxzYCTZr1MN0XhUeCLK8zZkxeL9rAcHY3oumQ1VDPhmE_u2_G_tgOmUjfxWm9DOEASIrPWCWeyDimd_HKsTaAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miCGlnn07KjI2bbmgIDHCyoGOuKRjrsYoF9kmhNM1UG3-sfitfdKVOntUVXicZQJy-d6-woyVcFkAQ-CONGZ-IY0KhSuIJEjDFIsglKdG2iYRKsxvXrA6I3IuJRiZNjdw8q90awlqdgMuFpWb1QrpNSCoy-vXcmmyOb61phaB_iAEdcQgs14Vj7hjkFiU6BDy30Esaw-7q5wtgwTkVPcFdZ7kvnt6gBl9JXYpSpNjTLySaLXL7vLLeuRFfdk16oK0oyvkNq7YLLf2E08p4RYCJpFNl0EWYJf1z9mZngzRi496XaQu65-JWvMxXpeWYi9m0c6lqgZ1IkB-h6k-CxC4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRplOeNReZriwL05Hcma5bJb0eRnzDPaZzqGoZa3q9ybhQ5JKPr38GrITk7hGb0B_OMJ3pEMGhu-id5QBVG5yqxaf13uX3g4tW2NuUVh5vxwVwtXN9tapFt0DsATprDbS6ebXpOjkBQc9cbPIGBzeiQzSIONIdYF05_p_8AkVDjhfeeI7rkkEEwTpVJAkdBYOoEbnkhfT0iAHiIogzJxhp-bhsO_PN2MBjd-KGuWBzEcapJtBQ9cV70qKPpAwSjzmOkU6awCPF3X2vK4vYqMJoBfLniO5M_HhWvcYt9fEhOBpJ8kf5OgzGgSCLk_wRyqMflZg2TiW1z452yi-6_1Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KakeA355kxfnj0sY6HbUgsZxe6vq5_bXEl9mt6Vpr5PH7f3edWbNcomTIND9O3bp945eiCtKgrIYtuksESRfF2OUiyoSBghOXWp5NPM1AaoqoFK2D7nvYbzxcuBRkNmhnGad3Hwtaw6Rzc4GogYs57fu8x6KEZSOe9D6dP_PosZP1pztkUIjlwWwCdRnKSC6Q-vbuIWqgVQGqfAzq0PH6lq7447jlGHaUVQH0krCAVyOTLmf45n7jkx2gJ_EgctLcEBykGjm3k6u2y2QJGzBSt7jCOIwT5baGJbZBjMEVqwoOplIHYUGgOPLUTnwpfBOxit3wLkzTbXgsGne4jbwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXUzrgoFa2Y4Y_7Jof54w_AK6VSPJ44mcIdvfNO5N-mqnYPP910qDZzEGQkVnEQW6Lz4zyY6wr3xSuqy-pi1afh_Be56eNqGQUzsQmZFOwJ5SXVpZcAyX-XF5k0y2O4etAU7mT9TyYRsKrGP4BSqrAAquKZKmqe24afGfbi8N3ufrdecJsSOUi9Gr1641Lr6-waLGu-NFMTt2luhqgs5zVddhvCjOfUhwJookuDkFUP7ycfQ12LTnO3OtjyLrIwEzGW8twGOzduT_UBfav-d1obVbA00z3REcpjih6ihycuQtWNYw0YHSNgLisIzMOpk7XeeBCVqxIdIBvroSMCESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a54-a1jbpVzMUKFyxjETplr-OZ5XjD72J_-0XYUPptxUGDCh_2VeMj0M6PJPNLRKwJMJxgQTnd0G4fp4R1782H_3g3qKvp3LXhMygqX4hj5OdWRqVGyD9ZJV1EzWz9r2Qlmm9KCZzK5VY8u4NLpBSTXcfTHEhTMI8Y0dOMpvtSq_iAwNwizZtWoq0Ru7R3Zo9f4Wd29_m-U8QZb3WaDYns_ITxn620vL0zjdKcjmGUT1kdT4aXcLDQqT6NARlhSpZf1dAdctRhjJAMskgiW1ONdRwupAAFc3HVDqSX0uVrhhg-vKccdmq_8EE9vEU3abL-7gE_-RIbKWKA8kNz1big.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmnNt8xcWKVAcgBROaK6R8ZkZLn8IqANrl2vHBM4fGVrOjRa8QVUR6X2jBoYPmofc330_z4TNBX4tPRfiKEJZ5kUAJZseF9ccENjlYLvYLbbW_47aWRoy0eGS5yQsBsgWLlyxJB-PKWS1ZSV66EVNyi6kQrwinYJrtv_7xxsfkolGtfvmCMakBHYhi-ucQG85WRh5CKvpY1sCUxy1ioqwjcJVzuNTWMIYSDti38P87KTQYiuQ9Bwj53J1gr_NNaWfx3xuQSfzNzDfwDqmx-kXkpBTugg-Rcb_F2fMo6a_gitqJcU284hPDeQaP1Z3tJJb2drRdOxMFn1VGhdfAIJYw.jpg" alt="photo" loading="lazy"/></div>
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
