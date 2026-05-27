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
<img src="https://cdn4.telesco.pe/file/PbK9rFh8iVgCCEU8ZiOEnjQ7G7HcoIst5FDVfbZocbiSToMkrMuZRpkJI2rp8D1vqvTgGKcMVrVLjo2BT5e5chTKDoKuywpfoYOobCMhFvAA809DdJIHQR1lDC9CeVJePO2BqwqRfmF7mqpTs6fOIXpD89I1jGfT3Vl8NOjorGp9N6yLyFt045Z-0ZLMIzNqtNMsrk950Ef0zNvfRFUE6CgP3X9GRu7M7WNXlerfB7J0haqZQGF6zf_PwIwcScKlGyH_32lipxG8Nr7aYcB-o0OsUrKVLZzFnViOnG6zzdLJAJmRV8dEmxAqxX-HpZ2VpswIM7imQcYJv4hGnArffw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 03:12:00</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 247 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 342 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJc_CKadHLiBq1j8ZbKM60kkrSbKWEkABQIqFH4uxqPRUi_PEx69YXmrqFLGrLgiWJFfEX0Rxl5T6XsB3CfVnyktUcjHaALGBqiYzFx3t0MjrmnIicyu4fEHhqFunUCtWEqeRGrfcCuSi6oUnUTi2fv87r0BuEcc9KZgiQesLChJVGfSpSwQLHKIJa73WqXncjftdUt84PEyNuI1TLptqVwgk1cbdtAfTy_VPCV2vh8wJmuJ1GKWuZVn0TIGx3R2YpsvQEeU1CUrjYGOqNDoUfrGTfg4t0twFCt9_T65YWdzdiVq0-9LZhhDpelENv_btsCJluCf4lQffIbT8PyUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 437 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RinpQfzWU422E8RiBuAClkzWTgpuHsvN4h3iA9hrYADpsCv2Mt6bfHHtACavANU9QgqqqbiJh9NeRE80JZC8D21KnL2SL07RR8KDk-IqDEkouGcxas54te6-UmVhnZrxJkgtk2-zreI9cBFRDs8JonKyp2sOcLmv_VUac6V5AkjY3fvsftyIldbbOykNNUui3ooJFYAwfQXgm3wXU6TJNRmm0CugyQuOfHDD-kHCTJ0mXXoAJtP9Ay_lLRFeYPkqvU7U3IhfCgRHs71914DRd6DMjUWJT1IArJ5TUIg5ZNFfUQMiP7vB5D0AP3rz8O04EbZ9lbFvbYj_9iSnsYeJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hmM7S3h9mqZgG4dw1zbIwOqbNddKP_FoMCzNPm8M5vm4zHCNQ4j-Twywxr7E6PYUbEEYYSYDb85NqbmgMHu14aoFtuLaLW5Azmc_VXE0Ocw45myzARWYjUcVodrkxFGzUjVwu9Edijt86wa0KiB4jdmcC9S2Ui-Nz0FVRLB79hBzymdy3pbumw1zjyyyydkM-k4DtvX6YdckzRTW1JbuzoUdLw3Fno_u2rNcn_5X49uSboAdLafCN_tz_CjAPoUEj2w7W2EGaCqVFWZ-9AVDT89WeB0PardgDLo6feTe5h3muUd6GvAhUj3m_l55rVfwpFmsh64zVG6sjQsDrh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0sueVT-Smly1ZbWyVZpZteUEg2hGjycpydWpZOu_YIdYuFzQWbcery4SdFPaQIuCnnZ5cjm9caMIAJUvE9XT3m_NHQMl32CTEVgkQezPZojzUvHrFEOaU00hOWwYvu9sDphMlD2MT8Y0sd_G_Ahb6NGS2ln5eQ3FRIfp7z21tdNwtDgto5GQx0z8QNFxzJMqTSiLFwajABcHkjGZPvNpJQA9AwN7mwGymEcXZN_vZD-s_eZlH6Q8JCwlG3b33xcskfCPLaMbU996Wr4i9g3WPV6k_KX3GunuN6ftEJhePvIfWjwQbhKOaThPZmCB7B3nSOL4vuL4eEikZdJzGl-DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 998 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJq8ff3Qzs3HfGIqRdk_MvZ2btazhA9zUeCzf4znqpF8AdLnd-l3hWLqZJZp44D3oJ8rmr-mFuVCGLJE1Pjj_Gnn98yHlm9yWjNXaEc5XprGfA1HzEFA3Sn-DU5rGnoLVKNnlW611v6IrKhessYU03CeZeLvzjaC-VMnGWQ93xS5Z4a4RHOGSMKMA1Loc8CrtYifmDXmL9SoSg2PPZr8H0hQSj8RWsS_O3rPwcPPMIJ3zgJrSVNODDE57MYuIHc9LRP-2H9ZignkKDbznw3rO-A4-SS2E3z7jB4rkFfu8k4e8Ux2C5yGcHnpxEQRyAvUGP0by6bc5P01g1tqAQKmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBHSwv9HJ0IJNQ3Bd20WjC16WvWoJ1fhAYs3Y8a3fp4Ue8D6UeeS4dbSzaeNYNbsZKJuxmLZYEbgLv0xchz4QSHrLN1Ye8tbln5L73XrJjz3EK5TH4hUprfrv287uUVUUy_eIxNvGJzihuz67mj8BBTutgalXQyFs2DF40bJeocQSptqBqSNc9ZGQbD_WrKoyh8UEB5w3IxTOEb1HhleqTFwS5BrfRQWB6pjgxPbZEn2cStzMPVMdPZSXld8gHH9Vs8GAt_mJ43hYLzxh-p5oSEk0_etAx_1rrqwj_15pUuRLFylK38Aa3JrcW719pWUg8cOI1kMR-XUF7_ilwpbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBufH8VIrlMcOGgySB_U4v9oozyWbgj-MFYbhz10HF5ed2UxfPLkRLPoXyNDYuFlh9dPyAfNOwVxa_Int9KG2tocF9K79d2iYzB6ybsosIX3l2F7OYUkStNQmXggml9NiJtq_JkOEtPaqOkkOQaU7delc3k8Ep6vkSBzsusVVTW0fZb233XgXVLG7DQbTXZlaecrpSbTE7b6MSwp7AUAHFpyd5IjRy2P-HPhklv6Z46ePcIVzmIp5cccTfRF7GpgnD1EZtuUKrh3hWv9nEr1ZkLoelKO9xyfuMC3xsU_LkWLP-gfLWJU1CmYKMEEmEgGNt0R9uGRHzIqbdvTTh2Hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Trw7T8l2UzdLRWpwuuFxfGnpDOsPuA_503iwV9ZbV8V2AJO_5ZsMAd9hGhg9yt78FIIQQqqXtTg1XK8AG_6Tak4NNtY0zswWAKwe9-DakrUC4WU6X1o80PflQG7JPodmTV02vs0thYGLHm4Acj_3PRQgpprVcUTU8L5FEZZ1341g_b9LIjWnvFFyoeK553sP5ezrvcMGdvjPveGDHJAjmXfejjR6SozN4Shihyzvy5H7pyVWP_ylAlaV7C1mqKeg8Lyj72lATjLWnOsK2l0TAqNnRlWyNiJn5ugd2OaNHdATMZDn7egxs1ELGnulJZNxotlz7vcZrAO5wmFnxZBxwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9O9B2kJVmSW6x3N6Nrwr-B_4PVS3bpPu-YQCm0BxtSpNjae4PtF0Tr6t0lGoUTdcLgdq3-5ChfBSnXu2mQkvWQUda6bdILB7_vI9hSIL-YK8IwT6ehqUS3XAbcxhtvg0rtP479FywSQronTrqvltC3PD7otz28cBEYR5ZZXIrpt_IvErTnY5dRXPiPHuSuI-VlUlstFz-P80CdZpsmygky32vYCdsxxz7opvKtfUhDYMDni6gBok9-fiA59dfd9wb6GErwLNfyFl0vIPynHGr4ni1RzI37gZv9gA4URZ3RC2Pa0812vMM4Bzkf8XRdT_RMc9acGIVDi5ZRq3MSMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUmD6-XHXgXO7ojjxoxHz-PEwDW1kNvAMhvjB_j6xIBxI2VX8u9AbBYTr-qk04dAPYjEI4XZ3k66JnKOXTzrCcmK_3AM0Cgdd0rRsmTDu3fgCt9ncOmJIvZ2ExcC1baXyRgTxqA0DIVRmqcsQKiY7b9dNdyIHD4ztPtVQtBZxluYdYI0wm-cr1JZTdm3-O4xE_-NJJI9BocwEggC4gOzzI8yuWNV1o5VQ7O5mOqOLjocRajzoxOXRzbp5aK7o8jBmVUEMA6B-dxX-RP8QwLhr7VEiRIMBTChPqcSuibSr2VF2rqLGAyYtdjNzQgat9lJf1vJObAKw2RxS9bSeTPBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC94KjU3FQWsxs4Iji408NSvHxafGywlxS0YtqX6oMa2oe1z9biUwLhOtJGpUv7XsKx646RD0Lk27FAw-j105GyLjTvTma-9TdAqKMBNQKx45tc3xPoABcjtx47A6w6ojsgiPUY-yghGAwx-WqOTponO3MdDh-Ucm-S2pllayjPLlpuDcX7zIq0fDuCims2fgzdcVj58QA9jyCmLujAhn55ijknbdObWFLnTMFMNbnc_22ClwMh0BockhZB9OikewCYNNaCxm5-STdLCUHrzVXk8233Q6BpKtgO_Z-2AQIz8tjGCDVboukYnkkl9TtPPG4bFbps6i5-1nPuR5MeqYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 825 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo_Bd3hfEV0jacCaldz_gSe_vMvLaqyEDTCO3878fBTyrE69GV1qjRiJuKHsfOBjchNyTj6m0XPFfX2_UlqEG1-fjUtGXB-jJYhTLLSxbtieUWc3EYImKgtFagMdmOwf2cIQzSOp7eNz3XnDWSnuwuRKmJSw13xdcPAXca62AkuEkr9cSwoIYllhsVSTEAqCyFB1_3V_edfyHmIEXRrfVTeO69JHV-YW4-K1BuKGSXbSQZox8sKfoV511GPMMuu8AUqLBH0WxKgPORxVmnn-blg53l3dmLq9BiOTAZNJRc1QFY63vBn63VxulUs_9zb3SmJ8HHRHD0uX2UceCAJcQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgEf3p8WW4mgyQClSKZIbl7URg7Vyple8I0YhPACFME6ODrppmdUBIDN9ClpSFgP-YmL5-oYFWvwPwG13W4zYHEtJPwXEOdpgEhhPeT83xPa4YiyF3zB0M_H9do-88mHNtEWGgVqvQcI9qmao42HQJ9l4cTjN0-HJf6K6IEv8Xu5KzVNMWB4f5MzoYQ05Z2Hn_foOSH8APhMebBOVF6iWGXBYMrRtfDuGTno4ZJV9j35gzwJw28rt4bDOEtgJVF4WXKuD8wN4Ks7GAhdO6ukB9I6Yve34Z_949uXgxmmYxPzUOHEUbnl4hoGPJxZ90JhZfovD-osRK5uWoxhpImjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTVIlIaz2O3USVfFPyDgkb3hKxKmaCPNrJSKGsIUZqDyX-43FIdnY9l4zz0fpv6ik2ozjXe3QKwKVG256SDI3mAcvTx2St9S3n50Go9No87b2E69dBY1p4GyeWhb0ZQY7e5oUWfAIwTpz-ywcJ6twa-QLUe8ARP0XTxsxWnJlWHILxHIKdCH3SOpdksJ3pjq6F284ahpwfd3nbfmY8joQiLQqp7dSsp2E00o__99dbCY6C2HHCT1slbWpsEu92xu9oC1qP9fJJNYTkk776L3qPWp9NLrmry0gl5nolEUYoNMmTIg666bALKuvJnkRm7Id42gdtbscQy45ZPOsSGTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abVx48cFM0Ua8JGplmclDKPh_pDvp5S5BXLcniLzRTlIefArzyj1zt0JF3p1PfdHh6A38yS4TXM50yPYq7ARVU9l6RNMzcAjk6nbfNmCCYBnIRm5MMOA9cPt65-Cyoln04QIk7NAWUkcCzpA77wVL_5cR2RCCt8_hVZfa-p48LVo1cdNDEK_q10Euj5we8AMPqwMIKp3p3i4GgeIMli9oWDzYKsSvE_P8UIl5282ZMUvfsaZjC9O0qH_sYBqZgdhzRNpEjlzrJQdOsSC_Qiw4z_nJAMZNx0Z5lmUkf9TwdFy-65asxQiu0UZa4K7PrmbE6XYr4apa4rFGBfRYgks9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyWW-HDsSt44tJ-CoRyBlC3sW_uRBLJPWpJ9h7ISd4FzdAj5Zh2ajU61KbNpDm4DQ0O9QJ2iOgtwP3FMKKIpVrGhLhJgTeK04rqUan7rpH-bEurOxtn3Y0iwUiQ4XgzCyJwfXLK5zXaYF4iEvOmr8iTJdtfTJAHcg4GCl8633kbBycneoQej3CgD4jIXF0oqNjl7hHsONIjgCwO4RzplTwlOkiihTuFlMyPSmI_j1LGm5kPabn2qWOdriMPbuxVzCCQjWyJvwg3c3Sw3fU-u4WnX2tcvzW-oPh_8MkjJS1FdT6wnnQGMmpoZnNqDh-R6tAi_yFomvRk_SVTPHWYXuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8FAZGJHvdsQiwRzq4OVS4VjBqoWfbzAQgwRa3sGcATkYrn1Rw8JL0EKs36lh_CVYdvBrK09sZPs4Gqewbaf34g1iaatjy33dBpZ5ICHx822Gt5UC3YZEfBz6Yh11YkqOMLHJADoZw4tb6ewFxO8IlXgoFEv_ivnzDfuWA6a9EI260iiDpO6_TWIaVa0YrvPvntF8DnvkHTY7QU_txVOeo4IyV1rfM-sU6JOWcUUGk9th67pfLbawOzlTVFmFZM4A5xZPIl6kAOTYda0Lf6UKGskJmepO4rXjfrZl9-33YPJTJPgbFrWFJ5FC3AwiWAvH1t5mlDMuZbE_FUuyJrN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=GdD4CvY2zzbmc5rM9skkA3tTQ3StmlEkvZGZzBjzELk6fE6d5HQ4xmSgrDU3ndzxfmORIEYJnvqbHDFciD83jvokV6QRhGc6aZEz7ZAp6vWlumYlzu5W8u5z8UyD6GWEXymZVPs_PSLrunqtNu04lzbvc-xbAm5LcMGkS3F_gJK3PTxefK7gEQkSrmrEGL13nWeoEd_BZlxvLDzTJacEfoSFQw731AWqNAL5FO9cZkcNaXbYBOEjTO8YeA7NMcN2y6rZQAe1Vnt8dMpHsbAufAOc2Kch5mY88MPDnm-AIpwItPCJhVKNvKUZrMaIU-nuVaMd1cGTTlEdSQNmrNa_Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=GdD4CvY2zzbmc5rM9skkA3tTQ3StmlEkvZGZzBjzELk6fE6d5HQ4xmSgrDU3ndzxfmORIEYJnvqbHDFciD83jvokV6QRhGc6aZEz7ZAp6vWlumYlzu5W8u5z8UyD6GWEXymZVPs_PSLrunqtNu04lzbvc-xbAm5LcMGkS3F_gJK3PTxefK7gEQkSrmrEGL13nWeoEd_BZlxvLDzTJacEfoSFQw731AWqNAL5FO9cZkcNaXbYBOEjTO8YeA7NMcN2y6rZQAe1Vnt8dMpHsbAufAOc2Kch5mY88MPDnm-AIpwItPCJhVKNvKUZrMaIU-nuVaMd1cGTTlEdSQNmrNa_Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_MXQEqJIUz-rDgaA4smJTzr3dgLYHoLpwoirQv3NVvckVhhgDlF9ESoqXK23cGO3jIEkmWk-N_65kr4KqlPfg1pmVJ7LF4MILJK4Pf1fzSuMtJ6Ru17wdYehe7geXiHqsamJgCIVogIK_lpWk0L4nrCY0r5wCq-A-rbhLQQW2ZnsCReXZ-6VMIwvlPv0LzI9A513IXt4hfHKoN_67aVw42tO7deoNtsIbiVhlEo15obsfGijnKwmaL1e3NtrsEOWHBNi6k5bmNebI5_j8Wk7BPrCX3BpBHunoT4G7bO3P-R9rCp0MYECoYkrgpaYpdjKpcMPOZivIivHVWaFkbFoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfOH6Tlw4GA1r9W3y7p5Y0zAh3m0yVm2FQRQTXfy75p-oORo2O7qH0Z-GLYgTy2o_opzS5R5DZa62BxfWVPd7NXIEDPk1Zfmw75osLCELsOSJ8tpbGTjBZdPqZUdqBHJej0pcoeCRd610F7SmlpNJBt8CQUD-HVJ23mVHI8f8-CqftyGpnIl5u9rA8q6G25_Uf8RpRBaJPF-zijZmHstPP8cH8lQepHlCHx_16ieGTkOQ-SEaIIKSX39axAJIs13RpwCJlK1LcKmUsdhpeQsVZC4ki8d2ay1ZDfBrlBtyH68Nn4rhukkGIfD32jaO_Dl7cPPGeXRONJ-iyOMMTrelw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwWoVtZ687GOw5VMLU5AquIA4yIETwf-XHHSaAnpmxJf9yYTyEd21lF8R9aipUPjVC51T8rj2P5nrp37k_OpPwfO1hgsrgwLEXzqQ_VnXl_bm10FDyslNxeZk2nb96SG3lRlcvd_ZIjJSetvueVPtuNHGILn6CiTTnPn-AtnD8xb0jiwDaR9csJ7312YnS8ypB-1E-DEfOqAwg7sdEvQJTPgAtz-srorSo3p42-7wvMtNsv0VrDb5Kn7S4wqAmGIztVYRuOAGxg3SWdQQHK_wvy9S1J-F91DRFv_Zeootfn7CUnODI8Mkkbhs628R5kGiY_7s-RcageaX5rXgasXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGAowh3GV5OeYV_lpJ88KAcJdNOn39Z319bapuhhZdHjNgz2fVPphp_5xnYcI9rPSMi53TbTDa5P81c_5CCA0uu4vh5gdmCz7zAXIVF4VrfXePM90fnfffAcgZiWKBCoOFGgvZp1C_WgtKb7my5FmmWYR4w0jiI5oSbBDtxMoYTvGy_0fB1ix9h1czhPlhNeJ_994rh22SlD_pn5TFynBVrnoUEhLPe0xsx4tRd7eURwJO6yqCAbVWeNPlVus5oDJPOPI55EUqQ62_ofNJbWhocQasxp3eN_GKXce67mQPML9_X1oq7ZWksOJU9lS71T6wSgjKOwmwcQv_7YzC6eBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHgM3enzgXJ8djc0dzZI8KO3Wth-njz1zm9E9_gmVGIFK2U2Ik6QZRa6nR1-B03fITKO4NhRPUstMd8VY7qvR6ZutwkcURSyLNyNzo9xAFN5eJTfOczxr6EfY1-_4y1blILdtdxwBu4Z2V5oY3P5elXD2nrhdHXDXaiFtaofLOws4gOJAzR8Y-NkOGyXl73m5L1ye2H1pkBCw9ehDyE3pr-PM7iQoqBYmLb_YbMrAsJIyPwQ_g_A2ZloKMBY4CvjXvLWb9pvwPZypL-RzchwvKDYYIFGWkNFOHGrWuIqeUJ9kJ4Akm9vm_sBCL4UUDRjrvyK77-iHhjxEW7-jwpBjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoA0bDN_ly6jYAPro1thNLo8m7c6g58-0FVnLWcLFXiIuQIMEl4jRqVJxHLcjU3vAyZ-ZcMspYOdqqUj1VFmzVWg2B0QAtwINzb4iYirs3LjwvFLt-KZHvQ2CE4wfqA22TDWK8SFKPxXHgzCUJCwqCKW-KxfvXIXeZexd5JuK06W9TMt3wJUrNQng-ZOyhiyU69vbDm6Dx99STrQpvDXSGgv1cRnBkHQa1H1uyoBIWdBSo_B0wNoxDEXMlgqGZQ6icegosyOy4SybuLi2vB9ZqkoxDQxtIO-Y5Lqx671J-9dhnVCTXcP-ZTtotn8sLmGrVjdTjHqCROpCy3p_kFEug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7xgp3VKJfgvs-fHDXL59fnEm6U5qnyH5jrX8oekIAckFjVvtMfXDmwoIuTDtMiwiI7z3fUDYjQ62P0T9pQtJmNlSLE1ZDYOtA0SblbR2gb8wxYlgl2DyJSN0PeZnfOJ8phVsz0D7zuSe7ZLdjQXjwbuHAW3--T_Ip2Z827v727hMnJ4BGO5w3q3oAxkIBjHyru8kSuHiAR8Xar_ztg3FGzCqHsOuDPd8pbEbD7Xy9UaK-So4OKbiLEvj1r8d5HWrHDrllmzS8rFYvMUD8cjk8euliKfz-lYdHBY-idiShjE_tloCSLOQmzCPcR0g4sQZhBjTtvY4bafOXp1orC75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vbm7WLfu_7jvBTmZY7E_VWSlwbd5U17oOGL6nhH3FXKREnJThB77lPSnWZy_eFEuh3Swy-PHTe2xQUNFZpkT0N6nGR4SpwmMeCeakksg5gnWFnTh-949DAXF-nYOrXnY7rCyTnzw-8zKh7eVdpRRuZ3JTDjUT-b_XoGyCkoDRmJac3nz8h4aZLnTS976ItLgDJH6yHg4R7j4m5Jqv7xvS9fVU3b5Gh8kQp_zVSKlOj4Pf7lZJsoeXT-QwPtrN8gwVru9qJiZ7WWEYuh2s6G-pIiwxS3UdeAvMJnMEUi2E5x_mniNOVizn5hN35mZzS3_aR6ZgPn-6dYO5hacNaoBkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl0ZC2MezOx8cQAONGEXDOOlASeuNimokgVDa3eFrBSr56NQTTHK2oAhIQ_CqQ6VRKcw8jyZgYfMmDHF7uq7I59Qet23r6KVqOYedt-jeWOtOT5wlYwAcULvsD1-LItVhxTT_v2XZSJQ-NCRyJHBixox9Lv1jcWXWTJLNmKmaDUN8dujfFjctB3a2Fcx6vx0EguCEDcgcoVaDpEkFDMBZIK2ij1wQ1M5t7h-ziXEPyEmFjBw2estoTFlME6MGF_QHBYGmnuPWlQdtIgxtJp-a-hEyvIl4Y2BnSPQLPJaL0WwJg2MBtQNGg7_EzdB4lGrQJgYtqhOw1ugrNdER0FVYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuEQWDhi5w4WiQdv0fZr2vblhnnTcmhAlUqqnOei9N3WV0KKcyoLl8SVvWVR6fqKdTVYzXkcIZsnkmmv9CJsDcLF3iXJDv_uKAP8dGI3oTpFljKncsBVMQ5LJg2wkp_rXcGAaodU81HfGATCahTJZ84w5br-wqJIUYLfQ9leQAlrrR-Ma4Io3sL0GDpgIPhJh8VVbRz64VocSVxYE-d4n-lQS5XMSaU7hUYw1Cqp4RN87kCI0xAzsktNp3dTpFGs93ZbCtR2562XZhLtFMQp2rgWVMR7hfD5MHDV7Mw3Wke-fzflrezbOU5syMhYuOPSzbn8iUdiu2jOLZx_2gHD2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzRdHwjq67NeqovODVgcf9A13Wc4BZeDURRm5B_gVgUQvGnoEf6b1wDFlfJUSEgLD9UT11MCCR69zc8JOmel2qKxapdh5deH7PoA_F_9GtOnB6PvA3SwMol39zWzg3kfMqcYAH83qoTctmKxn8ploRnlnwt1xORkhy1bcacFNCoA-51ynbiARgyDm8-q3zRIG_U_CD7-kHS_yZipN1hk6XRhSABHO_iz1SLMKebEWsUyhUXRRjfLP_cEUImtnfWE99PZ7numaKOnexGY2lhCU0NFTSYd7k68ByiTz7w1K4jV2BZUa5VHe9IkAXh0Fh_XXbztHoZCLQ1UpfGBIs0Vcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIIu4JyyGWvBeZgag9WRs3JTuIoFDCJNNiIFL59NKfUBNTVG6q5KtPqH9tg7AuWtECOHZFvoZKefzNCyACqIVIMj2oWMcecGdAO-bhGxN9ZqXCiga9V5aXDp_7rS7nTwb9JR3TbJsN5ahpBX1uNofyDOa2FCq7Z7e7PzgK_aNZUOqDfi7TyHoLeu1WqD2D-hutJtaHRJ9MwEDYuzpEkaX-wp06xfxxl0VCwNVNkS9OUQA2O9amM5KZt1Z4TY_R3VcmMTzmc5OL1pJTgC1P7csbXBhLiSn9QHbn50ct06t9-vlg_gQ8Fp0UOFXrc3E9s67hA866mDvv9sLnRq0la4zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qe-K7eo48MGRzruzxauUWWEPI755hMjRxBL5dJLG9VLOIqq_3tbe_3eYc5Ok4LA1qArmT-JY-gnCa3z2j9NLzVyOLdeD6_JDc_AkgDmQxtEF6D46d1xeBidnlkLnrtH8EusQi2XG4jcSrdlSZ42aVQ4G169djFrBpd8eOHmyX1DFYXSX-J5QEs1V7bin4QK6BMGiTszTmPwDrbL2QV5_TxrQ_zEwH3IP7MQFcmouqkvdWGi-cK4A3PwWoPsz7gAzyKAAQf4NUot-2xkIi8s8YBH-IW3zJj5xdDhsJknC0wv31e3t5_E-SmgGoLZq6jWcWy7n3SRMpdtCSlUtsSt7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-O9YO6ia8BgsOSZWJKLgGjKd24syqVMc6Mo0oDRbBVIcyXPp1AlUnULeh4iYGGS9scUiw5gFDmCOjm1-rk9X8Ax_UcsAozwihLcDS1HYw0kw3dhrWJcqGzvOzSL1Jx-TPjxZ9rAw6knv-P1kbJ4q6fiMJvNnq9R4WKLcY6btKTGJ2TSyvslK8kJ-IsdVi4E-VCdiUjXLa1LnqQ8FLdMKxrb7Z55Gjred-QeDkcjfaBFjFYV0zL5tVwL92td3I1S6W1Kf5Gk-s1dMDGetfh94FYPtVuKlWOvW1MGBq6v5DDCFjxR-ec1773cLT9k-NWeRMhGqmVlD1t84B1km2fYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZfwb-CCOjejam3IjQvn8YpMXbAmNaYS9W9NO7PCMTw7Spa8ppgYmFG6CoVF_sCuhqF-KSZ5YZU0_Zou54RcoW83SK507nJ0OQpfTCXBj6RtH5NVeVsodaCyMYcGcFSmcAsOzdDRLYeQPKPP2GOOsIdiGM0OXwiinJuLYjvQ9Ja-PbiEuHG-utn43OMlSjthl5QX4oUAZ7MKFz9GkKBPOC2z6QZpXOEbcB6GWcnOtMYIwy2WUxv4-Lg5gDeSxtYqZP220_qF0YeOAvzTz_QIU860aXAwy7_GWvUfn6OStNmhT_CfN9qQQbt-fa5idKhpC2YW9XLPqWYASyHqSvS8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REc6BtrKTn7bJnrcA3UAUgIfM2mJClqUE9BeWxpUn11aP9a_hwiy52Ts_OybWPgXzA-NvZfRbfaEQGnEqjf4twZdQC92z05BeuWDh6VOSVh0Gx2gvoKhOwMjmLfxNgKtd5kdo1BlftwCDJJjfomfpAPEFqEwZllSgHrPm23Ft2kBJMaeSDCmm2jXghAtHfxxnDHvOJQtLJCjUye_reADrWKE5bYMnfuM0W-VrxsL0rndgptnfNVUJhe2RPpJeGlQm-PO2apD0GYTtSlXuoIZCOm5KtdQb0osUv3x6lxg3kOmTRykcPo76HKDVU8vzxxd79fgSGPAZNUCvREU49GLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amtz40aJFqwq9i3PONlOXl5xCtb6n3nTiYL4JUKk-4nd8cttBJGOe9tlMTG4R-_LXbr8piJD4f4LOjQpd0YFxgJq-wXGd510uIbmAYC2Yswo9Ls66UKFoFYXnfrwm9e85yGNPbrmR3VmYsQCKWxhbVwpAVThrzR3WT_aRW2AOF6r1WQbO5oiS2-l38eSjj87F1O98GU5F1f-jQgizhsZsEgPYqsR3E-sD70CFtCxUdmPwkNvALCOIDD4q1Y_NoJcXbhtBi0c_5GDEIwNq2eYLrbrlMVkstlfrX6y-MT_6foUQjr6ZftmmHKL15TSVolCxSmE5Vqzge-92fMewiWxPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heNlBMFpRHq4KtbqWWS1qXgQFJdOzzy3gDe28mxFIzAf3hoPiMU-2AHCI8FhMTDtIW6dKNvgllTEeACCa11pgbI83ypsnGtCFmWVkJaiPPmiItK1n008YVTCpoBPCkQ0FfARiaUufnL96LanmeacLDizhMo3k9RSnjPBDC6Jf88w0qrXIiNXIo6LbIzdixla2N9Bd5qpVpT15FOwm6ukKM1-wng-vmImM8UM2KeIdgTg0gv7_6q7Lcuf97VlqgB8kroSoxgjtErIBwZ4Ca_RE2jVbTcZg-dEU_-IKpDtRsOa0wVf0668dHe4Bmq_EqQEH2D6-8q6_1WH_o0mKPpt4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm7texRQJWU7TPyB2cRgT-qQRzIOfb3hkeQcQS5fI6FCDL9KQRrRWGTX_6zz4TEKxgyz50VuApIwrAPftHV2aajy0-sMSIh3lDzj3SF7QmrWd-8rWO_TnNAUFIhKBdjLHWfDmPThp4pULPFfctDzmHf_ZniJexgATY2bInwQXMKXQvxlUWuT0Dpx5mISh_HCv20iwlrmNa6KkGa2z5tLhbplBf_ZTqxtf35PjnKR5civ2X8ZLrpYOUdD0RN2vGvnCgI7a4cIQczdXJAaeW94JDQTyBKNfnJFQRNB6J-S8purV-GwaNTURAcm9NKN_q5Jrt1WbJIlmRM5rYCzPagKAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYNRboIAkY4M7bQSAS0l0DezSYNl8IZHGq0Upeeruq4dQOHOY_5nQ2gGTzxXy2gwl4n8NLdPuovzPY0sgAau9LFCwpIrkF77V8uCYwWTWGd8rySdSQO2PV8lKrWVclizxHKpNsXxwdkraKrxoJIgI6UiTFAeqZubF7rBwZhRGCpJXnkgx8Gu08QRdOb3R203k_Blt1iNbpojZYiaxEzEiCWfY7j1StfUvdzdVyKkA53Q0gQa2TFMb2KbxZXvQry-o6x8o4Yri-nuaWFhnMP3ru9fE2orepZdrMOxpAHUUmdeJVCmbaib7Q0sFF-Ww9w5luJ2A-SPlRdUzWtOaqWHMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDIRN_3wxd-K0CSgHZekP2le1ripXS29DH_nT8Vvn-ONX9Qzkr3NEkS60X7-nraTU-bpcK1LdJ5OuoCQ8wSlSonbBrJXk9ic1fzIovAFs5SWjVfDfSI6aWIuosRelA1XC4YXm_CUDpR-UQTDYJJnETPchFXuKuZoz4wY9zI8uelZzIybZgDC2w9fBBjD3WLIb5UgLC64pQqFljgcTCK6jZZWs35lccvHd6KUHxxROSUuG0Y3-LXnXpcTptaqShHVWTghsVZf20KTjhYUCPijjFVUx9VOkIOnsvrBoAtzZvnIWJYbnyQQKeDGNzg-oNGlB8YXsDSH6MgRS903bqyzZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ZFXXLfpmw7qYYSxcDd3skB7NUTMEdYj8T0oYS2lwHhv8H1vftkmgAhX5F9JXiiadJouKMIlizpgm8WJ42MsdD0UeNhTnXuSBDVVu42bmtdyk8ZGbjFf2dhTyQ9uTI1K33OlLm-Mr2vIAQ1KmZpi-jqw1-tF6_xWXxCrGXt5sDGjiO3CXCB2_E-J_gRIlQMTtOcYfQfNG194KBjMJMojgjIPrtXDwXY3CiW0mPblEnpeyqWcATKUHAqjnX6l_Vsb7Ok8dA3PH5CRFa6IioK4byEzHY9ugqeTpHiSoQ8bLdt830a3Ebedc_U2uZAVg8FqlE_NZsSum4EH18vPnSlmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUMBxOgGb73X350njEz2-dTmQkIUNWRbGKpux4CEyDSdg3bKauXBBvRbdKCqQB0g5UrWYBJu8l554t_diGpUEl5REjcn_RwOEXUTsPX7aknp9uOotgZHncyyiOdcHnlsv6O8TFMa_ySViKfqVu-lhYt13fcB04o0v1tlMpODLIvPvutBqOIsvyPc5KcuxZFncYBtDsXutD--4meYa43Kl9Rxiqmi6xO2_UhdbhRfibV-BXqMrua-rjjDkyrPPu2ZLhdvJUD9yCF_58G2cr1blWkkrxFiDpOr4x-oH56RZjKwgT2IgkjJxgB_OAoF61Ikz1w7DKsr9gPUEYI8KJecvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atRm6WiQYcYXIOhXZv3a2vNvDIQTzlv6EDH2o8VF0tWYPI_s2IqhPvh1W-CApvNYD8GauGn7sRObqk0BssVV9Yk43eIFk78h-Zol0ULiws8Lt7DVXdOVai1NNyPrbRC72HQXm2gCjKgBfV5uSS-mt3e0pBUqnVZwlH2YUyb9TzKD2MrgsUPpu7MNElsORHyD8Ne5ZuoDEBHZT8YAmmO9y0F9loAEOXr9EsCpDq9Pe2JSf6Zeva66yqGHqKta05j-EIhuVpnBb3itzrN64j31Ho0w0gt0wQAsEQwhhUxjRzpiENH4Af8W25DT_ZYz_hnd6B3uraO8lk-sSiOFMT_hgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGbCNXo5dIqofTPtFj3kvfmiT5rITRT8ublLYH7AA9w_NNWABAKcstjAb36OkPSKTwxqb0uqPTOXo0oJuOH5pqDsxy1UskFUfEIdKf07X_Eu5t_kI7sEIU5yugUw_4v2NnlAr220Q7Wfrht6tvG7Ammf1Qdn3Ml6WlwAgwRiH2EMgcLJalUw0iugbUDHpSwRpa0AXi1sABExmN3Zur4MiqA778Rmu4XFF6BH94SKHS1bnaiXUh4S6IzLS3t6YRaew4GNPOXJzL_kbth4j1F-Q4bxDnWYZP7oz0t7rTUidWAMJnpKmDtLRLa0YHcgaOjkumMupw6SsXHLsYxhcYgOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbkjCuDrQvw-5UqG-fPJnlkAQXUppGFtzfvvqelEV_BJiaHCUWYPPz3BSAdircfbrMHfcoz95PkNHKTbY0cjd-_iLpwqIEEhLoPcgqksnQHlxoMXLgDrJR_ewr_5l-yKvSu5XJrblvLCTWulbOGlcQSrpf8i5Sj5YjV5DqOZUOXwv2SimwVKJ5iqtwS6fX2r4PHH63ZUsf8Y7Uyqr8KnaoVetPsSnew--ZdTbPKPDw6uOITPFwe-fxASX_lypfZm0iMkYZtd9tTCVc8dbEe96Ox_wwkgn6SQBfU3hfHqnh6L-4dSAJ60Xq703Qprty5ZmCcEuhtmpB241Tv57ZPp5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbhOFxPMdNH8L2J0KlH0Uookr0wy49-WXwbnFIg91RYP6XW2u2hu-do6jec-BpLGZuiXM_MoAPtxLUKYqmMp37_2dbv-G4z590UWt5aojW9pnmBwxBX5miyUc7LyJrwj9K_kZx-klrCV1m-dGrm30u2La_MwYO6d0u1S_WkKpQeFvDb8iTEDJbJ44lRphqTUdCMcLHJtZcX3AJz78V87g233J2e6WkK5JTobqcxt6YtwBKU5xPYqpwpAPNYwY0B5zkE-0BmOo7RZdvIq4DUzQqNkb2XYWJBQhYr7AO_yYJmyXzX6D2D7nKv3ptZ4D6KihwLk3SanA4NHIimlhsuuAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLTqrofPiZ2I7yQHSo3V98ABYBFFQCSelrpHK_HAJg3hPgHytbdMltUg-CoD7d-bSxhY0UQ8mwcRPSX9RhNVCG6MTM0vClVeFG78WUBlogViGBKHO_MaC2aysWlTFUJKYO5vSlIBOH7aNy1D2DNUcqk0AYbdKgLGARBKaUrYvyaInwGP0uLVsqfg3tFbv6UIk1IcLtvbv0SgisXGyICiTjnJ4iNmMzP7k92GBcpT4C30fLUGvbB-s9Sdn-AaGLl7dZJfhqP87IU4u0CY7AwmkkGa52bORerhMz9fDc_D1bKgBmUo6ZyWvC0IWVYxKA1p_ZIIf1GG0ht_4S6z7H6-uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoJl2QMFEyatXm60cxAD61b_j5b_u_RxxZSRa0uwNCAtuwowiYeaFy-bD-g-sUTbvHWWedBn3lcYPC8PEZoUZSIGeb0GXXuQ_bnPxdFtCpyPvnbYEpdCcgKZpgEZaMBi_e4nHFX5QoBMNzvFlPCHfMPrAAxdN1Ey_s-DAP1XDFy_IL6Qr2bIBHLtNHdeEmukdcDQQDxo9YwY5SXQ4sMaaKJdenNCptR1EsIIAAR9pvAWqCS1RsDOU9nFRvmY84C3Dt4-CiiaZs6_pcR7rejl3T0yZ7uWDCzMhEiRdoIxQjc0VZBjNm_2nheE7hzUE3YULbBxd1Y2uogpLvQOLcU2uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4OLkNtSA1NxYl3Uj_NIrL9Vb-ZEObdCb_glsfkzwRHmIC0ieTQII2ezdqnj-Wwnjvz0kxSXMFScib9N7V3M3iRPj_o9CRql1Skg9n5v4kt835ZXB8peKwazGMOYiFMi1ztrRlzCAjwB2g1Nuxpe25J8pYxs9XxknYGpVD3iUPDuZTs3EpprHqHaruxgIfS6Qne24JwjGzFsfI6fajRa_4E-VS88uSSb5MWs3uVhMuZhsbBUzstYVBQ4FZvZZaZc7xMUwaFrs9MyDPy7fZ8k5s9DVTCaFlylDzpFGM77UMMq90Ly796toLe3NB83i01HfK7Bd4AvMCMdi2cMIMxN8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrBL56ehtnYMmuX3F0DxELc4RtsmghN8cy5Ufp5pv8_GWYxqOC7TJrPnuC58onXj8ms_sAiSjSg3BY9Rszv6JJQCVR6n5PXG5wPmbuhy9wKh6CeeqmSfMRoILEtgkmT43JI8F_b57gJvAto5wOd4GXhJ5VFlelDd7v39IaotUi3arBHnUniIYZ6Gg-dHo5gbbEle7jKvk7x39fTWlBfJcQzTRvvuRdPBO9TooGmW5CzOLfq2qpL6se2Jhw2P12tJpRlFAUHR_S7S63MXXiUYBluhz4hMmOo2YKpFPGuSt9kA2rM6Ax13JjAETS8h2Ns-KJzMpwPRjLG4ZK6hPUOeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfLj46tIUU5ZdH1B56x5-wkfdUGHIK__mmkAeC2UK5CjC27SsisMrVWmZyUwUX0_tyzd0_E_sCCQxS3ypllpSfYv32u2zEecIyhUSWn0bymbi-9YbZmN7qYpg_HO6B0th9EtZmlsIbnt6fFgLMyc6uA0QkzzVXn7SCnsHzcFCDNHk5TaMkZYehJX46dnxqXPi6Wy0ASlfgoLxvZ3x_tngIVNiks44SBoK5ogW5iltDnfWOBWPpeElhe4LmLs79NlCjx4mild_p3aNAisSJ4DHdzHQG3jy4Navgr95MHzRL6u3ZA3ehb3EQaC6Rp2lshdA27f_yK4caLAipRScQs4KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsi5_q1d0ZAubICPbcbJZNrnELuKo_a23Rx-iEerOuW_hw3_KONJTTWRyjWlT7pUZ3psjDUyNmqTbB1znR2I1t4ORfq2pDH8hnNO1tN8TVKIL1n4aWvv0nAmcD6cp47HA3PNVkb2KQIqIz_fHU06Qq4L8DK3OyPdOq3Z6Sr1KWKtsltDvfLfQN8uLy9dDxX7kZ0awxx7YQgN3hD7XfBlJ9Y1ckyaNFhTd1Xl5F-9IJgjeum8bzOvQGNIs_OliQzv33dWZD_Ky-uAZpqEunr-Ab7TQrFjvtxv17QDHDPSW5wf2fxqVwJUQFwizafrzkDUXq0MhVWfCWDBf5XODA_3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyLOVgur00kZ3s16IW1zmq4nanDzxAX6NM1QVzoiKRtiYu1qMsJ9ud5a9OOHCSNtsMJZ4zqGoCJTR1zp1WG_TmR-7pC2cRpXxpxjdG2mKVETRpQqjT46rng4aWg51W8Z98R6ybvpAmBfWbd6RiAtcwgreOtATWQKhm0e7PndH8p1YgBh9bni6GLrRsezwF6Ejf9SbdY6I5lP57ue9jVsaOdXrdC3m6MdF4aFr7o2QZuWsbyfLVm5M_X2i3DGyBf1IMMqUqTjVjH1Y0xaUBajPWCdgKv_ZcSTkJBe34aRi0vj5zCLBcZZMdO2s5Ln9HlbsPRFPbIkfzSTdSIkkHvE8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toZM-miavImb1ACJnanUPuNE8AyyXM-ImTY0gKQkmmm5DVLPOO4O7ZkCmRCwV3mvDoI1T1DwSvkCFPpnrGL0_9x-d1QiRpkUqrhmJ4IP2qQ8K4VZflJZmp3cIjImgRDHSB9VujOI0pimfikk-3Z7vAzLJagm3Yk5EVV6lJik3Ill7dW4kW079UmniiHB_lz4CCG2vky_TO3ekxCuaIj5SxABa2Tzz1b-Ca9CyTqQZKLie4Pj2hY7c5SwpSnxxgDLIGNIP8mDvQZzf6lAAl_f-ia7z3tSv8rLLXroHxZL1BfduhJzkhtnqGx54NMlKs1ynZ8UDLpj8QOF1spDSST21g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG4tNxb2XIERoig__ixk4iW2frr9DdK8CQscmdHQGR9xUsDzBpi8B_tC3VGeGHUF8WDdq7Cu4Ztl8voo7d0dS64Az9Afg8RdTRUeiExmBTz1M0U1Fa9prjNg-PW-VP_xBE8iz0vNxq_w5_4HwV-KzBl8g48dG3TYf69MpJU6fKJMhyD23vsdJ792Q0GTwuFdZafzOjNY5xIRqaL0SXW_V-hEW8zzDjD2BkE5yedK55OKiUWFnXYeU2yjcvKj8cISu4rPaIBAg7ibaVHU2EVDOiZRB_rMnQSRyRvAVMkj25VV_mNGah7vDwx7J6HCmv8YmUtVIbyLNIDkNtXqXgFXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMgGhGzKIDraGry6HVJQ4BXh0r-OnMRTk2KLQsTvo_X9ZciIKXotkmV19i0RbhIwOQ5csnDTw2q9jknwTDCtsZ9AoCuKIppQjfXid6eqKoGGr01i6r-qt5VMZ2mqq6codpY-0sK4MsfVTobDgYhASv-8ko0G5mNTyGqjVmQ9VdPEShlUafPKte_DIQ6ebXL8V0QGDw1jlVXGp5FSJTY295qdUidGqvaDjV8F5OGjVqHzs80S29yl1VXkZDr4gTCuwyE7z-LHhwLfsDt6Xl7GsilelXLDWuPFDWpW8opBwlahVJmGTYD4vxibt6uqsb8SMPdZE2nmBcSUHwyIf1OxJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4tP-XUhjB_avixJBVPDyb5Kw_nzp3dS64jcMH7hB1UF4FngtETar6RHPPj6LWj8uiXKDFGGC16xRygjPd0k_To33PIxX6xgVXBnB7ZAblSZjEJQio2U5UgzPJK_6ViB75tBj1gKKJVa1mUPx52uJwNQ9nnxGONf9Jwq0vaTCPviH0OPFLfirO7xlhoxFCEzfzX5jCPqRju2YoB_Y50EkpvMD1LlmREzfO7njISlHAwl235f5QuGFxbPTflb9T0IknEqaUZU8G8mmTzgizjKAetCUNoIPuYtLC_k4toiaKl7tRF3EqbSUpPpebgjQcLXa37Rb1tHaJoCUBxoKttIvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcX0lpjjXqHS9eUpY_-eeDivmvYwCRAmkJDDnsipBfbTvl2DS6lmhLN52i_sKjSzZfh1mtX9iyfFnjaL1y0DtkC7Zod9CMlQgF1hNbyYz_78IsYTFgQcPq7Twg0-nmZ2bJEkYUNT6HwWeQqJgF2XB_NApG3rFBStugNbLRY1lhGaNaH_P23nLbbI0bcDYCwVcufHQBu7KxQEYc1125En0-nJqHijdoWhZpOkPoyGjM5Y4FoqrHJmEVD0MpQ0ci-zi_DKjjUsDPAuNkP2k5zxtYRpWA9mNUpQ2GbYFwmAr0iDUNJyHXr9N8-oPGZljbpWBFEk9O8OBZwSUv8NdQipMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlsHqb1_JA2vuREKHj5JtaxN7oUjsLemvgG2Gp1oXQ__GxUNNR1XvDdhAn-qALml9_HbFY_qiicFk2_c1LEd17mtj4ebxcR3pmBPInb_bWaRxa-k7G5OwYAGN9_Wr7yH9oP7EooFcCF_ECTkFhV6tRLpJLYeI9Rq13eJAn79gEGOBC-uoLtWovGGZxAoLqHp77zIQ1pSejILNFch4ouEmMzpJR3-TnLW_FN-LwstR2oszHEXXIN05vI_ISRG0aFUsdMMtAG2XwGknKsmZPTdZ8l5yKp1rJcR2d5aJIenn5utlOyjZpJiHdAPh9q4iv9EsDdS9xxNYWYgczBf4El59A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZwSKoJeC4k4PDOdnDgUwsM9gzhcTfedMwK6L2cmSWAt8NMKQGxxuJkymCe_dmjB5VHPvybVcHdMRVHps8l5g4jS5LyYFEYuxmGZBsjfm4-pQ9XNebQN7opwd0CXAbJHGyLA5n62ItTIRU-zaI2Rc1pAlRJPDQWC9GDbGV9uQCx7axwjPaBwYD-xiSp9DWSB9Mx0dpEryozYZXzEk4ecWFYZLlArc7mJf6dRsELQmTl2lj8BqpsAGOtvvHz54kU7JZ0XH-3EfKp2IsY-GJ4X9XtTO25W-qcVeGzHAVlCQgWaCwx56aJBhi4_cTPhEawSGz32_ungTqthrEC4ACqd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ox4855hTUgjfaGmPx3Lhp0A29f5DbA3gasmOrBkqYgphMeOGnVdQvaS-LXIk4anL3zEYwoUwbt_MMRZ9xnYscK5-tiFzzdX7HGHBhYqJIv2OuguZa7-s0pvfP3j6yHmFwCU-gEJzo_WrsQnzZsKiB9S9fGdpwgvnuwGoTMX8vEyuEPRg2xl8Oe_sS2uMWAK94H_iRezvQ1ds9eZtHedzqWge8tOj9ZKtXGQLhtIdpFNZ_fGmbYUXch_Pc0eqjZtsBrr2hM_YY23BKkN2w9evRK0WEJ5m47jhdf6wF0oXx49KGTCE6AyKEqQVm69Vc4m605SRKEv0hC083FLkZ8b3sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlZVQKC1l8MGrI6t690xuQvgF18swiPQK5AbEgy3NJql4lPCs3tbm_CJ1yz6-sqWDOo5yrZ7lph8RmzPCDFyBpduIOtAEBpcP7K6irVJ7fcq-V4LfwLSxIPH6rwFmpyMTYZ8UvrLNSj0uTW9982LlKt_n7GUaoPIr9D-HTmvrEqmlAh5l--dTxljGMp9sGU0Bw6KTk1XO6gxRmfk7ViXMpRK9WmEtC0KGND_I61RBQ07L7WuQNUDxw0XNfvrjXGMXeAYsSH9MkTOpRsG6_mpa8oxyOar6VhWt9jybBc5mvTqN1J7ZBLaT3uH8LTecQRD5aj_B8RHPOZFc370qjXvMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX08ikGEkf2aWF0a9FkGuVKV9tlYzS84aj7x2WuGK6og5i4qMvzP2SUbnWunIt5F6zVMYMlhb00Pqjn_kdJySU88y1Fs4nGT_UMNiw5jkY32Oxx3I25PqbJbDUA6QdviSFg9LJonr48bjw2Fb_xatvAoWuDHOfxI-daoc-Znx5-9c8QAQNv1dBsA7jM3VdEpkVsv1TCqFbZoTkZ9CXR1-pfmcNnVWHJ0oY_TRcxp2EDdpcBIwBd2ExJQA87-OnrMw_EuefOP7oBBdBTIzcuJ3uWhGF_w1ZYZGnTeEDCcFHWzvMLSvnft444zsXI9AxMo_Bl5lUTYvhGnYLdq4-CKfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNE4Y_sT9UmoP482Hlem5j6kTHOa_Y499pFljGSJ595KTUGm_Mg8El3YuYY1vLpKexs2Jo6xQaoxQW2xpMignJuTaUOcNKcV4RFC63GB7WPczMEKbYUNi7UO43hSNH7s4GHNc4jYvtRu5ZqdwnKcCXLeM32ldLRjOxljudVgsK0UFKXCFsm7SjHHJ_yHa6LlAy6fT6MlbMOjhE_8PEBFy--HuDVkodyNDDcFd0tERqWRH79auyiLFQZ34SJk3KCFkVX5Fbg-lPzaXH_JHrD_Bpv-E8C-BRPs8lUteqpgNA8avi8yXYSPedbIv-15KPuwESRY_MHb_hMKSnTIdTU3rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNz-ftuufYmsspK1UD3cq5i9_W379kf48emYzrxMVXFcU8Rknq8HgKK-KvCY-ZKJmEBsk7tuas9tUu8wEg2hqgnU48ZWWRU1_ZtyCDEc1hu4bQymsMsBe9kCvoX65x-8wwR-bml96MoFX6i89AopTUsj2xZAq_rU-Qf_xRgN4vIgMPyuuNMHdj0IYN9isTWlS6FSpsDqnSmteWeNmLW0N9UctXYXJPmz9VW05Ek35QGhl6lAzi8baEvBUMITT88iTkc5zpx1eH2ENviAPQKfsJKsIHDCSVv0TVxgDBjc2WHFBYhuX4SlfclfsG98RLeXHM--kCPo7YjU-2OB6KrQvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=pTFhmE_hhRrTwEJQjGgWl3eTg14-AG9-RaxLfBHrN2mRT_1_fs_GdcHwf0htF1R8NTIf7h9quBq4CyVmucdoEgpq2d53wxOQxbbBIbz3zNqnYsVmzFzvcINsM33gQzIE2gSVb3lwjAhurAWbUKMU69xjNRKQkOYdJMztIq3imooyJ1LL6QGW0L8tDwzIvsFpy8Ik9XV6O2sIBsLUCCbJ15aZkwLSyqnGNxVdEeatVM0Z9Kf_GPrdm2chGJvx0kOVqPNs7V-Sbj-oTIuZfBpVzSQ5fa2ymOA_VH7gAu-8yji-6aSxsfOt5EhrLbdBjYg-IPPTKtUwcvKk2mQojx0oAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=pTFhmE_hhRrTwEJQjGgWl3eTg14-AG9-RaxLfBHrN2mRT_1_fs_GdcHwf0htF1R8NTIf7h9quBq4CyVmucdoEgpq2d53wxOQxbbBIbz3zNqnYsVmzFzvcINsM33gQzIE2gSVb3lwjAhurAWbUKMU69xjNRKQkOYdJMztIq3imooyJ1LL6QGW0L8tDwzIvsFpy8Ik9XV6O2sIBsLUCCbJ15aZkwLSyqnGNxVdEeatVM0Z9Kf_GPrdm2chGJvx0kOVqPNs7V-Sbj-oTIuZfBpVzSQ5fa2ymOA_VH7gAu-8yji-6aSxsfOt5EhrLbdBjYg-IPPTKtUwcvKk2mQojx0oAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLyNXzOSa3ew2kMZAGMN_EgOldnUmP2D9aVZo-hdeb9y_FLR5SzXaB4WMEylSBMxT-UJo6yk9z2Swd-fPrHZvjQs_tgoLZdRdenhWRQt7tA8eWvsMJ5PwnRkcScW7eEVGlWJgC1a6gH7d7M-wqeI6_VqyDfXbq-OCnu1DRRnFhmcMZKc3lwlnO9YExwlt9LeS0F5mXUAV_zFfAv_7YoLStmg7ew5J9drtHR6zXkADGlAJ8icd0Qwww1wxiBv9SzAQrmZJXciLCcPLle9Wm4hk3XYi1j1kGWz66q8sOUd1taT7RdcU_mB7bexVgdcCquFxvw4J66k83LM0d78z2PoZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snSuw7AO54hwUBeqdF3lEXofLkE-LSUNvbnJ832UpVaeNZeZB1cQ5ZoqiaZPG7faFJuP-urhwtK-ihPQatr3PMDlrKaq7L2ioDA7NGboPKROyXDch6bz3XDgPtP0z6jXunktsaoP7fGbAL-oDKlsXPNUmFSC0YZCL_BuhFa5xdyGGwd3nYAZHgXuavXiT1MO20SSrIizPrjmFK68nlbqyPq6tBQxgdzlHKeVVkCYiu8hj6Dtt7AcLtp4bulmjNcNIQSEKqm9LczIF3xW3FngaH0z-ezUdTY4VGOHgP0xNymolVM86I--CI__GvrZhwTx4YEJgBNy4NVDNPAt-RmyQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEv6jGAnv6DDAURMAFXiypjr-RYHtQ2kl-LlloRf_I_zsxs55fF-zSTSA3TwE54-ethE2CzXLy3FxSu7OUk1182PMQ779KZDZuSqDJdbF4Qes1qocv6Ou6aM_swK5wcizCuoorYvixIAON5GxVswrxTeSUiCrHdBGN5pSCv3i9BWwgpzuOzxUP-1ywaFfuGbYLVDA7EbxmH7DVXKIC0aEf3U7B7Z_5X7udMaFyonp1HFMFTUe2JrueSjcpRYiklZKV-IESwUUZwkihcNYffC92kjCv536_G_kgevpgIM3e_4rM1KO-xnsThlcK_lWUiSPttAx7si6q53pGkdD8Q-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cy1NYy4yzPvz7ZUwptfKlb1GYKK84cUhzmtTqoNyJkx6TnfqtegYCZo0cBt-wyCf-T1Ek8BFQ4pJ60vKIGmHKJo5gJZQ5omau1X3axM3R_bJ84x79BUu3U6rfjDWuftwzZmPtIdxSfKJaZsisngVx8IYDyLwGanv5KZW63Jp2ZtcXp038gsVbDZHg2Kqfcl0bPby_OdiXvhWFgF5I0AY-cRqjv3CGCqwbpLbGCOA_qhtWlfMVYSsvme4Jj11WEAQ76tk8TFJqVW4MqH-5yr5Vg9xNEQVmo4ZXwuVdcErCe90Nt37x3gapGcA5p0jlYRN78is8Mxwp8JPWKJnunZp1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyYNetRyDK7PbX2DsDrqOGBivsTzy3SJqihe8LUMCrlOU7NBCP3pVGtG7FmQNqZCc_1Fp9UN52Llrq01vJ2Hb8TbZrnJshnvLkkB2_678TnCuake27qA17I7rpz6pzjp9b5C4LHK4JBeniBfTb0zqAR4-TIPifZ2vb6QqfEYN2CleoMs9g334pUIyRZply_sAigmx5H3yivxJbH5rzEjr4O8r6233BRzrAGz2rHNYuyL4Eitj0l70ibzycNJgPKOSd-SYbv_QQXJZBj8E-qNAkisUjY_1SexvSa8Tqpv2sedCiv_vlm0xsPbMz0oYGdquCaTCATfF9w95CiiCgu2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vc11XkFgl9CZ8SPdSlqRVOAgOQ9_n93GWMATOy2j2iqvZwJpiWOq5b-SoHJrvMfvYytYmMwg1aQpKYfe1pBWG2MzvzCxLa_4qdPNU6COOLKFCxykbqWihkfyqCZmOJ4_qfPSVUsoWA31x3SeHSvtnfkWh2KCsk5Bh7_zcDgrRmHqzlJAH_azUKLq0RQbX119IbiJFvErrzSoIWWm8SxJEDfS3dGlPi1JyDOdgrBi7EIxfYlUDbS4ZwM2zRrC-zNoRRBTQqy7dqKnzinfINwfP4O_egI2_BPLLT3ufspEG20Ds5Vm8Lf1O9hkqHpiHTMHBESomofsi-izsLqVo1Qn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7ot9hhGuDEMQQwhriRR4qz9QIWRVHqyjxDkPcB5rcv9woMYqQ9EkkayoqTvYbRXp1davELaUWFJ_2AnjdSg8aLwbC7mUPkUc24552gqr0TS6zm77MCy8yQumKoghM-t-p5NAblTm1lsYd5iG4JFmpMYdwYRXWQPUAODFHGQ8hhzQJzxUHom3tK5Sc5WSehxGVPd3s4Ba7X2HEfKDIIDBOa10ifj3cz6f_Gy1RLfPj2-k0t5cxHK5Zeu1oe4WQDEMdRmH1cxssogUYJewI55r5SDrnzfdM6WGihuB2bQ3gLthAhkEhfudhQ2cFIo9mu995T4OWTmB1wtjAFM2KnlRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=SRbphChOVYeBJIGdgOJZql7FS6lluftR76cZo5JXShmpcc3pii6lMZPiTtCWm_fUjAFcdvdkvaM4znZLr2rCLP_OtJk_EGd2ml1i6VJRm0BevBKlPKF36p98o4SjzJZ6QE0RL031SFOYQZhnF7gAJWZgeWlj2-phOi5xOGe4tnM1XtbACKoVyzS0mNQPI0f_Yg1DgjKacrn_c3CIW-qlTtq1KUazAudX5MgdhBzhGAqUrRMDV0KdBS2s1s-0baDLMIvHq-Kl7EPujfWGbDlo-bOu1lQ9YtCbi-S4wVz4KaTZ8g6Tah-hud8mkF76WJxqdoyZ24SEj4FV-kNxRInnjT5Mi7HQBqhfZSw5YdbFnRh4WSmizQgl66oifFSGzies8CJXbbyNUBeRgcj2TU8TE9PPT0hcdd91VEdZY0gjfQ2RSeqlfdUGw8hQRwsVpgzV_Iyple2nOPJ6iXguIXjJORQ-lwqE2N-D6ni2FZbaQ7d3ZbAj7VniSGPuUdp27r7X3I92N4FpbtwI0n2Dwof8YHN-ITjEACpe6Uv-_zyp-_s50N36E7jPiIvHff5HIP--zkocOnY1R1CnNbzkOIOJ_J0Lxc8aRrOQ1G-oiT18BXQfrkzJ-ThvrQB1PSz4NSpNUBCXrg2a0hQIKt2y_ANZHF-xSvSOSw4pg6c_wUDL0Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=SRbphChOVYeBJIGdgOJZql7FS6lluftR76cZo5JXShmpcc3pii6lMZPiTtCWm_fUjAFcdvdkvaM4znZLr2rCLP_OtJk_EGd2ml1i6VJRm0BevBKlPKF36p98o4SjzJZ6QE0RL031SFOYQZhnF7gAJWZgeWlj2-phOi5xOGe4tnM1XtbACKoVyzS0mNQPI0f_Yg1DgjKacrn_c3CIW-qlTtq1KUazAudX5MgdhBzhGAqUrRMDV0KdBS2s1s-0baDLMIvHq-Kl7EPujfWGbDlo-bOu1lQ9YtCbi-S4wVz4KaTZ8g6Tah-hud8mkF76WJxqdoyZ24SEj4FV-kNxRInnjT5Mi7HQBqhfZSw5YdbFnRh4WSmizQgl66oifFSGzies8CJXbbyNUBeRgcj2TU8TE9PPT0hcdd91VEdZY0gjfQ2RSeqlfdUGw8hQRwsVpgzV_Iyple2nOPJ6iXguIXjJORQ-lwqE2N-D6ni2FZbaQ7d3ZbAj7VniSGPuUdp27r7X3I92N4FpbtwI0n2Dwof8YHN-ITjEACpe6Uv-_zyp-_s50N36E7jPiIvHff5HIP--zkocOnY1R1CnNbzkOIOJ_J0Lxc8aRrOQ1G-oiT18BXQfrkzJ-ThvrQB1PSz4NSpNUBCXrg2a0hQIKt2y_ANZHF-xSvSOSw4pg6c_wUDL0Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBOwP5AIGTyeIwkFsGADqrWqiQOagSSW4QyXUHgAJWxcV-kxluJU79ZcrEK5JM5ECzfq5vkKw8PM7ZGuD2469qvWj0Y0qUOz0kNti6lj_R50ECpUjHKyjoQ3lB4osorWSBG4OU6PW9V9-LRxAGtOKHPU3M2gEcDGNdNj23C7KYOMq0krxcS6Z2AvoPRBQrFZ5kefWYXlQQqLcUQHALnxueNnLmn1lx-aFuV-8gL1sgT2HeTCy2qeVtdJFtkZpqX4xQvlw9uhN91TuH2RwxK0wvxospkvm9QUR1fSjf2qpQw8Ny3AV_pUDkxFgJ4gn0wDZb_3yPYrUIy1Ka6pxDMxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMIiwtygcnnLVK_0x6Sjp5DzM7Gpv9dWAqRiHGASXDwQtVJJrqES_2aMyCi7A68GKbQSMTYTowAMhbh8eps0tASbj_3QH-WRbd1HgrVBUfKOP904yZZtFBeePCDJ2GE1iPSG9V0HkCKxNYJgA9iqPAjXnK5-fkrGnNNBJZdPHRnsBDE0dlpo3CPmCGo1smKkSs8cTevH_1IepnZuyvvilUs08y5RaGgRF3jicrTRkksfj5rbJt3tX0GxvnOugZws8lxtDcW3mHtlZ22GJgMXFXLv2HjNGZbf9MH821nXe_ui5ILYOSnbUez2fftOIhRpzciIPWA0kLyA0GncbRncRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSB854ZdG8gBdZI7QP-DwVIDj9XjPe9rx9OOCIQjnyVfzJyVh3gRxu6BDIxSnZ9HjHbJJwPTAzE_0KH04M_-X9QqFkA_zD8HggtPIXbCi0A1hQmKK1ULihWZxiyC_Q6DiUtEQb5Z4UAQngO93R-QRX7I131VVR8hC_qU5EQGiODXy98eAzWKgdzeTpiRdErrXH6f9y9OwOcVWh9OzbeAkb-AUF6uw4KR3_obIhk2xEBLIMD-D16SowcZAkp_UyocAUtD37PErXgjS_q2Cj80aY7ga_n8qCIEeEBcc1MWO4c_v0IJpeFjIsESlb7HgNd0Z877Rb6xdLFamOY2KbEc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBDT2-vshxP2mYvQiA23jOZatqy3P0D0AurdLalk6B_Xyj_ONscYPctwiZTXPHqCSNt3vwmlDleROI1Vux_5Yn0fBk7Ay7Hkq_SFU-aFBno1MBvlc19zh41lDX0BADgt7e7dRqH_L81C8-xFbFIH56OLRTgQX4lwhcCLUiUvJ85tWlZ4QL7l2AYOStn5Ma6re9v4DFR6tEFivSuieVd_g9Nw0AwQyjHx4OfyWh9xOHv5O14YwhbiBWc7puD3y0SCNgd2cSaYlerfSMn8UqbpoeXcbdMhXA6oEO7UJkaikeA-6t_7Xgmmz8j1T4yB0973ivj4RGHn35BJtWEGu8f1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKDbfFbVI62sAzCdfMJkKRbXyJnEIqx6_2kJy7X8D925ymBzw_8k3WxxhYBfOrLcESalEOitb1d936kMFkAqA8t4X-Oo8duu9IPh_5vfbTLg5sKF6ItwhJ16OiyhUYQtLfpBHtQhg56ZI1EAKn-o_U6J3q8QLQqdoxDITd9OxhDOK86U_sANcfRtGnFRYo70a6uLi-rh51KVp2D7apXQGBBwfa4OjTqXwh0PeONtU0z_GsohP833uOTDKVgAsAdmlGIFquK8sJuZzasyQfzBS-QKRGWGleb-OtEPUgiTWR2lIHdi1Z6KRriDKy88KOqoj5sjTfYMLXGi49I2A_Uk1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aIohxP8x3-4CYeSgYxFL4U7ztYWwSDvTSSY2mFzRHfns7C5HdpHIC75a-1f-tRGitDFXlL5Z4DFqjkmgZpFYMYMSwFeQhmnnZkdxq0ao02oIL7GK5OxYOWTS8V-Pk80FoqglB65Y43pkSARhhyWBnQ4iwt9XPe21rWBuA9Wy-U8burRgdSWsyMkVo16fL6j3a_xpJMtwDCfQPGTbxa7gwyXy8CS-Gh5SpHu5T29rXMq4lpqsk1UjR_kpEtjFUBNGYGEpwddl4rKbIKQF60nBgO6TodtPcmC7pdfPVE-tonevF4bVeg9tLdqnH9b7RLBNQVhmLBat7Qq8pTTbqE20rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aIohxP8x3-4CYeSgYxFL4U7ztYWwSDvTSSY2mFzRHfns7C5HdpHIC75a-1f-tRGitDFXlL5Z4DFqjkmgZpFYMYMSwFeQhmnnZkdxq0ao02oIL7GK5OxYOWTS8V-Pk80FoqglB65Y43pkSARhhyWBnQ4iwt9XPe21rWBuA9Wy-U8burRgdSWsyMkVo16fL6j3a_xpJMtwDCfQPGTbxa7gwyXy8CS-Gh5SpHu5T29rXMq4lpqsk1UjR_kpEtjFUBNGYGEpwddl4rKbIKQF60nBgO6TodtPcmC7pdfPVE-tonevF4bVeg9tLdqnH9b7RLBNQVhmLBat7Qq8pTTbqE20rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQTTDLuiEJnrJkfvuNcOAFDWWrF-Acy_gh8csbnVg2yKDNWdjh0BgPZr4LRGGVK6pGQz1Na5zY9yNbmnTZAbm5aNVwxah9gHbubrl81J8IQ05usYp7Y1_g2mrkjydDbh2Zml3kh5zqmhYp0VXDBn4kvb4CRfKJ3NU25t8XaarqC_MJUJVZFYleJIkIJpc4y-qAH_SqPavi6r_BXsftnkHS2W8fNCk36UqnYIaCDG0cAFBUVO-S5AzkdDt8cwD0ufPNcDe47u090fNCuzLNjwtsdgrebRDfFjOUhs-H-prFgeKqjbqNR_SjSwrasOa7pIYcRHAZdWRhsF7ztow64YAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhu9PwKA1VEkVzLiFx1XmvqodsoD93w2vZGGEZAuQ1s8bpuWpvW-CTttzrhxc1n61r1fJ4ubG2UDeguv0IkZf3kvjAnywK-se8JsUcuYw1lDtP6JMTIoBNlcLuVPLep1sWnJ0KL5BzrqouW_LU39EwEjhXjhXYsNxfATbsImPaiMfp9GO6KgO-x47BMltHrFsxFMK3AOxiu3h6VNtOfruQP9Cu1U1rNcTd-lHvryjSfA9LwKKwmKeskhi0Wv88SHm4g7VD1RVDzBZh8rk-Lx7ABt6S0-LR1aBLg2BycyXbGunI_xmjwW477J5X_8WN6EOCn4-zsaIAy9pJop_DQR6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYqL_dPizw47lQOeiRqtrI8pJ1pRkevky12vIK2UCTJgFvO1SU9ECP47VuStHf13jmMV0SW7HL6bvK97ZBiMCblToHokKDiLXDKmI8aO2Xfum3dhFx9EJ-UM6w7M5s6sKYTriRDY7DICy6tt7xv2O1s_7Lx4Mm0fX84mgh7G9oqcfstym_r36EgWErs6KmxAQ_bpS77kZRY8J9UT1zfhgaoWTZi0U1q95n14FnzMjU2x4D6W3wz6YQH8U3n4cH-gEjvvMDocz0csCexHOEQ1tiFdu95GiEdC1K6vx9i5nCirHiZmO2aH4Mi8lOwMqweCNBNCVbo5cODWHoRqzQcRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZ2tZi_ySdh-VoDhBoUVea66Ph1RSi_o21yE1nCSknJDRT2FsnB_edv-Bifx_6xSiuj5NnPhOayFIKWGBJrxgGDOw-kVqUUYc4TGQuKvBBdsl3qK1LruJFLr7nk8zHASna3lsmOOc2ZWHzeu6ZefA3LO6eI_o8czpBjL6R62xWlTNGKtUq9Wo_MBmyE4LVWSWJyXLQ_Pyy8-qXWcOMyrxFSe1BzeAuQ0fctZ110AfhjnHJw3o-nWgFPhiBHHu9HwsJSoFWPpNCW4LWIdr4LCp8ayzR0Y7Tm9mKu0sq8jkNpimz1rNjgdqx7cHqg7jObof8GR3JW9gzS8AkBTpDhfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQx5cTbW-1xASj9aWu5vIkQVTT6hSv2UIY2Q88h1Vg8GR4vAhTyT-UoCJXI9PsQJ4cGMSnMVgYLCfoAr2A0xrPUcOBwVsER8h7GpgVtzftk-B9eqFCaZPrJk5frRIu-p3ymTKazCf9THladPYdHsWtrhnnmLTNAHToKFPD8mqqwdf9auG3xJkw2Re4BJ109_rBOAg6Iui-nNAluBnajKnfvkdrHTmTfQkR_nPrcDr8msKpbA7y6CT0BH27UdcvJFY50qPNooWEfhL1hrybD0aWvDyGpy8n7yBwwK5TNSKPDty2f2Fc66_CmeT0F-WmOWrLgrmQqDo4EAPEbRJQ5f2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmP1Q4gn1QRYgluH6mgXHoBj3Wzrwv7PDn6tVzExoi6946KrUhpRpg3PyZmIuVrYial2YUvTilv33YeSo5lqnvY70mgqWMB2XWCQD-TYpyCfj3GzGls35CFbW4mhnulB8CO6Oz0NpFOgu0udugU2ZoVR32PMVP-9OP3GJti6Uh1x6pxBpFJybeftAcjE4quHy0c5km4BIUVIl3huqndvtcMCTvmP2aT7VSplTLHSdfzPVZhYYCTqY7PIl3cpW3LjMTB_1zMRSczTzHkqgd9QZ_jZTFyuVOZKb5vGTbpSf8gpAC2bM9AE8RbPIGa675xDVf1Y9iqPhfK6Nu4yOw1Xgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jannah-theme-6.2.0_NULLED.zip</div>
  <div class="tg-doc-extra">10.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/800" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
قالب جنه نسخه 6.2.0
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/800" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
