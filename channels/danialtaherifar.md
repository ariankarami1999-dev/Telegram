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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 00:57:54</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 332 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 495 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 598 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzLpUUkprFF7Xk2yhDJpROZRu9zb0FXd_mi-VC1IhQVrjXaVuT73uffRmMNDK63vBpaQaLcMr023P2MyG7rerCYSQxp8zfbTTi-2vP2HA-8iPEM1E2A59GkXB8cVN6x0aaToEzMwhIWYGHwbM10OSDmVeceK6p9c2BGfguz1fcIOEW5iSPvaET759JBHveB74DiECUQSGhrvDucCEidqVksu_pw1ulprXbNyyTVHo2BbpPrXudgU_hqLd8j0aU3pgOEGsnuKZgnfOan9lgOajHFsUmTGhs6zVAWHXu0uZ2glxdDpfIlK-kBNbPR0bcHMO-bfVg0Dh57_TVqqDv72Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 631 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaAEf0qjhEHFAqlGZK3-xiNWn6yHmKdyWqT0tTFXoXYyTE9O9_P77BKlFn7_Y2sY6dJ6tQtpQs45sdIYHfJYqIS56vFDvKer7S-5kz5W06OV4Qkak3OeGRXEBnKAcHaikw8GBKSlC5vjvK3hXUCI805Qotn9XHs3_JiDPacCyN_XBIYOE-3GdwMsIKir4clyJuYdvc8s4WHGxXPSlbwd2rh-H9iTYzx4lUDRthC2HQNpoAhxFp9Oeic0n9Vayzl0ifuM0K44TcPvStn7N7aqf3oUpcVkXo3cwglRPmYQe_Ct1G3u6W2APlmMTuQuSNBvVy7o343MifAFS_rSDvqt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkhAUPNB64Bbj4L9fvSLKt8-QVdilnd2KN_PV4CS49q83eJHgBIl2ZIk7BQUxoEEZctFQ0OVjd3hObjc3mM4vbdnpjs5gbA9n7k0sNBsDiwfAqU5elqgtUc1KjS4cylKmuRVVyY1FE190P0xwnXbTt55_v9GGCEPLz-QozT9pOjttDpmpEttBS0I1pdLizoKtlQylFqOUhVQIWeFTuypVTbn8wqZW4dDgiADCOqsfeOkmlnnFq-aWsnOZ-kK4lxWfQDJ-1lF6FweIDTvqvv0U3IaghWrmv_4W_uLPtwLrSiG8UyST_oq7XbyRWrOlTsKHwcQrk6HLDE4bnczvDNkbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yse8S8CRtT_v5xglf1rqUj7rQE4MQV6xFBQuO5JlJiaj2F3ghHeKuVnIhaa6fkmi4j5oua8aS5g55uhcMyu3rkdO7fSmf2nURGCo7HyCNjWtnjL1rJsgPt2cAFzqQnTqTYEDkEtYi430Tz-aJUKL6cw80ekqngqH7julC-Hdi1oAbmnRKoAlHsnQPdPul8KEXYhpcwVKQ6ZTxEuj1JAkFAbTlBUFpuF8xT6LDQ3jMIrCdoh7m9H9v86ucj-M4MHCzt0SRwkTiIPZUtGWrc0L8J4IZeKOoaOoEf6HTVc4nbQUDN-u7PNzZ7VixqJAgRXRncR-7nVUhl8RBvjNsXaufw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z79y0yTuWsc7TwYxZvm6zpa5fRBDz6EnKveISDJ2YlbIeoSrPaaEbccIAFRdCEREZCwlEu6rlpKDYB7_tMahP_UarRx1ggxd6xvwMhL0TncP0cuR86dor0Z4vD2zCugDTbV1RDjVSwKENF6-kcNOrQ28ceLaRpVKrreGNBRKZN2GNVcuLo3QX6sSsFGJobXyeNJ1rrAEFWMD574kJODEIcOazNeR4V5HAXIALZJMQGGuc0QsuoWmP6v13XqZ0ul13-uNBlo-ezyiAkqIhgaS8EhS7JxaFb8HhnC0PArrXq2LaYoBm4kMxOjOm6sL2aiR_dxhzG2zBDEfSIdr7-MbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6c-asOUOyA8jmTkSTWmkH8uTbDHmizYbQY1mfc8Z4c1S5HfECry6HARmcHIevPTeRtB2hmcwEVkSM18b6h1oUqaf4UGEgB5zoaGldee2PicnfbdeFA2-S8p1bMOZ6F5YwbBJ1Zws9evdNsQ5LbR4zEHBdEBMeMUFxpDGErxH1NilOeQ56qDyCcaKiZrGgd4t9tLys6SuPnWkxFKUVeMbM1W92T0gAWj-A_aSQ8khQM9DL1FzUNA5VDwSuYQem2Bi9fad6rmqwxzMncOs8YX_g1RPGNf_JngkCmP-3rqgZ6GvTF8k9uK9nc6v4qWvs792dSj9mYlqRHlF8rT8S8ARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMusfVeBxoVb5y1iEZ5VEt6cwlHgi_yPNW-LSHhNO--ijLgTaZPEZ8WQaXT0Dv-SMb79DTXqVP2Ra4XPrPjo1L90FYbGVvug0mB3pkcgzV9V2Sd5KkN2BiVhXFquC7lUv77H1uVR85qq0ZdgrO7S3jmOSzghAubpOa9XbSGt28_2ouq3s84i9PzL1mYQI_bang4x2mniHOkUVAf9R08fxup8RF2n9wvXRt3h-p7ceURkI9bFfgvrYiJDN78ctEZ5rwuagWkXQaXbCe5tHeQwLgD4kfhkj-AL_m4hzbCJmqZCuKn1VazObZHAuzm038-12dOqaChrddLRnLWSUZOYfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxs4QNz4usSNAOnrECJRyrB9ZVoIgEo_xcAIe-oyq0isMDikSbFzMhMSLgOq0ANg259TfIipq7ipJ5wPFjljmej4mMSfnt_3NmGGlVU6w9_96xKQPgMmqrPnALde8E0x_NVWkXYAw1VEZ9ERqs9golDUB5JcQ6b8La853ei1fx-umK53II6K15lB_4oGLhnsc2IxlA6pejj446X3ii-jio7DXKZsMw2TWHynffxH9ZC3XIiN7JcdYojrW59plR8O7rjIEyD1W9kRWX-8r0S6XAKS8x9NPwdt8FIW9lj1dCrzO9F-qUIIdSSmPHN8SysPnjhTXvPR9xZWoG8lnXx4CA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=pbA_Z_P6bcfnwaWM3xI7wKd0pOJCg1JV-ouGz4RU3HyOsNdMvIi41asYkwJNv83vsQ1RWZXozDMyF5dh_NRPIkPenID2Lj95XT6_a4QKzGriS84Sf0U3AO8w_DM9HjFjvSTIGAv2AH8gfqYc3xfRD2IqspSf184TCXHx_dCv8O4Wyz4GmCFH2ebw-NHmlZCRwzQCuWJAaJ83w0zC3EhbR4HoIcUYLEY4nTuqW4ynnCd0O6TstJoqElUPiaurUI732oYDrohPVIfgtVPikQ0DCu4kNVfbcuugCe6t2FZGHM7x50uMZFYhf_OPw-G41J5JnrBdYFMmCZ1gYjt7GLhysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=pbA_Z_P6bcfnwaWM3xI7wKd0pOJCg1JV-ouGz4RU3HyOsNdMvIi41asYkwJNv83vsQ1RWZXozDMyF5dh_NRPIkPenID2Lj95XT6_a4QKzGriS84Sf0U3AO8w_DM9HjFjvSTIGAv2AH8gfqYc3xfRD2IqspSf184TCXHx_dCv8O4Wyz4GmCFH2ebw-NHmlZCRwzQCuWJAaJ83w0zC3EhbR4HoIcUYLEY4nTuqW4ynnCd0O6TstJoqElUPiaurUI732oYDrohPVIfgtVPikQ0DCu4kNVfbcuugCe6t2FZGHM7x50uMZFYhf_OPw-G41J5JnrBdYFMmCZ1gYjt7GLhysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGIwR6uzF86egyifI1KAtTNn9Yqir-mJbDARbFThl3PjFe4z2M6QzX-DXu18NCLwoqz3cHF_tNmd0PcgdKZ8DOwg3_OsTnp-22ykyONqaEkjibPMIig69ur6SrIyhgV3mr9KN5a57IbCoQOijDbMxSIdA3KA3CfkSx4jIM0BtHM1nkRwWnPVs6jZP5fdaAtNCn5vm19eGzTA3OdmNOiOrqauvOepXfwkH_eyp3Hzpa7GBdSm69A55a7Y_M6jsjWzDaJupt2iVOobLnxN293TohfxnQVuugNhqbhar3Zkvvxo5cclY9jnmuI6CqVy2BoibrdE2kw4aPIpviBKHSETQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Ft0Uc9BavSGuTRs6uozXqybNh5bMMKRCt-i9IQdDzSUBJDphbFkD6wJDSeiM4YswIRPuQnHrO60WZECRPGlEE3zF80ZqyzJZTvCfNcWGxrjKfAaj-MOuFqDKQs3tUkOPG39eS5AIkOufzEdJFETxgsXB6dSnkpafTXmEZtlLt419gQeS_x75-ANJ-oAOx9QDqCeu1yIVWwZMWQ3DbSH_an4QlafHGTvQ0nPW8Zf38PCUJZXwcGKpANAn-9_oNOth9tN8O0_4P9E6X3h_XCtzz7SXNbwoqCvsGTXo_CbIPWOp3azsz0eruNCy4v5lLheQ-Gj5qASYOS0SLiBi8-6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/La1KXrObF848KJDujVVaub6aZPwB95w-gUWoCXsPpJS_QmoIW7YY1IKfACTP3dPEENBr_k2pbCMbGAw-yB9yj7rZGJCkn1JepURoYDEWo3SFigsgQKM6yDuWJpcF7KE2erihHuJCCYgIaHx6Sf47UdMapS_0rJjeNqHKWeK6ByMSPC_9Bt4ydRH4dE1yt267qMPyXlFHvkhz6beFYjay1eGLy9lKA_rZEnUskKOHzBikowltAugAtZxHfFv5AyKK2Y-yqQ83_dgnCgsgAIPYWRz9nAHBBupTfPZ-ctXPZAoQUa4XYo9jfxwj6DjFueChPCJ2XS-6VewX9VZA3hO_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgJWbjj9kry9rcFYzoGBf5s-IT523Tj4Bzfp4efpKs9QXGod2kppq6Lbh8uK14TrDybQgOxDI5tqnrnNDqwIfWvqhXiQRdX5yRMDBzTQ5g6kQp47ec81lvA2mVASGngWiyDPt6f9u57DTirAes80NrDEsO5cZ26dwTRIFqzekzYARfwC46h9vT-KqQ6q5Mq4wADro1m9n0C42yXE9L-qeAPWIXvYG-VdTpbuG0lpQV9PqdNjbU5abvtBM8Yh9g1YnIlIRM3ZBeEKBiG1zYn4S6Bh6ITdLqNVXjjzI4l3T5utSLdWVosfBkUaeWSFBt1vIjnNwlhwuN0k4GJnppGzZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4p4twpkVVCEtKVAAvH406VKo6Uwi9HTDaz3cKQsVNjTOy4TUEFQaMsLkiOdLELdtV9AOKOnPJVdz_mLf3HnZdVvl0q3VTmM236ZRNEDvQyTC80JvoeT6h7IcK8t6fLZv_bwN8g2lssqoeN-XqzMXdJjp84SgQTSEPT6YxRV3eqN9e_Exf0kWkREZ_RRS3RZhKD3MdGxqRYKpR50EnjNNlc2LCmZt5yiHh1lqpV4JBrXX0MBSZj_8glCSIIQhJcKxkwi7_TyLzi_B0BWfKLzyf4CSR49yW0P6Fa2NgQvgtAZYqCC3Tqt0_TKJQxBTvTHloV-_aCsrfYlcOQZw-iL4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY-HB5fyeT0G6E45uAFVQyYFoQqlT0btSq5i9jFNs9nhf4G7kaUZmkHD2C_BP0QaVEOaApJedY2HFhp4pm_MsqSjpkipZ4Cegp_c_ZiYvNnwVauRN90LXbpluITqatoKs2yb2SgPpDfWBNbOa6jNCbRDgMIojRvHH58p2VmpbEi7qk67RWBesLv9WgeiM1YcMjojsG86SUjLWFpYfVm2taxmLrruXBGuXpWJ8dj3gH64W8vBOQfilAG4VVGzF469Mx6EXWwdjTTw3_cBt8dgI6aEsqef4yPO5wWHG-pFlQoTToJMJ-WOAHPdPTLnBrnz7eskMaOXtUz63zISvXYTpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNnBr3UoYOOKjyASVLo3vFqL7rKSJJC90ql4k5nzS4wV2ykZ8EBr6X01z-mULTI1WYiR4c3q6H7iZjn5MZ7y-ZHdfNC433T7RW_5Y7lauw-D8WO0Wz8yQpXgTQPGxOqwW4oHWf-nucr4DPrDX_y1A_D9KzdTPO2GfehmEmqRMXIlZqxE0XJylcDLpKhBNLIEHDfzXUcXcbE9T-V5QiecnhftAVt7Ik9sAbm9isEvHgZ2TkQzYFoT8ba2Bv670z6g7kaE6QgU3bIFag1atu2Hb-qdZf_n5MkMeaF99BXdKYLfyGGd-ELuT9b9sLMNnmBYDTu5naiQRa9e95aKJxgd3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j13IWeZDDPGy4xQulfCSuAN2SuUuSUFMdMGXaKmBpY3zvzDGcbZ0saDZPoBdF2QUaYgx8aHmzm32YpHTN4w6mKPAkLxaDePAK65rkA3APR7kMH3aFlMR068OrliG3FzssOuViaWkXRcFMx9m-ITTz_sNFtU1p3XeAoYuNwyfwnvtGGiQGFtmvPu5HWOxGdPOSl0_R-Xb4xK8dNSwX8DRtyfoltHJy5xPjsRu5_CtbgEh6pkSQ0np8Ifo3eiqYfwze0VWCIc4MxiumVuYE05WLypWnM6Vp4VFYn1Ijar0sSHf2fJ1-v_DfiSrCpF3lenTQ0HnceIC9GiSCaf6xp0Y8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxccl0pE5TGFjRKaaygK8bmlvoPtD6XlaIVIIJ1VA4mFt99PAATItth1ejN9t82ecEsj8RWyzMuuMV_vMCndOcqgH1lDs-AAIQYehRuYYPUCOdrrEXMP_OOWT1EchHHQ-E5lwe7qKA1WIUA68Q4YpkWzdD1rEW4luBvO-3HeVbGCsA2KdCb8LjKWhRL9yW6XnQVUia8WlD0IC8KbgDG1u1eT-u84lWZ-LrBOJnbCWs_TvwVCzDOMRc3zY2BrORMn5TGIUBapxt5SVAv2hkPApzB0KjQMTVBzNNSIST8nTZ-xQAnQnly_5FyYFVBc22Sr1jdujHiEUqMrlI4sUB8G5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_-JD3LS4EG0kgtV8BQaaRsV-vrm8Do9h-dj3DU-Usqd5ZTUd5jKDp1AeYTtyKQsWujVBa5oaPEWu2TbyuX8stLyK_Ab7YGJj-lTZOe1evKpRZfyohBdRin4D-zjwksyf6IwkBjtLE5O-aeF9NMUzpER7ZyBDtx9rMO_lAUAyBeBn0nUip2RxfAdr5MiqOBjcZSTmjOYgWYC0QhxmcE9x1Z0Oz_GXrmE8gfoC3eiI6oAP_PhD5406EUwk1Ie2cYA4EuyY7HEBjN6BfP5K_aqEVMhOmk96brxuW30g0xhHgiZ6X3mM0XQO7IN447-coFh_ovba6_6TKSCO1V-kRLbKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNk-Q6b0-0x_wI_IIAtfFiykbu1fKx4sn_mrEcJFUle-s-95aKyu4WkJ0Of76oXj6cbuk2bhTUDdIxUI0CECTrfB4B8j_DtgwBQHaKybchctYbtYcHn2rO4u6IbU7nsDkZ0bg3FZV7_0gDt2QtMSpGBjqdshzAR9kLFwtrnnWfbDuQ0Jy20RanPtI_3zV8mZ4_OA3FMPed0ddUcUtwM9YZp_nJGUdW1sBPqr-fpO93r7bHfZiU7qSJC-VriAOVZcaAPeoR2wacVxq7FbvYmu7OxZyIcyyoUz60jf7nD7zl7dWzgmTUIg76cy52ohBsa5_8emG-CXRz3mrMiiQCyJdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNL_C01xiwKCjUtiRZjdNDBCBZ9AOBo280bdCuKyvaZMA0Q1Q47PDjgRQHFnH4BVKWADhwm4HDLvDCmNxMiMbZyaZQpcv7MiKzlI1Z2REx5uldkLKWBNgV-1OZVaCL0jdYekTuZqW_fzlR3TF2R2ekVcETRlZ4M3U1DM5-kbDGWwsAiqe_oPGFU7ELZK-3qrvtDs8l0e0U656tpn5C2eNRGQggJk_4t0mwtiqNvxqjXXa5A5QkW6tZtW1abAkbKQxSYy2ZMKeGNxZ6qYkHE_2BkJat4XU9Oc8UVgikaxSagkaZ9VmuEYX6wD9tvPn6YpDFsrxaon358QK7NLZOeNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPLgsZ7Z8tROMwOqxEkYSiW7EUW8kFDIQ8QiYaN_N2bHxmsMqLNeL1s751ZDHvWpeJjIEtyOqH6VWhykhWjxE68Q6BczW5mJdDLcjbA3YD8UU7hLEWzeJ55nAy3Y5ElInlPaf14HIqRMFsfsgcnofWps4RFRcxXrer2br3KrJnHg0t-cvq8Ab9Ch7Lk7VAkAWiXVUdL5YGnbMvvJIo5V8P1C7UXrdOn0w22_BfzIX-dkqsQhUUCpEG3ndRD8r25PuJlq8-PydoQhce2LSvhisv_nuNQ3oboUb4oQ0ZclfvPgVdW1y8x93ME0CmjiwOpvY4J3D2d3CHuuOUvyKIUFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5UWgQztZzCVHUbO89l6ujeQCZ1K4PP2eaa7nN_WiDgJ9mlT0aZFpwwuRgl5AtMwLU4EKgRrLLNbOEUalVxJa7OkO_eN5_47Az-i54DvCdpTKjA3aOqZEDyVA1J10VPZAeay0REMmm0U1NrdNyJOPVgA2H4uj1VsFGxPvQN20I4O1iS_-g0iAlVfyaiVaHddsMHW5FetB-PTcAwYCKC1vZV3dosLJhfu6lizbfD8poHQutiM_wtTxGOjWfIX06nYyT98LbXBINutcTbv0awg8FTZVkY6NO4x5V_M7BVjxMc0fsIZAzb8KHrQyZmMe_-Fymp2I2nENG7FJvl2PfnBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjzlbLsv6ZPbrpweOntQqwpap5WxjHDkTy8cQnjZOyyHmcdaAVtcSC38QyqObxxP3sErAuUua5c0ve3CVpQgQ0-QAtbCPMxw9MmdKLkTT0XMOmgjZH8LgY8uCC6hFYGcfZU09pXBxI0ezWpjIXMZXDR3w-ivc3eQYzk6o2LEBtV0JsHpyo3_-6e5rxnSsoBiKRFKszDl1X6kCT7oazTCxt7WoRWl9EmjiSEic4razbAJT_wu_LgljKrFMA8IXU3T6CUU51tb7CgrsTEyzkBJW7FElITKKuNbe0NYklzMoah7TJd8YWLR2gSPYHpFYl-LomSVVjXLmNzPk4ZkKpk49g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gysAf6Z4tzlgIVJGEiMgEPkdz3bzan1Tm68Rhn5E_0hT12QrOQ79Y55njx-5RT5_r_VL16h065zX_A-v2kzZx2TdLAO8VUWg__B0StDPTjrDeqGn-A6LIkYGRk6JgCANwQWQSEgxOM13-1hCHopgj0JX2udilnWTg7L3gtRWLyid4K8jnUUmGpdUxEaWiHZRjz_Lgu8M27ixQjODM10Cad7Z3YWxZXREVtxE3Gfp-2vEBhG0qUY7roWwSe7eBQ_m1r-aBr1ITqQybskw_UISa1pQbvwjGau-1NuWj6O8GTD6rakC4EhNa50Zs3rZHlSiT34eSzaHsiv9J8W5Xp20nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeUDHlfWvgUxsOit6A9gF6pj7RMtShee-eFBgILB_EebbOLESaPTjvk52nbFRgXfpbmrVtp5PqoD613VpR01tcb_t9XlYEK12UgwbDU2UjcfiHPlmaoqzKYvK_wz71Zdd7fXb-RaPAhoS10R6hQkI7KsZhvDuHqLKRX046pqgzsriZ81gmlLP888d-pf9JIURkZ1KaPEYfwawe-ZZNFIpojyhrk_VplQ7ph47UjhkLr0OHipjKtP3chb81HNoDwujY22OM6joQTBBhRr2w1elvApMiC5hDfnbx0dCTpQJD-P0skwqy2VjPa4kOxiuVJTWRsrlfzwOarjtI3dKsY6iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0t182d1JQy_a8vWoKdfHL2eSyPiUzmv_wnMcg6MEqpti8FduJEfLtO-dJR2L0UuWMg2jVhh1321W74koxKrPDV_wFzm2t_7xRhtOwBl218RcUByp_BWx2d4HLlUCtJL1RTA6W_WcOkTbNHlAdJaH8w8f6M2fAFTVpQ-iTGhJWRV-woXVaddc9KAyrvJY4sjH6brflXP0TgUKmmyZCHQHZ7hjSpV4VAkB603Ej94gFDi9iOJ-2U7s7Af1SpPUUqygYn1ryomFxOREW5pofOp038__n4_wEUdd2R7CHf1_D-wFlEnAPUQZtj-u5iaSDrelX9-4IU2QykOlLoP33oPUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIS-zHT_b4NzA59MOgevC2dTz9fBqXLwzUPln49FCTxuU86JRmqgt8Q7UaecRit0iBn09d3Pmux2FCCb1ocdgQpbiSGDImw-gLFKHMVTOAXQY6IJHtsDvfvJS1aiySfQStX7MmJt6z4l1gdXuBvLt2MpWMF8yVdrf6qASxnY0g-5QlaBuN8dVxmAKIdFUpbWoDH8S_xxDGsGLSPpmkieXcFGWgBCptpJzIBu5XbgmkgjU1D3wd_3YbXZyZZPU32Mr7MqmX5daArvll8FaQ7BthVraAqhmr71KQhJYCLSktU1BGxQiJOpKeC63qpNf_xN71eR7i05o33AAs2gL00r-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0eUn4eoRnFq4_Oz_NrOMsG0pvup2p1vXAOTh9hggiWnoHWeHlDZIM2tyqZeZSFEVIrEl4ujmv_e5XvsD61J2jXJepMR1uNkVsr8agCYTTxa4WYt1YXlH98oukCL73pts896fRXPsCYkZqmxAgAurKOMo2TRJx9gwsjlC3ZmsuafLmpYJULxcB3a4fLoChXBTZAqNtJWhXIOh22r9U5PWTUQ1JOWbY_9fVmKFQPKq73AsQjxK6eDrFHx0q1DcuQ1OXLZOv64XQ0sjedrtJEbgVtc_urCKVBToYbZ1jCZtFrS-3awLsKphYu3RG2x7E1gpyfixKaOAO44oeSD7CGMDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWeKBq1gpjefwo1gpWV99wW_Gtw7ifH4JPcWUL5JSy4-M_1tHkmHqxeG-D4CU5RTksLUNFoDOOaY5bnG8u0QdpB5YwTNU_KknHanqkYYT3sfPgzLP9173aH4kVSSU4bJdcGYhMlQQWAMcnYQcUWJGVTHKqM-Eq1kyQI3Ontgwb5NRZ-8Q_2gOxZNOiyWBIk_8KFLEH2z1wNM0Y-Rc5gujqRMa0JEoIiEmaCRS-dMdGujqZoUONLUvG3BQm4iBD4QrDT9p2HZnZusxiiNz6VyPqA-WvdZcewiv8fr8K01bBOmcBVL3IGmuvpVGCoVH9uOcaL1xRLkSuSx3UDqQ_K_nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3pz3J3Vo-TzCjA1KGkuCFXltNjK9kNEm4FzPEicA1yyO9kSzcOLaq50SAik1l5uR70G0obysK_1mueCZX9L9A2WHaeqQkngC__gEu6cdq8pc-GSY57l8xyeMIsJXvF4BjnR-zNyxLWTttSPyV1JFk5i-DRAKKsCYFgJn7p9WxDmdt-zldwgj3DhNx_yZDM7x2rCeqvlgfpx1CfEZP5UzbBLRuJOf75c1WHMpIwnxzR48sO6IAH6dP-9iawZz9MVRIZvjbJtKwX0Z0W3dBeHxZg5DnX8tE1K1HebIcshZAFUBzckwgxam4b6mzBjGa-ZZN7NhARqBT94TbT6z2218w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqHKOLN3PFh-8VHyFlcJTChxbVWgf86Hq_GNmPO3LtpZYybcHFRAQUnREBz2CCyl7G_N4poYtxH-u2MVUVaVPBAVtZa9ChhCkis0uFQ-un6CgeS0IC4SzFJIt9jzKDolMygOo1Rg6Qk9Rq_lk5IN0VHqWUWHGlxzIdFqDC2odA0QM37kvEgZUK4t4NrNgy_kL1BbIY_XkhrI2X0txeHf8fCrIgiz9rvghY3hoe9sE9PIFKqiyd8MhINZZDYNfTMD41rn-92aqn2CRV8Y0FzyLIBdgBc3OyM7dmQueQvNFLX9uINlrMyCIfzb5xrU776USF9FSQs3tvDqoAiRaq748w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNgC6fVSnpuPFSlDFuv-dk30sRpRyj4tQFkpUUCsRHEX0tVuXo74973qcvT6ZpdGXTAZBmmpYVc-uh3y15E9o2SWfrqLVMliwblK6KlXzpeeEY39aVSpZ7oQcoH0OZZKMiXG2yKuTDWwyel3_thagwNczUJLm7UDlPTQlgpHab5vOCJDGE2O6e_t0sHvfAiCZPoUwidFaHGB-47BgxNK6uOio6nhLzKQVjfeJ_D2V0XqDP8deICWEHwuqaUitJmY89vZDxl_RGltJwy5lRlld2mCHLe_jc0XmKNXBgeNYJGrnUl_X47H3K6S2TT5P6jbN2_tccMd-HKRc0LygqOf4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIXieRtAhCPXgkotbJ_faDvOlsPEFVZFBupGIXc5NukjKawAymo76VUBLDnazWO2d_W_B2U8e7zZUUcCIW1lQcwR1_c1fhWqD-MvEHWnmqBWCKxQfLCDP_b3smC3Bws4a_LARyMZGSctlM6vTITI0Ev4tiNPgiUbT9iJC3xa4ut1rYb5qkIjroCoKz6PlOc3qYEL1KFwqGyFjhaUVawtJRKb8gZb7ZQKslapcIyWxc0QdFoviSp-Mly9FdvAEFms6MO4fuJvMm3OU-bEMhecOMcxEtv7ZsTu5g8vPJMbeckjHvNDFv36rmNsB1R-JzcikJSBez_hy_9RZGsvAVAYAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFND0YRfJlG6FV6Jj9urOwjrWJ3c0BL4JmNRO3H4pMI1GCC5CdSL-s8gK8LJMF1yR_yf3TUI-899VanQ3u_IZBCuWGdgW0MQfrw7ANcK3LoXWGNaV25oCbP9fr_KEB3V5Ow1oztd2CP_JLMUlEB3KB_2Tls5JMf1APWc5ADBOV7R16k2JkiIA1RF6olrZY4VpnxQGvDnrop5IRHI5Me1xUYDLUNXBX49ONVVuXt53ZiidoWw1aA82cacZQPU0u_8EMO-OCzc8QwkxT7mUZ39YiYLbNqksUOudZ4M7_AA4j2CyjqJQqltlbYxt4KZk2KUaI4TsQaBOHgfmBUdCvpitQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTENrr8BWnoDCymgdVAMktc1WyZ2MjlR975UUYM-KOmRQQ7kJ9m2TkLcDvjRHO4J3DJa_EsBgmuR7-weMRdrbMAWvDqpL6ZcPcpYUGiZ-iwW3mXcg6Zs2kxOCg7wmP23Oydtp6I_8Qeo5uwyB0mPuFgOVU32bw8CLQl5h3Mu9bMEMPSTsyQzJHe3V3n97JFzK1P0Gq931t_1IKYLarWrYNId6KjJhOFoHZbepZsbQ4aWmdio2y01DD4R1C7vY4T9Iu3yRmXdrz_fHjeGGWgjLhGMqejnFUwqRl5fNNj-NZu0aERe6rFyIpTsqLgZXwgsLxCHLRg2HO_D5zFtfCjyPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzKQo807SeREBfy0m3_PLhKiaKi5_TE20F1TO6gwtjzB7nSnQEAyysR8mOmlZOo8c9LINOryWSWuosOQG_QVuegOKnCFwnMFUD6XcJoAzPEs8mPWmfiACKXtoQlqiNg7qbyxzNmJMWFGf7Y0LKn8GBNDFCQbjUyVufKrA0S1FIs5kJ2onODFzhisjycVkKBDTwY1_Wl7E1mCwG49zcynByXvBXv1SyUD7CZoyC5dvP2exXikhftk0CiCX7bAgNI5uVHCnLloVtquMGTL2kBiAyYjvKoLf0otkU7E9s2kBSAMgULRGBy7WkOmSeuJji7R-Sav1WVYlcsstS7RH0EyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCwgABgow9paZpicT5P87xi4e6MphdfI5OzduGkESo_2fNwsHE03ODtkwgVGwsH-bEU4TrR1uhPHfQ6_VdVRloagSCg8GHmCzjQbgOjkfLXhvpLh3CZ-_EwmVMOFPi-YtW8dC-cb3b12lJOmPcUicm6LYnc1votAgUMJ0Bn_YfX6l-wsyjC8_dA1wKtnCI_wMDef5SY81B3QPmH0pYijkVRIZLxLKM7x1EyZg9JT4uo1JZv07X2rQYaD108DmK-QwBWR4-znqTOoD5bC-9oAi5H3lZ6FeKci9_U1bAe3_zatxdAnYXlnmUJzCNtDPqu9mZ-CsHWofuprDR55Q4OT2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAvw1MkxRB03W__mtccTWh77FJKyotEQDXWOXVd822BUUhJkR4H8xCm6-6orSP1CqWO-VSCqTvdgUhfpGSq6AFEH4DTXM2HeX6MwnTkxJSBntFHo_VDkQ9_cViTlgU-GuJZUoWUgDA0Q3w1m3r2W7ZR82jCWTQZjBneXJGFwl7IdBRPd1dZFkTHaVHCDNry8Xx_QBb1ZlJduFaWb3RH3yJSIWi7fdJhQ6OyJkVxg7RGNzmsqsHY5b7sOFh1vH4zoRDWnqUTQXum9_iQSSDlpds_o1962BJLHl7QqLy4VqJfolfktsCRrzOZweB_kx0QfaUDeEDCnDsSE67-BeiGEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQnLPfOJMgSCIv1LgQkzWduMe3YZE-GH9G3t3Z7WV4EDxKYY2sTTgcb0ZhR0NPNhD_Sul29w_9l3Xm0SBAnWKnDtgd2-Zp2Ch6z6ElP6yepEOxwFBVcVXVByY63UxiyQ8QIhyrHFqutiDqVeGNZHHcik4fCOmRSfVb1oGAg1WE9I7FprnhDDTY1epNP9dUlJjsblHHz1fYdPA9LSay8nrQE3lYK0TD5ko8qElwq-s42DUVGUcULY_MK-w5gC2aDaLwWYLNRZmh4BwO_fISBEdRqn03vE2FVTOoN4rldPZrn8lDBmqBwFBxhqkIpLNrmfwE6a97NAaXZNuL1p6i_yLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNhQtChUNrPMTEmz9KF9gjioRAA4zLa8J2_d8uHMnLvZzyVAKiArzm8f-9a3TfzVJK-DSU6DhG_-qNn0xLQsdMUcq8B9JNOXKshU5ACYsOyh8nzpbeNCe_CgRIq__NMqGgKfsiOUUv1WYk8OUaeXbnpRE1gKoBVAmOJbDqI1aRX4_6J75eynvSWNoblHq2Q4FoBu4TlPhPVsfKnkQNTcGEaW_im35MYywpPDWf2KVump6yOgIaXFDR8ry1TCbMFppCneSat2gkO-6ULQlhqDBLkl8CciKtBuvaWFrQ5P_43QDNK941f-2w1zZ6nM6RrHvS686DYaqrOMfw-4DqQ-dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vW0YqTML8IZIh7UV3L4n_dd7BlFt0WCgQg5FkTKGbx7KK4jKLUBpwQf71aF2HOxQ5B9THZV1GBBiOiYCC2x8brvzlj5VGwUy-benPNqd-LRLrStZF31YAk6vwSe3m8zdvHhE7Qa9PHIt1coKSMrY-YXAiBRBpyO1XQm2BXGXh_r16C1_t5-3W30RfncY6KuHqUDhHxmOieiMqhPUtFXaVTF_LUVhoBHrO1ZD-tE2zH1n28MxEOUFmZn8acJsxCSDQstolteF82gpsw7XTKW-YBLcHxgySazAG0ALm5svFDYh6KDQm-m2iUSQOSJKJbs4gK3nJ47R6GrmoxFU6NPibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IihrODS5DPwKkCTZRjxsDKjQ1yByxF_46aooh3DXyhAN7m2jm6vzI4oULitHFc87Obk-9oUeIc6B39QD1szlHLSCcSDaVfHSd58blaQZiKfiDfbADuQpvhCF_iNOaZghCP76tb91WupP2Cb3tXe63Ss98nrh8lNwk4Nu5YV-aB_qqlWLwlXlvA9xUrlwGfs8ck3QfEmTFLa8reqmuHCD8i2LdV0ogdfegTbMO_WrGh-7yehYm_PuLR-xKZ-sTkBwDqhK_VS-KWsCmK0-w39FHfxaN0frEIMYZNAMxmjlxNmKd2WItxtycHg-6URqmv2YdwMm7M6rcP67v1Ef_LpvnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFT3OivwPCNcES6YZKoZJ68UCRonHUjavBkB4wM5wqDYKkJxIynWY9GuWmQ1w_xx4nHV07mdfqae9OXyGTxHc9OYu1grdWQKXLrVj-3mcCpOUv5_OuzirmYN_ePbQIol-sPoQ51MQiPIUHfRTpHZLarp-m8kB2IfX5siW2fOagDpQvF6LS_zlZI9YDZWNUfy38PiO0aN_ogav08_Z9KS0_geKx-L786EL3lt6saDg6jKa9Kw4VpX0FkHaN00vurNUdatHaO0w2prh0TvCmt_loc8j8YweLKotDoSspps3GKcgbvKIaB7T67brJ5D2NhoFTMH-elxzGeGtEB7xdCNjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaiP-Pg7SlOmj1GvOyAi91TI1XCJ-sQ0NO3HXsAPDVBP0ub8gXID1wtWe7gPuMN2EyDNBCa3Nstt5Cm47SRoEG3ZeSY2JkpEQumIyB1tssu6BP5TvulUykyt0fiPmOOghOJXO7Zz6IZknIMUpwRU2JDx_0TzcBrSlzYtFlMbCD4qU5Y5B4MJK3wQ671prJw_4DXW9Z22uCCiFBb_1ykOCQlrx0u5xJR70Y-CNf3OAfpCs24jJyNNxDQB18REhDTBaQz-PO7T6etuXFLcpgoKuvWXsRDQmpFtRaTkGGV1LUfFMNXJ5LneK25tYqi6eTalDsU4eKg60L2qVGmcKtnxoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqx3U1MyiugZge6gEkvsaYsa31HmRu3AqxeN7U2vZNWrm5YOlD78qa333zBzKi019SLao5n-G3RNYG2KVcfVj19Ac3wChSDw9jPd_JEHp91br0grh31AGZgBo2B4h9xFFBbnfTjk2-txUGxvwrJp3wWmGEL4uKXUET1yZX6rhPo4GsSbCP1TMv9TN_hM3JnOVd4KvmZ0BVEcMnFQj6R9SykQapq--JoJC5W7mzgfTDkxWjv5bylaXRrbyrLaikJcqdlEehOikuiSmdsfan0CDkyt9fQ-lTBB6PKYiTg4cNRzC-b8lyRCI4qEkrBJj2eYgPu9q5NpydSXiFNvQDDzfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmTMUgeM7DgK8_m83wzo1YhR1lXRLWQ6bsFj527QH2wKupxvZVzaS5yplNXPBNDy8ZvVFUBOxRDqHWriyNLgC1WVCh2rhJsQeve4cHxIuKkOErmtC8MVgwNN2cD_Bmq8n6J3xO0ugzVTiHNnsIg7K9VKJbyYrpQnu1C8rN36iNLRdAerN8A2fO5k7eT-OCMF3y9X45Aru8UEHEQ-dmSTvXnMcCHSjLseNpAPCZEDU9H0-HC_4TVKA1ijfMuo7DKZn53OjUDMRMJ8e_RVH6pbtG6EdvX1GEfxhRc3VXsrkzOn3_jPPsW5qvQ9ciU9Lo79n-gk1n8W6RRxCURQJgwESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sy3k33qoRW1UlYFdcbfX-oMzxhoQfE-P6kiUCJ8PsHeCWEMMEZzph6JaOUcERymmwGK5v5TvTf14gF0oo8PPtlYy9F2XQ-j0m_clRPpn3UehHe0uHvkwemP4yvF3-Uy27PrR2qNktv1wQIsrhUIChtYOTfGS0-jcyEJmx-lemCmA3SvjPoGTCY9wCts1uq0w0kNFBtpMNrUmgtKtOiQ1pTJRAkhcghoLU---19gbW9Qt2jUF7856ZFFbNF1MCc3IfPjFAiNdzuBhX26i4s6TQQnhD4Ch8mehfPhwo_WYWOLt6EAP8yxu379vV1M2UPtevIPdf062mPCnZg02wBiP8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMuhEksV458HYo77g6WprV7GnFW4BEfZO1DaJUcsIOR5Xw5rQJQTz91gHSAPA-Vc4okalybPPqmZYP5dNcIHRnSzO7J0iRrR-GacpFU1GZcCdT6qsn6CvNAfWIxMZlhZ4lOKesMHXsNcTwTzqgKiHyY3NRpQcEPftPKavcodsYOnMlgemr0G9CmrvKTKdmlhbJYXSkcVd5ojquoC5Sc7bLTJr7F1jM5AjJ8REaeEwgGyJBuuPdP1juFk5EHWC3sSzfTlL5BgbEk5W-SstuNzlwcXf9aou0zq53V2hMwtwTT140F6sMaJ5vUOv5PNqUKlRRsNVpuYff4sofx-1B613g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9eLhaK75jkB1eA7lNLYse2Mb4IsLwYjmr0XVRtFfbHovioDqI9Bd1fma1g2vNugtww0hvHCAUoU9klJR7NvBYM2TB2tJRQEFIGqHXfbDXp6daiBRTEX6b9cp5FJIAKnGmjvgYGqgcQv35iZJEHppTP8QlL8I0Z-IOWrUVTUSExYtRm_vFmC9ny5wUopDl0_a_BdolEfUH8NDqDY1eWU8Yw2xxQHWGYqOZJ5OLDnJ-iS3-bAEyV36GeR9xx1s3EJzV27RFPUbqJCckiScSfzM8ItnpZPSqHnQG5P5-B6JURdBM-k8-ZDiCt3-AY6y6Yz8DS4pY1impPXafqQRVFACA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAkkMgPRgDbeBhfYtwGKG_6mrIWWgqPiYKIyQPDvRW0Z5MHZ3co1WZHl36lw4DV34_PSfuSPoV3Dzn-Liu7YZjsCraG7v5YHm2Z8EdMEGgp_CxELpERvb759ClAAcxrntrEoo1LUOq6Twg8VhUXZG9E7Qn-Tesk5XC_VY7VfmWBF0m66kdgseEd_6r6FkgiCiLY27IlDk-AP0WhOPMKitZqwI53mbuh6YZq05NaVWDjbHexus_TgbiKFVqmAyi_cuFhZSeLp-Ijr2fEnMyU6VUyG0ePpHnaat4PwH74ORVEz_X-GnoC7nLZAPWqgq2M__cfw9BVlh43jCttqiafSpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZusGmKNpfdemqoeBo7UJeI4JxZ8Y9ZmwknzyTcuH29bO3sVGov8CkaSbiYwi22kvvlCxxiMrLTUwbwfuOChY4NLG3ALHDJ5KDFMqiFSEh-IOB10TSBlBPvCxARj-sN5AInLZwjPZgGInfZC1KmImnWkl5apisjSJNsAxLFgWB_ciL6O38sVYvDGm_m5GQvaLiOKJyJplkkop6SPow43UOQyEGZzBc3xpdUUIha18q55dEdAsuKfdcDW1PMy02FhLI55nwSBB4Fck4mcBANZg0jx1_dz_Li3iILPBiQ_6cAa0fHQ3uuRaVY0d6XSGszCi2LPfSlDOGqp3Z0QA0-9xg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=L7xDy-Hl0rpEkh7wOZA7boMp1roPFmyybZiJUb561Re2iG2pwQzzVs18jfKLv8flWzsE50iXbFeE-p_oo6H_WSbxU35uslQ7Ja_JWRGWAudenJ4Dl-QPziL101-2mjemXWiEEC3DzsafG2NN4AJ0uucquxYm8XCXWxNd-ndtLgju2Z0IQLxM6m4uMA2mAAskkLWuj7sasopPNThZljLoaFzG3BI1LhcOtJBeRSv1Kqgp1rxhDMKyP6ETuvn9WbwsMantQeFrwrRkbq3CTpobPmhWMxjwSOvu8KMWZWV-VSX7KV8NL4yd9ctcRHQVVilbwuA41f_-KhEqaXHFKGC3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=L7xDy-Hl0rpEkh7wOZA7boMp1roPFmyybZiJUb561Re2iG2pwQzzVs18jfKLv8flWzsE50iXbFeE-p_oo6H_WSbxU35uslQ7Ja_JWRGWAudenJ4Dl-QPziL101-2mjemXWiEEC3DzsafG2NN4AJ0uucquxYm8XCXWxNd-ndtLgju2Z0IQLxM6m4uMA2mAAskkLWuj7sasopPNThZljLoaFzG3BI1LhcOtJBeRSv1Kqgp1rxhDMKyP6ETuvn9WbwsMantQeFrwrRkbq3CTpobPmhWMxjwSOvu8KMWZWV-VSX7KV8NL4yd9ctcRHQVVilbwuA41f_-KhEqaXHFKGC3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBD04kR4fAOnN0f2us4tXi508jfxUHnXJdVGIe8s-BbA-0nXJpAhss7Z-wDldkc1ywMq3btG0K0nRMPAuxyMgF1BdFalwGbt4lJVYwV_mGCOwV11cz1BzgIr4ZZ-z2XR6aHowXrI7pQd8jHRVWmVlF0-hy4PudFMBikG1icAmWTReVCRrF5S5W4tReWSb2nw58smEFgmDi19xonEh43-vUBWTjcpKN_cdrd3gQu2gq51lOs5PTnBhkYT2HVw4gpNB89WVape3uqfGVNAPrPqyCU51vqksNfXO_nE3Zj2lso8B1xcmRHUZP0CbALsUbHvpJzn6Alfaznudzcsc6F_AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWnVT6nBwXrJCiIkLwdyXAOrBhQdqgIU-JtyCnVmv9ff8lYwKUxVcYDFaa0y79dPIf1v-f2PZPw07xsgkgbhQKJAkWhCqJUq2n4h0_7eHga7ZA6AkJ_K0KsX3BTmaPQ2tLOAH3uLA0IsSEAErgK6TqV2GKQPi52-qfEY-8JidpAiW0DyNKqEOo0Nc8TZG1eNfrI7nenXt7ijwmJikRolUQXVLfUyE-ZoqntojBfvFm2PC9ZfvOwgkYWfDMs3Fuy-A5-jVrHyUhDZg0oYHmUf1q2lHAiwH6eV8YdMJc7DiBR57hg1cDlZfvw0k_OnfKbhfHsrelbYAgAGj8UiLCCJew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ83q-zzA9f-F3UWk9oA1OoPDgIoixiGBQ0nkGoCh_9_ivR0YNQWYx9tZbqb-IuncfIHj9EecwnfvBXgC9F5rXHWX1FCAeYtyA7hQA2wAJdFSO0kHVozJAnxAHdZq-LAfGN4aGOwW8q9m67nrOPDII1z1XnJ3WHcVI40NT15GDLTK8-pbDkSxyWY72PDuGTCMMdReLl2fMAydNewPGlrYrsDpwmNz6RIrXPi7xB87jG53vHC6TunXMDvSCvxY9r8eDVvwJRjC5t5zLeDd95646Hv0bo5sr6oflpF22G8J1oXqJuTbFK36frxe43GREm9k6eb5G2v9pD8fb9O0MPV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mW9hxxtBE30-fUYkWzK9TRLTtMDQip6cGA9m29BKkS_jk4xs4CZT1Lw8SNrTjzNWJLNaZptOaFk5Dd2znTTMHV6xWdUjyMH3td-2i0_bzrDn9wk1LK3hyJCVJeBJcw4fV2L_zb9cqrVRJEc38BDVJth3lEugA41TPj7ROSUW-WdgCI_01T552CDOQEigbG7jd-k7BbeTYm69XCCVWhkghYBGfvN4MEJVP1yXl-e7J5HnYZMi4VvNfFtj8mTeM6_rh45wMqIr87qU713GkQLf1LN4Jnw_NM9e-QDYsuS4DfgSYcsvxdjXYNhgymG_kcb--R0vxdjkgg5RwpxpotBMyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nD0Dk9A0ByxwEcdZkXICNaqhkG4rRvfyt0PV9s1_zVDxyDExiyta3AslUR6gjWKQG9d8Pz1zS7w1W_T9iVSGxQ3chXe2jFaAcK6oUUYvi4iWgn2o1ApuvCK_VydhjcFPuN6Kwp_sUaAiX9w1KpRGtzCt_O884mjhGTgxJ9kv4OAaUbtsX9np51h9EkuzwCuajKl5hWA0eycjlkFdp98yUE4gUOli8G6uopMIW_OCgnV4vdKagkwSohBLArzYFyb_c6xixHV6bViXfuULq41MEPfC2JSK_OV-JwakiK2LbuSptgP7tEJIWfzAK08bfaPNOm_9feAqWF8EB7Mh1oo1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLCXvff12tkQ1DSQ9JDAHIsjPS2mjaPtChO3ILVen-KW0RyDcjuCCLMkIjspvF73Q-qiMVXNgBhbGm52YbFT4MUg58RM1rgEVH0GnAWpXQDF1CzIGunialMF6XYsh7Etb75pvtmpLO3dy0A9nK-MNBr9Fv7L4xCzJn75X9V1OhGPQ2XCQyPuFT723bE4aQ-H5xBUgKjdtOTO5UMvtxY05qqS8i5NtTA1oVPyrA5JDrD5OJy3J4AXsR7PUDJmcHquYexg9AAoj0NQM2gEN9hDjMA9BKkMGlhW9kXX9i6XazgyGKWQb0Xrh-m5lEwJOuJzRhUtNt5SCzzopHWLR6FyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkVW85zuBLvir08blf8lxblQ8Tqy_l3gxwL7gSdL_FQi6nHS2rtPVC9dpr8m8C331wIe0xNf-bwvHMMo1XFLhbQX37WqONnHVDzc3J0vT1_9sDUfosUyTaeS1q4pkMpmA38sxDczvQeHMVE2vCbrGVnhFr8_-xLUX4pwv1Q-kgUnGgYnn2RGcDaxHxpYkVwJr7WC3D0Q9-GGdR2tS9vP_uubF0GPHSQSODFKWTYehr9dInNuwIvVMgJIY0ikrhlO6D5fMYolRusAdILcDMyySVynDSnSQMAbMRDNOGGy7Fm0vpwt9aCJvD_nbm0rP96mlCMT5iE9n4HR9bp9tInVMQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=R6Ad77_CIOsCx41JTMqMO8NWqePwlOnOxXgoKuXYEGDEDRUfXdG-sWj3RG3FWZ8-44JYzRBK-eykqrveO2aC2-hzn9sbWjTSVTt9vlszemikcINIwcPT5MCHhMU9aDK5LlVJxlh54RyRn_OpdzIzstaBBjoh4UD2J3cgwP3vsVeQ8WXOKQChvakvnzNJ6E2gKRsXjt2Bcnc8hSssfLiDlK42FHpbX8aMxA879E3gFxPIifMpVnZoBJ9Yv2W_RlUzWCtsov2t8Ze6kG6_OcTpZQ7Ehqg27UpDDQjfceuDSOoebooM2OP18bPNSn0_U_78JFNiA08ZH-UMYJibk5O-haJthbDyS-X2Rv4GvOluyugNeXSk99_fkU7r-QEhzCkf3aiPObh2pxMWUeFd67PIvimaUj4yCfQh833z5gYoTfWBRmr0LF5eF596kECPyt9b4lPv1cgH3yFVC-34Z3MKe5rOSpX2uKNVHlfKZTBZSACNWeeLG_ZoogVutz0Ch7w2vXVPd0rn9ScMAS_dUuyUhY5xTzJV6mSeV8HynsAL93zRCYnFyJ9l0P6wQFRsMMsB_h9ig0Q3HTJOEIPqWnAcCVt_crx6tp73e7XEpi-zGb7misIBihmppwpYMQgZjtveznuLH_9jGgoSdpEqPQU65zlbrGO-nlVdQS-QSHUD57M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=R6Ad77_CIOsCx41JTMqMO8NWqePwlOnOxXgoKuXYEGDEDRUfXdG-sWj3RG3FWZ8-44JYzRBK-eykqrveO2aC2-hzn9sbWjTSVTt9vlszemikcINIwcPT5MCHhMU9aDK5LlVJxlh54RyRn_OpdzIzstaBBjoh4UD2J3cgwP3vsVeQ8WXOKQChvakvnzNJ6E2gKRsXjt2Bcnc8hSssfLiDlK42FHpbX8aMxA879E3gFxPIifMpVnZoBJ9Yv2W_RlUzWCtsov2t8Ze6kG6_OcTpZQ7Ehqg27UpDDQjfceuDSOoebooM2OP18bPNSn0_U_78JFNiA08ZH-UMYJibk5O-haJthbDyS-X2Rv4GvOluyugNeXSk99_fkU7r-QEhzCkf3aiPObh2pxMWUeFd67PIvimaUj4yCfQh833z5gYoTfWBRmr0LF5eF596kECPyt9b4lPv1cgH3yFVC-34Z3MKe5rOSpX2uKNVHlfKZTBZSACNWeeLG_ZoogVutz0Ch7w2vXVPd0rn9ScMAS_dUuyUhY5xTzJV6mSeV8HynsAL93zRCYnFyJ9l0P6wQFRsMMsB_h9ig0Q3HTJOEIPqWnAcCVt_crx6tp73e7XEpi-zGb7misIBihmppwpYMQgZjtveznuLH_9jGgoSdpEqPQU65zlbrGO-nlVdQS-QSHUD57M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBNTUZKMJYJ2dObYof0xYW17PUT7CzX7GMutj5xyFE2aLtSk067pLGamU-EfJQChb5xsXbWKRrNf-JGPG0Ppc6lXAOPrHaAtQBE0k8PO3D-OPig-WlWHwMT9y73CZhCjzQGYJkR70-hAMS_jR9kJR-0AikNFWH-hVXTdxoakAEFBbu9aaIgZMA08_5VrBXQax3ylX6A7tfEawRrpwa7VqhsafCK-o_TGtgX3vz8ErSpVzvUz28-FSmirmLKLrplMFFnHA8KzW5WyaoFNnoBazBDTJkL92ctZHeDDq6r7Um87grp5Zmd-6nlF33oWUTELMfdUFphcJkwEM1a0vg59wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEJnyCCgOkiA2tjUufvFwQBXUUXAznTlJznIweUuKwHsl9cwqWgoO75suTKRrBHvOd2HXVODZ7FuiIk2pWSuNGNSV9cy91pzTpRBd6-JEGltZgiZJP0Pg2HoWYn8otmsJfCYBSmJ2puNOF8PplbdU8lwibhVd9YgsrXGa7IwCk-SUc-fHKQAMWfQ6dnFBo1DPmpBPIXHTsZPfTlJtWd-8rWCiIeAGSR6anSetsMbFuzD_AAien5GiZoPUc-Pi-y8SikozMZ4QhGfJWnjFHPWrGoqRg1Ev6m9nZjTk4FC8hEZK7BqfKPungBFH2Td2lR4b8a5ZkZTTVYKFuZqV5jeiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh56O2visBdjI5JXZTvrxvoOFGiPzw68R-OKsIxskjPp-U8RdBmss5t0FdbF9shQ_HvnYekWhv0phkCI72gjjERFbFRepBouIXaavLhYXDN42RiqJGbFwHujYFpljHYZ1RqQyeiGTljb3-rQDu-uBpngvzrkZ8SpPL9bP4iqu4HH1ReJo4P7jjVPK8dYeVP1fgkWFkYJJxAVWbbmoaP4LHdiwL7FmN2aQLqj6r-bp8jCnzMBrzj4IYBn8YmYQz-TZbAwx1OUCh94DE4RIg6X0PUcC6ZhotsvU-lUlt5mi3mhZr5e86m7HZRnE31B9tuVkagn-aT0lIbSAFBVgAH1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKZnWPPA02VS-UjuW5-qw7dRjpALxQzocJP7BZaJbAwB1JnEFZFxQ-VY5Fvp9cB9C01xyCDhWm8LEYPbAtt4pYfaNv_rBAq6wCdkTdJpSz3j-4RTvKMbPM0pceTqudmMhbM3xgbiC1iPKdBxmr2CjIWKBXfPIXA3OXSTYsPT2ET-njamBb7wfIiKsTXyJ3-VMgfQCB9bLS4Z41vpHpWAsf-nc7pOjhDpO-jAFbYiw9Smn94277LpkTDHubpits065Sn1tlm6NHLWSTCj7Wz5kBCVsCSaGGsb-ZJ7A0QKmkNAjXDdzPEFarRAk9CSq8FP8sBVIcNI2HkDWeuvo7GYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tStif1O3Ge_q8GQzUq3Fr2-1RM1UrgH6QXNxcKoY7WsgyZVvluY8_QnNbdK6bYg36e1MZzjO8bKjASIHsBf-3eU4DBU1rFH_RvMwZUxroQoxYE9fLuUgTzCCCfHtDs0axXE-fDCnvH8bkx36dtmwxMLFY6wjKnEX-0JVfveTvaoLB3JMjpX1ov_mdm3iauPrKkSjGfNTKqMg3PSU4yt1XjZfiE8YWomElu0JwPyvtV4lI11PBK09OV5A-KRNm78JuTkHNpeTN8kgzx4dFvBYsEG-Jo16MJk_7u71YBkqdmOiqnYHE2z3VsB2w1Of1rCv1lrZ2KoGngAN8c2MoJjvWw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RQJIHBVLYKgXiRALgf7rWPg9I6wb8oGs1OaG9Yd0TvamvGYSDJA_W-jW0D1ehIY_-GZXUIWebrbO0K-997SDoB0Y4QUUFc5QVs6l43xdgBTqW3X24LSWDUJDFgvGs675CxAU4qd9SiV8yJGf6Aylw1dVMGwGCMpb7XNqJq_TUKTSbjRcLfJX5XM6hqlJ2L-gGnvmIg6-ASyfBwaV60tZQXQQ6YF8GjHiqFc7poJzR5-r6FAqDsvzlBy_q-YHS06gTsJYuU3SvY67ng4dv6w_nd_RIV0ccC_X-yrvUVUG2tr7rA9TIVQpvHgUj6bxD7YY3TQ10bJbEYJMngSd_KqLwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RQJIHBVLYKgXiRALgf7rWPg9I6wb8oGs1OaG9Yd0TvamvGYSDJA_W-jW0D1ehIY_-GZXUIWebrbO0K-997SDoB0Y4QUUFc5QVs6l43xdgBTqW3X24LSWDUJDFgvGs675CxAU4qd9SiV8yJGf6Aylw1dVMGwGCMpb7XNqJq_TUKTSbjRcLfJX5XM6hqlJ2L-gGnvmIg6-ASyfBwaV60tZQXQQ6YF8GjHiqFc7poJzR5-r6FAqDsvzlBy_q-YHS06gTsJYuU3SvY67ng4dv6w_nd_RIV0ccC_X-yrvUVUG2tr7rA9TIVQpvHgUj6bxD7YY3TQ10bJbEYJMngSd_KqLwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smOf09QwNWLO0ZKZW6WtzylLUP-DjWx8EBOczY6esbAdkciNHodAMkc5XSuTl9N0Tswx5sllOLR76K1PjYdxc9Olv2oNXO_-7ztVyP2VYd-TIFI5YQlGXcQFxubIA7FtybEK5gy_sUm10MbmNDGeo54yAHw2GZAXml5IAiLSt4QhV2oiHUhgBf5snqjXEP8f_Nh_JlE7YLR8l4B-lo5stvlE2iE9udrkdgNESM17-JCjK5jNuukAWKJmvo1ZYRMnOwAHgwIadehTHDQ94G1--hs5eIFk3vVERrJ9a2HxOyEC8jh-nB1Stcc_4ERSnljTHFCweTuUksFaxho8w1b8mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKXS6K3WfdHLTj42e_hUsSbuSdl1bdzBQSBK7u8mqCkItteh485sn3e2TDJ15jS3nwxGOw3O56nLQYC24v7L3Q2GqNgcTYWz6V7cCZJwvoyfY8rfzxziBKBr0yX2oZVN89I9pYoLbforSGzh7PWBZFdxZuepTSgoxJtIe2qDNLoYnLpMUF8XCi6dnX5V7EPRVmFwpUO-7y4VfGSEP215xWHQyWy1WmZENAdEmzhL_WtULSg3RaPNrlyRcgmc8CWs8H9OPtHm_RtjM2CN3fB5_3mdJOmMKFZLumetvAYT_8IjWeuEH9qVcXDgOZ0US1tRMYDzGP7rciFfvZJRDdA77Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8CIknjqMTyVyJ20OtpHgxcuVGP8CuD5AfBvXejH5F8rAcovsssD5ckJYqCwZg7I1aNjghybcMWFIV7-wr88rh1TBGh92R-HsMUyz3tlTYG7VyYjobeFf2nbItDc0UDnI-9rkZ-Ou6A9aoF8HZHsFHYlFosCxD8HfQdnzdncAZUQ2KNRBV6ilusKDlJnKulLDjH4kvfdk-GqLMj6yUt2VZp8rzmotAPjDR-OivSHnR1EJaFbjpD2bWjOFXAxzUKf4YUs0w0fptvzKZb4eTJXkENgTtqjSZnHcxrm7FE3OOjDbQcfJfRhfZcxzdVm_bAyBUgP-Eb3j7v4seX883K7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jii7ZA4awlzf9shyM-Kulfphtvi1UZoH6Xpr7svkdruvX8ibw2OosArnRJWVUdU9gWH4Sz9VxpYKMqJnP-tqhDAZbYpvrmszVst4AWRAPImWZ47lSbX4nIp6JsG-4fTOQop82N_Aob4BL1AKYhkBDCBmoEwxFq85DO7msn4gwLXywJuLxKOyIkpNqbcWGAohyo4oCQ_TiXo36KnpNJsqdqGtrA_aKZImVxQQpOl1-tTcAHmQ1QYB2RpORTF4_rYniaV23ggIN8BjU4CcSdx7IXw0Z3HK2vmtRGbGn7lfQwb28bFRC6lr6aLbJDX-Tl7pU8lc0aZ9kF9z3NU6Ukz9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6w9lyEckQt1hC7Ycr8ty3YccPTL7Sp1a8tY4ADAehSY6FQIPwnKf1qP81SWoQpZqooCMQBKt-IcfegcIWARXa3bhMxOrUBkmlHwWfSvy52vzBf4JC8OpNu0ND4IrJtHIR07fQv28oEJO0sWk-wwfMTe84Am9hJmm-z_mjI8tiVq-oW0WW-Xym7bVPfcfU4z6FTKY4UEa1lTXsWCxwr_WicItYtPzU_VawSdhFjAJthMUqa7yxD_Bc46tBiBlm3CEVx27kT8G0jtPpTI98oa-p4cLMDPog6qLhrmpyDcuspDCBLlXokrIvXwePFA6l56jiphfLgC6ToHKOkAHRqG1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmtqJPehVysPSZ9tJe0_kExJxhuglRQI_0cCYyOHzHwRUHBO6GjVsPx-WF-lpZgFF0BrNsGpVST4rUU5drDjCxyKOpDB83Y8t4yRTp6mH8F2br5rYJ3yMF3DwQ7SN0BWF4UbYr62SHuZ-J9WzrcbLMZPjlAeFmr0MsAKmx4dK5VmN06KMSNYgm7wAUvkcJLBNaYNKh-hRLCk8M4NWB33Z6r5n_4Ii7HJxQ4PV1OTPIAma1hj5O7SHyYEsGTYmnml0s5fGcm0fBRZUwDAk3jy6mX36CkcAnCTOwZmRF-J2VitREUuAi2SucREZ5qsTP092xG8cggpbtPB1kXl7yaArA.jpg" alt="photo" loading="lazy"/></div>
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
