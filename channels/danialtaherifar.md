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
<img src="https://cdn4.telesco.pe/file/UlFoyFM48aWhwpK9_2FsquVVuV0sYYzb-6YjAz_5XZIQabDKWgoNeE1FDfNsb1x6IMb6aDlIgF8EQCb-rZmUuVeNFhOVj6dXvemIlZVeV-ys_VEuewcdQ5y8P-r62uL9wZIH4Dtid0nEzIttfmxhtMtydNSnysNE1-GVXIZRk4waC6wi4gzzcOqskkfX7qSTlMTmHhhY-7yKMZihYO7YU6y9H35mA0MKjEQAXkXI4ZYpYLUufS2LZQcNK5SnJaWIPaax5VaLHDLMEwyYYTpoj9975ghaQ35qOZAEl32DJSnvhs8qn_0FXZQa7qBHxVbntjodMhZPBmjOk54fHxS1TQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 16:27:18</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 291 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 465 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 572 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfhUGbf4cCpRULpwu_NqxE1HdJnsNaIvlBDMHgjUKUpYHQOR1vsAyLah7lDa9fgRiDTps9E0C0tgxMZk-mlodlEWpa7-mcgc75KH4UzTsKF99tYBM4gQ-yGEK1tthaxWl3FgEVrhzNxaHQY3E3gzsaoGczpQM5YBoZ1itRErFaN7475SDkbHbiFzbIPPZcvbpjpsxp5wY-loIJnoU5fbRkgO2wcd3uYUX2_6ABQ77irWtTM54MsiTS7LuTZmk_xVs7JlpEzS1DmFYJgXZUtdKzBs_xZhl5PYEFWZndWE7EcDB5VMBOuSjRRA6EE3J0ZDIDSYTXhck5zHPt-n2bQZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNh6PrN5ZJfNsNVR_jSpOGWtSVgjNbk5Gt2UAlH0NaHQ3dKDOxH8KtHT5ZuElhP0FV5gD7SyiOS82f8oAnRWXX5dG1E_95Bw3RadqMlKtpC4CZC3_XXrYo3o_2jInc32Lv6XrzMTrNX8VenSSy5noo7xyaQRjoRra6e8JyUPhCzS6Obppw2LZJKjIyY1JIkksKjBKO8kLXDHt_skqfpPdTwQ725BC2NgicJQxHfbEN2blPI0fqg9hDj6K4LeI5syydoChQD8lqaAXIMShfXhwNXtWInrXOrzMZh6ZMgSuDcCwsLdDU2xA1VjfZrYpLpIOo8tIJhj_lhgCLLH7QTSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKIecz6iYJDeFFRxfGaxp1Q7zxBXks8fekuKthnR999m-GFYZIVGJ4XPc1PsQhD9sZYsrRrIdqNlTutFn2d9sU16iTY7E9sU7LNGu-ltr5nk8eEDcxx3KoPT7Pj7E-XguMjryhHxzj2918G7jQ7hn_XVbjY6zZ4qkoM1wYMWh10JrNO7hm1DjrOYuADg4MtPursr7tfu6G17ew86_WjnvS4w9BhSQrgCfwQeWuHGhWG_IyglxdKzqG60ekmeCQSNxVgJMjbr8zCawdEGbVhRjikpGYU9s1_JcEe9EmsYZaWD9rtDbQu78AySv73fejmtSpiLuQkEjZHWvQdvrEe0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiriib2mRItoSl8P25TAhmOisam5sWx-92QX6zsnX9r9v9daktzHPOn1EqdMCP-1l1g9bVKSOgyTaSVs3dnTVlnh7zTygM_lMmIF1MedmjsBya_rrHTn4qBwOw_3wKo7qWM5jFyZ_IoJ3gaWY20XCQRtz3Z3b3RgtF1uOFoCgDt0FXVLfmvH_4a3rarIuYzDymbrdRQTNCAJayaUkRh1beMNwIe2_-y0mEMp1XOS_lFrTf8SFpEatlQsQCtW28-wDoVfwSTXGwyA6h_os9Czgppom5F3xqAbFhPP9fUS3W0RiVirCnt2ZsgGUOxUAYpAvsx-ZGCItGAAFT1Eto_F6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1T7dKMKAQnzqjiE2avk-9wDNvrCHc_4W_gMtWxL5Ekzp_iyOvdIVb49_Do_XJwzqD8KY-QZTVKuK3QIwWB2rbb2F2eBRX5AK_byXUnkw9l76UgFJAkZbWlnltbbrwR_ZfWOpaOQz9ML_fFC91M6lnjDdQV69hY-jJvS2p8xdsUq-Ib79jO421LEwy8qFWGMOH6OrSHNOLSv5ky7tUZDaomMMLPsByoKh-reHnjvvhLshkjpQku7NsoMJxfoQP5GKOnlCICLGJj0Nf1gXAK9GTyR9OGBxhCmLymU_jtM9BOFTTUJXgwvZ3KGWFE5fe8g_n6FUfF1Yce73ggpUpQYWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVoH5QZp2pUp88CsEhJelWZELocFtOav93lvp0F3mCvsZOiWBOaj4kQxnS5cra9HbRAjoRj_rwZ1sI1WMYmt7JkrEPWGT9m5Xefw4o0P2ovZbQLgdFPJU3-6yMuBuCwh62csXzrr43brUwdhCWvWGbFpEEm-6yYZNtUy-cQnVnhKg3EOWbnNx1Ydj5moHQP7xdh2VcoF5jPMNZTOrxoinnt5K7GN8eDw3k9F_E_u_f9wJAu7mOVbd_b8aHWzgCVaWwuPC3dYl8oZsndrvVjm_5aYBCWFtaXFb1HkAR5UU_FhjrjhA_FebzagTXiUY7kv-M0xWQ1UfFdcau_dgWIZFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8TcGso8cqtOSwehiOnnF6vgxtRV3W2FgBTcY1ynC1vxej0RJGT-55qkM9a8MtsKkJX4cD3Pwrh70OADWnFIoUtneFiIhm7XRS8rA8YkCQtWhYGazuLTAdlH0z9M0Y6WrWJyHXUZ_xPH-EFJQriTpp5vk9aZri3qNTn1SwPpnbwmOnTed5q6xjWFmsvi-pKZrHgpFfgvhrSZ10C5ZPyayimIgr9TqJQGfbCyJbqZP99Fj4jgOiRcBZkUurhCIZgrsi8zqSGq3m0Vk9fo3bUyvv_HdAND9x13_YuNH3rMLn2vWu67wSsPxgBdk5ikbtENyuYeD_xw-ogoCkrDROCCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2-EWXYg_jlNxklIOYN6HYgnwcasCvPeDIwxbEWamvCvuvETfjebMo5zY3RW8JFZz7dgPCAQKrN-v1twutnTtvIuos5TJSO1FqmjE21NWfZh54AOJATT4p2To7NhS1gC_0HqmPv8CY8V2fqih0GR09BUyN_6IkE7D9K1o7mCkP-QZB3CNAL8DpJC-3VqHa3iObfWG7dLjBzvTWj6MhG3kWSpZjavhd2gm_6cJRaH3L1CDjIICjxxf2B237p-wRUOB-Fe0cygiYyOSsEsCKkYx7DMkKUMHD58PZiHxK-9InQ1HYG7Obt3OYOR618_J964OZqNtarmcZZzw6vqBNVkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7W9HjzYvqF6etTg3fA264aoeScLG9ephI4WPeYAPSuU8_UaMtfS0okvEJq4MwiIRrykDyiI9A1hUHCStILfSIm5qwrh7t7giPf8huOq0Ve14bzaBww9j_J52uz-CtiBT0Q44xCjMenB6PiC8WPSDo1i3uZVDlKC5KSIeqlP7H3jmsQ8c2yHvJrgqUzZaSCJOcSEoYzyeqv13GXB5pkItdC2uvKYaaJ6D5xuvEnUCLjOGX4rW8hxMj8Ti37rxK6eD2-H0Cu3NCUBzUetJMZb5DkFHIU5DUVQ_CG4ReJXdDg-rgugJ5kDpHj2PQbIkVkSjna2s3Wa0sia8Lv-yzSUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1Rbmwn0pydMi6D4afG2M2cd-oy3MIboKTyBYDfCrF6ijFv2pcE4SW-1kpB0qj1-86bAVi9z0tb0x5PiVXNZLtt_patzgUzUBGbqsDKMt5ZsQL17kTWiNk702ljAUP73evvzA1Sx0oSuRHXDlQYpzHgIYMMTpA4IoS4nISfMMuoHWJpGzCNdIhDP2vqrT2TmNTRlbTDIjIg0Liuc7GjhSqVD928mezLoYsq4PYLuTa_FtlPhS_wgNj3PDnT8OJ0fEGNTSEjq10dFeHMqbOkRnV_XsZkSTI0M1YTj1O7HImXqj076n4_nGK3swbkmVlQQb80sJPyb2hQnIjdBCMUC0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUhqFmaif6CWgyToBC4vEXLP9LFzZZ_5IqmjSPvKNJ9DeHRKfzoWO4eGsbO2KvDp4mymMiIKdlqeEJOprp7cpb3uEEEHQ_6I1Q7QuGVR9tk2HX9JjbDn2uL1SOALGS1YuSsqi2z4EAXQl0w7n8Mfi6qRoHnNit0VM1s0iLvo_7dIlFpCIsyttmfPxRtHcMb5XD8LGrnZyJOLMwTxJrFnW6w0lo8mXbjXjvQMjYx8frvxgcY0U5uvZGcfCNQGCrQBg6WjpOKPjPE_UZZDsXoJcsrZ_q1lCLRs4EZJEwA687sfsikmtpq_CjF8rFuYF_ZpRhnWR1wKrmZcTs2P_vAnEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tHbbfl5nwgtk2PY7gze9QmMtOSzJjGSphdJNb9ptQqa3LO1haczUzGcvQcvwtnQqa4DkK_qdmppma2L6RWOopq9BrKdQ6zcQMs2_dP7h8khQt8dimVw22BVWwH0yhkflYkIuEWrY-360R0G7FvaH_Jy0s6fXpSLRzzWDQR7Nmax4CzRjo3eSKY10qw_vCMC252ccXDRZuzFmyOWZ_W8pK2KnLsPoZJhlgGdL-kxVwabGB-KbZYAl-9_k8IZS4_W-08BXvkWoDlLUY5MrGOp1_70ga7HlgUSD7QCOEOc__8ZFdoE1QE628HqwYRHkbZq1SP1dSXF8yndMebjbPGGo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tHbbfl5nwgtk2PY7gze9QmMtOSzJjGSphdJNb9ptQqa3LO1haczUzGcvQcvwtnQqa4DkK_qdmppma2L6RWOopq9BrKdQ6zcQMs2_dP7h8khQt8dimVw22BVWwH0yhkflYkIuEWrY-360R0G7FvaH_Jy0s6fXpSLRzzWDQR7Nmax4CzRjo3eSKY10qw_vCMC252ccXDRZuzFmyOWZ_W8pK2KnLsPoZJhlgGdL-kxVwabGB-KbZYAl-9_k8IZS4_W-08BXvkWoDlLUY5MrGOp1_70ga7HlgUSD7QCOEOc__8ZFdoE1QE628HqwYRHkbZq1SP1dSXF8yndMebjbPGGo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_i-9AqLdO09Tp03jEqKTpVNZPZ8xnnLytWhPN5IUL-vPfCecMJBYLMmW5ZDrRiB3CtAWLrogZ3LE8JyT2PbfCt16gS0J6zyIE29XxVEFGuqklktUVXdDmOcxEAOPExc0rhyPKsFsSLthcf5rLSE2gC3Gbu_7Hc9W7unUbR-htnfB5tL8nrRW-mDXaZ-huDo3t4cNdP9qrqf2GqZj_ghdqdH2Z42phahfl4oR3T31CD0BRgdXWRhYk231Fe1Y95NuNvP4vqrWZgAwyWe19Mw-p2KqDrNblIhxUqoQYZwdHpjX6fxCGLjgSw5sgQRPBOyXv7BlDNSL4CFiM_P3PO30A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAr63txsZiL296JBT9eNVXhlkw7MMvb1EX1hLBSBW0g_ZhsIZJFk5mhexH0sz7YHSG74-ICSJccHwxyiRzHhpKbO6d_sZTYHBN9eEmZhJ1sH0wpF0thTJeugmiIfcLqh-iC9rxxz-uKpjXe5d8pZOXvfVvnSjMyrS3H2z3eLSCAMrCGaR28IvARteVFYXTnp4Crxi0Fg6XfcN7vkztDjQ1SFVvY3QrUgTkxeAr7MOEhm7hmLSch55snoFvj2XzGsRdeAeOsXEGpuV-9InI1k4ty531jYSf748z6Y05hZu8uzU3FM0ggv0dhE4VVn7qtUoqaNn8NSTd1bBjkKjW047g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jakNW0VbtznZQmfEAf2R-m07XEZZsTqohaDNg13vLtNMYzzLm9jPR1TfGva0Zv_dCb7xWhU1MZVpdXdY-Jab0Zzr6JZXR3unbm3GWV-Cjf1Of7CRACmdkh5cRs2Tnc3uy5MVY6Ez50Osau7cScCJpI0wyX3Y5785t6FgfJdm_f8uKxoH7Gf5Ud4LCPQlfwPxSnoeYzVg9Qfd8c0sieE5zg153qkL13EDjTnS2dAY8eG2GDxTlPgmfBZcfzlIHVW4WgsnM1heH6W-AHL2J8fn9KBa_OvoF-_8jBzObuEafcoXavW35sYNQ-CbLgevIyJtmbQ5QdNnJ7VRabhQxNK0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fx2wP3oLsxi4nQCfuTDB2_w0k8y88j-a0ojCImNxs29dGPjJvrQVJpi6Og2qYN2VsScNVwQpQi64QTfXTOIF8rYxmH_DiiKQ-lH6cf6woI19b6n6YjlY3mqAu25drEhC850ZSB8bAphfnYVFnoZ-VR4QRrEkmyLubkPcPplokdy1l0BRhC23F1xvbnHsUFH1pik-BYOJfF4_dU249XtdFtQrpHfwC_IKGvIzvKWyP0PUJtU_DjwLc8rT-zc4Tu0uEfyvvqJybEbcTL6PN4IgUml-S4a_aREnb_oB7Dvzno1tD7Twt7LFwja9L2kSlt71nxOxwpMGEkOuVQnw5afrEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L66CGrWU0Om8MtNbF-z4Ht7_9VL7jyPcTdb1A8fVgdBxPv-5Rsbl2v-OJu-pDgTXyYkdFrvLkrJjy5P_CzChZtnb-I1XOYfL3Run1tPQKVDKKSnfHtKt2FeW6JBdlb5ETyXVHUnwGAwNLW4TiUMB08qqHIl6nTc1t8AtJkay25HKu2KWxi064FEiOT8WCVag4qXrtwMinjeI7XRfjsY1ubS2F-AhXTINiwHodr0x-ADtw2xQxSZBSEnNBEA2FEm2tW7C55x_6l2O-VVZk73gnXX7g78FMSweebvlLaedKfXaqYP64DApyWXZh3-B8YrShmnHDE263pSWcWvtoQYB2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFc9TgllBvYtUZ9od_3iVCuH3-NCzL8T88M01UJDAT1AILC_tHiGN8N2yrto_EKa_Ha1Pd56qJbfKLQQc6XQLdbaOGN0Q9D-pCdt1uN7wiU9lrjwCaPuLzJA_4uqeZHHaenfYDsS-oydUcwj-LWIKZ4oZP9hVIF0G9TVwtUNemTu91CLUT-DQRO1yViHAaD606b04RGXWsnv3r8t08otZEHr8ryqgBvNYnVM6BmVyCUjVtJ7cMqLMDiiV9ODC6LNRx8hugoZGH4yrnHLZLfCUYICcEw3hlGRjPy2BwxNft_F_35fsVg1iC99-HUnuln1u1IOkZbfkjEK_C9Ftv_3RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDWwlXlKJvCQKC2diBO_G3kv8AatumhObAEfum-YgLcJhMrxlK8Vco5EpXXFwehLaoH9PpED6al17dSxvcG3eww_ga5l_FtglTUEsquhY-TaL-G43nrPLk2FZ0rhumgOBXWNCU5DtVeM8vfQkXT1BqgzmGsPPhm6Jj-Y-yKzNjOpaWf314RxKgrCVwCyfVTb0qLHGr8Xz_RV1FJdMa4K-RAcwfsHwNoyiVBXmgFrG7wK0UrPXbyUoLC8XZZuiLcBXzOKANv7jBGSnVExiYmJljDRcSiG71oU1nDh4VVALAvxP120Cf5d-n0kOnkToIi3WhkwhUbkUO5rXQD0FweRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGCu1m9H7PIrNINlbduCmYkAylaJGJZ5xgH9-ffMG6TwDf174RCXnMiNJSalwa3WaeRPPZLTvvelFHURUZdC2Y_LatUENkgDCHiXe-rrEX46S0BC_UOmKkdJ-0ixd57F1N1BgN2yE-PM_THHKVR8YaK7APFB3HNn431X_TV2PSXdAw93eKrleJgpo6wUxGE2yQJ1BSVBfeWZ1_zsN5CcSJ7lHi-ajLD2zgvP4zRjNRpCS3J2L7tTYawEQvO9aU5rVK7ZobPtYo3ufzIWlE1jd4h-1zXEl5IyNyW-gsTL6XROmlfM66JtCgmesP3lGwhywK3UadnFBLmHe6OhhpONjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaP6XoANgi4GM-wyK8-V5Q1nOwB0I61gbIbvHgsbHEoQZaq4t3lexPKhmGninBF31RuJ7m7aJ5lmoA43PTmz9m4uJu4Yvft6CNl5as6ZhjTrPTnAITY3W0yZhKufnSNeZ2rnYQ1zgItrjd9x3YcNnqqSvTHq22ZCGKLu0rOjDQjb72opq24YVve7svXBu0tSxjjpfxqyTSlxC1FX-aPH57yWQiZHgl-4KEBkTSwLW1ajLZCPyL853ikORAd_sca1JD_PmT_9-GG3ciSE94PEOxV0Yki4j67NlVTvJOn5fFdQGhUIxGlbFUTgrXiO5NSz_DMKaHBGhZU9Wb_o4RR9vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFYdjZGCndxVOySXEJ7dHKvd7VlfzPGm6uX9AaZujIiuqk_pdJu_T2yH9jNpEtkGexRDJabLwBj88NHkmoaB9PH5ui6CNJ0UR6XY7BzTZe_QTcB2vdw_zowvVTST7-UOwnnzazKq70ZxOxxDrmg0IC6J6Ost9rpZleV-9MEG6JF4ps4CVfQgNEozE0XtRoiPkby47cBfQh4Apu-HnZZ4N44jfvssqwXeV0frvc1Z2p2o4hPbJMxthye0AJAvIuhuTxwHuHW6K0Its-EeqdlQBc3aF-zJ2hRkh1dohu2YsuWHxmkAapJd-t0djS_sh4d29bHKPe7ICRw1wvGfWuWewQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJLdjTZVwu5oqqmRhJvk04JnwQDpIBlse4hSYGPs9kbzsJkXZd44cHoVmm7M9FwiiUfASWzQxxpzFhomATCns1Qt3d485ftqJyVkV5Il9b5sP3F7jDg2iKKEDW3v-ES6BISZHBjhkxoTGBFMt-JGrkQwwAhPfUYKumTeS7JM3UaAF3t-_T1Jgp4-FdTHOvA5ir0EAX4T4m0ytSbGRxPTN6H9Rv4evjnSgwo2bmYczNNwkDOStT4-KZIEIC4B6ZCYXtp-Y1KHfHuFvztv7hoYvCyyCz8JKnTc_PxsIQRh0z_EUCZ2huhEnLfAiVIpvxLDz_jb9N00U2qnsE1egEYf5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8xKUZozGMbya63mRHzpTzd7rY5GDEauz3nzHQZVhV-CHmIadZFF5JaVx_BUgXlWMdJt__xoRAZd4PzzRZmu-S8z90fn4gVhUJxUd3spQrRHuBr-ejb5CyRoAD6-Ex3O-KeEzIIFgD_iEBgmOUQyEUZy1hdI9-CaydR57EJkycyAynpUkbm0EXUpgGX7Yeewe1GRbXiRziFzPLZMP07VlhibVtwjw0SwDhIIZtfLJcaFEjIs0rDHYSpEta5Rxn4ZiM0THYNaG3xzSUaUfz9nks13ndTCCcXQe5O5H5fGKkraJGTQbGZikdn4oJ_kIwBdmauig2SZdHCCgEzvw84s_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzXjU9cttn9Dmj8yLmLku0iynTF1G6oENCUo9W8YfCYn8U5O9cPbi4coJxzsoeiB8-ymJnowUGbZ6njnHllQfEj05_RI2Pk8hs6ZVhrq6Y4PUGM2_bZFY9icBLe1Zd2XHAuMXuvUR87zaLzcBt9_dxNoBoOaSuNnNWtQO8RvaJRqfAUMZC6QjLPbnuQcX6DIguKJ3ycP-1ShXxkW3VPcfSJQlK9eTwvMh0P7kAqrbAGkoTsocjlhZvDtOIIJWW_eatgczgN_vAIueHYpziIjLJdPdjLPMb9QAZWWUGpjGMmDHz5sDs8QZ_DOfWE1JRkNbY6PAQG5A_1pAotKVHv80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTn4WC9s9P1O_ZBEJlPNPV88Iego8lJ6poxGgrNF4ZBpvvbC8cOidwk3G1XpnROaQGbpytxsR-6DA5U1rdogD_49QUJZd0gacMv2iOiJITCrsBysBLzZMWeJVHe-v4Ei2doc6Ar6WlvFxDBL4TQ7th33iO6VwgAGNS1zic8cIFfRJXama8k44xU7OVbBpg7BWTUbI0GDyTk8W_uUv5KpBPf7Yt9Un_-c1zIldgl009GsjQ0EV2_l_OrnHf6uM52J-NexRvksyHjGY7qYOp-SX7G39-z9reLqMHZ3X-UtM4yQwEaInIHeh8Haa4H9z9-99ue2NLr2sp0f3vcv4mgLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERrz8_EFvQTzfftN50Bq496QnaAn9yWUNSkjkbLIDofEAu1loG4XecvpzXVDUDafcRVgA32SrJfrbjYWq97T-i5tJxRwreKF81ctGsWh-3utR8eIrtlfsjdKWRa_CXVfXyYh9KYmQsQo9KzZd-g0QVJUPLGWcUkvMQNEfaCNtqSD1QmuTcZ3pEcqi_bljoGMmF4RCfgDB4u_Lr-ZPcY6XzHJaBHJJ4zO8A-AoeRxpeKLni6hhyP8vis5Y1vZrNDsTiX-12vHaskWn16Lvv1tPKrm21iISLVPEiwVQSV1xyYebYJHF9PIQBX8YY40rPoZmX3gdUD1ZMU4D4lGvjHLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8vDc7Xi1znmT50SWMVdcel_vsp7iz8Q149-3ENsKZma5SNqCK-kdUVT-pFOMjBgPbHzP0djTVYtg2ErH4JYlFR3VS6OC17oPlQKOdNd1CJy9I56pD4qsseRy4DyI8M24KgVXfA66gdzmRpzrI9SCAgZC3-mMEsj0Rq4ShXshRW0DrU01KIF1VVoyqYB3sqZ3hvFP9-LZo-2JDxvZdSExwNXLE8NB_sorJwgDLs6EpYkJjFCmnoa5d8-psUO8ypc7DtOkQTsbmaMyoIV7Zib4IEs_6HbWNrvPLX_UXuYJW7idowOqt8V7x3xweexummh0fsPDWvT9qvdlWJvmb2dsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMjtfA16sXvy0i5rzabd4n2TZvrOmTIAVIpAf--LiMjO_Nn6s0L5e9A5LedbykctIXBV5t44Ygpliaz9jUN11ABVku-ntv8V5ephR45BXdEVzavsJnL3LEDtdcETUB9h0oF29lMCmbTN_CjkomhYpdx7eFy7jllbevIeoI_ConhVEfgVjCbinTg_hy5nYlhLTcvw3hVsZ0kajBXPLKZpUl0sp-eqCLEga6m8oOVWgtOb7a4SsMfn4IZp09vBMESg0c3XQeWxiZEsO0Km1yyA1zjHHTc084mbW0qkyBSmjOfOLCTjWCpAIXrSTyOnbvUeAuKg46pt1UBsYP73qddTKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbr5rn4l5lES0cXCRHRAAID9BnzmZSYFp-6KgHjWsYq0WsNPhbvmSSoV--NQrl5f6mZFYoObT1HloMtfuxvMn85ysqx7lFibm54TwzwIC7Gwt-t6rkCiFZHlu0202rTcuaf2UIkLuRGiGh0b7awhmbngBnKIvuv7ZUIZTfc9b5jIU3WXiLzsPb2PLA-NynKhndxGrVQ5y1zOZSUtHcXksaVjnS7AoH9wd-Qmi_mrZjjZk_LGWbf-JJxG720CP3I0A6QO7gGTSVi4qw1_ys0h3LVT7TgbeRGq5z7JYDWyrMR4JWYATxXXDtFmS6rtO20yTHbEY2WRJAOY3XIM80iLFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEFWdDL0vcDMtvUwEg2wi64WhKZSE3VhvK5mG7f6O6jAMemafySMxvthz5kGtFVtjQlZ5p-KV5cSe80mI-gempcvlMQ2rMi50_pMU5m8QyB1IQ2PuWyL82zv3zLDgppbSpGqu25sf1Jlo6wee62RbM-h13CayLUTSqva_u3d0QTy1fbWTu3NhykkbfVhbH3loa6F5pxIg8fW0uXNTSTxphWIQDE_i_wnXEuziHdGK1rZI-3Irt1y2HTU6GsV7LbcqUCd7fNWNp1kTepJcY_OS5uPwdQW1tevlWDyC_lAspKUAfioQ7jSbCTGydgeF-vXZNub7zsn-kgMSPst8gk84w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ucVKwh6MtsgLEWwhnil1Z7WqX--QeWIQLr3RLQJ98gmIYnmRI4NrZ3IEm4Bmt8APYQD83C16cWhtEzRlLU_Dmbwyn6WMdvlDUuwJz9CzOL5p-Yt_Nyppi-C54vHN3i4iqLpQoxpvuSFXUH-iiHVdcH8zYqGUC-LqwZoZJZq4HRTqQfy4e24ehLS13-mdLNdF4f0u5lRnV2RzhWYwJv82yj8wASe_tZMCEZMCdGuJUHuNmzGHgKV27txWQGuEt_LOc4L9bCfoJC38uocaNfrqTZqOkfmJa4ouZoNMg9hh_MMlHXxNax7jU6mE4xrKA5sT8r2qndf26oxlaB0t0wVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fggJXWti8O_hum_jsXBTE8Yeo63mOqGAj62yan_IPrLbiCB74jSAo7968CzaBPH2yxFcxSCOVmw8d5v4aHozfkEs1s6M4kJWOUYcmAwr4hctoejMWWob5GohDsCf6Vze0B3PMUYgk9_3JQGDezORNeozOuAbNcow0bKImrQePhHTnwpjhQBrbnjWwy0WpytTPj8Gtcs4d0fPVYX4MZbmDMQMpDfTSL1Sin49zAiTSbikbYNcFnIFYw6FruD7Mj9kIjOTuIpCU-O7-wU2tmiVCV2KAK62a4E6r45jkGa9-bCrO4C_yZwXJCW8dkaHY95NtLrL-IyfF_0_MN3xRrJCsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwNt7A2pnjIvktKvvHEEHIpjGXyg9k3o8jgYbwP2f9pKcaTICTwcxlFWEkR2VZU2zNKZ_V-w52tJOb03-nZ6NZ1T77xtVIYPsdzqDZLpJS3A5gVecb0Fk3lgRtbusOnyANSzhL4bHtJdTKhirFHO83TidylmTIBXdFy3QhjwGN9mMbxfR1LPlaOgTkCiXSH3eF3V2YiVhhqNybCNxVSFxAGHr-nD3yOhNAbw-VZjOXVWCAVEjYjwTgWzETIwlbL1XnRgD0H5DjDhz-xqBjZAP62Go-9zkA2GAzk-EHu_fHAz3FAeZ4AlVcCu-xivEyZamMsT__-v-C3RNGnrYJA3nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwsKQBIfgfqcTaLhzw15COtKZAKYc3d-qM0bQHoQLwWytSzC0BDY-UC1F5UmFynKOZ01hood0Iwe3jOzmE1D12gLFsGdOhRxKMfrTWl40tmYD-vX64tStxz2zI46VUELt8as1NqZh_4EMzd-Q3EAzEqzAV-iCQHyW9OaVjMllgtZV86bnlQ-ffC2vsLbFldozNmFE1metk-6VXRIBi47ygssXaAWWJvxH5ISKfIn-d65B2H5US6BhK_H3ekyG1VTlURWQEGz5mIKGML_e0LsETALLHr9bWu7YC5geZCA78lRh5BDXRKCDtE-AZ333Y49xWQjX5CSU6uhK9StriTqBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGpRj1-o-mlvV_QDac87Z3K8JNKv_Bk9enknjYNRepjMrsb7Vd9ykEAkcAlPrVGXXgFPLvGUVas4pjlPijWGcs0IfjGmd1VrMjjEGDvjnMwyLXqOV6x21icTCE4_OZ25E0Y6mdTxf87Nzfm7oMOzRZ1NbBYYU9QQhD86iJGbc7DrNeafktfOYvZgPJ41vowg2T3K0-jhWakKq4IRuyZ9Ber2v9290F6av8S5K-9DD0ssTb50quouia3XGW_dIXC5rYtWQXqp9ni7sjJ4GRtm_01XoF27VDHOs-WaG1Bq1aS-XuMGFTEqmdCyq5hFYt_NGrBfxiRajwibktO9CaPdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSPOt4y-Nl9SE4U7OpvbnVrjoI4mzUxbn16cNpEfPFtCBuKiRK4TL4xmSzA7h7DKWZn-UporJlaObFLsnrQw4ZHmaFTZGxrhQpIZVOfIX2TaFd-rMCZOzMuQOn2piLyIowjntdY0IRUSa7HlvLa3fNpiS1Q1hDwdZKWqQOi1anQFwwxDy-3YT_gSxZjgfbtqfTQIe-2z-TrT2duOgmjnU7uZigMSJOz5ckvyLsiubnl4CfPlAsM5sPeCGZEOU4mraMZ6eqhETA-C3ow1GYprqZhK9nwGhi8ZDJ-J9V6w020M5r5DwuPLcLezZE5bXFbKw2qVFX8epoH37AlO7A_3Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqA603-AOF4rWf6bRk-wbUhVXGxtWTCORz3z8fLlStn4WdlrQ-Sp8wCBcb55cZ748HZxLfX4wdNNsod9qurgFeugs381_IeVX_qk-u95sOI_-yXtVh8UXgERx2asr3jAwY-YtGHe90uLuVVdcZqi-5ndZEuzTxnkxmalG7cmGKG2nCv7E2GYit_6G9zIZ1qrUmyvIpAj8MdUfU57MHBXpb_iHWgJYwD1q6YBWliJCDqdVUesx_0zCnyOerpTbCICzrqqQVjdisX1v-0MmqmP6UaA__ZZM2asUSy7PyaLDcjKmiT_F2wERUwGojNR7z8EWXFI8pNN-lUW3UuEGR7Ntw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSYUwqw9jaTJSUN0fo-nbHrPlSmCKtfz6Hvfw1GEbGxp7XlfcwUFd7w_2B9cqGTr1XDijeiBS1QdcVPxVJh2OdHKP1f6gur4mhvln2McEiHYcxWq0TAxsy-8MCvL1a8Ej3F3rL8h_5psmF_JTCJhReJl2HJcPSGHMQRhYmLlC9jTsiflXXtSBGML83rBLABPdBi4uIM0dMWPHtLCLPTjeJwe0N4_WpiC87-ApPB807InHtTEOWlH3H5_kxdHy_WqpI0T5D3DBhF_Sq2Pr9jCJnffeTDxKzC2GET7pXmonheg5zAPoyv7wuzMHAfDffOSEqdtQC0A589JXbeRQkVxfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZX7n2Pv0RvFRfXA8agEwSEChLgu-jDlkLKdssy45_HFTIKgzP0ZonH2OyHty1xsJKVLVYx5db7poVIqb1w6lnMd2wclSkwt9xAySonfUstuOzL0x1zi6U9ETboUrNuTbnEbqZKRuWB2y4BnXwTmj3F5g0wZYBWKbZsDrBngTkuZ8hzBE-jsv-D49X0b-sbotRglQtSNlYBReHLYDGRlLmZJsC5wvzXHz3pao_mxqbjmFnf3_a7b6qidbNpasTacuhaUryRQwSUk94A5ZrnboQCIAcUUVZfH5AFSpPBDcK2bGbDEyOHuFPTN7F4ecIiZa0mU45ouptVBghlQt63zWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBuP5Ykn9ZLvSXiICmwHTt62MOr803tIRexCxBz6QHyUUmGwwp1yef4cpjLVzIdb7odURTUXw_Q3Fc2Dokh-6cbL7K9hQMGpqyuYKeJJaHnZkM2uBoYVLU0dMCZkBV2GVtjUTy1Ot7cUinwAtIKlwzJo5lFW5dUNUojNeiWYoid1VBki-jSZBQmiESsVkSOvDzeTwHFeUbRYWBYf3VdA0bwcD_Mh6RJfyB7E3Sn70PfK8CRhrsL0DoAdCvCpWqU_ZON8OjrH1AxWOeikeU2prnNCfpGpi9R3RfB9kCmw2SvxzjE26NYVAzLF2yXqjabPg9tgTDqJKuUofgP-iMe78w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Whd_2IQ_Als4HbGYxs2U3E4neUQCiXB1kWzpz2D4fMB9dOP3y4OhZyxtf6vH6ZBQfdgsUH5HCl5FyHjx4begPD14EmOyrHyjy0QbamOlAyHtA-HZlHsTBCz4HOIHLobwSwpwP-_ZBeTDYmdwleWaER07YyteK_JPV-Vu406j78DjrTkfZ_M_hR2arzPe7_SBLrKTAoKI8kh7_0IaTy_1FGRR-x7Mkioe-kv4a3H3HNYLcYl5dDJ77ydlXJzQDuZ9cYtJHr_RL7Nig5Tp5YwFnpcNT7Xuut1BjDmcjbE_Gk4xe-h4zBiBrsUvlKcmG8kEqo4OCuSJgMQNO_Byf8F9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ebdy2W_doosN3cAyYZRZjIdBiMi0snB5XbyTatKRsfFx8DxwXj8B5PHvMO9ugRrsjhQ20i9NSCBqYV_QptRiN1h6p8cLanq_FjJuCAP4_lfm7HdiLmL91N1eKWxeZkImYAU7rB7nzmuui1VNMPLJI3WmmHiz_yw_oDsH5FOYq1vHVhs5sA-lJqiovdICxNnf4rLd_bA5vCUqZ_Xo3pTOzqOVkTH5pcV1Ku5vSdM_AjiK64q8SqP_difBUujsaDUi1KeQpmPj2atXjffs53SmCWu_i9lASCp5mbpFXsWxGjc7ujOWzgV0tgATmVKkXzbz7-fDk5V39x-7_f7cSr2Frg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKbms5cFYrBqX6Ojyq-iISSuOIiiKqv39tuEMJi7bgYRcb_NzVYlpt4id9JLrBS6abGGT_80tBd8WjCFKB_mwRgLNgWvvl9n2zsznZw4UdWH9SQHRNVHSR_lU1vGt5GAi6KxPQpWWFZQR3-cIQYpMneiyBSSTAOHSWuW1JQSHJaFuOK09zugy2zO2GHdve5zaBncQQkTDAKrajNiMAEQDQUEpfY1ucLQ_EOdOGNs_0Zth3TRTBidWQPmpXGA6CNgMuFPFiGNEZrTarwz31giCFM1-esY1LrVvkLl43ewiJ4Vc--Y_wkPEqhuwOxTpOq3y-LhmTKLSwP5SI83wrbSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBV06kHynA1VB9D0Z4C67I9g0vfx40er5hixhyHSBT3y27Kpd3O7EpNiB2Vgd0FmdYGFU464T9HxMcipx558957akDqJaTrQ5s5z0uOvSyf_bD904c1QK1ncKXeo9u23XoPI4hRQiTC0JY_x-9rMNKLHkrPbY7ZokBxtZ2F6o1-kAJzTENwTDd3MmUBG9yWSoa5jRIhoSsszEnT62v4B_BHBwR911tBofJITSEfbfkhHSe_VmVPOhZK0Pq_tNiY36ojqMBQ1geHXF79kxbRGCvT70veEavpojQ756TIudoDegWtuS6G_Jc0TBi4z1osf1-8zlJnCMhVwkpFkc4aBlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izek6Dxza5qmyl5EcyD8xpgMefbcXyvl8kSpxtol59uYDrYbl5P45REdUIPf23gG9yqRPN6EEitkrhvnCmDrUnF2BoWHw_KLREsfDq-rChlo47HScW4ombdlN3IhotYVys9UWmLi0xmnjoE0ELBcsUmPvQjlLn1G5PeF6FA-i0lAwAHQy2BdV22_zx-JM0_VjBiGLWrRowbNBqkhVJh2_u5_zfmY1TXsPn9hr6s4s4jXYv5tgM6WefqPtS0c3l7Obr-XK422QrLmFgniGD-lmLuouV81fD5hpLlr4UpQARZ0z8hFz32zli7opcaLlRGe3aDhA-lgxsCXGjYUaKJl9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGaXD7dxSik7fMR9H5UXhIpOFOK76SxqmcIg304O1fxiMJ7nqcQRRUPjACySFMJ4ZNZ75sGBsxdCXB_pFJ2tZQKtg5jhqIWEtiT5p-RYYwfA4Bn9stct48SSF506BsrVuX6K6NI3LmlK4PAPSmydErZ4Td2hHz33D9O6RZsnDKmkEHpNK9mOffBHQNFG-jD0X_b9aSczXl1P-SqhOFLdBQGLsHBDXtK8NMPNwkNcFUnnWc0qvkCbwmYK8U8DZaUOh7u3ckeND6LDw4F67CXzI0q_WbHr7R5tS2wrtt0CnecO-3kA6zcsvR6thNVnZCV-vYPuOJBQtx30Q7SBler3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVWTanka5TUoTKdCLDWJohZkg8lWGoNydVn4H13O8f9xXJJsy_CnJfi-JK6dMQZDM5cNs5AKI_2vkbJd-BFcGn-YI2E9lxkOKgAe-D574h3ouoPojmG9dwOiKzMapgrP9aH9c1c8JsekBRAgQ7V0WNeSPIr23KFQaaWE0HR12Vxjt_uY1VvqNl-F5Uil4brMWrlJwCSFxRUkPtpp0CMODDQLAZ_DGjFcZL9cendfB37Ru6A6nH4Lw7ljhMF0-8IXQwQEBWTyb25NBZHGG_n3tVIRl0GPE07iA-gmJLaBXoKr-yklUubFvswXylQtHLOriR8-a6P5CYvPXipaEJ7Y6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsD2QIZUIv4AbpPWZCWVNfowSydBzKEbC9cVeakpPdYmeLNzC_msZ4bMl0kmepppTwXAbtIAyk9digKSUHlj_JYICf-uLtpjAKm8_pyCPzqcusmiX5ULl7tqr4Z3syJhsbfFtnZ_94v5liJEvmaqyw43Y9xPuvG9WCGooe4xF3xLiSsYH2NWb8UE6zJi75uSzS1lZf-MKqWz9gV8Ym6WU2HPch4UAt0ffAQHq1BiibKQaZwgzGVj0bbGXy6lxcUilalnMI-svVUXYV92cLa7yVAgbpxE78TjDIDZE2ag_ZaIVjoua0hhGYQJTWSQCDazQK0CU6HHBG9_woBWgHFMQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek-lDCoMNLoUxXrz8EdyQ3KMikNWAhoGpmGw2RWSdR0rLzzmradkR_gtbKolvfFDBiUgECc-FUJZ74xCZkBpJVAIPb8W26pJ57_4h44lJr1dIwVNGL4SYxMmI9omjJ_Q3ieUSW4TRUriZhIwqrK6vmf6lZYVVbmizDFOra7hKFHWftItNEH0x46NA0umk5Sf7_jyM-ah_cF27pYRNKnr2HRDgj7Wx0F6QmuoPFZtv9sF9MOlLCAsLP6tNbmgjsUtf2Ej5eRJtDPFNiUF-9pr5KKcHUbWp4h20TVkw1FuI1wP74orfOZo1I38aXjTgC1crkwKnVYQIh9tI9pCKC02hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMVdxB_EFAjGG3VO26BH6LCNLdoAWEA4Eo_YnyaeqqLbLDhyYy8xvx8fykDbIWxgZFhzp01MiwapMK8g0oJOSESllseuQlVcoM1jSSXXKJFMwhXRNrvkxC1hhCV25OLcwW90Lzxnr_H14LZ0SCFqWJZvS_GDnNqvO6y-ifZI3eoAAQmu9Wvl7Zp8e_ggStwFkAjj1DXG6Zy3dvh6KqH3xZlZjHn648PCiFiOZ_FSJjUBcH2Csft-u1PFLCYiJBdaQkPl9FgiCx6PzHoulNmyWPFK1ZYc0-Ns-v2iViscE7I8uqR_WrxL3HzyFtCfGmfsbCPLFTaQLXsFImBQnc9hVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAZsCBolWmybHDhus6MXx_RG57W-KWBeQ9bwkDc9SyUzckABA9wlJMczPCe-6obVVYrRzLWtT9famm6vUQG5GoMwjIodu_FgmHTShJ3EdShOmhujCTUIJur7ld9Vwv2UYKptw0L96gTrr8fjk0FFDU0ZrHDJOCGahVgB8lgU5kuou3GS59xQKlVRxwAfygRbHE2xZQE6agwAfbsVr5B1bA0DfzYyJBIxEJVmkFBiEi73Pm7DuFGeRkN7Z_O13px9ybFQP6nTC9WLyno3SRAfp3ilK-DL3fiADlt1W9JU50Cg_5elqLdBnkfIHy434PtRbqUf7qDbvk3qN9EQxS6OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ke-SHJmN-6BtOBlWG9tASpCY4TqJOg_Zg8Zqhu3SXoyNkYy4X1Zp_6FovIl15xNaq5y0WtqXthiMGI91YnamQfPYeysg7fJuKRRXDSNwnvPEBGU1hwS4VPfoi7NCHyEWIDSKmAcw4NLY82N_Xtzebpw7WHJD9tMYDFSgnf0c7QFuO_XiIvyY3MDn3v1IiAb87LIHDm3A2Bd5APG8ut5xPBt3Up6uQdDD2kzB727VptwgF6S5udfJdPrLnR1G3ublsAao6Rwq00SWa3gD0bbUk9FUQOiCdF5Yd7Im7e0EonKmUB8uMYBqUieQlU06PineMWhX7ZxqgjLYUVeH4uiBVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3lIe_piws1cJ5d0xqIudClx-gt43De-YW8nyuFhvEWkhPd5vivw1IS6R3oxagGp7md2cwBuYVuq3vxBOA11xOm4MK9g1IWt-OoLu1We95zyi-C-u4LsRcABv8VQRSAavsGXD25JWgacaX91Z920h2ApjYlpf86vCuX3CLJ4qeBib6Dzi2fYIGDMpvgHXz2IOvRcCgEuNlQc3uzb9aAB5lcf2-Zi4sN773Gfevexsvz0UGHCn3srMgBVmFSIO5uOGWK985X109ilnNFqglj6X3dpAGNsy2rCCIG1peghO23s1f7UgLTIXpUxlzLWPFVxKnY-2Fx4XKHcB6WNOqR1jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-uzXipdN0ME55kY31-VulhWHWEwFr0eNBT-QLTeY8yPV7hAdvpnaxl9diu8z3gwwrPZldeXO7VARMEt5g8Tzm1HnwcZEq599pVjiuJoSoqHsjcwzcpgMqLGwQvpe5hFRLm1RA6vv5UYkgoZInVzywqhxpyROjbHY3iCzAyeQ5GOul6qnIqpH6CS1ozwqrXFIsfXFjRJBe_-ZucC9WYnbLVt_c1r1PSdNVlhP4QVyYKXPAL34bWWAAxEOLEWaMOMk7uwmzZES4ITX-tf0EK5YrCcnAoA6RFc5a75Zym_fy0Tixt-Z2iRdrCQE0qWPN0sq4qUrEtq979tCnzwQcasrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5kMlLasBKM3k_K3WTta9-l8laRuszetcewoU2Eu6wD6ooZP7nPhHU5eSBKi49OrH6IS69qjYhaSXGijPVfgZMk4sMqsX009oaLbnwS6oESqB0MHykYwjEP_fqqJsXqkOuSfNi9SO516h77WdhABeW_d0g9y05qKdts6NwxdmTLt3th3HQMpdofYpL23S0GBpu4aPxDUKfopMLFsdWjbxk09ESl0q919alH_yhJdHj-ym-Y2KpTlLMJoOLy5CTyidZqFCoh1V4QZXWK7cm06BHzilig5DpoNaSAxCoMQQpZRWYir7JpSGMWESzHowHnRewvvWfIBak4NDSfRUWho3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI4j6HE62VVH0wr_-A-YNFuPtL7n_Rg432qHrJbddEDQqV8YkbiWYoQDGjfYyWf0VojpXx68CpZsSb1jeH4ZlB8zIZsonYN_Cp734yrVZ95IpvvF1D2QFyrQz2LGAnL3OmKjBM8-8BxgDMpc3f2zCKyqLxXxEljXFv56BrWLjykMbenXsAyX-Vst0XfdvJ42VW_TbWkS-qRWl9u69qvtbMB5_o4NdhPZd5_03afRRV9rH9GNyeVgh-Eq1IGgRlCyfZy68v6p4mX5SK7gGu4SyfUn1xcbRFaj1HNlj-nlr98Zgsvcop8Pj6IjyGLYJ_lFewhVJMkwj2C3JPLn7MN2rg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=GjPi7ETk4GJPKJ_FzWX3IKP48V1L4CB1VH1pkua8HOH-sMI9ob6y3PEcBVbkFhC2zV4PBlwSwhf69SAeXNkTwcN8I68llJTJeywK1Yu35v4zhBvys0DNAPZjqiqjWioGsP3k2PUtCuGHNt56erwpdwnHP8JGZE8P1LUHdCoQ4b_H87s7O497ErzQp-D6ZJxMReeQeGlIEFXe3cWdPOQ0lh63Ks6WSYXaPgANdDoDobLwLmDRCaXlH6a5qUk-i9DgH1XDYIYYEmBTRqPeDjRx8SFDQi-7U8hVMSBUDlqe2fwD7VpTL-i3FyxlKvUg66dal8iUkBQQFL2KPLQNi0C7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=GjPi7ETk4GJPKJ_FzWX3IKP48V1L4CB1VH1pkua8HOH-sMI9ob6y3PEcBVbkFhC2zV4PBlwSwhf69SAeXNkTwcN8I68llJTJeywK1Yu35v4zhBvys0DNAPZjqiqjWioGsP3k2PUtCuGHNt56erwpdwnHP8JGZE8P1LUHdCoQ4b_H87s7O497ErzQp-D6ZJxMReeQeGlIEFXe3cWdPOQ0lh63Ks6WSYXaPgANdDoDobLwLmDRCaXlH6a5qUk-i9DgH1XDYIYYEmBTRqPeDjRx8SFDQi-7U8hVMSBUDlqe2fwD7VpTL-i3FyxlKvUg66dal8iUkBQQFL2KPLQNi0C7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYoDtqFazgp-fIeCx7q0lsCjWRJTgGpwr_tWgAsj5YgtJ1XHv-l1M7ZOFRGjMwRu6gpiPbD75bOprtckOo0ros9i7CNK5xRT-peeqcZGC-_jy1kiCVoVnQF8E0IFvDmII630tVWsTPzGZIJQX2PEntq2cTtZuZY5tPEBnUkyQ8xSm-kin6Tik9JJGVC9qZmGBCR20XIaR5s1FazG0pNwWEImkJylDub8D_BY0AIT6r7nN3XfmHERdpDy_sRIaGHL8dr_LIpyxxEGmt4Mn3jgHib4ITshyjaZiwvxf97Mk71MsOSbTrzuM1wQosqEefB0ol3OtwoiseoxTzBQxqxn7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul0IrlaMpqeXhgwyRLOYyBMU4_5VeM2O-pp5-g580SbmQg0_X0_BZ6mYW26XJiNnzT7BN0anZ3vC4TfYOJgzPaO9PvOnWJTDbHDJ1Qf_Ix4riREZ38P6AV-hRBiip5CSntDyO83hYAUZ1C680FMSNhkPZrw4tEyCiAcdnzu_vjDIfZU6wXDYHh3R4_CViCn1jt5YJ_6OrwiaSknssYGTfKGLGFimTe-gM0kcc-HWnwSUnxoNzH9h8WjdJoZB__SOw_VjOpwKBFxgp2fnUSlxqDl0FhlsDnVupV-9Cdx6nBPbzNV93CBf_4hFKiUg2ehEuJnnxxbFST7f3FMRsl0bIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-4nQEdpcwH3Iz09o-3TP8uYyrqNwSsM2p3Lewu1PT26aBLH98YNwZt4XeMGCH0WPa45J7Vfm63yxYeqpuQ38_r93CroJ0OdG2mGeCfHEAOU7pNFikDFndDJhmQ2iRHB-OLvhi0aunPLV-nGV_QLMWKx2t3OWbjSIOVpEiuKSSIrO0NnnePaSTDzUT_EUDlQdWhlhO2XsoMEcSilLIRfJ94QjQF6mDGHc5H5bHg24_qsijaG4mE6VD3qJUcvhOZv9r0JLeyTbpPLrAllNHx83CrdTxbD1yIM0QdyUeICh5sHq0omd4xzfM_TjJDCewAyUort8vnolvTomKd-j-rRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2vpwrKK30zhtHxJ-pkq_xLW5nBSAVpS6WSpuor_QlNtMzQFAjmN5KdDmPyeZ627qteerYPsgHZIjRKX5riHHRurJMQtE0FEFMPmDwoh_yvdpOP98es3PDH0VZY9kplOJoXr__fZESPRd8ugGQQ1wxXYhNYYdyooC3VgUhp683M4rWDC0fYO9yEDYPk1A3qc2DaCbvm9D4B8IrrKjkORzMcYOwaoOUetapMWFJcak_4zaoJ_UAJhvqJE717DwQEREUU5OpWcbIAkxojSrVK32lF-knG39tXhOrlSLCwUjXeaYK3HZSjg04AJ67XCXpUxlS8D_qmAbeuPHzqBUfYWZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLWojYZ8-1QbucAFzFuvy-qgPFBWZ8Z03fH3fF7vFHJhLA_thjsnLIaWyNthGf55AtPjHZhYiJHhuZGD7e-4xDQW4-u2eLZ2DfSQtXMdAzkK2ziKUv9ay8h0c2p9Z4G50Rz_9x0IawN0LMlnkX3Imh1ikkdU8ZgAG5pLNTHMYWcTp3JDFDLwSl1VWmZUxnYZeDqSf8Ts7pZXnb_cLyVZbyqPTIetmf7PVKUZoKFNBLYcEXNY-yZfjdw4voq2kM5PA8s43-RE_5Nb9wyLf5-W-N-xvwOs8kXRboo9LhgGgLmaIGXqjgWdJindGP2SzyP7GQ46e8TfK6rXuBK7fqvk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvGVVfhe3A5GrnYcP5ir_32IacXPXgtcoFTKI2ienAD8w33EedIaEcUYKcP7jx2hbhsl1EH6eHDxD7NuoCjheQq2p5JdS6TWWL0Np-Gx03FLGCzXqe2RmccfL1mSHKgN-oKoudBbJXsVNJXYbnaRPI0WfObeUiFmpI0SKfwz15W7hCG9rFa4Z9_kL4pv65lNxixpKjVIxQZ1UEKTEFCECxOQdvwr_CAHlEEeY5urJM9qvGjZjCWI2BxFtUJ7NauYQyLa6Sw0YgcKPKdk6ZoRyanL0qKHRanZ9hcvRxyIqHgaPgAwMPKrH7VZvnPUTM3iuhoKaflqk4KNEvnHQ_bM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD7Q4x6f1pIQBCmGUQ8RdWiJgKqZeaQM3Ls6Y_0T_cFHWbTo8oiGHwDfPkPAmxhd7m3KvvESO9XP75ikTSJFF0UzqWKCjB0G59UgP9w2J9zpMNR5ijBn0p7XPl9LevD5zJOZpn-VGfB5VFEeBRqgRNk7_WPl_PotVuKZVhgBiDR8MZ7kMUXwXAp5wCeJppX6l2ZR4e40ksvSPpmBa9w1BppGQYk43npeAltrUOTA8Ej1_yLEeilzSoTOlDJx1x1tBlOs9Jw-NUB5X9YVKOXAZdUQ204lelh3aVuHti5g7QLBf06ooi-eT0hpabElZ2cEkGCuNkArfhiHTDT3wlTivA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=mf-6n_53Y6XWjzVTqyxpo3R7gSVEwsoSNqnFLc8hH0f8WcXKIQilkBbnajWX9yl7UVzFkpGah8csxu08QdBFuvMdoEnyEPocAGyVaKWeYVfvomQZ3oyb4YZ1tjLzCiw98zBkoN9nvE92u4XLo2X2ZK-WVhKyb3Dj7PobSXaTrsOhpF73QIAL1nKKphgx5N7Q4frX7TejDvvGGL1y8f7IcmtToE0iDtqAqc06pusYDRK72Ob1xJnEgz937UyST_mFKvvNsJN7uKm03i6d4Y-xgaavshGn0cdgNTghM8S-mCuGERNYnQtwfEb4YrFq5U0suqXFnbFPQ-UXwiDH2mUxq538WgKmLQDhEhn8heanBRdvXXmziZUBqc6Q74ny7TyE48qxPW1KCiT1lOPovNnUuneD4pAL2guBTGm5WhXWQfCII8KNYPZZQZyY9uWZjTJptF-eQBWKbA6kldVFVM7JMS1V80mtIJd_h0N0YN_9sVIV-yylV2juUK54S7OuT7N2pq6WOafdsePZzGoUxYwJueX87rRxM2bVMSLNYexAnAcexEpgTCfi0D9jvmg5v4sI38y31n5um1i0o7zf5mztRDOQO5LWYjEWIR0gjBNUVok_VEBVLDREgCqlYR1SrncgT3fgdgz_ATVHnadlYJM0x_GRFTuP58GyzIoonOtpVH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=mf-6n_53Y6XWjzVTqyxpo3R7gSVEwsoSNqnFLc8hH0f8WcXKIQilkBbnajWX9yl7UVzFkpGah8csxu08QdBFuvMdoEnyEPocAGyVaKWeYVfvomQZ3oyb4YZ1tjLzCiw98zBkoN9nvE92u4XLo2X2ZK-WVhKyb3Dj7PobSXaTrsOhpF73QIAL1nKKphgx5N7Q4frX7TejDvvGGL1y8f7IcmtToE0iDtqAqc06pusYDRK72Ob1xJnEgz937UyST_mFKvvNsJN7uKm03i6d4Y-xgaavshGn0cdgNTghM8S-mCuGERNYnQtwfEb4YrFq5U0suqXFnbFPQ-UXwiDH2mUxq538WgKmLQDhEhn8heanBRdvXXmziZUBqc6Q74ny7TyE48qxPW1KCiT1lOPovNnUuneD4pAL2guBTGm5WhXWQfCII8KNYPZZQZyY9uWZjTJptF-eQBWKbA6kldVFVM7JMS1V80mtIJd_h0N0YN_9sVIV-yylV2juUK54S7OuT7N2pq6WOafdsePZzGoUxYwJueX87rRxM2bVMSLNYexAnAcexEpgTCfi0D9jvmg5v4sI38y31n5um1i0o7zf5mztRDOQO5LWYjEWIR0gjBNUVok_VEBVLDREgCqlYR1SrncgT3fgdgz_ATVHnadlYJM0x_GRFTuP58GyzIoonOtpVH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEiNsoReEtLEqHYtp59t2hwnD-TBJl5OUG8SN5_7cbwkXOAmm6Rje3IWF69gklS-7V527hsnfpehFKLf-aXqEMBaa8CJCQGbPwV1OVp7DXRyePX3XsjkrhsYvmFnnFhFla71Xkrnc2XM5kC8j1IVCUayItkVSFAJfTPsoaA12Pm48xNhZsY4V8VJJsxjaSrbzzWEk81F8mvKrqB-nCT8Ulmeq9Z8nfgzMA19IniAXxXZ-ryGES7qBYfrQzo0u0IamTSni4KHHkDidy8IiDmfqNBu_TJgvdysOxK1WQLHwk1lCkqHb_9L-AO2lGq9wuqJyPxEG2jJlyuWLc1IEgPrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGH4pCGpDwhGbn9hHiukHr0nnO-0MGyTFLY4tKZT6n0v9pRTfGN4N11KFXKPsW3LmIwoenSPAXMEXmtdlGpZPJyhuuoK3a13djGyuLllujrhdBEayjaQ8q4cGR7fY9JzOWiV1PE5W1kytXIo0hCpZzcCf7mR6YgHplMnNw7kwXNc18ZqkSYpwRp3YXS4-FudqE2qouWU3RSfDe3VBBadyGK0tYK-CYoR6z7NV3tG73Us5xhADzPJSmRZl8qqBaRidi8hT-4XJh8jG6zO5Rn-ZsHO4VF9FzcO7dCq67DZDfirBuhZ10HkaH4zogFzjepz43-850UedDsNUVydkR9LNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZONGA34owhlobQKQAwmxG2NyfN5P8ywj7Kgd5kRB8wLtCG1lyUt6NGzB90S0tH8tKiEF5Dt-tz0EJSr9d0jvn9fd2jmmPc7rDsHs0OkI2-0rXvmsXQG3FdBjj0WIVZEr2YrbbSsxYadf9NIOqpZttdKIPPRflcjJmzB7xphO_4l7NMLLLaXK9NknKDcj1uqJq0Q9xkazXpRTt2sMmVqUPSaWY0nnjksMZtvDagdeCSPrIrwtnfrYC5uKxvrtorraHvbwrk1ixmPhecZQpjD6R6_uWNi1pUO2vaeLaRy0MFcAFa7mQOBW9L5xO25RnjvDq-Qf3yvKxRdTQ7SfLz9yIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvnNY4KBNwTqEkNZ4QffEF4JdJmTS0SYm31sXXxyEsrN0HaLdSp9X6CrewT7_TSgTRjKyzQGyfBrK-jpajM5WLJjBHYH4RFtW-cK3mdLyY6Ud2CemFIdaKSSXTWpP7oi-5RfulepMuCIupXfDzfxyToM77eVpiOj8MZhveCiJ5js7FxG_woY5T6Aloc732MtTyGyARfJ1Gfbr0Di7sXgmRDd55eBkAX-Tu51WvUBxL-l3OCr1yvm0JATXxYYmGGsb0wf_zPIsMMWMpX064G1ncSC6mRG_uTJtEM1Ql6D0wMQadsz60Ls7vc4V68nOGk24aFRF5Jp9oE9tPiOzFqfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbYmoIc--K_aE9-LmYxirY2NL9wB3ejUYBrBklAhyzVYAfl0uPg2FAitUBdXc64F1vitAz6Ox3ltGblWEHvBzLycI_-ZNB86LgM69jsSFoDZ5KzRr6IvwA-moNOgg2evTZH7LsWeOLVNTCqteHG5lVut1zsbZpDqTbnencOrqArVuCiT7P9IABPGDqPp8bK6mRCmDObcFkimMI6WD4y_5VzKvCHsC-PpfIzkUuJM8-kuCbSTsnCbwBHjx_dDDKmS-UtzaE5iCJ2yeGoJu-NO70ahOV0Nb4RESYkCdbwV65_pK9clYSjcTfKvjs3DLVlTTkOEwVuFOGKUreo7YMT0Vg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZZ_l5Dr_G3KbqxK6ZpqfJnYZVnr7zdevdUxOQhyPF8hoBY5iKQKpsA8DVMXfwgk6nn6MzQaXo3LtVEPqWzb0QgE4bwkpHN54S4H72MGf_4On2h3v5miC5R5AxpA-ajxj8HDDuhpS6zkOFdCUjqBlNNTVgCPuE5pv7t17F4Sxar61rO_SXzFsveRI4yqdT2sSNoBjk7zbsDpw0VAvR8OAZ9Vtt46QLQ_4ZW0jotUfOXmfP3bOb9uBOB1M74SVXxCvEI25Vfq8v9dyA6C5WG87eiBcUr9jmSK6ORnllK9i3RwhPT3w6Srl6Dziz6wMo_PE9BPJMFoctCUBpIZKjEO7n8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZZ_l5Dr_G3KbqxK6ZpqfJnYZVnr7zdevdUxOQhyPF8hoBY5iKQKpsA8DVMXfwgk6nn6MzQaXo3LtVEPqWzb0QgE4bwkpHN54S4H72MGf_4On2h3v5miC5R5AxpA-ajxj8HDDuhpS6zkOFdCUjqBlNNTVgCPuE5pv7t17F4Sxar61rO_SXzFsveRI4yqdT2sSNoBjk7zbsDpw0VAvR8OAZ9Vtt46QLQ_4ZW0jotUfOXmfP3bOb9uBOB1M74SVXxCvEI25Vfq8v9dyA6C5WG87eiBcUr9jmSK6ORnllK9i3RwhPT3w6Srl6Dziz6wMo_PE9BPJMFoctCUBpIZKjEO7n8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIq2acdPkTeQptotbPdDc8KEUgDfeYkxqKESP0gzAkrBYHnTNSQhbby-cmjRfoxgUWuX0Yk7pTs7_lSLyplVyj7udDpiwjgDMog4gpUd1eN5GAdtDbzxyIb0yQZckPoRe_r0yyA3RNKHE0t5eKufWM1u3Lenv9bZdhZrKkpze8ELWZrO4ve8BxqhxEUK8Lqlv7jqKv2XuWLhiOdafED8iWEa99c1AXXErh2BLZjReU1a0bNw8RpAbQAbamdUTTSsRYeVFyNJ2mpCxqpbIIEPMJpn7C_xoOaQKZ-rPUFTJIP06umI1XJvtxBv7hRMdd4T7iDoCn_yOTxFuVA2Dixxpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRFDwUbX_o8ERyrFYZkIHzmg7Qka4KMptTqf_tPxITaBwQiilzWnzTRYDhXl6WIFmiJWYz3vzLrrLNQwG-YEuwG64XCumJENBz-ujF70mmsLxxLvkuCf0IfLFlL2qpUNB0at9-EFWJy0MqY5iB0JOGga0r4plBwxdheANLmTNvvNQZ2Onz8_e7NsHkMnbCvPWOs0FeALjCh2jKv0ATo3zNO1AATjzt1ovuNFkOuYSKDYnLiWaUYWvxN5ToNPdpKfJkn3Q30O_79wn-BG6am5piOiakbuX_K3E_77YqgToY4StYMN4gcR7fwLe6MySv2Lp8L6-sdg1IXj5Xa2_uILzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlYEiXZaFcl2eeCAAiop8twJOnjcFlZPyknRBFCsoXUTEz-vKrNMzPqFnit1Yx1edG1CvmcejGnDUDn98ihFOs3jcRMozSLsOdaXPrG_NSi2y-5nI8jlMPCi4LiKKMWrtWDg-DvwtnPX_5fjcjA777LLGMdVcFPZ6NDXRVjIoI1xrgtT8H7ENsZxXoNzqNc9emXa5opGB5lRpd1VcpRTJowYr2mlvpt6iGhLXAjnuH-V1Owyftirjxwg3Y3nzb3AJo0Z3fx6ulsJHEkP7kOXMz05yopwGKd0IEMZi938HSr3r0PuEcq9Nf4ssA1VB5XfhjHuQWMtzrwCP2XJ0nxFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU7VzPlu9iTath23PbFE_UNrZjXgPs8YtL34uVxG4FyPiPgi2JbPVMMIBw51Mce6IzQKG8Z_Logv1lax2rfXT6B2axBvkkm1LQSG8eKpgPK3b-n06sTAOrp88rYIcZt7R1H8sWkgt3tm9eQUsKROgMXLRzCpM56lLaJVZ4cshzPueI8aBtkYWCwS6XARvuI8Rn__P-twvkJw2bVk--yHsj9BCfqTxFigXrqB4U4-gJF485ah7qO_gvW58Y-QI37y44IEmW_MnL8iQOMq_HoVHcj4aXw8Uein3mJsV1atCrmtlyvegGeXK4CKo-or9FmgXTcvcOd8F0rAPFWMJ_yBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siQcXMs-6qMICWz0XDtzKIN0G2tJCLyiWHWRcT1HpE4NanUL0Ff7X-5GvnT31Gxe8k90oFs7zJd0L6acQhctsFkwiVGq0GhT6MAeXXkkwkXiOforuScLgJZrEGKMkbMz-Y_ohQ9QnqJntlfGyj0zWWcWIZQNqIWq5Ms4O_zt6CyHH2CT_D64_d2YBNdUlv3WggyT1heeQ3apP_l8aQA_i-vju0kkDntgOnANHuhRbKM0ejtp98iBFiNx8yivyuJBy4PtkAPlMQSW0qi_7bcnrOiqCeFucBU88mEVeSutEY1mTmgfPjIBWcLhilVLRg94ZRYs8XEEkoeKdcSFTxF_aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV4mwGV1OUBJDirF2GUI0A59JPIVX4GzxzwJhOIbLWHv-8fQzjMlnAoJzt1wUJYhOLd2iX4ZzIbAw3M9VzDe0aoFjVNJDE-1_vPTJFcSNKjZGz42zSxLbeDDDudRJ9HU9mEWz1AJIBZhNfURQ8zL8_Tlzo8hxorfkwvMtO4apfYCgAp1VN70YnU8B2v_zBrFcFu4nVYuaVS3xoQVuqwLUXYEpRjhhA9w--y0nW_yjFEvPW9OTcxnojimr6bkFW_YuE_bNSp5OSlCuoX5t5FE234ou41QTPAeg73S459y62xKy5LV5B9j9FxF9jFChEn9WyG96bvMrF7qqTLth2r3ew.jpg" alt="photo" loading="lazy"/></div>
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
