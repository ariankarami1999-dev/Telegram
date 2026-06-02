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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 08:37:57</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 324 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 487 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 592 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEGj1W6aim5Gn-y3O9pmwsGJXKv2sXtYdXJx8MUIEe3uiG41sZ9EfWnVCRks7B4ybhVfQye1b7HS1uYSisJ1AZ9ZlUEhuq7S7JFbrrOb60yePAdHd0E2MXRSpk_D8s5G9M50kVpiWpfi17NBzOjApkN3yO5pNc6Ug47QAO3TRcKtDUaUyFPgQ_96RdY_RkAFmgxvEjaC8sei3V00e-46Y4alUDQzES6Ky1j2E6G1ypTzO5c8l-kfft7lJX_3vaKx7pfhiOxjRK5dfNy_6aDVh7zXt7Bx9CptK0VfBBnDMvTQrmy2RtB6HswU45WfgKQJZ98Y_wGeb2oOy4grOTEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Cdy7p45aknlPpI8TYDwZMO2NDcFSzN8t-MWaA8zjGprP8oOoB520wnaTmiv9RkrMATMHSZn2iF2F9hHGbCmF1YCHbTJ3ZaGL-lzncbUzIaRAsvA4p9_ELXlLP1l7mMbnYuQX7j_1ND7Hiob3yighJVuhHlpNkrfKk91cIWncAD06ahrWCym9DmS-1aPY2RFIYCbEuRwbSELF4UmiG-7n8WTn1eg1NmaGe_NH5SRhqcfccipZAQU6QgI6coJFCZKT0SXH8QRepq-CNJsg4uXxeKX3ssmOLT7O0G_MUkhg9KmlTSMcqfF6MMAHofslAXtmcJtpBVbVrHYV8Hxtx5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0I1GR7UgADJfvKHje9HMX3GgdHKL4ISOHx0PzXb4H0l4eAV5k1bJ01g7qfWxd4vIuQBYcK1Rx6G8zdXxxi56q3Rux3VDNAD_s0SEk9HjnCnZQMqywF9lushQ1zXizGCqZmoDLCFAPNr49mfnKK3A37R8MgVV6sPWXQ4Ufb5jIViOpnuliUFbS7ltV7NXdV0kp12H5CJ4XcLR2wtXNUgUlbxtdqc2WqV0D6WZPXOJEW3MQfvkb0LJQCELix1VljA7u5TtuSiluijAeltYiCpiP_MESs_w1xPxOfQSsdj9mRv6PxGj55kV4IuCIoCTuqstWY03_MH-hVzZm-nVzD0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8sJP2tajyoddg5PhZVZOyAXCFrMoBNfDz2ke7lLk9jF-4Ehsq09HCd-RkZO9FmbZW3w4U9odt4u1j8h39Zz0IDH-EfYLmb4wtvXzqrwovwN5GmR0bPrrnYfwgMfCu_ztQL7kK7Q-luZuBeilsexTwKLzxIFTtOwGPLpq6fsJhWFU5Kh-VIxeLB9AED9YfNrrcebRwHyqC-efRxqDrXc3Vkv6T56vki-5m_oCjw6TUl2yY5O_AoX6aAh1TnLdw1LzK5v_KoXq2lUt7rrQVpovQmbbmyEMIEdL_UuH4SIAfwK_JMGrAW-LaHLdz0jN25KhCT4OWXs3zYLewcVkyy31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Ta7JCpLBiRhSbmv8ya09YoIW_kPooi7l8j5L1P19894w3th58y8vAnsGDHmRKqYmh5ke3Y17ABEP3eDO-oGDzbc65uU87jNpXcMdV34gfn0VnY3OX484GFtEkjKxVvhq4ddWsp77AG3Ro1SD3RGnhafjeDXO3guVg_f677ErROqksSuiCDbM745WCUz_9nj6C6OjULCfOHaM4Ls3L-fCn_N3cxTx38HxzrAs21_FNxlicXG8gX39-iX7uSoHd8r5i-mvEukOni3xwHTUhFziFRV_9xbgfiD6r0dafoiMWv-C6uSMNmJ4yxcu9nbtf5dSdEA-CONwdODUM8WSXz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFy8-BApLb4Et4uiW6T53Mpz0-XkM_gXOHp4m53Q4RhfCvb55lyK0emWup-E2rNRxtPBahEh3ahXN6TqeqjFyFZml--3-GftZSQKt8dAkwLClZJZa6VDdBfNhTeocCiFSPRt9Dn3V3I67LuswyoKI4deLm7e6kQd3s4M3zTdGDEqqidTTwjP1lhHG_GVf1R0BfRzjvUHi8FnTD_ZX8mCPOm7VL9HsQQ9k8gpR4BL5BxL5WrZW3vkiIA9LXnvhb4XCanna3XaLDBfEr8yEONZ1smg2ZorhqwuP_WqngU-d0B4iUsacRfupoWFECgHS_UnlvtItIOVJmDzxELB709IbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkENhETe7Lu4jknpc8ATCK-mQ4tgi7Su1CuMfjOEWBCb5WMmhS2A10-fqccZT34PFySyw9CWrL6Osw9JAzbhUR7JdZn0OgJxpsa7Aq5xHQuUf_seE2c9MtNaazwGj3sxjO1vaghtGPCApAYY2yW_la7RAn55x49OrC-L_RdUHTH00mSyhxkxdv7xbbsUlsT0jZDpyEkFPc8h9GvvJoIOsRgcplV6nQUS-vtnhAYzwBzklZHN5dYm_dF5Baqyw5IN72yFhx8T93Y4eQ_kQRkElgFkgOA3HnY6oBrbwbKiAwJxbmCImz_KqDVEY9JWDnSlfiP92JXyxYsr7yFf9YDAEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-v9IKaCe0PLwINoIsUrx6nxjL4A3jX7XDeuGytgiuUJiFPl09jQZjjlTOLLjWjZ5czZa5orTEs1fdV3Qwlw6CQ6EePMHhJedUp96fxv5mXr7k6gJx2ICNKVyb8yTyVtwOVWrHsACFO-ZIlrWTXa2Crpv_MNb68I6G3MKEnljMy4gj8RUyF74Wu9_PPr2ZQK88IXvnTUZmnCzeeXURuAk_ISzVR4QWex4ANtcns-58-qCV0HcTiKRlptkxS8I-ccII6peYxjXY4KxDEfMtbw5ehFfk_EpQP6vYFZfupM6xkMd-FqiK8rpVC9IKNITsCwe8CHD5EzdNlzRAGMjrAL3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INqqiAIQRZkyVR0eyQMu98InyQaKQDdIVWEc0w4db2Dlol0mZCCnv242BDPLWI5imhhSIPtrmLA6juK0nFgDiBPxL6gWwrwAVLoSc8P0EEZfi6pvxusckO4L3RnGTegJTtDx_CDfwit9nUr0CBbgOyIq0xR4LN4WS5u02c-OaMCA1StwgbjQvZGzYfmMhs5ddKnMhmIQONXaXa4jHr7gwVPi27OPqpUOJNXp7dsd9bNzmO0S98J2PRhL3SNQC1CQvw0L3Myi7Gak36qZvStFaQczw9VKytgJRB5P-Tk2dU6Z4GHBPS0Fa8e9Wk5pdTZ7vMaXhXt8EXLHviGm6FUlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ps9w4tDh0UIICi85Pw6QIyFb0NWSl3u2Q817V5u4PHt2ncUMrk0AvQCS3wAN15P8BvAilC2UFyJevdBtSOBfOphI-SFTgTYi_c1vzMGpM0k0AiV3e5rSwV9H04kMhhADvhlnugu19TFo9_YAWbpDcCrbJAxeTF8pdIRgqQVDZw-8E0jF5EOkac6vvHkmcHRPKsid4nJZ8Sc0qCzowbHpGg1mklWL2EiE-bW35c8RmdVQIcQdbwgMWphn0wLvWPGDw6LgCDxBB_DXCSAlyJcfPmRvZTXSRrjDGQJDMPj_ylVHXNeYW1BEARQ8Tqf1-i4WtMnpb87U7aYT1XKEs6dD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHbopv5j_pjLBJC5QYuDcKmZ8aBvegUyVPjSy3_y5SKLl6LMEiSiELiGtOGuQN0TFwcCGahIf9YcVMSioPWELol31xK4o1D6OhaGlJlr6goDiQtP-_0K9MsI1cg4wsIHSTui5nZXsW3MhXP7IzittqT9mpB5z81K5j-7JZkNt5KFpYpAMuKbSWk93Bcxg6PGgv0IaIxnTonvi5-z-nvR3oHU6W-znuEr-5BZa0uWoGR7IUgD0FIvH2MDhK9rD6kByllfsmASxc5cPD94Lvk8Ilxivgyfo8007Tht2Gj7LEb1HNHtVXd6JK2v52MaV4urau_YgpSYjSCQT6L4D_1_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9pJ3vDc4XQ1V_BYQvsw7BrQTTPX6JviVGN1F3EZnykcdoiFv5T6vMKjK44dU3QW-FjBsG6FMA7L35J9UefbDZpc2TbxC8HZoxf8xpTlNJCSrhmTZ6oStJtYuxAAM-hdzdP-7oNH5vmDlETk2_j_BGWvpZSNQMD9rEuOcuFEVghnqpopMYyZxc2dIa1tSTqla2blEhEtoGqkeSP5LhPW1ly-z50x4F1ziKjC0JX6kvVNjOZnNRKSPy0RMgbgU-BEYD210Obh6hM2U7lcIu3geeLRH5ACXk3l6196npQx8rhBEu8ZAUv8UgHET8UuNCkzip8pOaJBj32VzCnPWtjuZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHHSTJw3wfmdU_QE6ZJgM4zBpHCtrPBvmuuQjn6C77AEka6Fw0b9MhMr7rHMV0gg4P5MI_wLrizb0OXP-k_-iqpL9AhtVkq1nVuWZNU2NUwbsZEvVaMaC5miQ0HPeVwKCK75DQM_b2iBZsaEoA3gGlIAtlM_cG1HWNnEBa__NqJtqcCiC6LgZorG_744vUd31eL6KDQtYjYpluv_8PiVzDjBc3un4tmfPjKEKe3Tlsm4xdK24GQFoZXCBEmhEMai9mWWKnwg4GWnU0pn_tn955vefNG8Yy83fEZ80otFvy7FAi4q-MrSdQtcNbLCfwUzd6aGgteIeDkVqvJeFaYsXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=PdYzsEk2q-lW9645iBGK4DoDU1r7EqG50a8mmnGBaoxbmpwxYGM_PdOugdIVSc-w3zY3UPEPU1M53PoMaFG1ksO5ZoqFd8g6Pdq95pck6rwBrn4BAbVwJh1DW5NucFDNUEux6WwaF4KwwhqQV2LJ_iiRVhI34MdSnTpyQuhGB0aJXweC5jL_H5qLqDXBb5pV90N9k7BRTBGknlsHmE3o9iwkLemmcpYC73OOxTomf2zFLDjEr5xf7syTXUOuGqw_y_n7RV6SQFGO4ZcsrLoQPxQSjxM61pj5eVr34AN8Q2C9YSk_uNbSj2IZQKWYimDabwfTg8XyfMyEQcdkWYZZtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=PdYzsEk2q-lW9645iBGK4DoDU1r7EqG50a8mmnGBaoxbmpwxYGM_PdOugdIVSc-w3zY3UPEPU1M53PoMaFG1ksO5ZoqFd8g6Pdq95pck6rwBrn4BAbVwJh1DW5NucFDNUEux6WwaF4KwwhqQV2LJ_iiRVhI34MdSnTpyQuhGB0aJXweC5jL_H5qLqDXBb5pV90N9k7BRTBGknlsHmE3o9iwkLemmcpYC73OOxTomf2zFLDjEr5xf7syTXUOuGqw_y_n7RV6SQFGO4ZcsrLoQPxQSjxM61pj5eVr34AN8Q2C9YSk_uNbSj2IZQKWYimDabwfTg8XyfMyEQcdkWYZZtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEqa9tm-yCSuvk_rZ4VT73IBK8frbgx6dmv1fTFzImgPB0ygBGqyvszBy6Y6XYokU0vCwwkko3df8N0Yql3opnYYEmfYQo8ezJoDo3A_BBhc_ZYDYZjjyS0ivtvl5hFdNERewb5KRx6BPdwHxRz_lZmwUTwQrL78KdAThW4iX_GPqG9QmaxBjbkUdchoIv2uThg4ccBBdcwP3jMtYXUNaRIV87vyxnRk3Aqk9-kQhqC9_gV6gLb9lMeqKU1zIU9uHdpxHi3U7j7-czhw4foXs1cDdXKKxk99f2_2izD6RaMs2fYKaNyrrszxgZIPQc_2Pfi-9U1h1CoUk4wgWJWmlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSoUVa75nf9FGE6gXc0PZYUGaLkAj_dzGX1ZYSzA6syqaSUi9Xdq-2eO45JPEbSNfBjLH-aFQLXSwrK_zi0v3hYtxNp1aZWHoMj_Ng3MLUzCKz3qG0O32qFZwjk9wlgjroKUZCaEZ7z9G3YdiAs7_Lw0N-hrAKUuFi7iAlVZowxhOh87U36VSBziN4Dyv2m-y3DHGS_zKlT45ZBaciGWe8JSOFS5kaMZbJlQmI93zwQExr26PnTOfg48ooqzoLjthKM7imbT2OWBPJgHpgaR-aDpaaYFmtqpkiQ0AYmxlxxpZqGGf46B2hya9PXPuYRUx_V35N8BEqDj1mMOqlTdsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIPlEVNVhI6uQLnHwVe6dMU1QXBv50YIjsmBiaKrqYieTDnFK1eom3kAxj0x2wDgMXrew4wJlHQuddU9Ms_nIE3h2WQO_aD5-UD8Qdp-NmMcUpuZX0zPEseMZP-8ntBCWdlYmYXVVRirVtThXWreaiSqcv1mZcaHZd9fo6bfEYoKSxv-TPIfrZQWkUo2ERqNw7eQVzZZ9I6ZpNdcwoT7i7RTIhOs2y8TGGLgaiZW6kDWKpI3C1T27eQl0RoRnYBZ3TrxBj5EG7pGENXuY8etDku4Uu4Sc5IVHcQ2VhV1XrN3YQrw0LivJo1r6u6tR2pr85lemgFFqeykOKMwqA-cVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-P-jk76WpPJL_qO-yj0aUKQN3qjtLCAoGKwuBHLw_pmml8Utqn0-8_4reE4XoaKF2gCkfRqOD-bhvMW9AWQMcCSmdM2W_eIKIOSdic_MwkhF3dJD4B6p7DVPIn2L0B2Fv4JyZtIR3VX-lvxagQICCIIgZWiwC9P082n-lIb68ZpQ-eG6zIfRt9_EV9MK2KOPTktqSxLIIt4V3S-I2OAQ-q8J5zQgUTdI40Dyx_QfBGp_o6U-XpgMdRWqz7OF68SnuekdMupI3NQAOj4LZICkPNDbCz908heYK_uTBEMuRiMa4OeVeNbjjD-s7_buUgTlMtjzzhHZY7P5acFIpdtEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePu_rFtmOTPTEInYeFIrMTCGAOAeOISE0WNaMPkbk4gauNUwLbiUpZsaepKjEO2UvX8YtzT5ettZMMp8kAeEs4-TQoZckSdfqUCycfaLPdeROrBe0PqCTRosx0m20IMTGVptn2xJv2YSu8oR4Mkw7uzHsyBE1Yv5kwXuYMtaHZvvWuvV9XIkF--gUeGGmn97W4Da-EPN87nqDrjsD1J0Y3zwqieR3nqDn8vAl2me5hLJ0VdMzZq7YyfTX5y-5EHdeOAK29N1gEuv0UA6kUQ5h1qVeRPCtq_gkylg989KRf-STgfKElmPpddpE5-1ZFNcqEQvEx-d1jI3lrDlaobLvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHzbpC-PaZTe-jWvhxSVgltG0AK1qZYMn9M_KDUtQzm7qtx9mvgMngN0hFOxxNxpoeQ9ZdCwEtL5_y34thO29jzb5srvtaRigSkyanMLAf1NhjXw9kiHiTr4MEXl72WxXDmuRhgZTlDoTVL4p9a3t1ABGpzEAsJ77eTqc85oqBvpqvrLAQsjiQU56tKirrYaEUY864oKVYza1546laIzHANLolcRJCFm5SfhrIJwvtZtRACFIYs9cCWl0WeE2Pgt1D_843LAo18vgR36A_K_6CmCksjp2eWop9Hm4uVThmMqJ9_8KxImn5zOfKVeDuMCNq0adHBwyzY_UTpmLElnDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYzwPl11gpgNWK-rXnqMR7BIWj1AyFdgYxCQN15T321qIUPDaVfa2W320QpzSyT9skVW7zBXU1tnVvuBleKYHO2cnAtIjfU7X6b6YjRsgN6k_hp01OQxTL-4XaKIlO8dXM2msCqp0W4FMcqM6J0L2fVa5XuQYR0p24L5keIYfH_DuJXsONa6YhZm0jeJLoSnoNCpMkHz5mPrB59BCnFezMHINPNQx7iM4mKwnxjQi4dcjyQJaYnXzPN1e51haBnXJosujdS3XEFN5j8LBcEIUPlymJxJVUkfrfm5C_Dmit6vPG2frcK4ZzGlT9TiBRAdxuYxVQkJHzRr2MW1tWhRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjTDjRe5xQIo4xaI3v98p_T1dVB7cSJv7yc9EyQUa2hbNpIlK96vwHugAAh2gnImk-Zh2UZfAvoY2MVuCUCQRur3qsoaIjrpUCSlqVcyeZRr-b3yhIX9d6vZ428I3TQX5DROb0cjufODkmUFGxwao4GvjSSubdyRIp88gs32nFBsuP_4NJ1kzaCmjoKBrNeFbEPsHnNrnGECSjWJdAy8_cLY1HNBlLQPjSPUQt7ekz2RPVG4WF-TuukvruGGOFx3haLOujt_XWKI5XPA5oMKmwNRQTRj7T7dvp6zA24brjCmxiZ2w6RqY4efs_CLNvEEuqAWmuDxQKKFZPJ7erxv9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL8fYo5nNq6aSIPVSfPfP7qe6WbVd4-qOl3_p63Zdox2Q9IPzhcRI8kzgZS14p6DTQt9X2t8inUzPkfeWb5WRV3eaWijBrjsASAeB5IK_cXM1WG5fhbrg2VZ-RbbV10MHlXs5Qztd4P83jGNkYj8Rnqf6Y6y73lBoCzesPvMsRlIRsYANiwQ6lXlNqUA3CDk4EK7sbyFy1979TgfqFWR8VjvN5IX_XaRMbcJsD4eoedW2lK8jOH65qMl9FwoP5N91uqrSwdhCADWV3W1j-ATALVqE6vtsSDzypALm8wzPxzMwYvbiQAxFEIYiWbIbYSivOqmW1qHRSjzj99JVkdAEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlnCjGL0BKwyIVW2J83wsBNUeZkH4wtj0cBLUWSblL2AQbeMY6sW3AP6XTu8rgYErF6tcTfxNuq-ZYTS2qWQNxt9sfUOezPix7DMzGwNe34dOCAgHlQVBHt6NIHQKcu2bHzDQnqTruvH4FQoOD2a3Z9Xkkw4Sw5QfBGfE-S7RXlBO3s-Jw4f6VpySE3kX4ylWhRaiSXVF4LjjsjGF_N1da8J0GGpwc-hEJMziNiDOhpECetrgbZ764O3Q-cwj6zG1Q6fkt5ABiP47N5-pMyxvGhxznvy_7Yi64dAQjGqKwVddrzYoWp5HirjH7ImtAyI1VFLkOpgP6bGClkJuqYcVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLj6lS2_z2tYdIX2LLZlc2nhe1dDO8J9KeyFkub5KpeecWZ_enrUma-PeOC0HSeazoI74yHcY9jN3HWj-iqC2SPCCSRGNNHGvfNhIHF-Wnf7OnXoFF37TA5znEXXiOIMT8ITmJrZOJhNeBZVXDxEh26mo4mQzfWuBciN_Qkgq8_WrJgl_1xc1Bse2zFySgZtmxMmv0SA1FAHd0bX83ZOEfNsTkQapneOpsQ4K_aQ9rfm4-Y5iMq5jYzslMn2d_O7EbAWkHNikh4ynKk5h17n3hTWwZgpbCA6Kx3bYSWmbyPTE2i2dVX1CPH5SarzxPVYagRqGu7tBolBouqALJTLjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C00Vkkpx2D-X9oH6W7zm6CkNnheI2QRsR0FfiuEAK5TOrdH6_CZH62xd7Bug3XChi6d5YNhconTGZG9IZKABZ8A2W8Op5rPYOs6JCv-6JQ9p_p93YSejmLtB31_WJqpMZQNkXv9p4CWRIFu6uz6UftaqT3TWyyXyekjTvkqnKYfoLAwDIypJ7jFxFQnN2zVNmmWwJuXP9Da3PbIB3HcLZdzTuY4ygVHMx1tTek7Kyo7Lntx7jwBvORqzqSqaxTzzu928qkAvR6NfDQP-aHZ3mrX1Hv5GLsa9vW-lz2xicFXO0I6T5f-Iv9u7yUNdlcmSQ4c0EIxxyK9qdkL4isJGhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ch9DJlQdkwu1BC21FmCx-Cfv70eAIGnH_cOcjF_x-8Moq0CERwcO494o8rteKi-Ue1Hq4FYvw4VO_Gi2P9wGjulN92OI0RbzLO9MhEYW7IWMh8BbIEvMvB-fn0chRbh1YJWXjRrFv3v73RKIABFKb8BV0ieWNu1XhOLh3p9y54hwx-SwYvqoO00PcPxnLmG7PhbdhTaPgFrZsaDQ2YucbpfxsFu11Lvt9WQn_c5dAoWqHkavVBNgo7H3jzuYHrrWDy3R4KVPuq92cD7KRcWVjexe0t8JeTh1gM5Jk_WvQ8BuWhLzczPHjoWklb_Cw0iqIuX6a1dd91QWGcZbi_lnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WB2eExMHNJaB9K09mDmeON2P7maZ9OGwtHTdLG7fKMTdsC0d9LnvbsG4io7aO9nUNnjl-KM2Yu-Uh3_GdrEcfi0ESqIp17F-iejs7ao0fYwrTncCyCXzhbpl--XjBZP9xct7ty_0qgJWI6X0qKLbftTFOP6TC0jbdlC7ZGTxRWzwN6c9AMjYm56s2RnSaRU72VaBfLsCVuqoK7iNcUOer_qMFGcxtaP_13Dct29Uj3blbqExMfxV2MCQTz9_ka3HhbzkNy-s4YWKzL2ft2z596NhhYL9Jel7tC_GWf-VGIhrZNRIwdWv779-POwdrbgDJZyIwRIF-289XZ_qn8WE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuWnXPHaMBCVP5-RGlYsfAMtvU3G3A4r-Tl-0-3jRf_bLFqt-jBexfU4dg_tNoLYIQMLT9t0oyDm4oVAZeysfWWk-8wkTC0RDaflUR1tlNRGWbGtNqi383HcKQNNHb-LWE5l9TX0hFc5TXinKKfTshryWfAIexvCwh48tpz84RRX6GluzhXaSou71g3ny9OjL1axwIOnEPXNytmgu_wFLN_d_jLETEj1mKNtBv78hLRZ4J7N5JAzlMHbJRn8UeWp0sKeuZ_ItnjO431vUaGKAPPM0d5OHgsfRTMfd9NXs4x2ns2pd7BAe3vddEh9N6K1UvKKvtl1ouql8_Z-2xZjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeXEOrrOcWd13LAQmpXHAvfyHeEuasFGYjw5201CpY8ae8QuERvlnN2-IB09bK1fc8jHgxVVxnE1m_MVMzjNt5EMxBCpRep4Z5WWGGOnKAgvGO-IB3gFK-2watexYx8ssQTRrJk0EO5exiDZTj1pXFOaHCR0RC7iFUm5flM1jxGdNHcemcOax1Jhsphl1F_rHOfTzsVezkrfZza9RFC9hjMkFQOU_mW4HJsQ7VZ0ouvk9qzzN_BnLsUMCiy4f3y7DqRZM0PwXFxudAfbel-y5BFefHIcqbzAXoLBq5Qb1RZXfKHufc2oPW2gMx4pxscoID3t1XE61HSfoUEzPotBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVASUavnKIJdTEMFRJL6xf0FVzy02FGlzBk-8sGNo2_7PXFreWGcx6-smXCrqS-AcRuZV0wctraTOt9tdrLxponTPLsdJ1AXJJHyZ9YChcm-4AUsM1KvMzRYCoT1UzKc5jADiX9g8lUfidaH3nxR_QVSYLFuqnodzQFwYL2akahi4t4M3uPAuEQocKQc-tLqUE05nQzBFxgtgOLdXZ4FdT1RoCRIMJ0w4_3jD_KOzVvpjBbRRZ3BEQY6D-mMGtGSO4BKeviWNOUkNkCbz69ySTi9k75H1FMVnqPC15sxpdjtoPg7ovRO0JTYZ0k7WHYe3TPvL6EtiUQ6dwDz5PRIkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTqvJfyfmQj-Pr-7_3v4HanbpfPalFZs1ydYX9aIWUcLPlOLNJrVrnBfCd5GY4d1sU9W1HQEUxAxsAXJBnW8O_w6nDHrbuLqvlt9vJCd-jxQzjLVv8ibhEOiLmp35T0fkWiqmwng-cO_tBilscAOM00Eqv1Ujjo7QQFUy57COPDoXfoODdmR2uXywXLH0uAA2fJayUa_sTEheEA16MZAS6XeaSpxzRdiY0eYmV3I7YMtIEDhbAukTlQ65LpriKJIejA1CTWgWIWFDdPTri79glcyl-OCiSU9ZHo_Xh-HApHAkF3D2YSP0aQ1t4IsKgs9LBvBPmBuHQF8mPYyFcC81g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnMbA1d49Yi4ziNF5C6ph-McPVSa1IcvhovRx14QOOz2SJbGh-2vIkf7IK8zTSEyoymSjdSAgp4mB77-wADrutY4UB5VqJ_4TOiBBu4VWLr416HOQ4tXM5vmhLefJ2o5bwyDWT71m_2Kwg1sANqcJlZMWwzWVUkdY8JiEji2cR49rQvqT6ETTM7kEX7xvl3Twyg9GQGDAADJAhIT98r6KkAhmVxBOuC4yVb1P-iAwLlDn7DXZvfaNzWQnDn8y6aH0-mJTx1dq4SjH8yoF902Q4gDEJz5wmiV4VVAR7vzKiRaKXo68_y16WKb0H-wP5VFb6Zu2Qz1Hi2Db1kzuHsbsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJxd1kM6eN0GQD3wE6wQk3w6roNkBKVJ4nYokJ2B4VH89mO2my19oN72DPwpTbb996nguiGq2nVyjpLmpIBw9Mivhu-KCVqtMZY7f2F7mRQaIk3-VQucCTe8wlSq_y9UQPmIVqiySaET_xLIrH7oyCAR2DQfdeDGNmGB5NqGn4Eqj_dQKo72kaPIPhJuXoB-pQJ0iyjojJBQ_JUhFpkWq5Zfny4ombZb25GN5-3Br2mo21bbhebny2c2yFoj8X5NxoNiWTm3FGd5IKQ16y-8yr1MdhweZ1-8r-YnVcmKv0mGhAgu3cnM1RWO62UTUHbB20omk6cmg0Oe-jBdqiF1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCenlGTisafEvTFFLEQ4yq98_xx4Rx3-boC1bfZ1mxk38WXqbYtzl4FwJoNYkzLvNgtXCg-nlcrJ0g0iKgFeZvh9e6PK40vVvmnxY-6uTRhzC_3QJgfPE3OGk_L9u_orWRKv9uZDa06gLIskp-BMkaLV4m6uYAAn-27l_XTTW-eaoGszhmqQOWbpJdElef42WddUN0duAth0xWX6Vmmcugd7FPWD611rBd5pQciU7dOlmIyAyIQM_pRBdY3Lh2gZC81sTYL-3gvBDuSoqybwbrBORJD1LW3Ah_wDIMkKJDwbvRrTf9FREDVcUP-n9RoK8WSlt7JbXOdaDkRYnBQTpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad_p5MgaYF5enQwUbQ0uY7iHZyw2gmXAQKQSuadfbclGXkMyS0AVuQPfvM-h99pJCAqMLROyTDTZjuwlHdhPTLExAqLn7CoL4JXNcf2g0DkkaB91SVzVuULfz-reCTZOQ8EhkicAzaYgjKqdOelp7cuJluj1EtNCc4iAO5lYDafoobSvCCexECTWuAKUarBxXHCIDrphqMA3ZQvYJDXhw5fiPejm3PVolOYAgsCXlvPNEZxjIhAiCyN1SiQTbOIRn841L_e7U1ey7nzXfvFy7wr1InjYl3wQhBjUmZ6hoYPs_Gqyoe-Dos-HLrn4zKFKDrsDgTwuM3Bm34R19FqfwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc0URUhVZ2lr_Qfh7Lm0xF8Zol6FKiMQgYd7I-hPS0HYDmDCE2wWIPKsOkR1GNkYZOux7rZ8IRD1giE5ToWv69y5hQsqSBEekkFNpTG4PeV4Z-HE_4HjNuA8eUbIO4joEB7uPx_kMNXTXukTlR3DiWsEFLgGx8Jq1GN4Iuxe3rrIVgPiQISKi5TJu0tzOQIFFItCazoxULY7dmgY7tHf6BmAqjeIV6bRgBP2CA1fq3NrQe85I6PieRzJMmGHpE149Mg7uZ8G2rotICB6Tzb5_C67u7vaBcWdM_JP-fejT2F_8Tgk5bZ3kx0ESj9PpbJs0IegBVPRo1Df3VuzWKjKkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1EWG49gIwiTHPCDHfZwa2sS4dwAtgFljcoTITya02XVqCXyj8i6wETfqOc7JEORmQwXNMN5yzJwwc2uPqM4Q32KI8y6VMPCzcztvpD1xkdOKbsl9azsyNwT6sBPYJSZJP0peEHZrPcAkGxpRqbcI5BSMZzR4FPA_ek7nt_a9X-1OTUGfdM2qL0XeeIbC5YfMZMv15uSyw63-dHj4jsnCi5suo0Z0aENk798ptCKbcuBwADxvbhBsKniI006RxEMppUXyknFynoE3rdH5r1FS6xTQSFfpmsYLbgrIczVbqSTAs7gV_y10fgM40KD10rXQmlw4j7m3ZYQP3GSM_w67g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhQh6exttV2uF4DVzuV1jqGN8sRbJEyh3klppqGOUQyuKz3pSf6W92ZKl95IdcNqwTt3uFV6rqIvuiMK5iKLSV4kA_G91UKUUWaTRPC8ekgeKmmXpmj9vg0rZ3Lm0WQ-xHNpyb93HQawbApI3z7nSaiUUX_Cr3EgSMzROSSJbcqb0LmtkJFsTwpA2RdmAJvI8e7T2lVea0Tgi8zGSwc8xZTZuZkYa7BN-JVY_aPi1C5sa081ZE0WDHgbG3sNbRGgezvXW7wsppF8izubHTx7kE1WXd1mZRhE2FZMLbo6MNlp4Rjn6TeXFBwTR8jtRsIjFrzje5PhxFp1BB385EO4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OM0dgBNMmAx0PTijRSPT1RgjEyrRRSfvskiBgpLFYnzLvEfGysqzDIcMSvh0GGT7dgdHEloTW5VF3dDLCnoNukShJPMphmL3ju-DxG0hkaUr3OMR5SAVgvf4FM1pNo7bDWHBcTyfaPmtuD1mYtk1ZHCzpYZrv_jmJPcjJQjBmqHSh851slncP1u2ZPHJrj0PtfpXWHUAPExqux_xoanlpjS-Cq2e2xqNsoFJzGUYVwukG2EyMCJgsrFZR-Lf7nN3xN4c2xMz7XhHHqqBtFaZpJFuDT4ow7_6ubITGIPlWv-PGz9Hf61cy2BLH5joD7Q4iFn_tf84kAiBOc-KaIa52A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKrgL4zg0T_u9o6wSCslLEc8aXIjg4waxJiizihKUGSD5Ll8104ZVTN9ApnZegatI7qMXkoOr7OoPbWoiMolHsHqEDAIFyac14DQJuLSTdfYzw2_c-N8y21Ha_dYT1g_hUJeb2FdUAXUx50zSiEcQvA1VrR49DNw64WlV_sbShmGxkKmz8WxYask5e7z4sNCRNI8QOZZBph_RXNe4locaSOd70blkAcy7kTSYlLK1WDIHVn217MD1HNpYF6VzfQoRF9B0LfiLDTFSIoo7xbVdJ4C_Ks0ZNoAQDXgkNY-d28yyYxouHZuJXuNCwcabUJtM57U8je0fWh6axyKYYtTKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1uYX0htGkSfb6olvXe5obh3v6kCMnhSwQc6bGb8-Te-Sw3wAsFgPSXsRhdak38W6YEtZC7ShkH4aI6D_f_BwmByxHTgxARnYrR-nR7X3iZL_CqtJY66l_1AssBE5HsPtfM5CMHL0Ftbuul_71hJASWKh3vAjqlZ-Qrgp_Pnl_4dGGxK3AeVll5dvzQyNtcLePWjpIO3XIxUtVycX2TdiiGLtq-PXIaIGoCEr9o_gffYKYSKyu5G2xWCVzARi1jVr4bLWJtQogrYJ3LCut1S-r24-TI4sJJzMixEdKFM5xZ9AoMG_H04fzBm9i7aXysaKWZKyuyYmghb9dZvQovhaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui7x7JM4mnrHFSZ_JxOMIii6lCGDkSntU3H3u0cqQHwsUsmsNjkPGBFzyfAxeqAWp8ekYZtA0gG8A_x6QpMKYxkFyMQYsjF_J4fI_t8JvDQdsDMf61cjv1gsnBX-zAV4W2CMH7yXJqp3nP0TGNwgd6Yn6YH1P9SbsFLZBowbrZEUiB2U-SY-uXUp9xIuEhvt1F6CLjQlKemT_eH6ll0_CvtXhgYfCkfTIf6iPmlB8rF7vWf1F_-MpARHeMQkmhXSbmENNQ4xpoDY9Ok-vCGMNkFuPhTonqohbVltw413HOdHKI8SVDLxDpkf7atYEF-_dsNrASbFVSpTZwTT41Wjkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2v28tIt07PDwpOwg-hC5L0s1kkFrIolGWsU45Q7M8WTkwsBEl_zW-_f_huaPb5Nuz8NV06nKf0VKhhND40Tcm3HlfoCUwPnKnd4iZlDkzNMkT3BZXUum-LQmVT23QYuDdG2YtwiH2yV_h9NgNv8TA9Qft1rOyTiMReNSFhcuG_N-nsofNxcG1TdMou1KobdlB5vfROwcwfz4bPb3QS2MnNwqzXY9CUScwBROmF3NE-mYHwcz84H6aBvHRzu7xh0txWSSSgUx4FCkYgA6KOcRrEa5GI0KXNWhhNNmEJraeAwyuM1_GgawKWBUV6Xc2wsOLFpFSYwGV-aNxrw48qSxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3QZxT_tWHlZ_c0rU33eRZJPextX_EHDSPdAfIvL2YAXjeC-0x3BuezSzU_ljBt3OCV-bX1BsZ_G0HW6I5F0Yu4beOYIDrKYQOjSgVRn-LOdS-rrSbLkKLnC3hvW82_eXZfYZ2I-zaFV0XRaDXphvVWNIKzUlo3IryHZo06ANwq8_rgFJ-I_cIyqF-hjV6GV08EeqrCMAT64hv3yVGyg87D9oeWEua1WYceeYQkdVHx6LFvDDrjvA4bDXBavc5fCwdJXlIAPX_ZfoFtAKAbSGBUWPjl4-OgMW4A9doq_ppYSlkIkMMyWWH_2r5PY5EmHP6uPbwRlVWl266VghHPYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDSl2Y3Libvx_ScVKpamCzkDrcB2JhNszRQtRuxTIlKLR6f4cR1pR9LGYGajenEDQnGMQPIDRvayiq3zqo6QdOlr59ufJoasL5jfFmXM3DEvxONJGmuA-lcdf_SHKqkmo4DrHNQzXhN5-53HN01izDUfltU-gB0WU4a0XQzNzt7ZJ4f1y5Pe6UTw3BPtKq0Q6twuMyYsuc2haIYzYBB_0KKOvJ7fFzvwK_Om8aXn2XRvxw3Cwitr4MM65Sm3vP6Mr4dWqUE3i6I2lUfOaTu4I6bk8BbDYEvU3H8Juml5BvLyjP1V10_fWDY8vEBBRq2lmR26TcSJpELLUESgtZnwvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTMGhb76Hh7kYw-4VI24YQgu97waOkQrMVJ7eRvVOL0k0s2cP__LgK6rNnAdIu5mNahMRzd-9L2gIkO2gBKJ2atKTERy7Y_m7DqRjPX9n9m9qDG4vwEh2HoQv9eUXoxokcMZnrLM3qTpQtck3BX_qkqtPPFcINzwBuOGceIWWFimT7dm3Ih-vBvmKKRM9ZpSZFnqKyl17gCeW95a8N1RFLrmE32h69FvDB1Jn82H2lIuBIKaEZD_1GpGOBxV0LFBAKZk2b3I61_RZinGFss9_u8gBhjkFh7WRaX77K5lM-HB_Tsma-yiEtyWtix35jVBU0_WyceEg3nD-iBbVpsR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5-A2ez6oFmyYTIOP22qSWLSNcM7ofa8A5A2B6JKx-gpP8FLRPYJpKgdQOccnBqgewVe48OrpGQx6pYJqKoud-aNfSJu81XFOYVP1bup8ov74CkRSOsbYRacOTsPNmHa_V4xD2-vAb83SlllhrqmpABJrYoY-0OmlBL73yoGzDNe_VFKcozvgWeScesQ70af0YZoJAyX9EdjvKNRG9wt2gYkZQT0y1D1gk7TuI1OZt-Bb_DGJ23dyw4-_6buY3KlaaoOgtVScpkqEObp2JIpJwRO1T154QxH-M6HbgexciUuSwVx3FJeDXDTsd8_0L7Kh35ZZ29RY2747dvn2UnLMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMe4ESQxBxvBloyGz0sYEWw7laLuJ-3Liu5sCXYh9k46POnGTWhyUCWCosAmV1RHe5_h8L1-IIT8SvmaAkvMWWRFPUry1hs57whVJBuZQspqw3vCPLkLbywfY03GD7l13_2o-4SYuxpXUvfw41ZfT34tWwOz26JnqLJWZ9YgT64MAkIupjcgNK08587oJ2uvLynEbTn-ZEc3Pc7v2trakxINIPYZIf07fl8-bOLvTzOvw7nbUiac1Y9KY2ghVG_dxstudnuLmZjmly-Q1Lh9gqic_Qn-xNWWrknOAfEwK_amQhSYWxvjfS3Caaf1Bhdet5o1PyAI2ZZlK4e2os8O-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rpyt6k-K14W7ATF_kJkHwWTsNzcdLlcZCFTGRBG0IYX5guYIPq9scBp3s9qP2N7FCkYYKODjtp7UK8YujH2gP5loaLFg6MwA5b_HfFfyQEZNEifrisp8y6pB2qao_CWHZNV_Zqb_0Qf_nG3tDDsyomNSD-OkOZ2z6yfraiUVvVyt-kAom66a4iEeZ8RnRYk1_X3qkYrEQ2ZgDiUH55WfJou7oU4skZOjIq546EmjqAWpc66OB8b1KlAPgC9c6eoyny-C1TjHZ0OE3Q4EUPdi77QHFXejRT79UpMOOI_dPVZFdl3IEucyEUP99-2EAZXYgMDmBgF4o9lo6TJ4IJCnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edpmHAjT7L0fDCd4gTOx_wOS-dMTTn4Peqys-0jXtmSxvukBYPWn2oaNPYAd-YjMmpz804IwnzjGVGY6XvU_ez_Y8TxXltbK4wHlzLLE59fgoYivJfK1qX3qrxRbKLB2TwhIkIRhq_YesTX5Qe6BWdmKQUCDiqw7WWLYJ1bVD8CSVD3oN4Q91RfX0-i6JtGTQqwmEYlIrc1F44Bk8dqC7CPmK-ck2gqjYCFJb3IpGRn2F-5LQGUgqlBMz0cQewXOCFjde2d6e4Ju63DGpyK10HLWcBLIQJAyJklwGpmuBmYhpfu6EnTt24Z6MpdLpxvYJo3afk0lp_B7rRJXLsp5Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHhlNavVtiQa9cQdjsRmpABXL4vCCxP8azUcvjFrtQ0C5tkeVNI83i18Dfx5cSFibDFLzsMpK_vIFA0F7-jwYKq09YW1s7jfeYicralK_nvltKYLtY7BpfNG3JDOsZKzRY2Ib5LIz2V0V_pFZAkUz8qbbSzJ5_YO_s2pbAWLdvdRES0yHPbS7UeZK0RQOcZy5t_lFvtMlYPWbS-Dfp7v0Jdc_iSgHjaLu4cRdIJH_eGyJx4No2h7gLeslIhWFipYjKCP8pfHOnnqvG4yqCSP548cI5WSMaKjRMOlBJAbcFqOWl1-dEOamGJ6ELiGBmshM3DZgN49zRiuYD6niPn-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUMdoiuUxQffvK-9Jjk_9jzcQmyWP7RtClVznp_SBc4y-2gHBf-e52o2mbp1qcyAeCVL0mmj2F4EXDRQnzeB6FlIUkIj84XpwWMkSM5ArY0u-O20agHnJCasf8gXMUVsdvWJC_zv-u7ElvjiQ3xT4o2MTHQ8t25TmgEcyBugxna_PNwe1_L4kf8mf3CC1a9gLbZCu3B6YuVBrA_fcdaRDROrxej50sh2ord-4S9ktXmtum29MG42-OF3Whu-8_MWT-XWac51I1SDXCdI5zf3tDnPy2fUApb5z_UKfJCUAMPOSIg-uWCv4yRYXivoDj1_NlZc_uvSntq11PGTjoIkwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoT9KiXP20UbAm99ExAB4iTJ04-rPgcmzkF_W3PJBFNeQi01HcXIoxoLE1-eg2H2EWBxTc_2SxX5BiInsVAary59rRAa6RCu5xLUNTLg9Nbh1m0KrGJmX69rBqOlqHJspWs5XGis38lY701unPXRRfbNHfmJglU4SjmuwlCazAypszXFG3A4WkM7X249WnUrM1Plu-DG-ZDzHIeVXznbDlIIwB5TVY1KePUe37oXjIYanV37nH7HahkuxjT3rh9sGGWKB6YhpxTFuMFr0M91YSKvzHjbcCsxznZ85QZ4n5mxZjyiwf-JJzcqECh7c4NJ4H0k_n2ztN9d3JVTgHRzww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taTdajTrqzYagiFFRojH4MuprJ4WMofoImw51u4xe77st2BPvCrHbwD9JhHm0oM7mL_FO8J0PL2ZBiolyiXAY3NNT-HrSAw5JOqhfzdLmsVPvFHypuljLMwmp7lKSB8sw65TczDn5lgNk4rCTHGzeX_3jsF8vg0OHjDVJohrpGqpdN_aX1BMg8Ac3hlnrFH91wII3GczxLNokWD1vh4sZSX1jZ9i-Q2EZRSVoskrUYOLzOE71ljCnVKMlgx6OlLlmYi2AdqDTQdbBLYEPtdcwjx71WDgZtZw737PkcNdID62CzNwfoU2nNjU_2bYEB1t4s3Le_yTs4bm-hZoszcAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcjgW7MU6ewgdyZ0qWgtr7I59GMhqNs29tzUxgOAZezsp8o-sGYqgqbxtfTaO2QPDT_lgwFt_GnPts-oCxSo43P5bP4ftNzGlLMh4FK9JzUMmjJkWEvNNol_TFG4J-DqOb0WP8BuMv5xvEKMmA2DiFu2NVYEWAjOZa4BIeaKA7ucKUtFX50gpQFrYszmcw2fQiN7N7SGUOX_GqUKQpXl48N2INcxiKAGdp6wuqs8ovf04uRPuFLdr4e0DKHMA6CRLq3ETWvshv4oIzTY9L6Hz6o0FsoZ9kRNCCCdIdo6yLDMlfhHZuUBLj0WXfpzfUBntYpgcYCsJigdhtw-8M3zkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn-MyMlf91EzolZTNS7bXP__A5NkWTBZ65V1f9p_B_1jHg1aF3kSSdMkMU0DzxQ7YiOGIOTL4Jg_xnJi-nreRuwUNiGQuyWe2xL9RIc5jMhnR_Bmc_qy-Tev1-sWRh_FgEqy-pyIkzeLX-iDmuWVrR1joeWzj8NwkrutEjQhMEM6WtVTA0Wezp4_54ukXDbrDmL_rjfF-EgLvqqKGWP9Sc1pxhstJUZuDZBt2TM_-h2GwT3f9alC7CDR1oo4W_c6-25gOlXB1B8tJM6LRgJX9vrlnyMPEzJAD72gwgj8qcX4_qtx8Nx1eFOXVxCzxwYJm9EFsg_7zffMYGme82TVyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDtrFk-_Pg2mSNiXpkiOauWzxRSvu_SSyrDJAaGC8LtG4NNpwFMMRfqDOetUZJDa1kfehtTWhahgJ4vdbDI9sOG_MBTzmr6YiktLmQCRP2m92nLzfpp1ZvM4Oq3I2oRp3NGfkyLXIwmYVX4Ce_YtojQMxi11mFSODUgHasCNSJOnz0ZemTW5x791P6lFtex96Ay_tJ7sbQbPVsKbzTcoRQmGt40oyeUm3-TIzSt-8fapzM0Cvy2mrWGzjuyq9UWcqca0gN_joQ3XEOD7Y65rniTEJav2a5b0g2gKKS_0_6bze5gFKb4cKOVg-RNYKmpNiRUBwc7wBqWUOMPoS6Y0QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPUVHEBBotMV59TjnSpJqg4uK0zvFAPVnNUo6ySjbEbIj5jtQahmjkWn4mpajgJfIzu7exD0Wb02nPVnWlg8b3gcTBqUjgAFX_EE3Iijz3DHMbHZasUNN89zJdABnF7Oea9ZWKCTlS4iR95D0BTaAC1BXe70UURn4dJjSbB9_003USFrF2GaCzUBgcz-ckU2CHMYaHFbRYLAahrJkVXmI7N7U5ME5L1NhEwLRwM12XqB8HiwTtBLYH_4eh3CISR3gmJ5Xg4Vlmipe2F2PHHQxW8eq9RpOTDFzzPrHUgRTmVe9hz2Wy3tpAHdUusDjkuKlvH0wt_He4FDvBbT-wc5gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3Xw6WuHnOyL9zqbE0RJy-tAJJNJOLnffjff3d-ilANdlVvF6yjFuGGlvufy1bafbUBiIaRiTRfepS5SS3CdJBYM8gpVmMoiUZlxzWy9z5HlzPQtnDHx4iyDCuhFLH4GCPFUVC8xXgSn2-em12w1WmlyPreE5LnAJXPl6dMZwqKX_SVWzL1vqu88Z_fu1sTIv1UqMJY1U2o-HFaNEIA-cjxC4xkwQVSPbMKpbCuD1FEbY7dylRGKwzJnxLvbrV5JZ_c0ShyyqXS0eVyB2q6TnThWAmATEM-CyLFMjDpkHxo9ZGQcGY6jIkUJvZy809IBxWrGedyac_dn4csmOlGAYw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=CbgvnbGHqHWAQTTvASW2t6nCsYYOSh_YsyjdM5Xpys0MHf630fSDMb8WLSfwQigRPOGCDxUII_lhx7lvaQWWMIeZeDF8jLJJl3uGg7McksxQGfsDbX4zCQpPhoeJFcIVxxWPadeRSvlSDKQwuiS0l5qUIqdcneFS844ZLhLSv8jd6gi6fh0ZoinLJVd_KOqVDvUZAq5_MNZ5pKl536cCsX9yZp6yK99KcjGP4ztCYYIsF3F5zVhC4pa0THp1Nnp6AQ4Z9D2T3m7yLZ3btn3A34MvnvEAJwF81cGBNBnLnslMoD54jpK8vbFjDTSJJaRHjXeJYTaMBg_Md2t5_jxAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=CbgvnbGHqHWAQTTvASW2t6nCsYYOSh_YsyjdM5Xpys0MHf630fSDMb8WLSfwQigRPOGCDxUII_lhx7lvaQWWMIeZeDF8jLJJl3uGg7McksxQGfsDbX4zCQpPhoeJFcIVxxWPadeRSvlSDKQwuiS0l5qUIqdcneFS844ZLhLSv8jd6gi6fh0ZoinLJVd_KOqVDvUZAq5_MNZ5pKl536cCsX9yZp6yK99KcjGP4ztCYYIsF3F5zVhC4pa0THp1Nnp6AQ4Z9D2T3m7yLZ3btn3A34MvnvEAJwF81cGBNBnLnslMoD54jpK8vbFjDTSJJaRHjXeJYTaMBg_Md2t5_jxAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilyMQFxydIzU7ctvBLBjZYZxbCFA5YD7419cDZqosIHRBW4DKSy8F4tywOBlJzar4wclYmzLSxLDPwgwR-ee6z0LNN4cV-rGBotyen9-edmgTrCpgyegGLeExfB81D1xA4W1l-ihTPHI2EpX-P7W_XNg5utMjBRPcNePlV6XWoiYmaWEcpYH5K69zH9S66vwldPXIajmPm914WBYC9oEHkCTegQ0TdYJLkIgZs6acwEtRYDXoTUY3bJytIJLvdc74AbqXQ0SxnoXEf4gUh4JAKRf_pguNF_osv-z53OJJfYPt9xEosPLwhhp8w-v97BCU6tiQ9znd72yrrHCyMf83Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psv8-JMMRatF_IGpawoEdwrJGM26FEmSFoyqCAGEk-T2vQA_OJbmzSZawDcR7RIWa2Unx0aIPffVMKlSx6S_A5n8ScA1tHpBD_OpGsJhbvRXZiVFkTQusl4fi2GxTSSVpL4EHd7zasq82CK5SwW8hB24_uwLfHZ7o-MOqhrmvukUbTK5ALKElM9x22y8F9fFEQV6n9EIbXe1bLG8RQNnGWrnW6Am5fe628D6NXkn7rZnGaSoe8PZr3zBtC3OhO0lZkZLM81iLDWlcBTvo3k0_sZXS8z7rn-yrlrpugFOyo9VLj0-MtZp18jigVKfgV4XbuZbrUTziV1YjM4pGwKe7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNS2euS7_2zBE3AlFyuAwn1GjNVEqqa9TvFTG4oiGB_Xy0BzqqsM9Labo79YU-_-l63iRhP5PGreTp4xLHXvi8CbZi6tyAYJ-AJajzksplVbxNmT8eJl8-Wmm_iGclAocPYPSmp5ez7GbsQVVfcZneFBuJFm1HeEZwq78qudkdjTdPYt7w9rLDTEm8-d7BFWL6XAL-IY4UIrZ1UhJDiqO18UVmxTP2T6HjrFuPSf697rHRrYF3O5k5_IZCzPk25A6I_abu-ZYsG-vXPEcoscrwzAghyj5HOtOuciwNkhidaUl5VU682XfD1PU5cON3h0QPKYvx9Oa4B_Gel6Yel62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNGhaEIacPDihNDVUwgzbXImD-h4qNIM4cXTtjfUN4GlhWJsiMjPb8tuCRlr0WzlGWmEU_FTbPcA8VI1Mvg1kkPrT90IozfH0L_sCI8bun1lgcqizuZtxO_H0DpWE4Lw2LlIXgHVzdrVpaTgyuoxG0fgP-tdX6nyP309hHVq7LtA5jwezdUJMWJANEIUkv0j17-1OIBXL4LaiuZl9NkIZRjwgX3J36sXJoWibQXfI5qHcb0goYTsQJQDw5CMbhEGzxTe2XNJijbn_rxbpl8fYo_oscmrS8_k7pizNHBbfWi5MKWO7gqS3Hh9Z_dqnAaR1ISW4Ga-uIbVMa9scRhSbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_T8nS4wGZqVkktU1B154BwcTbEB7oZZkDtgUcYnF9kilR7NNyJ4wEr8aFjGtQLU51-uUzzhFK6M6StsIaQK9fEAenXiz93ycD9Fls8QuP3I_Ju9vBryaFwRd5X51OgUUfcB39dHsr-LgLvePQRxD71BO7f8p9pk-UrSwkqs7MyagrR7fMrVgkKyf1mtm2T-XnR2_JL7nQpZv3_nbCt1UHqS6obZxBKBzPJKbmwEwsBESKdNVcWhCropqwx6gUbf4GeHdIeqmxZNF5HabFt3PIYRstgHlCNLlCmZb6DvRmTfS8182ZAEv7z46poBV6SPO1uNyr20VYB5b0T4dmuMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZxn0Z1o5cSOH3i7PPNjyvnMBHjUk87hIO4R8qW5zXkk9YPGHJ7WThrjF7ko3eOcxpivAC0J-n_vSdDAFCNKB5jS0_bRZ9ZWLhi58qC7z6DlIJqvd7t5SRffRlTJnRXMHH0D5FyaeC-H50K_d5hV38IggCwFSAYHwqKvgkA3Yu4bfzikFcuJTkIjTHamOgBD6fbRT-BUmx75SQccpYXoVhy06aAGAHXDAbqhWT3twCoIkvcfkxg4UmmPV32_Xs5XmN9d0Gc635ZZxqkIOU1r2usFrjOgu4BTS6co9opn9rSsLihVqPD3PHru9_ny7tObpOX2_IUkG6SwkHD31kbGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYUID4kI0L4jR_KOj3dG7wIBKMl8j9_Sc94eYFuUsK7I2mxfYkfPez1r04iU-CW1Npg0W5UXYWWgNnkoA-5uVC5yA8XFk4e_GggKVJkeU_bldai6RXwsE-YjTS84r8yLTa4VRncp-hkvNSJ1a0GxWAJyAy9HFO6M4C1EAflQCXHUvmTL2qRpAl5BuyEfB0fiGRXWMNQ9AyauZg3pYo3zTQpfF5W0DfCYSPWANPPC-5HCWw-tb0m7gfcxdiCTUXb1L-atVHZBf_wRUoVKyOjSMJ86Eq4R0gv57gV7Du7151umpWf9ySXIOXzNMPAS4l-Jlc-AHmUAfJHnPUjPvgRwlw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Yx1Zz269n84OM52_30ktDQMqUPJ3aSlCLicvcVVCCfX6DpVnKRXNzLHqpNUZIl_tcLMn76LgzkfCcTdxc2ojYjx7bOrERqJdurm18h5_Xi_YUJb54wk2qIkFQ4Jg1gFNi7RjKsGHHYc-Kpa0RPEg2IrRMS9erUhVIaDdlth_xsWPOdC8WgDK_8ErqMVbJ2cYtmexOriiLvT0tgDebftF4xyqC6X2HZYw3dWWroV6DJiUtY7i86YdCVlwDXsD7zy7kj5BaLnSJcnDdDCWOUH5Xpn3PYRdEst-CVSblsOO20yEpEXZqNOgmTo4EzTCTLf6IENzc4jkWI0KXa5TnBkHgwwg9M9-czSwNs7LkTV8u5jAz3klvZLOC4JQLVl0PgrEOKMYqj55LHIMFWcTzs3lq-b6zfZR3NmcruJcNL28cAxn-aQDCyfmSTRCHaq_os3BijmAm0sST17yIIaELFT2qN_ldJDygh_RhuyhVGPvyJw6VUFvaK4HNiaL9WepgFR-qooXImI1BOrc2SS2MaomfffkFReCcAxA-JHPR3IcVoAfmBvj3m7VoR8-0MH4YUmhSW39BTBviFuq9YjYQ4Y-Xs6YK0lFHeIX5aQw3eq-1tdGVPC6ejrd22IeFWgXlN2bWBwpmrbE2kFTsl3cQER-D8fTY4zsT11rCjeuDJwN9dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Yx1Zz269n84OM52_30ktDQMqUPJ3aSlCLicvcVVCCfX6DpVnKRXNzLHqpNUZIl_tcLMn76LgzkfCcTdxc2ojYjx7bOrERqJdurm18h5_Xi_YUJb54wk2qIkFQ4Jg1gFNi7RjKsGHHYc-Kpa0RPEg2IrRMS9erUhVIaDdlth_xsWPOdC8WgDK_8ErqMVbJ2cYtmexOriiLvT0tgDebftF4xyqC6X2HZYw3dWWroV6DJiUtY7i86YdCVlwDXsD7zy7kj5BaLnSJcnDdDCWOUH5Xpn3PYRdEst-CVSblsOO20yEpEXZqNOgmTo4EzTCTLf6IENzc4jkWI0KXa5TnBkHgwwg9M9-czSwNs7LkTV8u5jAz3klvZLOC4JQLVl0PgrEOKMYqj55LHIMFWcTzs3lq-b6zfZR3NmcruJcNL28cAxn-aQDCyfmSTRCHaq_os3BijmAm0sST17yIIaELFT2qN_ldJDygh_RhuyhVGPvyJw6VUFvaK4HNiaL9WepgFR-qooXImI1BOrc2SS2MaomfffkFReCcAxA-JHPR3IcVoAfmBvj3m7VoR8-0MH4YUmhSW39BTBviFuq9YjYQ4Y-Xs6YK0lFHeIX5aQw3eq-1tdGVPC6ejrd22IeFWgXlN2bWBwpmrbE2kFTsl3cQER-D8fTY4zsT11rCjeuDJwN9dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJCtuNQBIap6AXo5rjNgu6LtcegzUl5tIOawNbJlKKu-Zls2aVL30qB1v4iauhD5JsloRmumPHXS7j65lQ_4lw3FaUotXt5-QOi4t2zYdWByByMR-dQoJvnXjMrV1Ap47M6kPnLgSw52G4GTerLYv5xP8K0X3zK1Qt1M8ZSsDiKAw6wiRg3qLDpiGBAoiyMdSGUzvlxabNebYUVV_DS1uoycIvQeowBYpdP0oFKTUuTaMpJit-TPOdb64iVD7CvnA8glHEPAQO6Qs2JCA7HCThDYKrs-gO4EqJ-0g3MtcNKBjgqkkpfvD3D5heTFwW44PKggm2QOx8UICQEfcjZuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsH8Pj3V_1SFI6HAOGBQQM6nGD9FrYX65sSPh7JsSD0jYJKJhCGzTgCOYUEJWTSkpabwOPygtB9HiavYoBD2_eNctCGxmMrhQZO4J92iIat0xbKeDNkkuYK26jAyoGzmjRA4_EA5xUv_C1Sx9Rq67ABJBrP2MpH9qGZUak-ZoZWukuvW8k_b4ntwfH6eI3j_C5RfjxoUPzPACPQMyDtxYeqBspmCMPm1K1Xpa6boJMUmfEGIk4iAr0WZif3N8wbzm51TGujuvltiu6qKs3Bc2Zt08E1eratwON_wS-vMz7pcRjs-cwP-TekUZ6vb65WF_dkBEILr1um0h1VcfJtLfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IshF0Ih5MvfarOwwIF2ZtZRgIy-aHoWXjLAU1rV41eHKO7AkWXR3ZQqbxaOqe98OELUJDX9gEKxZmOqjIFw1Kdw271W8eKIyIwmzu093ud_uAt3V9OHbgqluTJBZwrv9NpD-KjUz9eHbnkCvciq5p0JZWidhSorWllRFfk5Q8wtWPb557wFf4azWEtOglIT_4btxN3aSxmJd_UT1BiJc6LX9Hu6s2jsvldk5XdCWUNsAWVmW6_CSsVz6q11TMK5HJZNjSPH5TXyHZbtQwhp9c4ptvrCYhBjM0HDStDI_6HrDcAxMxjoIjwhUszy6gvPAqhFlXKBD4UIcsUel_LsdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrbgE455c9veI77eCxAN_DO9b_P3354gF7Xjjxk-qtgZ3ZgTyRYa4pBAi3mUxvhqbS6zVsiYYXwKM0PnbSPcOX-4ohh2jYS3ofCgzvXHzfoqREuRESBV4AZeAGWJL-P-zg6G68tqCJfFYHV6ZN4wAV9-e1ykg5ghGjTrY2D29dVc8iJ7LkYgbZ1RWT6wj-AHFzsKyFQm-3fzXvX6Y5MS3ykLBkpOYmY2SNuQPt3KRBmuHuL5OGLJlZOXnXl4VCzbkiH43VDQOCyG5pLUkkpNT_F6D5G_Kk_g6E6QacQLmrbBg68zoHlFuC2EiwbntoMsA-Cg6pAcHuWiu0eW5FSPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edqDQW90KEJc5a_6zaFZu0qIx4dreykHcBut5yTjWFo6x5ODP9tuU80qKC2-tA9csT7f--6Nrv5P_w3WxGANmzMcRwcaBxOy6x_zKOMFHqw72X0UiOA0a2eNs-EJ_cQtP4708MPrYv7Y7kFCQVD06sZQH48HYLfQSAaXPUZznNr1BXfe2UcI7uWNUqZ5P9tZOHb4Amobk_UlZOzk-ACaB7ksxhMHbBdwVbGvrVpeSjgE1MdtntWT7-GEumFUNeIUh8u8GmMfbmxV9aeN5HQmFVTWA8xesHyCZ1I_d4jeqZrngKjWsumw8DOqnQPykfA2EapwVGGTjqzJ9FH9ZiRyqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YYyIGikD_aJzbqAZpr94H4RIRLemAW7bW5fCfILr6NTxUarilo2C1eE8T5OmaQcXU4d-MV_uujreHqt1ekCEUZ18AOdKzEwXV7Z_wDhQIvBcAFPg7oQ41J33dvoqFctXqHUVhNjAoccT-tSFIhROmi9mJv6jCxHf8Mw97qxU1sVe1yFVpBe-TxMBHHRUzz2n0uSuFJmYUfrEHmu4SJdITaahG8wW7LqJzXNNm1eAH1ePRpe2FHPu5Du2swZdjIamuQDzJqj7o926HB0sZ1Uy-GPGkjhxEb8s2X0Z8_Rabl5-98L_GQX47C1o3e1ZCF3wtwiIrsp95Go8WBpRZOPr-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YYyIGikD_aJzbqAZpr94H4RIRLemAW7bW5fCfILr6NTxUarilo2C1eE8T5OmaQcXU4d-MV_uujreHqt1ekCEUZ18AOdKzEwXV7Z_wDhQIvBcAFPg7oQ41J33dvoqFctXqHUVhNjAoccT-tSFIhROmi9mJv6jCxHf8Mw97qxU1sVe1yFVpBe-TxMBHHRUzz2n0uSuFJmYUfrEHmu4SJdITaahG8wW7LqJzXNNm1eAH1ePRpe2FHPu5Du2swZdjIamuQDzJqj7o926HB0sZ1Uy-GPGkjhxEb8s2X0Z8_Rabl5-98L_GQX47C1o3e1ZCF3wtwiIrsp95Go8WBpRZOPr-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaUkpe8yZYigBAk9uWWQwEGx29SHz-FGBVOQdOMdgr53bWQ2aGnyuSRDOg26MV9nEeKAvYrdErt4MUffFqAgriH4E9RncN2FQmT6v1qSu8IFVRvUvynpv7S4-ml5rTaKIe3EzZ4lvtfMNwLnSlpmmzg-o4EqJZyi0mt0Q1lOYLRtR5_Kdawh2Jwv4b-SsSffh3IZ62vXodH0hIzZbl84b-h_nl5Vq4XOeNA8pFQyHYPvwsf5t_sZWKax2_F4gqT8e95JFBbJQYhEMKNWMR3GMO9fgKPQSiU-0KCCTxMK1OW3pEqeZkfMrBCuizs7Wd_aUcmHvHsw0a0Jt7pT7OdW6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbR7R1SjPOfUFW3lS2ZeOJGCpyjtMP2AdSod0PFi85kf4V1FGK0Yd5ORhjdoLqoiUhz9SQWQ3_nLiRpR-v0a-so66iF4Bpi9Y0vjhiIHaC10AUchUwA9dsmUZTFVevnOPLQx5Th2t-UlJfwe_-g1kTMtZul7TAUgBA8j9MhOf08vdaUZvEikoc2bv9FqtdWwUfRKGOFVQXqzYiykEHi4F-nvlZRfPaImnW8rhl_BhW2j90_cRmP-lY26fUSgwpRLZP_VpZymlsh1TXcx6hPDG4E7vJ3Oh4bL8DrgQvPcH66p_YucnjgX0zYhZh5tCzCwEFtd8zMnMX8yFT0fN1HQbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIrYtSh3ktrsSzQ5ue5FFSwdFKyDq24ZRfpABibNjASuWilMnSEEDd_7Yjk0SIEVdeUBDXe_XpPBSGUFkRPGj1V97sU1nQq5F1ZIaPfOda30b9X5aA29KsyHfOvjBr3vrSbica8NY3DD2YxMOb3cI5yIgdSKQtyBEb6N4Ximtf6IorifEuMy-63Gz8jG20nsbsF60gKpeet9bTQRYXsMOddadWcxqxHhFz--b0rc9NAz07JADGvAfoL4ylGTg-HI-2ffFerqdW4EbNwJiGDhuinF_OYs2r3o7yICON0q_0jJLdj6w6xWAGc6Fwgr66NSMv6vv-owUMOXvxIBtVPfqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgiibquuK-nRmKzNYOJbxCDmqXJ9RK_g49dD9AKxjEgrf5yNUvdZ-G3rURwlSCtQ8wkjrP_w0D55-0VNIIa1binngao9Co729nkuAeF7S6EXxCfvseImRUwOyTUgPu4yFx_6RR9eO6Eg1a7-IRD1QZpi3WvJHu-TDxJ5mI6xBgsAUWTVz4_wmdOmE_Rn8ecGgX0tPGtN9qC00Lz8J3QEleusDGYlHmcvdjBioFa81wscU2ZU3QJbW6De0iciHISV8lUNbcGZ-9EXBThLmQ-7i6FJAm6zKFFB9B09rFtikhuSXoZSoryLvT9AklDIUpM_blaUertKbJRnYVZhXyC9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQaVew6dTX617Wj_TnxkIBXDkqVYfx4NTb-n6JQ_bf9sfz4aksqCmSj4u5iYk3psjoLWEkM67JTB9VTJC_rcgTwu_-hicgKFUjxiqLLPTfZ3qJXNfNA1pAh7u7rtMam0BMmDyWQFvpgjP7fVTWPG-osxw7Cn9unHCMcKj3LekXTv7ONS8htmw5s1NsFByTkRVB7rLkzXaRIPqUj_UbZJYSOW8VO6KYrFeixw3Jby9aPS9Y8Lv7mp7E2qu-Y9TpcEe_PFRb0X5dNpet-UjPW-89Rpq1Rl90fEvJVtVT05rEXtFUPQK_d68x57J6XCw5A8nDQJUbfFaJ7T87AzHuvcqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnCemTDs39V5Bh2TyxT0wNB4BB-7b2hf-PWcoytSJTATT5PYD_aHFFAylTpdZJ0LOWVvK39kw2HM21XNMZ5RUnGnXIL95Q9l2QY2Q7sGE50dRvmz6JB3yMYIY67Z8cVGqtWOmqLmCqQoDNJFq3RLn7l1g0icOjPt9yJb-0gxo4Sc4O-aZBycTYT3TtB2SHlvYS5f4aPtMHN51y1fdYFu7xlTR9apdaa_oUXoLuZs5X0JjjfRB2GecteJekXwCWy1YbFk1KoLdPWFmXcHofIYEI0n1tpqvhINcJNGHUaxcy25XleL7T9TMUpB7WVv7DbQuiMysW1Wpay1TApfwnXNJw.jpg" alt="photo" loading="lazy"/></div>
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
