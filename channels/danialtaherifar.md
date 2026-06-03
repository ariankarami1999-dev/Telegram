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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
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
<div class="tg-footer">👁️ 134 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 430 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 575 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1h-LL1R2dxLgZ7YaDla0DAaFeC2D3LuVPtwt7ZWug1UKr-d7wTDuFtdW6Tz04vhmM43epWBNUf6bvMaFYIvp8kmp6fFxofqQnyEWlSvDruHpjI1ZBireK2XcyRePCTVIBAJYCzb-ks2TMZuVZrLcvncoCbVnKAXxmWqVM3fl0aUzql6qiveuh3aDzXL0_3GWKyULr0G25At8MHUWjbqeD159eCyf8PNtMaoDpIpZ8a_hsfhvkYXRDos3Z08b_MH6YUY6z08TxS9vgbRPQkkk8PZN86KDa8QMqT4WJnq5bsGbmcTOTTdizLzuqbhmIqt0jwl7R-GOdyFPnX5WipMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 706 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axEO6d_R280I1cAFfz-HsDQCZaIBR2gGKoEXkAlBoXTV1t-alpkjtaHkxH15PhcUZl1qbRNX-I2VsByzss8wD3TziR0kR5TYpfmyQijgTfDB0bO_Y2assgMTQjNcxMSPyQubTld4jdnfPBY7lWfFpg0RXdtbQmYoOheWTgwrqe931rA22GF7Ey-nGJaJTZavKxaA10vhu1kC402Jq27G65qOVg6JsXFIBsdvvHveNG0nyVs3bH3lB1Y1cP9q2pexn465MP0Xq7RcMcFaBKENv1pkMrxxfZT7_NvbKlcpgYnGgkNWk3kyDQxk8Foim5MM-YddmDqJmc5RUhZ-TaoOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEUEDfazZ0W4EH6SglRzCDmy1HmOKf1xS8bdoEdmD5lvx89_OmzHayJCntX4p4C_aPp3VuY0O6EDB4NyIIWxV3vqpm3RYQ82YaFjo2R8WSrsgxwY_as38cSu43tJpVDTpOlQQd2aKljKiI5fU44215lUdSSbznq3SBVolKbly2Ak8Ta_ZS5Ri8f3R3ArS8WjcUGkpQi4grc5OqUG_GVKfL69x-5QCtHp61DCeOLeOOlKmXo9a7QPt6KT9dmH2Op96oO7_faK457tAsmMbZxt8xHDMaPYJX2konMP3MWFSsjJXoVyRiN6NkMJEnD_anbhsliLjapNkLrkyWLyrGvSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdGrtl1kdOp8jvHEtQs1jrz1vF3-1nBG76yWEjddRP9xQvaVmH17dvFvZ4HQwpV5-AwMXLaIViJwAor_cHK5F5hkMzG-0PtgFEZ2Szwmh9tWHb-MTflTIq88SHd_mvE6bG3DpBHEsqNuzeZN-YJL4s9P9iDTLqNFCLmUwcFcs4YvDnxuvA8cj206Vl3vJ4HNQ6mTRGUqZ-wo8YdOxQlOpQg7DF8oHgvmW8AtC_Zz_GCqYbjrLL2vWSRTnj7OPWKDPoIfNIqAkRQTtNd-bPVMhuiQqt6ZOnbIMrBlxFc_jfMpjHydTlELYUVcT2YXb5RkN2VCZTVcbODSgTSNDtz-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 841 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeTbegrt1wtIil3XfVhu5rv9l8-HQL5_It7nw_1eOLjhn-T55rLfVzwt77klWlNvLgkEoVgAqDX_PP4p2xcJzaVsoF0L4fdwZX26gBa0ZBhMYAbhOe3l_O_Q2M0pkhnR9uzQsmv7XXMuIzn_I9R7A9ktnX4oAI9vXU52LzM0tdR00FOLZeNa4Ev5bIDeKyB_UykVuFSOiMvcI7uJJZBGtf2xP4Nfr1G9RuCTIXHZ2DcmLDNoEiwJMgF7zeUjDHpN7IS0cwZpJfBf0Tw90mDBFTPqG-5W0PCRWmKaZHeZuPDsOg5etgIITkY7PQzxBHyGgWrObIZBEkA3bjVElpUDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxc57f_IklPEgTB-xCe7CGjeK--mIL__3sN0tYQ6SAXzQEGkrRVEP7P_T035ZnjZhekqDDFOwdcvOIajWhJtrZZbSEpnj41Umgbj7lrGX78URrw4CKPNl_8qCIMPnuQP4UFxy1CyP1bgH-Ja0kK5wdmmQk-n5hvpfFyhRZPNrctDN1HDF2XwYN9h-DxTO-KzZ0f6Krug0DC_C_N1uisaK3Gjy9A0Mau64hKhETtQo7Oyd1T_4u4mebzP1q8kRp8-wdMy5u_YDntZeKafeeM1OSQplAXb2zU3IBSyeAYwUVXqtybZ6UKpJrWJRLPOCaSV6iCjrNWF8VhXNK-cnIhynA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbg5s4j77ELOTP6_NeoQg8g8tLe0f-mTfGKnRvHboB5heNGmHO3WFpcAo_CEOPGCWsOVwaTTjuRAYC1MNSKgrQdDwiEmJ3rktk7h-lJic3pThZxulhNkYQh0rA4YDE_auUG9UGKFNkaKO6Iza_PYbZpT8H38dT7pO_i8KNcyE44gYEaO1lpuF4fZYqXSSx7l2GxYz8rZbqgGnx8q3IMFZPCg3LHtAXGzaYiVJTE1PvroC29u5ZMlnehY3SGJqydAF78xChW3ebO4qAOt6LhDtqbNi81FtAtdiBLdV9X7j9B9kzwtCmrMCOx20MxPp_QX2Jpo4U3hS5d0adviLSXa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9g9Ycp2ckv9cTgCDc-fxgj-ZHclA2kYWvZXxaQ5vDZJqrbWcSqdkrXhuYFD1we8RFK4p1bfL8rNxZz5AapBWnOAla0soyNzl4VHArAK4aUCbAjgqYavp2npXqxL63Jf9YSe8ePOlPfx52Lnpw-gVr7j9jAm1cD2eTHfZe-hhrR3b68NGQZx_C9Wd3qAHmvnNzL4gFUiCIWZ5BggVt0v_3UHcOx5yAE3BO9w6bai3nlhY_potw2v_6PDEPWvl8D86B4Tu_5lpbncUegdQJqmjwjOddJx6UmtA274TDOX7nd7YFgtaNAPR67BziLT91698OX50vmDF0ZL_Wby9v0Z4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC6e-OstUekNCM0KIMXlOmsmounbd3UzGSYnOwCQaGx2pPV3MydHMzE-iIfuYY467kM4dIuMdN8EuIYD4crSCmAgHo36AJ8mtwUWe0Z7KnQ-OK6mGonTjBxUf5Ti4zDsGUiGUj6QWqBq6cTo2qkc5y7Rv6ZEuULABOmibx4A_yUCerZloPQFS2vdNmr4RhyjC4HcsCOLROyb68kCgdTe_nJoSa9voi5Ivie8BTNim0YGb_bWk48IxrjfDSLe8JlITLEdk8hwdPE3tvQMvf-sV_r4y_zjCOR_ROA84ZNTpmQXvm5Ti30xKX4y2q1trHO4k_zN8diQNOQkud-VsBiSJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKwqHup5QZnGFDz0cyCd-kmxFCdB74unbl5mwgspmsCe7tzkMlifVJuEkJj5rRNrgFxzehY8vELTTirYWKR-JGnq9UHLCNGaONqKyHdwY3-ocsLbcjcZstdpScPWCEKWea6ywIqsErzCotmgRCBUMOFLpaB0CM4SwirnHYuGwPsymI4jpbO2WuqYIazUFpesrMBDAkAlnQ9XzklncXPi7mCGz2ceaX2vlO4PhQWYl_Zu73ipedOK2VtMVovwU-0f89-cx3Myh9wtu8uSoOhdH9fxp8yRVwyRFZb-dYijRIIMMBVPYzwvghEl20JxJuBIEf5csNeSDEv-aeNsBesstQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I98P-9vwu-YwIKt5abn2VSKH43kxTRf4I-ERPlY09lDMBF6XQCu_CRWeIBh8xUMGW3IdlJAPswYutdzPMnOh9_CGjU7Zd5OetVEKZ0gL2zMUD0ibTF8y2k_M6a0MA6pMWHepa5fmeBGlMtWTqR8WKLEM-Q-NhUTmCDEhm0qVOyzcVUt5hKba_amVPeY7IrMqP4Cakc17NfBvyKCizR1tl7Vf190KOGJqcyIxCHzz2dV9EqX1-WMDGfM6Uk9y2Vd94Uv-G5fi2r3KJ_P0HiIJPOSkTZ2B3Ux6ogfDoZ5Y4WnS48S0K5T8FXLBFdGdwnmP0M-2RG1kdz032dlhB5Ja9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIW7sVM49f8Ni3pazLLynDgvCmGMuHTkvVxKSqAz_tx0zf6LvDDy3BVSQh5BS2dE4BBvD9xhICk32KA7dQfmX-fB3wzl8w8vA4-DhUa81R4yCaFHQ3kyah1YKk7dKyGcLfhRqm_nJnDpKo2X7WVZ6-hSqYoBa0hy1cmE-bmOHIOnCXyhyV44HU7JJWn5ZQ_or3V1jfx90LV_yQOzq8RNyCJprU8UvfZG0WBBOC9vs2AaVIMbYCMJMqlPIyGuHmW6HHwBx7vzwO00TLGuzT0Yb3n0bS674Z5XMivIpX6jHd4kaYlF9aZziawuIsLflXXRXq-ltdSqoasGb5WkNwRaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6eyAv8tke87HxbNx_0nm6s-uMWWQqXw97Df1IbuW6eAQ65SqhuTm8b2zhXIJn0EQ1aN5xK11GpPh6GFZfrfSO1B-Z2vG_ExQv60kd7lIwBHMRVSrA_NVTFAX8tdz5lYFuWaQfUZM9mAWhBo3tWeW_a8QVpH3Sm9m6xG4_paM5tkJDI6JB6GzX1SPgcAZQsRlwTMAyBff5XJxiLtRtcdXQBbdnUb073FmhCs8lpkrmZZValVVMJ74VHVcsnpdci1K9NkhOkj-KTEMxqtrEKHjOQ2sHi709Y5uTOMHaTqI4GR7wsuqdkM5OHP7R5-t7GOC_HonYCXjqjVluczW4BnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZeCyAYMUcss67Z4YzHG-C5Gw95cFqpQZYqIEY-PyOKubPybdDFnzFd_2C60-6m0cK3jTqLbfjOB6chgxg0fUxdU24i1MW0I-OjCvt_zzhp3RabJuP36G0Sg4PPBWfMZhEKdCHe2YxBAFuTV-N15Y5UHZPweGzh3-wTg8gbmgSjzXdYUVNQzWo0atzlQaKN17armVDv5ZKmhr-sRvZSWQJH5mXrDUV0W5i5q2x3RJp702L0h4YI2cLTHC-ATbw6EswH_C8bJDvYmKCh10AnCGFg9GfuyhHeDn5D4sdTUY5U8IabT3ca2o7InSIpSKLqzLhyHmIQeGKUNFYxaAHK2Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcAr7WmOWnJuqKwwGQ1w7G5FuEZ7jB-dv5Toyemd6E56jvV-HtFv0Va-n2DD6o0u98m3vCpoAlLm4liDND-bdTyDy_7855NUx9McQ8d-gzfZHGTKxxVCTBpkjZcnNYA6UjOlez7A9Vh6XTEQ17-jvaS7MrBuGyrH4UQP7jsG1CgnpRNN0ahwFsDrZjzrC_lxuUBXZKdhLG0znSB80sY4Ex7YtSksDsmIq1klitZx9yiR8REYyt5830nUlRijq9G_fazWmW-L5KsCVtzDWr_at6mx2-gpG-UBHg8-aWfNFm23JfU4UWoYpyx029EuLw9plcCrGeg-3OcsH4r-1iPxqA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=u4GFkMFzHjOnYqPFaXr1R_dg_MVI_D0G2uUFvoXRfel_OdEeBsDvrP6EPOvHqazehwSXU3tg8D4eMEAYfQwdJRY43gy_S4AmWjTfS-UaIfHgaaY6NWxBeQ_30Z1MqzKOAXI9yUMsX0hBeAbW8dNin8NAq1YGfvEChvW6pzZcW13n4FJP8R2-WT4d3mIee1aQlBOWnKPNazyeqZH6kUgsxDtHWoY2JwO-ScC_vOkGnCUbHG3pTeraxHjWSwDJmKi5cXw86mbbtBCZ3veqR31wdwsHpQplCM6RlvflnTba6iforb7FIV0sqeR8E4uvL4VkDnwjMGdRKTP2JC1Toa_nRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=u4GFkMFzHjOnYqPFaXr1R_dg_MVI_D0G2uUFvoXRfel_OdEeBsDvrP6EPOvHqazehwSXU3tg8D4eMEAYfQwdJRY43gy_S4AmWjTfS-UaIfHgaaY6NWxBeQ_30Z1MqzKOAXI9yUMsX0hBeAbW8dNin8NAq1YGfvEChvW6pzZcW13n4FJP8R2-WT4d3mIee1aQlBOWnKPNazyeqZH6kUgsxDtHWoY2JwO-ScC_vOkGnCUbHG3pTeraxHjWSwDJmKi5cXw86mbbtBCZ3veqR31wdwsHpQplCM6RlvflnTba6iforb7FIV0sqeR8E4uvL4VkDnwjMGdRKTP2JC1Toa_nRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvxHIogGXZ0-__-jQHuykc_6jf7UssgJnA-dyEEI3-vswsJalOF2rlQCwJl43U1WF-vskAIo92cahRERrTzGGQ8OiXWU6ju8T7Q6C4uasTIblvR-jKuoNZ_-YepO_HBwXl4haPNCdXbqtFORFyxvjX-WDg0-gVWAkXBsKk9SHH3tJBqwWizflWFkcD8kUQXjMM5mMFzSFS21uL1zzhFsFbBapdS9p8eYd5e4KWiAdj3Z1eJGytOJm-byJlgpNTUlTE1e3WfKxVyRzoTKhkIhtE6VZ6nZWWRyaTVKHFWR0lgpI8SASoDLc9EzoDqeLznAdcJIbSEiWzwdalZVK_V7DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8SdmtfRcfaZ4L7IGoV8X2Z7yC1tg7M-3UtiSjw7MmFpBOHOj9zqSDea6uHgsSdMLb_ThE1fQyseeSGvs5tOjRLqN3KtYvte5-N-3KruFfHh-Ap1NAI4_WLTg-FvJN1bG17bpIVQjIezAjpgWcxNQ70nTD9u1VWLeKY_bJ-5tVbOw45k7fGHxdVUn5hlUFHHjFHwJmVVKlLY0jBBe2BUv26P9xEiLdps8E3RzoLt4N7zBZiY-BxkUduuN8dqr_a11GWwVwlXMc32G01ntdpfSH5nYFO0r0GZrCWKIaSWU-I2X7AHLUCD7xojGJIxkuzdMsycpyJAfxFbyY-4CLfu5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v64TlmHP-7UyMFiwdNMTPElmoqnKGcPt8MYQCdlp6QY27CaYcXCa-vCspktDYfxXk7aooqyz7E7DUvGRmxOKQsAZg5x4xnMVUEDrk9x_9P9I9b8h-dphTHg7G-wbaq2ULtPZTes0D_xGZWVHJAFAmS8QVkVNosuCwntzk0ZJgEUA0Mkfsh8VvwvgcGjxQuxlAiKVMBaGSmLsyfBiIPzpdPbmoWdyQLq7JCV9sc19qKSEmopi7o_PzjY5_JFitsYFlJ9KXXq1aE39GXQk6C0mAu7vTwmd5vKVFiwc2uoifq1pjSkCpoJE9aYKHI_uiernXss06KroZ9gUc2L0j5jOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRVdrrdRVqxh-FSmdU4mQcC7gd6AWZ8_Jm7GfPPxZP-jFduimz6Al9IWjWfYMMFEdlViPEU9NjsL96FjaU_wIjL8FRyNpd0q-YbwqonXJE_CL_2_5hYpxhveOj1yulZ8uKo8P-STQ12Enmf3wB-8Bj4dK4_LTzekkH9RuP3oYS1NE0IQi0h4YTf9vGsY89Oo95jvyg7f6xQpUeJVYUDSs8qq5srzqnrUq4AsHCjQbjfYX779FyngnQrKFKnFfEc-vunL7lNh9VcQBaAchH6fp-fEQDMNxewYFrvVCuGhy8gRtAPxNXGZ9HoJVcTTFG-7jGeAdlAcxZobJer7TQnPVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsU5SjB8h6hN4dESvyZ3ctOHC5sSsqpNwWo6oB4-7t4mV_-zFptWnN5Jgj8cy41-w9_Jq788xUtzOSX2ylAxaQ2wNbPPoTmOqDDjFFHxMORz8UhNaH1QZGhrkH1KJgbrp8M6osSTQjJv1Glxfk6_4wTGhPiWLk_99AHweVB_yU93jzn3fGYcQEueNKXT4in6VyJjLsRDUIMvi2Y5IF59y9T74AfvmiHEHPBwYFvLAok4Z_cMAoSLs3VX1abGw3JvyFGqQgXegOrRB_XLEW7ab9MUDXlOCRBNE2m2m3ER3j9Sz8dSNNILH6vp6EquHAnR8KR7Cr7-EsXSrJzkIE24ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sco-wMaPWYPljRyJSriu_UG28XONEij_4I9bmDNaywOc-ylkL4hMpr1xcGnCiGacOD8ncEIY_zknvGq1lbo3_7ui9YIZaV8pKDSdUaYw3CTjo6ocwiAnm8_TpyPYu8Kz-jSjiyh2-PkA6JDhv4QTNarsb7cwOUKfmZ3zu-enurQjKm1XcbzRl38xehsKd1W9kBiWygvPMHcGCi-AmIAw0bltqoeO-N9xpq_Xo8q1mBJJRu9WUSn3rG2k1huLrvgvDx74tjmTS0TrmmE5hxZ6KW4r283kPx_knk9o6Dz3_Tb4lph0x6oyVNeMI6VOTlMjwuv-KBOUYcuJIRTI3S6d-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCasz3bCQlVXhWmr9xmIQ-ExY_dyhdDEc7Wtd4fLN3saeGedUDrx4v_9_cQJplTOW0DrNQcaWusBMrGMDK1Dckt4_XilRW4SipJQXQAphVQ2mmbX6mvlemZnToIa5tGIh6OEO0kK_IVsaGSDBXPu7CaKN2Ukpqr7G4PtkQ-Lw1uvjgm_rbBQ0cTPY6qbDI7Hc8WT2-n7uiLTP-6hugu3nt4yWXw4K-0vnnHRbe-jLae3bRZq4khyV2bRnXtoH6BFbg18sk55NYSZ0TP0n8yigNlTntWwEAtAJlcvnYYh8cn9cRiqkzoQj0LW0knEvI78z5SCQlhPds86nFmuU2RDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyO7FxeRfnAyLlgswKHZxWArUxvEW2LqRRFaIiD2Ux5rgzuEtZ8Oooqdi3FiRjNCYhnPsINQaU3o-oCuxk1AXaFZGhv6hqjH4QpVEQ3xQt0awkvx9IeXeV-bjoMY-FP--REXsX0NT4xbxLk666L3VB2yqsWBoBzziqDWT5zEkgoJljC9eQAUs2czm045IZaCG6CLp5hi2basyZKLo0SQiQ3tFD2Aq92bfZJEasXjIA17SnE_cjph3CKp9qiKJ0p1ochOoBKX9mTv9xCthEpFsHyfq91EsSzOtnWxlp5Q7KjGEXsmODwtb4Lcsq4TJTs7EBsrcktC9g7ph5Tllm86ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bktRCsEybsOHEgsUhdewed5anPRxup6DmmK12xi446EMbCNx19qHlBoa5Pl2PxZPRx9cC3Vz1NGP31PI7Zg3WVzAfB3k-5yZBcTD5u4_JWnazcDwAAHduaydovv0HS7_HaYXDvY3lAOGgyVBgvHu4MWYF-ew6PvCsoqjxiM5ktq5PewLwAMxYPZ_pMivSsBQJ3ieBuYmFuoLUWQlngJwZz4CHNwGAJLm1-5mHfTVm_VnnHvNDOV3h9P1ich6hlar5gA1Ni6x-VQf0JTZB-FqXvJ38Bu-ige-7wRO4X0PY90-bc7j1-srnP3SxY1GzXBsoThNm_q2-LqBsVhjiA0dPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g61tKsZcAtTmQwjVdiswdTxF1e6Wv6BxWbAwJKESorKCrf2k6ztU8GaNgqDpTlutMCV1ihZl4a4TVc2QKdUBF96u-7qKuzSCN6DEZwLN-BtzauI0DDXlV2oGuJoOLU1cZzstY4UjktVVZxuDoxa1d265-SLn1Ke-yAcpB2kGq_UjmN5S9Qni5eMMZxZXStC3Re3ZPPxKg4N0p570Uh1Sup78PXPWO79fgviO5zS4mj_wiKSWpL_fbgYHJCVyMdaCt_mL_GGNqkWOaSC_dpOrrB1XjH8-Yp1p8eXY6phVSvO04o7aNlSqcLE3XNiUt6dBCgUhSPi1t9ILBBvzS3BoAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF9gmU4_j7bgGPaDSKX3e-1FwhiYI0qgYjc15GNX5Zbd-MUontuAe3kxRvkHfMSdr4B2Qxhk0uHZNxX-6HNYOe3PU7orWXxx1ROUQt3Ljl7Soc4CeVp87F9dAFSKJW3cRFVnIHqZtre2SRV9Y7GAApKKzSVkV2FOvPydn-qcopoSguJ5DhtpyXYKA08-Ax0pEy-1NteZHnkAoh8AnsgEFHxzv0J_vkjL4RkdDdWHONu6jH0IrYHUcJhcquy3um7DW3Qna_Ud-VTTjQFm_BRGPJxvbM1Z1S0ghd0e3HGMk40FwjyHGVKQ0xTw67TS2pO2X_jJiSXSrqP3n5FUDKUYWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGd8dNu68rESyJkJN2Qs6834QBuPYXlGAof-aQlBpBVnc4WLwFYVubRnAkEmQMRT-9QipeJVXZRw2A3yIhOmoaIcqCHOwZ2i-mxDf23MCToUQva8t6Sols5GeXYF1hp-1lQgG55N-WILFthr9OFPVr18J37BYpyZSRUcKMyw3SS82sqHAYMdiCZOD2HRStd1tgzaKlrdpT9fVRavMHyHyZ59ydf50iq0SSRw1T09Km5FSKaPDOhnJTt8FQEyXIXOuHmmNJZ0yOAQaYsY6fXrg2WtDr_vknijSWMWWZD-cQ1gmmeWPI47CcuUezQAOQn7HCWNcmyEjCd_w7x0H4w5pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFky-pFT0HQEa5Q3Y8SPw7E9jabQ6rxMzl5wmdg0LolkTE4AV1XIbnigw-Iy4aKM8zk-xg50UemLYTDgAbEHQVWYLOrTsM4s_tu2hZjJ6v1MZVDHI65MnGXFOzqZk1QXZHItVugKYdiUWE6LacuEogkT3Az-tKOLPio8YhombU1a5xPTddlFZADnrh1x8mL5YsgVQ8iszV83e6L6Q1jZcwJnanoQJLr_Ydqllv_bKrjOIUDBguoJIfCOzhR4sYbpF32BTrMbXGH9FZq8qqxFN56xIRqRcg6s6smKwIOxObt1zutRotlKCDJ7Jhsrb-UlzTYI3BzIq3R4FriukpzgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNYz8X1ETTdRxfpM4DUp91xqev0kycOQeXWVomNpzPNI_PEW-2RGjW-SXUYnIhCMAfbw0f7djL8r85YWJbK9Y6NE-qWC66yBtcAK31MDvIa7NHN4950aib97vNwkaZU0gpIedqBGOhH8v-mvUymsl_LFc6SlmV3TkFGmGYMdQ_Iecwp7uVuQiBRkviZDUi2EIKCwciqynfQNIX7od5tP_jMFSsUcsfJUE_dL6g35qOwpWF8M3rkDRwD4e_JdBqalGZ7sIc9Rlnwxeby5cWXuhyXScXg3ewF471_fb5WST_6k39vMonkHOW-8G46GVMXiVVcESqPTXxderzD88jxE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKugC9Cs2rJAEAC7LCVrg0o2uwnLk8xR9-g7WwOmqWiSwxPQqyzGOXNGzeWcEAumjo0BQwhTGScFdwbrcor7ZLJCv5vMoFGt9krfQb9jllr05-EX9wpJL6UiPeDaeaWy4YkvL7l9QwJpDuJy1zt7j6WV02FgXLXuNi_bhhvHDPPruMoYaO6onTT-NZCsxNzVQdwsrKhcTeC_Q4HL1ogSMytzWPZiUB7nTxFns-P5f_oTX_etX7MzxMDTmVQUqBZmkCH1z6ZoMfgxuRgJUI8GXAitBo8n7VkpL6D-b5WYkmN_yR5vytEIwVHKEFFy1uOGT2V09GhV08_YUSI8DM4GeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5ZJ0aYtiXE7MYssCiuh_0Ssp7E6egMayCbR1e4-uBDbqTB3rASdjfsM3UWOhSrCnT82MffM7h9WieYhpdjnvcstAFv6XSulJrlbkJ1Z0PUjAA2E1215KvKGgrXVHcnSCK-xm4klHmUSFklzNhH6xV-9H0vZdRSpCWkr2_s0inhpHI7ohFXH08pD6ZPLHAqMuZ-yY9oICCzIIrArhhv9wwzVY8JVYBUltDrTwfoO4iuQ8l83sNuhTPRh4hODdOPaL2zzyEFZaUzfbMzpz3GOO9s74iU35P3z_PGFjiJJlP5uZMSfBTcKOYxA4laUJh8o4oXrWLvIcqLdteSIAkDh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhntgEdCsjy6aMVGVb1XLaesfla-tPLPz7yd_-XDyzdh5qwoSk4J987zcDwc1DHsQn5YwEfv6DrYSf5qfPiokA3hymYh8oJ2BgFInY0CFL1WNXiL22YPFBd9pt_lAleyikUey0WIQpSsw18G78GMeZwElCNnTZC3Jbb9rz_QEvHCZMJVIk9kmm9pf0RLpzl7J26EqvqZzT2mfRpfUoIw1DBwlygQwpFDpij0rfLQDwXfYxeCwPBC05BaEyLEdrWw4RBAaWGzt3RzZLSrcOzUPnYvlcIbqyzjco1BYccX8K8yHYXD27tpDvDLeHoR6QipXVr1EAMUbNNcpp2Ef3s4Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO31qbSKqxrwjRpNIxh5JscTBszIghy07sC96Yt39P0Wil--FJVsTFFxIIescJoQaY2_G10SpuJv0SwZqv3tWrpPoJ12fmVwvWvjmIYtTY4on6TNleVlE-Mk_q_r-2MCwyNiFq8HAa3EmobNEaUMVKq-BjPRZosWwkFlV9MwOC_wrlL6n8gu8DU8oc74QdzgdQEkMkWr25TxfHh-gSKAg0xn9FGQ42SrsGHCP5fRD2sGafmUCEPFw_iSPxANKDFMMKkeYxYIjL52A6wILvpsq2gOXqOmtGmkyaGX7Osooy0YR03Zv4wkxQ0ZZacF91PuPAY-bQOByXmQo__OM9pnGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwhU9EesqjcgU-7mBgpIdIPcAmIXvzBTnCJDAuOUVBWO6_MQ-Zfp7ZyV6_AfQDxjgh4zIH-QSWu_BpSGfYagZp6OSN5D0N4_4ijL7wOOP1w2CmUbtznXxyOnwlcf0b_tGBXKFPyRWXC5LlTAOrHJZ4GSHGRl1Wyuh0hznfO3aqYXdVH0zXT-wBySoNtCgQJ4JhLcJcvZDRHit3CINyICAxG50pEwm09xJZHA__CWLtGrLYq6WJ3Vtml3CAtuNc5a6vUgDPLCmvvosBTJ7jQ6Qf5ZiBl3xLDkJnDFOLsppztu-2g5tYYbVtXNd4oQYg0S14n8cbv-zy844_Z1-rXSQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECPYSocFVIuhsInDeVwT3QKjeKRxEfkQ5k0gNyTOJO_VCF7DJ_0PJ9qhCw_0su7JjtQBAaWWZypgdjX-LbZrKd95fPpBJrxwueOCuJsXAOQvPrT50qTWCz65-xJHWSUi4b9izcfLPOyQ6nEX3F3dTnBYp3k79vCkPzu6anXQ1mgeZ_ZmNVxTPqA90RMXi59tFxu83ybv9DMCd8WIxKwSuC1VQpp1wS9Qrz-Z0BTY8DV_Q8WK81diyPpHBAW5dj_tONCpnfjecyrVRhRW40lO6SHKsr-7Wymw2u4Ugakp-puAFHcafyiLmvFSb8VRKj4hw1nkZwtiXCcQ0eDC3dEQ7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kimNX7_3uZEJZAv5vkN7mqWhT2DE3fQY6iELR-JoHXKCVmnISLxNoNBJttCU8hGndrE9Dc4so_0skPupLHFFO0jnk2uFtA_m3wI2ws1Blc6oL_hGjaPGjHjlewM_DHT30s3lX9G8wzzFaMJH1vmbkvIXHklEWSvOj03j06cFRoYA-TI9oXwp6g1XSBhBeYE2TN96xZavVWiinAaJQJTktp_kaUPzjFL4m_ajgXjPuo9g_GcjO0XsdqBAw6pBrqlWEnL1JAe0wV0awqFOjPqDVdBhvkBfQgXEwQjIQxPlfeIsTsfpf1fmRJ1zR1F630RLy7vzZ96dx_e4LN11p8vI8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhwfANb5le9CGJeO9r0vD6lMFKWxoD7ptobEI6O6Z9F1cLGTu9MhGx_U8VCtdfF8wQnF4aEq9BlhALKOI8yXDvHMvxOvpa1l5OhXdStoc9vjFtjQLjR07VX7zPkaEEjsGohYbUVThTQPw21zC3fr0_Ti1WEuSmVu6tsPMrYZSubJpyERu9hRF6G59fbJzaC4AfEyYeaSeEuQiJ-ZjQnHzi1AfxSHOBjU6EJqT7CUjz8NDWvzkEMHNtSmNi34UCFhm7ItYI2GxvDknKeAV8LvKwXgARjgsWHb6zSU1YdDg_ZootqqJ6kOefaqaO4K3EgOy-_4ZNkCyN2tQRE1mny8aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLgN5eiPBzaASf0IC6wicKsmAbd3-5ONXYDYrTckKGYYuaLLCBndZ1RzR-EVnVUe-3Lfec8qvqW9Azky-N09JcXIDAtsox6y0CejOFVhoyJP-wED1sr5wFtGzM7deGmqQXtMBZ-4Zp4w23CiPckkP0Uyxh1nOXm5n79q-weRxsvwj0B_Wz04kXBOp0BMdM_DzfnB3uxf6-vPxedPE_EtoJlAfDEGmAwMxX818S6H05zlc-aqBFrFR8JZ6c_ypzO2NuOYndwBYD-IAFBRJW3zqLOp3dCRiP_ENenk3Ptdh1QWaWGKQ9T7fzoshQ_r4SCK2fPX2izEy1-t--YrN5e25Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3-B5bOPn5wmc3MMVD8HCcF9ezcOKF4bH2QMJrOmULdVpZqWvPuDgacPKGimtYAoRojutxzpMiWuSboGVWDeHImZmV-IvbcwKVSimXiVrdAkNdO4xahuJxmQTQnsRERM3a_V3sicc-RAiojJcBwlGOzyoLjegx3buOBrLJBu6oKEG6isFVdT1Uxisg0omynMq_8q9bMr6C1tvvNmzKvLgksK_7dHgReEES0Zf-_VwyVijbeiCJOumjeML_Bg2E8QMX3--ocpSESxkzcywkG5-X6HLL7_skmPmrukvTwlab8qQcbCrMPr__RXXVDNJAHHnZEj3SXxfOSLbnGjXZ8spA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZntKYj4gfgMBQqxg1tcBdDIw_Q6h4xAWvt_rlMBF4BWg-M3SSRw4FL968bZm2b6pQ_DvHIdLHl9pupfVLaxrL2gMFTQZr3v5Z9Jz1DFLxo8FeZJffU0avEdeZIC4i5ZkSVH9RFF3zzio6cmplkrYgs30-ANm9p3TLS9aN9mJ0AAo-svSP0_wm7aG46R7HJ-KKiagnkZNsrqhHnqsQ1yqxBoCZ3emCQoTw-r-IIfN_Lz2BGPTggaYN5xh_lScKF9Er4miHPhlTUS5rHn9RXxcSDmcmpiZW_YC0mavYqjFYKXjs7WszUtBxTWc4xOCmBs7-UbTJ4lEknyF5sqEozEDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1xEv9USssjszgqK-rCcvwVZu9uwyqi0Bv8gl23GlTHWVVDBwCKVpVz77usMb-gawe5OPClu8_eilHIgAyguXbZ7KxyYh-tIX0Aycy0sAXLiwmCPu1hh9ActGP3DQdJjpMfA1JxNi0Ovi9xsTacdgaZlBl_S3Zhh0UUPU59vxBL_rZrPL227zliubGGyEb9n5hdJ301QD6_UOFmUUyGPjz6dP2VjiEtqqbiloY4cMSTKFZVFi1qx6Lybw0ICDSGDEtcdOsUoE-wuROAf9GGVkHdYYdVvVYeDEQtkmUMDcs30d7lwANuVwIdndPWqQd1KPcnFDHZlOQD_-et95w44uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GE9mfQ69UNupqIXdmDtybhDjDQbxhwssINRpKLlgFWO3fBHSN_KSTU-GYguY4dkxJv5PJZDi4rcy1_MBaIolj0kn3s2IyCTVv2jYVXSTe9zFgCvvdVbm_KnJ53ld40WyeNI6Xr1UxH14TXI6hmqFyONItJtHLJoqZyJTVSXUKuAhhl4g6e-p_Jz4CednZcI63X1fgIxegLWPzaKVBspiB62_JtZOPMC2tyPGLg6pz_BK8HowelIaP6mVKqJ8eZ3BOrU3NvzzxhEtUPjgT5WRLu-YX_IrEoTCJcITjm78iDUPVu_ZjYZJ5yvGZ7nRr87VufyGF24RZluI9nzSnA8jbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRWD3Ni5SaZ-_SIFq3ByJRU9T7sMJtuMor08mM-fUYQ9v_xnyL_dVYcujuAl9qWphoxow0v7c0WJAdixs06kRZOlpTIq4jHIWPApjGftc_Bj8rJufR2Y1MQJpjYiHGLC-gj9zAizrP-vjXt07oA_UavFs1nlOpDxKuicMU3DyLdZxQR3_hCPeQV5criGbgwxOuzgtqaiM1c4Z_bY3-bInNEg3_cEtc7nFwmY1dJEkorfUgo9LwbJvGbn4Xo02HzFWSOcFYAEULn9xJtznu8oN0v9obhxS_2ITgauGTUTPfXXS1BBt9IHCME0eJEVbZuEY3KBiFaJtxJE7eDs9_eq_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEjzu8KWLNwFfzeMs7hquN6HwXcc54r-bVgmgmuuy90B_OQMWmLScysq4kdxMRj7M2UKY4j1OTMDrxSfZumbJk8gUDf7xcxSBXC63KGsoBDj0y5o4iWtvH_ZiCPbRGPgX_3Mc_iygtF7ej1p1iI-vVE8oYqRdAlI5jI3HcupipmNYpCrry_JBUZPMCroUxAXHvstMRwdKXYSBD9kgskzbcy-pZZ7-aApb6zfTubSpjPQT4HKH-gz0XY6oEzo34ANUOoz_1Pr5WBaZYPtvT47CyyQLggS4tEIVEVf7D61OjHhKHAoVvTREYN4SawD1y6Oi0Ihz64XF1H6T3QfYKrc9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td9FFNybnVefI5OlDw8hYIDxBgOQLBzKI-P7p2juI4SlHuGerGOjTEySA1pDEHX9pxqI9eMVR6-CrqMCS-mh7lN2aQFYiHd4iWD_q29qBhZbKezrZ39mIjzvypoH3TK9SfgjVbpe_qtdp_GNo1iEehJoGZ5pZYpLjx7wSzJM6cnqRnbCHOkjTQJSqeWOCejr9B7jSm0V7fz6Lp8wGNZ3WOOhtkZyT5SHL1SprMZHEU6sLAolQ3NngbDnrm3WaqNmw3uFne4qzpx5UwBXreYLeNVPNAv40nhEzSKCLt8wqOnNYWy0ADrFsjDfKbfT_-TXjousFtIjWYfYJcWZR5OP7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfSdyCUAjZvpYo3horYpOiOyt_Qf4iBPXegsECwSZwE2SlHndQ2J0TNsp_f-ki7Axh-7NOZjdc5j2DecgY-HF4T5NOkyJEd8XdmS5yFQMjWvFeopbJgdQ6iWlT0RSsuOJI9iJw9FdEOF9erYksr0HeY0n7iK4iQ9F-XhMde21x5FqMSixQpeWO3Qcng8L24MkvEsV2VecEvDI3hW3vZt6dVo4Kh7VIHfW2Peo5empKa0D6mmLd1QPEAuQpLHLJ2ga7wbeSPTImOvBr92azLK9T3JoWNl2BF_vMSu4JerNmiFe15EQ6ogTk9SyOwTpF6pfgeRVAG_5Ubx0xH6MrANvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmP_fl0IRt_xd6WM6k59decxHpxFgNx1cXll2HoQ1Q1WZf7mbvRxICSHqRk-E0Y-kJo04G0UJpSYncaIJ9Lyd3A64oK9OqYHXyc4xuqMJW7tVSYGtz3vLezWLekyRo9reP5w1jtWFa0bY3Dt0mlOEXhaV1IVOUUXdEY31lekDRrcqvPheNVpKa7UC0YQ5JhwjGPSvuC772EhLrL2QNycqC6pk76ZEjaU0_E_PxmRXn1VZvtl_aJRQ15fVoyVdi0mgu14Q8YC4TdB6Q2J5p08W-n1nSoLxRqt_22aQdD9QCikw-4UVazTh5ZedqK4w3YrUNWouxFEaLsVcVVGgkpXTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxKH3NHQUwzoRKtlO4NXQZsTkfVOz4Qm-Z-je_8gyYqjllEOa3kvzdbEYkclfN0LE0JFHRP2tsqGXjU-ZdDAkM3kfULnFNUYH7C3XyqyvUXSz6d_nYqP2tKUKSZW8JFOvzcNfIrUjxmsQzuB4lFEtIhA2MD64legQ8Bpiry0nlm9HTXhMvvUF_jXYXG4chwUGp954nPuIM5upRVo1CILyxC5usSGtYoLlyLkvF621aLZHTKeMr7E6GndbXkrOkBbs681o622_iwFNGhRV-LuALME2oPQF1Pacov4LEIymLBsGSf_YVNkt0Ff1YtBrC65zav5ssDgvRgYRNR-tcnZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yqdlp9qUt3hDN8OZuc9Ke3DXaYRmgGyDroW5QH3CF0mZbBgUh6QN5vsXPKNR2k0J_h494n_tS8VFm9LPiZL4RVbqzgx9Zv6F0RMkBg8C9m_U_nk0m6QPRNQiOiH1Czo4UWk3Lg1bD7hhHG-nkk8RTqhHG_xEKOHIM4jD52326SibTc9aXnxdFp-F_93BoPuaWJPpUMhC-sjxrHIax7Ixz8erC6WMV2F_GjXu6_V9DWDwe6BfpKtf1vNRSwnknbx_6x0tzPy1gCAXAXWirhtmF_Ebwv7QVsUsPSOWh1pXdEWhFvKZI3Tut9rJkdfl6_9YE3X0Em5HyHDfdy38RJs6OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUmD7ST11jLD4TxRYRRaMzkVJPh7AkUQEopByMY1bOpkZevSCdv8x7p011UuExx4l6OOjvt7AHoYIgBBIqrYp0KJ09X312gNcXpMTnGAoskgzBoGqr1t7QETxmriaAOZdb1rlHMRYFHkXfygy3ZIMQQ0BHlDHeVXnmoyfZWPisCxE_rF9l0QOQq0mifJxErxRd3g4XhbeAhILNBCjB6bn23mzXA4XVtbkxCI5NooYZsQLDgfrB4ws5A73mS7Q7aO5HS7TdLUV0-2sbWU3Re9Nj_KG6sq_LMXKP5UlS8JQ-saWCkFcU1Dhz4N_n8ysMoJGxCTWaNd39X6EusiDhKu4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jiVbW-wHOwCRQhGSBpe1D6IvMC4UdNJ8ZR1TB6JepCV7dL1YmY_tiXvJhL6bWsC-MG_137cwCMYMr89cS0Vrpv5BGKCtEstVrEmSNrzIn-F7lHGnCi1vwyGtd4FYQ5lfVpdlL9DeZRPtxw9sJZ3zoCHA1JrJSwXTD70fTu65Yf5wF1hmX0fY_IS17fZ6HY7J9DFckhYaoVVVjR9RfvG4Z5H9gX2i62QOPjsTRihBBFY41w98DoLkKTMqi50bPPDSDpcYnvpo1-WGFwwpb_ls0hW948KL3yqHRHVcJbViMvTNB7c-k9slNez4EdCqZvLLNMw3QH6wCTgpGRtaSHAH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCWs3A1Y5f6aFg2O0xVZY-0SUHRLl2qJeviFunzI13TZh4R0XnGgXXKje_Ryu5nuQ-WAREZd9JfNKUEajVJPMDDQmG4NcqWf_9-BwaI2Vj-WMuVma6-4ovJnZ-WclbCbclAaNOOU2GWiF9-kIgXse2Sl9FXawdUvvDW3QcUuqSoWWo2ABRyagohnVgIYHXgO7rmklUvh6WhhiCQE6uYC_XHVViqyPDsWrxksFgDUTIpq4Yej2CbAIwfM57WA_VmP-gz-xyiCemuG05yOIbzqOazGEkO1d9E-6P5u7KogxnR_s_Xyih9vc2k-KhrJsws35hplE0JBYyJdspQD9BJAsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U47UtyGFf_YA54G6h3uaOUfpufESoQf7-LetFzCUik7taM868-8YQuBw71OKjQec-B_jwyMfqsB6yvp-hIqTcd5iGpxawpnfEn2XNlgrYV93EZXMZPKVca9jDgIOkxsCIYB67KwiTevFIphaWNDMTshJqp1LNB_9BQVXdxMv51l8Z06BzhRJgTN1ogR93jBXl34YV5Ed278fTZzmmloLmbJwWm0t6CqSHG5JJYaU3_svaeIBrgrDgOnra7HbsYIccJ0l33CaR48XvrpOsQcJf3u6Qkyl3JDuD5vXQSslI0T5EGmJma397_AN0nwST9xhmLPM8HbTJzbcoNOwhg5huA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfrqtzi9IQgkcQVDFx76-v17I-cBANZX2z_v8p7P-WFg4k2cEW1p075f5_UoX2kzqKfcvPd2MrTS-0moNO09RHEkiibB_OBKbiCuU0ew7VUCOKPI4dDYxj5Edl0EbZSIr8jgmxwjARuAHfHEtB4YcyfPuEycAflUj_ShbDF0N_pchv51oRKYS8kQV2amA-kTRrOwZjZWunYHTVY0xYdmKRwy63N_nQDxGHr133uMEqjR2bTDdt8c9V2ynDlYRkclucpXsfxybpXKsHYScwe1BTuvHbesE6ir0qtNLtm8kzlRVy9_Ci7_JDc-Y0F8BCWuu_rY5mwJavgRd177hGGUkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-SRxscv4vgLprQjhbt6_7w_VKs-IypBUJArzKurTfrs_xXO5Wj7iqCcXHgx_1ZwQWzfOzR2bpx1JEfYKdACG1rRpVtOyq4q97u6lTSwY8jkHBel4BRYt-tae9PwP_1HCCKgaYhFkCtWKbaWHjvhrrBZUmeYe1TVVanL-pd_mVcg7wQDvm1PDTZTgNrM7FLOuIFaD-5uu9AdqAl6fuR6fD2P5QhsVdeAa28muLtxh_MTtrNc0bzubc9toqj7zAeT9DAn4x6om7l-OdHPzcIurZxVOJUoshdgMza87WWFS-HOGFstO-AoMjTRGf33MZUTVmOav1tih1YrwkTyLOwGkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMooH0_pjF8cEar97xAQtJYCb8rdO8xLBaSz0OzRLu7Kycee0jJWp0e2BUcKOA7bag4gVgizd9CwyZKeFQ3Gy8JA70JoUDvUODA2fFcs5i9wlMz11S5sXMpGixcX_hgZ-6mvKX-72cX4dfEP18RYQV3QT_PqAGDNmFJ2zzbBIN92yAV-cnGGEmacbv80owXoPAB23bCh0AARMHZFm1rw7YfK8R2ie3dfptMDWE2BF56S4Czn03n973A42WUMUv1OUuqTHGBkWH48fE1SIx50aAv9tpnbS3O09LOKWtgMTGZQ7lAEoBW2gIDxV0F9HA_r1iiK_doDv5U61DNjnG-0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kb4Dme5CEqAiOu_NVFc0CanVDcAIhpM1JGduLTB5140tzfjYSpIpvhuhnCVacp-YFDtihTKlx5EU2NKli_QD4ERJVPaSOKabdVsvTtcuw7J_nrTs5W-Vl3x7azlX5bloiYrWzAIhHRT7qWvV4XaTgX5HpMTW7oUR5PuUGnDdKKqIAbcd6K61oyamk4ag4pPYciDnzjaZxLF12-xVFHczBCm7_mFDY0yv2kO2iBN0FRMfuC_4iQbQiTDog5n0o_53w2bKXpY8mseT43R0gP1KMoGb6O0s5yq3UvKKUP9_QJw6qRB6rIKogjKos3vF32dYywM5fXxkY6kZ_19xOKSijQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ4cvfs8i0kzURS6ulY1GQkO9tnQW9OTGam-RVouFilobK3_4nkwXoNZB4SShFIk8SmZXAPQ0jpStrIUHUJb7OIi9fEDsNxQfy0zRHMr0P5hoM0cWyu8_r7iZsXEIm-UTTIPSIuWp6k3kRC7_kWidHjm2MI9zxGzy-Pd82BY4lkYcywJCKWg2RLOPe1z-nahf1MLdfsAaQOL6Xs9LZhnSe-7WoA6yhpVJm_MLUiiWikUrLM1lz2hprBlqFOr0aN6yO3pvONRE1-DY7yFnfsXvZb749glJs8wtxshMFUWovZnZA8AdB19pO9prax5waQa7Oce3o0ZJZoGRJwEdFrA2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw1LXJzqOSD06IMtU0Xloq2GWMCnT8jlOSQTV2-t_oQdzmtae4C2XF4VYQa8pZZyU0iWmVeRvB4Msr5Qeiwla1iFef4TrQ7mkkmWAAR13DzylQ7ffqElnjOI0PMx9av3PhaWAl8ZhBXU7YhUqwajBZNOh9NagK7XWPNsD4ZOP3-0ME6f4kBKYTYrl_H-GqTKnOd_kX0q2-Z6Hfjvyqb0F_qIzDuI0aNMjiPXX8JDKXZm_muLth-VHc5C7w35q0X8r01Nm0CcmJPTP7WGa831DQ8mTWOIP6OjjFj0ZANQORUjt1iJaquVZcVyTwKYlUajtcxAu_aVqCrAXIRM4RYcvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgT9XKUeV8sfDhLaGQdI9xnea9ytaJOtYcmblPioSqhfruL6vLu12dc54mEGwPd3FoDmJe4biiCwIfaNQXeWqt5V8l5dp0EVN4va4KCwQ8XGlN4pozcPg-yBkxOgoYMuqkoDd8r1YntSYgddyGcAFCMAGLzEPCUvg1TEUwA751Alr8B72RwUuAshobZfhEPIk0jH1OFCfh9Utsn226nFaufFAz9D2_d_gFkXKbGkfRBubhAsvvfDvd9p9PlovCgdjBBSNG2riLGhvR7CFdDUdAf2EPAwroUwi4uXD_T7Hb3o1fP6ugpne9K-GewlxK9vduQz_zrEW7kQmpolX1j62A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl3sB5UNNxH1FjSL7g1djkTYfAJRLZveDJMZ9Spo2zZhyUBVRXguqVU-TDKx2PycDQpWG-PK7ak_EXQAF0rHWkhDCmG1ikc0pr5kbpdO-cYr-9JZ98anYsB_ga2EOrW4WsKOuQQl2d_9sH0O2rcFGd9kh6EIcT3rWTPv_4lAwGGsC8eJFjLcL-2yKqbG1ol7rYCDKjEkPAtVQWB1WlDsLWHPIYExjKA1LyUxLDBkc4bljHqda8vXWQSjtcFj4RUEMBy5fA7lBpd0dxxv3j-7bgwxAC-jQECxG9V6cj6jCrGZq-LVFxJZzeemU8yHXhrqq5TbJElCWNWnQXgPnlpJkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=DXh8Ke2vg5urrETaT2ILDCsThOmIIItsC1ALMhGHogIfSeWGzl87iJ-xxSa_hLICZ2VPeWi5o9GjW-tIUHHI0l_bOrttpOYvGeOksqoBFztAcHLbQ479jiQJ1DTAZWKcBT78KNjx8_Ew9p4o4IHOkEoLHIWGmV9o9kV-tV2q_TlQM39xfQ6j5_eLjpwYgOtFfJYvBnzIYs4aWe0MDpCfgBUHZ-aeof5ghYbTiPnNKD7NjDBxcKOMck8uwFZE4FuQHo_8TFsc12YbHs2bMALMOGkaGOAduhQCPTpOrjmwbqJSeyhUEIQ_8vKJYrUCEIWQUlVbBr098aOHIlrGU9hAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=DXh8Ke2vg5urrETaT2ILDCsThOmIIItsC1ALMhGHogIfSeWGzl87iJ-xxSa_hLICZ2VPeWi5o9GjW-tIUHHI0l_bOrttpOYvGeOksqoBFztAcHLbQ479jiQJ1DTAZWKcBT78KNjx8_Ew9p4o4IHOkEoLHIWGmV9o9kV-tV2q_TlQM39xfQ6j5_eLjpwYgOtFfJYvBnzIYs4aWe0MDpCfgBUHZ-aeof5ghYbTiPnNKD7NjDBxcKOMck8uwFZE4FuQHo_8TFsc12YbHs2bMALMOGkaGOAduhQCPTpOrjmwbqJSeyhUEIQ_8vKJYrUCEIWQUlVbBr098aOHIlrGU9hAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgv6DrQMmz7A7moyl_UT5NN9-O88p5G5Lsq-WgUorpnk8_EchSWfBezx0aLlm6dGiJro1BgzYBGj0GkRx17A0V7QifeiRwdhYmXItw_8mO04AIlvlRbWGNHcGfq1K5tnhwj1K9iBBZy5KV1ZAc9EgTg6f0NoKINKY1amzLmGfdjuDbx4XAKfTkgMwUOlZwjRozGC6i4g9KGDkJMzy8s1846xv7E2Z085Lj2tAwd8jsn-w3cPzK9mSKtTkl4k3esCUdziQaEtoPZWeeZQok6UWX2E3WndhJ_U_XkHhCDvvdmsQUnnMS-VySk5-_RrFPV_hz59epcxFHBAwraI2M4H5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBe-HuJkMweNeBe3uBI6Jr_LhYAmSDd3__VuveBiwuhK0idZmjC0myN1Yem9_bx8rqHySmlp1FIbG2XlUITZysFlucZ8MJO1uq-PGL3HQAV9SyffgbhD1IFLjFfiQQAMdksZtMdu2EtatmQ6FV_XPkWNToX9zEzLZhM9Ugya4b11wfwr4hBEc_4yVA8-rrVm8RhHyw7DB7VTmvQLXLy_Qq8utH5Qj_M5MUFkkQ4PvVQ1SnvasGcUAxhWCl43wP2MnY15C-6Pnb0QaBcyb8wgEzd7LEDkaBd24JdoSw3e9r3GDWzdQariJAz4Z9BArrznz0G2D5NbDKoiP_aqiaxDcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXPMDokLoomgsRAXM3Qsu4QuMJ3zczqW-bMmjj6bSSiw7WMoU-s797yp2I1I5ka2t9PZbTiKdZVEl0lCclUrsM3uo5lX_l4D7uK418129d-cR1UMsOvskeEVdDCvP2XlSTuDuI1MWrdfvqFyXFcq0V74-NstvO0RAxwQyoEQ1EN6raE7wvZ4yH7R75QEh5-OAC-7QIOlqZXhJde1wrFDJoQN2Dn8Yethhrz4oYMKMyuJFNfYOukhc-j7aw3YtRVoD-Fku3blB4W6HprAvWUeoi7C745cbNHb5JGcsSla7hgXP1y-ps0sPL_2mSLM_LIebzjSVd1Jl1v_eOBSkpEw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFvSNSt8fXUzxBDr96RyewPfI8qS8A23XJy3hRTd2Kn1Xbzcj2Oq0rbWkewdbuZLeb8eCTEJBzGnTYQWQBEQx8ktxwf7C_-rd2kgPN1C3C171m07bO3AyBTge4q6aKJOX1fGOksYYMrkbmJC5Smx8DfO6zXV0hSeBJFGYZz_LspIiRfQoSUG1RjcIb6VfYJAVv_gIMhRaXtedHLYWgKjb6WOlQogLhTRGxMKFnfPgK67ozxeYcwx4ttqMtL89Fq6BbYxQyxZQVDRgE1wsF4v0fYc9aDESVL9G4RChCNPvp8mEmSHBpH7s2VGB7diHbKnAow2cDSmxSizKKYx6QpRng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7S4wTyGhwFSav0ITW_FJJa7O9bdzLvay7VszFy4aXvAqrL6Sd5NmH-H-letTLRVbf0nJpQlurunio0dxKROs4E-visytUXY_UFy1DEWcZkDiR6-zEdAOcB8ZSUL_PHFJlhGhtgwcxFUTgnC5UiYSv7fkOJMnr2HDaindbYuUIL2JWMrny2I1sHZsoRX8KbYmWAcZwjNDr8kEbZkLYv4lpGZXFOtjF_a9ro9wl7Pd_eOVJylPwkJxhz3wUszddIrejWCjOsWTHcuykOCJhD14t9bdcgRlBz_MZcRMgOfLXEKfgRE5ByhZrxxrkwZG4Uh97bVazPEDuROxt7D6k9dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McSr2cN15c_fncYhlorikLKG_JlfA0J-79IU0Gm0LxcMTlSzybIfK0xwW5GQ2EOVHR6gv3H3uVWn9qm6P55a2rsQW1_wlDtPWISFClR7F0L5CESQKW-6bHh18TeCpfI65S4GgzpnCltwMrBVH37bTr4kb0yMWoOQ71qKXATIlIXdWz4aXr3yl4aIAl9pOWfYQC0xgsvurC7HiPQvDeIXq7-nbc4jiwsPxb2_SS_bkta8yPllEghGOj9RwnttMjpavJ1Bv3C5xL0GRCt4F4sbvz7l1lUSq26cOr0Sz3Rx3dr23dEp86Fxv4qNYOhWDJ6ha5HUXwz782KVcOybl6wswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ug1rJl8yED5SsQdJ9ZoUcR5XPMoTcw7I0_8sJJTyG_LN24dHEKdZpbqdAYogoGY58Sq_iEm8Pgpju6EZX7kvX-AKKm1WN0HLqmalTdATf8q8JkyYySxBN--j6E3jB8rCqNTLQkEpI4zFILjD9WJ4vDms-qMR5STC-ggV2pCMLnq0oD-2-48zcwwsDPMEUEy_y8JGo_onO8pTy0ZxaVrgvBoVif31r04bYQayZC7mZyb6L_CNPl8esNyGJkDs3i69Dcf4Ewm_Iwbk-FUNUhT-He9Mk5fjaScPyoclyGPcp4rKZrqcUM2G6kD25lgxjlNcVZuY6kWUwGn4m36o1At-kA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=JoOxsYcvFft4lUXATmpjPzM8VqHmEbb97bgqMlsI6MKiqvqSCqmkAeJeCLXjuKRuuAT36iY0HBiWgw8cnR_gMDI9GPHyrckdmIhya5al0XIb4E9HPkQ4hkxG3eWJPp0aixmXltzDTBmG_p1l9ARS8Mveh8JG4cvtC5kqDKfE3OenZhBH9c8xFX5ZHRjTBz023omd7cQ0s0S62D5DSkjDslSFymRdKYqcvGFOlCaKI_o-eIhQnaYN7J_7l_bxGvR0A8umjgnc8kotQI5RAn3yBS4nwhwH_ki3eM7XkwGCqZu2d2eoEbXMmGjBTEjgQ2-iAPlfI9y4Qe0CWHelXxDacZ2BE7eRyRQm09WtJzjmgKv5_MCHy3gu23IWEmhHqy5ESXKfliYsl4QGAL0ZNAnPOYH0a8YPNMM5k6rWueLl3Dw7-sTVmFGhMsTCb7ZKXCVOj5WqAbAum55SNaOsL_PohNxMRCm285SKK10U4pYILy3y7Xy7Ql7y0kGWrKShR-daHZWL32N6VWvm9Pw2sKhJLHsOvB0mQMyRJNRIujK_k5Qlxkkeo1RmmmYPsnRAExW5tlIu2C-6GsxmmxcjeAVKes9IW6S5mT2O_-Fu4n03K0IezMPXhOPsDQNsYJta7lhBVq993Fg9u7u9LBTT86zIuJvOxrlZ5dfky-EdCtLBbUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=JoOxsYcvFft4lUXATmpjPzM8VqHmEbb97bgqMlsI6MKiqvqSCqmkAeJeCLXjuKRuuAT36iY0HBiWgw8cnR_gMDI9GPHyrckdmIhya5al0XIb4E9HPkQ4hkxG3eWJPp0aixmXltzDTBmG_p1l9ARS8Mveh8JG4cvtC5kqDKfE3OenZhBH9c8xFX5ZHRjTBz023omd7cQ0s0S62D5DSkjDslSFymRdKYqcvGFOlCaKI_o-eIhQnaYN7J_7l_bxGvR0A8umjgnc8kotQI5RAn3yBS4nwhwH_ki3eM7XkwGCqZu2d2eoEbXMmGjBTEjgQ2-iAPlfI9y4Qe0CWHelXxDacZ2BE7eRyRQm09WtJzjmgKv5_MCHy3gu23IWEmhHqy5ESXKfliYsl4QGAL0ZNAnPOYH0a8YPNMM5k6rWueLl3Dw7-sTVmFGhMsTCb7ZKXCVOj5WqAbAum55SNaOsL_PohNxMRCm285SKK10U4pYILy3y7Xy7Ql7y0kGWrKShR-daHZWL32N6VWvm9Pw2sKhJLHsOvB0mQMyRJNRIujK_k5Qlxkkeo1RmmmYPsnRAExW5tlIu2C-6GsxmmxcjeAVKes9IW6S5mT2O_-Fu4n03K0IezMPXhOPsDQNsYJta7lhBVq993Fg9u7u9LBTT86zIuJvOxrlZ5dfky-EdCtLBbUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-sRbdLEUfv4A3VgcQmFHtR8JtLGPaq5-xZy0TPMyyq9JNp90JTctBMKpYK5lvbmGD7-gSCJQs1L1KgokcURAuIJivacitXDwMGlFJCqr9Qd1LNf52YSBRQJAENJKqau-ySclF1YxVtFZiaVietCSTw1WcABCbb3CF3ZHeRJjuqscDBfaSGay47Tujblze8Vn_YZIYgHyKeoNqUUJXFqqFeYGDqWUzUVSZH7VecT-A4T2w9qxX6SaBZEL1Eb7VMAENvadrNwHhSFWxZtCeeGIR3e-iOQefSwvzYq4qGzaCGrOZZ-JjVjPvWnJcXDQUy6dTXEYEVPNagstfQ6stRMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejdtbi8pDvVrbidDFTlGC--ehq1sCvVqZqcDGJ9BoZc8Xwvx-43rKlb9ByVAUWzjDHgOF1npswu4upo3027ojBgX54qawEjV3sI5kXmnKGB19I-xD6xWZ6xldQ8xbO8WRPhq0irFIq8RpvI0pcZqANHfZlB-iNsNbU0l_bWodmjFX4UN5IjkgGR7u0WEHMCCasgEJMfzhJuG9rIWSEjC5nqDzPPv9tonr7CBqgUZNIEwQCew_eoZaH9ZUorjgXP1vjXbkoFuYdegCaZ-Keg2GEOyiF4UKlMMZVHz5faVKjf2d6tVDbaGU2oVqji007fWZlLCXB0f68Opb9TFK4uJew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOO_u-AhdM_9mlH-Sy_BHKLGkvxfYM6mqkT3mdbSaAULcCmoVaO8VqOU59ZU8MPHHze85zzMD6d7G1z9cfoCCVaIP48FBH4IPCSotxYGYb-KqWjKuJFYt5-hQBjC4odjirDzaO16YmujQLf1XVpzDM9IZnm7GmAGsTq-UlWAVTjaDyae2OwGgEh2sTcNKFUvBByWqnV620wBSxdgHWc-1NvNC4eAmq2Z0csuEcbmjfyHpr0NPboAPicmauwqMun6mV2NhWB4xhAH_l3nQrmYyqaaLNYXcisO3J0cBEPTH-vz00EhRv2wjRxb1PQhIBadukVopCTtRaaDH-EPOFydkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mq-IIplzda_CpEfK-lRwXOh4cLSE1hU6SZZBh8oX3j6SzI-TsvhvpJYLF9wQUzOd2hFQJubgEWWsj5kt2zYvYguJjRf26ugae1KJ8WRbkWKklJVrM5OUTWIE85plcSMAKic9k0wFaoEt-PA918U5mDoYmCebm29qjUzo47Fh850oHCK-DkTJx1u_vLncvzY7uBLM1iCX3wAoyE4gKDpRaZ43rvehOgnfAIYbMbFVho1TXgqvP_05fFvDbGgD0AAEe-DwmISZ8x-DPFxEOcVTK6U_caBq5cZof5uEwHOm5207AscMDVWxnK1frRA3C9rKnIL8XFZQcXXXfXyaYWvDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA2snuO_HqFOHEoiurDD7OchnpgnbRLCVaSzAqNxQQATOsL-O9PSXh36lY3pAIzwam6c-QRavKUuFF31zXptSRtTw8gpk2qMLT0FXwkHS_kPk5DBphD1eagtxrOmJhEyra3iMy6kcILtFLMz2VnqgtlcBWNeCnOHm9Foj4u_55mfFWNq8MSFm9t6fr3RdG6ZeMN5XZmopBHKdn_52zNjHReztzcSmo6ytIv70k1L44GA_n1uLyoP96j7BEKf8hsS88kCc0Y3vpkrszRkgJGPwJJcCuV1gK6KCRfD8HBb_RfGVRdkPvDxa3LD-ZtppqgSXjeNAYXNKW4uBPAf6aQINQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m0kIQf-WbjZS8OXQht3mC5cAtEkTemyxYAZJj4-1ch-vwcY442hrT58TmOocskjU9itQIEjTmPGxSOMQjvbky69WAyDfvBKYebVS0VpQG7mG5ieGVSkHvG8Cw_VroTfir99OjuTYwSvz58p8zJxQQLK_pTaSxMcEZ2xmCKl48FQi78qW7_9FmJ2G0Ia_aO2kY-po5Gn1jZkkMmbP8FN_dlsM5G2fmniRWCX1LtVWD-pFACGRcOd8dgAIqJtnetce_kc8HBbgbsnJtWNj2iMD-Jf8hvHDjfwB1Kl0ja2frrjoZQvVyy687CU5NZGSG06vZy-rVN4LxnEAMjl01DpB_6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m0kIQf-WbjZS8OXQht3mC5cAtEkTemyxYAZJj4-1ch-vwcY442hrT58TmOocskjU9itQIEjTmPGxSOMQjvbky69WAyDfvBKYebVS0VpQG7mG5ieGVSkHvG8Cw_VroTfir99OjuTYwSvz58p8zJxQQLK_pTaSxMcEZ2xmCKl48FQi78qW7_9FmJ2G0Ia_aO2kY-po5Gn1jZkkMmbP8FN_dlsM5G2fmniRWCX1LtVWD-pFACGRcOd8dgAIqJtnetce_kc8HBbgbsnJtWNj2iMD-Jf8hvHDjfwB1Kl0ja2frrjoZQvVyy687CU5NZGSG06vZy-rVN4LxnEAMjl01DpB_6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQJiOmW5hgFnP1Tf9REXOWg38U-8jqQXzneSZO3bhGY209wI75OA-F2OT_K35yw0xGA1ff6OR8zrnkNE9u6N_ptanv45qIkio-0iS3RemZ5gS1IvM-xt6zWalFrfI_i03E6M9gAB55nr8_x3ImDSeK95rIsAE4YPMj0VyzDHWrAI5gnMVwlh_z6F4HHEldgdP9AQwfFw6e8ydKi1se0foFHSJ5dVKbyeFW5EKZPNSQbXcDxpo4AZhuWqCPO93N8y4JLpSpZsJUyCAP36UAl55It6IcAlxBaPaOGT6bwnL9hOgRiVykEWHbF63B8j9voEQN__hYAeZBcPFJrLMr6SiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJJM8sKRy7BAaRS3a_FMu4esCrgc0FTvqe1OqG9djTELlfttDcSM77Fq8a-ET-wPkeu8GgETQtwczsqw6GLvaOO1b_Fyd008p0rptk-BPhkE6bqHymwVwP-9N2Ev_XAbOC8538Ku65g1YmVAE-YnQi7PF2x9egQak5R1XAj4Aru-vtZWRuInz-09H1gE7s3pvrlSiZM-dx3L5uAjsHOA8DxHGcVqUSSJVH7JzqAOC3cWoKjC7gJWhm8xwwYRcTk_MEptrVb19nrhE3jeehFIim_szE87GUbhWqNSvK-ndwWvJiWIKgoY7dVkN8Is7cYFncLg_TWDSJY5haahsiKI0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyWGiarlUgvdPPJ5KLwNKRsQInqgyimswTipXH5WMruyhkKXAWOskmEDVHWpSHtqM2E39r1kLCE0mMirHjMa3uJpYkQyD9MI73ZHRWwBAC7FuNu9Qq8hRqpxg_X3XWzc30_RYJrtIxTx30NFakDUScS2tS-d6b2mA53jaEQy4ke5_h03YDrDl0yYsNA6Chi8XxyruWtTZoLwpYLH1VW_8urrAGDce3bIR4PQKzSeYGKODCKyzoa7-xFhoS23C_ns1r9XA0buA_6OyZ_tL5rmn9rbmqBFUEqbgtCLTia544O4sXMn50cjCe3ITRGXW3Tn2zlbWqmbnFIIFjowBilBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeK2CL_I88-RWf4k4DohWe-6O8A5AFlp2fjjbNxkusiHkrZnYXlVWbxyvMTm_jLB6ReWkizhSd2qb1FFc3750p6NWhuIrGMljpHy10XGZzZV-FqIqd9XICwa2rwLyA4Y-FGUm6Wwkf7hNl0kqiHjL0s9-S1zGKaYR0nuGAnOsAapD4O7oCLL0FZXjrZxrEILVcczYyNZwP8-ygC7Myn_IrC36WFcZ7DFLq1iaqupwhD2eopuyqjN51f4yGSW37ivdNEIQrENyDLq16vEd3p40rf24iju5_nD5jiIJbOUZzcDQP8S0-jWBCtuRroSQF5y_banWNwUwYG8_82nID0YMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxBor1AktLHPkyDiWMY2oby-x0WSCirfFZki_oADhcQcLoV5WPVeUKj-dMOhJBUQYhKW_ORrUAkBikiMI5QMYMEIGTZh9H1-XpFydKVgGnUhzumXyX3h-S0R6dGACjxzp3BSBZQJE5P52XYsG4BGWxKQUuRzIjDbmCQg3zMdyS_YONu3WPsTo5ZIL8QQZf0M5dqKl9E5TfhSmPpKXQ4ZJ_RpV34ORA_cX5XH7TsiPSzmiRfVMAM5onZYRmE0F_EzQBYvOO7GRoYs8xHh0xqAZ0s21qowCliXAFO1S-gmvg9YuVeiV1_u_TyzlNZKgnfy5j3oa_vsvq7eFAtSz40UKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUIUwongeisT92tBn4b8X8sRFZOEYV6GNk0wcfnUiURBhWCVffpCBsVJnKyPOmXT_j8CGGeXKZHvVMsxgERiyQtjDzAPi_5B6RNbjtMrmS9yAHLd4x-4vd5TPp0px159vYu4yK7QWpur0--Pfw-3RzzbAoTNl1Ht_ItwWCvL07Hl_bgrur5J9mpSnOfJJrsKFM2zV6nR7iUWGhFnezzQhlLXnWV2rw1f4QhVayYfaTJteNhAsmd6WLEslheUslclKrLHONKlgFcTaHW2MRxRqNiSJtCkP2JnsdcmK4bK5jX7Gf-ZalAvaqiTYgSaMVIcaBdeRPYvbGU7j5sww-1MTQ.jpg" alt="photo" loading="lazy"/></div>
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
