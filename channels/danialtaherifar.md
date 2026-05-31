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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 20:43:08</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 299 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 467 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 574 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfhUGbf4cCpRULpwu_NqxE1HdJnsNaIvlBDMHgjUKUpYHQOR1vsAyLah7lDa9fgRiDTps9E0C0tgxMZk-mlodlEWpa7-mcgc75KH4UzTsKF99tYBM4gQ-yGEK1tthaxWl3FgEVrhzNxaHQY3E3gzsaoGczpQM5YBoZ1itRErFaN7475SDkbHbiFzbIPPZcvbpjpsxp5wY-loIJnoU5fbRkgO2wcd3uYUX2_6ABQ77irWtTM54MsiTS7LuTZmk_xVs7JlpEzS1DmFYJgXZUtdKzBs_xZhl5PYEFWZndWE7EcDB5VMBOuSjRRA6EE3J0ZDIDSYTXhck5zHPt-n2bQZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNh6PrN5ZJfNsNVR_jSpOGWtSVgjNbk5Gt2UAlH0NaHQ3dKDOxH8KtHT5ZuElhP0FV5gD7SyiOS82f8oAnRWXX5dG1E_95Bw3RadqMlKtpC4CZC3_XXrYo3o_2jInc32Lv6XrzMTrNX8VenSSy5noo7xyaQRjoRra6e8JyUPhCzS6Obppw2LZJKjIyY1JIkksKjBKO8kLXDHt_skqfpPdTwQ725BC2NgicJQxHfbEN2blPI0fqg9hDj6K4LeI5syydoChQD8lqaAXIMShfXhwNXtWInrXOrzMZh6ZMgSuDcCwsLdDU2xA1VjfZrYpLpIOo8tIJhj_lhgCLLH7QTSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugbctm-E5ii3Q6sOWAAtj5Bq-QHoIV6HElOunPhZiyPCyRChYqjp_eC-3npKDQ7StgATE_Qo_JcTkR74XnIUtFC1Cvb8W_tc9NCfT34ekIS6qch7tKM5rI3_Cp6qZOJx_e_ffhyacDARWYQpzjV2X3vUqpQG2DHrfVSIwciD1FkR318T_f7AsHHKimgFwmFH6RVUf7Lh5b82X2hGNxn4dpGGfdn-LERrb10evTabZj_tL7_kuhYrXmAYJHamOqzRMhVJN0t5VS-NbE3p7rzVyxaLdGj5RuxHsJuXv4N9GjsIwjKBYTV0S1PlfH9IFKMavgzlQ7DStumugBHVjXbMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_2JwO7159JU3Y2w0RZgS_rOUEodroIY6EkpZk6pYAeTYvH0Vg6gF0Cz7FXyr1Mewb2hL0Nal09varLsYnQWvHplZnrGPGmQm3cY_D6T3ANuthiKVox8um323hyPnMaJY706D6TOsD3mSC8Ikby2jrsk_wpP33ROiZ8WzdeE_yUUJ5BRwfDsFF5MA0VeegmFY8LxMiwzVtiDKk3K_L6p0I4D2jjQzGbvNME6UHPY4Vmq6N0-ixUnSInN9ix-av9-XSQijaS6jnt1AaC623k3VNazfd_-eiyr94KfHajSoyhHVpCVnI0ADhtM8pC-6aW2TC2VDc7BFzC4LHsQR6ptxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK7LIu4vSrvR6279WYFXup91X0t2N3bALSizmVPXriSBSpBSpgngfxveJ2VEuT-ReoM96GGQZa394g-aYfYSlS7JpKBEnrd6oEJVS1XqFm7CT8iOI4ZIOyVIdJaOt83rof6cpM8GAxiEDTyT3WK5DKvBUrpDXxTFfvZET5SJiJjNr3oTQdzfFrOEznTM5xk6T7ERB0IbAGKk2iaCbdXQneVd6kr4pI9yWq9X55UwTrkbSyVyu4IJINpKX-f6JIEc2J6uK8K0DMue6BNXYsqREOxEg6xOsUHZtxfOuNUNRIDb-sU8ZwtEBbJW5xW611jNZZ4Pxyd47hRjE0KRtRvdHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub6VeRu7dMTctc8xT6SM97IPFVOp7sPlc6fiiGcWhDUzF-B1lB4s_xNEN_K4yrkgzww3pif9qEqeOZ1hYOldu9PQiNK17-71K4onxJ5tIRnMHdcLQWeZwy-fd59f0GV6zA_2z43d3NPJ0gz_MwCoQu2_jVnPLbLkE57vOw99bjIBJ-JNkQic_dJertVWCIe8qcG9HZO-EhxnL0CxG1R83b6I0WDyFhTHmJDaOmtETN_1l4AxSBMjbKT05wwzt61KveWUgq8EWbrK75U8MsgImKanbRnLRzP0zNDmXKANwXC8rYI8ZVzZAACjD6Rwde3N4DycfXscCXXSDGC-RcaPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaSw9sQ1WM72zfQSTvCJxMDYdvp2nXGtPS4kuvK6R_apbERLK-zli_qjjJNF6EvN_ixj0HccdF6tFLeAx-260vsF1746Qratz2CeRddLYcR2z7ARfq5bXpBq2l2gy__657IPzEili2yxbvc5DeLN39aGC85jvqeD8-vyV_UfLclIa3iGokcL2Jj4BR_dTjSv4uTEQl8-Oaupt1dKicOwRlExy82FIgE7301igjpQDizrRt8NvpcUk4mffFD9YOOghxvSD6phQsIU8V41_xNor8QSEbpsWgc0pgb_l1VvR64BSZMnjxnrB3jERS-hpYAYFmdSdYiGt4FFqeAU_rql7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUSrewkttiftru0nlZtH29cq9AWVL71g8eeNKT3VQdiSS8Ca3tanGq5vxbK_ZySXMNm6DhiCs5EUQigsFKnGgZMPtr5lofjxExN3B16EALzUuqBupFFnP3KwfvKvkXoPFJddEWSX5y0Oma90XMULyHrf10J6nMeQcHQ6CyowY5hzLiBnXYawKE8L1CJKyrxGmRCDIlq8bpVcYN6ymr04qErLJ7CgNtKncqREwkGhcNDpQL6ImCvmvUVzwmggTu5rAKFu6ckReSo8odMoTvfLHdU_UezVjdZRyE7niEjykcRkNUp-B_T0g4FdgGuDLhXqQVqFDbnajDI5_Anf7_MaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgaNbAvvFvOYOwHFPJ4AEHtmFtkdadzFUNKyCBb4VSwpQHOIz6H1c7O-Y-VTJsgH5Jl6dMZUhg-wNxy5clt6uAQB5qTYBF0Chdv0mQlXmEKVXXoklBbfduDMeU_oGuY0CYaCrHrcSsp7Z2DCzftZZsQczzJ2Gn_niQBtrk2H0QXFsjNU0nUCnDYSa3X9AvyawkzN3SlIhmP0eyY0HJL5z_FagYCYvZ8pKIGSAh0zJxkGXLjXwvtyv5DSIaQ8yEpEQnLCGSg_koUVSxV0R31jgxJRjBHitpiU8hc4_v-KZbWIFo-1pKKu8QcBCnWqlO5rKVVOsPc96PTVQccgE9Qztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCxW2ZjI31g3SF6ofLsjxj2-4cFUSapwRFozQ2YBKi5PSBq1anb6B39Kr8OplCQK0ncL2mGQHzkYtjXQ0LpCMpS1os16GCHBXlgNevCr0F0qK5m18l93_k3y1CgUpzOhvdfiJYnOA7QmCpikYgQjUgwmMMVTyQJmb7PRQ5R8xoL2ZTydMVweqAqn-LCPpJSCPVmvRJcp6BMrmLrFcta0M8r0lx7RsaocPdCamXtO9OjrM3z1rZCGNLBW4qPrWHdFuAA3O9p-yvtczumDgd0VVTpVHfM8WV8uthIJTmuCa7XfyDH3626GmFg_9Ph8ObDUhaBY7A69dTz1T5lu6YHD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxcUR1Dou5KJpf1GlAakzTkoaRA60bbBRT1ogqHvip7ANB1qgGXOJVZmCU7RuCjNWUZuEbqexcF9dHTXEn6Ogt-MCVzdY7cjOmH3HFxhN11kyhNIWNk4ib31FxlJgajK0Dz6b_27k2kcQtNU24ul40ey_wVvhxihCG3Lt1uBz8UYrsM3HbYTW5MkxY_R3rCJJcZoUzWeFEbi7YC5atu2sNNJkwt_37H1N-PjGocDYb-yBZNdEb66x7qNW-fifbtXXW921QXXO-Ep4n5cp8LRYS4Dx5CvktH8Bhgb6xNb7vFO5Hk0rbui6t2ug98mmWza4J9LyNvMNUsdA_a2Uy5GVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MciPpQVHHlWIAA7YbmKnclhBU3esFblkWeTfP4yhhh7AiwySLdCUzk3kPiS60IKkm9u5waAY4gtdArHVMVdU0RFz5rNN9EizXzVNBoYuQiuk1kfXW-gz8YXP0qrL8S3Xh_8sc3_uJSFyitR34mc5dKCXeImSa8vmnHWlPp0RTkuCxmRs9pG5BGgHO92lX6akBa6hoKROKL9ev50zUKy2IydoDejJX_cZr2lO0yMFjOomxn55-bygu20-WEj2-Kf8_IZf5VDtpmxr8FSEGPi3O_xPExeKE8RNcebQHn90TjX-5RMIvOp4JQsuWXbalmgTaPOOmtgqVmFWo_wRfS1aMg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Zfpa7bGJZPo6AycsSCBnbFOirH4GOfoRkWWITqPrSf_DiY5De6Hrnd64Z6W7gCZLKtEmeQSa9mlKZJdFXu7pueCdTQaVN996h9I-Jy0oqOimyDtZZaTC4S2-z-M_8kkO6EA7wEHxwLLEDs6L52Jn0uNQlwfm9ya7tbyzcGSu8N_58UFhRjGe9qxF1n6mm1M1P53GQyJ3BV5-dkjvhQDWP-ojMUr2AJgxjkILBA_SjL75m4rKWSfYXWnG_w9FgaeK3h7ADXjQjS55feOfvQX3gmTQCGrKpvYOh5OkVhvCSZOeQUbgeBYDtBCayZR3HuwEnfJEP8Q5YSYruC650I36Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Zfpa7bGJZPo6AycsSCBnbFOirH4GOfoRkWWITqPrSf_DiY5De6Hrnd64Z6W7gCZLKtEmeQSa9mlKZJdFXu7pueCdTQaVN996h9I-Jy0oqOimyDtZZaTC4S2-z-M_8kkO6EA7wEHxwLLEDs6L52Jn0uNQlwfm9ya7tbyzcGSu8N_58UFhRjGe9qxF1n6mm1M1P53GQyJ3BV5-dkjvhQDWP-ojMUr2AJgxjkILBA_SjL75m4rKWSfYXWnG_w9FgaeK3h7ADXjQjS55feOfvQX3gmTQCGrKpvYOh5OkVhvCSZOeQUbgeBYDtBCayZR3HuwEnfJEP8Q5YSYruC650I36Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYzmwJ5edbm0-4ER5vjMmFrrpfSffTYpdSYvWMo91ulRZd4MK2FENkAtmGMptee5_vPWiHxKkcb7C1FL6dYuNZbL_pNBFg4TL4YyY8trNLH5n0OPKOCurbOFh-LjJScNw6c5B7zCn77PlYKuCSbESSdKrNvyGJR_jXeb2NKSTmaQopFhrqNXRZ4YZryoTTR-bwOPYfkCXHRZyY0_-az1y6cFxe8P3hf9QHBmwdWY8yxPBDcgyZWHeU5EGGjf6ctuzr3wFfcpdJ7x4QdB_AoL_uvUC5DOZ08500SaBLmvhIcEjsUDAOYX7a0w3dZ0-RIMt1zvMdWe2aJHEnJjOaIv4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAaWaj8cVQr33-u5499RN5JN3dpYLDZi_RBuusmSDTLLiHC3C_IqNNSG3vxvDRS3C7ON6RhizNVXcur42FSsV8NEBJBLoOsu5yuTkBpk0ssXAjFu447wN2uvfFtt_kI1_RktbToZwAi5qnGvqDzhiiXU9Z32dn1w9UzGl_MAV6Cuiy-HFNVBpm-UyU_YUkPKT8MZHqd6QeKL-cby-5bORT7w--bWTgMTU9nYENwHbFJgHi9Kx7AW3dfAuk17yZQR6ezY3ESH1N1YUISaMkdqP2XaZYT493n4y5oIRARbIL5nD4Xyzwx2-IZtCOwe_RX2PSbN_0fEhXySfVPGFOhR9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxZoEE0JeVBL1UQf7jv4gVVBJ1cbsvfM3LJ3U0Ik6PcjX3w9ub3Ty__-EOABdWKv4sm9vglwrAPj3V3OQhIFaOYeS5L9B2orYOME8Wf9mtZWsCVK9S5z4cyoPdmZxoGy77vNC7Yek0PTIoMVyxlReLUptqYuM4-aytn2pBjGX1blmWY8BxhKVTYW9miFkwRDbq3CsIfHo_sDTv9bFluJg8xZop49tJ8HEu9vPLmxiinEflP6DMqh_EkjeTjWoUUoucl8xWlp4d3co3LHzK0T4rNIuj8nOxJ6FHMalkd7mQme6MgXY9CEK0ZQOb5fJOEAHcrdHBevnGVOAyztNqtQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pREaJf1V147MGDp25-J9h7lixl0-xR6a3ZW-notWHI7r4oo6cqo8Iy8fbaEROWFrXsX_qsD_96VHQ5DhUQPuRF1QgghTSrTyqRsUkhf0xT2Xed3ktPSTvFkQoe41JwPnd-R2F-pLFQCbZAaLovSlQ-Za32xnXcUbtyinJ92z5hKKv96geluDUvLmRS_sRx25iX67e6KNZ-GAVkDNvrQC2qe2zF2BUNTdZE3InYz0nJD6A8SMLNJRwIzp2QfZJoLBeFf_cFsleLVYY8WpFOlATGQtqJ4d66Ub94G_wpzSCPVQuCYX5tKbB5pqfmSeYiF4AmqBR75OpzG_CnG1XbUe4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAqNbGFi3D58PG6kqZfePh20wYRVZ9JRF00fvtJyasb-C4wU_yRrb8xA0L1mreuAB1rR4bnewQItw5TgXR1WN8a6DlzzCH2GW7leT8UBYiaSW_ue1vxyDWmQdnt-5PvOpUjgE4Sht2kbC5QeFV83ZoQ5v1HDZ0Nnf8lSQP-4INLYglcR-SgS4qJLRiE52wZ2eRvhE3ppWt8x84FGyeoE9zj_d412j2MpaRae2IsuI9HjWTPgwehcfxhkHBPsQ4Wuc-t9SZLnrPbVtt32IdS7M1dDFdiWhUcb-tzP1FGcevwpjVx91vnB7hJwm-tufOD-tZeXAM8IyBPs6k1KDPl_Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TspOnHtuNwBCGnwN-Nx4efMRoQEGCtg-hhnZqmPTtUm7bHJV7T3Q8svgs09bF46kfbegJF2AiluDe0lha-8GG6p7RetRyl3RKdICfXUIHkAzHpErKW6S7F8R9WB_u_7BQTEb8kfgdO_AoCE_n3RPsJLhZEnRm3HcDU20dMCnl9jOpkGihvZa9NKaLDqi63-xGyfy_LlmGLqwRw3jkoAexkUQ1ZtcGSTJk9rvm9UFEa_rdS-rVEqDUCh9BH2hxclPjB_tS5Z4c9lciDLVWZHjHpQvRKGZU2YX25E6MO0zTfNUIoZ8ZkmgIF35tBvgXWztPhJe_sf50D9CpeCiNfUAaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOxgCkh55OMsu-dz2aF9ET5tWAhjujMrUopzwqGE7ScfMLLB8RMJTnmg7Mc8YsEuJ70IvZkiPxx489KJdxxBeSpCihcTZ0PRpbwNNGqS0e_gab2zOTpDKxJJ4Ag1W2eGLZHi_hjGtdoIWMnAWuq9ItfISBrZLC5SEmU4w9HyxZ_hvdeMWNmhT_vJQinKKmpZ8OQDkdW4HWbD9X-81slhx1MW9IPQV5lOFftAHzLvVg1dyq7HIDZCwwmTO4A9s0dfsCbjnk-OKQbRLyBbJB4xS4kDTBo3QtUZbnO01aIGNedafAbndb7OmyBV59i2oU87le0Og-RQpCaaNvpZpraaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqbOTv0uqeKZWIvp9n9Bgfx48aHrMAFjHXyNWEDYx5uEvJX65fF1xMiEtvB4d12IfFRXeL01l_818obsgLCVeh6oz5kywDDz-qugKyGsGQZvBMuQ0qtd6bkcmg1mRnbN7RQ1KCZzpd7JaJ3zqOR_z1Hv0MRBBbdXKVFUJ2x3FKZgZvQDxCmdgA7G1JCJpXM-BjBM9H2a4FSy1YN-ocYgHfSdCxKnneMysPYZBc2AhwOg8Bk_w1qt0uGuz1dBxC7fXhBLY1Lf4Tsp2WeyiD_6bekVeOwGW1yEmocYtJcUyL7_7_VaLqH0ROw3D99TDgU_gwqOc0WKyqAOSru0Eo06MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1SlGRui9HeZR3ozqMs3lJsCzzvL2nciOLayam5PPIwayWg-gVoogHRPgGbUPIZVmFuk1-DRV8VyBqAJ6Sa_hEC9kotbxapieHBi6W02rcBkGOEZ_JhFvHFxN6MX84QbxFR6APL0pBzpAQ391Ompb8heYYyPWMNpfr73FYWnOEPlXvrJuQJL5fJBPifGEPmR8-YyUGAPd9irYZOOUq5v10dGbrfs6lfLGHy1Z7warmpn-IBtObaCak1RV-Tba5y_CY_j1EDjJwXZt7NCpIW3AnYDoG15w4B9st0Awos0FxN-L9EVISn23p12Ow5N1NQWSgZHSIYVHBbQfejOaLnEJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUW0yZ-xsZnw_wD5i9OYWluKnxK55fvcdn9-j3zaS6TjS-ntVoDdPwgNQLVcqbRGbIAEhwuN8RMTnIunrLWy7yx59X1ZMhOeFnnBmstg7Mys4HZZ602ZkJkAAmX5kwZ37fCx7jzfhFWKV66SMc3rDl0KpqJDScPz9Wb4CqkzRuj6s2T_zxEuGg0fGCYhk0mhmFOdzlcls79t4pWDnFgHcy7iIKfvrjRjW87sFeuKr3vizRDssvlKlLmIFqOalvkcVAv_MorjC8_add9VrlzV4ZXB8VvY9UcXq6YwOjqWiZghNHG8D581ykUWM_JEusXSvV19TKfmeyppVPYDYUuilQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQsgh_HgO5SmpSLVFQsJq8y6j3vYFfgzJMphXQh79y-26uoZMa47NOnzoMEQbeoELf1jqWXaXTxNEO-JpySx0F0ERRSpvQx0scIYJ2xa47Fi6MESmFRVRi03AhGYW2wOfTLtKBNKisFLAvSQoFakKzPiHD1B_8Nb4bLqpbiJTOQNk2beL2MXBSf1C48AMii0C4yRs6M_GoEmoF1EzBuzo3t--dRY7YZqcFVzkoGQUrblZpvcfVrIi0I0a99NrfP0tPH_d4CBwJ8_QcYbBehDMFE38rRwgWrmFOnCiS7P0ARChDKvvaPiQLE-RDSkSePOoCKFxtGwxnQGkv4xs-FBug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUvJsxysqERgQRMIlP5PGNbZbEUr4Y3fhFdptwa3ZqmCOF4oDOAlTFNDOwCiVFNxQ7uDzg5yXNc3PaUXmGCZxUtC9-WU00XnvCp805NFSxJAe-PLDF5jHzB8mgM9F50Ca_9PawAEjyW0UPs0Jfez6J8CNWuK55IP6IjtCXHsOzT6Zv6FSK7Dwqc1rOfS21UqgxlvjClohYJAFfRIde2cDA3EbMjWMAGjUBdWayJW2uknhNm-aC-iY85EWpkE9BkKl7Mzp7h7kqCIP6Q-llrxdO7BxG_U6em4O33QdWghXy4IIQ8ur_2_ETz6W6fGiJCt3TY8cJYQIXQsskASQOVsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BH2DXJ5Vo_8Q7UVezwsCqQLAkfwjss1_WN8P8rApUDgNjXIbmwcK_Rm0nbTJ_pDNM8aLJRwIdXzoltG5x5i3hOcTqFULXsverzRI1NOYmv4BacbX9bCkbKkYhVu7wdj3xF0pEr1eAihhVC0mz7B4kNDH6YXgAcvs6qVt4_z7RGKgS2OoDVInvQWm4vRHvwfbsyIJ7Xz4UuIlueqMZjZb-hFI6jRzY8xlHMZCuB89sH_id8CSSEOdHREBOED82rv3hqzrPELnLuEpmDAn_DR-8q158FPD-LsXxneKYuqwxsTCdbtdZ5REql4UdCIK9S6AOlwOLRnxIBRLOfXymaVEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-PXpQhVi9-a-5ojmS0lzfCTPqpHBVFohNZMnsQ_rh7MLKBc7skozgUgtX46nheIPDfcHHGtOf8Tm4wcDl9SpH4am9ZRGevXgix9qeCqk8V477Bn2GuDQyVvLsJ1DZ7OiPe5KSb9qfiLx_b4IogS2sxTs3utL5dsaAaSSonMPRXHOFbgpPN7q_qb3CIjIsEv3RcI7GGduBxdK3WGLf6biv_ja8H5MyW0_3D6IN4aY8MGwvDmtbuiLHjvowYv19B5fnH9Lv9s6V7U1vfLCbTDsuYNA4rGsyb9ZhNnKvo53M6BAMwPTPAAEvB6_vbu_g4WkdgQxCMrZ8X2gL7RrYTtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoeoBuvwxTFDCOu8OgENVlbHoYpr0GyMmZZk-Bbym-sLgK93QfRU3mzgxc73ZVB090hP_kSwYzeGDvIHnxhldnkaIWo-1BsrNxeHkcQ1BFevoKyRKup40FQucCoe9ksz9gXs4URI22GRRvTfkpWY8mXACluY98chbPWeTilrPpIsEGspmArVp9jOuGkWmkb51-OEeZYOBH_MkNmyato042l3yf_nDOeHrXkdUaWPbvJPb-cbZQ7evTxQA4VKAksoSg7p5hb_kBI3c9wQzSRM4VTmv6iC-FsYo6Wyw4igf4voeT2v6z0pGlzVrcCti4rTOh4bmcPmpiGtvToZAx3L9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLV0ujF4gHYslZl0zgf48GyBHsAAMFf7aXxoBGpKEzzs4682H_jTuxElwR2bzXX2P2BluKOZiL7Prej5Ow2BOzJh82h3qo2hMAJZ8pW2IvL6xzu_Jk455ADp5gDsfCG9GYFJpLTFhSVJdi02YkilBi8yWj1BDsDoHoA5ayXduQhGpe2VC92dv8mIMlv-du5tXCkOCmxIWzHp6BrzparopvyvOwwm-KZFT6qhjjJpME2p1cSXh7CrA8iHy0a7px1kcwGJtNIFPXTBmKEhGg5UqyAouTUoW0BLrIqs6BvMt5_ZTqRSG3b-_RnVTpm6Y2d3H5OVCY0jxxYOvz-eNqFmLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLZZXFUmXNqbc_ZewSw_mG_Z0FYnpBH6AS4n9Sv8TEMZywR_SDkzMdmVzx44fqdAy5KsrM3XsgLa5goaPFxDTMsDsnDWxmP5bHtsxcl8JRJqWvNrpe6k4njbHVNcxTO_KUC9VsyVJlaq0zFzvS6ZYgLy3xJatUlEpS6oa9RvJ4JWkNY4axjqiPt_GS32m77_T6ugDpSL_q9hwzvkPai5oW0xyCPIPbkto34RQNPjdmKTsZORN-yNAJJDW6H9xHueW5hqc2hFeIzAfMpdXb5of-O8I3nwU5xtqg8UYOeKL3UEvmI36Da5gOdFYRgsz_kf8fACCgKiQXjKVep8-YanrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0cArXg-Lxpcr3qaDxmWhhf72GvEkzvMNd8uyGAst2BlPXwKJ7uVmtgR6IpcZWJgkEmNBcRTSh3LbXcJcDIRG7xQ-RXILphFYD1Dyz_lHiUyf5gRYE2EqykDkyljMON71lvIeT-xjKet2l_am-hU5cZOSlZ_LBJE8jHuLR7qjPy7S5H-Rpc4BgZFHPXNx2IsNZJTuhj4F3h0ebZHrn2rRoi-zTkcN-3e2nuWdp1kmHkpoyXJFdh0O1LjhvVItJXr4t9Z2at0JZqXMlSshneMAAakrHJamof7OkZssJOBMa-LaVXkeRXqPrEJCR74asg0bDS6hO7X6xsDqticSurUKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlzUTcSFqXUdNPOmjZE16wMJHVHOBtFMbUjwySaQVnlKUTlnzteDbYBDHSKhixXJXqOum5pSIcw66GuPNYzsFw3u9FUd1tt_GxNLwfKWHFdOAhp8wZSfJ0e-xBARShxb3AVNoMT5nzo79cXM11FuZx-iJ1J4MS_BAdHxf4zpFtU58Dyy2xVSLkk_rlbPajnwcjfWtIKLJQtg2y0LLjVBkqmY2zPmRpgQC-j1JYFLAvLd6eZYvcsFGODEPY1mTwMrwIXs1YwouTS-IMXUyGyCUfuENDq9cpiM_xdWrXav1TuU7tYcRFZhHM2iUsfUSu1MyKd0nWF08HeYG0rzwMvi5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXhrKjZdofQo_WMLahkwD-6RRquwOXJ26YT6k7LlBt5MWNI4TLYCJik0DtAaAKKssh15Xt5mfRtwUHNE9wOw98Hs5NjnT0MdupxsOB7KzrVxFx3qnr2F8CFSFH8JVGU83hZvubW8fXy0C9ZidKoYIwz3qBxLnDWlm8frE7Oig0DHJ0VA2485-6urbhK86e-Sk8SpHhmwM4_ggBbZ7sUJ8QR2DmaeynJNSrwbkCdPmLobrHX2XZXJvURuulF84wEYChRGgETWSb_2qBs5VyHVcupXK6wF9dwQFAKdBSkS1gfHg0O2f4nQ9x24u0YuG38hA1suwotPUKyqnEh5M3q3mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLwLGb7Rd1Tvjfi03FhMb0uRIR3CXfnHSU_oa0hrh1IF9yHWwy6HkqddiFjaQQkVEEOK-xQLT0RKHLpmla8XV418h36YlrstAYPebI55R2bKMR0YS4FjEEFCoWcaycq3T4hT-q2G_2pkIOe0tVG3CTSdC42pbzDpz7UiAQFdsaZMvIzX5PjGltKBl5tTSr0137T-zDIFc_8NM_rQZEcox9vT6wB0B9vRrzWIs5DWWY3bVHBayCCGsh_hz_N_dwf_TLgxGuNKYns_EhKKtloUaE3BDPDdCYqz1PkRbO1klgI6_91kmvPtCx9TO_rg8e0ba8FnCAuwLvIjbZloVUWIjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va8Nv5Rol6n3WK66zqDfqUejTKIQ5eZXazOUcpeoKoCdjw6-RCX_ZtxLtg8thyBx2fNl0oAX_FcHTocTfJp59USYSKoSHh0v8wTSCPkaDkO4Khn-6BREqCxlaE4jUhMiNRb6aZW2R6jUtkNe8EcJ3RdLuD-06KZHpcIV0jyyUBIMyGg8h7KTXo0ZrMwOtvSh20sEFpG-yDNuU9bL0qwjTLN_ySsx-nL7b-MoabE5174RmO1QHx2Zfrg9UyL8s0l28oemWgxur6jsn9miDjffyeKO68uUdd_bHivEhS3ALMeJseMlhmFMqrY1s6Be5VaOqwdGmX3CKgaq7_mT-DCniA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfUrRrZYUr47XFFvveI95miCkrcuUrwGINJuyZ_f_5NrD582N60ngkaN5iQpyNcBrk2f5Obp_JZvJ8NP5To_K3G4Yc0jJNIAyPHysQzD0uQoCjvjMKQNZI3FUA1aRtv4HIZnY_iCFtW-yrMbs9bHRs5fFkH0e0nbWZpigqKUUF0-XB-tD68WS-1o8BwVx4qfy8n4eH3tfqpostLMuDMsYgURskJ0efRgtJKOEdhsj08o8jgilxwoDI0bkUDDO2tn063CuKdqgPkcG0I0TkAqFwqysE2o-87Ytz5tTf-I4qimOONhcuB4bpBGnkUiJRJGKLi_21oTa2FwEm72oweCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P58rsnmD3GXI_z1HUB5ZI89gTdxN5dXjDu3Bp1s8WtjdNQBiHluR_acdsNqtwnIdv7hnnSqVqy71OJhTuu1eBRewTU0fkq9AmxlERAorSmkfD3Scy9V7aRWJu9Zx4D5aCkqOOPCYoFeiHPRN31bBjEpgvEv17Wdale5BrJnEnMA_XhmixDdmMChusqgQ8GPccfXx7fj2Rz0Y2ypCaHQ3nJQdgOfRythoD651Dde5eORSXlqkvv0EGuLFiRH5qTs0Mo0m1hDflEzrXIedo2lNcN-nbr6CWsJd02sfWTEb56HGEHBiMsRpNXIH0JVJieemBvfFAkjgSzkH5vWt4xRg8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSqu7tTBpiSITdtPRwD2NRxly2d4wJy0Dx6DQOSy675Su7kXffksso6eX2sy6e-lwuEzcMWFFin3rhU97W5GoccRmJO3pXc_DwBJyR64Wt4gAxZQLcGtj0MkqtAs9NeulKbhKGhJDkYB7jrqR51X6Y_-Z2ihKSPa0fedrylzhpM8wi4B84iLFAdgUlk56bHQjwEMZLkNflCWaitgeTJDBwZzbAdXUCGWBsuO1lvWrlVMAMmpUe4Wxhj8L8lef30ZwXxaWtxh7igzZMayxXDd_qHHbkfosLsRjGMrUeYxgORK2RqR3Qn3z6sauUNR4IomhTaDBxY7rjm-nCisTIgHBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wha5tdqGm28ad_qet_6lvhgFWdAoKVC59alvTGfADdcJqoWBgE15O2TUjKiwLULeXrQYw2ngDy4k8lkPFz2AzUKzRuEksFF9dYbLHoWa1p1cSQz_ACpE1FCm_2ZtKqLe3w8BQ_poEvUC5ZO3jc0lz7_6Z3JVe-qoE8yP7WjRHqJCiuaqvBjWeXslybpEPyxxYJMyNQfzuYAchl3a5zlKOjPaxFTUxYK5MNPZsHuM2gxZ9-hM2IsSIUPElS6-pnUWjex383F9RfGCONAUHW_EyX9U2I9oVlJkZvf2nQ8sMcWYWDDIOL-qBqy-1UNet-WxSqTQsY5vWtlJJQqvoyKVwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFLGm8usl5me__dqwxJA-AFRlka2D4k7yJmb9DUiPE2W5F4hMNtnwvB_XOoqHrw4t6R3Jb3m6UD4sv7f_8fesGFELN05em7BJj_PX3i3xHp13a7BhKAzNxipaHHlkwtwJhLvU3ACKk9EWqELPBnjrXDCv72Mm5JGOiMCWNVGAejBOjzTsggY2IdUVdSa5XMuBwhzGHUDufCDbTj5E1OIyPQ6xbpI7kR5_1Di1Zfd9eBkDg6RZo40Dd6BW7Az_y-DnCvsckXudI-tnp3kx8PTVFM2vu2c7XlybVqA5OYWTlrKuzv1GVH8kxj3Kvezg8NvH7X5zGu5O29cUqQX1OgQOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDnDmTclODF221Notst9EuHDMasU1sFrs4_FJfUa2_rDlpayouv5D1vAUpVMzT_4oU-V-khG84MoLcUI41ye8B8athY3WD7aCaHQWh11qEDoPlPLf5y_I_trU0grrjkXpB08ri0FZpEVx-m4Pv4mROc3TK_C1MEGwHAGTRLaFRZ793gbyASBomxC7bkU-tp2msFXES4yWKhE9Q-KmCdyPCA5zIrLF4sEs8U9hZp5FIZIk-XqEa7FEimGXgnz4Ja9zRONvonBkPrmNgX3e0QzGpbcrKaHmhKPO8buLoepGdfLu0zychzEsSI46tOLNgTv-p_2pm_BBs_kMntcFJUVwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWjjXnSp1OSktIoVfhl2n2lpJFxIjtYHgkNEWr0uGNR6gpH2LG8CcckgKvdmQjwKAYA-BpY_oM54Y6r6EgygtEBMcBc-u8ABpMqObqeuSBRii6f0VXRrMVbM0Oc6y-1ETpuwL6Za9_beROTwVutLNqwiMWAJcKHuoML_O_4cGTJsKULf3Mu6kVv_6InhaUnct5Rsg06rS9Tg4QEXDRJoEpLmro8AqwE9VxD2JaZdF_B_ykZaoWSaM6z0_RSzh_29wkL3R4beuCqfu8yYHIHFKezRCLh2rdPYFIfTu0On67RAQQiKyVWHaSEo5rLUQgz4qlpIx27DJP4ga0OKgRAGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0pj6JeSrMuR97_Uj-9S0QBZelqaC2ONwz__i_EhcL_vhBMdEFqB_mUhmZcQZ_dKfwL829-zPAxDLN7z6rDn6aJrH9phQEylYK9Q7dUkGoVC2CY9IDk02A8kRHYQz9Xzn8Ll7_8niRrnfW_Jtw2sHzRDN-1xEBXHXTF6LgADaieqvVNb1R71clWV2I9LtxxCcE1HOVARFTK1Qyb0gitXRD1hoCoz9-WGtHj-yzL3g2noalBIm--eYWbAkzIf62pkVtANto9bDifdlgmY78kwWdSdi8R4GyH6Y93hBCcao4IU9O9FzQ86KzJjlh35dRbsVg-FllxSPMIsefrttcdT0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAr4iFXOdRDtqxi57nzf04dqEYfsbQfrvBWmo7Rprgq-AEx7yV4XV_Nz8YN2TN2H3Nk6f7Z8S-T4SJo-8Ckm0FymDM2N3UqjfaQlI_c9dWET1snUFe5uic5d5ew3MP22-bORgBGt7xWsNmFPa9Y2Ml2w5atjEy0E5zb4kC4COjwlClG8tb6em3zgvykfDlgR2FBPaIvverA31ZTa0OkxgAY_U1EIz7N3JgRQoD6LB_yJEEToWQYfIqEMUyzo_V9ewVke23AfSISOxsN2Pi4EXrd2Mvsl0ApHz-gQW5mQXk6Z1-CVT7nmUNKJiS_IwKAohNSx67I7GX69l7WNLAYoHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq2GRYcWmlCn72dE03bumu6q8Qdh20mMfk4OkHtJwgF3tPxanVFh_ZTeu3tPvKyZDY8B9ANgwTdVycAKYNGEdgCV4uvTbe9w9I_pVFdVgPQloWET9bw5uKHZwtQGx4qO46HyfeCaAFF9YQBDpEjKdjYTpXUFaUpdQrAJCpjJjZTYXsFLJUvjOodiQxjPFtwBgr5at4O8A9y-a0axpWra4nN-AOigo0SWRC5gf8rzir_VlAgQ1_cAY8Iupf18yLw3UIK2uk8A47XB609f1kgObJjOUzNmS49lefII1bLV-oy_rfXN2vTrxzx7xgSTO0qKO1xy6DtDdW3APO7OoLZyvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tL1bgj2HTYOB4hemwGeYJywuxSXa3GwOXs5bJZgSn5DEGtKCUWUpwBOKHgW8P3Fxs4Z40sjF_2UnchXIpH3RtxXiKZzVyiaiytdi2LnBXwWpfNMKi6eEByM2n5cmaiV7F3thw3-yXmvTJGHu6whYj-pgz48LklDCnwfbqYMXt7co8Y84jGxcSZRA5OuJsM65XHat08krkuuEKtoOhkIjF7yXZeG0DXP61_q_7nH7YAwhqHxvFWOeyS233vULu2SmMtVlEadLiM6oT2fG0zN4-niCa357-hcbxMipFgtrbuA9TO1hyHMKklO-TqGOSYmh0Gl4IH6jP2_LmbuJ8kafPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyNqe5bxCZ43BdR2KieJvlNzhW7kuBKKp4HvqNSYuSSGgT-YDy2nr_teXoVw05ir3BGawaeFI2n8iDKO7F-efW1iTscnDJP679S-o3JvTmjDuHVw1h14CnqnoiLcAVlW-veCXvrTD_SxwPWA0HirzaYae-hYXeJ1fvsmF4IwlHrk4LzlewlY2bURsQE30qzB2_d2Rbp6sC21VB_94BNKmoScbCXk3jzK0vDyxefAasrdE-FWE2eQdLCLGidFd8E8qfsZTJxctANlIi-z-A2biUGLl0dv2JT7OIkmY-j0EegObL3vWySnAj78S3jRy9DxYWH6e_b5_nmUeXUa2oCJvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0oGYZltNGPTvuLrA00RxudjHkVg6VZM90oV1tghHBzNW5RDxV1shMbhiQus1Gu7yPtKB-8nu_Ab312DwChBh1tqS2RWROMj-q4Q1ipuLUoKQ38bH9DhfgqKhniVzgzUAwfwBLo9fba6KkX9Zw6LF7yNY1lg_r-eANnuG31Yc_pstjpGyJHVwTS71wbGH-i18Ogg1aPq5t1gXLj9P7BEq2H-ARj6rqh4si1SXdUiPApguxJqrbeXULEbt0mCUjtCoG6HSTaYJGUvRtTY2KsQlSjjrQD-BkTXdFKxPsweQqMJnnFGx0hFrMtmfhYs7WzPZjn7f0lTUtu0Im0PqaS06w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRDwnTXCZ79DjEB5wNuXCn1qOFjB9V9DxofKRLauE7wi9n44Y8NdLpslatvodX-B7Vc4GppvOUzpDXz5xTZ0Vs_Y9odJ-aTbnypWc-wMGBfcac5qZYaKIu5SL5sNjeq67C54MEGD18Lrf919zU_VsEQsybe0T8MHqQMauSPYTXsK5-pU3b5BxuqYW3tA95FNBFjLKl3MiZ0qIBDnLiyQbORipP6irix7JDv9D8cbLDpd-3lPDvB3B4rsY33b0TfVTLtKM3PPUuL_V04S9lMtjOGLlCzEnm5e8SagEEjrdLq7WSSbAo7RCW8Ny_ucXKYCRlH90kLp0XON0D0nya9wIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4d9JeWb-F2Add7DUDEKgrZLE4lbLeaxGSHl6kEUzABHfIZtjDmCl81R9d8YlAXmMvKOPf7N4O8r3Iz2v_Sef6Unrsh0r4D22qWnYWmoxDAyeYdimLFovvfhfOgIw3ULNcVN54egr0ehrEuJjD9t81yfcDHUt_1NMNjv0UiENSu2YcVSsPl5SmNjwOOZxrBo8AW7pP00IPNmBEYr0MYdCOhHAfIGJ8DmcPwSKRt98b3t3iHrQNjxzMAcI-Ind-JZ4Q02PbvCY55sGdBLFof8nCuTyXiv9ntk6qG50GUZdExq3sam7KwjX-wuijj2awYgOg6m_tuhlBYwtgK_0I_ahg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyABLIeMZwtWHDXcon9uNneoqsIn57-pO9ZYf1CPpf1NCVwWG6sCct1AxdKfrdRB6OKiWW32O2O-AfDHwkcmZnkneKw-oTei0JXvzkTT78FqeeMTgmqwgN652dA7v0XbXhXBF9RIMtboGp4HTiKEA22jKNqpg69yYRYqdxyw6Jfqr6hVvjPgbAwzTRExGQBEYIWVJev5N4hIMxMFxXfJH_cNIB4egzqAZi3t4myTtLobPO4-WAUd8Ie8IcpH5hdn6Yu3psQEkzHWKfqORNz_Xym06012GaVT75YvVrr-V1Ck5RAhvVB-Vdkt2QUEnVfXo0XK8TyNaOmMlnqfIB82aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOjq4P3GiRgHzLombNdxG1LYcSnvWxV9VvMLxs0S7lNe2nJXjr-HyCILP2upeLIMcLDgNQ3FkrF5k_lvEKEjEz6UwQ2mxoOFdqNN3Ys482zNhRmX3xRF1Vzg32ie39vbFsucIEPPo-ir48_c-LPleAe0TZjhDFId7tEKQ9asX7D4xg0w_5KJDDO2qvp0PvTnct3azr8ccn3omyO3qjQTHmHRnalhzY-gvUuN_R2GoWPj-2EIjKOLI2WzHct-xngyzR9NMYaJbkpfzuGzNXBAhf9xHnuWu2BrUTYZYkSBh60P2ryc3_9D0z_JkEqw5dV9oD4oiPc_ff55NER-ohkMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRUrH_bv7ICPsH7O0xhL7QZTt-OREj37H90Xhdh414gsRvu5Ca-MF1PqtVrJreyjSrY_DxjM3p5vEiItSxIhNkTDwWNEH4gZ32N0muWQthDYDDbUImw44qTF4O4hWMANzusBMoWHpdzZqNaTEyBMuB7w7petI9fz2nU6rcXue_4xPP2P7Wx9szkwUptOLmSpSghMbh_0L7C79Ipi0xmjFoP-hEzQSL6F2mTQlpT0sM-ltvEXcK4rrQzgFY7woFhqMbha9N_7bzz5k1_zfTqmN7a3VJUvJ72T_saCy9DqScZx0NJ4RmQQnH0dMTJSJZzkY0DyR3eqFc9COa-vGges3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC3Val-eEuUOh5mwi9dI-gCmIO9P03ABDvg-PT3rIyBQj3Aar-W53xzrvyUGMUzSxTDCDUVIUInKwQteXkWWIbxvL1Kj1CUJON8yH_T5k9NFpizxv9SCUAlF6_A8vchP9tt7Bfw-6aklXbChVTbAdFRYfXAIBy4xspu6s_MfJVaXdUtBudO85a0HG8Goq_wF-2me60FoBVKSZyLXPZTaN_IABSxo-WKu7X4DB9FQLjI4tmGuZn0lJ9CbmA2D-bwbh5kDyxRPI3vO6fmaQu_P9aRoMTpPJbTw0JF5M49AXZf9DgvzKLZOKfdJb2FCoQrdnX_RZdnHZKxC_DKlaEkaGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeu0ME_5v5m72qz-hueguQ-hw-yVBHOAGh8Uny5O6T-E75fByo3pfA8jK2LHbTBRTJVQkyU9IjOLOVdZVllmSlKhjeWHL6WIlocoy4kNuDv6DZRJUPRTZBgmTGbQ1ya4dToQm5TXnIT1CkXTbabYSQmoTWABIFn5E2FSql_cO8XaQ-kYaD29b5wHE9MzoThTRa1BktZUkqcg1_85hOrYCxz3nUfZjrnXuDbCnfJqyOwHeocApy_9gFQ9xlkecsRXhSBpQtbxyz3NvMtJLCOf3kDmPF5NXSvFPyOwv-Ei380cQrXmTYoU2q3thDV2P-npE7mATvw4cC8hmECNPR1yGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-4brGsF6equRsBlP1CuT9Uk5aa9kDO5U3M8jMIv_6g57zeiSKEqBbl2NV1S_tyadCp9lDNuGQ8h_GFJYLqGs0AY3wP9fWGSw_Nl2s3Z-fb5ZEbJm0K3o7x9ZrfeqhUpxyyOPGTlYN0Die_6MB8m-KEpENLIi-hwx0AXqcEGFmq58g2frVOnbXKC85mrouQqTBRgV0dWHBR3OI11oaGDR9BDvrlu89jIm7qmraGPl7of_pkRr48YlHWfwsiarIx0PevM_tQiRdV3fb4Oqd3lZmqKVZGQedjzwBppdg_bx_xQ1jnnmlkiC-evSzpS9_77OWNFe2LBc0b3okKuVA649Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0L_RMpUFmQMN5RuLncZMxDY6a8CJyFuutQhHwMXpWxDFw3XKeXuX7IxxYCgtXyRo2HTjFSvKXuR_QKDC37Tj5ofXznoyjOTuuMzHYx1-oz1ONT53WA0OxJATXvwxBvs49cQzTCArgWVwlphuALemReUfmfmV7r6D8YsPsroJW9Eoxz5t71QkwQM_gHEmmduWdeogVmVs4eZQe6mtQ4IbNBK-vuL5doEJMK9hACJmvCEBTzUoiPuLjYAjfQjHd7JjZGZVtAR3_Lo_Y2P2n9DFCmU08VGL6jJmnCyGvpIrVbJ8nZFaqZbzzLRZdbYm330Ig6ObacIaeZ3eknIwZ77OA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=o1OWtGBbNDbVC1R_8C2_5f8ZQ4mRl9kwcUsdTffg9Bsk6W-LiReK1LbDkwdlW7PlgawibeCK-PllwcQI2kLvjVSxtsmr0WxYWU_dy80m9C3QAnETnQRD0ESXk_U1VsdsdwX3fQVLosYcMh_912poQnnzse-VvrlANFz9H6DP3rjZWOH6hJUeqGCXRCmNFUBeqiL6qce0VhFY0kbWZWgABPxQzu0M36ckefI8jJg1gn30DdRm-x4zHGZNJFSZ9i6pnsI1taq8beisw0cNTIAuvMZDfCBSy__-VaZ_oZ_vHsChLFlwGoZ_L8dCF6sVcPXCvsYRcM3Oq-r-oIfV4gZsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=o1OWtGBbNDbVC1R_8C2_5f8ZQ4mRl9kwcUsdTffg9Bsk6W-LiReK1LbDkwdlW7PlgawibeCK-PllwcQI2kLvjVSxtsmr0WxYWU_dy80m9C3QAnETnQRD0ESXk_U1VsdsdwX3fQVLosYcMh_912poQnnzse-VvrlANFz9H6DP3rjZWOH6hJUeqGCXRCmNFUBeqiL6qce0VhFY0kbWZWgABPxQzu0M36ckefI8jJg1gn30DdRm-x4zHGZNJFSZ9i6pnsI1taq8beisw0cNTIAuvMZDfCBSy__-VaZ_oZ_vHsChLFlwGoZ_L8dCF6sVcPXCvsYRcM3Oq-r-oIfV4gZsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyz_beluuE4IO3j09JrmsEcVni7L3SV3LDJDA0awRF2Wv3glyTFP0JToLCZynCjjbDGxME3qgcUQ8iwAzuNR_dwoFS4tb6HDvYIAqcFQ1XQ6PFjbNnDwx0fGcCUbcD7u93-O4eFR4r3KmF8Yp0j64D94o08awZ349mhf6O_-K9Rih-PLS9a-QDfvbPtyxRn8EMcwxKbsQOwAxIgdSbHMVMaHfErjq5wjYIJ3ZI590ShMBnmAqeUd5pgquqUe_MgsaUchec8jvntt8ynt0N9uwFNLMgRpDQ8_TF8PRNqmSvYMtvd2mAD94PKKB7tff2uSvI3xHYCVmYw03ThRnU4SKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzC4AkLU8CgJoPk4z-ECOFgQvrMAAe5U11d_mCwwXklqzSJlPWhh6KyH2b8528dDwbd7voU7ic6jhO5_KAI_KeK9fy0uwdiG7JTz1QpjYTR42bhWieusa-N3W56DM4MvDIUiCDnfvmw1pqYYiuY-8_COK7dqq1M5wsoVYwT3NOlBe4hR8WmboGw4nWDtIPpV6TcNGfZJKstDuna0e1LWWt8HlpTyZk60EWskvuNTO8hf4jjSmdWCzuK3BZDhAOkr7VpGtVbe4vrH0LpVHL-GT6EE8FeRKee0aNvcRs3cfWX4TjzDAcOAjgBuAoVZYPueIonVeH25H-gcFlMM6-GwMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7GP0f9YrWdPNQSlewOsoibP0kfZh6fW1lcO9Ul4vv3nQSJ8fbLsjjAddQhP8KGRzi9wWPryTSwxcN0h2lMllwCHQCjY8E50gs9-QUQ5AoPZqDZPDkz7Bzbjmiwwl4m6YBCdeg8nOvJFybGgCqeiODnWf_LH5mepFsjg3kcdpGBAWhhZq5IW5qoXA7aMdcyyYx-e3xIUXA25R9quBDPlfEEGA1HEHF_GEW64E1isSpLYfqQ8exu7KsKFjVI4zGFidZfa3caGFCoo_3TUdm20X43kGUKgtDizRj2MO0zLlKutFUmY3ogXsRos0niVtMndQBZyvTAwfA8dR0xkj_6VSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro2oYkk6MFGAq0BWOPg28S9hnj90GRSUkGcaJXUS62wkN8wD1iyUf4oNDac9GETgzVNl9VYRvlVN_4ekd18WktAoxs1t-DsuiV1RmujZ-Zrl9F_tWLl6LLUVzO4ArO3GB1-VDNCSgkkztI8MRukzF1c1WTaXoG4gSWGRj9v6ZLp1eAQhXg4EV22h0aN-wpAjrqlRaMGauXtDfaE88hMbIxwKXNcuoxnHtP88cs4ff-7dQh_4chr6-3mTs0Hr78eW_b1G-FcLBtXQTkMpZMW5zEu7DDUNVnAcS0fOasyIVDLpUsyKYs8zUthCZFmZp1KXi7Y-V8AYly3PDEIiYcF79Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uW-D50OjdCoHZLcCiOZZJlEF3wq7cJrXk3UJB8xh0jz20h9iInIHIxf0Y5vX5ZR5dkj3breZvz5piLrfR_o4dusjvPRsyuucQ_C0UuZ5dgOozGNmkousNspaEnSuu1UsMVHJ5XWuo8od0RU9qiwOyXcOFl_Nru1P_lou4REeepw9nsivVnAHYF7wDwgWNYsScxZUKoOLcKdcKylcz9KvG1YO6wqBI4DWCNoMC3awEFWK9M8DdiC1I4qf5r8VStQlU6kuGGDbbxW2eiMe3fWGeuvPasRtPgQiEUib8kml9FMrYxiOTj6z_e6ikgz3QHrr1O-X2ndvraj6KtFVwiLRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6WIaHQ9QNPvEUQ1T-dbe_Dpwq0k00ocVP8MGdDv77b41UVlvM1ysPaTsifI_l2fuZBPgCOUrfOPFnu6fkosPxj9873yXSHG7Nk-siJp08TURHR-cjxvzPq-odASem_2Q2fgFw0XSjr6BkUnoUSfbNRss0YLqOZ8WZ-pl-fmMb9ylbwX1MRq0K6Acd3uY2vzfnwrCfUvCcFznHaySincnnDwN5ij3YLh-YHcclRAAqTZsusj8LU_mnw0x_p-eLTVHMI_5xsi4PP10cuWHHhmUEHx6cO1iEkTBBBvHP80dfbyBtSW0Xiz4rTPWquhyaVrE7Cq0na9z-mUmEsNcnabpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1x-_4kgy6iEAxYujZAjrQZ21eIK59BFs215vLAtcG8Ogb5YU9G8LMBQ80tRDbk4adkLqAELy2ckxKJ2blsThwLkS7Uhzeretf8cXJw7XHKZyMNmOVSqKDXSUh69XFWnPaNsh7qMvDLEKfzAa63auzrqWGvArcFlB5qSB_QdykBNq6U6rDbcdDCP9SbZm46wPefbKaTZg4ecnTxYPuMm5JULloaRloQTFk-kbmtptVWyylJsxtG1NA86Qwnx70jPGbJkTZnRKVvVelKV4LmQhEXkWiuCEec7hgnL43XHHcOIfFebEON55dYpHfyX-a-RwYTr9hSHGX41Jwi1XhFLFA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=LdoyobFIArnRLcK5CZ7StYwr43WNEn_qNFvIR_tyTxopSOFHNlb8zHnHQR3bd9jlDNPGX9p5UoQXpLCpW8HiwkRXGNJkTeGsQRD2FgafTrO-ZJc1k-MyxhmER7Xu_fkYcqJMoYGYPFqxjojVVNOZI00MFB9j9Qq07figJi07HgAAlGcqjwmZf9BN-EtSu6nMnK9V_PkuEbf8JKPvq0sQ1GDMaoURFxjeQhpFCWm-06-e_1Qyjt94uoz66A5hhGeD97Z4yAKbcvF0V-7a7DmzLFDaN72LTaoIwkUZGabPOnhrnzD-tMia8S5gsjShZA73jKufjVcxt0kFto3h_4HtziVMD1wcpawmEr3gLEIW34iQHYo6wuPGwyqqYT7yKjVqO7-mTuVOoA2t1mGHRCrItuD3GZgJ1ypGwV_-o_cxYTxCD3gaHIgV9bC_57gQtVFw3peQ-O3umbcurjAdgmUFKHBq_8eHfHs0qWxuBzladUAQBvb2OE_xFNrTmFltmto5S5-jbhWHNPQpM1rA9HlabiDDKWUw-9JrHkKKftsBhrGXGyneGDs1aGNx1p3BU2bIlB6xrKojGHJDtytZ6gTL3fI7_CVdGDLRGK3i8v0orXHMNtVo5lzRCTgd2WiN9drZeZ07fisc1nzT6iupjm13mvy2f95jvgG_vtZ3hsLau0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=LdoyobFIArnRLcK5CZ7StYwr43WNEn_qNFvIR_tyTxopSOFHNlb8zHnHQR3bd9jlDNPGX9p5UoQXpLCpW8HiwkRXGNJkTeGsQRD2FgafTrO-ZJc1k-MyxhmER7Xu_fkYcqJMoYGYPFqxjojVVNOZI00MFB9j9Qq07figJi07HgAAlGcqjwmZf9BN-EtSu6nMnK9V_PkuEbf8JKPvq0sQ1GDMaoURFxjeQhpFCWm-06-e_1Qyjt94uoz66A5hhGeD97Z4yAKbcvF0V-7a7DmzLFDaN72LTaoIwkUZGabPOnhrnzD-tMia8S5gsjShZA73jKufjVcxt0kFto3h_4HtziVMD1wcpawmEr3gLEIW34iQHYo6wuPGwyqqYT7yKjVqO7-mTuVOoA2t1mGHRCrItuD3GZgJ1ypGwV_-o_cxYTxCD3gaHIgV9bC_57gQtVFw3peQ-O3umbcurjAdgmUFKHBq_8eHfHs0qWxuBzladUAQBvb2OE_xFNrTmFltmto5S5-jbhWHNPQpM1rA9HlabiDDKWUw-9JrHkKKftsBhrGXGyneGDs1aGNx1p3BU2bIlB6xrKojGHJDtytZ6gTL3fI7_CVdGDLRGK3i8v0orXHMNtVo5lzRCTgd2WiN9drZeZ07fisc1nzT6iupjm13mvy2f95jvgG_vtZ3hsLau0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxWKdczeEJCa49qxQsEcdkSh2IolQBjVUk_Fh1-jfM3JO_mmykt3tqUnIjvu6wuIx4AHDIJPiKVxmjf4xuVv-2E3k2yvEUS0YCFQanKfE7EhLJvOcGmlxGLZYUtPws2Lx-IzSKHoz8aMYVPmJP-2gU3qGyyaI6by6iJYjOv9FqnAmksDQ3fRCaARXeYgle5OVjw8NnhVSnapjIjshuVm3zmk7t682P64sn8ohAIUoQ_CvrKNO1qoVyL46WCMd4S1q2AYO-i4U7zlhJ592EyZdF09U7d9PsC4E5xDqtihVkoXYRlccHyKcV3YjMZB4P_RoyDVQ1RU1szIKKtqZuHK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b610nEvyJrtupLbOHRGOmvjuVWY80LOCH_YjKfpyTFtzDI0sZ1jvAaYTX7qgBltPBOxeb_iMJ9fYDu-wVKJz5k1KDagXp8qialgkUEimfGt6WCYjKzqXTLD1eQorwjA5dUFC_-V_T7fIOV3S8FuM0e4spwLJBj13qI14UjPwd0D27oFewt1xVdVc2GpByak8xQND7hUy6xP3o3P0nBywr1TmJ-c8Z4UrPtC7QGeUmXwV8TUJf4wUklJvUIenZj3etnz7YIS0QWpuIRT7rGj6BV6G_MX6UOIIA1tYZb4Rbyj6Gqt9BZOeMOblV2I683feKnAZEdEuUPwoiblXPM2zUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mO4x89g7DURJwM-zEwX53AyumY0k04_T8rAQbg1EN6-JrqHSOnLvEMLtgWritcIAEs9YsXvTKHipvfW2C-s57PckAqdBCGGIb1GaeKnaUwW33GvJTs4LV7qi58iZGuG-BwTUZDs-YGgIdu6QiPtNtz3ABelCIcPeVi0ibBfY3_ztCBrIZcsfVHZTeWaK_5_Qe48aBn8tAzOfbh5oMftfhQC48HJBZObhv9YBnyztLpknn0GF-LS5HmN3VP29MmcxtmZBtjF3r-epstWWGmOoarZgd7UAxnKj9TB4m12Ki9R1PVgAj_Usly8SceruUmuMIKZIPTbGWZ2Q8aC6zLH7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih9OKH8rFD4ihnx-vBB-eAutijna4meurQhf27_UkpsNdluulyiGH6LpgKx8Jk9rsyoQMwlryfjJf8S_3TI6qIgr1iZj2jt4UDPCll0qtLkFBB7UPyQJPNpN0suKhBojIYlyO5ZOlJx3Ug6Ie6Lx-6R8ZxEeEjkMhjqQuhb0il28RSGYgxQoA4U2RdASZgoc34Ib34ZxXRvk1oCSxkoPYeZ2WZTExz6nw0pkDYTGHg5fNA3Gm2_J-8VkVAyScGKcJKEiQut3vzx0Jp5r0XFl0BbZ89GmNCbkXOt6lNCyV0VqK5XihNAM6pFVt47wZKD-KiYOJUeivtd9G8QVbkuhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOSUIuWMJKhp26QoZpQmLQuDdkBM7hNkh0O3kwBKZsSXJUxoB0CmcT0RqhzYRXV3OSNsiW6cPF-4dEpQ5L9KlrSMRnsY3N0T3aS--ihycBZacfwR_Ltx2td8UBY0aNRA1fipyqY-wspTtPVkBcauyu5pv7G-5a_V9oXPCHeSVHQAalkHTPjBSQZi2UvkZ6ewKpWS5xVlptHu_ilPgfo7-QnKdBG8Ef8IjMX1JmoyvLPs_URfGHV0wZbLqg5oaMOvg_YhSX38ilVUKpMJY7NSu41e4EMcXu5h0-TFJch4aJF4ijXOW0dzfykPwiiVfF-yT8VjalW0_JldrNk5X3XZSA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0cAPJ8XalA00ikjoCXHcGT0TiHDhuSQbwGC_WQrdWdXtnzY2IAWBUbyhDbArm5Xgla1wv03InEjvYgVOM0sW8W5nHMnK6YoJJwK5Mi-eCrZWDv-CF4Lv68zqrNnPCHTZuD7GtvekOpQa9I61ovVAtcz7Q-fFUDMgM668fqdYUDgRf5cssxW3X0KI1BxcW5u3B2pj_DujuP3SSHE7NM5fpxPPOLn5pEdU81KsqcKfkfERyN4LB2K_ZiKCZsAvV9mPNN-IW-SphJ21e1iT52XwoeqLJh3MqRtfs9TAahYCrjhAzZr6kH50gIN3QQHHD_1ZJJVIbYsI5MPtl1W8ICn--Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0cAPJ8XalA00ikjoCXHcGT0TiHDhuSQbwGC_WQrdWdXtnzY2IAWBUbyhDbArm5Xgla1wv03InEjvYgVOM0sW8W5nHMnK6YoJJwK5Mi-eCrZWDv-CF4Lv68zqrNnPCHTZuD7GtvekOpQa9I61ovVAtcz7Q-fFUDMgM668fqdYUDgRf5cssxW3X0KI1BxcW5u3B2pj_DujuP3SSHE7NM5fpxPPOLn5pEdU81KsqcKfkfERyN4LB2K_ZiKCZsAvV9mPNN-IW-SphJ21e1iT52XwoeqLJh3MqRtfs9TAahYCrjhAzZr6kH50gIN3QQHHD_1ZJJVIbYsI5MPtl1W8ICn--Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krnJJGXi-lscuseTxJkorL-I4ei5u6JawrpGj7ATlUfwyKkJjm83hOaZGbjmDTkqWuqgKzLmdWi3yKxyHeEbmCTRKbmEHp4i08q8vae6Y_isKPN5nMd0E1LKGxy4yp7dzu3wWNpfLhtDk4EqFyk8CnyG_PUy4_ML-M8IljjM4hg2hWX_4dmdyMAseVTk_lr9UMg0wgnYXADttNdG-Hin4Tvgn5FVY47Z9KU2_xVeenbvp4O9h19Y0_F_eM0I4X5p6duI3ZvYKAia1gPGz0p-Zg9Zod21Ej6MoFPIyEnoge4DJXeJeyP_qr2Ya_lvJGTmKiZ0szkfVJhmjH_zdGuWag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNzLbvLTGbd0AMktvw_rhN0Kj0SwSEYEfuibhp3G5fpk_3BuBjJ6gu2HO4o4OmKcz97e3khRcBsfsS7mPvmT0Ms8GTcMOMYm9JgNE4WjjA5FaRjC2ndMVCsESeQ5URW1JGA67ERCaIInGtmRnmoSmGP9HWu1r6UK0TDZiIajzqqDdObWAWFbLzaSp04HDLtxkB4JvE2AgRmzQ1kGMHgN4H1DVURiRN1rWPGp2vB-J5P2ZWzW1qJq-JdKR771DKpx2E_-ZC6nyXpm2hwkmHURvf-4F0_xdJsB2Zvl2GakOI2m2mkLBzbki6-x-TNWalx9BpfAqGL1ITwKtTqNIkzIaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i018lm3dRhAtzh_u0HYG8IAdBpOtIF4IDt8KTORKQEkP2dMpd8adlai9tNTMJh8hl4yAYUxPrdVgwprH9uuglXsoI1GNw_Wz20huXtZO9MZjVut9SyCToqZ6ji5nlDj3QqmT7PBHf-pHd5aFyk30jnUTfK9Z5ta2EgPCFUXeaAmYc9bF8HSZ92IC_rDUdHtOvt4yR1QYSqhbLiAZSoaOspIMOgEapY0KGHoj6PVqxyBG4y6g_ZmX4vaUV_fGOQAm2Cx5uQC9Vs8cFugU-Vr3x22Hpo9MzkyV8XIwEPtrty1uISURImrxMyunIIP2hZ9-eR6HusHmuupN1VloOKXW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwusihUbR679yoJPrdbh1EGNP3kxfmsQjWH6goKWJFqCQqajIwJwk1kRSa4Tr7Ma3tKTmNspLZpqX86OOfg4LZU4JSeBnLIP5bXxYBFlP06ars6BJPkE0FZcFdF0Z3hZ3ZwCCLIBriITWkgQvxtccAeTAbaxg_mIl2kXA6hrHt1D1jRS5XfkouEm0PHidcsaeNtxb9u5tA5XCWKBAVz1I2VIZJJacRW1BT-IjiNdjQAPE4qgCUB-htpT_uA7XBP511Ssn1l1CDzWj_e-giFV1tqcG8KECDmjpCy9GlxYJzZJ6TVf0-GHCxWwkWz_LYldVPqv4HqB9HP45SOS3pcTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJ1EEsp-YoqSWSY-6m8Sy9zoehNimPoQOe8jsj2hjBnRlc-1BcLeDLv8MqKNLtclTj-rMvlGeyv_6ay3g-y1ZmcooatuBNhHrE61V7XqGdFzmLiXDI0SWm9i-qRLRTlGTvWnuthK52jQIVtqzCm4T0veU1uejPb7aD39bFREDpG2XmbJFIF8K9VbYeHNAdmd2Z1RkKfEssG9a-3upek55mYWAQHms_Xo0epe8bQYz_wixWRdd8Nn_at_IAcBEIoMFM5IUVig6xywMBbtEH3Q51LD7TZjOJ5G3sxHqb3hb7dJSogTgOEtnyqjp2KjCOuPqQCWw9uKh5SFS4F2maKPZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ3_mqgnIpSHogaTKujGQ-FOmKv049XautpBZOx4BwrS3Quk9fDeySMDuVdQLRhyjIoHaTUFnRV_6VVmQEPtg09vGLrj51BQ38Sh8GWdO5_k9bXaDpq-l1oJW81ikAssSVY8yrde4B41dyzAbGnhW25jK_mTpi_vOWE4l-s8L4BDrhY5v_8jtXnbGnTZ21Z8PA5LVtlUxsoX9hwO1L0m1mMeF_V5haoL6P7CSvverwWbN5oFesVKvT786TJyHQzozVrv7Kv8jS8Qd4gbc8KXNN8ZeXpSr3aNqKGwf4qUiWQ7Ie-UpVRXw_nEvpTIKCY4ay7n57f9Dl6gMCfQT4n7SQ.jpg" alt="photo" loading="lazy"/></div>
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
