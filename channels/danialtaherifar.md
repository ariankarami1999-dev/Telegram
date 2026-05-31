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
<img src="https://cdn4.telesco.pe/file/iUdiKE3lW23jwJx947hrhyGEGnxnjO9n4Sv_1wTKjmC80Y90XHXy2IPGLO6GWBMVMjFU0ZzODydWNI4tHcRikbJ2Uq4K5tmMflwPp4MuU1g6GwXNicynsTSMP0krCUk-68_x7zDZXQSd4f_pz7Aw0gLqdcUxWDJTViVtQ7AsYgkTsAT8D-Sbpp2ZSQQ8CTTns-itRlp3kW6u4ujLZGPiEL-ZDn0cRixAMBGjUtCixWxFlyoj96Y9LhBP3CuXT9y35UhP9hfK7GCwYVFFxIdU3ZSYr2dlaAXS0Qi_KxLvsY7glcfhmJdHkASw7w6m7fMKvJ7UXlQK4WUkBHI5U5qoOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 02:21:55</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 471 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 576 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfhUGbf4cCpRULpwu_NqxE1HdJnsNaIvlBDMHgjUKUpYHQOR1vsAyLah7lDa9fgRiDTps9E0C0tgxMZk-mlodlEWpa7-mcgc75KH4UzTsKF99tYBM4gQ-yGEK1tthaxWl3FgEVrhzNxaHQY3E3gzsaoGczpQM5YBoZ1itRErFaN7475SDkbHbiFzbIPPZcvbpjpsxp5wY-loIJnoU5fbRkgO2wcd3uYUX2_6ABQ77irWtTM54MsiTS7LuTZmk_xVs7JlpEzS1DmFYJgXZUtdKzBs_xZhl5PYEFWZndWE7EcDB5VMBOuSjRRA6EE3J0ZDIDSYTXhck5zHPt-n2bQZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNh6PrN5ZJfNsNVR_jSpOGWtSVgjNbk5Gt2UAlH0NaHQ3dKDOxH8KtHT5ZuElhP0FV5gD7SyiOS82f8oAnRWXX5dG1E_95Bw3RadqMlKtpC4CZC3_XXrYo3o_2jInc32Lv6XrzMTrNX8VenSSy5noo7xyaQRjoRra6e8JyUPhCzS6Obppw2LZJKjIyY1JIkksKjBKO8kLXDHt_skqfpPdTwQ725BC2NgicJQxHfbEN2blPI0fqg9hDj6K4LeI5syydoChQD8lqaAXIMShfXhwNXtWInrXOrzMZh6ZMgSuDcCwsLdDU2xA1VjfZrYpLpIOo8tIJhj_lhgCLLH7QTSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugbctm-E5ii3Q6sOWAAtj5Bq-QHoIV6HElOunPhZiyPCyRChYqjp_eC-3npKDQ7StgATE_Qo_JcTkR74XnIUtFC1Cvb8W_tc9NCfT34ekIS6qch7tKM5rI3_Cp6qZOJx_e_ffhyacDARWYQpzjV2X3vUqpQG2DHrfVSIwciD1FkR318T_f7AsHHKimgFwmFH6RVUf7Lh5b82X2hGNxn4dpGGfdn-LERrb10evTabZj_tL7_kuhYrXmAYJHamOqzRMhVJN0t5VS-NbE3p7rzVyxaLdGj5RuxHsJuXv4N9GjsIwjKBYTV0S1PlfH9IFKMavgzlQ7DStumugBHVjXbMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAU8POccBEhX8KvqYRlO56zTp2dL-1-JUVNC0FyupF_VpMYGG9x2xt7wIabXh8GRQMvgT_34tniCDB6Qvma5ljxD83VjRpHvczvO5XFw3IO6whD5hBZxZhkeVqyTDaxmix5tKKjMQc29EaTi8W9A1qI6UMgHGA7kjGHNpudkkY5Pn79cWkHB9XA4ZHRHJSp6_Y6P0A338BF5vwehjgwDiNKrz5tZyo9tjpIUEExj3h81vzKLJZ9gzYXp4_2yKiTzR3X1CU3VUZ_Hx0a-Ux6r3LifsfR5FAJVUXkCg5Ly917IIE6MbTs57JdOSvI5EjhpofK4IntvwJZ21uaY8amwiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmPw9bdh4fbw7_JRO8QBdtj93ejghlhpQ-VTZJn5dxDwg48ccJfGzoqPjMdvn3X53z-eB_qKTTApwJExfTh21jKfTOi5qTHHGXBP7JQFvslh6DLdINN6n6LK-CNcMPImdcBlz5zeuJzZqdBmD_DvfKsN6RJbCQotLx4y-kUP97ZG3Ayeromo1Hs1jNtB_hLOLQ1oSp2tjppdY2cB9IVYAuzj0LLFy_LHlGO8il-DZdHBdME8Opb6gtnGtLHBZYAlQ3isqhsfK-Q8YPWj4-MEsv6ynSkeWumov3Qpn8M1SSaAoY4rFc5PI3AeSQpL3ORZfl-Jxeu2LAmNFbqCHIkC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 775 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC_Msv8qPZnOoz2_OA_mdYTJ4ez9kxzmSqLuJlBdH4Z5L5l0ASQ68thgpSBsBZMWxPSETHOLO4fzVfi-db6Oo-sOkWrgmdmEi1DtMRj8t9ovLliRrlh83pIXNFfFuIWFbna7anT7JojLpCMl1bOw5s-ZwnI6_6UqC9dcNpnGhFiw90I_E2h0afvva-Txak_SOKE1YCAbXswtep9T2Bon2rSmR1wup4k1jh-ZK_OzQPkRuRdj5J5QYNv4dEnuKldzeqQZ5MuoXDTnzYzXtOWNZnWSkI5QfD-kfsxMv4uLrpAFpgwQHIGc6oABMCLnTFiihCjkoVih-VBytR9HPYz-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/We1eKpgSL_Brq80s_GDkfs6-2tLqQ1CGMvQ9_MtosbWPwfAXBG8tJ74uC8cr8_Z4j1ULi2r_OQMRIgM-10eBNRPgk22VTriM3Zn3Wd3gqhOvWYtDge0GO4EGCatwBQDSheojVKMywAc45YYfObBUuypn4Im044QxlNqdN7DtGyJFYf5Wt8hIq66k7x8xzaDBl1KGtWazB_UCrZudH-BJLQFlIg5Fb8buX9x19FsB9fHhsbivm8mQYXRXD56qHO7C80whrayeVKkPZ_9T0XvIwQGdPclWbSFO9OMVOB4fcoNo_YvLgYNl0QJaEdnzI52q7_zviko4GS4APB-F_NO9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceO1J3vqFQxJjbd8GYOKxKDKnz3NQf85SHqDlt80Rb2eBYf_TK9qMMMznSW3FTGtTzeA6Bi2mhdpN5yzS9lCyqMG2iJq9zd4Qk6rdsvK65ZiDdMjyAvelhzUsVvvAHLUrHYfsjEK5TZQgstnonaRXaOm7DMDiMl09V4kg2GrwI6vp6BPs4oUIBhjanyOn7EnXWs1yZ68XTmgijtLK_klxqd9YZQqXSd2WjqXpjlHLb66c0GW61YVAI373UFdoRX0aPvmorz11WtfM3nKHEa6YAjJ4Re503X_faW51DOky2Z-IU6tIh2WlCES03JVwlA5eoWqWffCSAygjE82rWJzPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa1tUHpyIhos348VLeP1Iey8Sg1aRgALqAAw9UowXtmSlc6xUaoS2v0Jx3hkUEeBvdpf84-jgs-Zq0LrZzn_8byJD87rjyGUaC5-tEo8eemeuA5r5uvgprr65MZYMS-ALIs0kn0ZFeR4TE8hq51gqjIzR8eHRdn3ue57203afeswYiB0w86gftUxoacHSiAbx7spbRlakfGAPQ_1VQwxlCqJy_Ldj0DQoiJYYFiKxVMlp2FbK3wIsUUbm2lgYeHdsea-vExxjyJfkYihmxgltZAp9npKTXuYCh_aS0yvWyOOY06aLyEn_i9H92L_cBMqIzI3uoKgl7rCghf1bD0JUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 937 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzZqiSN0rt8s6h6NxFHB-0l94IrbOmD06KHOJP8bXiEtJ8ypKKZMXOo7vFNRwhNP7noTXfJScQIzWSeit7ebxgfeNOozf5IPtsB6nM-Mpm-aO0jtsEY7JdbdBg2GUKxlbfoyEFN-rzjswAc5fBNTy-yW83jksshJDkwtGDO-L1rvqaDnzsB0eGh7jjrEogmy0AzENz7jpTBYtUx9jUroJqh1Xzu5E6AiRA5xR_XXUqljJOxkhxoF_DPe1pdrvoK9RbWWsiU12yjWMAh0GnfNC1MGuy9S_ggokO3u3q-7M3_Joq292VQ3mwBgdmTcsp2a4JtDfJccj_AAuyw09AnrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC6tolFPRfTDcFIfwQ331qKKlaos8VhplyF52vB-0kypkXZarSGnKf4W3YHX5_E2z1NzYLIkCsv3iwj4FqXjTzY6sqt_ZR-L8PIipi-CXQVYGEuRR43sirsJspwvR_laBEQJbjQjQXOO2-MN7rj4mNS5uMqnyEEFr8skMXXJo_-UjrdHecXiNdBbCF1TUHaNQT302EiH5N5IGwXazuQqYoPnV3V8BOpPR-vY0IwUZPFENoZhqlV_A22rwpRMfVcH61MU8aS-a7qqtE3GK9S8z6f6DDCyl4PyyChYxyM8P7zqcfS9ykr3v3TBbRXn1Wk5wEsKPt-Uy2swA4tkok86Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 673 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFW1PkzZq26UDaBkxos6wQ1V7atp65HlKxR9hImvXhZcwS1NKHjAm9o8KfVnULVkXtjgGazMMAnTmyCMBGPz1IaCZrvLiTNkP3MfPNt7TUjNyoebq2ieCA6RZhM-whsk-gIGpU-EXTCfaJCyyRVFz1EKVJyWpyBfb5MB7QENDqaDFOJJdAymRl8VUsjywBSGG6VQ5-SswImTpZ25Vv81cKvZxfe1kZBq82kte8DF8mxGzhmjfFQwuGXeFkmOWxW2OAjv35WkGD0Jovnmo3YfxwfVL0tKPI4uqCo1KLBr5v4lI8dlo2xOPKGfYIybApa4LVx6KjJFbBEWlGMvyuDnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvY_cg35_Xsp1g6-xgn9KGxgVCeQ0ifRkw9DzAgLYsSBld6WfFoYHZHdBEpv7VQZtfT04_VaoUMrK6w-7X_kCXAz_PK3lwm2TVe4A20RrsuF_Q55wpdwwHKT-pCKiEM-FDVplE7DPza6l65vHEdOro4lNS9YeaulZVM-DL5Zdn0XIgeTWksvyEGeKfUMHH9ghOPbs6HcxevpTl_Mz0SNfb-4RlLZZgEeiuB9IV0UdwG54W1LcHpV9anCvSsNAwXzabqcC2HchmgzLpHqVtk8ypHr1JEyABy6Qenn54Sdzp6ugLhJu738V9g5Nku8jasbJl7nDa7y0WwKP6Cw1G4KuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo0GTjdjQFP6XssSErYYV-i9X72gzxfQe5rPZEaO-xJ1ClgQmGljUVTfemPyRf9_zPGzGWfbF2ruMbEK3HqL9trpeWPQchvU56vpxBPRUYenQ7gOwC2ZOL8n2QoTrYUCdHT7diq7jU0BTc8cHpH4EU9CxZVcErRzCp2yjogCx3HDv3ePu0XP0oX6drf7gQz3IXwF4lHsaw_K8QiSJNUVzbjXdl_ZxQDeTKarxoNJYnNTr2q51X_fKGYMa5WqZwp274uJIi0z1hc-Os1zB4g124EjKu7vUZeek1YbFrlMlM_337lPRh55jQk9bQo-HGR_5M0ffsspUGeRi0s6-fD3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxFJ-8cKSP-1jgKN3oYm67as8HhpFqQZ2qnq4w8W2WZFRS_fAwy13DeVsYvwLXB2wAYWgMU4ZG-EUHDKp-nrV4YdIJQTIYWGfsLj-sZERvGaoWgkcj9aqTyr39zhcaRreLU5Io2FmZwrSRMjxwU2gA1HFFBUBRzypmLQ0b579RHI5vEH2PjeOj3zXRx4Ntt7230A_IGgYUepmLSd4HXcTudaBnOb31n0QglSnU2UFX6G33Qn6T4KGW7V73NxAiTySAFm4BNeU-t642ZgpRjixENNYW1VooZTCmn78oIGzMBsYvVjcXDfXycl4_ss9M912nfAbEMTauOyGQaI1uF9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWuos_mTFg7PU6onKGBG-xKTzgQXq80h_H8a66L2kvl75xBZNyYhYC-7jtCiPltMwfvxniPU9pjWIUKXRS-MbZALQg8IZAId9IX2-Vg-ptCJ16wMTqENP2kMTxvp9_714Fj9LNepqyUGZvmQjz9ISMA9n2oHpBP1PktbXaShuMSE6EQ-CM19DONXSC6a7-sg5hu-MeMRbKmBKwb4466tFD-unC8tAjKf6xvcAMxX4q312_Lbs9LgkIIFeVnro8oeA6Zgstuljf5iuH5Kg4fGl-mMXIVLXN1iEhOgmcGOPj7se7MWtiz7a045e6ukpabSRuLt5hsusOz1XY3O136r1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIm47j2H6vQf7Mmy3QLQY9szdItaRdLQC39wcn1-gER-01PniANWFvRMEh2jqTCpPFdyZ7rXR7yvS84i_sd_R-v9nVDWCcP2FJ8dOws8VYOyesQtCUwzPwdvelQo8_CyCg1a7q-I0CxO8aZGvHCvUyZ3Fr0zdBazRaQpuM7amOw7W41dzyRVakN00s5DcYn8Dzj1W6QcKKQAanSU4DtGFzJino0h0A4CGwy25WckZKlIYMBEOVP6zFsSslEq4qz6phNSWEWaerCcJBnPfxkbJAfJmjnthYX9t6mq8QtCea7U2wUhvdMjLqson-9ABvoYMWId3fpE8RHdciKs48CNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=bPzAebIqSQ5eW4Zyf0kQXQjzB8dKuCO1WdrVLoRlJfVuzv0-ChagEFSbeVN1DzMiKDzhziA58eUPSQWZvnF50fdgEtE0ygKC7gca7JG_TkdchZ0MmtkesoibOa90t6RxTjSNmsFKRX2eBQRWIlJhnVQuFN878NmvmmV2-LIASPoqXQFkxWZyKRT6gQEFQLuZvK4y8QZsOk0DHXtZ-VUL1pjybXYZxSr6l2FdxlZDPzEkVe5Kyv18Y2rTAFm0ZRu_3Q1zuHa96d24kYKQAG2xT8st0gI6Cs3UrnxEUTOeWY1gJUQjhFFn2aNQmKGhzE5rvXPE4Qs8XswxGsHQKKzpPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=bPzAebIqSQ5eW4Zyf0kQXQjzB8dKuCO1WdrVLoRlJfVuzv0-ChagEFSbeVN1DzMiKDzhziA58eUPSQWZvnF50fdgEtE0ygKC7gca7JG_TkdchZ0MmtkesoibOa90t6RxTjSNmsFKRX2eBQRWIlJhnVQuFN878NmvmmV2-LIASPoqXQFkxWZyKRT6gQEFQLuZvK4y8QZsOk0DHXtZ-VUL1pjybXYZxSr6l2FdxlZDPzEkVe5Kyv18Y2rTAFm0ZRu_3Q1zuHa96d24kYKQAG2xT8st0gI6Cs3UrnxEUTOeWY1gJUQjhFFn2aNQmKGhzE5rvXPE4Qs8XswxGsHQKKzpPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q49sGalzF5JzOQkvIx0xrxZQ9k7kWaWIFmRHGyPGyRNnZQj93Kf_Z4r0Y4__T3WiqRzgu9VdSyVqPIKtMDvYDt0kuSD3kowWqy8b0L3J5jTkKU18E-HR3scPhwSEd2Z9YTdICvGSgN4BnJAIDM9-cbspMTlgJ2uLu4QocaPh6KBCvwvbMJ-3bnyDyulaFYVL8hEPAiggNzAJhdQMBJsCHUiRYDb9x1iU3ausCx4yAxv1jg_wV4Q8WI_IOz9l4T1xVcOhLe2dgTltw3FxoWfWNT6BGI8IWRSV6U8HQ6KDfK7qDnuZSIqglmyYkxcVFH7pxSZfxqd4km6H7ErwbT7qIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 922 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMXui_jpgIExr1k1he-C0hGHVKHXSBpn1SiXVlmBeI16l2bWJznWNNesmO_YPJSOAW_FM38727Tzi8j4xzQYfY-09EtiOV4blFSwLqYrSKSSnhhu4cCCh9B-hJYwsAVLeO0x4rPZKFXCYeSEuw-GouJ7rlSI5S40zLAXFwhslr2vFMe0FYskR6PGxvByyWEtxINujl7QiHnSKoTun273JaFtVfwns-ifEY4q2_UjjSeIxTY1GVAa5gq82XbAIWdnMla3t1IcsyriOYrArIOK0qx1bhNXjKwkOn6uYPkzE7yK4d9KNFycEcwtG2in8w8REfAydB_Urt9FGcn_Hqb13w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 775 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lElJBc_lp0mX7T8oD6RirTAxxuZ61Mpm3NJXJxMhxl_GkZ3q7XXVc3cTXLWbnrHD1vSbkAqLBMxPCG-p_Py3lJ1EkhG2v_5_ty4f9fy8ReWfLPT8sBqgOWVnPLuKywGRLNZ_R4Kwy57_Wz-jbQzj3NB89JrTZ4dxemx2eVlNOTg41Qn_CWlPWtmHPmEKCdG6LAtKJmGEmhS8C1EsdAw6024ok7OhjQ4byRXLtLCunE-xCHn9yR8s6uk32OLZrglFFvuFsdjHU8bCNbbkdvevKAaMQ9gQW_nwe162ty3ZKQd67V52k-DQSAd9qKzKU3v8pbl-snw7i8TS2FdLB0Z0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrXuBFt1AvpvbHpF8D8IzrW8DBhVIQLFwNGsCVZ76hmG0ECrr4urdhZ17PbQcYveEAHPrKV647DqiA3_qCT9ZE6yfT6zq3arXE_NK05VcrBYoMdE8zfwOk-7pLLzHC9v6wqZUhpJN8fGKhXBnfJAyn_tGR_ueE6zkwnhOhDRLyzwCQn6q3uThVauFq8GnfY8Bzorl3bgjqSuwx6NWNhYm-goUPmMA0JCT5aztkzhLkGKWCjNDG3F5RyHiH7CU5ZFQ1BJiigmXEBiYxmA-R8oCwaHvNsFjllHIbVK48QJ0tLc-yxzR7pjxpv1JuJ92Edw4c0xoqPqcQMlURyl4V81UA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 796 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
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
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDRKrU37ygiNwL3pCw2eWGtRJNMkbI-Vy6dK8Wl0NHHEfKnubBifCaPs4jn7cNgz2IYiF6j2Ng0xYvSkolw5scFj3BVQIkjYrbcbaQqs2m4r3nIZeaghAqqdy7oPI4CJxBT4nB2aR7loXS-UdvJwG40ZKa7WccuG-NBjJ-H8vDh2CVYtgcUhRRr76iQhZlNbfsMB1a8PTi_VJQCXeh1KQf_TpofznCS_3OQko4may7f5Oup8TnzKg2UP7eJZ723FhMhpShtwFMtvjXxt8JI0KZ4XIkyctQnjYt-YrqgUepKkiYJ_CL1r2cHgBTvzg-z_HuocCAnN-E_yZkXZB1ksVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEjBj3rYpJEIImBVDcnVNeIPq6k5Qq0v8wldrZ80pVT7yM-jq-yxrh6dXXOsI0mhcalkUddcuiwHtBMn-YsnXz8GNKciQNB0cW_6cM7yUq8iwMK8qRiTng7tEXEuuV57tvTEKtASIqZPUy0QJ42fTbJJk9nYdpaEyZ-UiqtvZt5eV84Qc5PVcq8yzAI3gKPTShiVEmTHAJvZVMDyDA2k_Or3RjYUeP2OvhSOpk1B4G7z9kpTmJNkpyu1NsySI_osGwX4N2iWDctTSyrHuGxlLCnLFl1emWf-4H6rSk8LGs-q1cVizfEviXfQpt3d3Ho23YMTYX26uh0C_79-HN4MjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRoEtxui5VumCBtbzu18aZ15L1gkF9JSyMndC6C1-ffXqfKqRR07Fxin0oVQve0WENukpoOL3bkmmtUL35hfXUpYGa0mbOerPbuU-aEYAUaU-oJLo6bxPwETy146769qnPB5QKb2kJ4859FJAVPlhAG8NcRRB0Z8tyMfp6kfq5Nm8YwpRXKIp6ohvC9W95n6hwT_B7rqQLB1bG3nvbM7OvHzAZ7PlF2jiaBayU0_e2Q5hWRKRpGwy3KPeoz70j4iYoHOWzNW5denyKBf_HfjU4PGcBlagYFT9JqkdNWgCde5-CirBmvWp3JIs9O1YcmlIrVAEWAd_OtP3nVM2A_euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4ish91j67K5IHrMLqNZvaOXDBRrcJE3FeNJ3gzHAY0jbAvwydfggprhIMzjd50D-_jhkK2cw6e1TViYXXc1QYpIcn5PjICR3InMRKmgwIhk9lRPyJQgwihq3DtoluX7ufkLOkk1xLK8yEu26TAdCL7bopfhc83tjmkJMATbkT_DcMWqhpanh-SdW__vHwb9P3uk5Cp4zn4M7ugU0cjRNOwqGUfwT7DjVQTF1Z69j2UiqZKv5nRED0nCrNlVjuRs46IX6uYg8zfMSoq2lyO9nwrxjlAwADJoqNkl63TSoxKJqgCDpZOZkNBvW4PtY8pNhLsTFOzarQ6oM5C7ZoC6ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8jwYL0_Z6ki9M4wtI38IVoRA6yFEJmYT7pIKYqePzW5XwSbGBWQZB8arR6lSnjpvaon1P0MMc2rggGEPjJOfgb1LUZIGgQSHhQUqD3rPmZuMybcgaZQLOThVsn8byUtyO2iSCfFubdg85UB_5DzA-JNp4QQHDmrdAi9iUopaIV_Lf7LOfJtdbOnzStV-Alrbcm5B9xnac-T9Ab8RN8in_7or80eLPTD1kePTgV77sBIDYtHoGNKD5mdMWcQwEe8XOOaLgMSRUCUmBOvIlEOL6kCvL_rEzrbtYYW9jbaeLvWYEoLa7f_dK5GBNv0aPSqGOjkrVXgTxmqbBFRW--BQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 658 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
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
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdL1UivfnpkwXTwijNvG87uqwTPeUwTIZJBQkYGVa2JJsHJplSoz81ceueMSiAS4FCySJ96SUdCSKdv4YRkkSRBSYPQT5HXZ6Tw85F2sJIJHLVN-pmdnTiS79Dy3grIdLa_x-a0-eJIeWGjoHGBvQuhUsQSkwAqztJZBCX_lKfG1jEQZuFTg1qtZJ-CkB4D0lOFJmn9zenHbw-jfcJI2t9HDeO9U7z_hLJVFZBFT8axqmKX3eOLGp_84B-U_IyigckrOFiR9xu4Tchpl8YZJh5Y-O8-PBz4MM34P_ynpe420FAj5fAsCprDy1o7aguCnQ2ua9sTdIOYv_GWkDS8SjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9vQwlqWsLczgt64zATMe4Aw5pNb_6uivpm3eylFU7-I8CMTGlJ1t5Gqx31j3ZImpNeiNUx8IWHDCLAOc6QgjRVjZ_2PXqXMtH70R_rCYBh348NcSXjYsvjNBzTAG-LVD29KjcXBD29o-UISCuiMU5U3aE0baUz3Ij9OVFYoOj7IIrFIKmWoxfqqzlS4eisyLIHoaIuVee4yWOL9rN2sJvhkprH9RSn6AmegaWTdZDyr00b1V7f7ieipUiJeDJOLFV64MHQ4EXGfA_-CaHya7LZoMOHblKZvzh8AoPNN4xH0TbLfZlHHu4faQj7TIvODsT82FkIkJmpyfAGlW9SiuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3IYprAP2DNBDNzOnMTDoRMccmREEeTxSCjNKTJM4tHngTwgxWKZK9VfWXHdnTMzP-E9D1y_jcu0nX6P3dl2n2LtvaU_JcyRUu4gCRYR6AEwKn65X1JS_FPs_fkJUzoKb7TEyWbyNW_qidIpfttktC9d5mtPaRCbjGHYr5fsNHX2cTDk94kPGeIMgKjJyvfqxvwBtcJWepBpIDcvrTdXf60O4IoxaI7GX8ur7Ge2PE9Y4guHiKTMCdKJPnd0Rizc8jXCnQbLAOBL0kdoOUooxWGFqM1gU84MHSJfdjC0hIMvZi0zPQSosxcKvsABjohZR7_SM-JC4ueqQnm8eD36Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyRsDqfNfzuZ-OxVD17Wam8tgjGUG4r0Pjy-yhZpCpDoXjOJ-lzJoKGq3xTgZoy0QXp_3i5jBM_tfbpwHm6OOTUBtbEAL32WhJf4emlgCdMpJX_uHHTyCm9T599NKHOtc5WBe5BuHpMYLx7q4aCMDUbCuhWNqUYgI1UUhTB6y94x3F1h63BTAEwZgB-XQPsM4Z4FNubWWP5zyZOcqlcO43IkD2V21qcJuiymrnoawQLaYpqJpeW_sWwE_d8u9pf4kcxahUr3V-ff8b82YZf-0DO61wbenq8Yw2DjyI31TDXcicQrMiHAvs_JS7OY4MwJqdb2OjXC6AX2oQYNexq-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWvNFTIfigDd6Dme5ofn5UAuXb5EueGU6jeeY7JWX2CPBbTKq_m-idSO5rnF9UCe4jQY4YS1OFr1OfgqEt2HaNSSzhgIHltdM-SeHnqW8GinKSwMKdVbmF2CCiYDnDFifC6UZHUzeNIDjGYAtZHNzbaOatyCjervW3sCRHnMCiV-B_L25GJfZafoaVyL8EQKTS-Zu7TYO0XMSETO_VEGZzPydish-hzQuypfMPmmH2cHMBVBfX8FK4lS926BArSv8AuiULz9SSl5SqJq0J2bmnsBvUVWJ3T_RgARUFGgS1bpBCVsiL7mNE2h83r3jK9tDXSlKV5PZ0HWbLgaH16I5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDW9kD6SLEI6IUqwzkHfdgwoe0D8v_4LUVEMAaX7dhoI6cX4VLT1HnBomMPdKyC7hzT95ZuywYc6_dN50u-rVBjCtK7OsEcMA3ecYDyjv5MMcSzq-Jm4uMeciBzrAFs3IcRU90f9Ln8QGUpy52NxjUkdG0K_rldpinbkb6RutZgVuqVYaYkE3xGZM1tpzCxZ06VFHXj1G36uDyUTYpqxouq4ol8pxYxeawjpRZgXdrCiwKMsT3PXEhNzMV8fsGZf0LhvQLb4lb_fsbcy0kNlUbZJHenvmNQnTGOBvBPESNWaYY7HAtZo7-GBVtgPLYlG5B0zLbaaUYDYh3Q19XIaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dl7HhXljVd9BgtWl2WL4gj9OmRMP0JIYvNqS_RNL_ss3gXpbLerDIrYeg88F52-Goc2nwSrUbmezA_aa0xUlT1R4U6w-_GCgARZ3Vw1aOWmc7yX0sfGZbRK_QbjiQTn2VNelBuV1bLRiCeYYqGfyeblDGAE1ME8sKyGvJ7IAAlCMHGzbRvZFd7zNYss_YYwSX7lbFJbM0YeilhK2rKEHvwr5wOxNci_VM5jyqGXQn-3LO2oYOqUA-GYO4NFXUhAn8khDU9ZDS2nH_VjUbLTIS5YIK0g-OtA7uBuU5KaOEiBOggefnud0rH13WD-Ew24rNu_ZPvjGnUwV_Sc7nGbbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p39pS6d4fXwO3NP__nz7Hw6fUmg9HEHrEwTD9NkSqIIq-zokDxtezYWS6j8KXY663p2peW1emkUZkmp35b_viCyQcc5EU9CvTTerB8gMJhaTaGOI0Fd6o6vAkrDPQPSeVJvDyrxwJ8Qfkglm7y13PJ0nwpg_kr6pSb0vhXrnN0lcco6f2s4SdWKGN_wnU7HvIdSzSjkKhb0j2SknTkgwJ0JMDVdI5s0OfU0tpfSp9fbEcDeFflkOr9m332BJlh8Or9LegKJ1qbQNUJV08fehV80LJeX470COEB0d8gQkWwqnWLzCBA9NhEHlZDNImP9b19NBDpMAn9Kkeuc4sSW4ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLb0jCoY7dp01F26ZyguNtyG-lpsp8fyO37Ptp8YPE9yyKVwH-BntuXvHHcOc0-YE_m8aS9k5zh9u7MLkNpYa_O5a6HdZgcyxuqePvlInly-WZBq1kSIWr3c8dOBLNmKR6p4PjuzVtAb4pYVpZ6hXe2WmK2DAb3Qpsv7MO1pQUSPVU5BPHEHRJKXSFyYNfF-sFNsffJ6BWBS00xAhME1n7W3qCZUcOZCv628kGz9naWsuazrNS1_qYpECEEQbkl3h2HMQ4knExCmd12Iy3Buwt9RTrQHuxAUUoJbxKmvkztz6_JMST51-F6RcKu8XqQFm7L-SGk5p42JEzo-VuAILA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HawOto1B0hC9D7TIt3nStp3wQCaxxwZlhD-cPAerlcpyBRbn0hmBL7cKuIySudJtyulvX3MMFAGQ03J5gaWLSTjM4okb9DwblHtm9lwKGYgEsHavxRF7GAV2rPrBT5U-AaFGpY4bTz0hSZYUdQK4kW_48U12CiaH9vyVyuTBz6MshnMkCWO7qusaux_mb7HhlUE5NZB3cB8uLWkC9ZkMjOfeI1HmQtl1V22vl7gn6ryPiBwqBuIXlwQ4R-4yDfzocn9KV0JMfM09q8V1KXNorzEmp_WS6GXQH5Xw5wJ6uUVsQK90CUGucU0tHiWQ_wHkyx9fS4gHgcQpUtwtoP-brQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sfqd7ZTgZwFl56sPmeZJW4zcZjAxyqWMjRBTP41FY7d2K0WxEW36iu8nJeb3o3UKJQKN6u53CuSjnilJ3uDZUEIJJuIrkw2jCjpL2vMI8IyJQAs7xN29h3J0m6Q3HsgP9CRZiXvgaZ0MFafDYmyMZfC7vZ7eFR92IZPoYQyvy8QvFnM-2asll-sFCkr8svXmleudyaDefUSOANC8FED5SZ6N_ihJw62FlaW57YqHMWNKr4OWYKCo9-LlGq-lSpyhvjGpJDnnKSGN9ApHxwUg1mIEjPRXswO4YlYg5oto_fGfcgnGEtPoikQh9XYZ84viH4L6uZ9_FxFRovtMQxmMVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6vo1HHURCagR8AERe4bWTbgZZtFzhSeuaIy-AEKmpawrZ5XpdFToIELqXkm6z1_CAJ0qxH_txClDEBYpRIFZJybGxwbWHNGih4ghQGyfqeDC1T3gWys-xB4tUjCwh5dRWRl0vd1dCY8HPnNjlk0ZDuOWVjHZeUXmx8r7sQOvmn5kY47ZvXUxDI-vAFwpPI3GCpSDV1sU7qUytrGP1Knyv4pWzNe0qmpoU44c9ThdScNnjD2xJArtE0y6reSIztHL5uV9UWF5MIPDxnRkDJ_8gKE9SKPc0anBFVP97BdfyN41e3YpLnYAUjGb6r9T-xqVz66ss7o-GYC_OIfvzENQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHSpv_rvZani4AdGF2xHqiMsMKD9hDh1sxhpnb5U5T3pbD9gYoQyt9p4pNtBXATwqg-RcWteMLnkd1rU95HH8UFg1vbhRPFy33mYDL9MPQbLrvshXzBjIB38QyvauU0haI4SHJz6KX6aK0LYFyOxYgbIr8v_g6BPeumBjBhZEVnma_Lbn3A6xCACGxd5vdH0B_mmEvFWDCcMQllN4GHZfdwNKR0U37tbJIOAIbbTFQuA7UL_wzDCIDgD_KHXc_SGgyEEjE73OKlRG3i4iDsGsQRwHf9JVCJ5tFuGxb49xQi42WSsEoeXUPUsmyVVkDMp4NdSXFVhTlCjjuEH2xNttA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDOuSkOIwKH8c2thlwx37nJR1idUPYrAqJG5QfKV2PNHtSC9iYsw78gW4m-Lx6FBAgcx3jLteXWmT8Cq9eZFigDBsQyppkOOMa6y1ZdQz0J-34SpuPYjUj08oQfzV5gg849MkIdZIPgtRtq5fDIMDhBgJEa977sfKLCctk0eLpYWcZCD3i0MSgAjBag383Env7YY_wqKZIBR8nKztsx5VtF0NsyzLnPrItYlL2bU8VhOMv3FEvy2d_JD63tkewxUgE5nG4RA5VHQ6rDj4rAnmWvNGw6ZBzgkNBiBSYB-NOfu5l8ySOcR8CqVAfWJ9Yi8-w9vaHNTLfvtVEAB09Ubtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFoNUOnFJmKYZ9nhWHYjECKSHOHttoCXji9jRxD8pp37lYu5dGN4sTfNPvwjgdO5nS3UVqSMMDTvdi3gjctRfFxGi4o_c9vnriRd1qTVQyGNRHCWcz8gK15Yldz9t_JWbcRGWrogYdqTLpmBUdF_qTJ6CzfiZzWq3_Gls8kRvtPVhkWVtEUdzdikAeKHglvkxrL9r2UEIzusmcQ0uQy9GCsRLYotHn814AvTUMjSQJ1zooAj37VpCqPkkeJGNgwRLa3nHGHpGdKeNfTz_rTFQLBK7FdwXLsOSnLJbCczvVcJZn9H9g26-Y7EF0ZayVa-_0o7QAzTWvtF5RVTo_9Rpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Odwn2TmrqVd9muTGijTulkvrxUgESyDV3arPUHavQPNiI7gPMPZO1aPoVLXSkSod8TE63XaT1jfFTLfqgkU90LZwuaZIb3P9vk6pbFMrc2SeXCyp5AJ22MqMwgKogpzmC2bmURqAxHoCOI2Usy4xryDaoBkAVXNAIfWXzsnxFmw2McApr6EV2gqfZfyPA4h3COpEgXVMhD-zUTomnadcavXu4YZfDx-5xpwBZj1uuzSH_AP3tJ9w5SBOe8YLMZNe703b0msXN8hdWTRKYhG0nlHenFjVdrnZjjpkebKCujgSxILKbOUN44XyXaGofoQXL7VBWZP1SsfroMVFDpQhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-MlX4LKXQ-ebz52VdrZve3eKHGW-VUeYUAgKOu5qUEb5puyq071RxUPV3TFsXbTin4Dd917MXn544XB63PLLRfT_1lQY5Ob-jiLe4ojgoKULkIEPKxXsXBNczAr_kwHuROWT-fTM47NRSrnBGFvzmnXbjy4O_0kxg7wrUDrb2qlLm2u8V4Eh21q_5x8OLaM-ikdNfJrA_oHQTDbBxbkN1jDB_5mNwPxUkkduq9-Oe60vXCc0E2QWN7brV42t_hnsCdu-I43xVnAheEXtIQdMAaJNSQ3CSQPYh31GIULmhHxHTMAUZdYihSPoNO-GsiWkMuCiHpCJP22VO64ObZH2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAps4iTnAT3l10rZGwB943-LsDHsm-WM4K9NGAM24v5yVCir0s2dlJJ383yu-BXDlAo3QzCM9ZVgUjb0LRoiuhowJU4TYTQ4qoDDif3SXDn-PBrai3OOFqhOxiJhHnuu4WwtwMwbuGId76vj2BC63LqKvyz_o9pQABN4aOzyo1iGl0Nt-YPPyRVkstWp6e3d68gckf9IVnprSu6qR1vpmJuVQXEO5hn9zg5710ExuSfHoUwdXxsvQfzZ2ckHH7C_SjnElXGBJ1IPzqiONaeHe4Dkxar3LrIw9N58zpAvd3SK-evJG5mxpMLwMp8tuLtHd6SCOFuBFdIfNoBOn6gRsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDtQzu0CCbst1vG905D6C2u5WrPSCmWqYBwML8dQOkSUR8gvVfJO6AAihHb1C0_ZSxaZLdiWScdF_ridfSishJ6TJqwwKqFUz0fzBa2RR5OGsQnE7ScZNnV89fSUtYeJWEK6Pe5YwHHdi5nvlRcCrMNCyItez360_yQz0w6MQ2HbB8kT4TU1Dk5JieInkKcYhVqk5fC3iSrz4LsKqHxPOqjuuW3rrhnBSCQIVHVG0I2LF0KZLnrR-yDdW6wsHAGGhdlbn6e8thobC_FQKmpPiJNBJRAbaIwRjiXHgDSLerS21kBlGCHpT4WhRjAjQI6lXqhzVuPjsFOK8TCJ6D74yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0dwXfb3caPF3O2NcTZMAbUwNeSrucLOxq1uXFjf1yl899ELDjL5lS3zBjSRNo4p_SKLADVgu8qy3_160XlTYwHIyqOTfEubTcJEJpPFjPRrboBB7ihS4XVyJ6vpjCEF3TyOU1YHK0biX85-qCirnsdge2-I7U8yNxmZpxg6rqvRWjV3FNuQMglwIlN6Z9JIlfUgM0Y_hmIQWSzm48C-zrIUQTg6dGPva5lske3uCuDscSZwGZmIhpojlEqIgxhIFhNeUJa-av1hMEkrRKRDx7u3FDTRnK8DrByIocbNqHdCb9YkDWTg-IiAW1_H4pGSTzCQIFIig6TN6bDxmbD2EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyaeWsmtH7wQfKVZRE3LYZVaTetSykbzfo7wO4Vt2BIRNg4mkFfUC0JAsNX9CaRomDqwmH_Fo1LA1FWekOpwltgi_bYWGA9n2Eg-5d0Di7_-EDl09GDztFkBZ0ZbGSNoumOg-57l9tNyOuKceYEV6aDT7lbWAXtmPhefXV5_zt_Xuqx_KLLTnabSJiv7IM_UQoqsO0Dy2pOz8nsTdqspg6tATwCpX2HaNZA5n_GlOs9SP_QCAQe7jxC08rphC1WgSnQZ896xxTyDuhDd2uhB_BooCbZIiGgf1qOYzqh7Zq_CxE-6i_ZDjuZnTv8nArZw42Uk0piWIYEH3U7lXgTQbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxESyujV4Lbwq4SBwtXRmdA8kRKAwjjUdyeG2pD3NX_RbYhF8okiCyLCfUmuR0kNC8IQTdc1SwAjX9W1KL0X-5OkZkFs6Fa4JL9_-PSgg_s7vLekxc_I_J8BZ1Bfjr17i0iqVk2QaC2kIIzLQlLTlyVa0mXFUrcbjljy-4XX5HoYnzbtZtqokB34ldjCvb4Hjo29-ROmclhDHx7zgS0VUhZYaYdJnc6i-D5oO5WKISvgomt1Z771U9lrOzA9AJb5kibCDG0ysK4xhhnWm850-9B6pFWJ-dfE9v_GBJ_TIkmuRqRdNJ5BeKn2TpnPR8aQawnQibSK4ePhOx5MlBdqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEVqrWOTW53JKdyVTlad1QajeqAcDPt34U6kPtjYFqSlf4DhCigxbVStM38Xm4B_QF-tR0QLsG4UhgklIfKiPweLaT0UMRd_817yQWYK8SQlmUv7TewjRqqRmZBhCUjJrmR-i9qE6QCLp16CoHRTPv8CZ9xtAWelY821rff3ljNci7QBw6PBL708MbCsY4fRl_4_bN6ybDTEXefjKsaDv7ftLjGp4oWzxS4GCNq8HyRDK3YFbOrtLbGZVs2ikebwDMu2EkB4BiUAsQK7XWhsC3oQl8NHFDgJfiJjFJ7JSUm9T1GpfNZJ62NmO3HgNidnK8z2cJiuStVKRX29ViXCFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT1i4W5MyEIjHM56gMVq8pJGDeYmxemzBWUK43y3sRXICJkZvvXHsO_bMeiwcL8TFlVFcbhD8K068Qi0ItS3CmrBQpCkBookqxX7P3WxrWdYixl_odIi0HgjmaTPNcgM-UMeSlJnay8gP3whD9oX0Px_jSC-dJFjZOXUoGOGJrI_YOykwELdMfdQrMn--JH6dEV2oujGKfWWV032HDfgG51nER-Ok6IIHYlVV9CPtKIhPEk9h1l0Jyqi0dnqpi095WhtjAHQogBSeqBozd3G_nm6fOvzcILISebEyqmFXaL7GYbEE_IzP-Kg3Jm_X2BxpHYca5_KO-Rdx1rjzgBikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJJcbWzO7XWtwUQ7eGK7RLs_WAr1m1MYcS7uXa_ZoFEJmWWgdA9Ab00exFG2YjHMfNUTdiskaXY-m_zj90wdyXlVJPZx52cf9omb5awnF9tKe5ZxRgi5d8q7TyDhsfVjQPUsYFQ87Fzi_ORtk2dJa0ihRZs_9B8ZEWQFu2xMEC8KTdepV-Y9OhgN3J-eYfCLobrSR6dohsNeH1dxapGfz8ugQvHtKYvF7PVXLaIrbRU5_nPcVqDuKwW1_iLR-RAQdA3mPI4dk0IM3QosJhFmlm90GMpWFXyVh4DOe0pkrVTdIHaqCB0tG6QxGPgQQ0l6hU25Hy_7IyR6SzTgir3Sug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHTsZY9qvrU2ERjB1YGncPyek5SfP0qFsC0k2wWayCSf5jUi2flIh7t89L9mwMp5I7XnGiMqJC03Qvkj3MYagB-Gqm0gZgBh65Xi9qBG1pVb-uacSthGaEPoromlxaTV4R5HgPndRzbDQhAlYRvwLXVFe5y5Gr8qmZEoAA8ZpvIirRr10iJXdEsurQFe8TWrvqIXpH1MdvQlLc6J7j9CfGMdQ4A1JXeGcNUeegWNXUea1GubmjIdgFUuoIIFR6as23jnPI0Vr5PHv2f7IWauHQ9GHnREOncHCmvpBi2-C_D6yXJHW7tMufwrIm2v5zS8ffp8fMCtdsPQSc_7AG_1Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQSFKN_2GK5s_KLw2XrbJj_teDFlN2vdq12xx_wqLcCjuFPmvoCL911wv8P3DYoLimQjFm_Bo1Bv9KmUcyPNIgWWefG1jYniWOVbQ7aPu-iQ485EG0y2wzpDSE96MT_xh_Bt_9fz5ptciSlOwzaV2Eio9WMxPU1DUikBPRG9XiFvRQJHNiYDvve8fOBat9xM7ceRQQhGznw0LetqR4aHel3gp3bhFPisnyhV8iSziQYyvrINwzPB-AtQ-gonkrpJ9W6ASYauT8OKdPOk_SlgUuSLbKxqFUJFZPjEaH5M4h7Tz37DIKBUuzO3zgCO7oqGHZ7CP44s-Rfws1dbhxM7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siljGO8iOnv33N6omcEiBQDtXgXoKBVAIzfwASokPGJw-G5xFxgCDw7IVDngKkssB0NXLmjLTbPIFzesvMMPUH4mse02Md4aLYaz4yJqE6AS7orrFV4uPzsbyCED7zUVBl3-_RJmrdkbTTRqbRTusPYpT9sFlfIhej56fGcEc9N1b7s2i-oolEdLRFMms35bMmYVDv9vHjEX5k4gZvrkPgDgCMnbFE4-RjpdATzv3ZG5YC3i9zgKu7oymmZckDVctWOx32Qz0opPbgxLhnAw-axGGqTVgjQ83m2fAFRxlfCIc9M_Dielvnl6_760czz9KvZb0YiyS-8OpE090w1bwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP7KtmIXcy05V8p_saSRl_Y5-SNra8CgjWz-NpLUNAWp5HxIFuUdILM_IOfL2CieX_8ZkHf2rRazQ0Vq5L583BqqklxCYe2V1Ui-C65WsajYXKLmnZ5rFlPNRnmJTvjsRgYzezyvlOPwqYSOke1TzBf8C8ETJ65jX1laug7c0dELNVWQXpiSZzU6bocms_PqGBIvvuhSzTl5v1QMbvm_rbr1MMmw33ZbeNp4fk-KbqFdIjKnKb0xRpTrrA-9zr2fW9Fm3kI6Rg_stf3tOpsT_w1IaNj_R7w3hj_RuTFAKm2Yzbs23D6PrAt53rcgOuzPj1_zKhMI2HGCZIwBMs2STg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shDdDxnOlhci7--LEDCEygpQEVWueltSKT-th4jbjigtn1A2AQVEY3X0y_iZwnlBmmZt_wEBcehB_yCck528jLHeF9MKCRy6sHdNDkeYUk_BwZr8-Hab49Ct0QJx8wqDISnObqSenZNznibyoeXfzsmu2a984QW_iyQ5a8UBJiF2erJdg27Xefn0H5g_KGWS-BCl-adtVwRbx7hqanTFndvcb8rCk8SFa7Hbeq7Lv4XIdAvnVP8JAZ4hiRbTiqF_p38fQ8IaGmRKQ1eG8jMBsfIodpBfADRlhFKLbiNmdgxmof-3lhSGqvIpeEUc1shIEzqiMBh097jPbbaJqn7faA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUeuDlr56COr3Z4KFSacCT8SP7M0g1lmRrc42VjcTTRsWcMB748WjlV-M0x_Z98PpJ2Jz4JRUQU17ByoWU3wA-3fO0gacx1NQKz3CENIKaayG7m-E60uhiaW1F4a9Q0zpTkO9-cgn3aSDRKSKORGlmLnUi7vEsXdp70kikpukNxtufl_kx9ul-OaVMYWrqgKQTiPVe3ajRA28H3ppGVqlnEw1-WssDivp6AxxdakjCriuvycLFYvhcTUB8bkYJ3Jt6awZriVd9bHdoEgrYoJs1XFEHM-WzxzJON9pK-BFagjwEc2pHHihMyFA4mCBb4BlDpTSmIJeyvwQ8nDDdl9VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSMAIMrhMl8W4tOAS74Knv5C44-R1_Ytzz656wrYUiBcKnJZAVqEZZp5_Gg4FGUFogoOK4L6qimp5eWv8MYPaJJA4l1AUxIgViR4TKbkQm2L4jc5iEFRlTR8As4_Zk8muupS5S9Sok71QLFy0YV1wWs4F_jMbmEBd7KWjUTwDX6IXXq752C4Q_U2Nkp5W-znf4V5gPjAr-6Z3sb_qzo4HlhcY3iL4SsL2J62Ppt_nKGpPXl1RUrZPx_ZJqiliyt9_GOvUgwhcVCYagSjjUctUNskRSodDEOKm5DuSaz7UlRN1C11F_Kipz8z2Q_qz7RT-fm67IRrpXjIE3W4oo6RaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/du9VRPEFInGGFansW8DJx-0JhPKRSrKAw1cFXnpq_u4-4n_moYoIeWYo1krqeel0PKhwFrah2c0vyBgScd9Ysn8fb6LuZRStRoMzYUnjm40TDxyXPifzoV3JZaXyjeuJUxKXzyimdvsELRGvN3zETDJuf2IP07CQH8N6yFdGVwvLxT77bsE5RDcgi-ACSf4tycLKGpYt0FdDodbAD-enK4qcdkgi2Yxu7__ZPRYIEYvnfloepetaYiswc0-77zTIQ_YbjFIKoDdyGTp79LORBFbMofrud89rukIZ0ZSx4usbawdIFgOoJKReMvv6-5V9HuB-vqVWG2rExykSglkvBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtdhINobmj1WaBLUTGV1kyEvv63Kp_t7QTNp7YxFPfufhI539sL6kADJlf0B73n8xcihf4wUbNCozN2X4slwxBCnp6zfvV0t5gVXAbmZpDKXJxmuh6YYntNBcNjsVDK59nRq-IPy5hgX6A_eLr6Hkw1CNWFIgoX4Xt-EZ9DMy_Qw6Zjnvn6C8FK_Pg4uiH5d7oC8gQZ6I9QgCsDrts2TOijnghsdFI6bcB_QtTV676xD7XgklKmE1YHfsoCquc1XM9YXS56f5v2HdA9Zax7QutE68Vw3LNj4DECtmnNEF6d_HSnk4yhwdaxtTIa8DFkthad-N_V6vSHlr7tna-iXsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbwqETvAS6Qx_kSLdQOsDForClpGH7O0v56Auc5Gq8mKgVhINhfA1Mca__fbSYIS7gowznoQeSNcdM30bQyXUJ2IZ5lwuU0xolPHTZROQXPCQ-dBxWx2lfi5jERqWUVhnCmx6Z5dGn4XjPP0FFcLwCFHH-dP4ZY-kUsPKMOz7hes-5leJrZpkNngDxUpxsyo-_EL8icEUA_gvqW5kbCEt8SEpP3Y6HJSCvDYoKOYOx2z-u1paeXYd-KbISTu3SmrHj0pyrD3rexSJ50vIabxl86XGGKyVs-4Djprj9cai7lsfmXB0vQNaNqpZIGVH9JZmk05EXTYJoR4azMz1_GbJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArFQenitfBqrVztEQf2LNzFA61kzXVo4X8ByORsvimUBCw4gwame40Qp7dewp32QYFxNYiOT4uYRDV1YoIhZ1dt96KiM7aaZgXy9yaGnIfnsgNfP0GtlJiQY_mrUXMW1LtMw4yfNolIs3LExGP-hHB7_S4DLMeepnjoSGnatL2xzG3ynYkpIsN5I0alyENLh2QA4Rqyyq5diLeLab8XccJILqYqO1H_8Sx9fahULZcjHs4H_NFU6OoK9VcRdkMGC-o4w3EkiIXoxcCGUF6KqF6kw6_ncLrxtlW46EfZ3iyGZbvCkP65H6vCHE_aFhySVKuYOLwM2UYoLUBSTDcujcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjFze_bP6Q0Yimsa7Gxp9O-_f4QHJAAz2sAmmXb7icSezN520DF25Y5Ikm9b_T22I2dQBXRoRzM1rL2e8EzjQOy9LbAHnErbiZHoxoQpYV-QAr7rDrpHj6aGzU9vyGFkliKyn658ihNne09zUfZehc1DFyD4lotd4WcJY3yBRjMnlrypw6OaR475eUrlo3T4BXnXBgtSNz1gndPl2_OlDmkbbitOF24jTMiPr05nFiReR4CMDiHe2_-XUvQ_Slc5W5U7-SCo4LAS-5UyD1d-EC6foasfgGtQVvmIYoNFFBfwBfFlurPsB8Rt7nx09b5VW4w1Jq1okF6CKRH-ICCrJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=NTdED8QMVp2efhdZqZGo1SHGg4gZ01_YoENOSW_s1GUO9bu9gEcAtQuApjQgE5SsHweI-y_bByiBB8U0wVTxAuaVHBm61tMWhRrr4psyOoMcpX4EnqwGehNttgXBluBxD79esS0_vgXYJVv3BX69L340WpIeL7M_5HuD3rACjftLkNGNkjF5zmpaXLnEyWT3GBswrjfj3DGwVI15PAagDX5AiLLvIacDtRnCNiH4aSjNb-mjdZnBZo3KvToHqgTsj-gSAvVmN8lKTJ-0VQlwFHuk21zaHwbvg_VrD9rU1gbDVIaHos3iD0sTGWlXZtqonsdQngr6qL22axYaVLPqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=NTdED8QMVp2efhdZqZGo1SHGg4gZ01_YoENOSW_s1GUO9bu9gEcAtQuApjQgE5SsHweI-y_bByiBB8U0wVTxAuaVHBm61tMWhRrr4psyOoMcpX4EnqwGehNttgXBluBxD79esS0_vgXYJVv3BX69L340WpIeL7M_5HuD3rACjftLkNGNkjF5zmpaXLnEyWT3GBswrjfj3DGwVI15PAagDX5AiLLvIacDtRnCNiH4aSjNb-mjdZnBZo3KvToHqgTsj-gSAvVmN8lKTJ-0VQlwFHuk21zaHwbvg_VrD9rU1gbDVIaHos3iD0sTGWlXZtqonsdQngr6qL22axYaVLPqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yiya6hU8e1Kfk_P6s2-iGo2ApRI28rS2JLwp5lAchDRYIkQ949LOb5F4yfhWvA9s2ky_g0f0MsPhCT5qFPh7zj2KqXiUYIywatYoRBz6ukYMEAaHHvpCb_LIBFBAYk64MOD8tjkvPJJ46WrQ2jA6KJQspahtGJLKGbNOBdaTXGUj92TGOuxUTJgOhvxHbmfpdHNd-JmHhsQ-nDW-o0t4wEEy64pHbHjKPg2G1llP6VOTejMDEEaIvT3p_JRrCDHJD1SB2Q7A3WF9L7Ha6B4H1DgYb1q779gyJsLoNAbQXhPvo5HT0Y6KmzANCFijeUmK0wZcl0xGEelwbeBUC3eogg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szLw9PG3Ut2DngJHCNeYrYlS9aqm2Ki0JR-Rj1vR8FUJtNfX_PmUCmH-a2Bs_dk2VsHZVz0_H30YTeA_z2ohn0OdqjJH3RUe5uX7_Ach_GYfkww13H261_1KATDPJljUo7n3XESW616SO21zHXbhLHWrTTU28lY2JmBuB0BBKdW7YubeQ8q8CvdCQmJNaDwXaw-3ayYlNOdACyFhtLjnDaiEuzVdqfbi_XpJyY1aqqoq44wHtjwflBj7YJUWkFWPusjpd8jltHJlf7mYILSYzW3-8oW4bsr4jIqEkYXILWebGnB1GAlAAunyVOkECRO50PAPcUf0ZuTliP-3pleG5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMS1A5cDTrzLk3ulfwDVVRN_ziWwqsI4q8U2c_Ju7UC6Z7Dh0jmY0aJwO9Hhgmdq28Nwpq37CXyT2RODRy5Ku0G8_Lg8uLoBstYt4nUYi8ekPzkfWZ4rnpxzJNbRbLvL4LuynKkf4OUIOKblQSAHNRNiG0qPdeQu7uGj0kMCkoYamh6utxdPrZRGfDZLbXTTQzvj01GQG088y6NxtpOMnUv346jijqe5ik9vHn4YCFX8EuIltwGABvNwUHF5c_p1QTuYcyl1xKnScnkrzHBvYsUu5_dMX36J0yIEXDYbkTopJU3Kt8tb1CUO7fl73Aza32keaZ2xGHswDXo0p-sUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDTlRIT0JFTQDvlp5wPyX_PN9l5LSoR5PeY_SCP_b0hrQNij1m-DIEcVn2nBJC-FojmG8Wedp3Ug0vyRjYCi84yRyIgg8P9u9Cazz5csLqMpusINCbSyMN-KYnnut6epUg6YRi1QHVi9wYwbl23JmW9W2hTqB8_HOfLQjkvc2-Z-4DzmWt415kb7F-Azzbl1dFkQM8kD5PVcKGw7ivcZixS5yUqnudq5gMOw37_rnYxla8wFIGolESCCVQzqVgKOFTimyGYuSiissr80UKEqkghV51zqIozFgu58rH4pn4evHexTx73ByX1uu6k99QDX6nYOrEikvQj5j0jleOzCaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNa4ohjOR9I86gZ2GyR70rs4YoGpLoR91ZPURkziypilnnJuEh1ksn6lKt-th8s1hk9BFWJMBt8V_ky0S2Us6ilv6exdojh4jyAEUSeVwCJT-6vrTVIZqxPV1Dhr9VJgXTlyCuhL4CMC8N4Wml7RS485BdcFkX7HUH21qS-B07qpJiBG-IiSWv9LOlxb3Z6eFgXyWXM9hFQv3l-ge3VcuSuVRe07ibw40lvToabAaykWCgcTgcO2SJb3A2yPwvwBqfDWa1xUjDRAp8oWOUqYmfF-Pvg7XCQaJW0g68p-UieWUtrD0ENd0hWTelHgiyWezSW-AgYGyIAB3GXC7JWPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hU_ouMnQMpsjr9rqsKPH7NQffNeYJBk7-QocU3qGoCVpu5t2vEYARB5RWdVJdzQPARYHRZC64_bSVZrfujgmSwQAyCX1wArjXmr4wYRGGuegKEvfTS8AL0yE_JM4PoQtHOFz1USgNI0-FXEebKkjKIq5cF6AsW-T3Ct1gefx9JAMeP8ZXST4dtddbazpFKRynSwBuaqKmrHDPiPgkDxrfpe4rKt6ZcLAby9DSPiWoWeqvT9Kgl9KL7SkFqYU8BIhYbBkQxcEh35itXUIeBmZ_hXrPoOKgEqOz9DRanJ3w97UwiIy1F93IdiiQaN52wzXaqLynzpKbqfRuyDEKZEXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCNnu5PWu5KUMANN2Ej5X4Z5T9WERtqwMQIjSyihgGszw4EVkniwWxJSXDH4RzyIWurE4nW7Y3fPpA5cB8YXYirPFNqQnQCG55INSFlxWMmU7A2BnMc3w3KFw1KhMyUR8NlpvFMX4sHeG8RryEsXEp_H-9pJpR2P1rvEGTujBgmelSuLvPW1OSfFQE8xRvgkUPixf1HOJUNWAX0KQMXG4fDFK6xlur80fWIqrCiLBd-320WbQgh74vr32Ia9YA0ly41kfXztwDhQYxAqRior5X2yFpjlFyrWt-4HMU7ESelO_kddpLUgIj61UgxeYy5YDXPVz4TPDlMmAQ2VV8QffA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=bQroEEfEU62ZSZ32zBh-QhhaKtI_--ggBJ8rBQKxxWDjn-jcNo9_z0HYDb2pSNh-OKFK3VfnoTaFzlM8HjGqBHkUrrE8w9ctO8dENrHxrZz3iRkR3LKfC1DpsK6X9LDmu0tVa_sC9UEafImISV2pq9ASa7xH-2-tDdkBakKTNU9qGQfW-HWTnt1WCehhBIuPDHn22_SyJglXVgMtX1sLed2ijOouqsTixy8GvNmOl0KshuK8Jfet5cmapLukWLagfVUMjxvk3PNJAhAi7LyN1xcQbSAajwVZHTx1zxLX2hPnszJ5wxTf3NM74YiXG1htWDfvpzYRMxoeN9boaq98DKlpiu0vFoJUs7DsvdnRrn7w87irHDgAihZ8DU_Xi-5ZbCIawp1ozyj9SNNTotImn6k6e7yegct4LDmxhLvped-_LYavb7bKo3dztqdmludzAdtDEG7L38Da6DCLZP1Do3LkibSpznk6w7Y7L2TpZ--keLdAzhvFQCJU4HBCESLrn-GYWYQwwydS4UNVktcEDhApW8bzYrLE6xnOvPkUqv4xy7kGs7dYiot8dSejvvimWduknHFy9owefK8nz0p1psciWI9NgNgLpxN6okAvaQv75XEmTamkrrlh80zse5v1YTcb-Wsc0P40Qme5v90O--j64qvUu5pS_ZcZ_bvSYTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=bQroEEfEU62ZSZ32zBh-QhhaKtI_--ggBJ8rBQKxxWDjn-jcNo9_z0HYDb2pSNh-OKFK3VfnoTaFzlM8HjGqBHkUrrE8w9ctO8dENrHxrZz3iRkR3LKfC1DpsK6X9LDmu0tVa_sC9UEafImISV2pq9ASa7xH-2-tDdkBakKTNU9qGQfW-HWTnt1WCehhBIuPDHn22_SyJglXVgMtX1sLed2ijOouqsTixy8GvNmOl0KshuK8Jfet5cmapLukWLagfVUMjxvk3PNJAhAi7LyN1xcQbSAajwVZHTx1zxLX2hPnszJ5wxTf3NM74YiXG1htWDfvpzYRMxoeN9boaq98DKlpiu0vFoJUs7DsvdnRrn7w87irHDgAihZ8DU_Xi-5ZbCIawp1ozyj9SNNTotImn6k6e7yegct4LDmxhLvped-_LYavb7bKo3dztqdmludzAdtDEG7L38Da6DCLZP1Do3LkibSpznk6w7Y7L2TpZ--keLdAzhvFQCJU4HBCESLrn-GYWYQwwydS4UNVktcEDhApW8bzYrLE6xnOvPkUqv4xy7kGs7dYiot8dSejvvimWduknHFy9owefK8nz0p1psciWI9NgNgLpxN6okAvaQv75XEmTamkrrlh80zse5v1YTcb-Wsc0P40Qme5v90O--j64qvUu5pS_ZcZ_bvSYTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMVAFxIJXvuWH6IA05RsHszj9_54ibrENYvK7ItXILJQtVN33L1e8oRgMS2-I3u-zeXVCKU8TEGBI7pC1rLTuoBEXkwpXdQgm6z4eUbl2pe5M7kkynze7E-yzrYNM85LRIGaf4WPO-QZa0B7-j9PMkNNlY_gvU6EVOdqP3w42sMQRWrIlAi4-33VMhJs63UOEegedgR24EWX7H0YRJ7FGk9Hbdxcki8XSE7OVLd2IUSGAeGU96uSp7pPpMS0Qqik_w3eYkyx7qDJweCP_XoVihn15GNsueRCONU4I65ZxEKoApWQURsaFDfzGpcNKtNtN4qzNYh3OGCHDOPoVuozRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsDjXC9OdOtzkhisV4tO0bRZDl0F8unggMULYVxy0gPAxAwzt4lln6j18apxL1A5_4GTGx3-HZUCJ8rqUYPW8hzW-_VQF26re9Tx-5caJhiBZIW2F2iXbSNcYx0E7F0od2N75jcPPAGmuW-jxdTo6jWqm9il_KMoQMKFPocVkKCvRPJg19jHitPV5VSjbu1h-4jyA1imEgofALSZYh5wb0s2eh3eQLBLBRwZTCyF7ViFWRoyoy80Scmx0heSK1BvdpzbHY626VA_YXuyn1-VlsiPjhI__hx9VOlZMjDqObVdJ7NT4CwI_jfvOECc17vSUixR0T_1BlbSefajmod2Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4XBGUOUi2WTtmePbPPx-uA7C_lj2w8Wy42fx_Pu3E4ERXvyBkxf32FwOMh98oKYH5oWmJOpQ5u1XcnW9tC8ktnBCbH3x2d1zbKSPtpXMqzxgxUeOyrpB-QKThn7SILrrYRBvbkPtZUGQ_bZA9oU4cmtPHrPKYbQTmWOZSlwvXDxtghrv3oeqT4cjKcgdwLM5Q_e1teBw5Y0nRHkHTPZRwKdeWI1kPXmJB9IuWeiVJ2nKd1bHsp_SGarPH5q0e74U4KHGM9WmwiyCfFYm1nbgO7T2nFXfRsUfnRjA62if9U31ugpgsuF-smRl2uHPwW2ILbWhV4MZ1S_t2dF8tnjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmQ2nJcbz1DOqqOw2IREGT1_KrCz-yGFeZsyjNBXjp4aKDQlm_kk0vuYHgjHtVxV4M8c4Ee2I3vXABGjuvmiP7QcI6xnfzdc0TVOuOLltU8Lqzy0QaioLvLCcJXMGwzso6W12XGOI4x5ee_mySMpxRJNPbWjns32nMT29KSCtHiMgwsgWx2LQ0JIwJX0sP0fBNkDjDap8KydgZPZF1bLgvFf2Dk5XqNAGSQW6Jzw-uKYiGBClH1_zARPoSxMM9EWiNngwJ-bDAFg2k0FF5Fa9a5DZnvI6j_5sEsVNTGCGMDlnrHGvf9ty47G4MQxnfmNr0uYT5wf0zUNvazI_VXGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emg6iLPndKaZiL-HdPU-auif-7I_cRhZTmPlhfXYy20IgVto5GvLDtwWUu3thJLf4-VCfdFRO_z-c_n3hQTv8IfQNR_qT5fADyEQEBIaLlbpYDQP7-vw6CzIblexUnP2CLXQSk42V_KHx__-Q2IOY3VOovmpSo451IDcp3r_yqz0Ko3S8SwAl0Pz8qnS4YoVTfVJV82IBaEaGJTwvlASvtI04kEz7Xx75RWOJnnFZDnml3fhz1S66Ng8uwd0b7LtTdSlvLl0uqdh_y1UKs2rbLgnFmJ9DCMtKOXYOj9rO0be2i2KyeJSEuzIHt3bHW1z9-DZQnFdVyenYVp0KFNGZg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YwBQWsIpfL89Xj5yNsfa4_c27ZnECe5el_nhxnviSezNubcF4XkywlTVHVcBp1kUuehN8xr5gp--DkxRTCm0q0LumSlArcOxQXOdXc2RhTck34ahjxA1NN2AbS8HhgrW1I4dnNguzfw4rHqu0ECdZKMUbKcCjqVpnYjlWHO0E2FphNyGWjaoGCqAFG7vlACPrA2ykLEIzpqQ5pgABplS_aZ65wmwtOEL55x8VNnU8nGkME0AZ4YcsTHoRQaEyV1H50OPjQOKQ8qyO7ml8ycTi6sNcFkFlM3kmoXBTtqY6FKr9ur0dnD-0PLRzJQ8Akk-aHOm5xumNX7Iv6Rvxkbxbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YwBQWsIpfL89Xj5yNsfa4_c27ZnECe5el_nhxnviSezNubcF4XkywlTVHVcBp1kUuehN8xr5gp--DkxRTCm0q0LumSlArcOxQXOdXc2RhTck34ahjxA1NN2AbS8HhgrW1I4dnNguzfw4rHqu0ECdZKMUbKcCjqVpnYjlWHO0E2FphNyGWjaoGCqAFG7vlACPrA2ykLEIzpqQ5pgABplS_aZ65wmwtOEL55x8VNnU8nGkME0AZ4YcsTHoRQaEyV1H50OPjQOKQ8qyO7ml8ycTi6sNcFkFlM3kmoXBTtqY6FKr9ur0dnD-0PLRzJQ8Akk-aHOm5xumNX7Iv6Rvxkbxbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3MNM9U6NYIXM7aq8zRfw9tWnl7I-eVvxTZDs7oAWDFT3IEZK3qv9WqBIonpg79gu9_ssMrg0mdadOfFI92VK30HavebWkEQxRdL_PMnSRyMCzai6-n_3WEWI4pdCPoIOqERCKT0KzIxe6wTWMZhQcbK8bASNX685IleL0eo64djvBUebsdNHMVb2YjSlbZTRu9s0AGaM11l4jfEKj3rCWfXrl7KJZD6Y0YLjBHtO5rjD9av1Ni24OrkfdBgiNxPrzNg9MNaf3I9g5JVAkscK-DqhUU0juzdQ_I7VFfQaPVs9ZzWQYgfjp9V90IPuIU9dFXDJR0AK6jci0Osh_56-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBhnGeCbrqEWae-W1qmOzc-ElsuCy-0oUb32m2mfiR8JnpLbaFyahfV21s7XyesUHluVhSckUa3y_miQwLQQ4H5DbYEVX5tO0aO3QzQUHsc_pk17CJy2veNSjtwe6CwhiIpVg56k2dSFaBhR6_STyRN2hDq-zUfUOO5Dl9tSuwa_rNgoXLX9SUyQGIhzzUrCPmvLGFQpHEiSGcUvtAepr2BDlBJmlY2k6MMI93ZoOJwudAAVRC4VWShmMSd0VNtr1AGKH8vSk5IsnWUpW294fnzLUCzEXvyLjI7LA_YjR06c-A-r0a47hbOT2guLh_PyF8_a3ntW3hh9LetwrkYtEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0_NL8HRGqaupnINNhDfY1NyOBf9YUymfU0h_piTH_FGocL16QjHyG9C0CjZszF4AiMTaj53SNJy7wgaEDke8ksjfBYiDyBwVmn-xOn82A-nl1wqb7j2fubKwIRWI3dryJSffxLEi1RvouOVKFSDrnKXE0KHUEnBOP7E3f3XSc4ltI7AB-tyDb3oYrqkm_XK98gj-3O5aAeNZ8v2V5sugWfCsmlx5LBIif3dQP4Fq4HGc7D8jHMpFINbT5nm68h4xFIrGPL0cl4cQAJQZWxZ012ae41QUqsDsn91V4ADLlXnbSZ15ugan37odQFP3_b6rK3uA9j08wpDTdsCpCluDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdrlR3Y-TvjaO0O9tlfuWOcsBmfRTfgKsPjcT9vhtwRkNmEUdPQKjChbGPWi_EzU-IHtBS7_glaiCOXPDdkB-9fcN3TsVn_pRXd4ahoc1Bm9hFc9sf7QoJ8l-8_2Gly9MRj_RZD15qS3QR2eh7peYsnBRb5ygNHtla9vpppCuHamMONlyhcTN8di9XIo572bLoHd1noXPHBUQfofo12_Ged_38BiMGj040Nhaj-D3gsUUguqV3ZfX3DFITKZpXzh1lwAaYxnf0dZNuswuuy1Ho2qjavCtuRAoeld7h6pshC8Gq8xgKnYXryFx19t53vtEfSxsOCZ9IFimanak5djGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaWWBrSHgi3P0r0URsSWsKRrXYWz2M_f1x8JSyrbDqWwpN-wORiH063nBRcMICXjlxKkTic8f8bMSNk-YYluaeeCWeFwNCi13k-HMTpVxwNEdsC8diy5mRhGPQ3glAkSt0m8m80IZ-i7i4a-FZg6TrYWOSHEQHwSj7zX2PyNonoXhQLaxiWBhg_bsPhqao1wxUhGw5D_L5XHLliYRAm4EmYhayfEGQM_4RcLeeZ_ytc1luUittaE0OkLtE43rSdByi8CwzbOllzNL3p8fr1d_BI-9ghLv16aBWDhKQtg7bnxGP0iyhaUa4gpNvqPaCB0KV5TTwTEtpylS7toePToPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK7nbLN80UVHV7eEmnGL9m-JeCbY_S2W2L2CgrEBO7a5s8aWP85lnWynzLQSYdfE4Bjdd9c3m2hdtldh906_FvnU14pvpwbjww2uG66CLa5a0pk0WzSscCp3PQSVMKZiOMo7jtNnH5o1cCHfpNWc_rH11AoVBr2WGGyiIYs-QWTfMutX6mBc2ikKxo0HDPww4DohZNYKObHzmwmiF4ql5M6_emvD1jsxWJEJWkzbEib3SZnM7V_405y4Pn08_Dom8eNyYj-dsGnRSAPPbRubIhPX02ItOCoezkxVsPRd3JsWqaL_CSow7PaHYcugSdLaOu7NT7yBe8oeh8V0QH7PPQ.jpg" alt="photo" loading="lazy"/></div>
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
