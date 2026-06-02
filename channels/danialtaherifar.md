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
<img src="https://cdn4.telesco.pe/file/KB1AwuDIgmZJ2HFHAPlzl5DdHk3OgUVDyimsCxisT4AtHmhwimhtPy9-j3HmXOaBc4G8y7j4SbtQpJLkZXZxkD17RZ34xBFQlBx02td5To6Eg9GMTApoQQt-aTZb_9RKssgPzKSrQvqT2DWRkr-EWqm85XHJKQv758n_EbygAG7-a6rnCkQC2ch1jRMHhzqmq3KwbAS4NXqUaswumBuB3fTPU2xOrQhg9WcaqUZ0H69X9YEqHPlTUt2kNxd00YnscYDvc1iOGZLTynaBe3I6-6R-53X2gxjHa4nebe50ll8zIFQc9jD7dKQjJFI0VU_MAjIqT0hfr37p5zQU6QrCSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 328 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 491 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzLpUUkprFF7Xk2yhDJpROZRu9zb0FXd_mi-VC1IhQVrjXaVuT73uffRmMNDK63vBpaQaLcMr023P2MyG7rerCYSQxp8zfbTTi-2vP2HA-8iPEM1E2A59GkXB8cVN6x0aaToEzMwhIWYGHwbM10OSDmVeceK6p9c2BGfguz1fcIOEW5iSPvaET759JBHveB74DiECUQSGhrvDucCEidqVksu_pw1ulprXbNyyTVHo2BbpPrXudgU_hqLd8j0aU3pgOEGsnuKZgnfOan9lgOajHFsUmTGhs6zVAWHXu0uZ2glxdDpfIlK-kBNbPR0bcHMO-bfVg0Dh57_TVqqDv72Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 628 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaAEf0qjhEHFAqlGZK3-xiNWn6yHmKdyWqT0tTFXoXYyTE9O9_P77BKlFn7_Y2sY6dJ6tQtpQs45sdIYHfJYqIS56vFDvKer7S-5kz5W06OV4Qkak3OeGRXEBnKAcHaikw8GBKSlC5vjvK3hXUCI805Qotn9XHs3_JiDPacCyN_XBIYOE-3GdwMsIKir4clyJuYdvc8s4WHGxXPSlbwd2rh-H9iTYzx4lUDRthC2HQNpoAhxFp9Oeic0n9Vayzl0ifuM0K44TcPvStn7N7aqf3oUpcVkXo3cwglRPmYQe_Ct1G3u6W2APlmMTuQuSNBvVy7o343MifAFS_rSDvqt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0I1GR7UgADJfvKHje9HMX3GgdHKL4ISOHx0PzXb4H0l4eAV5k1bJ01g7qfWxd4vIuQBYcK1Rx6G8zdXxxi56q3Rux3VDNAD_s0SEk9HjnCnZQMqywF9lushQ1zXizGCqZmoDLCFAPNr49mfnKK3A37R8MgVV6sPWXQ4Ufb5jIViOpnuliUFbS7ltV7NXdV0kp12H5CJ4XcLR2wtXNUgUlbxtdqc2WqV0D6WZPXOJEW3MQfvkb0LJQCELix1VljA7u5TtuSiluijAeltYiCpiP_MESs_w1xPxOfQSsdj9mRv6PxGj55kV4IuCIoCTuqstWY03_MH-hVzZm-nVzD0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8sJP2tajyoddg5PhZVZOyAXCFrMoBNfDz2ke7lLk9jF-4Ehsq09HCd-RkZO9FmbZW3w4U9odt4u1j8h39Zz0IDH-EfYLmb4wtvXzqrwovwN5GmR0bPrrnYfwgMfCu_ztQL7kK7Q-luZuBeilsexTwKLzxIFTtOwGPLpq6fsJhWFU5Kh-VIxeLB9AED9YfNrrcebRwHyqC-efRxqDrXc3Vkv6T56vki-5m_oCjw6TUl2yY5O_AoX6aAh1TnLdw1LzK5v_KoXq2lUt7rrQVpovQmbbmyEMIEdL_UuH4SIAfwK_JMGrAW-LaHLdz0jN25KhCT4OWXs3zYLewcVkyy31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 846 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVQQjg8183iofZZk7NafWG3lkp8r3U7W1wkjFdiOjdDDaoaAUn6S_ol0WODVaW2tfGJBvPn4Te4ZNLNBraPwnMHkjO_T7ct3CD0rqhHIsygEyyL55TJc-DLZMv57AhCliV0FCvpP9N8M8Pl9Ls4IlZTPemvGcfnwSLeuZpMA8hOEOh_5_BcKKY4ItQqmKwcUEnKA8Po_EBR-Ss0igjCG2Xk2UpdrWWLhNeFdgLuuCph1LFuq6Pq5DB1YMAYo7IknEGqSfsK-zymtFlXcYuLnJnBr92KDXP_5KwUNihy-CAyrgL95sVn6p5lJnNbmVgnB2r0GEKyey67glwxrnY6c7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtZixY5cb5IBM6_bNozZ1jrS8Znv9u2B-xwllo7hk0nqKw3rxqyC5cjEczAoZCYPa_0PJDdq-tyWoMYtPZItrwQmayBmxMEh15q8_PWSBNPLzK2qgfxe1KasyOJZqKTpfh6UcjKCBpLOGNV6YoACs3rse-PjvIgJo0iVfNFOQtOazZ8S_29fPtjpoBEc2cQK-Os5IFP7nkEjejzeMmL3Ft7r2GAImxG-uCSjqjhL3T6NKANcM9Hhr0ggl5zc4ROT4d8pDJUF8s4wk--Fy-Z9qwKzgGS7VDm4ZhR-G99Fqu7wUFAasj9mCCrZWUkG2hnUQLYSJjUtnjzbbzzaIDQa8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Ta7JCpLBiRhSbmv8ya09YoIW_kPooi7l8j5L1P19894w3th58y8vAnsGDHmRKqYmh5ke3Y17ABEP3eDO-oGDzbc65uU87jNpXcMdV34gfn0VnY3OX484GFtEkjKxVvhq4ddWsp77AG3Ro1SD3RGnhafjeDXO3guVg_f677ErROqksSuiCDbM745WCUz_9nj6C6OjULCfOHaM4Ls3L-fCn_N3cxTx38HxzrAs21_FNxlicXG8gX39-iX7uSoHd8r5i-mvEukOni3xwHTUhFziFRV_9xbgfiD6r0dafoiMWv-C6uSMNmJ4yxcu9nbtf5dSdEA-CONwdODUM8WSXz9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiivO48oa_2LD_b4HN3whxg2vh076Q4qhmZAS3Ftm22xc-MlBd0zSkAAyEL-XglwKStadvF686ez5ylGmKWtZEFI4Ko5p2sJUQt0NCrYoezHknKjtte_pCl1iy5vuAmIpX69PF2-chRLrMxPIYxuX8SpBtXrpgmxvRTpU5ZQnq_sKSScKyAt5u4fl6qvEYFMctp0RNTa4ErNxd0iZA_R_8udW4eT2BZyPUHq1NuJijOebx7vrJPonaxT_sVEp-3vnoc_zjSfoM7oOefH-aFwy-HFpAlFdghcnKqEpI56F9wW04PEtRFiHABFGTWxNwjJ0Zqn2GtbuFGe5nYXC9r7ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXupVYJwHf0FKnwBvaUTzQxI2UoAI6MvmofZLdi7-1w1h_1f8xmRZWkk8RWizzDGwBJyLcwXaWWkE8MfFv5I1DCQBQ75pKmDpd2iKgbj04R2JMtH-ogfgyTbh0l0RxGPrWpchzvbC-Tmk1nFlwpQrnkHB2rWOGaernE7YIc7Vr2Lm_2MJSfHrn8BbsjRjf7EF_rjoq5UyB1cPr4_pmpY80paB6g62nir2HydGpP-h0L4Oo0c66rzyNy-AY4AAhPfNnG-7-4nQeOcN_e0qtsHv_Tq8aSfDY6gm4_EsnxnStXGyMK576YuGpFTpKN2oyLtDcFjEl_JLojx5FU-EJGlhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgG40igTGUweeE21rExFqZMJjOvmyJeeXU71bs8CD7COpweKS3E3_4qs4CXms2mcR21NWXnDpyUkY-yx4_TAFzRbLAAKcxOdSoNMed0ZpHHRhZIEPia_9qP8vILk-X9qh3DaL_ROstoJpgKkCIXBTBlmDmSrzXDQRkdKEvcEv7fwkXdDoZ2tZO7OnZF2EU-RqnYK1lJAu2yNVKfZLJ_25nMG4qQl1nECOvEn92imCpad6V4o9BSq8n4Gm5jDIW7Z3V9T2u35pRwWebR2bCSBkgDD46fySoubQ6IUzb2maMD7R_N3QDDrI6WgYUrld2zMfGkot9te9vLoCMrDTL_uYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4nYt7GrsOvQ-EDxIyapAwvuBY_Ck6nJ1lP_9wf4zcHOudZMiZWy_4ycqKmCcbRTPoOUIgnQN0HUD62MqF2EqwKhqf-l-kYpL4q8fsUlSy55DouxUqZRo0jXaJ6CWX5ouXyF9k-Bh7ov6Q4mMejC38LDmSxa1UDQnM5rkE-5P5TVjnd19_w1HboLASdy8vuL7G60dx0sV2e6v9_Pvj_MQNGWVaFr_CjHfud5onOKbRBEzGH_LYHBLQk1PLxjIEZ3tT3SszAlFyevHAg8DmfZbIdwRmyItCn1KPtFolXmX8x2gxxfT03E1U6PU1JpzzgT48s43gnteDjLZyfW-5odnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_bDTn-f11GOm0Mk07qeNHyYwkYJUu5VdSaUfQftsH_rkVKzwdHPmkG2ZBSlAp52sOMzrXycCpG7fscEYp2Xw9W7bAS7LAAT-EKOSP_OXB37NUbiHUrekSTfeu6X97hW8k12GSP7MHT_3LVHULOCbzRMW5Tibk0ByzzcwfDiy4eDbyoIX1aGjLAY7HJhP7VdaXtXXjkbtmxiADmJ8A6NJ86vGXNF2Mg7v-zBMjEDGVGuX3BsDfKiu2xayp-IFCI4TvJNbHNeqp5utv_opHP1jJMdzMlotTUwQJQOuWb1sEu2aGs5FK1gAHBUtUAU9wFTQeUVKPaX8rrpvBa_IRi8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_j-9OBSjkQbLDZNLgU3lkVUCbSFIAskwevQRbPLAo2JJvPlKAhGYggwSl0UrXzQkrIpFB2KVRdZASPrPl0KOm79eXAEMXcymb4_srjUSCWCmAnePG9xJv19X3-MuxrK2aVcCxO8wPmT0nmLNyXIW-7wCVMk6Ppp8NiJ6HDpb6FyZx2K8BnO1BAoI7QC1NZpXkVo7vaM5eRYm6gUgz8UcSyjaVeApV4mbgRpqJQ_6FyRI4CcnUnzg29rIo0ace2o6t5EcnT2KhGIk1V2Fyt0Bljoil6CWYUCFHMhmuM9JAug3LIdQO_8U3b7Q5WwYjXXIM6AlV1x40mZ8ix8p7LGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chalUBCIntjp048EOUzLPXgYCMYGNw55FzxQVlNS7czHMgOFTkqHZO5dmaP-GUH4INJ3eKH2weZFXMUbS-d4xImnmB_uKNtFtODXB1hHT5SDFoY0OYXoGEELa9GYpgjtgL4S5a6j92DSvk2DmH6sXurgqMfHSt8AI0c4ZAZPtB-1rE9r0PynnJ0ilinq4i7dwGyb2iLeJoauqOQKHKKD6Wldf3OGPKXPQ9p2xaOwh5VdCR6Toe6V5DUw478tEdRd6iw4Lr2je69RTjUOClIYD6R8olJ9eC9UBxgG8L4QLq_vTCQ0A1zHUJelg4O_lTVCR6ZJ0R94PpCHoaMKXDB78w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6QsUOcW2xnA9XdV_VQh_yXTeSCDsqsxYxFuvhYT-XZRBINMnOsFm0EpVzvCm0LfKHtf_w7l5X9cr6i6WvFtpnpSNv1wfKHHaASXQkTYduNkwNLXSbxQLrMWWzy7ryPcRTWe0IDBstlwB8-MMME5qr1TMZRSmd6VfH1uzlO7wnweN3zGbLK3w6zrRHWwyGklihXrgb0vZsxqVNXcqEr3gjBoJ4Z-Wm6zoGOnKHVyQXPSUlEcK7XSHxZiFLxqQn0A8AJVuQzu2Uw8b1uhzl91hCWIN32ewbT-h3Gtuv76k4b2IpDBHej_yDtFTujeQ5G3Lxsagrv8njnlKkqAb7oemw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=l8SiSse_j92en-b-nAXBGMwGOrPunaRBdiG8Il0bgLZVtQ0uQFn91MbyI1lFQ9vUhK1rrRbNO7ecvwxxusMTpzr_7dSGff8LcFu0iuAyJrRJ9ovieW5az2e2uG-GfKm9V_kHESv84UTgJKDzGncQO5EuwjaVuyMJtaGpYwj9XqPhPLLXcvR4Ix3EBPG1J35jmOHTJ-xPssTxclRoGOTA2oFbE9kzwzFhXCEy0shrXjDtPLEWv_ZbT4Z3v9xE2tXsbIKavhgx5Nzp-CDS98PwZ7brQuLWOSrZG7S494tmPv2E1TJOHaBUUMEt6q9jbZAShSQrQF688WrCN8XyYwzQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=l8SiSse_j92en-b-nAXBGMwGOrPunaRBdiG8Il0bgLZVtQ0uQFn91MbyI1lFQ9vUhK1rrRbNO7ecvwxxusMTpzr_7dSGff8LcFu0iuAyJrRJ9ovieW5az2e2uG-GfKm9V_kHESv84UTgJKDzGncQO5EuwjaVuyMJtaGpYwj9XqPhPLLXcvR4Ix3EBPG1J35jmOHTJ-xPssTxclRoGOTA2oFbE9kzwzFhXCEy0shrXjDtPLEWv_ZbT4Z3v9xE2tXsbIKavhgx5Nzp-CDS98PwZ7brQuLWOSrZG7S494tmPv2E1TJOHaBUUMEt6q9jbZAShSQrQF688WrCN8XyYwzQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyP9a4raxtkxefPxgQSSHZaJroGlSarvu9d1pkN7ygcoULPbpCxn9oEy4Hca004N-5prprQYUob616sNPE1zRfetdwxq7igqcVOA4r54gNaxz-Bxu1DHQjhMriX1_JgFq19x8dfnUEPfiwwU9FEJKczafzjy3VU5F2SMRgzpCvEa7b00kNthtIBhbfJ9Kv-KBVdifs3MJvqDNtva5B_Uhk81Q20OZ6hBXTGrbv0orRpE_gUg440-mx6_5fk8aKmzWkNhvj9KRvv3RF9QpV3q8BCQ5K9RukCLfhRN-OjAogcOq3U6J--A4kKvs-1Kakr44eSkCb-9Yg6ppvQ5A6PfYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAyMzSMvtkv9ufFbioQ3DHOhRevT9osqGVrg-Tc0fIyU90wFIA4amxNfMOXrdmSrLRyNoUeRFBtbw45v_J00x0C8-S0fHSBtTaP8P-_qPl7d7idTFKm8tyq1vIAbu3ZbnCPreEtk1A6WIpmvC-lBAjB1iN5UR1N7QrwCb0lZyTzi8G8cn7FWQEYj3_l9L5WkYDMtjFeH4lHW_3WnWS-oEy05k10xWYNXSmYCSAcZWbo9zjSTyvrZJeOpYm7VdHeQUzx_HSkKvSQT1nVHh-wfNaeLvGQ4UalbQWMyhGsDRL8_tFzD4hWaagTIdLZjSDNvWZeM_-qM3H-1qzqHmsEzRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtfVaewQgCarnNNvUr88a3SIE2eFZM4SRflucsNhc1J-48l9qkD6efTXg04G59hb_vD0I4AFugtUNdIlffZg3cd60fhyHRc0KLKfF2LUYkKTkSVGD22tec2-jwUj_IewM8GDzxSwpNBud8bW1Wzm7UIgPgTAhf0ljHrOffoULKtpT04taSl0uTna0xOnKDAkgv8PIiSZYcQ2-wQDq_v2Iquo3mlxikkC1iWnYrhPOhNiaAIU-Jn1U9K-JzBJBaqsVSC4dOunu0EmFZkodcasQZt3cSs5jtVg8fqZDR25ez3l_awSUOma4-E770I4Iv2fdAPMdOonAvQ6ux70bC_Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdl1G7qRA-SUA3289h9xCudh8CWLox_AeyycRz_P-A23assVRpgU59O9Pa-j3bnMS2Y6x6vezDGJwXSKBmYGQNaRXq2r69w7hd7MuQP455QbD5WBTAJ8FtMIMb8KCthi_Iu62qgj3CMJsHemUnEkUYMVCv7F5VkZ8IYUUBL4Pxdhvpp_wtSzRJhXj9Z-B0iP1qyjh8dzDYG7V_WXzQCtjY1FHqb7MVnWwlLtb4hNW4yKqNFjvaqqRVsh3cNtkW-D-l5_Z4ZxyCwbPfp_G3DPiXVjHFAiivz24hIDmmyAeF6GINzKcUSRLfnwErLCO_qdLYZXUWXyJcCOz450wPk17w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0nWZ3DKUfB-CALNwDY9poUI_caoX1q8TK82UK8At_Bhf08JEjjPO3A2KwOxJo3VfNV87iaWr7udukTQIiwR2hNqwz9YzBdOlFyEAbKzo3ggpwiKLdBEBpjLQXrTQ_DM7XVqsj7Jm5Wvp9NxLDMwtvw94ZVqBUqrdIi7goaYkOmiNhSAVd4NabjHR0idOARs59Ke3bIFahDCw3pQPvf1cOn4gWQko7EsKLs51phoP8_qAQWwfZLRbyl4XeqwTrP4WmPNnxlHEmsZASKA3GbcRbHAN-FSlBGFepBSDGUkkWqzuecaCSOsBaoTWyLVry-zgvpHhLkSGa23n2MdLA65pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqcvAsyhLn7qJgO2rcZ3nGMDUdYXUGPSH9SJZkuyztQraNkhImchi-X-fmj4VxH01ZyBbBy7lL6Q7aUrCAgrLnbkLdGT5iwbwXCox71u0ExmGrNoFXdSOsN2AMHCAhrrHJYUHupLH0ghVxZp2f6G-woJ9xeYgmXNiGmE2hbEg1mhlhXey9XYAR4C6w7OnPxjWzjD4t3WWludPX22OPi3asnSxYcr_qPYwPHgBFcH4c6I03hOt9MlI3TGD18dLiSSSFsG2c2lTEu7E67Ck8p2XFGbdfpE91Ug_zCNwWVUjX8d1GUqJzuoah2AWZzznYQwcV3hfxvnJGQ8JKKQRGwSKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGkWurH6YAhQo4yHG7-5P4-_VCxOKIm3k3zinLackzN84xrmLAYQmgjHaItfCpVILEdH3ASjwgH_2T137bZrBJmHWIDrh4yY_vLDTqu5KLXzsNyOpbn7Tl4zZQL9JMV9bTQ11BuQs8SH4sc-UnE9Uce1SU29M8isNe9YawiHGvWFsr4fPZIfQOfMZu7wKCtuqTn-8e28Udi3Q3t3F9zPV4SuxzYIllmCqXz27ZHVROiJ6FYR6f4DSRjUGW7d9JBdZ0oDR8wyfcFYec88CecQ3cLgRZtbl7le1JHAJiGr5qIRX8cpvf9VaueoIv8RsnS9pFY83JAMkjZwiVNbwODoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWTkYPJ7OQm2-cSaq4hIy4DJLBUl8LtM7US0wM4iC2qAvVw_MR0_qsIEZOVtVHDUQNgGoz9MQZyKBGnQQyPnZCKenVu_xG0IiDojrkBu40Ul_hnmHf3uVezQBYg5M2ubiI-yFFQuTc3iQrUCK-tW5JjMwbAV14UROFTQv0LGCSt6gWrWP9_dJTRfdKUGJ19alqcRTGCsHhUSVBnzRXLBrOxzjWLgsNOSuhupb3IKfgAYcfVSDfSyloYvMx2Ya9B2BDdmV-8CJiVKB1obyFv-weVqqizz8YarSTQMrqvNBnUYk1rfVs1Vn2HvwxOWdoY_ZryfqzqYlJFQDyaT3joffA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7pTvOkSHOdURicU1dCoXmYkIMaKQMpX_a_VD54L4xRJhtV9Jl8jMRRa639hLARjKCljqIFqM3CsqTE2-UaRoJlDPqxwh72s2Ao2WGQUUDS9daiyM1Q8n2pfPxOhrNHZtliMrmcfr9BTYBoW7ATy6c5Mbv2_0LVwzZx-1GbQxEe4Esnkz1Ya7LFdxcpIbX47qnXMwq_tjjSzVY_boiGv3fakDFtH3EZhdKBJR-99dVfQV7K6FfJ8A59O9E7MnhjqqsaaPBOFbrdigvkLThNjKs9H9xJ88dL8Dw14XrlXkKdM11BcAr_FY79YU5w4NWcKU8uO4bamfuYO15wdW2v4Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqCBmPa0gSR9Mi95_PWAmeHA1kX0CjK2kcNdzWzhcDj1TVuEgCmKxuXnPy_bszckSRR2rX3uAMMgIFLtMcj7oYVHPdWw1YPXHiXTtkIpaQOXp466EFNYYyN1CdQ95tWuApG_9BTm06xIUP6d26QxYQjS03C6ec1-AowEVHW6OZj0DA0lQRJEqdY5HjBhzFXpIRLmJO_HlXDuhp6KSH-Qb0moDUzdskp_Ea32jISaGD-mdthWKgXweItxH5l0Semh418TMNS9vYcNcCSYEmPMcIHRSNlWFno7wItcvyUDx1g81HD1UhHrjO8ghXz4Jw9fRvHkcdjbpmpPgkrlvJ75nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHoEn9FpsXKgdNocm5dQbksnCgupiGo2oTivr6oD_e0feWKbHfAvLy_PSoBV7W8_cr_4uqq5_limYAJ-2RxgQoDo-cD2cecH4nMQLTsypA4DQ9sd41ZKHhrclHY0Zz3Oq6IVIdpFHDpcwY2Pwv9UZSlPhI_nXpJRmlVqFTFu1kWWGYuXSy24tvyWJUN0C-IbZLAx84EpV2MG-Dp5vj3_m9tfGyYzPopdPYhvjHpbVy7z6SpmaUbwA6uf6fsFyVr3fdHNiKf3BR3MdJ6zTdrAr4AdHbNdwnZkDQs-CNbvqa68t3UNcgKk5MXFG_22BxkB6PBHu_ZVKWGREMVLpErpuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S96Gy4qOErK2e4gXtMujEFh1FV6DIY7i4gRdVmH8v4TkBqiBeqdR6QLDMY5Jz4ExlUgzBwQTq-kP_t4v06iCPfRVKm-2La2v_kLrtFysOqim7wv50kBVQ6jYqmo17T80_kXeohpOjAjo7XvbDBnZZ8K4lQRmoseNOUnntXBy4arKJF_oNiFSMwew7vF3inFFIcVvJ0yevY0jl1IsZAX5l_AtV0Laxpz_ndf1-Arces1a8GEJMArMnKSWEMh7vGca8Hupz5Wcl8DmFkckBFjYp46zt492RyTFihyLSSWDuu44bHO1zIO_DYIQ3tPV1uKePOW0vitIPFKvCQ3MtJ6tyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApLE07J0O4Zb8zEeXQsVExBZjAVIr8jMzwlqxsUbBHFfNKey3OOv4NSgMbZ8dqfiP7Z4QC-BipLQNRacE2KDNiLmU84ZooHrbUZs44MM9Dr3Uiu8cp5c5IALbxh-WJfZBPUtcgW1JbTrIvlu165ftF0cUfEsbWN97EZG29dxv-C23kHDcjjlDRyn-yKi_UdHIG5AQUoqnwzjiI7DQkJ_nwED7GyxY_s_xfwRDODI2SCmO0Ra0nQY5Pl91u59ICjly_RSozidy-zlzGkP0gCSE1r9WgFF2QxtP4JP5VG24rsp-KtKU34naTI3B8TgJ3RpFBoHn4evYA_1pQ-yOWjhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JD-8LcUQik8smFNc5X_BNgYAXXbJN8LZ3bUV7jeDHby7Lq9VnB5_DoJXzvXQa03RwteC45xWDix1EcSMShHmig8N9vsiBV3NoJ6_ni8Chmvx1_uZ95fOuJ293NPyRwe9M6qmk6uHyVdCNioKJ2LfwG1Z3nC_gHmIOYhGfEkbu3oE3puEJ-k7-H976a4sGFi73_9c8G0wag0k2HZoIl8H7Uh2P--482Ry7k8fW39raG4iLUSZMAy3tkoECL6_5G1-0FchGFEMpPCzfPYe_z7rFBHiMPlK4F5XtEWG0WKFtci-LWGoV7dChyrIGO8aU5S1o3Xcpxb5Xy8ydGYWi22cRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMBbWoz1uiCt9VeBPAQhwDndFoXqpHHYsuu6XeBaFR8bYLtbEdbTdW8Lij9UAVB8qDBMrNsV4LpDYRFVQEmaXp3LzlTDPKaAP8QqMLFa7hRWFZY1-kxJYB_CQzUIhOddJNdcq2hPk0-Q6E-Mq5UHk5bjeVrpQ7-J4_5k9-RBnmOnyybWuX_aY0HtZr0LUL7qEg0fqNGdTvj15-Tl_u21uiBg57wPJpEjUN8R3JyrI0gABXI9m-0INa3f3hAnTArNM5HIfP-dc1wl8ILITrgREDvFBezi8qDF5evScGrM3yY-uzkUFKsb_1KlpuXU5FY0XXFP7-1Omulbfq9sKYmeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzd6Mk2UUVd-4GTZzCJhWRcBnnGpRo-Iv2qbbJHhT1NgX2xQ6aOB3aGPPEu1X6IXgHQEQEE3leyC8bMel7SgVKzb3AU0yqEHNR3T-pKQwLLxDXPiigl8K1jGC8tahU3mlBT0uviwZ5SBE7ZiInsV-qEUeIbnwGg4USQxepGoCtQy_QZs3espdFR-iNXgrPxeAXtSAYVcGr6ZDQkzivCJ2vmlOt_u3nzqfhd-eTsfHqpHpbuudDeRv2sN4GFNltJn4szWd1kjBhOLWYszt00NQzxNd1GaR-spih8GG_xBCXTEXaqgOcIMcShAEw60O5jysVW2YMRIW_-iTtL-YB87Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcv9uNqqrOR1fmEznbZ7kt8RLaSObMGhLhDIiiW8reiYezUl3pueQvt4WyTnoKVGeSo7RNy0zn9SiuvNfwLIJIhY24I_s7sSrwGBFjtKjDqKquICQ0NW-p2Gjn2x9437ZD-1bAhTR-FGSMvEmwxYKfMoZicwmZJYZR66yH8NxQfk61RzKNsSW9Xun_ywDDCBj0nM4NlDnFLBVSoqgVRT4Gf49vWBCKFPWCdgB3fqSBH2KlB6uDuF73Qz_GoFTM2k8Xm4uUQ3xQCYaBOLAF0Bv9LiZA-l22rhchO_8iGv777qfQE_L4YF4hLIG0fdsEw6tGk2JRsfjOPyvg0Rk2aYqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptih4y6lAuF4dKCZCxPwkMPBzr-V9WoDG1wZoDgWJjo7Mhr5RlbAQJR0a3U8uPg48Np4DoGTABd1_c-dkwPFWNldZq1fErVZ0d-7GQhIBxK2hi73rOxkfYeYPCmyIOA7TmU6d35LJ4NOnlvaBZBtG_JlQFAecxL2GiB0M0qsjrfFuKZ_xYXBYb1saUkjybjnwKrfzElxBhsuGerpCVoZnmDTKShZGRJyDUckLp0P_DjWyIGpdfY_r1uXVbZytRwf1PQEW9RUFdFo3FebdMdnWiN9iiLieSsDCHkQK-nBdFS4VcKh3SenxcbkM3COTunb9NxjQu5LOC8Fa3BPeUSZRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoZenEBpS15Hvm4yJn0QZvJ8kEUwUO6vZBsMx0X92A3kr_Oge2AR2Y0bqcdmgVHW_xoKnklqx-8bz2S7GwXjUZaNiHG3qzAdqwpBB6Rgl--wIMcZAPjsp9VOOHmMYxy0KHoZDEI4NXIvdbbV6QmfhQWC3lSVSatrdG_3gqgg1nG3wjtKaMlIGHBepMVZXkiTCdr7Catt4R621zH0wFXrxurURlI3pZYxe8ZSViRzSShw5D6v8bKyGISjPYdlLUvzHE-BQ8jmp4d2Fmw8T9z2E5rhYG9P0QGKtfoqp_VyU5dDaPaqDrB-4aygyYbtC1U49A3Bu2epDBQ8nEhu7dxhlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE4ErVMXlZtTqJVTFD2FcB8BemSjkqRxZgrJYCKkSY7ekhUWHGyHktXfWqwadNsAnyYCSjgh-fP0725YfQUO7BD7dEh5j2U07NMVghf60wmyAjaPFSpGSZQWNlysBahLQMEuaQGKakTftnQDPsKwsXx-v3Rr6SY_VzfxP_e9F1SO8OYu55GwgdCo7hv_B4juD-7Q4wZ42K26pKJUmf0wyVeo8uFg76JCq7OZl3BsqkJqm4YbUozCDnUX4GcU957T31HCsnwiut4cQ7rbfSk3o0c4gDUKNciSNZM3Cc9Ek31sKaGKsawXtjiktq6iH5N1TFcndM75IyNqP8OJqcozng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD4G4hvW2NclI2HnIIGqezQkR4Lo6NnszA_UATxWkTsODR6wx6JKfUSmbDEJhD59BTZhpPWEv3KAON7T3WSrSvThoaR7zAGrOcxIxTCgr5Gsf1qexgBlsZGm2dHRscZokbt-pNrVbQvVhJN9L3p9Ndb-5ess1hdGcP0GrJONvziVLA_Eaku-5mBUMsEOwAs8PVuFbcC2K9tlnGwQ0z9bdd9vJSratlIfy8vrqsNLCEe2xiVjqevQrQvfQXKIJIq5g2uavZAJdFpA2nYVUC8JearfQcGeDwaalcCNDot2YXOCLy2LmvhxYKxMoJvCSzJRSQGYCGm59cFLOCdXDesPuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8oj5qfv8DtPnT-eFOaOlUqyOkh3Nc5yYRHmzPyMU2fIcIUjynMrIM-ijqaosm5eqWzXLR-1lOfv3kosaf8teejPFIcYOE8c86oMJHLmeHG20NgFDVZI-ecm7yc2oX94aMQBQ5dG_uJ6XwHADG4QT8zt8n5YekbipA9Zr3Y_srOenYHX5NhQFnUsvqsNHHkRpzyQXvl43wYPq6OHRMy-w39dBF7DV5ND_6AXvKEsoPq7ep-R1gjgsO3xB1aYrZwbI-Dz46ybbXTHRKa89l4XZSB1Ckg8-0zB0QIm5yd6Mp3LfyYAfzNR-oARmWRyAbqzYQo_nglif-qbByOgST5kHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6IsaREwtNNjt-3uNEcZIKWiYw0Dj0eEqNL9JM-qevOePRzCQaz5rmJNrUPx9C1siR0WN2CF4nT_BpLXtrPm6RvTUt7esOeGFbA5NReGLs5vlek8lVxWDMH77GmACoQgNt_f5aoLGizYycNh4--7gPHiL1abP2lw6-3ZoOClHWl4qi3Sw4JpeYPf8r1JBuridjItzBhyw7C6uVBj5BW0Bj8sRDoBT4DefJtLZLuI0V0shW4F5Pk28gRNAk46BNIJNsro1E1bBxgeZQQmD2HO3scH0pwBMBU73VNx0gAyJUqC3tjDkpD-sDg4PuLWdYoFL3AmxIe_41mvPjmIybaKkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMn_CqHwrYLX62QHiUZrDACFAnOPUqDHqkCBSNRndEQAsPdpIEgp_CYIeBo4b5SOEJbcu4nG1n6DnxYm2eV-_MITGHsDE8G4PurkjGUj1XAr4nsHsbfhi1YY5M5iVp5DtRmX0OsLdvNFSIlTMZ0hNh-6i0ZuOKp_2PKvwQ0jBpoWZTFREemUH7VAZ0MJvkECEHMK2PWqmaleOBXW95LzYG4_OBJUyGWwDUv5D7g4C4un6TLLUj_RbE3_5tMQbaNbdx1T66-_xfISViTyZBvizth2akPvDznOlfeaB3RIhgb0G10h5jq4ldsU_fPg3ocXzHhV7i70htg7KHqhuXGw8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENcjw3zBzaGo4AIPXLcrdpKrK0TZcBWE4Lct--3QiaBXqu-ATouNJnnKMkhWd3d6ipCIY7invbbbtvSnRPLuW4Im52kV2zTfSCjDD0tMDK59Gdw64k-_Ts5xCHxbdlcU_ALQVeaBgolori9YVkuwrEVPFzAEAkh6aurRAAfKK6YEb2gGCAagmcXek72ePR1c9_8n1JOivmZ0apTUwL_WqCaWNyOS4ksGXXf_jA6_67P8jneESdq3cS480JvViQjZOfyBVMnYPC4IQGCXKRIvnokzd52cbyPlrM1eD5-GIL7tVLsiGPSo77qZF6SBNAf3vnMs8zBmqD9QUmZfHTyoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BY5sR3AMyrdCii6OP_e4pIeyt8ho85VEiaqAdZcVzbmyehy_loGaybfRjXW2QwR3S94IyM21B-gRLmtZBiIyERs0pVbs3jz4Bry8yZOrflokj7iyZNe_Ij5wWZgdA3cVRGMyR86ZFSsLCm4q4ICiMvcsjnm8-HrH2T_Vlzdmawu0bkz3VhxwvhC1zsIoyKsnxK8PXfCdTfkTNFTZFGMToaEA-tOV_hFyydRqjJ8Su5wkrY7LMP-eKc1vvqjtq1q7XHTddl3NLSid5Jxpp5SjhOyPw-yoYISv4Km6GzP1Tea8z8FvFRFcYDKbtM5hwXlt-PZn8v7g3hxovMgBmBmhIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu-e6GDyjuD4TNy3yl5KH2_2s_pjoRJ7YKdgcZaVK4NjPfLemhNmzNBbcnlN7or3sb9JQebfd_ZPs-3R2C-664bLdwS7xUpWHfnj_TE6gecDHtfWUXQ-xkvIq79rxF9n4WtZ1bQjgl8Aw5nReSMqOTDsS3D1RIP9Ykc9S7J1PERrkc2ZYOb_lghz7jdMhboOFGDUsgpF5zkPnpdFWNfDpgg4MdGf6QAU9JoFdONi-ATHb8tjWdzuDoWPU33hLh0HqGbTmqxV9B2wxW0TkSiU3mSUunLZwwweKRIfHk4qhBqLmIL7xFpuj9DavH3AXqIjAeJy9WyeCRcyjG81QaNvVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irQfsyb-y8ltNn0O78Td5ZAPQ9QVRRpdEnoPna872jVs0MTFtNzmeYu8YfhVxli6Ckyrldh-OWdFcYkb1JXiv8-r03CkGaOZ2GWK4skpU6E7NHsMGkVz8h2CytkvuciuBMjvow0h1VWy83ovPsIolU-QrasPbYJtyfiWWFrHlbCdZS4plqUCaIcIAUmuyKFUK2Rdmw080cLDCl0Ob9n3rFkcdPuk1-ubVgNfBHM51t_qgJBc4l8KJJZgvipKkuKfdTuRuI487mzYRU3XLNTtnm3sMxkIrvpW3qZq_nvFfAGULqFrS0IH4Y4MFriM3izbruyLMube0545jLDflCoGHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCS0P4V3u9rW7yGEI2U5P5MF3ndvOt7uS4j_xKkhE5wWMILIMAKXsi8tFl0x_TAQA7-C3XuOjTcgNAosbR8wVtAxFeQGRkb89lLad08Y0yAw0Ob7xRFCcsNEZfTYTJOnnQxcjzqXTAvawoUrgwyjcw8D-cy_KryYjJ6x9MzxOOWGNJnVEhgAbQRnPVrpKs2Uagq5gJzYimOfPsWs4T_sC5jpyLyWqTYwNDsrdadJoIuuucWgeZGeOKePoyIKGvdk8zZcTW5f47h30MpIozFFb05KBxfdsYaCoVhNjqmVNQeZqKaJfJLOnN5EjP5_SaAj4ykzX4Tp8gytEDEY7bjC8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzGLyWmc-E1PRM0VF56QMifedWI1Moq4-hrgIi2HNaQZiYRQx0orfvxTSBV2KslSPFQtGS-WyJdVs2eWhunWYbqa8VMKQrEbMik_sEmmhkgapNcz6k5edH-tMxMTlEljLcBfgsXFzeQ8UVjvlGbzwIhLFdfp1-guLX33bRNE7cE_alwST8Mam6MNcCACIe6Zrd5rK5lKs-LjO5yDN-siNIPMPU01kvRpPEw7cJPnLi0Zz4TDupJ8c87IA1offmZAvmzPQHBFpEwyS7roNyG4ZS4f74MY84RVWuKVT7gA0q-gs_uuHuSjnhq30-1jtrwUdeAWrbIiuH_up9IEbJIyug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvN3_Vq8n0hsCtgQmHRXSuh2MShXzhTJm0ullvCXH5-bxwpBbG432utTOqcIbKYb_Jw4_CfmnCZtVZVqeEXG05MyBGqvXYynuMcb8sZMDZPxQx4JAeuZrKNRw-LlBEBzzUWitBwlXG510j6K1KPtShugdK1i7lU_SqwuDWVzT3MDnU3yojpYXWMDuSVgWDjjVZMik1f3EHvgtxcr0Q1skBXNsetZTMqfi_zR9tIj7TD4cn0mDFuat7AOg6lYRlP2682cWeLtKuVMgWTu1CJl1u6bQyCo8fWgdUQVyZf_ib66M3RcvPX4KIPfFvTTD5nqOeXh9IyGIPkkHOhEWkPE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_EW1F0rwzSUK8UVVHIkrIy58TbKHc_kMdLBT2tqy65qAEuqMIeqbtw-xTWX_vfYfQn9rOMv8Fw7VO_YZ9F0X56V547JilsdhnyVZGCwaVcLY4QCh8rCiyiq6pG5MfCTY6Yzb3U-X5awf-SBrmLkbi0oMVZYLknEkFH0eAUGzohaFxUyVakBn2LLOO6r0nfAb-6XxFvXThe8d9_OIpnc4xlp1nFk_F5V-7pGV6I_Tax0ZcMTpmwPHjXtQLrTV6KYwBt4sbsJ1_bqgkecKuuhCz1J30T639CYbZCqwDXsRQsbsd0OoIuC7dQKgJj6Gh9XO4wjcF23PWrthxiFHaAnUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5m8MLsgwjPOMWi_7tlPfyO69JJn8UvHQk1yBq91zcey1xBb2F1NlhzqdxlRitBcgS1RRsAadjQMPJM-ljm-igyPm-3WLxhnSriPmRa_F_43-9Ycfj47ExzveLuE7D4gKRxmQ13KLn1vOvCDGDA8DpF0PRPg7Y5wiUj-Gvt3OX3eOrCUl1ErqqshdbMc8eF3H3IAIegxLKhq6LXyVlW37r4zf__jUIYMANi7bxxYswDlj4--VUE9d16F_1dxFAKL9PUdB5aPUgua1J3HEzGzRwJGAzfKS2CjRg2JvP-3Te5j59PQXMNTuxSbpi08-vCNu8pMjPDJ4-vjMPahG67Xcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kliZRWAMGy4ZLfsUkariGur8c1lyuwKsHysaFUAkqwbOvKsIg5Oc1FLxGNmfKZBJ4GytjYo5kRTGKZqzqJuXd4WsYEZJm8243bVnN7HvJsS5XgbInLKNZZwYHzzNhunw2nggQUe1cuH4WOOfZwrOW50znWAMMfh6fbky-nBioY8Df4dxwuY-xLS9EUfZlHtoCP2qHYLQHk-auVTgT0hYyJuSl2qgJk0aJ3O9pawu-3hfx4WxhkYqn-9CaSJVNM-yLBnax8-VgtSe4VMF1xtY3ID1mUrZcvNJGPza79kBRggUHdttTiUCQTXjiUxIM7ax7yj7pZg1wPaK2KTQViytEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFBkeq8PigsvjXFHo26xOEhopY4sWiRKiJTEGKsgJ9UeQSMRoYZkBGhphhLh64mfpGGlWbsGiV1FeGfCUx_XUn36uanji7pP64byq9XWnBR7RKxl7kINZvwr2nZeKxmgfxu95pjLSpJhbGARX__htSjpnHyJGvU9W3ziKuG1WsU4hghJyOggeBuNd_VH8Kv1X28Ed0ZG4RJJ8P9jlozhL9bnc9VwrXhFN8l7XumWf96A6OvgZP9tY6XTlov6WZJP9L3ktzsmYUlyRn1FOARvL0UWIq90G7FySpqbifyF8rHUJAMZOUvR0c3d9Z8ak_LWREDmoRsmnfg76PDOqFI-sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Av9ecM-GwdtlOwOjva_q3APVXIJLgrUmEib2I0nTgPFYRagopeZhMEczXAhMOL3afMFiLMcD22e1P64F6QaWdRx9rjjFvotA4mG4mQgSWvBRIjKJKgJ_QDz8ITBEuuHp-uKrokA6b6TB2_1q5Bdx5GWzs4mpjL6q9BV9Z75i2y5RHJ36CppLY9IepjkIq9z2aIEitpkCD-mnOlTnEwzZFLTcIJFm7VbG6daw41TDArflgOGrFFI2166JWhpDBT3tHeU4GUOFei8gD9X80JyW324tRb_ZpdemdGYMo0MQHwARXaipTPqH4oQnPULP1_Ng-OH1q4fjIiT_SWAd1gZdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbFXlfaEZoC5q2Ebsrxq03qz1Eig3JNbRO7YhTlXHe21_FlKZQk-5qk74qrmWqqTL9qKkQl0T6emCwilredWbsa_hWZXTqKPYvNsejVbzDJN6FDqd9OjdCxv-L6cakyzw2Cv4D2VxGESfrrLNGprHzJ8DKzhPn7Y1LYCwjIuIa9zskoayo4IhrqmGVEloWW-7MU9q7oYfs0xDyN_6Z86xq9Sg_WeoHReaNxE1fTSVZQ-bQOt3glgimWELOO44dUUjGpdiESOir2MEuZ6vJTvrIsW1cnSbTKoTH-IeIljMHFfRqTgwchXgGqerlSACkFe27xSXlxM5pTXgUfyMpMTYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtcYtBF7AsyNUovBaTCHNJZbdWu6nq9aAk56Ug7vVTlq-ANmfVrtTFa1LYeku7orhdMXMV2nPpZua6ENiIVTy6dKxE5_pfKhHgPJwKAGPTUJEeUrGNSnkdeGZbEHBq8KG7ErlTuPy9xHyxQxqhgeMS5Cn2F2ezmsn-_46YOs5h1PluA0JroWBGJbT3Ap6nLDUIY259dDVdu2Uv43kwUcwen2B7j_dJ9oSQvous2bX4qoxgZ81Cypr56DaqaxUTGyqJ5YcQymZFnRiA2eL9LthGK1Hde-18bwOd156C2DD5_3KLiiKVeRFj2CFJflIkHYmnmvsYLWCubHvGuYlbYsVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpWt4z01PKbKoIj2Frg828XH5ZPNKFq6EeDPGvSyGQAQToSpofVScdtfyMpho3fPdbVVN0mJ5YxGGJOyZvXOxg53cRUqAg_gK12AOl3XVPTzn9X8YBJtvV2Aqfr1AclLvVbgbJUUtTKrzz4hJQTboKEqFskNu_FYbeMTHr38-tHEtMCl29Eq9I2vvf7JNxtd1lXjdVTf1kSFUBCpiS-8i4cY2vYW0szoE95ky1AM5Pd_OYpWt3IyhTywUNS4X5CsfPhJgXDQELG--zNO55lsVvuu4fqFEkuzITc78EdJ82lVFQ8hG0mWQb0jiksSY2IEVfTN-wX8QgdFBi8HQEo1Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqPK5x3_uO1-_ehoi8r2IxuS4t_U068aGhhVYoc-o0UjBCZZfkoPAvlxmou5tSYAEwmv06-054A-d8NlnIF-x53t7mPH5BYsFCDuoZSV9TFSVfMVhETPJ-877KH6EftnvziQA-zR_VzterpCc3m-BlSw6yteWbb-6DLRnrU4f7jLIheKqQCph4EuP7cIqHJ7xJI1-0AILBsGKo9aUtD2G-Nf4XIvIBYWcnOhaol8tX0l2HoIBvqioFtTM5ok_tNgyhs_rkYSABbUqUjSX9juWz16CgEs572dmn_pbSlKy2_qXaQpiv60oD75Jn7iTfNkdx0wKw0lqafgl6ohi4gB6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2xe7i5BQyJd59lp9ZcV-mBj7aIV9GHo9APvBX5YzpcUsKiidfE66V6o3BZmjeNLhocdvBU-Yd29obAPCaoSHk1K2aYk73B1HD-x4gNgvQdqZHeOpuWlg5Ub2kuQ5hBtv5KStFJ-vdD-TjKK_EOC5ML60m0cjUnuZ2nKX7Q-SSe6ln0NXCcPx_1RqNqPbwS27wZyxLiWWNKxA5MI-anZsvh_RPJHWAGcAQkeTwl264belQwZnVyAPsH977BAfWWxA9ZjhwRfGPs0BwfTtmyNytxrA-Av_JrbrlpGbehrqjcMWB1vE7yMwuGmhUTOE_nqrdl6_T9oWNt19jO5HMoV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfEcx7aMO_G4i3V8XRXWx73YRHGvrz2OpgnSGAkjQ-jn_50-IAXrX7qazQukJO3OyrD2jziijgwhgqkzR3qDdChfzHHe0VcV5NPP2ZAFDvEgiqWNP20dxIZCixpDSEfZ_nEBkkRURsT3kVAZKJP3InBjdLDTV-pKq6lmhlPDyVD0LWNwLy_HP6Hsas6mbK-wVB25fUOgoG4cHupB0jLbw_Idy0RT8dh_Q8Z4IFxKepG2qWIAsymmAywXFSW1R_pDG6On5HJh7-n86Mjkfw_aqcxeXNbVy8G4EPfWjz73h_7a6po_s15SqPbPHCj6kmbrpeud-qUqDRgchMAPRSqHMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2RUwgM0IoILm5pQxu9yKrE2807fmCg4B2ZhMHgiMuu-FyLuF56s3Cn0tuwDk_J2pHPcLO-yRefoEpc3Cll1FUod0xjnA62FZU5xO6mnT3jb03QN4SADRRj8UvAdtVDvuetkWJdt_fiBr9Uz9SkRJs6QwIlr0i2H7MNCZpSPXPq2NVlF2VDVkJ4-6TpMnpf879o3MgpmaLRu5pbwoCoVNVMgFTARVxA_UYBlMMuJVWySmfNn5O4TN3q6PXv68UXh0Adi6anaVPN0fujePTYf9i97w6WIyGBOXklFMfo-mfxR758yMCRJeMVScPmHWKUWk028xqKDPSW6v3KFef7cNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etWQ-8TovzY5r3WsDhKSbtX5Hm1mB-VIxZFbEhZiUgaSca8Wr2r9qmF1nLPLszzm4YImMhtsEC5ZtFL7R3inBI1n6WL-Fmi7gYILun4B_ipMPdIbVijNoL5Y9zESC9olhXs8GNWYhmA-hbSqZSuLloGi3PnzdqplcZNZa-6mL1dX876Yt83vzHnj6bfK7e3M1HvxcnY44TnkNcmspZv62A1tDb_x1T_HH0Eg_C_tnoQi--48oShgAwy2_0-ltEz8R4h4SbSMe5f-NeswqbLgzDPNnLII3y3dKCK3Blqdn4-DiI25G8WcsDDkpQbkyt8BXQaVVEnB7_v2DYdn_l1OEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiZtc-kVnXwcziYECuu8KqKAi-92T-Y9qq-CByWjFTaQ06CtbK7EgTnysXnAPYBKZoV30Ke2bl3oiMDJuQkoBgfKDy_nn-XFMUeAFyASL9N54hDrPvhB5BTrnrucUJtRvCW5mtCE-BbStuPpSFe6vAqL6ug2xzvzehMv-aVVmUxTaNngDGkthHe67GZCSlGh9lASyaI_WC1vshFumZsqUkjH6YObhyfchosmQXliLC0G0fF629j36oIJPWhM8klrMBpXZwR9nVL608p4iLg7vf_5BbymPHSAsMbiR8wE7flxfuZ63Ll4zikECwrstZuHp78vwzf0Z_GQxEOPGOm-uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrrWG0ef5qIYnkJim3NXkAOoyS9ErwZctkVK7aTUNYdylLYTY2GQXMNj3lOYzTwS2DAcJJHFnf1HlccyegDsPDxlztIJFgOZ6Qby77NPtTrGmbDBvOGgKRaI_omUaaExtNER2VzQpscsGPOcsDkEyB2MnsQ2TqpgnhOqQtCY6kLVPEiAAMV62LBJchk0T-dht-o6zEnFTZnGzrJDEkQ_ilvWdl0NDdl3Du7V_qk_85lhkrkMxYxlRcJFiWzjFP0kcuUq5EvsEvu4xzSZeWP5vuFfggTFx_5Nj_yFZ3qcpzKKSt3ugwr26QBhejZ6MK9KhBA-1xUn2OK8974DaOuT5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=h1TikrmrTEW2tywa3RMUy0Quw_eTITs-2YJAa8SnhJcKDRf6OEjClvXB7LEcHQfCbyU0SU3I9krI5xeQkMT06RZQH1KGuWJ5PW2I3cB8rmYa_Fp8GH5cZhaf8OwZk84XXQZZbV1IH0c56GiumVkjUV3wvrUZ2AHfEUzMlQX1uaycaQfngqqrKERkOmFq5O2JkxRmXxiKhEGGS1pSm9w3ekks0wFiAjptTIGgKdxSb4PwzDvtWQ8fuImq9rbecPukWy0CMolU05cCT-buG7jf9OIywBk97UZlhsrVyFnPwhkvvHEdA_c53-3xFy6Hd6nDGMu1ZJ-5Z6Sj_Z2sfSxD0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=h1TikrmrTEW2tywa3RMUy0Quw_eTITs-2YJAa8SnhJcKDRf6OEjClvXB7LEcHQfCbyU0SU3I9krI5xeQkMT06RZQH1KGuWJ5PW2I3cB8rmYa_Fp8GH5cZhaf8OwZk84XXQZZbV1IH0c56GiumVkjUV3wvrUZ2AHfEUzMlQX1uaycaQfngqqrKERkOmFq5O2JkxRmXxiKhEGGS1pSm9w3ekks0wFiAjptTIGgKdxSb4PwzDvtWQ8fuImq9rbecPukWy0CMolU05cCT-buG7jf9OIywBk97UZlhsrVyFnPwhkvvHEdA_c53-3xFy6Hd6nDGMu1ZJ-5Z6Sj_Z2sfSxD0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc5tPLUTKx-lGdz2Y3JqfKR9KMEHun5VvtnqT1XNEsdRAJhH1em06ogbGSUBCoAUyzE_Ew_kCPKXCDYSgyaTgnj-sC9y56YMhCDwZ_uMjrA_uvsNXY-q7rhJY9Lro_5lwPh8i8SFqgeQaAXV856apEDFg8QpyzZU7iOfKqwEtyrcXYKeDV3ZK6wB5SfK3Y-UZlQ9Oc8l3EjNSqFHQs88X8eM_98emlPa9KpjKN81lxN8AzRRuh0O80ksTPUg-to_XAbt-2gagH_jeda2tgA4YDezxDuft6Aighuj41mcKvAXaHZ9tq1QEmVhmICzwZbt1mrTbfzMkwZc6UzJ5hL0dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXu9MydWiRaqazJjbepswrcmZaEJMnkqGwp5tX_Xpgrw6uS8KGU4_wnAogVQ4qoeB82vkPy1CAUOhCaQVhXGSnye4Kz5v-FqjzHFk-cZ4p05Z07OTR4zHampClTGpqkVmPW-WvHPQ6U3jBjQXwiue7RVlhEil5ybNuY3VKteU2h4uXID6VIdGTQpO6u5_wpn31cFUFFeqxWVWg0IPAiaw3QklsuI4DoQfH-ElarNmBYQtKGol_xzXkizjfi07A4lp6E_O0DmF1iAeuR-7wF2fTNqKZyAqu6bxFXjuwRfeZSm9aSe55UY2I7Hfm8JiWDNjgXi58qCLKuZpmbFT41EHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oONuVLyYv24VFM5BrgBdFhy4So3CfIY3_lB47iUhw6hm7_oiGJsk8iBKrea3APqvPU7VFhA1Df3RBQTIhdYHg4ok6b_NaC2nhWeUUSD0qv9EKtWZkhw6SFmRC6paWqyOCEvkqfP5eCt1u8Zj7xqrDcYE9NlNqdC4OEhfcpIkaFJDhejzeZG8RbUc7fnB-zqBe3zcNMBQKEG8buULcCo5wrspEJvqdeRo0S9HDzUR8dDpGzUMpoPNwSAiCMUaIIkf0QKEJ8sNdS8ujsUXsXT0gZ1-tJIKcJbfKk-oEVrVZSdrsV2WEuafzyF9i43SajMNMYVSwG6ASGa4iSZsbRqPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8htxDKzQlWM9VPIjJxmeJz_pmzMx_-Pia7yzEuziIxx6wPjdgp5n9wRrMN73PKmy4AIIaEMhpxD5lgecWDxOo0BuNn79DXDy7cQyIoNWAHnNjh3bryKhgmQ7SMi0n0jNbFrkTHwEPrZLBCD09J54JDcwq6uGDsAgqaKyCBsSKOBX8w8EiSBBUZNXb4U2utEOPw9pvZriDnh1bgjkLiKcTsKJVMy_NidymJhKaN2lqcJtAsw1DDx5z2asfjK7q5t0pweJmSe699JSiq9mqlo5vb1v-H1EyA3uVgtjhipFXnwJR3fYvRRUTXCR8Ki2VSgqVSl96tOPqbVZOZ0ihLb2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2dyllHc0TPEZluzS25lWbVrl-5m4jBtjmg0iPuqdNVk4YOhDHy1FFB25PJsfkbObeWnDbXl78rsOlxPiSaWCwnlVOd-ykMTxqUUtIbfQvYlWPQbgQXPKwVZOIrj3eU1u9aGTHZXL1Vh8EBcbwXmIwGdhZFm2CcLjnTsO3lFLODUdjsnJCvRPonEl6jTLZrTbcVgIO_nxzy4T7VCZXnJR2Mbu0QelklGAvmPyfwSJqq_MPv0BN3aC10Df6uewNoVduuMI0EMKmstHeyhCGonIJe8ONUVs1M0qP9Lugtpsqm7_MJ6ci2zFAOTTexXC4jC6XrxZyKevY7X3t-_OpcNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4kJxlC-kZyFBE2H6Igab2r3dPqz-JpJIyWCZxYypG_We3Ggj5PGfVFKqWrIGTaHoePEDsJYpUdSQdR5Etu2J97xrYex_9UCBv7NIa8xK4_xoqFYIZPeYwXPqDl2I2NBLyHrasrfED3IINofEddxUAXdOivmtU9dCD8OpG5YAQxigmBmoIyybKx-M32kVQhXyWwLyRtFwBIaUy61ylA3pfeUI083hpeTCQT2nmDpRYPXUVRAvJSZ3EuuL6opIik_tOU7F1_U-sORoWBxLQQTQDQPm6TAYIqu2wOQ1tFodfIFf_Qg81HmMv5TrqmU0IgTHgeCsbDzjSA0W6YMX3gcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLRc3vqOD3C2SxGGF8N-Lo-46SCvZeu3Q2wI5oJsPgq8ba_StdW5nYbVagWTjfXnjh-RL1VdC0dfHzWeteWG8LWm9Unr-dR8xrnl7UQrnGEbNIJzEoxmXY4QHvl9ttnpcDcGbKUBXIALb0hFuTmIpZDlZRrEE7C_0zzzH9OMWLn0pSgUKVfoNIB1HLjhgjBS9MManst_RD6GujdqkgRAc3FsjcCaPJVInBp1AODm7gF3r-ytmMqQPOmlgBk4htCB4SOS3pd1JlrrRAEEUZaibxzWrgMyjqkbHYVe9V026WcaRKJI5-c1U5Iu38c-B5zYiz3hjJyn1I8M4QYGH_6BeQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Vw26lEp2rvoQJ6XHGiDbZuLQmTRV3b71U6rp23QwgFfpWlDhqpo9KEYWdTO1xWlZTR8OoLPCssLW5bsoCy8Awrqi0RZ-kmJZDPOvHeEfv2THOOGhRqRgJX11vArL8aRqikVNOmiPbBBhg8DgPzjKM3TyRTOzZRNr99xhnZ8StBpXJFH0XbvFIzXF0CYkJZZnk8nCAx_QCf8Mv2V1gtl_mXPdhwMg9DHJJGv2AcAdvew63-6u70I7WGsyj4wsLA9HbVLDf6sMrCaew76VJXUXyWkiIz5V0KJFpLiiZ9P_-q6IZP4-sWzbqJ9rc7WtZEZz_xh0C20BYw4H2FSHKXcyb7FJahOSekHAmtVxhctSE860I9OUnWwGB1GyeQHwxbMlGNuSabw1Gb2AHT85WvSyrOmpJK356M7VT0yag8VSHrKKjIzShC3Y3i-dn8jPNIEh2mADkvQJmOEiybI-fShpybEVqZ3jyRPETxsszv1_xrUHQH-7a6Qmvvof_PbqSDJM1A2VBpt6zhVZqBa5z7kKK15kPUNu6BAs6ZU9YXpg36o2l3PirDeSKOYER_82nIoSIvKo3LEBYRJsfoR_vi7z7qJTZxZWvqY2uiX5B7a0rDB7vXk-8TTWflQGiDTnWnQ7fniP4JG0B2tLBQbGqXR3zyiBFdwXmLI_0g3AQlIFRpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Vw26lEp2rvoQJ6XHGiDbZuLQmTRV3b71U6rp23QwgFfpWlDhqpo9KEYWdTO1xWlZTR8OoLPCssLW5bsoCy8Awrqi0RZ-kmJZDPOvHeEfv2THOOGhRqRgJX11vArL8aRqikVNOmiPbBBhg8DgPzjKM3TyRTOzZRNr99xhnZ8StBpXJFH0XbvFIzXF0CYkJZZnk8nCAx_QCf8Mv2V1gtl_mXPdhwMg9DHJJGv2AcAdvew63-6u70I7WGsyj4wsLA9HbVLDf6sMrCaew76VJXUXyWkiIz5V0KJFpLiiZ9P_-q6IZP4-sWzbqJ9rc7WtZEZz_xh0C20BYw4H2FSHKXcyb7FJahOSekHAmtVxhctSE860I9OUnWwGB1GyeQHwxbMlGNuSabw1Gb2AHT85WvSyrOmpJK356M7VT0yag8VSHrKKjIzShC3Y3i-dn8jPNIEh2mADkvQJmOEiybI-fShpybEVqZ3jyRPETxsszv1_xrUHQH-7a6Qmvvof_PbqSDJM1A2VBpt6zhVZqBa5z7kKK15kPUNu6BAs6ZU9YXpg36o2l3PirDeSKOYER_82nIoSIvKo3LEBYRJsfoR_vi7z7qJTZxZWvqY2uiX5B7a0rDB7vXk-8TTWflQGiDTnWnQ7fniP4JG0B2tLBQbGqXR3zyiBFdwXmLI_0g3AQlIFRpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq_gwtKASvTRc6LHR71AqmneHrB3W5va_-pTnkOTpU2btL4vpxgF7u9tvQwPJYM0x2mDt64V-uQVO6uk3w7QWPH5kfxk2VlfzZjXkqcjXzKt2_sl24xnm9pkmJCnS5wjOPh4LjUlgJeT9l6JDYEEzGmG6oRztS5B8sDnKeTVVOoDBxU0F78KxOS2H--p4VN7FQL7aTEjYwLEmfX8h8jX_ulsgLtZNBKO5k_vFNMDqIocFnG6MqxzQ8AnH5gVyhqcW5jrZKTsk0VpUCdMsASPH_zyH5mBS4rz2p5ok2IGti7LEsLOsSrHTT-R7d-dPnTv_wlCBaXv3_ACoZHnwOJAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2GbYwvxiOfSu_XGa4mX1F3FGPTToATi1ZYmmy6M8V3_hwtxmj8nZXWlq5m-idSwCcsNLM0pkaeIs_5rMaYS3a9kP08RxVQSnozdEj9tNwZ-2NpTS8IMtsJSbe0zWEt2Ag5z1UWzgVv4YUaWW7Oky0nv-iT5pvNlCLfDajwU8FetGFGxOWCDGgCB6EOL__GzcKO0QZwUM_ua31VjnTLGHxLw-_vbn91c6EZ_ZV6I5GniUMJRM8N6EjzaF-FhJJXPBuoK46jMRtU9OfTgroHUkUuTqTRLzvXhPxH_hbQ-04sYpeeOxjt7rR6-sydAqFutx9d2bO_sBH6ptJU7ggMqEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDpEPyA82TRvxKrPsjvDnhU-XBBzw3tZswE_yEjtdwDLvMDTbD7qj2q-ooZ7xMeskl3LPmSn1zq0jpCFphdh80p93G7_m0MWFMS65EkMupZsYmIYtFFkmYqRyAInVSXiNE9zxHDwLGnxDmURDO6jINv7c9n_qisxpjnOyBgyCTkyoOHLA4RgI_iU4SPXj4NWrGALgm7x1xE7_1v7QM6jD_n8jnAKIKji-3MpSYaunyz_2OkS2BZp_wPxLk3e8rdyFbySMv8-cgz1UXvFq_JJjXCrMDlyt17EDnXYm9qUV6OXdiuJt2oCKraxxt-pjej5WJ6ux3O8ChlWZYhrs6r5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5m1Yo0eV8-2Rjp2PWMNqlSBk5_u4FWazJE3nfSb5TQvl35_D3NNIiYo5utmqX3W3FbyBeUB0-JJ6SeNC6aLf_197LFGdiGI7YhEhLgXjSjYABvchLXboGrWxOFanQTNIpu6zIStxiYESnVdE_-oxeecf2T2unblOCwGtD9lGNlY0ih6sRq58A3PyxQYS2lhrRRzWeg-UTYpGsF3ktbxMwssbxCHNWRYTm2AIehowwDs-ePkiknE_htnu9XWvcSg2V1Ig8Ezvwboi2N4rQdDwt0oplNBZqlmiBaMnFkdTu9ZuE6JaWIbyEoM9teUKHxJXGuVq7nLrMcoImlnry6sVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rswi8pBFdgfEkKSISeqX2zQbzGBGY12Sv8jDe9LSiQfNcvwgLhEgII21iTkDIq9N2IWnvxNPWkCcnoOFAkRQO9pNu4uI2XRF5NTXjNizxwv7_UgVJnd7-CHxZ5PBJTv7LDTTxR1WXDAmk2q_q5arlXK9eBOoDKqSWyUzc7zVqO0kriaDRB_yBTAxG0FwH07mkKmGCPu29Vo5edq4nqeEck--nDytT4KIreGnZIu-eRbqhL5nwUbOs5YWqhfR4gCFUN-xxoVFvvtr-kG7tLFYnGHJ7rm3GHQpbRzCiofF0uGjq3yMVChETmkvmFQrzi6r84lbTDgGGhZhx56OOj3XDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Rk7_BgKithrQ09_1yoyyoJh0bc82Ho-W6UeoGLWTEMUYo9xwq8uDq0G9tTSAggyV-w1YFt_WE2vvH5Pd9CaT4A16WxphfP1nE96IBG4Q4aoWlUYvKLOxoeVO9Z9mhPBivK2pGlNgQi6AKHOpsYOWQZGjXHLLjN1ph5BynvVs7QRaylXfD3bFM4KX3Xsdz2AV6yPifxOW9kFMT_zWee2RXN6zekcdGktLi8RQHzT5OJ-OADRNgdwsxxEEhod4OdMqjyDstbYEmDwS3fTExBn_MlVHuNxnicB4zQadpNryidsVP3u0QRusFu7iiCVHyna8IiK4xwDDFCFRIris-PY5FI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Rk7_BgKithrQ09_1yoyyoJh0bc82Ho-W6UeoGLWTEMUYo9xwq8uDq0G9tTSAggyV-w1YFt_WE2vvH5Pd9CaT4A16WxphfP1nE96IBG4Q4aoWlUYvKLOxoeVO9Z9mhPBivK2pGlNgQi6AKHOpsYOWQZGjXHLLjN1ph5BynvVs7QRaylXfD3bFM4KX3Xsdz2AV6yPifxOW9kFMT_zWee2RXN6zekcdGktLi8RQHzT5OJ-OADRNgdwsxxEEhod4OdMqjyDstbYEmDwS3fTExBn_MlVHuNxnicB4zQadpNryidsVP3u0QRusFu7iiCVHyna8IiK4xwDDFCFRIris-PY5FI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMtmHjj-RLNP4UfxHoKzN1gVRK6_dC8nHkvgOmESazBaPrwolcxmdQi1TV2s8fLUmTpM_Wn6Ky66EYJGDE53Ju71BI_bYp0clnyR5RaiMpt_r6ZSNmPyaAF9FSvduhMdtkc4v_GQotI4rwzZzP9LM96jDVc8FBsLTYoXGFLCMRnyy1tKP_fPZ9bZR6ccDb-OmeU8EZlGmzBkXEsZcg-Xzcm0CLdcR7OA_SPkzHv6ZgVoi-4dkXUsAl_zlaEPL7MNJ8Hq13cLVaLNqj-LTQ58vxc2QenTU7WYfG20e349Z-R6xa5uvRL1akGx8q1sTeh_SKVSiZ_uw19JuHJUqqS66Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFrKkjOHmj0ytlWLxBQ9JD240uFwvgshAwxVQrRVYtl00jyp6ESEk20RyhvZnh_X6pPFId8sF3i0Vq-ppzxsaoWPZTlTW5EeNAUqAJAZ_gGGsHdUyW-R2zk--FR6VWwqUy3JsOVB5jJsKM54k_kfxowXOwSKnIMgRHb52Mwj7fZ6fWk5ii-DWLdOo0t5ZfKz7xiPJSxrv896Aj4YQAI-YUK0U4azOU1AnfYkq0W95EcIDK4cQ1TDrgPLdllyiY53arf6mOBE4D81xnD1D6WTue4RWHZnsuz2GBPVQnvg5S2FbL1xTAVS_bvodkj-lKaxxQ5IRtfaMetd5iogmoUMxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DToGYjuQTF8fGq-yVRH7lHrwD9W0UxZIC_hhnG3m09NEKuO2kOGFHUq-zxvBmMtVqvMpyTxf4CzVzgsOptS9AlF8oiaFQJMhFwrXD2MxpwqfaLzoEK7uvfKvI3E4dwmoJOf1GRBWS0FDOC9iYYibdDVphroU9CtjQ19d40DGGxlXMMtISBtFCJN_cm09jHZwjUQLVTyEGgixTGYAsX_YYy8bckYISR34DRgmqPlOOTbbVUmhCQuK1ycRc1NmFRGeKb_MLioZ6Fdx-jojnqDKZx5Yurr2Ks6HmrLeeHw0hzUagSJXmxVrG7p1tAZwexUxEJNZ-bXtG_ExodElE8KgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoKrdMU4PNRiFCuQWgug9JjUIuUJc6lz-qX7Ahvit1c_GljGuAlY2kEb9J2eBWxeH22ea-wQ76bJfUcRsTRq3WcCRxnWKSgA1UNym_ELvt9VLm143bxvKSmq8PzUFGtweWE5ytUo_kf8Qmef7FJlRBOq3AXP02_ELMLyooUvrn9ZaA7OtHMqjJRCnlu_OUbtYgM19eafsEd3LpwRJ3k0BYboqLCJrBil7_cjGoK3Rbtekvs8qQs42D4tqaXJ0wzSYlFqcO71tsPm-evTLHm2OQYkGT8epQRZoYwsTpf4ycj0bilnEDHWApGKF6hRr-SEj3-Ocyqf7rlGK30Gt-nNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_cLAWGDmxFwxC4f2Vg6rTojzGbqwETpgCj6XDJNVGKIF_RobG8wRNaedghDdNjfrnnh6f0_7PP7LmNE3TVi6nDWVhCKtADebYRihRYYcG0P9nJna7uTGySRKQd1dO9tU8p0iEcpqn2UYYDRA-cfQtzL8sG2czydNrhTQplvSDtQmx1HsID7KiU4Fs8evdwO6Ke0JDPyJZgMYnGNiYcMDp2wjZH8atXO34iRwueADqafb7Y9nuqy2d5La9Jv0DU21jBdjLFS8sNLLYNZOaTRf6p_SkyiavVElyfFCnj08Neca6nZJVpO745EWbUPd7w0ZQNwLBaPG9otWd-z31OUfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq19b9et66mimX56ZzOvRB8AxeO8_PSOveP-OxwJx4_rdH-UStFZcRckeK28manjzg4H9DVfG8WJALg3Qri7f81f_lEbEFmmsZGcScOZ56Way4C6DZwkLFQRRgbRb8GbN_mTjMy4f8OscnNEw1bo54VEQXhY9qgI4F_6ezmUOcthXKOl6w4-12cBkQQ7-TemrhM76XX-XLZQAaOjGVdA-3cpWZBe_XOitmWSE7MsEiwI0819wp4QD--l4AFnfbt9zErk-AMvXheIyrzNWMRTLRS8n-gfNmjgadw0mltipR2a9Q2KXr62FLA9lP5C-7d6CiDWbOR9x7AcQhEY7W8p6Q.jpg" alt="photo" loading="lazy"/></div>
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
