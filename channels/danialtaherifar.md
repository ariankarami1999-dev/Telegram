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
<img src="https://cdn4.telesco.pe/file/MS_GQvmPm1tGVcwCeFkbUQgIl4edbtTWhHOnbzAVSRFJvcOpCG0nfOx3WSdnfW8uVRirDmOA6dJDNXM4pGSJdetlF7rityeCJSDQk5EH5a8Nznz8Axnwm0VeHJ539URRvYzOcKOlroUdOW8P6R3WQFNQTANxt1paPKQRYX2xccctKbRwjj7iXjFxnrf7oByAa9qQTPvCQx_F8JASpTTuARIboLSzgF0c9VicQdCiqq8tuuH-eURXSKVKmSi-EwG6mH8pAxazxmDgQdUy98q1PkseFIUAn74RkB-SA89lI8Vpm1c8V7kwE2cjmqJSYfyo7Fou8OGCemnGwZY8AkEldg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 338 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 503 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1h-LL1R2dxLgZ7YaDla0DAaFeC2D3LuVPtwt7ZWug1UKr-d7wTDuFtdW6Tz04vhmM43epWBNUf6bvMaFYIvp8kmp6fFxofqQnyEWlSvDruHpjI1ZBireK2XcyRePCTVIBAJYCzb-ks2TMZuVZrLcvncoCbVnKAXxmWqVM3fl0aUzql6qiveuh3aDzXL0_3GWKyULr0G25At8MHUWjbqeD159eCyf8PNtMaoDpIpZ8a_hsfhvkYXRDos3Z08b_MH6YUY6z08TxS9vgbRPQkkk8PZN86KDa8QMqT4WJnq5bsGbmcTOTTdizLzuqbhmIqt0jwl7R-GOdyFPnX5WipMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axEO6d_R280I1cAFfz-HsDQCZaIBR2gGKoEXkAlBoXTV1t-alpkjtaHkxH15PhcUZl1qbRNX-I2VsByzss8wD3TziR0kR5TYpfmyQijgTfDB0bO_Y2assgMTQjNcxMSPyQubTld4jdnfPBY7lWfFpg0RXdtbQmYoOheWTgwrqe931rA22GF7Ey-nGJaJTZavKxaA10vhu1kC402Jq27G65qOVg6JsXFIBsdvvHveNG0nyVs3bH3lB1Y1cP9q2pexn465MP0Xq7RcMcFaBKENv1pkMrxxfZT7_NvbKlcpgYnGgkNWk3kyDQxk8Foim5MM-YddmDqJmc5RUhZ-TaoOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 901 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEUEDfazZ0W4EH6SglRzCDmy1HmOKf1xS8bdoEdmD5lvx89_OmzHayJCntX4p4C_aPp3VuY0O6EDB4NyIIWxV3vqpm3RYQ82YaFjo2R8WSrsgxwY_as38cSu43tJpVDTpOlQQd2aKljKiI5fU44215lUdSSbznq3SBVolKbly2Ak8Ta_ZS5Ri8f3R3ArS8WjcUGkpQi4grc5OqUG_GVKfL69x-5QCtHp61DCeOLeOOlKmXo9a7QPt6KT9dmH2Op96oO7_faK457tAsmMbZxt8xHDMaPYJX2konMP3MWFSsjJXoVyRiN6NkMJEnD_anbhsliLjapNkLrkyWLyrGvSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdGrtl1kdOp8jvHEtQs1jrz1vF3-1nBG76yWEjddRP9xQvaVmH17dvFvZ4HQwpV5-AwMXLaIViJwAor_cHK5F5hkMzG-0PtgFEZ2Szwmh9tWHb-MTflTIq88SHd_mvE6bG3DpBHEsqNuzeZN-YJL4s9P9iDTLqNFCLmUwcFcs4YvDnxuvA8cj206Vl3vJ4HNQ6mTRGUqZ-wo8YdOxQlOpQg7DF8oHgvmW8AtC_Zz_GCqYbjrLL2vWSRTnj7OPWKDPoIfNIqAkRQTtNd-bPVMhuiQqt6ZOnbIMrBlxFc_jfMpjHydTlELYUVcT2YXb5RkN2VCZTVcbODSgTSNDtz-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9zUTauF1Tp-k95EtBzznE1bMeO7o03IPyiZxm4ZWBHi9Aiddt80-f2uOrEpDtqQ4BqE1fKaCKx9CVHVEAv8gdzEugiNX74EAONbpFeuKWwFyl9tWc4cRhast9R7MA52yoqvVHIG6gWnnw6AHrfD_nBG_i_gK4vkDrZAQlqwM7AUY78P6NPvL6P1NLyQByz6dq-CLk4_Ybjv6vNFyBIDr2XPrCsd6lNWDCjYuB2FDFZJG0PPIcnvTnocI-AZPoEelHe_Idi_KD-CA_Jyj7GjOCV_KVMxZx1g1W2zNCHfvyBzLYfcUJZ-iT3OlegaEP1ELAjPofLWaTNEwiMBs-x1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeTbegrt1wtIil3XfVhu5rv9l8-HQL5_It7nw_1eOLjhn-T55rLfVzwt77klWlNvLgkEoVgAqDX_PP4p2xcJzaVsoF0L4fdwZX26gBa0ZBhMYAbhOe3l_O_Q2M0pkhnR9uzQsmv7XXMuIzn_I9R7A9ktnX4oAI9vXU52LzM0tdR00FOLZeNa4Ev5bIDeKyB_UykVuFSOiMvcI7uJJZBGtf2xP4Nfr1G9RuCTIXHZ2DcmLDNoEiwJMgF7zeUjDHpN7IS0cwZpJfBf0Tw90mDBFTPqG-5W0PCRWmKaZHeZuPDsOg5etgIITkY7PQzxBHyGgWrObIZBEkA3bjVElpUDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxc57f_IklPEgTB-xCe7CGjeK--mIL__3sN0tYQ6SAXzQEGkrRVEP7P_T035ZnjZhekqDDFOwdcvOIajWhJtrZZbSEpnj41Umgbj7lrGX78URrw4CKPNl_8qCIMPnuQP4UFxy1CyP1bgH-Ja0kK5wdmmQk-n5hvpfFyhRZPNrctDN1HDF2XwYN9h-DxTO-KzZ0f6Krug0DC_C_N1uisaK3Gjy9A0Mau64hKhETtQo7Oyd1T_4u4mebzP1q8kRp8-wdMy5u_YDntZeKafeeM1OSQplAXb2zU3IBSyeAYwUVXqtybZ6UKpJrWJRLPOCaSV6iCjrNWF8VhXNK-cnIhynA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOnxWJPdgajjNmX4p-YCsnwUgrwv5tI1o44V7zWRmH4jB19WHWCGy2vbxKWt3FbfBUss7GnbUWZ6YajOISTM-dSDdM_dCPGHO6JNGbc8horKek5fNF-coVdAu9tRERPUhk842NmDdC1oRY8bdZlet98YfHu4VsTCQeLh_9Ua0BR8vr2WF6j3L9ckXYL0NEzsjDJy3X59V3N10oe6yzr4mPhO5vgEGg8fSOilhvG-QpKkNrdWVQQvhKFUMYyngYCyrTdqUD7-aPcS0HfisplK2_HjvnSfUfJ-hEq08n9ramJoqSHi0UfB_g47NZtx9NdKmFkvpDwCZvNTkT5xvQYvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 659 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPzAVut_NOhFK4iJw4tUEHzEKL6E_5g74DUn5gn8zVzHzA1S0IPUqbJ9hx715LTlTVXuev6lxsnRwE-HfA7ZIzg_pKYaH6gR39eldoq_qaTCZFDf0UdjQlAlLv6xFjOzC3whpeo0dTcb4_ZkZB3pUUWtpsmr82-84jHiKAULANel9YnQApF16upKsuPawwbD8KTgM3FDeaXLNRsLlTNu8dGzwm8diz7LMrgaws-pthEkWANUGnqHC0U--hX6Lsm4pHlNy8a8IjmML6j4Wx3vSljiA2_gQ06VIKuLLmuY9siZa1s68Mgp_UefR5jMAdqMmWu-pAR5tYx8qI7nj93vjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKvS1edR9UTXKJrHJJsdjpPfMVDL88zM6B--wuFp3pT71FJ_XVfKbhI1Alo5-I7ImSFIV-mzwjMxJopvIZ8l8KTlAUT-kNRPUtBeFGUkoB2UmD563et0HgafJnOsKrpM7vLhMxNm5VADBTy2t8_7c7tq5dwEXRAuOT-moKRbAEI46ruCRCC9-0Z_XJcm-ki5rkymakO-owwvJ4tnHYvmLhd8iqA1e2_vUbA8fSV2IuAS1k-ng4h6wqA7Vw001w4-TmawHOB8AaLWncxQIR1QjX-S6tRUJamYFTKYAc4-mV9MFSlG0WUsmUtZBX7SM4Pvq-bUgvc7MqoAk9MUw_4aWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwL1SdSRW0rJ-NW78GPEcpVSaP8QFVib0kqhefBr8uLGz4JAdwHMRD0Mmtm-JX62Og6sYKjm_hrdIRw6A1sy0ZJ89GnBn5sIwMyw6722ij_bt4bvOJdC22FikmQOMaqjtH6uGq635V_vTdaIzyuf_lo0iGfDdwDHCzecbc27TjOF54CwIlUTaY3Xf5fNlSrqDpE_-YQ6VyI0s1atLv7w2oqbQwDnBLMuJPgaKbsfVgd2WAEzwFhwG5sasWliuEH2SgXbFiP61Q0zs96nC1DuXlFdZLkBa6aKoJY9bAuEykrBLOhqRVrF_hKfaOK3jE9k8f6H7r9XDVlolqPTfSNLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJpwfXIApWuAatjJpScdECOcOybS2ubiDxz0uSjOC9OL1qaaNvFWvu_VCkY8YLfWlR3E1t6jyvMelNDRjZHHhWT222Dy6GkCnlIMNmzHhSKkUJHMCjinuumKB3SSpvHBSjwQJP6-kEfdkFdckTkO7eFvKuzQkkthf6Fls2onHlG8WyFQ9NXwfKwhGKVRU5N5CO3BDiem87z5LTg4mcj-sf_I4DZIi9v10ZpjmSY5LsI-jWNOuVljT4cQmBanH_MkA12lBSf0UnhOv8xSS6ndZgwr3ldsVBmak08ZEeqRbOpq-pudTuATJInGb_VYX1V1knROzVeVLln9do934KA2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4jsdY10q7gTRtkgA0R5rnwkhYwQLCtH7R66TlXl6HUUwPfTHUAo7cn_wV7JYGfhUlrKztWIUcHHSxnGRjw6104lAKNrrug8dv04C1QYzcUooG6cU8cmG5B35OYjBIwdianFgbFiUPFXFFwdy2tZmjUFIYyC5swiMpd8EtaKbk8eOqcvH2MgRfiZHtlUKEauL9pj16yLX9nKJ_65IrzTP_HSBuUnqTX__3UpCgn_ZX7mU5YDtG1WH7uBS_TRS9i3CYlAkWWQZ5mJAxBcBmkDizWbQZbdZ7V4Gn5CXtkNj9Zubr-qABaggRlBokZV3ye15agJp4hw1N3n62RCozfNYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMFRBGj_ibCEpv8gtevKp_d5lNXQ83W-ekwI-PLx4Fe4BrTQZfugB-ARcUnTlLPBlQ59LZ3qNayEytvdB3Lgk_slO2lmpMwSCx6d9pWK9dkkWtUf90xjwLjTy2JXOtxVGFdZxAOW3IfTYI-DE0NFOUuvmvKqKUU5ESU4ePIOAU8EWmpVL_ktQdex_CsIJ_opoxPyrY0OzMMLnxn3bvFMu2DpDQuacPXLzt_Ndy-E1Ungle1U7hMr2L8mpfDir71rxUmpf7FdsmTWtPJgl55NLcDWAnA4LeV-fppuzUBQb9LmtTUqNj5LbOeMy2_JsJOtQQJR9WojgbFOuLiYX3EHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9FBaTOFxCT1SJP4G9x4XAd3eXontwIKUBTYQSnU-HZgMYS2a9mQP_dkbgTZTgyShRLNUHNDbdHsVpoSqPWOChm8a1jpYhY0bvEgtadDHp21SBLoZJHbMklZjqB0iaLRaGBIozNF0yOSdd3vP5qhYYt0tT34hmG4T9YR1Koti_wT-5vUywxZCi-4rKEExTVPJVJ1SpYi8d0FgslLQkNWp4_fIxv47ZHm0N7FJKaE2JDcTpgBvT00-5JgQFPIuYe0_xJBbJawUHqgSBOS2-CID0cCGDTB3TWW4kZAQMjYx30oECQfiqAWHcxcjKoQbMTUri_VHb_2XaH5sZloj2oI2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArIpJKR586E6Umd6XY4JvkpDjdCeeNJc_MHT74WjYdGvG6BI5tEDm8zv6koSf4eDPFUqNv-mALExOoBpDnLY8pSImFesFpZ5E0Dly5E6feKKPm1Cd7174hos3AfInrlbtfutrZ1XaTZxQiaJYm3BSvmquFksESDkfGpgMzlpZVxob4mY68gBm-n5EX56bFGvK7CeWX-AgG6I6HFwwaK5KhlhNstAgAyAC55qEa8-E-ebQr_nDzEjoMx6aK306eLMoBkOj2-WVllliGofdTiCimBTsH7nv7m6FxSugoLc-HY0OVAaTAmS9nV2nUFE2vnC2vaLMpkKw2fBDFshhuoiuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Nmdia1Vhiagth9x3JM3YHupfGz1oX-nJEcX_GtE9VaAccF9gNCart3V1ovmC9kZR95orSkDwmR5tojPGrR738Y9Mrxws93TFnqsaoMlZsanXev0knK3rzOMWRYIU4mvUlOa1d_uGoxbCYyFbNexsaS34hcNcnEnBrHL0e9XKZdPUjcAHrLNe4xsb0fEb1zhdhPL1HZ66jXkIYA3ROYK3-P1k_3c3k6hZa-qh861LVvw-SOwlbiGWqOR5kp9Ju7wiDmIM7hDom6O1yjCWWZo3eyzXtFOY13BjveGBLkTJ4wzc-d9kYaTPhdpGrsscU54_UiwPnu1tW8uDbXLvUWST1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Nmdia1Vhiagth9x3JM3YHupfGz1oX-nJEcX_GtE9VaAccF9gNCart3V1ovmC9kZR95orSkDwmR5tojPGrR738Y9Mrxws93TFnqsaoMlZsanXev0knK3rzOMWRYIU4mvUlOa1d_uGoxbCYyFbNexsaS34hcNcnEnBrHL0e9XKZdPUjcAHrLNe4xsb0fEb1zhdhPL1HZ66jXkIYA3ROYK3-P1k_3c3k6hZa-qh861LVvw-SOwlbiGWqOR5kp9Ju7wiDmIM7hDom6O1yjCWWZo3eyzXtFOY13BjveGBLkTJ4wzc-d9kYaTPhdpGrsscU54_UiwPnu1tW8uDbXLvUWST1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7eVqjlecffEM5H8Im3WuKiSFAnVA_ZWLO4Gn4emkKEPwVK7LujkPDNH4iRvarVIt9TaicYgUqkxNzPHTRx_mHSbmwd21DiJLh6CC3c_r-45-MXUDd7ImaIjmcxXbjiirxAyEzoox8JDTj4n6-yO6OjtnLNC8JUEw1_ggf-8sJjRZx3T5SOXRhlmbEwcQ3Ey6ogbiYcWC3FTXoef4cZbdRrijjDhJ5ttKvHnytM4Rqo370e8anMJdcGoGMRRMi8itVjNhemHVrb0qzQfuhcGej7YysQwjOYYKW__aTGH9sfDQccKwEuqCvankyvZlzhn4i2O9kAmwdii9_uhM21qVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5imK_ZaQXbDZ86O5UpssACyos7i9bDuBralf6lWIDysmKF3hMN03fszHmWE2IKWFqxRNARjyhS-MSKegfyfb9-Pv0EAliPcXghWsjBa_epE4m2hW01fH_RAnvlsmeJ2oDS0ms-Ry2q8SV5Lwic_pe2kZzFJ3y9A8OXXm6Wk_sBY858E3hY_YXjLDBcGmtKhab4-rt-WCQ3-23qDjA3Afm8ubUJNfrfZp5FTJlii0XkKtUpLBn-2OMFojmEx6otlKqi5P4qFhD2z2yEz7Yy-EMAc9jYqb9aJEdHwQ01Ol_UQIuxmZABzcSBPdy_U28BAbHln-jrlxKtRqHe26ZmIvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5B5Ty1d2BQWcdYR4RMP9sM0kkzxoLFxRa-SLtkguTzn3EsBRslplv4yOukh1ZE1G3hiaWljSV7mJFty6oHb76pmJW2X8wKlb1NV_T-UcgnBjhCStQpkJL_q6x64h-nilcOPz9YCWDFMXEmjFrXeHxcIERbvt_AsSAMEKHnTo7ggqVH0qBpSEkHfdvqfVAMk7nAtncMoBQ_heZJOfiq5t0SY85OKTyZGrQOOHaPfm74-U-5ja3F4dsbNcTVr4dJFj4shLpPn_YTcSEXZ45h8bezE_ovSWgKPSkhEcsJhVP0EyHYq4Cm5rj4XnzAKlSU5esUzV7jy1ToRK8jZy32i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr3CvhMrZy_7_GS4ST1ddOCkF2UAP4c15D8Ol6ZxgffIwSk4lvjNa4sTwKTqIs-PEmJOrwJD3Ujs1j41vYbO8cGX4PRfVIcwLX02xdhM5V6bofAehq_E4U4sTTk7Nb7UTCG4le2qDyIYVgFvEp316dBJabiP5_2xdGUUKzP_WJryXJWCjZttGt-MA8_PrhtkUZbmBh23HHgyyeV33tnCclfaA7PlBGEFa5aeFwVNx__vtLa0ZVxAPTCbCmPKFR5vhJlCaUsrS2lcK__VopV8OeGaqsnWZWG4GbaiAH7aeMp9skY9yRIIEF2KCkHWdI0PCdXKUyV1gxAJGpnMJAbqiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEXsVXLFULO3xfs_nqBJYQ5Y0csuEvIPUDMkKBRIQR1EPj9bv1Q3YlHREeTC53drY9F-3OQawEvJ3GP7RYM9dgoWbD3uCmvE02v-Z1lSZJHP-mQ9LzO-QFF96kOjuVfuKK_tbTEKVz3M3hV9bsynJ9mWuSQF6AjVh-XbAr6PT0r0pKZa7D-hSWStLtkh0RlEngBM0gSTS2hznjjPzGkJnXlWee1tnXIcgNgETXV8zW6qxtXzZo3vkKBDAQGdHB9fFst8XNJrdceesGffMbZIb-oMDgpy_ENboeLLC2mBTMea0k9kL5d58xaO1L_i0oVDi-_meGL2QlquYaBXH6jnBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1IGWfwLhfWR1NqKNfFkpitYUqgp3FKDh4KcGsC7WWkc4IO4PXOq7hrxxcRKZ7jU8zD_TeZHdXj6Rg65646DouC34lgan99IHeC1x-OCbtWqVVhlV3j43A5FXY4LPn81_hKnCfWHogjI1GYgaiBPSOrshkna59tc1yQj-s4uMcwgPg1x3WNZJ3Tq2B90zvT3KWxQh1OKGtxPqoi0f_6yJXLvkEpWS4L5KvEHFuSw45ewdz6cFyHp1Kpe6WLxewEQAO3Zt3B4P5x9FOPQF7fYDLeJir0nih6at3Hih41ykBnmJvlWhwNq7aegmK70Z4POvgx9iMnLLPSQp5KWz4EmZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecFIiAZ6E4QUCSWBIA_tR81AAmH0aZhAsGzQDh8PU2hBlGTKx74G4rzKQozknwBpyVzNqL_LBbDQuRBc_2pYcVD_-uLgS00rLtDtpMVYwWiwHSzG44wvsx8k_sTitz56K6FitcaJo1mnXnHtNHhxHcOg7ODY0-kFNratZr0RU72wSWprJZoyHTpIdLvVONLZzS7qgyT7R3LgTGBs2AJBrNgNH-owMka2ribJ9X5Vq1md7G62PwuBWbV8abWJA0MzKJBepj38VgHQ_PywHhvq6CcMvdjzQ2Xnugea4jbkT8OGLlivxbvHKqYnQ0wV9M3f_Cu8F3YM12fd5zKypt1YcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR4rMZyr8020-t92IlYI9i5hH6V_lxPOo6uLE2KMLa5N9x82opFENaW9C1xhYbYIJqWvdC0Se8CxG09UXtdp_WP1cUCfQ1lqkpXi5wGrvt84sOcXp5I5BMMW74VnUeYRksTpQVTMGhOQM1Jw1oo9IZxFkp2x_aDc3LPonorygHG5c6TPkX1RNfXYlHg3hvZ7eHm2SRKnoE0p9E34Izo-q3-gPs9fTFaqIlWeDQ76hz4UPUWNEuHN7TzsKleHwOh5tamtAukRSDXEpyMjjNoo4-CmmIQd_MtWWXvADOkoGW51NXKOW0CE1wZos5jc96_0kKP5KckvOjJlmmytEeLwTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH_d8SKnstKq59QdAS654U4eqjahbdaUllmuuyGLs2p_9JqfrkBaBPAvHxMeXkNj_ogq26sWnBqdURA2iBLGtVONSIsK-M3UYMqSgnsSGPCcwy7twcpimCxT7I_d4trQDE4KwoLOXHgVDOPmO-6SL2xs6NvF8oKBrbmIXlofnAkL-b-pPhC0x8FAwUZqv5YYDHKSiwyCGHa5hrv5ObVj2qlkPFv1lNbOJUNODLBaM1I8AvsMpS_yAfv2LfzhPdpjRDB6KyVN7iAQj61vgCvtKABK_Bjp6KM8sTpsmfyIuvvTvo1oyDmy7NT1-QSnJZfPqqefhpnDCGZD2mFR905_kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiQomF_53hvg9zc6GGjnOiIhVT2BTfHeJdL_t5rjLQigrDBslCpsgFoGFWirqeyIzKT4zbVnIjIpeMsp4h4uUNfcgyc1biXaXoG40DfEt7j42qfOpACVHb4lDXGKAzhZOvQ4L5qVkRdasb581rjUlmQSqHbEVfNLz7AXK6DfwoLog824fZD0akULgIqFH-4thWAONgRJCZjv3z9_n-71NkMcfZZ6aAgk3uZ63w3jzEV6-WUvEBPfrdv2SxfHC75kh9rSPADZPkAEqWft4cAv2fQtILF3Y8RieNxPoWMsHuDBU23yEOZ2R5My0XW6KVPzrOFEFI1v39Ti33LvnIQQlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu1yHBCMADvTnyjHXDi-uPq1HZjy31EXx2lEyEMT9OCKDTl20_JLJWAViy3NE4QX3qrZHN667xzoINZF4izeRdUtqQtvM57WEs5iQ2M8DPknMLZHTvOuCjpbQNq9DfWir16lyP2JBh_ySRDOBDxqrWGmKwMxv8ef8b4bKzVlmKbpwjAkmQe0x-3gZhbphcsEFcwUgTZrMelr6W_xZ3ofnElB8-QDfrm8Jg8JxszpPi54Q0pJ2AP2uJRa1rAS-LoVUF-p0TH_aPM7Z75cAKzZK_dk0eZsBUpIJGotNu5gUQbLcGiG8CndnONBGrxpYHDAGOxPggDzzvouH783goucWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqIiqAZnpEjObpptefd-kCqHMUfQi-Jf2Kamyt-j9P0fMJ3SGqudpU6x5QCdRmgDYoilmHdFrcsaiKb7U_TjxPCiuDh7ROIb1Y6LOlS3I10MSRUh_mmihdoXxi8ujKnum4GapmPy66fr33Q6vMCOlgpN6ABZUt1jMTO4wUGUqg9Vc_P-ZfDjVt2bdrx_es4znJxN9cOFYoZascNijIY_ZWvQ3Y1Dn4rhmuBsfXcGYTZ1r7V0KIiFZqF1sNECFqS9CTAN3uSlnR2LL-pTGDYJC4MxP1Y8r5so9KtnN5sYgZAxS55N76wETjibiMAbxORshXfXIIRAwtEIwPjumEnV2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUvxt4NKLSXio9aaId9zuCqRRyjm6O16Coet7_6OhUhKPfKvIHXoTN54HzNVYuP-hZ5i2Y5PZTu110XbHI2f6pvSbo0RNiQgDrsUwfEBCWqmMmmUjCVb2vnnL__DJ5gk4kmyAs1Mnc8Qq1iRsKYg_GhM1vRgfpV9GHlX0enX-QirX6vp6oOXlb3ggXPS2FfPelJDDGxTU6Idpernk4BfKxvrPHI9xtxWACqG7Ri13WpJodVhMy27miT9Wc6ZFva0VD2vPA5-PXC61CUS15hRK-JyujsOQi93_hGNT6zw372hisns4R2dpP31-LuN3ZvpZyEaMvWG-f3VH_8Oei5inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mekESYwR5PNIf1zfV9eEN7anG1vABj04QjpQ_cPxh2a-OVSEUZHp_EN4q2CUnjBjPywfsXVxI98y0QNT49SeYrWo7hfHjeuXMBjbnxOZVlxnxnb9vJ-UTLIjqK6W9zW1M4lekFKAoPBmV64bBOvWsdtOLm3b0jRhcWEgMQC-vtlbJkkOhP1CWpLeAHNd9KlcSOpMAZKBYgxr1Uhy4VxkzBE-jDofhrWGIyIALGKKDNuPCipL2tUEYqj2RtmKfJ70SM1EgpVP-fjAVHTyKpns84pQmHnyRg-fitqsf8JjgUEqhynjEhNVmSMU5VjyxqWRDi3cORceu_v3wjb6F_OZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXmQ5T8WhfFFbNXFlWn269t4Gfn76pWt5_fSYk156VeEBVo7OWvljw_Y3KFZccg5pZgP_POQPZI2bBJRcMYHqfcRzj0I6RD4Lzv53TIMsw-Jjtihd58rGHFgv_5ArNBJzG2bT7iHiyIus3jecZO5K37YaMa4ruLO3_i1WE7vTJ7RXeXLD-Gvj-UntyGVyqtO-lercVoGWBiTQZG5XasL_6H0EfZlZXQZ2zI4n3fpepERbOLl5Xf3VeAC_ua5x0wXkzg_IuZz5HX78pYWDVXNdeF49u7ZqswQGEfl9YrfbxeJhdBWCfSEcSKg2El2C_whIZ3HtXnKu-gu5wVSVns-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2IEm6bw3c7SQFTNPx310HW28P_3wfVRlIBTyHNAVXkCTZkulFqFgcRYui1KKhfJFdw5-2YNXQaNcZF7uqQk5d3HFKJ2IMg_kSPHCu5v9M3MMYX56UEdic9nRNgn4cdc8Nk2fgbEVOyxFJa6QhASLqk0JO1jP4LrJJrJ4wKldlF0Gv4hReO8YZeWTjzKXfWbMJuFM5cOT1ORkSDs7R4o1fBIIali6gl_piTA2V2zzoL0yDjIcpqCRnnCYf0JtZvMyjX8lElvESRrMjX3pnXlUZKeKEPMIMK-ln4-yg-QwXc7boxYusvtcZBnPFOmFt2LDefy7vABMZ2tgn7p9JuBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq_fu1lQYMk_CTR3SHiY2KMlv6jSStJ904n4r8mYxGn70OLrcQb53O6Vqi5OxJTOINKG3yRkjYLbmZsAhNYkUxlmzKDXRc1XYknu88h_siciigKhLI9Mm8bT8DECfsTOWxhHAp2ThvlazA7PBX3Entfu-v0EQwYpun7wi4ZB-ztOxrlLErPXgWFoGcUEJamYqNLahwttoBCsn8Dz7JKFMi3ovckr99iM2zvToHXEYxbcbkTEOolQwndr17Z5MfIc9zaozt_x0MZgAgPQ3J_Fl2qFIPWSaU5xMo2qLH6IqgAgsXhrg3m6YhoYyuyaSw12OKEon35XnHiQQQaUulrbnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbwQzBXs7fE7DMHX7zTQn2SINHRSkcMRUkVuVt6n9qHfqmwnxgtiHjlBPK4gI7ubWUvZAgYfG0_L5zJcVU-aqie15wr1Q2sZg5OKyavkw6d5ZVMj6i3S7uQJG-3fUC4fTlE91sbJInqMVWaSpNWC5MRYbgjtwG-mVtw4k6SCzxxrJxpsLinZ95QJwv4Q5ayLo1SW9igdZfuZ60ag-_KQ55fyA2VDnnNffNRBMLYbyK4AV5bCJXbIBnmPQy-DukQa92uANR35740ZWf6Lbspawuyg8_wkZdzFDs-aIIZIKsH-WYshD074Xsed3Xudx_oQxSu7nT7Z0magv1huj7hNiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHKislHxTTAj8bryj00H28Gk4NQZTwkqyunUwwFiDQr64hnSLcZqC5MStW5IVbvkJIXUagVN3XRcrFrwVkKRMxj2IqWanSj8wGxvVfBMvGvfaH3Nr4kTdwNQJnopr_PhE1AmqHMhrvr-gHHbLBJliMNhnvO7CFaBZNK9zIoP4KZQPrT9HuvXlygswp5bvHVbo0qfeD7gVZ9KFbNdjqkhu1c4heQsNILDv_WTbSr2RS2SDdg-HxewojNIPqxaJk8iT-aQTx1GlmIX7yo8wH32Q7UkA-VUmKeR3Fwb7yAaUdA-07zB8ixeMw34FutttmvLDxHupRWqS062FYUzv9KKPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbVOIr3n3CDHUEHpUyiyFe-bbp2dMbN9THrXl41fvEVj96D4ruoQQwSUt2H4Ks_VJNAD2tTUeRytnrA1jYf-UV6Y5xACgfqImL9QxtbfkVGqpaj293iZV5oDozv-kFXEyJl_o5zFvYhqcdHU3E4clp7a4xuJvKVe1pmD7E4CJRv8u_N9JJKQ_q7v8-sNaTR74AO4_5U5PrO30n9ovqksCnmn4x-H4eusD5s4MmLs0fXD396AM1O2u-Bj7GXOVFDs_V_e4svhN2CrCxiCKMg7drrFh6gRG0Rn30wqb-b9QZAhq1Jxi831qf5_vs8086cRhXfVamRbfgh8eWfLKfmrvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD0q3OCQupP7D0ZOIidTk99ox9iw0YN8ePKajUb_ZTR81Zz2UQkIqgOn0dX3FrpThEeRN8r6VBv0m6BfZK60EspePnJAMXDpZ-NqmbrOPKGWQC2jLvfvSJimOrW_SwEU8LPwNzbhYs2CjZ6X2D7xtE6nZFfUsxlg2NqYTQvm2wG2pW4mh6dlw5Bdj5W6lYN5lKJ4kd5qB-55ggiQi2g8zY066Iy06p2cZwPE1mPd3IiQ5LKbqK84u-z7KLnJQZ0nd5Xx9FhHi6SsEQXhYHQNGwbqaaV5J3to9F52nVhM7jCZMwFaNP516JZUs225xMMWNwJsG-3uIgsqQLrUDG5aaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEWl_tpLklBtgFLEN5n08MdXEOBEBZ9C36_lDm-udaN9lGXcq6lI0Kf0hfEaPNKEmcrnjGVrjorKL_YmvwDYSFv773vLFcsXkQPK4euSIVd0HJ-1ykvEsryktdOWBn7dorxlWfi-iUNpbWXigAhiyUAGk21MPcTLIF17Aoox81WL6i6VuX0wJIpDqUvogF0FyeCRkIcUUvIAhzhbdHAg2x91MbPc_I1b3HXqx3zX5-ah5JWpzoxT_E8pTyf8-j791XIkdvy_a26NLr1HztwVCKXeBGN_0amhYPKmBs8-KZmgbt_ox62P9JD4EooNl69K0y3AOGr1PPbmTMd5RUdChw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6n6vFwc3M0FQE7P9-N0clcDN55fopewWCYHwMA0Q7MCim2ggWWLJTKSAK4Ownh7zuxXF2GwCpBcZzqXTq7sXipw0Hljx_wp_0xk1aQDK3CyiYExLaooZff92GF-nEKgTIwldjkojyG8iSEU25i7AJHYobzn7t_lehe-b1PJVxzWmR1KRa2719qbcjHECeaSDlmlabmA1XbGHzgQz6vleCqdrLxNu0gSDLVgnlUBkAfVQx9PgC_E2-ewpAuX72D5ei4NjcJtOrYopdSlVQwc9JetpCdi84jRpujHes3-OIz_KzLFkcdAMpX-vs2k732eETpCf23DICxy6JiKlB6a4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoyrHy6wjqAarwZiFSvLYkbnOUplTFhDE8j1YzhHCTVyg3mR-oqw_HSWLF8lZFMLWAp21eqy6s-Opvwg20uX3wDNzMKJHgzcuw8OagRQdWosjoqrkR3RjtJvfQaMfmQ1DDN-GLaC-4U9a5kxTBIoqlnOdQ9EWQieSH5HP-w2RTsjnPszp0EQlyJPFbNI3mZoH807X4XwDNFCNjFxpbWhxsHfACY5nAGx1SeWmcG29TS5-l9H8AXLQTC2DHnJUEITWXbhBrBZZmrq1PQN1Upv4TqKhbCUjSeCbhOLr_N9oYwmWoAhh6kt6Krbgi2EVyqSSpr5KFqy7zwWYtpQaG93Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4wP1FpSDb8PACUvLyrfui6flvsGeNfUwXrXQeM7vmretP-Z0jEBeqCAS_DoDbyZTLFf7Ww4U4drZAKeoGOIBZEYwnzZsWJOhA2Ih_pXDbNKIuseDjltPlCzA1Nusn2Om2bpT-29-nWuGTIspx6N7Tb3iBdHpUhvKo8NBx3mJw6e6K8rMzATm_tvWvqxKQ9Hto-dw-Szf8KHTWcfWZA6P9xNxM5SqbvF5_UEms_qhQLmdhtB_3vd7cHOwRRRcXs_H2aef4UT87ElP-uUV1J2Q5zMlzywz-fgfkrvZWZ-AZpron6vcf0SqlFsRTNJx_G1LEXLgbcfw1189iYmEhXhng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9STND2DZjPlsTChTHEy72SDHaB2QzZTW1OMSmCR5GlG9jeLOL0EQDGz181UdbftcFiS9QvecLn5bqSUaKe1JJGwxutZcK-3-5YIjUL4FHYRBpmy0asflDQy7PtlT8SiTT3tYg9nI4wHpkgjwo4fv5zZPfRuHz3Swj085jX-5zYZQMYIJgGBDWuyMsitVtwPti-0h-pmzJvcj80b6sV5EGJ85xG4fbg-DQ4nFBj-ibSoXvTRKT2rj92itpFewEq42R26GbJTSC0rog4s89XgUgUEtlIeENSUjJM-6gjYoG5ibH8msOQO7ih737QJupfFV7WhB87P5_FDTueH5H43LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFLyPBSvWHLorSYnVUVdeZ5yHs-F-y9n6Qbh4lBXgCqLa6_C31JJrjCB0qg394MOqEpP0pmbUMbIRHhq-SnCFSfUQ9Bm5jyIQHrAJiZRrJ2LlySy07azSuk9tb8kickPaboaRvMG9ggANE3bOeJZ08FQIBLdfZUa795qwLxhRZXhlmzVIF0Bifeok6OxOtAD9BY0sfxmCfjENyG-1GyNKnbjdbkEKOegXcvAHLtA2gNVRWLuU47__S5BqSbPDeux4l7LHfNYtVuoN-jJu1o2SYZ8KDM1flz2HeP0cPCL0G1OxrSlqLjw-zGRZr6FtX9kNJ6BReVybO87vdEai7Jiow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyeVq1bPeLbmNDmQVjKzmICPzp2tR2rv0d8sWNU0CzFg4x8Kbw2CueVJ4t3NkfP485zeC1RiyrRFF5frnPpK3V4_F4VVYMmJ2jSFchuyQgGyERVaDSd0A74uRvAAm4Du4d7E-FiCPSsCHgKQ2HNY9zcoQ8FicirZK9JRMM5XNcODDadU6BD8HxsQiQbL1BIU65fqLjvxz2UqHd9FH8ZwPZ6TEVu1e1ZZpSLRvO2WEFlyKuRdIrS_OPAsYWFAuyb7CB1bkLvd7DaF7s610HAL93NHOSjBVHG5R5C_UsWI_bhW1yWon-OzxwBHVbwDxskJvo1lxg5GxCZqxPZ0zFEyNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU8craTZpQEIwKcHdrjz0icgZJeDtzuT0xTAuNR6NRm2AWbzZImnkUuCHmyBdlxnLZZZHPC7B9VGVU2MosoFIZh-lo4DgvPmDvfvsAlkTR49fKwkalSUPKByG2MTFUqr-e7hUUiUg2S3JhD-4dITnmclUGSzY42Z636sTIKAAiELGq7dhlHZ1N_C4KD4k6zR-STHlJFWdf17Hy99CmGE7yop5McDAlWQSOn5XfYFnGNXUOfzBkh2wMRVJhCP2rRPSxNnobKYGhwIjJJBE5k8_zce1MO4h-DbgfFgcw4egHKjlP4KxX9AJW67IzK9sMCFUjdaJ011DhTfuvCo-qHsMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwnkm3x-IC-fT64Cty3Ee3Fyyk4wIvvG9eDAlW4KoEGIvDM1saAyUSRx4yttmzyIx36oFPA70B7Nf9Afnu2IggJe25ykrg_qsG6P8oUwdJXUmPPeUzHCMyOYvggFCSr8dlTlbyRwF9KOdREOPxD9HPL-CBksGYCrinIKGlKZvJS-WBw-Bkrb4ESL_5dUdhzazepCowEZBdSrVAqJzlilar3irRlsFNDfHhozgLBes9HqdcunWWnfZRHijj5_FFjLN6qrThopyxz6N1EQ33SJq6KgugIsygxZmJ8RgzseniGJ5BdVM74-VHFfn9HcEQe0R7l9BLAhJ-B99_1V2Oo3UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw6Kg_iGrmwEdy4g5lnQRb3uvVgNj7XSRs_G9N7WeJ9tk3RvPPIVsoxS4OzmeZVH7n6NNqjD97CwXj5Cgy_kglG91MQgVw6poIVU_19-RdQQp2XVtkSvhG7JvuXDtnSu_UDKlfacKHY0eZ8zpe0wYPjOAz48Wwz0rfcO7JZJ_nct7xXayPZszSbjUwUCYTjAKfz0H5G2XxHEdpjgSDcgdOOLs5e2SajrWWBoTNpbXMuBX5aZGZuzKPUxtebXIyvOyHfVZ1rwPyHM-0R7bYWnAfiHk30gHetHREuTfF8iCg4iQyXGKdUhBmKBR7Vb_gGtdYFnr7a6vtw3rgPTcEa7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4_NylnA9Gy2e1Bn-c-KydbD23ILeLkSF1_f4ujQQiyJkm8mj1rV73qndwEGZ9bDc8sbaPfOQVx8yYrTZSRTXfXTXbyZyGTk9JkJHaqjU1MljJPbrVb_xXStIidSCTwoHSfSWqYHWJK-QL20zZ790Zb9IDl3TlatRrLK8iFiEOZ_SO67-_Vuopaf2hnxBtZLRtW-3p19YZ3VqKVSfd8xcNnXRm48ZMMjDJz2KzP2LQ8Q0pvB5XFWlG8Tw5bJmv_Q8RuOdoBCOWOS71BilYfMMuqajRuAb-gGo__G4upqZmzaBRjlw8x2mUaNRgTimY8NL60Jn7Xx-zT7vmB-ufKGxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/milayFUddCm2Rv_z0H9IitFJiBodVkpqjpNzVKRF-HHqcfXsDX8xIpOV_DrfAdl2vsuZ41C52lbsvylA4R7fEsAQ1RYZ_r-ym8hGF9nTeORYDjKRQj1LA3glH4Uxtk1cmYC3p2QWzSTaH8rW_8faHXK6h_Oy6Yjq5oXqybOjYvkWI-NYno6T-Iv_oFD9CaMujpbwhg3xSD1SJ9ifQBK1bqAu5vLcaadzhBXhnKInNyJDlzGElU9x_oRiVWptIG0aiTyLE-p_2dto9hS-RguFHFcTHA_QhRm-5UWwlgjGejBpdJ5wl8F_TRZ7mjBFvQZXGQIMdhUZn4J8XQccEwX5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5b6jxB0QNakzk5F-U7ts_fhbsF8lATWUkf5JEig6rGCeTk5lP-IhqzlLpSnQgjyeXQvwsSFOKc24kzGI2rr0Bkig2PuYeg3yO1F2fMzO2i-3B8JzTqEElht-Oe615HbL4z4ka5zFPbqHqtMCqfqnlHyX4NGIi7OpBjXlLpi9vQFNNPLXsA4HsMxCl7O7ZrD8zI0xOXP1_YnzBquVTEylxKMgvMAEhZf1vDvuDOYRRiLLrbjZR_Y6S9A1dKr6qMTvv6-GCpuTAroD16Z0xNTXPqA-pLjH-KZJKG2UQ_1JuoBObFyhFd-BB7IDR8qngAlo2hhNiNkCPpxDV_LxtWq4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R243Sf51rHXvz_g1R_YOhQjb7zntTNutRe1rSA_ABAGOHyCocZ1TBlmTUazsqgXf8_mXGK9-sd1GrUawdqTZWzMiLqktdVhCHYt5qsGaYxY7oI07BZDBOfo0QXqirvaqfkPF01fu5BoV3rY0PnNVQHylSCnezABG27z_LMlIGtMfilE1rtn4uL79aZO4lU-ZsCW2SGH_pBl3pi-Rdsr5IZINxnkM-4xmQQc1DFmjilQT_PbyGROtc1gNpJTsZTYXcLWICwprbLHEyHaA6Z3sw8l8qdlzxJJ7zOt8jzDvK-pvoqeWuYxL_Srzp56WUK-XTB6cQzTxBgIgJ9a-AOcu5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq9xc_U_RM5G55UPQMQKXVxPHy0RQQ4hrhVE9awPPzXpPWpaHP8rgMEjvzsnAPlOf6nilsI7vH7_rUOIR4n3d9rOiD5akw5IJiWhsws_gjQHcFO9gBgMkLN_3-igp9U2Bcx_vgFaQp2FBO2DJjad39ZcrSNOCf_d59YjOJdj9CEvWXf0JFmf54pueG4OINhWKrRKZ4e3CRIS_d--lZy0vmjqoEBxPxP-agDGf09EL6j8GSrgs6DdSCqFNqs7m2BM0cAo4060IUAc8uAbe1tSFhHZjPaN0spDd9dYrqtwLEkhLIAkR-u-j7c7a2Nb101e3Q0U80YadgKXelUOpJeStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcn_zdudJoqNfq8LJ8Dtxx29tfc2Elu4I6AA_iIZojrWcslorync4oMKuI0dpoYn51XXGqq7tw_4ug-P25kgb4rHl7VKaWkDuIOBCpKJ-xcEK9DzlFNGCbFwrVChn6YmHuOZWm2B1suWZN4LvWUdlPK0-ylEoKHNQqWcxxqMHF-u8nm93lJDpMrSBlzpEn0lRiSPLiZRo82G_xkuB2kXultmnRQklVqDNqCYdzOgzQhHr-Gi74eTyPh95iVf1KzyujmT858p6zsvCfG_kvWtiNZ2Y-gMW91-4bSRCwiCdWG6Nvbq_YS8ZJwAp36gZyAgg4br7cFhGo_3H366PeyG8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx_F6l2I3-fYA5C0Dc1Cf5R0A6BmSfF0kuULZ0910CQQiQFF_lKS7GndZ3XJxU6znx0Zt7P0zw4LqnM8jkKCA0_M6JICtqWdZbucLSx3MO9PM0PSkLNtk5DqUMrPfwapsRomOMXaf07TlS5t58KxNvgFPrZCO5kimI_2H1uALVwBmXRfPPSuhkDfYJ4YtmrTWdudnybqCk6QjIqwpV_kXifhXWr1JDFMFzSMRVet_zUnbkUU-RROnU9G7aSZ0kcclBZ5WokhA5iOV1SVZpJVIOcMTWV7UtGrn2vGmgyVTOYxcJZFEf9JPcxcT-3HYJ9z2MsRnPuQ_SumjPnAWS8aoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XevKA0GUPLXAHBsgiklA3TEATLTrjjqNhf70TDMi8CwMsa3CafpaXg0KMj4tu8MwUHtIEQzHF7AERDyOvnSwBZnondXFk_c_DdMEhEMuUSd6YDB2Y0C1mPSXYPddZ_P3bY-tzkDVXRBzTiHwNbTuCMhNqR654rrhv9SJIwuSyNP6t68GPF6QVh7iJurGwwKxg7ZeVo24-4vL4V1aTRFq5ecZtjWhOAcBTnj2J5ueMKQfhr7xjGZDETjhf-MmfLyFcy_TFP6-ezCS99vM2FbHjA56kqjFs4pWsyNYibAAF7bXTxKWJdC34gcPhFNlMC2kbSagKPGeeUtyqo_-NSFEZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUhizlsj3zsPDd_Nte13CL3j_0UmNoci8-UuCf-ZCSDlVHcgrn4r46hbyiKCn40PZPO9eSfG1IzGq9yavYQXMOIby6ZWRAvYl-oPk5DpPUxnLtVPHySo7O46GdnqzIRTtrTJcv6S1MkGyJW98jFBLpXZCKrU2NAsPIvqcyrxTdwmLqs57nhrw-Gxvp9033c41uycGDeL59XHuxWKrA8gzbQtiCeZT7sNT3CNBZYuN4x083uxe6DHBmfE9Ff61SlMalXjTYG0Hxv71YoWHT5bqTGwnW25lrOn3eGwXCI3Pe6tu3zcuxRUTlgPjKA6Ri5IbiaevLJQSRVbXcK51qtyAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/We2K2znNPUwHRRj1X8hrNe26SDRl4JMsPNZOgkWrau5cr3r7EwYeeDhtlh5SL5NkgKPs6myb81hpltcMt3wH-_Avpj1DjJ8a8LPwq8i8Bl0awvzziAsIDTpYONaWmCHI32Vnd28UPJds3uDq-u7E3EGN8GP-w5__AUmPLABLyo5GnaIy8rIY3UZJAZ6IEUhyPiFy4hyPXCv44oFOO0btI04yg0ZVFJQCLq4YkcZTUrF5hY6qZPLrRHN3YHod75ML-0o5o9zo1Wecxddkwe8N2iNCbtoME8AVGWG-6vETBMp9iFlHHT08d1YWtQ7D61zC1ZJcSs1ktT-fIaW1eSaQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpuBCQGC2nZ7gQG4AYJEmSwkE9Ok5VuwzwtBQsG3nFSmNmTAaCQd_wt-sux_vIQuQ5VoXYFaQparc4yI4GyF0qe_2J03nE2N0ZUnmwCOdU3aZZaWVmiY5IxENbu4I_c_CsHiX6X6jagvSfh5G2ihMqf_rO9v74DYY_7vubwf1ctlbRnzSFh7NuYesVa28URIZ6gPzz4hP5yMbIrqZvd9h_-H_P79Uec0OYqsiZAuEknNWGkKuXck29Xu02uyy5HLDc7_C3u0OT1ROCCZ02RDi4nSnqUT8rE_mrtODa0BnT9bdafMyIFCOJSxZqWcYrxVWfFf5ksQhHN_EPqHljpv6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikcjJCcXkJfWzlOqbIydwcq3UxUqZX5nt62RECJ-9ZlsMlJrY7hyhS9GDH8off70rSWR6csZQlqzhdOdZ6S-v7YThMiBOTVnJW7PKuB7BlbSiFclmDC2fJnayLdbPKszrrXSOqtrvvPcqY1YvJ_pS7IcDeqtHjFFtOSQjbF_oh0wkQ3Sam2-xczBrizyXS75eooSi7MY2Cf2WYysqPQzGOeOZ5qzTOR4i-JCwM0s3THzE033gdnr3J3kSJFAHpmbZOCRZC9Vk210nu85yJ56ZiqJ5eLesvgro6ag8vl6XWLhg4FhatQXBJh3tZ25OXQxEHm-WsB2GLbKEbKaL5yctg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksCJU6QUuXDQpdAU00AzB6CNNm2H7QRcttvoyotDY8fjneqEQstWEnK7a3f7Bb23ZFx0s1zsAoOKchqWD4aNbZeTpUrFSvv2R9Y4vYNucqdyhMPucX3eKiujOQtuS3TjicXdzvhoDiuyq879w7p5CiVm9hhWSfn0Hj86Z6w9KWsoWhYCfYz8cZhSByGsUm1h83WtpyanwHC5o9wCPtpV3RsRvLvWMWlPENIKQPYy59FWTmf1t0iFXKDars-QTq043gDPJnSc9zGLtOc6iO-eycTXrihSX8uBrAqJAtSxMBEyFWVfLokgpV0dkokK6m8XmEVRxX3av57Z_9-u3jRmlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmpWV63piPamV-BcjEDX1M4BoXNuiOy-5Wl-H6t-oWN6_guE1erBn4Z3I8IChg2z2k5bVMeFpr_yafY4rR3mLrYI9ndx-KoHbEqaKZ7rZ65LLcH6XQ7BH3c_vW8oOblHgqMKnGP2L2eIJ4p1epCpmN6KuyxkjvjthX_aGsfWin320k8PN5fJJ--VLPIRG9zYYh-rvyZwezApNut1ao4rERFk3xEXo-SxeBqZVEPh0AMxNCCqGsmgxjb8HTuxnc1gqkec9q8Q1FuVVDMaI_Cu5-QEq0KW2HgRcbJnFyvCoTok85-g1Baki1hOspoKEJ6xZyP3qE3CzBSifMJVygeEJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwXYBN84mRnnouwXosZ0d7Y4QaF4QpvYYr0qB6ug05-hItR9ZaV2eCZOfnyogmlrtRipqlHAD3IXrMxPiG1wJLv8O7tVgG-bDdGqjGF8N_cm8HdVDiD51Jom7hvhTCp9gt1QhO2wcOBPynt6WNBI1DedZ3jywnrBG1io3safz8tYf9_uVSJzE_W29UPN0Gu4cXoIRKLZ9GzLZHJs_bLHNX7eEDZ36EHnNiO4M1AciFBJd2a0FP8y3tRxvl0-1MXuxDFyCELqR_XMqi8tYCC6q7rEIjxuU8A6RuOX09tZhIZ5MLQj7Qb3njEwO23pqNS3lGfQDyGVFDR8Nk3-6M1_qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=CA30kL74bVfUMR3zIy-cqBGN2sy1uDPmznx_fvCGdArwMcHSPofI_EkHQwQ255B3XsBQ7fjBGbcBNXFZ3pHRMDdYdMoV2qtgKy_KvELPCUXXhjwcEEUs-aEwEHIbsbWQarIqd8n6TQCKN-NOLHTyjo5xZmxAORv-WNitH_Qo5MeCoP_0Hf5UcDmU5v-pm3K-wI0PlrVhGMprtyM0SGoeSGgV7bweEPz2WSWwwuvtkmmPjEpCcTuwixKGTk_0dOGwVB22GkxMEIBjwxaqzEcnqH00wvV32gZ8tKO0eU2-ofsgMm9bHvMhR-xFCjBmZuGp0eJc1KRnJgZ0VaDmoivD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=CA30kL74bVfUMR3zIy-cqBGN2sy1uDPmznx_fvCGdArwMcHSPofI_EkHQwQ255B3XsBQ7fjBGbcBNXFZ3pHRMDdYdMoV2qtgKy_KvELPCUXXhjwcEEUs-aEwEHIbsbWQarIqd8n6TQCKN-NOLHTyjo5xZmxAORv-WNitH_Qo5MeCoP_0Hf5UcDmU5v-pm3K-wI0PlrVhGMprtyM0SGoeSGgV7bweEPz2WSWwwuvtkmmPjEpCcTuwixKGTk_0dOGwVB22GkxMEIBjwxaqzEcnqH00wvV32gZ8tKO0eU2-ofsgMm9bHvMhR-xFCjBmZuGp0eJc1KRnJgZ0VaDmoivD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAUbgj5M2vzCcr6AynSc50pESSz7TV_zcKz5TtCe4l8AHc8BGOXSe0o1v36s9NBfLD1hciKcF1qz4RoVvMM8Icgs-u-P2FL0Ifok-CZvjqDr6V6OTKl6ZnlwhxQCRUnzxP1MGiDjnXSEbn80JkCWB9MzmamGQ5Zd8HC6RrFsrLaER8iHMSf-pj9Xk2LHxYE2mlXyOampdZWCfMw4RcQr_hE7D0mvUHTVr55WiEiO_r-IWreMVQvRyNWyC1Zwfd73R75_9awEiMzRKJKWLoVvW2MdOm2rG64gLlx-KDh0B5rdcfoIOWnIW65WtsxMQkTS_st81t4P5ZsP4TLpWaegRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg2mWABtOoFtEdxBzo0jKuiVfP5I0KTHjc5FvLxM59-35alwIHRM_nisPVHvjCfpTSMXGPDiO9hP65qO_iAjPOXS0goi0qesPPM3bBHpq7lySqzbEUBcxtXlT4kM7LTSJg0KLCAcV2joFh_bkUnh9R7q0IXdM1ydzqP15e7BWTTsnuCrxZC5idVJhdsCs6IDgOTklN4XH_T_rg0oE9qfFpeE0N2gR9HCMYk-JBGvE15Jwz9GbmMnd0dHtRikSwJiHow5m-sXt-4nx4vve_p8uaT863eILjUUzUUxjELudu_mwHKVhVz3MhZN8pQyKK-idFc1uCdASUEKuyyDHQv4lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oesq9jGsBqlaYdEX2PqENHyC88VSzu64fTOw60FLXyhh3v_YlKc4hs-aDt16A4kCVC8Yadu1u-CulB0PMEEMuXQzl6UwZ60nMFDBrq-aWFMVPZHG6Vj-7hKx56KM7crGivmYDLN381y9HCYpTTVISKdLx2iqQxHuIUB4-wK3ooMYvNQFXRHPlFgP0JuLPKKNlbKexsUbQVy0r8clC_60w-aBR503cCSKfYmE6B-Iw51TR8JMZzgMKwmnDTZ5OyrSvBESDMHOSGdkSfo6AwLgk_zq6WuM2JxgJfumuRQEECYhuF52O1N9ZTD47yeDYV5rm8NmuMHCGfyRDhKFuJdUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghNjHCucFddPLGe131gdD8iFFjgWyVJtxAbPitKn22t61pQl7uU4RVRUSbQPK1ETEa9i3V74wYXMwQWY5czLClroZpSIFDSM9GvSEBB4JoqzzUj0KMDq0XoBjZTI2aQMKwRdSHzxKTF3SN1y1TetaTLgqjzD4oZaMNe3GP49exmMwo_qW3DjgQOPl_J1sQdTg5CHV4QLZ7oL5vxfRU8tG7Ak5aEkRT1d_Pyytpin7EgsMnO5QDUNacy1czauJzpqm9kflUZZfPqYUKZW6LtknzBwz3uo7cM3IkSQiuoI7V4OjiiYNc8DgY69OuoAUcVoEBb_RoNYRojsaXXfY6EU3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6TnVk8V5KGJtSP1CyS_SiRqibGwSaoKXbUv1WmZV-zxtPkpdHmp3vhnDFdQG39b17Q-cNuWZzuJZIdWHeHi0YTWesuSh4jmsYWrdOD8mAj8dLCV9_3Hi3IXlkhJBdUmKwaK8wXz2Z2J9BT8aRY_e1W-0zXNtrlAdwgy8kMxRkzpCKD7uc3VLboyPrEfrOthjfDFS7Pu2pU1PQpv-OMu6BQYAGxRVVmZYOLnV-v_T27W16RWMFkdn-Z1mQ83VCasM5quahceWIdf0SttTNhdTVK0Lw98wvi7jb9HSf55oQ8lQVoR4Vz-CgsipAFn6tgrQhRLenPjBfv-AOt7RyfT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAMPUGr6y4q1LSSEF_qZ8iV6imdSPi-syDyKehEis7W3DTm5yhG2K9-jQVjgKqy3CJ99f1pMpukaY38Usx6Y6rXpmYei3YOJBNYjWO1ae1LNRBYPZyjJtN4kyc6nIHN9FDxvH0SFml6Df8pHZRsKIJYV2HLv0FAbTGHgy1tr8oS8wPGy2QXVJDxXlES0yAhwAdqbBQX8MfgyH3BpbrS1qa4Ym2b1jZt2120J28X17jZjms-S0WrGUBgwIgj8GHUGGAlJq3z-rSvipEzKw4uztirF5QgTKEM-bAKbLqs_nC5LfaUzN-XPEFTzwxBACUHiqQWK3q13M2CZ0RBVtA_w3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kbtw_1pyLAY6GSLvB8US-E8AQZhRXcT5huDYCZ-tPFDDJC32eezMHPgljJF65puopeOrcSoZG8uCDfAAePYkTafnrAdNkxGCZd6Igh53l1HLzk20OnSPFGBPZn8JRKoOdTZv91oki-UZ99l_uxWj9FKf61rv-VKimQWmgW5AoIXhdkbZBw5medBwzlb6bKSIGUtgCBQC0oCqis2qi6IyEFEYMDpj4jiyxskBW1tJmejRQVWKaWVWAqoUW3V8siuR3bwhlR-p-YYTKBUYSE2zY7jWT1DswOcSi6l9SH1VPrYN5Ce3F2SUn1aED2XBcuJMeIuu06oytTyKzyu7aSGkkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rE3Xz_axWvF_-_K5dO4_Qijkr_6_WBwZCZangadyhfPmxRaWowicMPeaMKZ_CYvE6xjspngdrlbwpVqJK2cTooIlfy-Me8VB2jCSClNekqB1RAT_CGXde39oXIlVEcf8JL9ZiHEptaIEXuNdt_fbg-18jBxU3SsnHk1yOTeMT9zAFXN5kfSJy0iYz1qY3Xk6lX7zSogTvsP62b-DPmQB96kHA08ZXXntUV6D1k3AWrE1sUQFpYQQg7epIfcHAZQJXWNLrVrGa8flo0y8leKe0Bd5SVkB3TWsB27900Dwkx52eCPUFFlHU1oCd3OvAgx_A2gcwL6MFEyCVGe5bonA7Aq5dCne8WMIcqvuSWyzOxVPXLV_VnapaPTcGBOFGYeSQQO-ZbIM3b0JVGBIDkW-QRZIs2_w45RZJ02w0vxO_pZAVmQlWofPs_L_Zeow88PBAq3tfwk2VOD3Cgzf3i32igaWPxwqHPWc1wzOg-O9MQ4KpZ1yEEkCpjVZAKSjagFBLzWedusmGpzeiVM4LVSci3ZlZrp4EIZnW8sPtq4M3_jCDZT32Jiu7ajcLNjBvxSJPB--FxKLPZ6cwg0vJ-oD_d2_SyRoeCqnUi7ohKxIbJwaR_IA2yQxn5tav7ns0qCEfMOhVmVqYgCeMXeAgSsxks0BWDqKk0ZWx_yalUuQOH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rE3Xz_axWvF_-_K5dO4_Qijkr_6_WBwZCZangadyhfPmxRaWowicMPeaMKZ_CYvE6xjspngdrlbwpVqJK2cTooIlfy-Me8VB2jCSClNekqB1RAT_CGXde39oXIlVEcf8JL9ZiHEptaIEXuNdt_fbg-18jBxU3SsnHk1yOTeMT9zAFXN5kfSJy0iYz1qY3Xk6lX7zSogTvsP62b-DPmQB96kHA08ZXXntUV6D1k3AWrE1sUQFpYQQg7epIfcHAZQJXWNLrVrGa8flo0y8leKe0Bd5SVkB3TWsB27900Dwkx52eCPUFFlHU1oCd3OvAgx_A2gcwL6MFEyCVGe5bonA7Aq5dCne8WMIcqvuSWyzOxVPXLV_VnapaPTcGBOFGYeSQQO-ZbIM3b0JVGBIDkW-QRZIs2_w45RZJ02w0vxO_pZAVmQlWofPs_L_Zeow88PBAq3tfwk2VOD3Cgzf3i32igaWPxwqHPWc1wzOg-O9MQ4KpZ1yEEkCpjVZAKSjagFBLzWedusmGpzeiVM4LVSci3ZlZrp4EIZnW8sPtq4M3_jCDZT32Jiu7ajcLNjBvxSJPB--FxKLPZ6cwg0vJ-oD_d2_SyRoeCqnUi7ohKxIbJwaR_IA2yQxn5tav7ns0qCEfMOhVmVqYgCeMXeAgSsxks0BWDqKk0ZWx_yalUuQOH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOeKjUlSbpU7v7zld-EY2YUdE-iQOygTA25R6fz7UKgwmZNc4eB58e5zAcYmfqEqCGMmR8zrLncqTgdHoJdc8Ux_t518bIQemzfo6ScpF_dlgRdNrpUMkMKs1HTKqJLQ6Z1lwoxdocpvPkCELO5Xn-GyUS07FdfN0NHZh_tnWvlimDip97CzuzMlpBdBb_hpKBS_B26WO_ZT8zFGt09ZUXFpoFBxkzwzkJhQbGs6TLc-n54xc2BW-__D-cmQfV73xz5g0cYIio65aMuh_ZNUzKqBaxNok1aWMjnEooHRTVb-oZmcxZl8bNxUSpKWv1lP7wG7IArA7HYygY6xtaWAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br9G5J-1Mo_FT9fj-3ELCudhIWmEwc2RvtdRDUKjR1m6i2knd0oMoZa2pf152XgjwPDiQrdBA9UCr8vTxwLoIyZ9eweCW2xQ3Sei-cnULuXmIOSXDsj_QK1MOh4CPYBnWg8au4XCb1dlNbSEwZ3wtzRjzYqHrWzhgvXfQmFWTYelhUwFnw5OwHmNJT8IArjoV2Rm2E1rlAmsonufB48kDixSQzh5TJ5CT59s6k9LMk067NUGxcdgFZC9Zg1jN_MksfSXW_Iqv4GNtR4iU6szWFDUP3tIUO3dBYpyJch6DdwT4TETm0o_DWuEioGLWH4xOawlw-NlpVMa55cQqRw99w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSpce9YzHApKamgG5YEm9ij1OdWbEktQVa_fGvGefL7_ji50MFHqIGpRmtW62aFJOqNmRHpOQeo2_fyhgqC9zlzag7HKXdfsYIhZn1rOlBoes_m9GPN4y558CmTbpAs2J_A4BsXkcLAej6juPt_qpaYjl96fIG-mViHAMoon52jcbSIDomjFbd0PxupcAaAok5EoJmxvkXBfEk-MRZkYw4n3jjVwQHDpXakEQtL5FgONgjebyyk0JslZJPdB9xaZggSZAvaDwizkJXgUQ53WarrJCQw10npv9WUcZ4WzbjUIl-yAVXWgVwxZdcoRyndUR2L3KT8bv6fBpqPtYykW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJDjJsdbrOZ6luGBeDhGwusJdTY42pnMy3OvY8aFWeuRPi0OsbB5UJ1GmgmrqkF9sixAf0YK4FpotRTXANdD0CFoy9boERF7Wcd4WxkFllpCcf9X4xjl9kQNgkL-x2KRjGEJpb0NixYrM3jWWAlRvEODt_1zCV1CO3wpdo2MDGbnZjK7qqVSrrzeNzYePXQcJh-r0B5bQApU7-ICRBoPVpJLIVyHN3OzbekqWg0z7u-YwmF24cFDaJTjFm1ERuRUJn9NjlmLPiRF0K0HH6UWfd--WD4mJ6a9hrmwBZDwlJ0xyRxfQojkJcUIRJFXfR6VH5X3tcVhxiWbXCLTCOr42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpqbGjNiXrmXw0Jy4McRPl8lzasyBYgEgH_rwX1PUdOfIO5MFJubWHf1Z4HLn6se7zZDSgpUYd9o0LeCzrLxPyAU9RmQQvkGoozbD244xjF93tG9LHUjUG3VF1tQD6qeD4iTlpgCiQL6optxm9oLkjq0hytzp2pNBuvacBqUnt8hIQC3q-GOHDeZCRoRCnv9GmfMeBZDjoNwLg8X6T3WmN6f7kuEB_hKim8Q6fxZU5hQasCDYvZuJAZRJjlm6uvmvAcLz5KfbdupN3UiC5-qIE-sevUlp_wVWBy5YonM8hWK4OBTpcRWOK55WJbj-Wh9BUrbOugNyxZ0YvlbSyQNGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SU5Xhbyqy6MysaO2GDXworBHwENexHDC_vuVaqB1fQy96yhbo0Y1q9jMCKsq9awpO-WPzogyAuSsT5KbjsnxAvKQz82aW0HYjKvPeZjJ4SAQVwygy9E8Xryu_jku7Vlkcmgt72vf75e1YeDyNoIJPnZRrBuhKro1DoUraglQXtxSILP-F8cVrL6AAkiphZVx5put19yWLCilzzJrN8n8Fn4GqZZRV0_fxLpZhbNAEabgECVYlGNpvEu2SLZWIt4IUA5msLCjSFN9OdLCj5YazfrzcwjQpdsZkKuMblu_rW4ZgiKgLs9Y4OB_CKCTx5mv96fSHAZJkNo_XCU-7wMFy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SU5Xhbyqy6MysaO2GDXworBHwENexHDC_vuVaqB1fQy96yhbo0Y1q9jMCKsq9awpO-WPzogyAuSsT5KbjsnxAvKQz82aW0HYjKvPeZjJ4SAQVwygy9E8Xryu_jku7Vlkcmgt72vf75e1YeDyNoIJPnZRrBuhKro1DoUraglQXtxSILP-F8cVrL6AAkiphZVx5put19yWLCilzzJrN8n8Fn4GqZZRV0_fxLpZhbNAEabgECVYlGNpvEu2SLZWIt4IUA5msLCjSFN9OdLCj5YazfrzcwjQpdsZkKuMblu_rW4ZgiKgLs9Y4OB_CKCTx5mv96fSHAZJkNo_XCU-7wMFy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8d75Xff3zdpjcmLHylsS-jkoa6zba340NLZydV2fcEo5YDOyCQ2zdvToLp7kuj7z1x3pVRv-fYD-7bx5deG6DBlVTF1kbacy_jqIJ3z7aYhE9-kz-jMDOX10rnACvOEBGqM5m7a-pwFSO7KHmJpHhEy74S6i1W9HdpdHs-X8CODBPR41Ugnw25AUQLLaG_utJ3LWyeGTbt3TN-dIYK_C4A5XwXKX-3MRm6MiTB_SiiCv1YXgrYephbxLnpvGkpP2c3T7MIv7V7IVxEwDY1nvgq6WfjasGfEZjp3XRzBtMyUAC9r_HRZ9bkHEjv6WxJgZ8qsrR54uSyu1uYUsk3V-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKW7zF53MvGtIKw7Mg9_KuUw1ZAFs5kVZqgOYvnAL-B-f-A4w1CFDT0SozNXF8CB9I_bwD6P7rOyO7vCHdjTD-fIHEFXKQp2Rxu6c3sguC131YP91d2H2lluTWyPxua5nCMdZXykbZqPkPskrgfCwW7YLKnDX-eKhqVrNEWtE5WRMjdnz8Mrz7n4v2VGZqdYH91tugDdh0GeBhfyCdSKgQE_-QU-D2WqwL5N3NGBWVsXUrAlDTXyymHAF2kt0onq3RBtneAsMeyLuTSqrR7pUzw9gX69Ko8rwR7pB7ZRBL3aiEyA0laYdydWqXz7zIL6JiwdyeEkcF9JmNC1Vd_HLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbnoCkjIryAuo53RswPQJpf6rdXLmF8_18nvy16In0EoPEDXWFEEAibKxKj5N0Hg0m4JcdA9c9sNC0Y5BFQWFtgcprzQMqJ9yl57dFVS00F0nEEAwCucwK5BgxhTi6ojDVOyd5FntXq-uYY8f-jD6ZH4pee6LyuRUNFaw0ShscH4KGA48ndEIw-95hX0ylhSI2lpQ9ih4BVRKYoBBBB8PL5JO_zyhM89_ASbz5YQXiHg-BRMVcD5hIowA_APJ110_B9uaiaK9ldN9lJDi9uLCCjlUNz0qBpmDKM8LQvBkqt_emJGuU2sVmPBoY3VNXlHKi1Y4jMrHo5g-ZnmdETkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Na86aHPl-1F_Ak9svLygKw4vedSY7gwH09SzM2WLt9z5RlqGUt2DpUETq-ek6hSYRzXeS6-qdtp8zolTU0BQ7T0cFecxpysmfAq6paEpJo0WDR7mxIMZBwa1RNFyW9b-RWvlL5DUrWJn40shG1X2ZiV5GqcV5grzDG4QXKHBCNYaW-NeImkiHBX-anL0qMI67buH8NVIf3q-opIYGpbOyl0ZpX-7mlUbTkmNTOCfjj8JKvWcyPJv7hZNSewXJCJuBkms_hVBqzzIQVv1WbmfQWoEUVaQ7DU1-uwl00-PGTZITxaBgJ3ebMwwpCi7vmG75-koXb2JeMCFLFsFnfRlZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nk71bb69l-S4rImdc96COtf6Grqff9qO7-klgv6321lS-5WT-6XlkqNHzTWFqVwK_toweDceNFEpJU0lg2EtZZomDyO_oWxvO2lc1iQLk8Ew6PsNPTXaUXRfn-vMYO61Sisxyrc0A4NQrSPmu9-jnVlJ_5OjJ-D3Dehb_n2Ss3gxE_FFxgZpoZZffWNm7tP7gwOUVNyuGcUahq9uOSEpw3j1Uf5G7ON2iaXuUTMDcdwGDO8KwRhZNHG11CqdeW3wSPeNAWXWcfWvg4787YJUiGzUcT1Iip05alXAclWRPYc9ligpRh8nDeojwCFXgislL-sJxvRWCXnqM0IWqGxsSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhJSx94NSualLvLfcl9Y3nF2DMyQyA89iKW549iNRqntxQVQHTMT6PWPtg6HZkHKAXeWDnXO5MvCqiJRPW-DNHRBdgj5DFfHbAJ88iQAK_2n5UHDK4OJsNpT_dGKtQtGcKLAnl-8BkLIByIEVPWlCrCPX0ZffBQZh1z1m2yYEgcej9vD74X1cBkgniBioVozFB6Y69zjXoZHK1ro7aDWitDHLKfjzHVBTee_OLwt0JGUgl-TFCaAnPzqSkoXucS5h3VXx9xx2K5xIE0_xaDi_N3YDGp65Pec975y7CLuOMdDl3FbXM5BSh4hlFcSxJA3yw7ZMPwXUXvfYDpQ9duhtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Rank Math v3.0.33pn&1.0.111fn.zip</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/danialtaherifar/801" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
افزونه سئو رنک مث (Rank Math) نسخه 3.0.33
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/danialtaherifar/801" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
