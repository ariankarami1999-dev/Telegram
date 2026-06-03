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
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 05:34:28</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 334 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 497 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 600 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzLpUUkprFF7Xk2yhDJpROZRu9zb0FXd_mi-VC1IhQVrjXaVuT73uffRmMNDK63vBpaQaLcMr023P2MyG7rerCYSQxp8zfbTTi-2vP2HA-8iPEM1E2A59GkXB8cVN6x0aaToEzMwhIWYGHwbM10OSDmVeceK6p9c2BGfguz1fcIOEW5iSPvaET759JBHveB74DiECUQSGhrvDucCEidqVksu_pw1ulprXbNyyTVHo2BbpPrXudgU_hqLd8j0aU3pgOEGsnuKZgnfOan9lgOajHFsUmTGhs6zVAWHXu0uZ2glxdDpfIlK-kBNbPR0bcHMO-bfVg0Dh57_TVqqDv72Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 633 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaAEf0qjhEHFAqlGZK3-xiNWn6yHmKdyWqT0tTFXoXYyTE9O9_P77BKlFn7_Y2sY6dJ6tQtpQs45sdIYHfJYqIS56vFDvKer7S-5kz5W06OV4Qkak3OeGRXEBnKAcHaikw8GBKSlC5vjvK3hXUCI805Qotn9XHs3_JiDPacCyN_XBIYOE-3GdwMsIKir4clyJuYdvc8s4WHGxXPSlbwd2rh-H9iTYzx4lUDRthC2HQNpoAhxFp9Oeic0n9Vayzl0ifuM0K44TcPvStn7N7aqf3oUpcVkXo3cwglRPmYQe_Ct1G3u6W2APlmMTuQuSNBvVy7o343MifAFS_rSDvqt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0I1GR7UgADJfvKHje9HMX3GgdHKL4ISOHx0PzXb4H0l4eAV5k1bJ01g7qfWxd4vIuQBYcK1Rx6G8zdXxxi56q3Rux3VDNAD_s0SEk9HjnCnZQMqywF9lushQ1zXizGCqZmoDLCFAPNr49mfnKK3A37R8MgVV6sPWXQ4Ufb5jIViOpnuliUFbS7ltV7NXdV0kp12H5CJ4XcLR2wtXNUgUlbxtdqc2WqV0D6WZPXOJEW3MQfvkb0LJQCELix1VljA7u5TtuSiluijAeltYiCpiP_MESs_w1xPxOfQSsdj9mRv6PxGj55kV4IuCIoCTuqstWY03_MH-hVzZm-nVzD0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 838 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVzkKgTIsOPIq9k_F2b6YmiQCZFtmDaLZWbm-v8Av0Mkj_-ssdif1M0B375R9VRkZyf-Hp3h6ViZXbyNW13m9G3-lyzom8iOp7i8kkh0gSBA1lNRpXDTBDmcMoXQbMlFAv3769Iz9LlGT_rO-pG-MfVlrjeNquVMsbp4reWhmTP_ltMA44l9nagJVdR3KsKUQ1H8wZ2e1Wv7vgYOWh871sq7VIUP158qscDogr7-IGI_F6g49YZ6MgXhybKJYZSjjc2lZaJ1DP8d0rFP98pT1yVss3kpjl1SKMPT1t1lWRUkrr-e661wbjqQlEvK2TBEA4EqwUctxziozBCuyXPRAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG9rH8zQoqgQ7pGdhEwAyTyMLSQEsEPXDfTWN-52nbwI2vdUSGVaszVSXkyfKkRKoUzGMv9FU_mYztgvqxyxa6XqveZb9UEddHSCQQ97fBV7DyHsEF5BMrYcJZCl78GFD0spVFMn7c5EhRJZTRUqnGlDNTJHVQfyEh1H8IaTw4wcoGQazlu1yumLVmA2144svOBKOtV4UdHJaiFSOF6ZGnTywG4WpEPY4l4SAsfRcoAfneyZTJ1F9CU4KM3nPnO05ulKWmNpoivNU939zlKBLIHCrhNCRT7S1dl0QksOpERBI079yZoni69kqItdiZu4rmVNpje_QMaZMr73OdLTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNSD8nClVm7aYYGg2Wf_c8FeDdenU1lZRHDGGn0Zg3x-mLnK6NPDQW7T2LeWW_I79zppdwd31xDdcIorxjHzNaFFodmY4n9-SxDnvCViAn-a_U0D5-526OtZ1EEBTSq4mBj4fJhyaohhFe7PO01iBZUCwfweJhDnMhiF25wYwEg-DFNi-8b-kbokowexcNJpbbbfdtkcLXmnHHnJHjOCkkRWZiMO3SeCTIwmfBQRBo7DyzQ4Eb3ooeKoio87pzsoAf-lXOUgDfFXaMP9VmlsQPCSk3APlytAa8E2jFz2fLkLpCBf1kqZ0nByVzNV_CMzGW7LSR1S3bXdUNVUvG5tHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 656 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzmeeXHd4FATRmlK_xkV9pBBw1mNqgDFb7zv1uP_vTjtBTKFpPJObufkEuRMuklv5z3l-Ke_zHSeyew_u7QfUHWOHkRjQOkA8A14cQjIFI6Q7axTZtwU-8lEe29Nn6jnm3CG9BWc5Cwa-OqrbsnYhne83Ste-_xMy59DlMfUCOuEmhA-uOovWzbmfcJLw-OzSAcuGUnjxYOttqaLJJ-YYKw5ojjlQHOOcqT4WWl8Y8JSV6a0rxZwJNXNu-Z_OrRzGiG-J6bMIC20cZbmFeHuav0wnF62NQzSUdJUSHz_4UZqMG5Dpp9v2-5-RPCZtsH6ZHa29MbJKWqmDpofi8kvlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXj54YnLZCNttdUw0jYuHdLMwbN1VJpHx4jkcbjR_cYfoKnIA7f8J718WDrTqw9TEScATnxq1W7LSZU4a9ecjq0kxpX2kOzhKdJIDbwIjVYxq2H0Q6QFfM1l_0eBmkDD0gKtSrtrePvu7PmOcECivawM2AJSIEBe_Mmjo-n0fFh3nYyOdAGtwxlk054d6p_evi0HVMmh3Leq03d20Jfoa7EVP7C89ZjqbszPIfP-gDsatn82XEdZ9-c790fxnpMBZL5U0OAoul8hKtJJQJ-SE45se9zuNEfDa_OXpkn6bXEdpqa3T-kKLqTcWhz1_tWjap723mrK0_UcTNKy6gFj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6OGQszlkx4u4i51xvVqtOlGVXPO1ao7knfJMB4ybsnhb19kpTRX0mQQSCAb0aJx5Q2VIZW9axspam8mZAeDJLoEW3suWL4Gr3nK-rm9M1PvWuUuc8Hcv7ufhRejB96g-ahkRC9gZ7LwehTW3xAOO5FriPgKUYpaj6pL3kWrCzESzEzCLBpN8fQwHYOKeMi36jzWjIu10dqxaXrpkjdhrtdUjU0gnCo5aYSn-syEr_zZQGoFZQNlOYnUTfDoIfH3Nix6Ir01cjvR1HfFz3pcYPQQI4ipJLdLvN77SbNfbjUgoVAiostcgpF_r4miKmFe1z0INY0WzNUdUEttepp8cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8OHkAZE3SbYq1tK_r0bFkWrLnHJu9kJUM6NHG_sHyTgra4BH0BnxnHy5zpDvpviWszgXnhuOmTua8Mw342WTTAH7rCmcZGrhTwjdZYF9O3comKA-Q8PsnYfQivwxv5-6clz_6F3QkgbH9vDFhc99UIEslpsplAYtQwF4Uj0QlypAvf1NXY1nh7hyfhTe8vyuOtUfswImH-Z9OeYurpM9VKwhGH5z5pl7se9pktSjncorlmjnM1XgeJoLZFvQzXJ4CsHuKpI54oIMk9klSliGLTeXvaxd-AJEbfACP0rYFlsZTZ8Qj2nTv8R4MA1kVFzUfLiVOsx-11WabOB-KwsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtyKCbZo5FZBDKL9ufe4fPtr4VQGl3eo95uqmEHhR30HqhzCfnRp7DDkfzTPthdiju5EcvlEcwBWKISSRyP_4tjj0V69vdlcrGz3gWNtNZ8M7nMHIt8LVtAI6UioAxDHvm_iq3n-0tkFGlAhOtqmuh-RMHMaMbvWLGWkkX4OnifZCOlD44wHcdhSwVHX7qXhxlwFtkAvj4cT9KVlmdyQ9NnPC72TcawEu5YyAdG165-qRQgUpt4izUwVwKLjZJIAP_atN_FZVBAhsOblJWarTvxsXUa6PhO0399bfBgKqtq6LxrYR0MxAQTqFOpvZORo22npQGtA4XHFZPQcxz7xPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVwJ6Q3-MAiyJJcdCUDaQkqCuYPCxOXoM_9bx1Fpr8w_RYzRzqm9xts6wsUt6GvtxoKsr19WykA9SilM5wxJTZK-AAvVnKqPiUsjLYSMUwIRElMuc6K3m_6Na50p0Xjb53Y0n94_al8c3ftwrMb2QpehqIwPpLesULPgQ54jyiEEDb5m7RrI84Fkg7l5s1rLvZdeo6g5ha7aPgSWHnm3hVMJiGszbHiijQ8IQ_92rsukt4KTKa7ZaVa3Oat6kre7NJ_nhn3lFNhzOPn8eFgZFm7G8v4ASrxbV7Nvy2-44GGYKYodpVVyQ2deL6f0mPqC2OQdXPGwoL3Ap6oPzA7EWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOc2oS25Lae0Bx8jjslNVVaf1aUIxWoPhXnoCHw5xKeANBxva3WxnMmwIzEX5RrlzH1lDY31i60voHpMm8B-CxDPHZetIlscloVuAsn0W5BTq0U9ypQM91YpWJDXHyrmjUIAiLDB4msZlA9Mu8iBeMYStL2MaFOjvU_vMas4B_InCLXglNJQZj9qgE9a8XmYrNoySdH4bMGIiIt9K4zkguKU_jWRD1zlxKczQJHhJUP7WMOGN1ldcKZGAVD8bo537qQ4fUbeqre0Rh3hpNjgstC6d_FAC6WDf14-Oq3kcEvBCUKBuNt6nu_m2XTu-rvzRPNMpRzziglx8H0zarYfyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARdYcvNXf6AUyCQp0GOdjE4FME-ZC6w83craJzsRpAexuGpPLw4Vek8P3H-m6YMpp2LJAG7b34mQmUcwFSFiLCTKirwIJMK-KES6n7s5MYN7sEHG7PknGcBjt9xA1RAPDlHv_in8lRigqPwoSzvbHjK8hxtQkLD15Jfaw0_JOOigAiXVoMEikHMIdA2Odi4Qr-HGheH82MNM27HUI7H5OtVDqpdoSMQqo2WUoibfckUUESlrO36UfIYU1cMRdbXqK6cQ6x-VtqFtXcVkYU6eI01Dpf628YK7SHQgyRMBHWvsk5i8lQ-aJd_pe5d5onFIDl5Y2qGySsD0vDBPx_DGIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=nbRSnCnIv6V_lkfFeAp0jXPc1W91__vGzBsTT46od2VC_Lqra9BByAYJ0Oo9TjA75lQfyr3cujqHc2Qw6kFw0tVe9VtHtyPQDDcye2zYmBBZ8OuooNSN_nXc5f3lFTITP1TyphiW8gUkJq54yKOcQp1bn-bRanGxtQHave0muvu9aZzDdiJcLLaCQQbQEYyojMBaJaWVbfBXvH9Ujy6Wd3STz7L850zfPCeoc6gwTVnbL1fpjN9p_CEru-9B7yUQncsOCh90KvwNuj2htY2577ZsQVl-12VM8nfsWkLoEoPY9mCqwS9oeLW6tpArRj0GNmMJWZ5Q8GTaC3RmfFbmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=nbRSnCnIv6V_lkfFeAp0jXPc1W91__vGzBsTT46od2VC_Lqra9BByAYJ0Oo9TjA75lQfyr3cujqHc2Qw6kFw0tVe9VtHtyPQDDcye2zYmBBZ8OuooNSN_nXc5f3lFTITP1TyphiW8gUkJq54yKOcQp1bn-bRanGxtQHave0muvu9aZzDdiJcLLaCQQbQEYyojMBaJaWVbfBXvH9Ujy6Wd3STz7L850zfPCeoc6gwTVnbL1fpjN9p_CEru-9B7yUQncsOCh90KvwNuj2htY2577ZsQVl-12VM8nfsWkLoEoPY9mCqwS9oeLW6tpArRj0GNmMJWZ5Q8GTaC3RmfFbmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siIQ9JRY-EISgzRvQRgw82kZHoFyHZ9hw7R2HOC_8gdfe2PFlyN5GMEbna3iJRHLq2g9MGeQPofPg2cV0T17t3OV2md1AFFKqK0wvSUmpXgouGe2PwLXSPePmU7I_jkZOjuZH6l098YztQBxrrHgHM0oDvUcx82HYiqTFR1dO9gWnZ534-z3-nIxAI2Q0xXmsEK3-dfYzPU_TNhch9AVxMq2mip-dNZkpgVm3LyFVTZWBc2Ntwwdpb7BHJkFm6JenFonICi_jOjrcVEUP_CBbPIQkEseKCOBqCqmBZts4pUOCSsAA2PyA9zEiuGWreKzhYuHsrnrTpiV1JeJUvMiKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWeigYONI0jAAW-BQBJPlNWciU9H7y0mpg0Pf5aTgWAnGvqAK23xAoi7mYb9deHSZYsu9bzRS5utnJWBo5ut1hJJ4KSfFnF4nj7WHBGaW2fNj637RSXu5D-XwmCfbKXk3CfnXuiPwSJMzDULS-YhkbooukDw5jk2S170LdNaR2JvuveswmACHsFPsugx4arfIfe0WgvxutIstUEs2TwuiiGzcR0_Js3qI0P_qaKDhJ0FFP6RF3ggqVLROkQz3GJMMnP3wC1MRY88gTfYKh5BkUUWUJM2jpuMn0-QTs4JyHHFKlk-bpgdmnKXwXupNCUrGTJW408RhVrtevlyZMKVZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJ3wUSHQK3wd2h9AA0Sa3YNMmXaqcUsUd-tlgTpgNuVtc0Zynd749YD-WIocKtCIqsCd9VWOZ4JHgdv4AYY7nSwZ2OfmrScvyOn9HDkvoodtTY2_nCeeVF2XZd4b6IPmVvyZJuOW0QK10CXYx1Kzp8ppiCCfbYvW8eBayGe1BxYTt3lDujiysr0vgM85PJ0mstslA3tLDZUEu9hgI7IyxIkoLv8kpzOKPOF9coVW-xAJdW1HGPJdJoWWkrKtHCUGD-rXd4GrbdSREyNLqcPeqTtHhDP-l5g06Gvs2sC2vYN4pGjZa-DGcG8l8Wps_ZH4zMUl2exydLG0ywoE8IJWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIc3GHpddVMm-DDa_zwwBO2tRYHUsZk8ZqoM5wPUBp01u7hN-l8uyhkT3AjH9J8xDPAG0HAYeHuY0VgrmtrjvWPYeD02iCeNJdMSEuKRO1M20TzHLigvYdcgIjW1NW2kufqR-cevumBocgt23SFEIFMvhuJ_hIzX7iNavqgEA-RH7FHmyWOXexq9gvXtZzklZUw-xG5eGYayt14H5q3UU0AEPad4g0K42YPQvFfhndN87EEvx8E2do4__VGfYsJKra98hKKBLs2IMKrckN2KAk_sts-kkSrOnjazuAHfltNXxfF5T3iJHQ6KqdpSgjouIcOoi40YMxGEUkSTMs7XZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07wO46AbyGqOkADF89DtxDXS1WhiKxpjxFcGzRYpA99IYTjNRUuWfJ1vzsTqFoTt8JGkArN2THobwndKco5AnbnWYDgNaD_l_rbrJsHqPS8g19RFBeTkgFHhM3lnwVK4OcEpmMO08owx3yw4L0gNENUXA2XScJ6jmTaCuXGSLfCWSMXi6SCr0YwhfM7byBpeJBg-JkNV9LyQ8OpEn0X6wgIROWY9YaGqBPBFM2qV-aE7Khvmq9c5_rKT5v-eUa5ocyD3cT0hTUddPyTUwCUojXvGgvlJNNTD0I6qOwjUEF2Ve_K9PkMzi7qjk9fAJXUoGBReOeZqjFhalPI3l3Fiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3PpcNLDpgB63kA5SKzerdLR0bEZJgmlTtyvgV3DQ5eBNF8e0JmPrEbFJ6qIlP2DqkAlWLCYx1ZYY8I2N-Bo4xc0b_Im7sDoVyoW2mZTgUA5GdUj8nUPPhgGi_CJR4pZTKJU4BNpm5InlFQMVF64WSd4lX8ak5T5TBDiOArdE4XUuw6QjzOY-g98Jdjkr0mPkcVtv6vKNIS-6_lSipBshNC5byXpbHnubt5L-3gG3rsFQVUBjLquOFaMfE0NKgWglROQKlxfLYTkDsaZWxaqu5uBkAJ4zJ45vGFSdy4LkwhP9nRqbYNt5VE1XUIXTJFeO_JmqlP_Ln98gqDF2hqE_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3xC4KCkd3Z41Ra5OOjJyBG39FHyi_sxL8kas3ao_qiR_IE05UHCoHroNEZ6RANuduuyayPacgl_VG2hNNKWd0BI3xtGVtKxquHFZp0yvv295PuUKqQm2wpG_b5BEgvfLT-qFuOvToVwnN22hoKCI1YLnF8g6dThwt0ryuPsSMI-1d_1eZa-UsLcwqPZJKYMx_8cm0ghe5Fz6JTXrbtXZnmAOp_bDgAgGj6I8QgW4f9TNj86s8K-QzgN6_UfDjMPO1eEKtH1W8dkdeiuCFMF06o77ZBT6v43hlQtO7BItR_OJPZ6GNzmFULPT5sSEB6If9bhbT6qjRk7CgLbXlZ4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AS8m5IeiNZq4PpCXEeUfXEpoCiT1cohWXoBquj1G5_NQOBHJi03e8XPj7zEaq1Fb_I2ePlPNcch5upzimhTQEUYXf8G7cqK5bbTpjCX7g6dTLgS5gWdeYO2FzmEEgjIMDzE4MCiIKazN-n2IUzlyeQAH_-Yom4Vm9J-Jlz795GyVDFQwRJLobuA9IJkLEBFinEaDKRCUbyfVJjxrs-MDOKZwhTsCZT0hJ7-MtV7JWAHIkTHYD7DoDbquJSeUAYC0raHm57mUCMH-FDMQmbQJfzkXVeCpvqhPnTw7dwoc5u8Hgo_RHC6QxHNL8dfUN9qUZm5eX8VAzCX1HF3acpFtAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 750 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ0EMSbt-LKsoNjdpNU9QMrmAI09b7gaNmISxVlypjPB15G37YuzCUgiTDkbR5N2pKaQSaEXczSTLfWA6zbufoDFbQOKrkRRkAffwQlgwMHusqJxhLlRJyfQ7f2OCkDIzn_zq8lWwpR7NWWy4UBGwVhy7G7HJApqTpkrNZWi3zZcKl_M4bhTaBYE_lELsyZABB2BB-m-zcgLNbwlhfevM10oVCggfHCdMpdFF8mVNaHkksM3gd_w5kB3Z06WahqUYErsLuCk22fjZqyCY1uC7NdQvtxLX8c_U21YP03cwpAmUlpMLQzQlH4PdnXZgFLU3xAvJCPL_mxJsWFn_4OZJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPmcUIm2DxBP4WAMJaxukZ7CXUVq3GdKrD2gedLc7VI88rPC8cLcy1xJY1_kaun-irqzpeV34NFDM3G7RK-2TDZGm1E7CMcqMcFz9albvtB5x1J2R4qIO6oKHQEBHP8SOsdBcUR1-cu02ENhN9X8bxagJjT76qHTa4hzY3Cb2BbTmpXhDcxTACsC8w0y2pLYgNDNhQYvxoMAXPJtt1-KykT92yms1Zs_WkPp2RI0OfhNLHg141JWNbd0sD5Yo1sFV8gJNqg1f5m6v1v-iuDZcmNqCPkW7v8sGGC5sMpfp-lwRxZ-frVAY5ok-J8ra-K_5PoPekWC5s61C-hl5nA1eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuvvFoU0QJm7UAd4jTnpKTAWVnUZI1N-t4T7XT716g9fRdYf7fOnX6yQwCJ5Sh1avwNsDYHq3WdhUGg-HqjlFCTvp1UB1gz2tHVG1IJ-kOfTBTbylxYt6yoUxzuggkYX4HAZEz4JN8VtVS7pUtUgnjEPLEspY6Oc0nXbwgKWAx2WzSxDRitS1WAFh8IjppjKYvKuUgyV9xMk81M8DfWnqUHR-XoOhIDhBsc7xphEzpb1WMgshkKma2HDuAvH1KIiZPiEQUW3KVma4AHbaE0ApbHg4kmzV0WLbzNNeSLn6xkXsJ7PyI5J7cdz9GC_rRSIGqZwY_ofHADCpAXkfwb9zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pskdwUGm82_9BHbRMXbWHJyr3spUhaIThbbrIX7OfP8P2tIBr8mSYvRcB6GQl7oZQyjp9AEHtJcO3JaBv_EEaUgmoLaESU2Wj5i1UVssjGmqTijZ-ZnjCtRm2VU_dxy0w0AJgNcGTLULxYGAzqlqYRONgD366PcLyaYnZpcbn-rVHOHSp_KLpWsJCK55RB1v_Wz3Hgt3kuNZ5bOJ8iaSyI4HFmbFRCocoyc5Xjt6JQWj7_Y1t_NwvGvuU-vqSA54Orpjy3pvCApNudP9MkRMwNvw-7-dRDggOfM1qyMgPgFnUapBa-0dUqXTEQ1yjow86Nbg2NXnP_OkYrSBJfxoFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWB98q4BTyD7BIe3BD6g4EQDfhCHu84epRhiOkxSZQNeSRyO50h6YMinRxiLV0rQeeKCQEn8Kzq9ltuXo87i3hokF9QyU4oEpANXVro5eLo1v3GpqPDRh3ZShJfYah3AaboVO1OkBXSPWG1WCh3IcTzo_2AzXFeZAZ_4UXj4OpTullrQsEDQGmx-5U8gRxfRE2s2mFR2yxjx7OajqGoIeUNLOX7WPWmX2bfTU27w7xAjcAqNvpxP3JrfdlKzbokuXNeCuIbjdCLSt2tLbu3kfu9Le33xHv6h42MV6Y20gwfhlQfina-Zs4NEsoHu1xhA9W2g6OPnQXQZJr1NULhhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLmZ1x7FosVHXfjL6bRcP_bf8pXm35V5alkzy8GQ40P_u49PWIgbxP2bxOXVF4bSFzUAnsluGbd4wWM0IObprrGieekbIFm32EJS62A5bBcdFvvhJMbOXdhpzZr0SJ5q0Km3oMbNx_U3jvoqWINwlCn5CmOT_YRLtSdOZkvrSPCMKS8twVLpqym5ddReVuZeSWUdRJ-yDOmh3wbg30DUR_pgri3I_YhscTR5bIzRjBxWDvOIxo9tfUx7HGBzW3AiOYwaBfoi7v-jDrnERZ5JmC-ALswsHs3X1VrHdwYTMYYXT5cM_7vMoLtOE6QMsdNncQduTTjsLlelqPsgHdHBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5UWgQztZzCVHUbO89l6ujeQCZ1K4PP2eaa7nN_WiDgJ9mlT0aZFpwwuRgl5AtMwLU4EKgRrLLNbOEUalVxJa7OkO_eN5_47Az-i54DvCdpTKjA3aOqZEDyVA1J10VPZAeay0REMmm0U1NrdNyJOPVgA2H4uj1VsFGxPvQN20I4O1iS_-g0iAlVfyaiVaHddsMHW5FetB-PTcAwYCKC1vZV3dosLJhfu6lizbfD8poHQutiM_wtTxGOjWfIX06nYyT98LbXBINutcTbv0awg8FTZVkY6NO4x5V_M7BVjxMc0fsIZAzb8KHrQyZmMe_-Fymp2I2nENG7FJvl2PfnBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqNho6_zJshs15d57DxzT0xthdNyclvU3TAahbBA_ZJOgz9RAneSm1fsAyQaljnlLER_eBOEUzUv6lgQYEsXF5JA1xfikjZNhrLffP8l1KdWz8EFVy_B1-z04FyVJLONFymgIXwY9tBPbqYSE2wfW87SHnDXSw9XkBGTxMhi-xG2fd6hLao-tisZafd2FWfx_IH6ERMnPr8O0Pt6N52G3qKMDvFXWEm2GHnSY5lLDxlRWAJxm2dcJuVEckH0HsJB_5np3CoJ3l_4_4O3SmMT-YRZQ4lzI7NfSEGoU_sxcBq8Odw9JpR9EoIJ4RAquo4PKlavRupYjUdSglnzr7kiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ucwry2se4NmPLfLhu2cst3abpBWSEork7Zc1R0Bgs1Ce0JYPr4QKElNiLOjbljpteuAmv9yQScxOS_Q-YHpgJu7LCN4wpgfG7h--0KoDqrdtHYTXdiENfjcnvi6o0if6l1RjZyr2gMaFJt1rYTCnFjYgTEgXTIzQFS3tTvddVg85nu0Euescl0x0nH46MbnoGbkgAblEaGHnJisxiUFTyx7L4QB6e7pnX5Bo1cpOun0GPnwHv89oCiNFbbRoZGk9wzFVQSlTe9yWNoG4cBbX-pJHysx3-Q-zcFv2knUIVROznlW1HaJ0au_l3yoccifhaVg2fSWm5RoItngemsHztw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4QWhJjsUt0w5Jvfivsrq27r76Cwwg-2nEZ6nLBYvSQXLDV5ouvKUrMtZ7Iz32V82Cku5kt6O7pi-uzcDjoikFu4qZMMWKtigWLmyoLQeAG7vtKLHtlfC-kCRuLcXid2eemraTW43KWGDCQdwMAODMttOee4EIdpbOyyHcfzlciuVQm5mA8MhJJZM8OdI8mwytU_e8eX_vHmMALaJFa-bASLc0Mb8LpsyopMrQmaZDyvCBWKNrpMkI1XLvFoCZLk8aZJlpdEkCYeYxkYXLYn_LzoxlWioXcF6-voWBiscBXTfcNg8aD3DjJ-5NWgMVaK1smLrl-NQS4xRGbfldMeiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMancM-OXjFvzOeSdJ7nTDmXYHEWhHkqq5JlB3UBCx9GLHs6CCoCu31U3Jbo0LkS1kp5DiaURQ81oArabEGzDuNR-ARXbiFgqOBncbTVXRLi6EYtuhtMbf5Bf8tKj_WuXFpRv5K2tUJq8f6weLGGmoVRo9iq7-4-ILBF-UfwMMQOmPnXsyqFFmRMpPsy6RZ6LH38KsCBdpk-Jk8ExSHB_8RtxFbvIM5RYQq5qG__ZuRZhjiSdU8cQTxgvnHho1zOoqmCTgmn86SIrgddzP6bN7M_ZPsJVlffd84Ik1V-VlKm40jZP1MpTnFFPwudRDBWecE2sQKW7HtxuJwJvfTolg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLVluqryfkHYh_a9-0V_-CBU5oVGGr4tYexO3RZNmIgdOzXsXVqTzruRKkfbDWcvCi4VwE9wg8po28MD1FFSC9etQHSuKK7sUZd0bdXRLBfcpZKmL5AV6PsQtVM--LluYhxagrCYBkACdTQ8TfFij6J6VDeHO4RuENBCHFv1kMNv3MEEFpJ2HaKbdSnK3M7cHFhW3mIwQhOS64oGZiJOz849ipCdqjd8DCSS0e6-YZTORUG7mm3R-5mzeaRwXsSBky39LgxWZ9oTGqD_EXVNn0PhW3LPJ17Gavnv9u2jNmHlDDFPdGl3BDxa0UCO8C6kt-L4ZzzqBL_d4vOeFQgHVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqgDyB2rzxwclchowAYxxtfREJShf-WfxLklPaFlxEcnpbqFLhvCLiz8IQqzYH_5iqdj64dq3I7jr9V2GYDyALwoXe51rfvRwaEdZ1er5P_DiPgMJ5jpLihsX9A3lSc1jTAzbLcx_9kMXBwaHwLN1E63IXbcEERIQVsgmVljm_9IhuhBzsZ7pF4uGukBUSjNUHAa4XE0JEJOE2IOoOZfD5hRPtzPmWlR6LX7cda4XOxXSlWTAasEKsPtMcaUpC5LMyMHodkmxCy4ifcqbphGx-kML20WxrEghY4TrKTUyYm3HBJzokfqdZEPk8wkFZqpdnvvvkSgzQNLOBZWBSaXAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6ioaqos3JNyVF9_he04JFjqj24Ce9WzYVJ1GNXPcvOGXv8j3969NimmQWGnErraMi2aykoYd_nfJpTqHIKWQoAZOmDkVHL8D69Mvrwr-DpaYC6kkzegAysJklaem9on6RfA7CQCLjtK2J3EUusc0g9A2UW342bN3QCe2quSreOLTjSwT9idmOTFKJUISNTw6fqTZGUDWSbuZhtgJxkA87lG0PkfXrWMljTYrLk9uWSifRSaV0JvePYpS4WTAgqKF6BmpxO8QzcgJTmClExdE0SK3TKtXip689AggbB2BIQjs5EnKPNahmAxmC9tx5SsMYATQ0DgnSVhWp3a_vLajw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp6xpqDI76tbj9Hg-0_X5H9xkGcovB_cfZJxK78sycm04AXbvEFiKQxzo_MVojKJ0-onqhjC3eDG35-yG5IHcWkunbErcNIXA86jYiQ1FElhl2-w8LlNzL9n3TWunDyY4mfphuNDW2f4ON_CKSlnweSHJNqMMdP6FWiipDWeCfM9Xoe4KjR-SZ0AGDR3-1BpugEZUO_X1qqCgUufPeGIcqFa8yWB3Jcu7VhNo4NFXHK6cUESTJGF_fYu7ZM2PGG0AUpt6FrDGvfujpU1eMyFFf3GWr6VXN-Uny4-wt9HBzVSQsomJw9e5ybo2XG7IFao2JemEFmiY62Fv_G1dWaVyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuVOvoUfLoiKE_4KCWbjFkS78Uir2qnujdm1P77KTb7VYUiJy7c1eqS-RFJmYBs5i7imY-DAhPxYZqcG1qhVSoXWq_lJTbLgqureh5XuNHdfRLxuflDmhbzuJ9iFcyEdKwJZvUjg-SCAIiLmSvl1UwrLzHn9NRKj_rZ_Bo10euKUIRS3uQSrIWav5R5TR8ir_JdKGBTmbrBnDtmKPDAJyDl9Ixpz2_LuvZ1EyEJFHWBStPaAXKz9e3vk8fZWx1JZGT_AGMA1_z6jN7Z5O1hUsxMSrP-UyUFgVFZMdhZ0C-juBlP7xVRfa9mWjuDCcn9yOH6HWYYWWBw-J4tV2uQCMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHfOJEI9UElLkVlr7Fekt065dNhu0HI0kESYN0Xca8wFYbn2---kpbjvVnkLrMpjA4nJWJF_nMbFDKEuO_6liB41OQ2JYXy807OnqF6YDudjECKerqAo8B5UGVaza-kamjFOFgPJbaH7t6NikLzR0_-Z-8RbLELv6uK3lGZzTT5WNSMAXoMMuWKGkUjXrH62BdfYRo8HFBNM6Xd-w8kkqbST7fYoWHLrgA6qjZARGiTAGp_5x05mqXR9yYaeEYFoy2R7oI0iGHmfy-hxg490eGUpMIvfXyygipSTI3Yt3vvhGau9gTkKuzcYVLNYeIsPCxbQMunxkP4ijzrBrosNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tn17cEHg8mSzIiwtvZaAZBHM5uvJDQ0IyYhmA0RK85uV_weUWwIYHV-fRfyolMlvo7GyBEr_C8WUhXgWYg7IIHbKyZZzoU6phgFDVpgZQIZAuzuKfDJRkgkCm-j6Vo4ydC-UqxFrrCFYRdRQWqRG4bP8MQh1WQzq8kM8SiYtHqhgk9L1oCYVs_-Gi29gL_uYv0hj0B2kQvAKIj6kWY8tC01to6W8Rnc_nJFnZtQ3bFtNDqF8ll-Qa8cNwd3y8JXzhJaYl02OsQre0yAMuPMvWo8Z6sukmSnUBUomNY3ggj0y5DHIIHIOs7tWKVtPwQJPZUwjZs0YOjB8LFa9rayBPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGWTabgxi4-l6BYiV56wOTk2LUX2CyGRJBn_aid-AFOA68T-_sCAJvz1i9dvgjutlQDDlB40Ef8bqy2vcbDvwVXOkSQZJLCaeK6-DCicqg-J4qhbo_S7LfikDkQhvbHsBEs4_ACvQxDbpOU9sPfsaMMNARpvkRkhgOk9kjbCXh9iax0QRhNZB8Y1f9m_HOtg3Y_TQCVBxhmNMzfpEkMm9n1LCm9Im7Jo0jdiW-d3-JF1M27JO0k9-eR3lRULZEkaTluWsilF7h2ZrkY2TTle9bqSVSt-KL0f9fGVKbnkWluYvbbmGFyrz6YO7MG9W7pi9nBZLXwWCIdDVWtHNGHb_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw-UgbwT5skoHntUOlJaghFMnREfyMCmhgQ6jMkqT16V9KdT8RkkBtspzQzw728prMl7iQOFT6TL-QuUC6XF6lam1JRM7j9vVNKk-xbsX7SKkRJaW06dinwyU_6V1PNULVe8WeubI9vsNIsSRX7XYQRo9bHa0w5QP8NJhkHtjrI4Eou3PppQQOUVCjebiDvrhbm9kyq9CyVb03lCC5fd07e7Mv9LvGrTg0JigbLl0Za4gXJ6a-GLv1PMRu3Nkmu305SPMPBH1kUhCaQ8NJXp28bAUvo7l6mn3BcsYOmgxQ-5vn0quoTvEbIkekOYo8glYTWGabCF9ZR1zFP6OpBBBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsNHpBmsS3lKqRkjD3eJ1wHX7enT5m0GksNSfeRMzvM2SbzUaGE9RZ_qjSM8YPbqPgl19k6o7L9f9s-zSqd-ynuLnXSgJpyIS45MdxISIDnnQYBSphavOjc7NqjTUtUFjogF45NQsrfOrc5P-wJrd7Qv6LJDsNYsBqgCewr5I7fVni8V14buEvG9WTdm6BPRyAlvWD_9cvUK-2TFwnnxj7ztdnwZCMeef4-WLOjID5qVYZTAtWt1bEBpZLE0ix6WX3OWVVkBEO-6LElq6JBHrYE3qQCRAyBED2GildsZ27ajD3878MJp3rGmNLFqTZtucrOXTNTu-SDXgt47oj1VWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOLSY3x7_T6iTYjAmpHlKGWkuRRgdhy4xodQ1BMUF9RmJgKlDPHxfn79_xbIDqceCaIxrXqgBoKMHn5GaI6_Uc6q9ktaK5KPNeD_WVjskqXs9IYHgIi651IrmYLYPb_65x8QWp9rihCPo7TVkFp_uGXQsep4ndeawPAN9ohce5DqjMYvZOpGfbuzioLDNHHBIPdMIU9wOrM9llQk5XxkSuhlU0XaJSPX_ElwJYfGaVgzpXfYlNTmupAWBxBjpz886kzitGiMht9M3MrEVnr5iLUAbCy4gFM1t1nk4cPHLBGMJch-C19fsu0e5Eut-kipxxmZrUznrhTrwkCU5bPhoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrT5Jytx4MiJ0bLw3FqFedmnWWoW49akxgajznl9ZIKYE7TTFb3oIfZh9384IBWRg5CDDVtAyDdEsaroydK__bzUauQ9SI9g-h1chS67MNypBIA3OOSCIcRO0_Z_a7zGuxTUCYqmZYe9P-6OGrzcn5s5gAKFKAIaqXrBlt2eUyuccA2q_L02TTEcSALLD5G-CUTgnwrVR9RSS7S3ZPtPFR6G1XiSnD56Ckb2Tm02-e52E_DTJGkJ1RFO8iGqMAjfQyXWtD5MoMDeq3Zr1Dlcc8odM1Z9LZXgTYspZKKZ8oYdannl3YQ_DY_XmM1-bzvtUlQasgDJFDnAaHwIapp6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W35fLmJXIQpQeisaSdA6t6rH29waVWqWYEmvGviU90-moBW7ttFBdjESxqQ0d6giJj1k8_vgzDBdsY15fNCk9sZgZ9K3R-ZiiPKc-KaCH98OCt5TBYFktqjD007IsbIVzb6nthtb01SD3igvIsp3jqQVErVefSQNPuBG6HdvPH1oKFk3C1ApHXkDoneoDkq8hT1x0rGZIN2VfMMXLCb3u5RbshF875mma3_ipL50ZLvUoYlgvG9p1lmsp--umpMwgFg9ZQqgDPl1iz9SLdN9xmss4iilsLY6aVHntt84Ff4eRNQgIgxxd_BMY7obrOlu0GkixeqTBoerA1Dc2XCcWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq-nGhnbeqToOuZVGor4jjqguf3Ralh5Eji54Gd_3Z3cNts04YCQv4eO2Yfq1QqAeKgnMhNOcrHKviAIWuOeY6k0OxAEqhe06kaCFVlCRBo89uLUbXjI-JXirmgGRh7-t8oBjeeKbELfX_vf81X5yUuV-AbcPMAjgmaFGfQrvIsVldHGIYopcAwce6edS2TLC8enLVzAG1K0EUuPnc7BKSl5FO5dMk07tkuyt0EkxcmWuiX1snkZWiTUBDbXngHKwj1E_gGuKOwPXgMny329yaMqtEuXU3Cz4U8Q-nJ2nLnS77zQ9qK-KTowhxBow8XXDyVXOJ0c1jeFN1rWuZHGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ledjcgTzKfZHEXRWNquGAbUM84kjYw-2sy3Lrx2OXwPe5r7gsuFMZPbTsNYl-pQo-9GTGFbBGiyNWjpgwpR5vgOYuh2sjsw2NzywdaoAAT1Aosj460maEm3ashDns8n0T1mmNiut9PIn_N9ya-O5f04skp3foEyYLe38wunL6hPXbEBcobDmDYFFvl7ZspC0UNyftrKCLhigTh3Z3E4xzKxtYk5RO5h5kXCnVw-F20dnxSG0oD6We3nOpI7BVyNXASl0SCT_cuX3IpriT-lnSmtRlHL5hXOk2rhTW2C4pBK7ZNxbYB7wYj8H9KzwurmSO6tywkcJXQ8Hm5yjznCv8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOYSyXU_KmiYNip_32nOLJccdhEg2offnCzOCRiGYJOsST8Ei8PzgtxEh6NSkputfuJB8nTZzy_bRHXF7O-j11u7BoNPLeul4ZNz4oC7T_ZYLg1zL1EEKW60qtNxnpuDtCUFhMF_dtECHjdYjUaZbCgbLQv2D0Ypu6z_8uCERP3LjkYcaMFS1Lw-0ngBRcmHeZQSdDxlmxZqq9Sr7Iin8oyx_q03GdtXbiwIrwOTHw3xiOQPn58pR99UuWQU05w6wYjo6xAqkzYpiwBBHhSh8ghnHHURBWs3H4XuT6t8RVasWoXhyuO5ZAgnUrjC17b_b0V2NyW21xdpfpR3orj4Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMbO00dObLZHFusSOST8xgEguMOS1oymCMyjjEcS5E-F8KxBt72tj8h75y8lEwyW6TBFkTzfKc40AORNuR10SV1wHOiIgVK3wTyrXKATM7rQP-dHdDV4QiSUv9HMPA8uKHJEX1rbuAn3QUUAEdC1KYOj-auoXyuZI4W2M8YfQZp3i5DcVgXzuC0haZigQuyS4kaC1B3A-By7MVMB8dguD_krZUQFAC_JJbLbXIJqDlbD5FhsjkWvv1nGsvW8foWmc-h00LXPN5kps-plVFUgqMPGonydK4k257INdqo1Cut_VwDR9-805fEER3uwme5LJAtqpkpEXSkgy_nIucHZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeKHqLCtnpMGkbF9sDGbNWVtqpXaZymqi1MCrNG9ZLQtNBc2DjHD7iJH3tuwLv8R34IMPXeGvFriMANR7GiSQDZR0kdJQR8VdX-LE1ddvo7z18u4kSCHjVHAaqW5APR4oIz62fVo2QE7OQGAEOr16jCEpazAc9SpiHzVy1MyHIzpx537IkgtvmL7058dL6LL_4wHDVAmZp8VTKBVcTT1M921qWPnWsM9ag3ooAAj0vUdM5ZHAB4WZhRYLodas8nuQlqqLmJoJ24Dazu4JVt-EKEM_eCY-16sH6XuT-n0evPqDfjiwASbDp0n1EUddhHZCJn8ZnDjwC6Sok3KFiKBqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKDcHfPKjzfDWP5gbR-V1unVzdnHP6XgJS7--9vLYkz--ig-Ja_3g7QJZc8qiDp3mosxVkqMYv5tXeTvA2-qzFjxJwe2Plo-VBzHJCQ568xJ65x4hfZG7EFEgKhmgtv7YjcBh_Bg1TqsNpDWOeQhpLYha0ydBsJtNZ8WCjrqV4b1vMtN2Paghq3Q7c0wjW_YfQfdBzXvEPyrPWPDcKB14jsgWQTjTwYrZztf-3WogXFPV6OwTWxsgjsFaiVXqnhoQ30I8ZFyrXN3YfYEb3b1Y_cZqKf1WUHQUobEJ4S15irwQrVXZL4fmklJ_rDJjwM5Xry6TlHvd40oxlYTKGYzGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ggiEgHQ1aRc3y8tPkPFM3wA_HaY415fjDyNYRfjc4r-7MRP32i4_8OZe27eSR5XLsS4F9XKGKmXBZwD7hHaDC7Rc-DntJ34jU-V6Jx78e_8515kbleqjAfECXls8XBSAuUzv1PnbjFn4pM9musK1Fhu6cSGjaeSMmVLx4e78Qf3xgRLRrVDvJeGUfw2QMNiQJndsPTTBHEDSOj5cjkANXWzMOIBf0n_Fs_S5uc6mxYMDkB-r-VZkK8HLSAIfQxPqklRQnbITpCfyPGICbxVLvfDRIvcE8A0FEBXx6-vtbGh1xzxqEmY5PKQTWHs1Mzg5EjoqaZ2e6ERS4yAjXWaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9ehPznCnzcote2SFT4G-344VCA_xqfq7cIdFzhxl6hwv62VUd9Rn5hBMg3BNXRPanBHU9XV5BK9qrC_pLc0urnQmhxbL0eeU5iKMxSBmRtCMm5zSfoCVFPMSGzy4SV_-aogWia2H5ZApRXvtDFMv1k3S6Sy70pG8epWkklgByXUpbAzGQ_-dFXnIXSQMtCcQlN06syCBwB9hDBSPTbX-zrGqKFWY8xsMwEsLFJnSUB5xOQPw1nzpUKPUbSBGdDqWx5UtKZZRQCLJZ_TRFskYkwt1r95uyCJbCc5ZZoDdAe78vfjjLZSwWrU907HdUlZHLzlmQr_wRgu-2ehmNFu6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgSv0JBgpJ-9HVqqgq3jmDCKn8px97RXSlMvNWSQtyIlXcRIuuBhVLhaFyO6TAPBZgUbS2A3FbI6pTvqaDQvYH_PGo_q136kip3I38Bcxz6uC4JSXEjFFe88AkMhZYo8mM1k2qvYN_qZkl7Vje2rBmbq9TMkYX9Y-waeBjEcsE4dxexnW8OJSTHyDiZWL0lEKrUWqdOUIoW6EPUKib9TdSjrXKwUYNYe5PTP32HRE1ZTfL9PTA7LC1XcfhklmhK2J5t_AS81yTv-g5Al3wGKu2hesf9SI5nF1ku3ZjdLrGE9RlpaY-8E6H8xiUPMHywBM1bqtovGbKOj0mMOgCuWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nevo1ZjdVH2cCVFnuqR1UOP8zmWmb58j2EUgEr-pmZmmae2z7QQjek6aMBI_jNH-nBdc6ApajSuA9rCcaCHIQR0DpWzlAYw5nHQVeIYS3vFwWfHW6bBDmIpXu7_PyBp-WmS2aD_94E1LcpKxKSxZ1wSNeqLN9vOZJu2yDfgEsNLUDEQoN7Z6U5s3pV9POKEnt67agTOuHdcMVkS9XPY0_M8WfxtDeULr4tABe53aAcHnuEdBzgit2Nq2zxks_AcldppET834NuftcXjkj0h0blTdgrSGq7iBNW4hqNfqN95DLpDXIPwTJOLui8kNsw66CTGaBDVxLnrFfpYYMwM_Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG7OhThsLiuW5nwiFDT4Fgw_sscgB_-gKEjDOcA6rg5HCKcAGvxhBOstmG3Au6NLEuOI85wnZ0yITMlYGDauFvZVC46DCKJzv7CxnAcJLqOAcyySlBVjXS-O6WhZM7NZ9veE0SUXPAu8FhVGE_Rqq2z18o-fe11JXzRTbcuFJOgwauOMWilm9NrxHjTT_6WDStOxnFUk5dWGz8bD2P-0FCZU_Q3XMlDA3i2CEccIBEc-Ey7hT-FciigX_dpab36eWEFF_c6f35GB9X9pfHwNrPC-GokK7TgOsGI8T6FTZUtxl3-sXOn8488VXY4R6SwUEGQ-2HKKhqkpmXZbk0yBKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMi_Z2sU_s9hmpohx2oNUrwUbPCgPVr_XO4U_qRQ4g7ClQB5iLF3KOQaQ8vb6jSZMCoLC3VRejaQdbC_7ergrU6IqOHPevR1paGWp1xk10g7S7c1pPYyzL4T2fslEXmanRb6bhhbWa_ftGfXOqPmVG_aAsW-M5byDgtKVaXKX7vAx7t5ldjKsGO8bGe7Olv5RlMieKmIRVf-VPTW9PNpwBIt425LMOf7vPVk_Tb7rOjlCTvj1auwEFAllUz5_esTmo4HLg1cWA2pDyxsx3DL_bNypZDP3hxPtI9r2iNC4A62w2P_rHqjdAz9z2rI-_BWVzoAg7_CWApkRVBDoqnohA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Crybsl-4odXJ0LdSoxZrdW9DoAc-m5yvaSzTSliNnxmGVsiFw2-5ENA-CdrT6qBVMd8wAnN9nOp7oLPLlNt7gfnPWXoAeXBEPLkfSTwVyogSf_fJp7FOH7wXaaFbT2bRA3dIy4VO_fHocLx-JEiHQ0V8wXsTQtTxZl-7exFk8moOv7UMCmJYISiS5SEcknH8iZW6zviMpJCrPfkYZe1DdY-NjMdsCEJdr7D_Fq6xPEbCYDMxdspcQvu6UIhU-g6vCRNP7480mnSiGRVO6QhG0NOV13nKmu4_zIo9F2awjLe1-D87CKUOeJ07gKPbV39nays7cZhftvnVVmCbdYiU8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEAtHWkhwLtJ4tvp9MWNRgHWSft9OFl2sNkKrAENQS_rzhaRiCAO53EetZppAF8_IQz94lbrkpXJ2LWPiSx_-NBXAXN3wAJ2Cs4QT3bAM8jnEQlCciSj5qODul4WAVF6R_pr5fr6VNBrk1nY0y1ZTspo4fAuCN1cDStj2xZQVSw5RPs7V-yyVddw8Dr5POXnN7E2uqwtoQ_ZnceMnB7TPa1Icz3zKmJxK5pZ00BHw1hXRC5LAbXM0ji0ikFFOjZtY3MgYZRBPgtHH1ESHeCm2uBW3bk0nkscl7efc0xK4f4ty2CtMk8iCxRZCvTqXn2gzg1ZOuRsqyX64NaSDBnvwg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=F9FcS2uz94pZ7Js9MML_L5jmkwWtaMWbrv0X0SNlnXRpNmWd5AYuJ4-Tk48_F4MI6DYWn4ZCWfi2PHkURCC3bkS8Z98OFaaALDPk4AINa4-_cmEbVjLYxy_Wm239JRW23HlI4Po8jzO26HGlt2iQI9Ly-REojBBIlZggZ4q7u5VB38X3tWOGIImAEcVJ-FRh-mablIFuqwNvbui10a6DvWo1sb3s22g8xFIDsq5aKweyW3sTS4H3zdeXlrU2SVEeO0AFNn2gbA6MkAFd39h83LxSRGML04vhAenRqpzQTE49xDsGg7ppBOt2jpUUOGUa2bJF0jl-wimbB_kY0yKyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=F9FcS2uz94pZ7Js9MML_L5jmkwWtaMWbrv0X0SNlnXRpNmWd5AYuJ4-Tk48_F4MI6DYWn4ZCWfi2PHkURCC3bkS8Z98OFaaALDPk4AINa4-_cmEbVjLYxy_Wm239JRW23HlI4Po8jzO26HGlt2iQI9Ly-REojBBIlZggZ4q7u5VB38X3tWOGIImAEcVJ-FRh-mablIFuqwNvbui10a6DvWo1sb3s22g8xFIDsq5aKweyW3sTS4H3zdeXlrU2SVEeO0AFNn2gbA6MkAFd39h83LxSRGML04vhAenRqpzQTE49xDsGg7ppBOt2jpUUOGUa2bJF0jl-wimbB_kY0yKyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXj1R_eVLLRRaXHPPr23oj0NA-EzFPKUXzZTbOuIko1QMGodphhPCZ__xo3IaY8odCaP7ORY90PwXMj7UhQoxEtVF-FYTyZL_BavxWlJNiaOX87iHRAFqJNxpdV5MgrYMI32M7IWtHE2q1mEkdMW75DwpInNJ_zZh1KG0fl0SNkglH20B-NicsX7EEqIWVcwG6huSxzvASWSB3OPCtmIy5i-MlJsh6vPkqOaHSgnTwD9lKdUPQww8ZjV_Nf3RWxMAgR6YdULN2t3KXXkLAxbKGAm_J_rbAT5DifNN8rDy55SZTRqfMbPo87JzQNHhjZiQMd5Bu1B08bUKsJ5rHxR7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3FjHs61kwRHmSuJ5TD1UU6GFqV2STIDo9J_8EAFqz5iBKPAZRGMBuD7d8BI9HT4-wHFHoQwKFrSOSL_4KTvEaazLpqE-OD9u3j3tZtBRVUqTtK-aG7pkzrjimLEWqx57RdabzdDdjN85jIzVuGRjOlmKFhln9ZYsw0IwI9-EJ_q1wHeZrKi8Djew49P0Fc7gSTelnquRSS9GvxaUtbbE9T-r80WNg0IIVPFBzxx49lwKnhobUVKHF_LibgFR0q6YhG148CP4xjPUPDrrBYvA8hKhplxeLWiUExYvDO1_ooORTKaeE_sLSxHJ1C1rHLVe9ffA2ukYCzQ32dE6u5bmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwcPEOpF3SxKq0jFQXEN5Ge5bJ0Xc0PwACY3IgTIgMx1UsVMQ9K5w3Lr2SnVVyQzJTN5Jzv6YMUPv-eV-E-s4VELrGQthOew7bR-Wx6rs1X2iLyGEys2ry5UyJwMDl7BBIi5WXcyxRDxRgIcpCndtsxDrH9srpPYVbo9bNPlIywMwpqaeJrthNsvBIWDsZCH5tnJAoWU8qmGTrpfD59UvBui_SeZNXazy7Qu3L1hOnBZcX9p40svbPphDoDou9z5BhQOczzr3RbL5RKym5oCopNU3tNGbO6-O1ZK2A5gJOBG4a_xZq-oIvPRA1ZV0tywigkUh7RaYu6sKhe8a1p1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uq4Yph3aZ-sAdplG-Eu0mkCmFM2okznNiPgPDrwF_a26lBCF6tsx5ZE9Vyw3N9XvA0-cqtFYLotifdAHJKM3SrwLGvKop0YVaJJHdCOMt9uXj1u8GXhS2F96sX55n1wclB-QuPUOLnLsX5UHm4GvgCCp4FrLHUIcjh8DnqiyXyZu6LQ0qPYMVMb_4NuhOU7w3MnoU8KfnH_PWad71RvUCCiTHNrA4gJwQm6Q1IuruBb-JX_3Of3txQ59DA60jn-ttLoj3ejlgsrCMs2hDHA1xkE56VJNk90KnI9jDk_jNi1ZqNQOLPL-tYa_dZz6k9tKwGMsy40_qcRdoY1jPrU9vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EeWNHcsgESRBPJMr_tfi7c-OEa87P9G0YmsIQquZf01-swzLl3NpHVIVAjFXVZr9elfxejz_ct1Maa2DN9NdFbBgBFZpk6-oiEKmHq8jOAQiaE4VrF_sEQKqVc6sTo2TBdESDJzgLo3J5Bv4ANaR9ir5cw7EAfFaUU4J6MDGmCGxZo0m4jhBJlk1Oyzc2lEK81ljjxyxY9DKbb2gz1HnEImkkbzXAnnhhtB_jxv2-otq2S_4vFX_VHW3DNML6zu3NoAzKMgmE7rJDcDuDkqYiMw5zMhOm4N9cYsVblNu-5d9YNeoEHP-5hRjRCeY4DiYu1UR8btmGBLBbOsLEiDvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqtokDBoKYnN92T3CxtT-L_zZpwN0T2QLYhIhCtj_W_PxjfCFrX9CADMQqQznFlJq8XP1wZpVsO79fdkflA5rwxTmAxZTurfObezBR_uwkbrkfamuydIubZCV2OhCUQ82XC8q2hH2mI5mY_koQCqO_zthRMDhUldS9vcRibWm6ybbn6O2rN9izCnPSwdNLczPO2xrzNiKiJT7i_Qd6-iQbNWW3xXH55ahCnWzaYoJfE_cD1E1P6iA9MhRVX2qXCfCznwhFvjHDsa4VzrjNAQaWCqXx3nrubHW3xo3Gz5_A7AUa_UtL5LkwMZM2PAK4zXH1mm31u8He9FXy8z_Q1O5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sm7B2WiNytSi3SLoHPX0hzwBuXhrGX_p8QdZLLowmJbtVHx1wh66kL3bzvB3eJ1NTBRBhVSSQ6Gd0X1qaYguCrj35sdAd4CTZPCq00RREEnlZlWNLMXW0iGjr0c1Zk9E5NKMMVVqjJbBNL5R3yLeFtTuUA4CkHEsXTuQ7cQdGL9lD8TU6otnrpmBa-eqW9B1x10MplTPU404XR1fP9VbcLMzpcCcbjLsjKv8j1huRlli823kQ3Ur9QYL_B6dmJeTT_98doY4br6Hh7kyRfm3Ex5UidRZhd11u_Uj2LmUAYIFekHDnNwDezTFGLk_clZqL7w0RagRX9XofCo0p3PITQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=JRjpynN8yXREjDuWl-kd-V5pgVYXJYghcpk_yx9RwoazbKmD5KZxfLsaHWxWiXP8nvbbOEy30uQLOFVloy1JWHqrV5eIOOhCIJIg328KK89nNGVO3iMJt0hFK8JjXS6cvoZSG0SjiSw1FWJb0HgFEFWia7U-kROjU34IfAKyEzTGx3za4xxmTYR-4V6-XsKAGZ_JSb5IKoAF51wqt1qDXSE65pADsE4dJGkfadCYxL9PJP-kCDJmDVWaoML-C3O1DtL5q5DRwVhSw8rQru2t1UljPmxMIhXOOe2MhSfBxI9sHknYQMVcbxMCL03HzIPkZhFKEFDgAsmUem51DBI5OFZH6Zm7jJpQv2phtrba0V_2CjbErS10OuSFfOBuUWlnqluyV8WishbI25SBrVHVSpI1V6UWbAX6DDlKOhcm-8NefsZWidHjZGJhDpwjnqJ_Bzts-fLWWAD5G6NAks2yM-59qGwXBSuy_tv1KIFIv8ZuJh-jOUGINP_FgJ2yUoOztziMEY64paU30CqzKaZuZrEESltmb2AkuL2AEFXYQdAOm3gXlGkQtF-EQa1ODXuZ8Q7ZxTvrqSlVWpYv1aOh6hei0RYYnfr13PBFVRnAr4tYQ0NvbArJ5qMJyzxdB9x6GPCk2vBazIWTlBQfws3v_jusKqowlCc4DxyQsVql3Y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=JRjpynN8yXREjDuWl-kd-V5pgVYXJYghcpk_yx9RwoazbKmD5KZxfLsaHWxWiXP8nvbbOEy30uQLOFVloy1JWHqrV5eIOOhCIJIg328KK89nNGVO3iMJt0hFK8JjXS6cvoZSG0SjiSw1FWJb0HgFEFWia7U-kROjU34IfAKyEzTGx3za4xxmTYR-4V6-XsKAGZ_JSb5IKoAF51wqt1qDXSE65pADsE4dJGkfadCYxL9PJP-kCDJmDVWaoML-C3O1DtL5q5DRwVhSw8rQru2t1UljPmxMIhXOOe2MhSfBxI9sHknYQMVcbxMCL03HzIPkZhFKEFDgAsmUem51DBI5OFZH6Zm7jJpQv2phtrba0V_2CjbErS10OuSFfOBuUWlnqluyV8WishbI25SBrVHVSpI1V6UWbAX6DDlKOhcm-8NefsZWidHjZGJhDpwjnqJ_Bzts-fLWWAD5G6NAks2yM-59qGwXBSuy_tv1KIFIv8ZuJh-jOUGINP_FgJ2yUoOztziMEY64paU30CqzKaZuZrEESltmb2AkuL2AEFXYQdAOm3gXlGkQtF-EQa1ODXuZ8Q7ZxTvrqSlVWpYv1aOh6hei0RYYnfr13PBFVRnAr4tYQ0NvbArJ5qMJyzxdB9x6GPCk2vBazIWTlBQfws3v_jusKqowlCc4DxyQsVql3Y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSUT45ybJWpJeh-HHPzxpFg9sOECj6kPWOH-RXabw83RCOpMM7iCjrdiPBCSlkF5p0jRqn828p6B_xFS4JI2rEcl_mZJmg90F1bftisi-v_2A36A5UwZWCcGnWuxFKJBadg08nwcHqhcWyDlRrLfYVUalHcVZRtx5VfU8epd5Gco7odAYAGGTkQ9ejfucMXJrEROXdB33HttVKqtND80gcWLapms5BU1RkdtvE7Xhj4wUOT-A8mpRV-hLog-P7E2UPzDU9UBNdczx22KQB7jkD_u4HqKioAXN9g0iI5ffrMcAGP24kfPftwlnc7Q8M0TdB19o2tXNQtfE8Epakwuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4pz2IwdiO7qD5W8optIysHwEJZqo8cTd4VU68ybC_2-PeucZyKMjl-upEUcDm9G_sDITthWhWpT65NCRXQZvjCUjXpnxS5FzgbqFSenclgflkHBvODwAxHSgfVcq1Wn-pZro-VhxTV6PFrcDzkVvqtNMPu6j8Yh3kS-9UND62F1EjVn_7NedXE6dc3mz3USY9GsEW8L9OpfnGKqMNRRGEqLfanP2n7G34MIi6HFKikmlNAaYx9fh3hEGUypv8yt4wIa3daFQjQqGpfsCiVcBO2Q7bPLlR1rDPSDNfGpj970IsEy10SbGXZebanIhEcIP7PS0V_Q2App29jldR9KXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBkj2eDX3Phg6_tLoMz48ofzFEhQLwhOyX79uWn7hQUtggRF40bbdo3iFnEv8BZpcAVEv85JhIgPIrGpcMBR-k7TE8bGeI_LijuKUlJGtnfPeixkVlhujUjqTpJCFVAYSGCDu7_6nxsf6HS8IheazxCDQVhEDLrn-PF3CoRXJPee7c-RANXHTllJ5NCugd6N_aiMUFIV-nnF0Tm-OzIXY4uuP5xm2wN9TrdMoN0qWk_KX6TYtzExJapOZNHAvpVVOivJLIFKYDKL_Br32-A_iEeNRSBC5Kp8nsOHp-KoPsRwtnErMojI_ajPvn9fcSeaEBmqgCzq_W46_Kq5_O6DLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLImTxnOIG-XxVNUNu7rMoSiwgDEK9kaiyAQ7wFw4cGEoi9OAtqGUZN_opCgPTLvgwjvDnWVkk9guy_eoV1_V86TM7cJ_hgqkOcNZ03SD0fentJ-ufU9QPr1sbO3bOPlOfKsZCOC2mJYbZCcl6KFhFZHD3URGAIHSQIU3LTUk5Tf0HPbgOlu8QmcVih9Q0KTjJZNVPrXH4JEzC1MLWm1RSjD7p1M4E-OMB2lia6QhZKShKJjC0I0eL6-MFXgSxz2dFWnQ-OILsQwItjyjJ2FQFIQbzChChngIrAfIM5i-ajMI2ZQYME_N2e3MLRsmkgo9RVp3DFYcSdT8wuBCP5-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rhh1r54pRBDBe3hGqm8lppzHhzoDZrCDFWnOALHYQhr6CptTR22EylfA6HhjxikpPQh9vkcuBZuvmE_NqI5kw3b_odCcrgLJUVOoHhoZ0dG0gTSxl_JuIALLZCwENRkMpYvOB1DKjJuDUPqx7NSqSm0wAX9vflB4XQhq3_-_9J9abMglY8qZmxRkasVxmo5mNrv5Tmcsa0F6DmUh-W15ZhOI57-DOhXSjxznbbKeQAozdWm5Pehz7epia1mxW_TCg6ZB7ZjRvjZjryvOK9gLNp8v8t5Acf5y10cdcyeNEcbInmHh2bI_f24pAbv8wz8yBF5rFjX1oX1QjGXACrgpCQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Tg5LGwbpM_0-0rNtXp1DPFCET0duCXTtnsy_fBR1jMZ9oNdqqLtfLAGWha02Z_7ya7x-jZ9VkFmO0-IpKjT9vi28WhCqm7_PipoIeQJ3Ndf-0zalPGprQpm3sm5iNNjOwLmbeEmzL1KPmFok7qA_YXnRCfOCFcitnzHSriQFHWhXFSGvguxXwk3pQEYhpIe3z_y2LQKdCwTeSNJ-6mpr2fBKjHYQKX5yibxnKcG9NZI7YPOqfHaMyzG6-5JHvq1YLX_j27K_NRO8XFUVA2HBJD5NWcLelcfG2bqnl7ElvafzBpSljJaRtwNeuX4MR1wsyfWKGfhitd3ILkeN5gP-r0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Tg5LGwbpM_0-0rNtXp1DPFCET0duCXTtnsy_fBR1jMZ9oNdqqLtfLAGWha02Z_7ya7x-jZ9VkFmO0-IpKjT9vi28WhCqm7_PipoIeQJ3Ndf-0zalPGprQpm3sm5iNNjOwLmbeEmzL1KPmFok7qA_YXnRCfOCFcitnzHSriQFHWhXFSGvguxXwk3pQEYhpIe3z_y2LQKdCwTeSNJ-6mpr2fBKjHYQKX5yibxnKcG9NZI7YPOqfHaMyzG6-5JHvq1YLX_j27K_NRO8XFUVA2HBJD5NWcLelcfG2bqnl7ElvafzBpSljJaRtwNeuX4MR1wsyfWKGfhitd3ILkeN5gP-r0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeqoMqEzAZb-EQevLp88FB7F3MxYMUM75qvVCBHQ4WNyHG8WjsrH7zUDNSPaxL1ooh-xTNHLdiBnFbWrDnAPrNYd1K7YiYxLY7RXdIf_7OOPfDoKCS3DwsgGSUqAUroyT5epiJV-wnlw2OPvi8NvpAAe5_UQixV3Opb7zhtEW-aaPkHqrIaGLmrbNP_f6QTA7xjzsfqqUksG3c6RcNSxcdmIM6UN4YXmlt4i2onwG6BZ8HLwxljp7gm24Rt4UQArj695AFbcFea2imjjgjSpJV6zAZLbt_I2HjnamHJwiF-wxDoJhGx8ybM71gQaMJSowryMLDDXYK0I8EvPM8qwEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAXoh2KzEfvByfeEst3CMUQ_qiGzhUyKObCWxn_-XIF8njDZkZBQT8D5fQ_EEA3oTk6DWFvJy_IwrNadzbvXkjj2rWrCFpIFDQVlSgE1F1zvLPnJwh-qokYfK8DTXVl71uR3Xm9hRRaTY5XZklI2jjtDjHlfaqX2uYvPc26AAabYQ3EyeOuSv8DbaLVy4WD_5VBwfuNZNv-YAfd-8TIGuEA0clxuUHvBMEy38ndpe1DsMcOWsz2QjgT0rbzN3vbswJhMn2IxVG4c-h4a1zC1Q8dS0qXwGNC09AW8IiRK9bUIgXSEqC17Bqnw6ODdoCcui9iaxfcX_vEoFlR_bIrI_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HY4ymKeBGrlP43ispcRBI2Pp48K4dnA6nVvwrhyT0GG9aywmiv0m2xNZcPsot-0NXmBA6cnYXVRJYnioFDVxXoetfY8d7r7ENuvoe6nHQWLOqBr7peSUCHtUtBQQy8GN8HcuFMTzeZUWhwYBFh9_t46JiU2i3fsCPwraaHGiINJiFk1In6FIFLSIDd4vbno9nd5aZ81fH-vabm2yLcVOEyfI79BVBnAKCRnO06SMIvHzt6bQmqvfa0ATwr7BHSiD1gx4eJYLYEd4FY9ByGpvo7eeALRRUpcQmTIwuI7vSM4QxRRUiXNhrwg4ddEKe7W7b7g_HTrYe9r2caDwh-xdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpQDP5MI49hL84Xog3QbSI3ijgf7wYDPSGRm522diPhc4u9q1Vx5_sulMo2kS5HxWP33jvXN0Jk79027IjojxSUB3ld5OVhIg6hCXFPb-mPh7VE-2PSNMPTfWaiwUJOG0FxDuBbPUhxybI1sLyP3lfLvQ7ya3iMOBigzrz24J775atyEdUUKSBFbnzQVlAvvq5klsGmjfCpafD3UI8ocqtOOOgD3UZEZoGnPUFkPFnOXd985L4RmIwSKi5QHMf0ViStC_3PsJJagWQFS7OhTCnxxCMJPCYh1haKRCqjMyWi7LXCjeV4aUZWoucdbXM4lCIr4KDvXVkRQ8iaZnxUwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbmMWaSJPIgcVUWEfS8kl1kG6hcDqxCyjPMmCSQA89Vx5Q21auV9C1B8NsIqK4f5dA2vUaqoIh_w4znWR4fUVeAdtGB0EJ_bozBV6H8bbg28KRA16TeMAFvBhgjaOiB5HFROHTri_Kjd1uFvREBX4cvuwBNAiBtnogwesUNl_vwngv6n-M5A_xo8E-FlsBfyW9gSoaYVw8EpQ94JiY-nELn_40bZVQDt_1WAuKeRaaHuAG4c7OqQJONXOG8obqi9szDMDcCQalh8s4SptF_J5qBCEPGldMoCKU2jMFg60nmsl5e9LL5Mt1iO8RKEjS7VZn3kUICXvaSem1z9tJbbCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ0ghQidBoTyDzsloq2a5eiXzJ-u3ICAsnPp_C8I5ZL3leFLIJarDo74FgNyM_XMr9c8934BXAFVVndfTf631uFLUKOFPExtZ10fMGvGFvzkIvvIC2MjxHgzx4XbOE6CEekuznl6pmC7Fa7EJISJDebp2I-KUZFGENgp-B0TxO8QJuzGfwIR3pKbUeEeR_u9Ipo9OtkqHiDALQd5YydzKA4MK9LO0qRDDhxJdr8fzwfIMKYcsBtgbgxslE-Xq1YyZSPEkol1K55D3j7rP1fpQKRHS6z6RoTra0DRgALFFmJqdyQmzhknJT7Rpja-sfQXg9ATL73RYOQIuE_uRxu7mg.jpg" alt="photo" loading="lazy"/></div>
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
