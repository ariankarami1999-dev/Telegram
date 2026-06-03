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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
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
<div class="tg-footer">👁️ 152 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 444 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 587 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1h-LL1R2dxLgZ7YaDla0DAaFeC2D3LuVPtwt7ZWug1UKr-d7wTDuFtdW6Tz04vhmM43epWBNUf6bvMaFYIvp8kmp6fFxofqQnyEWlSvDruHpjI1ZBireK2XcyRePCTVIBAJYCzb-ks2TMZuVZrLcvncoCbVnKAXxmWqVM3fl0aUzql6qiveuh3aDzXL0_3GWKyULr0G25At8MHUWjbqeD159eCyf8PNtMaoDpIpZ8a_hsfhvkYXRDos3Z08b_MH6YUY6z08TxS9vgbRPQkkk8PZN86KDa8QMqT4WJnq5bsGbmcTOTTdizLzuqbhmIqt0jwl7R-GOdyFPnX5WipMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axEO6d_R280I1cAFfz-HsDQCZaIBR2gGKoEXkAlBoXTV1t-alpkjtaHkxH15PhcUZl1qbRNX-I2VsByzss8wD3TziR0kR5TYpfmyQijgTfDB0bO_Y2assgMTQjNcxMSPyQubTld4jdnfPBY7lWfFpg0RXdtbQmYoOheWTgwrqe931rA22GF7Ey-nGJaJTZavKxaA10vhu1kC402Jq27G65qOVg6JsXFIBsdvvHveNG0nyVs3bH3lB1Y1cP9q2pexn465MP0Xq7RcMcFaBKENv1pkMrxxfZT7_NvbKlcpgYnGgkNWk3kyDQxk8Foim5MM-YddmDqJmc5RUhZ-TaoOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEUEDfazZ0W4EH6SglRzCDmy1HmOKf1xS8bdoEdmD5lvx89_OmzHayJCntX4p4C_aPp3VuY0O6EDB4NyIIWxV3vqpm3RYQ82YaFjo2R8WSrsgxwY_as38cSu43tJpVDTpOlQQd2aKljKiI5fU44215lUdSSbznq3SBVolKbly2Ak8Ta_ZS5Ri8f3R3ArS8WjcUGkpQi4grc5OqUG_GVKfL69x-5QCtHp61DCeOLeOOlKmXo9a7QPt6KT9dmH2Op96oO7_faK457tAsmMbZxt8xHDMaPYJX2konMP3MWFSsjJXoVyRiN6NkMJEnD_anbhsliLjapNkLrkyWLyrGvSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdGrtl1kdOp8jvHEtQs1jrz1vF3-1nBG76yWEjddRP9xQvaVmH17dvFvZ4HQwpV5-AwMXLaIViJwAor_cHK5F5hkMzG-0PtgFEZ2Szwmh9tWHb-MTflTIq88SHd_mvE6bG3DpBHEsqNuzeZN-YJL4s9P9iDTLqNFCLmUwcFcs4YvDnxuvA8cj206Vl3vJ4HNQ6mTRGUqZ-wo8YdOxQlOpQg7DF8oHgvmW8AtC_Zz_GCqYbjrLL2vWSRTnj7OPWKDPoIfNIqAkRQTtNd-bPVMhuiQqt6ZOnbIMrBlxFc_jfMpjHydTlELYUVcT2YXb5RkN2VCZTVcbODSgTSNDtz-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 827 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbg5s4j77ELOTP6_NeoQg8g8tLe0f-mTfGKnRvHboB5heNGmHO3WFpcAo_CEOPGCWsOVwaTTjuRAYC1MNSKgrQdDwiEmJ3rktk7h-lJic3pThZxulhNkYQh0rA4YDE_auUG9UGKFNkaKO6Iza_PYbZpT8H38dT7pO_i8KNcyE44gYEaO1lpuF4fZYqXSSx7l2GxYz8rZbqgGnx8q3IMFZPCg3LHtAXGzaYiVJTE1PvroC29u5ZMlnehY3SGJqydAF78xChW3ebO4qAOt6LhDtqbNi81FtAtdiBLdV9X7j9B9kzwtCmrMCOx20MxPp_QX2Jpo4U3hS5d0adviLSXa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STnLmOzBBBwZVMje6yjaImsUg1tYlK3y6UymYNIcdgel-1QT-eszi3uRW22wbVF3QB0_13Fv6kyaLYQ0B6bPWecUxgiFJEpz9-B3OL5rJY7lP0t5STeWBWs6appM0whYbYU12NxcoIDY8FNU4sN7g51-xOXLQfimL17rISA041jgELLDpsPEgr-B5cIOkV9h1nVqLc1QVUSyuYOPjLabIlQWyrzf1LpjOZ7J6ZI6cRZf3vSKlBacLcWs48X61zVNMooqxtOuntPIoqwgcBlZmeDSZ_eQWw5GKYOQgnQad6YSim30sB3sw1pUUyc1whTqDlkyE7vvzwmUm59dNlBhYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDrF9N4rRCHa4kGM4KiABNjl5R9dNSyo2HRcHY43lYWBTGj8csM3npe7d0pomDP8ByJGiAjso4ENE0M3KnAHIg8k0DsTv3WnWXpfBvntDfZZ3BR2nuxtFl7Bv7XMCbyzYJ7a-_ErAye-7Rl20gjhqRHadrWvwJ0ULyNUS7YBkfPO6RVAp7-yC81Ji4aB-18Wp_OCztuCrSde7cgObd0_SqPrg99ziQgVOjxYDJW0L4eEppO4S9aDeuohWjvvZOMMM9iHHeyyEDaDgaznNw7LhAMZeSXvB-XAvulsNb5ysWo74NzAh7PoB0tz1monreW0fPLt1pUhb0fKgupkemgPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASJnvyWFIHaDfUFAI-vewY9KNRXyOuzDForGRfZNw1zqUarh1TtkswnG0pLzcdfuzcXbiXSX2uSSUdG8pVoWtVjNkzzNTFE7nAZegPoMI2fdOF4IPIz8Db6P-cWcNGxayHrH6sAjtuMaVElniNj4cAPKGhnvTK_G-lgLmpGr94BuWSP7dGuznXQSVE87pFhJ22voSF2NJVbl4H4mIi9AUzR3owrg4Y0xgxw3Fc6aStjnzE1yvuQxfBnRF7GJHnb10uH14vuLKwMBB-_iX42kPwIesvtsVzILYBItpunXa6LXFGlC8yZYOvy8bZCg74ihMylZ8acg1zmXx8xL6iBkgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9L6Em8DQo3ihhujjEqcn10u5zhsbVGynAZeK1HkH37vzx8drLF606q-fsG1NZ8sTIVSufTUJscprWPeImEL80jhQzNnKyP5JRByh-MpIIfo4wf-DtSiW5SH7_6_1DMNBt_0F6NuYJBPZfUjzviM-aRkNcO01HxwVRZIYgwflm6E1Nu4SwpRwY2uM1MxVtt9QXjMyb1vLg-iVmo9H3jbNAzK4yDorWx4oyE2cgLTB8UHLrxc0tzzXbIm1BueydbILoj_YQk1L2O05JuTdHqneNMCoPH6ZPEsyzwNGwb36RHk6BmRvujillYZ4hGPHL689cBz-YKlZGnPnA4jeRNEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1H6N5ZJmfmCsLV-aiBtVkzXH0Wvgkmk1s7L4zo1Em6F17D0YtN8lp5XXKpcM8tZX0fE9kafk4XuNOKJ6RTr3pMYYixQaFPjM83EB_r-EFg4dNqyqVp1zDWY2ALpNL-NttDuvwvRnBVosm_ERfx-4hNPsAYjxew2yuhLClaH3kFhKQVcyxViVKDKdW39etVUj8HRziS5ZuTpSkxMeHUxyXwrwhKlPY1wlmnQHQfxy9kDcQy3JXtKwErwyBc50-x_bsdNKI6Cn7PdYyeDl8IMgbQLpjBOUoUlHdXmSbxeQjt6xll4aKNEVFnO7tmado1Y1mPfKTMby7AtiKwlGR-rCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhjmmilJx5lFInf52b84ohELabWQgnf8puRV5freQBN2D1m7yz8DqOHwV0uwJMWV1CcPbsjKoLqmR6x8ZPoEk95yecOwy8crsqO7EdTpi9R0uxkgERGHM3oCxkbJnAYwagUqW-G65WRYNZgH_S_S6o1ZBuAcsCZdPbSthoG-T4RTwwxS4txleIazvpQjQuo31R9wlXvw1bBRV4YQvWtJzCkX0RsdoR8zYgzTG40ZD4s-BMY5bGzFe_ktR5Gv2xC2562xJv8dvTNasSv-obbGvFDi3x97_if52WZ2uczKkFZsmPvzbNMhHTU6r6I7wqCMM87Surlbk5pYGTWnD7HRxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=iMygT7wMA5VMlydHp8-PCSbRX6lcM9wwyU6oNfHwHPds6bVgfOhT4PxdYz91LOI_WzZck9zbLi0svqqL3hS442eO3ecd1KO6nV9h2OtSoinSmcf42eMrh2mpd8NxKPCLz96y1zKhUPBI1bC0nR3Wj5_4xQkO-2FAjz0RZjI4tpBzxEgC7wV_CpYuUqkZTHvg2qnbjBg_7JWfTaLEILFr2-VXVAezWI9ae3M2VW-op2QlzrVVDeN3M24EZUM7GF6pUw-Yw5ts38eFhqB9Hx3rQTFWLbGOlq2CEqr6RJPNG1c1qFdtzJDpQJPgeSx9uT5NJsBMn3JxuemtlovtHiK8fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=iMygT7wMA5VMlydHp8-PCSbRX6lcM9wwyU6oNfHwHPds6bVgfOhT4PxdYz91LOI_WzZck9zbLi0svqqL3hS442eO3ecd1KO6nV9h2OtSoinSmcf42eMrh2mpd8NxKPCLz96y1zKhUPBI1bC0nR3Wj5_4xQkO-2FAjz0RZjI4tpBzxEgC7wV_CpYuUqkZTHvg2qnbjBg_7JWfTaLEILFr2-VXVAezWI9ae3M2VW-op2QlzrVVDeN3M24EZUM7GF6pUw-Yw5ts38eFhqB9Hx3rQTFWLbGOlq2CEqr6RJPNG1c1qFdtzJDpQJPgeSx9uT5NJsBMn3JxuemtlovtHiK8fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMJ9LQyIze4uNHWxxRwIBqxFqiyY0GfQ-4VwuQDZHOkBQPP1hJ62iJ7VhQbQvb2AStyRQENhuYjBYNBOXItBR7WQNXR4-Ccaa5nZ5tbNltDqYF7khQu_Q4RzSxhWb6ybb0XIkcAFgp-tP23Ku8h37H-cYv5w_8y0kly-ya_Q0ZJbljeYPuggQX_TlvIAjfmFALK_bV1KIcrvmzVN325DyP5hnKmvxsX9T9PdcQ2pfvYRM2Cgr2EH-ICb8SY-sjxfFoC49dm1JuKW24GwHoBTwLzltlHJliHgRI1WYPQye5XPJTB4L94XTihlCWEQLZK-V4OuBxPBcwYvPlJmyDQCsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXbtCoby-XvcTprGtOsXFgEifToCfiOVgBoaRKM6XzdDaUXoWjuRIhbIEgb1nTvpINLpl6F03a3r7HsRQLf7h-4pPp6QHC_zWQ7kdnZfON569Iwe1PK6EiU-X03NuQ24sYyurmRs4pudvLNq0_-x3iJQftGK2xd3X9YIcBOOOLPrle0MTP_60P3NHqY8bYmBdqiNI0w3STsBnMTSszX87h9dJW8A1wXeqQRn7-HcsauQLY6XX26oPXzdVyIFLgjLTbWPy41eZY06KQLfn9ymth9aSGVWJRK5x1rLfMvDADpY9TxGmOXWq3GXeZx1YkoNjgPZ3gz23-PV9J0ov2Rj9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdkLQQtI6hR6MP7XX0fgKq0P2Dkrr83MrvQ2veJn2FWRuIBbcswLfK77P1UtDkn8Yqzs8KCnZUp41dWomDh5eNjZR6TDsXnqN2cjG6-7ACb-BJdLzxqjcXVqRikOLPfUynZn8G-C514V_Gas7Sl4GAQ5iY36VvbfukcAZJnB9uADVF78uwIggmqGuwso703sVI2_a0BBVwVfoBcEEVD0om0xK20TOw3svBZ1FvWO3DWm5ZFrIqlMaEuoIcozOYqDX9WSvqYRYmOFvjBLdmngw23y4emK-fFuo9K2loh3O_fz4juE6Eo0aWxNtwiID4z_DKl6KF60Uk0vCFLOZiexeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO44V19rDqUXHOxEM5QYseQfcolN_akl9AvoGqOCgJgq8DJ3GOa6PAoYHY0mhStJLcyFhz4JqzfdeNL9fQ2SAOH14CpgKr5hut5GQhlAQSFh5EkMtBHp3ZZO2mM8N29c3k_lNeRouGpoZb1s3eYYjAN6gLPeAbYYggcyhr5Txu0tnZ4xbBdNd8PoxYamGzJH6btRsQMqWnejk2yZf2wrBNJdS1_AsayYncquA5q-8fdrt3GayOoS01YXewxE0oX9AwBTfDbEG8m_T9CmgClUjIx7tQ-FYQd7fe3xAgY0gkswIEPzrE1cgTMHrVeJO7_nSQFf8wk308B5s1lfYgc5BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FllsF5cefoBJCoq97vj_cNmzTYZfAs1Zdi0TkJ7vp4SxPmBLWjk_BxtP8NYcOFJ65enM3JxuHgMGPvUE5040bAxUfU-JkbHSp2nA33nxuaULzYThMc2FulZ9XAQITDgAgbAK5HYIqPtVuNz3Ekb4rLhHMcB3dV56X1ue_GXJcx62eP-XtGqS92Qw4QdGKLD5P0rkt5OiFViyfYv0-DuWEFVQnR272lK1xrKFz7ynZYN9R-12wZBQoYMmF_npPY3JZif9r_0UWARgWwAc2QgM-h8o2Q6KMaBEe_NYFJ4WzLtwhqFIgzD6l40z-uWFt1cNRzDKef58-jN4QTN_2Rku2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rawYaZBYCJWPtPSSV5SmTLkUDfWlC50YxrEmbLIo-FfFAPRaJOGhvz6inJoUmID1azMpYiKtOR2lnemHOlpH3zzX9coreLh_6lkt6HeMt0rKYl6X9aWQHvZSxCCGUwos209FmJ5TzwkR1LWqlVJ-vmPCbCXIOK9WrtEVPjppWr9tyyVs2JeJ1a0JfzP0jzCH96gXFDNMWJ6tbiSAd_mVYyuE9ymkUyCeXVG6zOc__LUK4qvsHhv29qaFdGo9CjWJO9ePP_wo7XxvxGsZNSMsoND38vgfNEvq1GZVHyjT-Fmk53NXe9WjGbKQ78QIkfSFFtr_g10xBv-5tXkzl40AEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTDKrnW94m97smGeYGIBKvpqGOh-R9HztosEkIv3rUFw_7lfGN6jG7touTIdjbNKgdvuh2OsUbZGfCZNF7FaKsEqUoR44-1b5p1w8suu_a4TGbw_GCmmyK1gnbJmFl8z6HB7f1Q_qVyoWvZx-WbzohoOwdb68aYdslg6ZVfDY1azxl7pqosTuRwEvbFY6BJM1Bs4OgxSWQgAlO_yrgDaR1LcfK5lD3aODh8dpKFIm6IXG662iZKS6gnOyVxq98WVjEUMNIp3K0M-Ub53ELFy8CTj9Ct2Yh7SgjnSNDtbG_prbna2Dgm4tZd44ImkF5DBZ3T0bV47M1SMqgf6H9kjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_NRcHSQG6PAjJPr1lgpkepDXvKdOQkpWwLCQuOPENZ2S_guSqcqXrQl0X7z6FObNfLamJrXn5nDjyozCbKCErv_D5dqAmUFdg7VYEVV0n5GtCqkIRuWRiBK4nMlBrVeX2cDfAoxfGL-RbU6wtCGAgaeKZ_YgjNO8c90h-4PQaHZvcE0WaCRCgLGLTBvuockdvE-ADkAZ0VX0iHCxB7ZBsHOhE0q4F8ZsCEfbdZzcVltlYeyPdgqQMIVoftdy5jrY9_4Kq2nI-5kH292H92PqyjZ5QK4YBGSCCqrxb3Hrv1BSIMNAn0jzHbt6R_qsiR1knsvOI1EZmU0GlqSFuw40g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJlXa4QBtTF46k55kUgrKqDJiBE9fhGnmHsbLfEeLhZ1hcR6Gmj_aSLN74_H1Ii17cFlE7BMHHrU3yIXMRqMY5L1LuaeQ2HNY-m6MzW9u1GFaJ7sXd0-hzkQ18_ZV1RTspEkqrZwXGpadho6t4bTA1cWRwZYY-w2GU0jeaY3MdlM6Pdws2hKeZqTPy7VQYfF7GeLI5W7nGjnYmUBnLS0_w1MJadtXoY9RTMpPxHsMH3dZ5EDIrxjhFgh_3H0P-6ioXoSft2DKY9pF1EN0yQz1Y90Gubpr8Oxm1j8H_v7lU8VFAnkfq2nzkdVtlTGsmES_J985aQbm5PUIeESZ0VX4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWFDIieuj5m7qw1Qf7Rso2nq1KW63lCbRmc32GR-LoHuRvpLkVaeYj7XTQpbK0zkpRvlBJ3Rv_srq790HAaiEj3r0BRVj2_dCHju5NSos4K3iw8RHO57dfIRZBkYz8QDSYlptEMvj2pnrN_Yx0UzN7hQIzHYgs0ulPDQU7pNm56DaA8siu1d7R_HG2c9NS1TDPJ2fxxAUk1f9CMIcJv82uN1XAoInwhdh_ZlAUnLgiAEN7jmkDGpp-cAbQMETdfZcG0GHeQcxpyue8X6FW5yyAoRJRd6469qkSuF7xXa8-Ta5ul0IYae6Z5jQ7Y_CSd8WWjIykudHzEuZpj1QBG7aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g90nXZwv7apiPnSF_S9l2DWCoY-jZDxNezEGDvwpoZb3HRZ4WS7YKCTLC4xxZlOUp5hhEpXgnfzi7pGS4SkHxXMa6iJpYee03EtfN6mT2BUgTfFK1vMYWR7Lcq0XTnnCzZtyYFviI5vzoc-CL9q3-C8ofG5rVrp9UTQtDIab_r-Rj3SbrSWni0OCr2cSNO2Fo-joArFwg8nRDeoTvpeU-74164sI8HW80kJ-TDPZpZK8gwNaOnQuSNhTUcySsz1ET_LYJ3mmfEHdWY127RmFUsb0LfYxL5C7f6gF6htJr4W_lgZ5TfiX7112SU_ZDYYepW5wqD0wYSWYQuw2k50ZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY6GUkAHoYpz8M1h7Wa3lCgfN9o9j9_ZVDdnBT4z5OY0NE-WKb4hs6KNHsqIlSVG6OzH2Y8NTVQoB_KH5y5YD2Ax_REu6o7syHXRBSpMSKiEuUsrZwqcDCsNBwn9Y4zNAlsLffqsSUfKzQ0qv4NTz2VVVLITbXq4_HJbhuovQ7-_tXPT8XKCDvSPwGMlARspzSqw5KlvZQ_KZnw_tllTfAukSd_agtgNu7GUvk_dkJAY8EfgfpuRIK2C4RteSFeVvgFgmj01imUMdPZlH6xsP1-Wxz3nrG17FalKu1idvsyRflOYjqyHe4ZDf0mhrqI3vBpNG5fxcyxNfcBa-zdXJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ok3rR27nTU2ron2kDReJ6dejN45DZeONMjfQfdoLt5dv3Y8IiElTkDi2pGzjv99da4gjca2c2AD2LZ1_b7eV4QEALmwuiVkW9EJQtjLx6mM4XaQlMTfwPV43o4Fsr0St5VlqPey0awKMOu0Tlj1EvSdfo5j_EKtXCH4SORvLNw5XuuK5Mi4W5FNGUS_WVpjoV74g-3cki416HHnGnDOZwSIoHX3GXHOlJVMMuaFNj7A92HY5tApo4xJulXP_jAATJhRcbf1NYrqqhsQvlnVwfB5z6_-HZffZ9JQ3l6Rks4SqzZc1uiuHLz3kT2D7ic0wIu96QhxEycEqBq0i8BfV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oASgwjV0Hj1R68EywmEXQMJWOUNh8M52xUcUfTJ8JZ_2qfWG54ogGfREsDVGUc-wuJPJK1Z1aPumiarikgdC2xlMM2PmBiMR6ous0ySVFZTUrASNFADDAUIbSbj5ueubQLE-tJeFHIqaPnpiHBN_bRtKASvCGEGABdDpV72sHvFL3zURBAm9911sYp6fw8dRVw6Zxk9j8oJrK-vD7Ol-Tv18-JzEBXlH4k8RlvzMWTYf--MaIpCHBMaoV7vRoYbutTDKLhe2h3rPs-I2PnGJkVWtfD5kTpxTHHeheWKYUAXIyFX665o-GoS_8NyGfaTitvCerQxa79GsCQXusxycEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjyUVZ3xqmtSuhp2RWdHJLrAatR12PgbmG5iHU9rOUvh6kcl7muL3UxJGHqBSuCMJbMFHj-ayVFU2z58bmxhdAhgWSQHn7piAQQDwphCYSN8fBg6ci_MSTmjyeL3jnt7MmyLeEQMRFxvp4CIwFO96SS9TsxCQGY3xi049xkZ2IabqwJKzABOyLTbMIrhKBqOrJqHtxzHqfEOnXhLwNMjt-hpQtIXSlWeQ_5t8URyPZZmJ1rzedLOFbP4xhpqRZCSoBo-J59zdOTF2Ts_41rvET7mxB64bFmaoIagGaJxCrrpAvUH9kqvrrA2Qqc0erhVMpvGilmMHeN-UaZtJXPgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnOWjDdpFGX7opW9Q_RTsMmDQHc45cSr0wuyUQoRY_vQiQpmvHzHP3NGe4NRMXrJVjgNpMfFqgtxZ8d1rC6SqfGT9m41N4se8hnM1-6gKElX9MFmIt1GcNnjFsjhYffy7pJzsu0cxsEs1-YImkPDb5O44s3vstIKwvWjFu1mWqvn8nfSptZ2Ekkg-FO8arfGP4cmttQVtw7vC4yJnohlIv40eSLiS9O2ba7Sf7jrBM2MsAq2Z1pm4xsZcNTZpeagyQsBOWX8vmifhmW4CICNnQMO79ZrJyAYxGlxhSFwZUmr0_xgNrO__NHvCYmibHyCMsmk3m2NCCiqeVhhNckumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGTU3Bl1zkmXMtl3xH7mKVvjsGGZn5rxZN057kfltbGrpsQRIza-PRk8VOeXLxOrB9QXFqxJPbCHd_48p7AHzzg6Yw3q7BIU_QWA6l1UzhI02er21gXi-kKpFKsqxZx0CfdmWdHkbFsQi-nqOT50pMRaZTuNnhJtN8QE7THcSmZPh17hqVViKPH7_nvglIK_CV6MNIXp7Ogc13QealpOQBSAcCpa53OilpLFTWkzTeUyiu2PCR5hMdFnmzG2cpEEMIygtr86InJ-VRksBRodVwQbOdvStmtO6P9vFSM_45LzVDhJNpOGWpJAyDkmClslbVuPuYmyZ3dogC1pQS7J9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6JimazGj7GAyqJyBEyWIvcHIZFw2wvTitBIX6rCkN9yjZT85qqdKihGMpDuCdchRJEocL4il-9g5aQFNOIwU76ulBYrbHrbzwhP_CChXRFYdVFk9vN0D7_2HIKsOyNKTc17_8EZHdcEqJqKI-Mp3fgP3SAseiM1Y60s2u8Btr1ILI0gPeQezkAxVPjrHMdkPjnR8XmIFs6IKVQmLoCFDpf1qU_3DrTM2sTGXsU3fB5LS-8rj_7CGeOXR3FFHyKUdKqqAi0RDv7up5lEtRCCwNWUA2d0yb4gaQF-mokROf-wn49JUJrBiVQ81hKvhobXVMgRojbnj2rRXN8U-9IQiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB03fknNfXzRFVRVZoKQRZkBP7vqqrHqvervGez6ZYBAClsxqpdAB4zieZXavrdoUU-KfbyMxN1nPcXQK56jZa30hWtCvRrSwOt52u8RBJTLUfhqEpoKLGO2gBk9EfVlX_jFGqpklrofTQquNnAqA0wFgbRZR0X3Jn52V-ytxqUMzuoFNcNf3MLpuMKB-7uMoaPdsWkX4ewtwdIK8jIDuG4JuAtRi9GbjJylKaHvHw8ltGxWcALPtleNOsf_BwbCl5G7cIobo65LELXaue31OBJaMz_HgCeOGyrhmXQyp1Wm8q0fbIKHrSsquYAdDbxe2mpgFSVAWeeidHX852IQLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teHjX-XKTBkru2ppMFZosu1d7WiwaTiMc-2Vvg3BhwwNSjOP8vEjzoayUCKCSFz-RWKViYku_ZH05c_UBr195qFmPjlXciLNhNfxX7M0HgjU9Z5EzI4ClGS-zzoRIolvV1GpgRYumphpKDiuNopPpvNP6BCa8omkWD3pPMf3Y3wRu2X44rAc8giVRawadYAfkDo7tCfQ90f8xneNeQ57nO83x7JiC9CojvrStFdEP00i9nJyBU4AF0c8PzxmVaumnSae4fCKbcohmhHRv3IpzzqgmfU1nLVFSTzjfkaDV0bP8oet4q70WlNaLv7omrcTYPLDGmtvqxBx6YfgIVY9fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skYS8uKjr-Rn3oT5_DU1TWJDoMZ3rBb8vXSP1ySXvjqR7QciVk5sj9MPIyTzifnTr6oq_guELCFN1CilYsJP_4TUVPiY0sEv2MFg5pg42h1-6MgYqaZZb7fBYTAUSH7CPnDGIEB1jRZ5PQkth2zLfInqJ2kTUqZ0EhBwxeK61_CL4NTptyK9Sq5H4It_CCuyhQfBTkHeQ3XmByBVJI72WSwWKwzxC71ysYBr-i4e-yrAQwmkkRwSqh39cQuCxG37Vn5m42w6Yv-C-j_qkuNNbmneWo507NQGqysIw_qa0NBZYXvX9Ou-Nq6MQmb9hqVkTmwHmF_BKx0chbuyUKW2BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLZgsh5d9k-S4-w9TksyaeJpsKx_trKiukoVzTE7_0khXk7ss1lqelKd5iJaT2UkMqcm08Ffg8Fd2sg9lBi7hlkc0GrZPf1NOGx2YNW7WHcNgrKeSP1EPfMDIvvNSB2aA_xRhgbbob4XY9GNIk01WAFxGI7oabYUiOBSL876MrhcXWTNEVqVNbpSxTX1HuLb-dvFCPFZ9mSrhL97NKHZFbDDn5_6LotUDSwiJ3Zq_4kJfP9T8T44wt6KUXLm-7QQFoGNjrcwI4NsZqlBspIi0HOG_MjEkuwKlnkYL6gz430h5uje2acmTOouDw2bmyJnkw4w3-C2FWvIOoPm6lg4eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cszGleut9jlWS9Wy2KlR--Tg2RjjLku59tTgSrewl6dNiIaD78l9jq2J_wXz9HfueC3748GC2KCpyL5Sl28w-02AoCSVsRZEGekS32wQSUoz3_yA_a1kSR5dtKceCfV--p5bLYiScryUNq675Wjt2zduQIQUzwehkIcgF1ZJsGzHom1VezgCnF-9oDHbgA6XjVETi0SAvOIvuEVQO0XTcdtLeELtStuydCpiGX9qDqhH8jUjjlvpB3wLJxs3BXnU3lI91_bjgKTu1pZlzovKvm2pc3NJeTJlmfXkvgTjC3XS160tELehEaHDDAfFeJ9-W3rTKp5bdLkHHIk0ez0S-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6CgkJpkzu3HD04fVvRCDW_pP5tXx5nSC1O6Pwk33W5X8XI3E8EUU2STcuYKUehxnGzb-d_JBfl5jUJNx1v3qpOxSLR9tUC-slkRp6nntuJUUIAQPm72YzCUIt9r_3iOjtW_HzS-rQAQsqJZ5_0OoZvGYKy6rLimiFqM9023p5mFF5kH8SkCtqK-_4IDR6DpiGw2VGy5KOZ_EMUGaxJ8UZwL9f5mEPHAq3BAwCKF-h5ulMLcLPQb-x_qQn4gfSNtWSkfLyhkNw3A6g7u69sL8pppR7043RAwrJpyilvqmjehw1kFdONK21o1wIcUfmVAn0OLhDn4WYTHh8D2W1RYXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUKa-EzVy0KsfJShpjTpzj5ZFO765vmF2r5v9e-nhtLDpMqC5znRxHwYXdDTwZUk3r6mXg9kbEa24x9rd10wlAUnpAIkaXXAQNPgWnRlzTJMmp7gTCCIpyeo4fgJA27ZLc70wcGkyOwR3av9ffQtQqmF1e-vtD268OFtx2IAlLN27wWvegRi9_Z0KEcJMk9mZEUTEiVD5l8WXlvhs-nMWUyVf1KXfNY7zw-PTcnj8fGuwDYNejwyCSxgl9pylzVPn3JbhtqlkWZZd-Va9GdXZ2jQCWQWtpiBAmFi4BPmYF95ZraaMn98xsMx4o47GNoSlpXvxWEbw2NQz2nJIcGKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxpuTUjvLjuYiYcD71cisGeFuLpSnzwyWHYR-rO7mKrAjVqMGjiDfOHZjbacZbtZUnb-B7bZjX5HqhVInoCCxe1IL2e7PJnOhM0s0agNp4H0r0RPM11qQrAMIJu2Z4bslLrosqVe88idKcVCaOPBStbSUQKb5ztJz0hv08GqsUirTSgowxDUQsOvUYlPhRitF4rsh6o0YfWw4uVKONEXvKxrt3Pjq9o0JYJMA5_jtHrG7n-1ghBABdSzG8W4adwtCecgXzyMw49ML0oW8xNAYZV63NXqpFdfKddfcV6rwOtEkpxzsE-P496pzL9l4wcRWHdlgg9WF0mfSBjVKn-0YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_3F2p4pv3CRaVWNDN9ez8aev-_9w9RARx0qhkXffMr5HJKgLwCAhX2rE9Q9eVeNQMl8sZJkZV1v-4-G731rGJaXSw8NFxTURH0u3RH8Vt4C2ljFR_bHwGS9LxTxUgCddMxM37mdOj9qY5_FMBGeDYvRUAkQSJEC_nT1BRbrB3D-9xHcd6klnEcM8BWG9HyK0nHZKwFzyDT8tvvewIxSk_LtAsmi0A2VsGkhQkqvCuu2jkBeEMHCZQU3G1tblLqfo-bfo5_YGS6JfU8agmn3-tvMH90suKQqvEq-jB6DaHP-qkZCokfHANFCLZ3AWOzdN1BC7ws0E8fRLAD72cvRVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDrZe7N0kXv6qXMdBH2eduQgYaLsYZWv4paDRGrKoQjC6elYGAQsdwIjABVbNLkoI9XgqgTGw4QmxeDFPeTQuQKceYKeT2TiiyPJxsoBvDHNQO4cLeyZTN_dcEzLcDIAIRNNX7pHymhzPO_E40OwFOeTc-X-_yCucPhWSZrbi8PtBsV78IpvYA_Mg5W2armvR7bxc-o7I7gt4BrZxr3qf1rfQrjwcmI-UzLMfgHS3FzO0MICxRh_bauO7BbXlTfbjBsp9vnys7HjWTA9yhPIL17Q58z9Nx3hGv9MVlnqE4QaQ9cdtdJSaV6FIJi_Mv8XnSNT57LJG3VGKT7R-RPsPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LElY2_cUZRiFxnWCsKLBCcu0XyfnpjbIKT51OSWHmRzYIjKZeli5kRB66MJT_ue5ZmmNUjvPEfGTB47t1t2XDamUEa1b0CbrauAhr1UBpSIOsDIUvXQAsh_FdnOfHudiAOkAIFrkzIF3tMKDALI4ST-gmWZAnw8oYhtwQUB5WJrXuYtmEkTtizF54yv90URZ7BuVDHQwSXI3W1QTcm9XTElHfhU_riJBs_IoAKM5PzWqosBbwnABknmlFOxS8-J0VdRvtn-s_uCDxIF_T1qWQKRfR5dM8qkPRFgBS-dZBVHKKxEntjCXssNiva2pxprISBSPKR3mFBLQq1NMSNK0eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmTroWJidu8lD7qpD9yq4ZwkBVYrbgb6MPZNe-SZXPhb9gWcugNGn1JYUoziKR_ZXMoTuQDyaGwZKBBbwyKmG_tWN5a5PnCxJir2XfUo76ukqNQu9W5D_NhO_z_BsL1meyEx60S5pp6Y1an0JnTBHC8d5fiW77mtIbvu21ougKfP1kDvkV5Maa4xiahUyALfANXz_KslmEXMbJ-jh48bTPsT8Vf_HwJQHaFWRwu9YbqqXMB5ty8Cq2PZMR857VVgb33om5UfUxmCQFE41VeP3JS2wd0OPW7xJWmNusZCafn5-1Yuwf5hj951iiX0E6trRZNbqYwX_bqpynlMbA0hBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rx3h8U22TnTQfTo2tTBSy4yeP-7M8otiz1NLILHssQI6jZ7PlzT1CehteIbaqVB6_XHfwXsaGCtVfgNjBlCzvHxBKO_VvQdV3K8jSXqoIVrGDDHlUCJFnR0zdFDYlkzg5oSqEtJT3zbJpOOVaD0AVtZIUgEtBJV5d5UDFf6wB_7tVC0mIM1eCwtq4KTHFkYtPJyzNaaNmwhmZnLdhFjxQKnByfqMP1SkXtd49yA79fvrUrBZFBb82hMFfUENu4W4Rg_1a1d4fY0wJTlE5dGgSmc5V7uNbf6dZgOmvGXho3vHQxGPLYEYd--E_GEm2__DfYDNbeP7yhqPfKNZTU1cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tr67JNa1NyMj9J72H0ai4YkREe8vaBTUplqKJM1bGl2iErNQ8oL7Ii1NJMAUCclWWWPhB1fs3FCCW7aoOQNF1ORUI6BR8R3V5PN7wTtYXpbYm4GZ8Zmc3oKl5b2fFua6g83QiaLOx_N_3FPrRNBgJmKBv7MtAF8WoVzXOTUmEln8upmGV3KgnMpKZ3IwjARPREfvzMVz32M9qRbrp0a8ZZcoU87XMSvUg-afiJQIDfEJrVFG6smMt-EV_UOhwzljoQjdISqxBGrRi4ehdR_rguqyJuIKvAoD4L3G3kfTsV5tNONMzHRtdHxElCbtCAalHzIKKrG-xqZNaxSi0C30PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrYVo4ZAvcmwQqGe1EWK7dgluDKcNmZfSnhCVMT5bsFQ3pmp5BnWoO9Z1Nyn7dlIrGwTI-DDKt-QUL-7VEfcI9hfcxOwpSDG3Hj17LZ2WVoL3Dw-yjVK83Bv46mLHdK2nUvxHtOkHsXxG-e6LhPeOWBfvpKwfvGRQJsYSf1s5T3M3VfRzFk3anlYnu2LDXCcmrXcmVWoIBDefwWE-qM9SPtTd8jd6f9Dp17JC0XrudjE4XRPj35-81H_VfCnZEz1pzhQef2coipwiAEm58ZRUmVZv3EyCOtVUeqMY5_WikZWjmXuN1EiPG_AHK_SKWZrJZZfsPILs5OD0KboG5MAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGILjKjACHGb0qhNxaIJq1QifGO0kELVZD_K8mezRXVMTpROq4U8lEFSBYt0XPB2Parrovt4FIRYg1y4u8TAOoPYKNmFn4tARR8PzdU3yAaC7d8irSGjBVB0jptK3Pjsi9iIMJPriqwXKNtPlRFFg7VYVVssXRZG92mLHJdfyhwCqTRQCCqWmjkZTio_DDRiiHVSoNobT4S8bqpjmuU5hZrR7QCcRyqIULp5HauWxNy-ypEZdZk2psTa6YMnGg29H3M-Ka5EhgYrK-lFviwQHzT1ruOPqwm1U0m94GInbx3WD2xgV85tKm9WTz9__PZygspL1IfKDz9x82FVBXRWrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hevNKZsgLF1cdNWg3MBhgAGM0-FHvcvrcoMMuwJ6KgaOswfPCRVVwgdvhNdwzyLBtoI2Vjn34vOl6X_NbWAbF5gbHTZ9SbQSh0WN7ITN_FJL_xMG7J3UystHIXcSy96X8bKpI9z3W3Iz_NzCvAdLupeXd8MUj8TpHS-2HOeGv3rgmfhIkDqGOncK0kXZpkUPsD655xmFv9_pFW6zzDYkTL7cfGvZgCeekK4NOYgWbiYdHayliAtaJKuNkPeNi6sDxnvzTcPbyAFZL8CSKJySzF4eVeFMUDnNDMX62ZqaVHq7CazaVbcD7-xWfxonibiUaefQGnUrCGQ909ff3QYwMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3Suq8GJKhVJ2h6aPB7NrKjutaWrAYtHoZ_8pYeXN7SFTghziO3M4YaFfBuCdWA6iTRD66fLO_AKpBwDtRnY7Y_LNYHYlDYwPTa2VzWQp74sPWuylcTMfeqYy1Y34pPwdZlxa3mZSQPu3CH6LnXCnRmPeXdxR5PP6oF1wxU1RJf6v9WZoHNEf91CvSfxbIHoArvWqkLxPJbsRpTxT5CgR5pXDdOTxoBXciDzmw1qBmXw0XlYphWF4O1qdlk9qaq1mw9foNgMELc0swuVczW_wPDzrvhhgqWBjfRdBz8zCepIw9HSVJqAVpcyrsVQYm7WY6161Uff0Mg_m0VaHW3pew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSMAkpYWM2LcvTvKPlLPrmp0D404qVNh_th6VdzG8oVyUZotdh6IRKQ24dmNgiLqTaWjjQ93JKBFYy8vUK3PmMoYLys5_UB5dHRk0yQ2Y6PAZtltePKjFdcAEzYZxCZF9zKPTbBJpSL4mBMgtGv_gYGYxL8AnPQIu73XJBRkwaWv03khzDwlUxq42kYQ2zto_bY_XwxegdivqHwS4-D4bg8lK-YSg8DrmvF_VnEkoY6W9vZB03RiWhNYw6pVXfrRTS31Oo8c2xP3RdizEndWgp_-nnsvWtAjcBSLycL35npUtur73JQnP2t1_kMok2TbpfKvUnMMR67EbJmWOREwAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REEz_fhVINkuNOp-d40SDXDvO0SRcFNwQAC6YXdN9B5jx3DvMAqCQh4cSZVohk7PwAzYh_ih8OmElxlb-Ui3olcsm5HAxdc6QH0N9vCv90Rw3hXZZwC7HG6vVPzf30ggJ_OmGsDXA_ttj1BzaOg3MdUEDtW35cu2TnNxrVX47U2DoSi7BhdZCmFbudWHFtk9YUQIhE_JcWR7wQ0oZ34OV8fzox0Zp3RK4K86JM2MTgHFwYRiDx1qPBKhK5MPHMX5uTmXukRpc5ICo5vuPQjuNV_rhAu16HT9ywjWYe8YUrGhfjhdfS-fYk6NAO4ZA5q-SVNsjN5OfVI-zUoAVwts1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y27moLDKkLD96o3w2LyLuugOp6j11BOwCcM_kAA4Fk-JRXacmObiIJn4KZLK2oloB8qMAhMs55DqWE1siUArzvVdXv5UDvwoLFVTGF3HNeF5sTECLGsUjuKCS6_MsgbLy2DXbFALZILFQhENJiYMM3dWNf5kCzM-kKekyV0kvW7Gb40ObFriSgQjGK3oN-1fpNw-e9s91VWiZC55gKNo7P4HV6xgxvSXOQCVG6ifgOrowFbHbAPOZjCXeOSVeAAACenXqXOjCWdcMl4zgykr57uwXYaG7WTwwWnBytfG4pGsiC17ROfuj0eSLLrfapfiyEWvTyiAJXKYDpJCEcA0fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObrRAtPwdluJU_gk5-t8rnXdZAUJLPX8dNk0eTQ_KzH77Dp34ASkzy6stOOG0ZlQHAEUXER6lwxmfkMzAxuGrUjWflPKzQAhn7rReYP8K_1OiPfEn3HimO_ZnhcTptTDPC8TMeLF_TjDHEWYCyoeBERbsTrH7Pe5QPPUuUXJdxnyhaFpdMfyAcTS_pntvYxmGV_8rjiSRRasIEyj6zbUimGaj6nt256CKlSkUQIFLv7GDNUtEZtrBsQPFUqvkgc5TbDZVdtH2qwxS3HZ8TKKdox40KQzuVcH1Pl5ZralofEBw29ZIhklNVETNKOlRixcZn5e61-IC70nxAH1ceWy_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goj6Cyc1NLLcbi05rot_nRth-7fq7Bflblpp-gYcqYP_sei0a2ngQGBofoh7cLdFGlTIcMrmo4c7WXHUGrn5umMlIISmKOyjgJJibzqUJXesWUH7vQEDb55mx9uKRHvG1vxftHRpfXmsWF5nys07PJrNzSh84yiRY7lKelicrEOeUV06hWAEI-s1dsJTdcd2QfJUiYosFJwpJRnooGpIRlTBd5WGOd84t8MCkxZ840SzrHppOSG9E3YgSKGHr6MH3x43EgSgNEPThuZuLv-82qqZggAlxbA6CQSa7zoYw7QVUfTobafeExBMAWK47ix3dLVb0EoHq-16ZCBCxFfk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg-XyO6W1Fw28UJETXvEk4wuAXmSoLXKG89owE3re61VocRL8uo0of38A8RlqWfekfNjSuOjv3c8d0LvqQbg4bQRCr-bMM3FRYdLLQYqPGsT3n3XOz1oSjkxIazccqYL9aDHg6dBcgFmWeGZ6XkethK7CGiKF4vzSjCLFoipZP1pGDjxeNf9Y9uv5U1E8XEptjuouGqEWXgp1J2pfAMzyIPm0RKavpsLHFH1dPoC-xJiSfW6KrYSj9QLZoOBAA9TFELuYg8-ESobP3mGUF-F3ZMplBsD9NXLTy5hPxXEwIqfVB81NImXZrYf1FbngRGYAQW_wQDO0fpjkD4RSQvegA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt_Z6iUGHR-gdVagG7ez16osvKQebvJMGs7z7poldXvBbcBXcmLHW0Ba6atvwZb9BkvFFzJrzoeAZtLiISpq9RO4o-RMrL4AJ96pUFlLvxwODQd2N506DHa9-7WAkT6LcaBiE0KoOIsh0ucOOVJj3AkVptCJuz4POvjkKzmb_kamAxsY5av4Hv0rDPm8RPLVpDm_J3WqYiNTQCa5cdRG9sk3FkeTv6Osmd0ZYkHe5tUxrTmGUZLuv0BMZ-eafcmw9BTJL8fRl9lS_EpwWjQ_gwuC1EQVnP06j1kyCHGIDvERQiT3GdMdwHY1NtaceAPcPx2qxRPlpqnDxps2YpF0tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqXvNLdACJrOZaxG7G9JOXGjUCPN77CT232YHGs1f_D0fVGSgRUPT0qMl91gq_PM7zXMO7zncfvrkii9MKPYSW-Dsbz3AESdfSqXlt5zcFVXcd5nghOl27rfuXTFECn-_fc8rzJDEY70pTQoz_c-T3hHkL9LEzBtUrcl9nZBIoxLuoCEMt49y3_gqB4G9zopRycSCT0bLp05uCE5hjHrBHZbRV-sf8TcOjHK3lLlkrD9T7235Kt2zHps2buKGk5pPRoVzfSrAg1FRAJ0u5a5oosjKgNPi8xk8vSHmJPI3ETfstTOI2esbrKCXf4rBidEV257Mj5kjeuBJpChVPoJxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZFGgNzDbtlArxRMlBaF1AleF7hw1400N6GKQ4tkQeKG8s9cI58bCQ-W9nhtoUZy5MoaIcT62-tWCS9ejyJ1khlZoJL1EujisNmVi5pK1j1kTXdj87bpTigPY3VdNMFF3JcXtApHrXLw9BgcX4Eji8Z67a1rk9XZRZUuo5TvYs-HUcFH_8iWbdU0YHFUQAUBb944kFk5EeQTRRNBA6MhDqtFwaJZOuqj0c2kG0y37AEcH2GpT5VZo1wNtCrf1NWs62Y_pVr1awj6K-0gZowNyymOGoW7K435tIwd2eMlUEPDzHJzrUkw-yiEJyt2yC821956DzkNJApgtMA2xKLDgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUTR1z872cFtYcO1B6mm2BMACg93kPAI7U__QHQoQjgjC_UkllEiKOUK1pp-yQnkLGo5gaj0ITJj_NNU8HLffr2lVw6Ne7bJIMFn7bn56gZHcDE2UA-OKbCaH6YlOhxoGx62U7mI3A-VYiVs8An4EnxdkaL9lkaSjo_Awgg8z-3JKMdiP2-n3JzS62veWGzKrC9FBlUEiyNfPeanro7mW-NyYusxHQrldrerykW5FKmNoz1gN6k2vUM7i6aglmEateYOHDhOzagoaQUKsf-QJl96pzxx14ajtFgXpVZiWg6MHLeSOzc8jCMDuTLQG2Nnlgmp9-75n-JtXbSDmUXOvQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=t9rpXgKfQVblsSxN0IMd3B2E46WTI-E-kQrFX4d5jwUZiFpa_4n4ns1QuqJgcoqRixnhRkc6dHBXtH6b_RUNMiEy7aO2M3NJrxqjScL0KYQ18fLenfTaGpk30aGociYGpKZvZp9dEePrvQDv2BvrVzbSX7nydtwvfZTnCu7g_HI7F87DukUz4h4yutIW6BI5R5st0ah9PK8md71fMzHOSr8y7M0JPnBT_xLj3DwB8okEerrQoGyJ22m1HG8E4lVMiO0P95YgJnxNOoIQx07ERFDwoy-mKS2vvOo33MXelU82nowndVR0V2o-2uLxCC2aG6U2EZXqjIEDBqdwRLI5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=t9rpXgKfQVblsSxN0IMd3B2E46WTI-E-kQrFX4d5jwUZiFpa_4n4ns1QuqJgcoqRixnhRkc6dHBXtH6b_RUNMiEy7aO2M3NJrxqjScL0KYQ18fLenfTaGpk30aGociYGpKZvZp9dEePrvQDv2BvrVzbSX7nydtwvfZTnCu7g_HI7F87DukUz4h4yutIW6BI5R5st0ah9PK8md71fMzHOSr8y7M0JPnBT_xLj3DwB8okEerrQoGyJ22m1HG8E4lVMiO0P95YgJnxNOoIQx07ERFDwoy-mKS2vvOo33MXelU82nowndVR0V2o-2uLxCC2aG6U2EZXqjIEDBqdwRLI5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHQSzbQaY1FKzYzUgsBU-gtQK8WTDFWGRt_EHShdsFrp3gssPTphrKZ0qlhbnb075DIT7CHFoAb13SUnDkrzYUt3nJeotT1hXXXXiv_AmOnkURqd1DbMhCReCqZOppboTTpUpjSuamgOEw_0lWMfdi7pOySUvmkblmcShPLq9u6qI5yFOF7imxTjRQONtgQpQnK6TVxciG6-9ugNTgVMte7VPcwVE-F82l_MKDaUAEObeTkBmFQpb2rENT0uK7Et1w4IFTQZSbv0lX37ByZ_u7qRsa5_nvsoAWj04Swn_zxBJzQnuV9zy5lmKfF6pJBADB6nVgVEzu9SHFPh9G0WWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy3A2SYhxQUYLmkHLvvPcKnqYclX54t5K4AEZkpqdtCxV__EBf8BWGQxTIQdDcXixRwzINP5DDqkOHFj_z9KNR-NmzwqA1GS9cVlfZWjG5A901_HgGjQrQLPmgdhg4p4WwlLe_ZfnWlEKk7sf33UDXTE859Amrf6exm-iJmmVskxCU0CzbOUoto9cqwRSv8_yWkRtis3V269BB0l_s60yiQPFnSmn3vAyxjok8gF3cPE8d1XNKl593BJAJnNZcyq20Kvzo2sQ1QtxnEZmDyY0WWSXwuoaxTMlCqA02W3XgeAMrV2GQn_EZSoDoJu1WyfF3G_SAI43CqeGjoX4ixpew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWd_-lke7s4fIkKipWqI0f-SkjDnahz3FUIMRhW34Nxq4D3hFCC_mVcjA7dgdTtp8qqNQAqqmv9T0cMeQkRVkJD08vgEkDZPeMChgwtaDOlbYXwFENU7EHq6Jtjzhn32faM3RRDpEDF1cvnu8ofmZUMYnm79RXRuX3Dmp1uJ1IMQE9-EauA_vCOxiWe0S3q5yBu-I9yWzF4QayZkW0NkrjenXpFc1FDlmDkublSZsWtHG9v91zJrhD1ZNfpCXOtLVs7oqHQlzhipqqE0bPzMGGWraCDDX-W-DByr8BAVxOTCx_JtqAGSSm5yuUdWULLBtle6xzRiTMS58eckFYm5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slHecwe7daP1Z0UlrGQmLSZgx1B1gDY4P9hG2bCEJyUKQn_HGg_Dujq8KDSQ0Bw4rek28mUp9OjK1nUtB0EUfnD06Q6_q4FoOR6wlCWz_RKtCtznGpAP0eRtTljukD30N0J7FkqDudquyW-sD_qgMdpMRik74DkFSLBdaTgA9dvCYKmvt4Dgov-g2qLqkitTczn1uVqx1Uq8QqqEN1SBdMctIxBqcZQgKnEE6Lcd1NJXG8SsFNRQ7xrJxu7r44pjKzPDsngZ-EETge9F8thyGCRgqW5bnVC9bw_ob8ovywXBUuecoPhBvzu0s5ONKMDtUqMzgUE-YUD29cDw8qt50Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ahq3ZhYjjtVs0QYcQIoMLjKUR0_H0xYUVNV0bDnCschKZWxCqoTnM7sO-ISs-hT2TK8bfNra2VCfJAor3oVU-_b5DDf5HMuhk2DZBFl4yHo_B9GDeNCJFRsYThOvtHOYmpppcJ9VjeUyusFt_XFEoSXx1USR7na4yR8L5C86WHQA0a86qBHP6QJ9GITAHFlahmeh9_LUqjdGzxNUCPMmkdkFdIBnjS4y87j63I9568nsECw_dE1_WYqiO69gDy4sC0zBpkYs8LqNn_jHcqloOnei3B4_YNEpm4mVdLvRNgulHYFdwC6K2QDU-kzdo6199GB63JB1hpotyezSO6iPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mz8ZzO1gRQ1UWYx8KYG6yg2qHDd70XWottCpAPvDSWojDUqdKdy4c1TKnlXeHa_hvoPc6JDbGOIkQTAZXgoNCrpYtpRyORBvJ9eglLggymoZRculMxHj0C9RcoLFXFsPjCk4Yx-LLMGB4Jv_Zw6lRlZx6ZHPdbRxkXAg0E8mfl9qhgTBW6CM_0iZUOuIwtTA3ePcraVCNkj6oY8n4bjK0V9COnpNKbnaech5tkWetv0tWzRpyBAYDJYvhINurUEuk6qDYdJyyf0HMLLIZu1cM-_92itPDovsNVBY685Zy-ts4fBSZMjn7duO3X-iQPhz2QLfEOZWF7AlcKuSyi6g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DT9uMw9Q30QrqmtaRhqBDQiJ7jvNx91DpcIBuXcp91MDwsC1tu3vmEEIKa4-Yvs4AVVmj7tFecY8VSoApbgv0rz34sAmMbz7C7DQZ670M9ZjMMSh-qXxGTaWKhocWcU1O-R6K1y4oeKZo2NaGs2jOE-eE4jq6z6BLzQkxj5jWwfuOLJg5BLlX1A0DYqfk7jVUOrrKmZsMUOnt3IyEg2DtfZ5UwzsD5ztUO6NN9KXR_TWJWSJLxaGDeV_bqB_qwRjsSRsvoyu4Le1NbSOaEMRJjXFF-w5cORwULUtK0zhUiwm4e_s7-7kVh38h9hbFBboBhSwMZYRTeu8Ib3PTzNLxw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MaAvkWU2M4KQ9SNTWhutPYGTvodUjgPDEGQsKN15ITlYwAAuoVYlr0ltn1_-6HPK0f9oNQCyWexUV3PSPowBhqqhl6j8QmXORDv5ijk7laFdtZRa2UrYVM9xS5W1g89mz5u7S3P7HrFM_qYtwZl-78FYGMem6wdPCmLMxQe0195P5vPJLslZ8_mDqeIOtWDOciPueKBNd2Hs22-POsrc41eSb_fhasQFE115hf_3dkSdhKmceZ1mBEHEOlxYelPc7-sfZ8Au2swBsn22H3lohWm_PYvFmI5QVvHT_l3g3JLAPnMoetvfmZrpvcEox8OcnQsG3ySe0_pmM_xf-rAAmT6UmwrFgo-gZOtpayhYjJqgB0PO60clDV5X4bflzS1kgUNCwVyFM2L9FD9SC2W1c1a7qeBLJPxeDLMmPWou1XhLo9qciz14dFLkzbtoK2bWwbg8M0lLQSijiwyul7Gko1Xvm47NaItzIpbVp5MiU_2uxaNlOlzDSp0sMwuqELGtJNJDmGfqrE7db5ecUSQzmj1wL1jt4FYZHjN8AGoiZHVvpRv1Tc2dMQb9fCElc3LB-44ITr0GbmvxhJM3Qd25FNFyoK6HRybHTPXqVsx_DszGO7O_KLa8f05dADDuE0gGJ2d59TfjXskZMsESJRNtyLKQs35qe7ldw7J5-23_-14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MaAvkWU2M4KQ9SNTWhutPYGTvodUjgPDEGQsKN15ITlYwAAuoVYlr0ltn1_-6HPK0f9oNQCyWexUV3PSPowBhqqhl6j8QmXORDv5ijk7laFdtZRa2UrYVM9xS5W1g89mz5u7S3P7HrFM_qYtwZl-78FYGMem6wdPCmLMxQe0195P5vPJLslZ8_mDqeIOtWDOciPueKBNd2Hs22-POsrc41eSb_fhasQFE115hf_3dkSdhKmceZ1mBEHEOlxYelPc7-sfZ8Au2swBsn22H3lohWm_PYvFmI5QVvHT_l3g3JLAPnMoetvfmZrpvcEox8OcnQsG3ySe0_pmM_xf-rAAmT6UmwrFgo-gZOtpayhYjJqgB0PO60clDV5X4bflzS1kgUNCwVyFM2L9FD9SC2W1c1a7qeBLJPxeDLMmPWou1XhLo9qciz14dFLkzbtoK2bWwbg8M0lLQSijiwyul7Gko1Xvm47NaItzIpbVp5MiU_2uxaNlOlzDSp0sMwuqELGtJNJDmGfqrE7db5ecUSQzmj1wL1jt4FYZHjN8AGoiZHVvpRv1Tc2dMQb9fCElc3LB-44ITr0GbmvxhJM3Qd25FNFyoK6HRybHTPXqVsx_DszGO7O_KLa8f05dADDuE0gGJ2d59TfjXskZMsESJRNtyLKQs35qe7ldw7J5-23_-14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rubejCeSaBqK-Gq5O0Kj9EBUJixG0E8A4lpZOg3uu-p-mx5vS7gZo6y38FJkFP3omfQnh1g2I0z21_lfKRRMLlrktprTnXTf15GUDgdihsJ8wQh-9PU629YDfWhakX4aQ3r8Ir5Ph2fVrfzxtaadDqS4cad29ioCU3cCZq_PENd4STIfmVutVZzUU8wOGXgahkGAaioAbrKZMtkqf3W4EQRrXMO7J1cX0YmSK1hXvpsE-astemLHT1Hzcw745UX_YncLml98gBbJXvLpX1170qXyHN_6hOLm7CytefGqbiPK4DACo26kvA-zVmvy_321HUfgiVH528wby44eNuk96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyN7g1VHUUQxMh7zDJUzcfymqSdrpVdxKgbOwfiAszWuD95JFuiGIgVDqIaBio2UQ0e9QdpP6RuqqHdnWXzSGfcRb1PY_pWMfESYkzwfekzuP1Njn3By2KMtws7AiHrQtQnMdd5vLhJO0T-UIFfK-4R6nvXu5c_scYOOSYuyXUYcTx2aXrD0-7RDOm8zpRQiQJsXVFasdawTRYEd6sbd4MskkadyniifB5s05TTqeN4oOgREM_G-o1r1pCgolM1LZ7c3WPtJqLhl0QfyIvJxCqOOF7loqDOCpeLtH5j-IYGE62_SHv7ZjIBq_K3cldNQCGdet4VQM-w1AToX5mJlsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bb-ThEoaxaOV2AeD6kQzbGSMMrMShUs5Uul6m6T44R9bMfx_UC4-C25NaavxFRgmwFKxQs4yxCtBjF42C97EeJ3yXAa7VO1Tao2y1vrxONy8gWxWIHnzQAt32jqqiyf8GuKjatv2aF-eDgYNKacld0gAa2mPrYklVmTH9KuenNd7tYPZQzHmsirk0FXJWvF5fxwTjH1CmHG1YQr6EybFFedLWnetY7RA-2XQgGZA-8KuX11cwR7wAyxchnYWVPZ2BcDgWmNL7zmDBklW1-F2xdEpJXAGBl0ITwZAnWtU9to5n6Up4a_zSaAq6QhPwuBGnC9SM1coA_Y00RMOEZTFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wwkgk21H2QigXe9S9XWB3Qp5XIRsKkXJuJjp4oy0SN0Q1bxqN5ZeT3J2BZ0LHsosX0DaboT_Ru0ZMcwnqChvIOHt9a8axpe18Pi3laa9rXm6U-n87CwjmgfC7LYN3xaq2PCw8WrdnlytKuiN4Gn5iVVMvzYMcD12n5zk3nL3yPadPit-vVgCYZopF2UxGQ3Z3trLEGAyMxyJipP450Zq4VHj-Y7sKWaUKKgpwsHAlu8UL2WmQNHpovYM-y2t1j7afD2wIKSIM9UjmNml9Bjdqu9QVFRLcwX1gQUKJE_YDuo3bjKlBqGg8kR_5TfFSb88jzHQnuu_4WOQwoeer5kk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKwk-tl7OoyAoGsoqNBD0jkZFtgW7V5IHyhI0Xyh4u7iHbhjtqE8OaHioZIa0QsP4XaCiXHg2Nn0dAj1YE5xJ6hL0H_JEU8nlXCMSmPCQWOzz5OKp5flN8ICk6CBp6-dpAwEl1067A7f11cqcevff3tCClkJywrfbgpGbQTUdiafrDPYfLiUZrKSaPxaJPd6qZewBYvs36hShODywQ2S5XRirzdLE6GQsYJRU0sWTZyZvjO66ZZwoIfYCxCEPcBvhs7wQKQREA0WpDWFISbU9c8UbZ-IP-KYY1a81gschCD8QIjhXGbz3kfnVB8CQ_Ck0oYing7Q8iVvVP_cOwbPZg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0So07oRr_u_jIRVMb13aynovyjMqeATWBS36QBdNbG40TSXmlpC-RGuGFPLYA9rVE_v8_KbiRQFRac7zy3itljC3vhkU7oY2_Am9WJGaDWjjZp_yQxfhdtbQXJeKL-j7L5Blryujlv0awJjdIZ1f6ozPs57n00sQeDINIj3RW11XoJw3oAqnMedwwErVq3qYivOzhVNO4k5nBIh-aE6bfQj6_cQjOKKPDQjVspPy1Iiv5QaPVlmKjB9-JDh-1eGy1uer-CP3grYBtDUZbYeai-73WwjF3yMOyXsFzBZIloguJwp9MxJiZ_TYAGVIlPQqv8LhSuxngyQdMPg9JYOy24E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0So07oRr_u_jIRVMb13aynovyjMqeATWBS36QBdNbG40TSXmlpC-RGuGFPLYA9rVE_v8_KbiRQFRac7zy3itljC3vhkU7oY2_Am9WJGaDWjjZp_yQxfhdtbQXJeKL-j7L5Blryujlv0awJjdIZ1f6ozPs57n00sQeDINIj3RW11XoJw3oAqnMedwwErVq3qYivOzhVNO4k5nBIh-aE6bfQj6_cQjOKKPDQjVspPy1Iiv5QaPVlmKjB9-JDh-1eGy1uer-CP3grYBtDUZbYeai-73WwjF3yMOyXsFzBZIloguJwp9MxJiZ_TYAGVIlPQqv8LhSuxngyQdMPg9JYOy24E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEc9hGyiuYJJ6K5xLUfIFfm-D6TYgtVfvQ2InAGd9BdZ7hps85jNjAsGQ7LoXr3CnRBjZm1enUZJ-rykGRy78zEdEn9MaAI0tXbgO6-5CWMvIH7a9ULDuqrW9LwHr3fKQOEPQJFzG3CUTJU2UHWAj0CRGp3IIO6cGRnagQ6dO88rQiW1JvFIh1NnZ8808J4gsj83YbWbH5bmXYwmQZ-141ncJoKjoYAJbvtK3jAPASqWa-mGok5c_MCMR2pcUL99rFbZ87bS2qiylpMHMoqQYeJaw0KvD66GLXtnG-6EA2_JOMaFjLCMuYPOrzBAWjWXi1MeLLIgsv3UAfRJGg54GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDrLKrAvWeLzxhJAW_xvPGA_mcR58MtI-lOYjqqhBB7Oz4j1njRkpM3nHyKy6N63vXRItFqzFhyglBY6zv2IlrfgAySGVrGXUs9Sci1dmq9185Xw1Uge9fg-pycH1o7P-Ey6tgxU9Re4UsPI-TaCXENeTyL4TyZrgrpfDFw8Vvaa7V7ni6ahivmgNZAkHXrK2ZO6JlmXSRsxuvu26Fcbz9KCGathGVZvujgkc8RoOgKygYj6YDTCtUytLHEkUHqkIkYiD0fyQLhIeGI3TYdzmTvHrxHf7p5LZ7MEanHYeBIsk52QPlQHqpZQfsd9-IgDvaALaZHj43JqAEt9hD6omQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxG_WRsEff3rrTtmKkcsJV6d0wnZDqFdnycf1I7FbdrkyrDq1pogv9gb2hhoyL1y4OnX6DUDUZ-JA8MewrI28_cbyNHgusOgGiTVknP9Swf4KrUk87a8EzQD8Q5NGi_TpUv4BdvKj7YzV7FacWlqLaU1fSZv8B5BImz21IgePh87PyLM18IxkuevM0O0B7jMTIBasQGJbsMnpw3-n4h_NPjQfDNv1t34x8e-_qDJIyMNfDWGWygu3gdfBmAljpxEB2WII6vmfnt2C7u0zEJacCX0zwLusJvTdQEImWMCS8ks1xH6aRud-IZSVFteCYq7jyGPMys1B0EiVi15wNrM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIMUqErg4DYWDWaiFyNYNtHAkp0bzwxph2AZg2b_2sMRBEYHBpH54WfEVwkK5qb3tGcPY26VMwosB4WbKhWKKXr5xrP1DazvCiCdKvtgMlZRsyO1FBcWRhOGVryYh7Ju9YNc1qF2hXDiWskkXGykoC-3QVX87kSG9vXOvzQXwu1abDT8VgDYTUsnLz6gjCfO0Erqfx8kMB4Emub7e_Bjp9HgskauHLNTBSUg_nM-JRMyLzUpLiaxDQsqXUnkg_IB-1afQqd26UKnHy3yKW8nAGtOQKCg5U8egbRTobgSWARwmNsrBue9XZWTh5oik5WPvAO1ylyTMg8FNwkJhSBO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMbLJJPYE_Gi1OyWKDfW2GXlMifXu7NXfPnRUBS8nY2Rkou1fGrPlpEH1_LMfLaw1pnHQqRECYxboe25KNG1_NSllyDyQ1WwWvG1-SmF7w1rNnMG2qNRZbbl8P-ejuXnznLd07p4TFsPg74XRetMkjrsH4NO01Q0p2YCZ2nrhwHYSYXGpKw4-lxtS3JeCpsDNAd3pCLSJBUD1S5WocEIWg2osLlpZBdkfE2otmRDoVHzc1xqrJc5sbKmsSvbOHJsiZ_3I52hU3NdonDj-OAGyw5WYyMvR23G29r2HONiheBl3F4-jDrq-4gn5i4epeby4tzukAN5P8xXGLdBakoaDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhT-0aFG87EBbvqR180gdovXwqhEBH2REwdT5uBdCvAnUEAdzMTXM0tb-Pk7J7sVsIg237tPayRpK39Zs5QJGVCUDKYH4wIb6MiJbfHZ1zN79Sv3eRfoVXGftMN5MxwpEHn47P5CU7Qy-0RxNVvQ-F_OSJT6rnpQFmXta8BlAIsEj_ec2yKIwke5sw4zD19zybkE1JEi-WY6f7QsyWjzVEtq4mIgrNEbdchycEGcuYFicKm7JbHOZ01xhrP8k9TcDpjhafY_BMT8gEAabGBieLo_cr2-kP1veyxU_39Hbwxe0LyKww1xAfZ5LiHCkXR9FJ35uAf7fIMhGAul0STMuA.jpg" alt="photo" loading="lazy"/></div>
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
