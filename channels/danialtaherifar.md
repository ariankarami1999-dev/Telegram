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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 238 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 338 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJc_CKadHLiBq1j8ZbKM60kkrSbKWEkABQIqFH4uxqPRUi_PEx69YXmrqFLGrLgiWJFfEX0Rxl5T6XsB3CfVnyktUcjHaALGBqiYzFx3t0MjrmnIicyu4fEHhqFunUCtWEqeRGrfcCuSi6oUnUTi2fv87r0BuEcc9KZgiQesLChJVGfSpSwQLHKIJa73WqXncjftdUt84PEyNuI1TLptqVwgk1cbdtAfTy_VPCV2vh8wJmuJ1GKWuZVn0TIGx3R2YpsvQEeU1CUrjYGOqNDoUfrGTfg4t0twFCt9_T65YWdzdiVq0-9LZhhDpelENv_btsCJluCf4lQffIbT8PyUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 432 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RinpQfzWU422E8RiBuAClkzWTgpuHsvN4h3iA9hrYADpsCv2Mt6bfHHtACavANU9QgqqqbiJh9NeRE80JZC8D21KnL2SL07RR8KDk-IqDEkouGcxas54te6-UmVhnZrxJkgtk2-zreI9cBFRDs8JonKyp2sOcLmv_VUac6V5AkjY3fvsftyIldbbOykNNUui3ooJFYAwfQXgm3wXU6TJNRmm0CugyQuOfHDD-kHCTJ0mXXoAJtP9Ay_lLRFeYPkqvU7U3IhfCgRHs71914DRd6DMjUWJT1IArJ5TUIg5ZNFfUQMiP7vB5D0AP3rz8O04EbZ9lbFvbYj_9iSnsYeJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 699 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hmM7S3h9mqZgG4dw1zbIwOqbNddKP_FoMCzNPm8M5vm4zHCNQ4j-Twywxr7E6PYUbEEYYSYDb85NqbmgMHu14aoFtuLaLW5Azmc_VXE0Ocw45myzARWYjUcVodrkxFGzUjVwu9Edijt86wa0KiB4jdmcC9S2Ui-Nz0FVRLB79hBzymdy3pbumw1zjyyyydkM-k4DtvX6YdckzRTW1JbuzoUdLw3Fno_u2rNcn_5X49uSboAdLafCN_tz_CjAPoUEj2w7W2EGaCqVFWZ-9AVDT89WeB0PardgDLo6feTe5h3muUd6GvAhUj3m_l55rVfwpFmsh64zVG6sjQsDrh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 997 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCDTGAaxUox4hAccN21px504-Uf4vN3xRpzUntgLYs7ZMWcx5VCmw_WIqs-V24kJdHGB8d8XZEB-VzaR9hvroZjB7-v001Me11hj4ChYb-aUUpQFCixeUZpmnuHM4TUPhOCpsBPHaLjrrhbCg-njnU-gZU8_aghqXeo2EvYmcIuzxQmsjYaT7pbYc6thYNaQn_QbMyyIDpJ9n4NbMofjQka2vRCTls0nm1YjFEkCx3a53R0Q1kpN7Zimy1ERNsxLmEDmRlhRNjqpZlfBoCamjvgXgUkbYVYt71L8qWzD6GKgUoURlQDPUx5BEn-Cc9BaEOVkTWlJBbTtWMj8pSgxXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBHSwv9HJ0IJNQ3Bd20WjC16WvWoJ1fhAYs3Y8a3fp4Ue8D6UeeS4dbSzaeNYNbsZKJuxmLZYEbgLv0xchz4QSHrLN1Ye8tbln5L73XrJjz3EK5TH4hUprfrv287uUVUUy_eIxNvGJzihuz67mj8BBTutgalXQyFs2DF40bJeocQSptqBqSNc9ZGQbD_WrKoyh8UEB5w3IxTOEb1HhleqTFwS5BrfRQWB6pjgxPbZEn2cStzMPVMdPZSXld8gHH9Vs8GAt_mJ43hYLzxh-p5oSEk0_etAx_1rrqwj_15pUuRLFylK38Aa3JrcW719pWUg8cOI1kMR-XUF7_ilwpbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjPJemQcwNS7cI8BJaV6cawQDn6gu9POgX-9HPhPr3u0cyFGaZQt4IlVdC8EIBWlCnj51zMXY-kOZ45q0A7TV_c1AQaMcHfIJme7gicaJS6XImhjK0A0x_TI1cX2h905nfRn9mXKY73baOAk5e2dvIgCEihLM5ROdlA-1PBAoK3uRHY49QttWsFYQ3uxjZsw9Bm84IAJhNT3Cjg6x8Up5MjrvKngCvqBw_UL4Jm91MLx1raD44soLa2IylZzRKx_97l2588Tvwp9Ofb_hv2EG1IG2rCaSVupyXpxyg7aIqkg4gg4OwNa-rvlx--ecg4ys5ZwGvMJ20UT74Cnzr4jeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5C_WK1azMb03vnTvIyVGlW0PlZ-qC4PdLtwuqsSxPLCfZShVdwRsqikoDuVZkNRL7ZCFD70Jw0aLQp3YwEKryu1jAu2ecWL36Wc8Kot8mghhcDbfKrAnZNfVvYyuRPzjWWsOfLAX4zz3_tAG7vptIVgptzQosKP3JiKGi1Q0bFcuFc8Y8S4TVuZQ2FYHKwKdzwZWfRPEoCPjQJhVOqRGsZoKZmf310rXGSj_KV47jmP_2JC9GYRbzwnPlnF0pFWV_-LmAQXwd-66TTT3yv_8mnj-MyCnmnvubwfB8aJouXgwGsCxOUUyuA7YN2O2RVcKjajZliTxnkGAm1GljFVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuHL8SL4HMO7GpWKVVZ2JpZ4LDDL1SK1EWv_pP5SsOYp2rSOqZe9gyF0bYtIWC1wmNkQ7_LtJJFOkAwpeh1OcAvC-ND324i-csfcLAFLw6YoLBkSU8TjWa2H3NJSmto8kwoPzoA5sNGg6hv5pY8hOwW8wHYKJ57-cfFVYqCA2-2MIG5BxCD07TymReHKZW6exwCzdJ44dxJzR_UjgyrxY2sqtDa83RaA86neUDuvqI332yAMyn0cjc9fG50eEuSYIjMw1lH7Ow_NunCqY409cWwL3FHzz81lmfvJM1Zg6H0he1bP-06It56JsN-d2l3hS5PdiGNFl53UFFEfrXh4-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y87YwXBOSu7rFIky5k9Y2B8WPJnxrCDX-7KECtf30Vkf3WXKkmFO5aiTrszdcc_1HkAQqKc1X6V3NKCVkY5TAhCF1j2CTdqats_DQ5cM4t9hSS7dFimFjJ9Ihb9jaIS6-TZOwYvgkXToowSy6rZJ4hQyQ87L9pbs6N5VrMep7UpT9x3HYoOjLCuI_TZ6U5E7oQDqbXkbUQtVTd2cA8liUpszCYVXxseiujDerVV-BpAwHi3I11cloEAZlZH9diLBc7-BRA4slAA9zkZdB_IPZkslXLkHvp7AKcyKOxypH59jBMS_Ka-o5iFqukTVC8kBNNgKjJvW1dlvWkJwUehetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQ7_r0togzPLjw0L7Fk91aNcy8P6R3y317l23grt2uyn3KsfRu5Awiu3_AsLwyXA4y7MVE39TrWJuf55efyuTcTkTbAgNXlsG48GHbxloVCHr_C7i5hW6DhHWH9wHlZqlALt1f6_Vw8-GngcskT9xW0WmmydtQTBRMrOzRdiQcd9CMCvxva8VRblOiLF_f4uV390fcgJekh2iwT-qA55akmwPVzOE-CQ9DH5MFBCf2yUpki_BE1ZeYcgdRubEiQmrv_JBIMQ9Iz3C3UUSbAaiyLUd2M5QKSJDAYSFJJqOV4fsGME1Kqh3hXhPVfvzMlYVl8p9t5lBkFI9PczR-whtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkpLCqdn24F5hjSUkMskNfvESjSLKL-JGl6TnV50TyJcVB9dt2A18WI7M6PrDk0H1brherYLz_-CS0vHXITICSJahDNcIsmoqTewETiglYHKIsOfqemdo7acTPX5JbR9gI_9ifjwJDDfwqgZ_RanH63UspbKwB-k5MOzAQSoOhtJNgoKd9aZQGaA6Tc9z9R-VoUQ2ejPTqP_OYUOslM6mhTFyZQDLJxQr0rnNReQpKqF6wZamB2KHKBK588chpPqE7MP2YSU7rsEDeOrIAoUpNd119N11RAKtAatKug0cV0e-W3GbmYfy2QCArq5QzcH8sxCmjo2pVJZDZlVL7TLbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=lGGwZcjrToJFGIK-JKVhbxuDPBhOCC7rzGe2o0kVKEZ6Is5KEkfj-aSPXkNctXTzLqgh9FNQeKkwCLncIYqUKmEsbDJXH4DfregKGQWyKVvLU5V23ZQY8AYgH-X8rWtM5mSnkzJIx-m0-Jpr6H-iqaARMr4ufGl32usfc5Y3pFb-LYftm_GnSMe0Rew8tliNTGtChnooiPjuMsZR37IOo6vc1omfDU-ndJKa8g5O0abtpbAXhbBkjeV4muLfqDc6cowet6I9yemnJrH-g_KufGpEt6CGkwi1Hfse10tYrjEmUoah_BOaOF7LE3Jja6alTv8u0emdT7g4q-PTXkDpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=lGGwZcjrToJFGIK-JKVhbxuDPBhOCC7rzGe2o0kVKEZ6Is5KEkfj-aSPXkNctXTzLqgh9FNQeKkwCLncIYqUKmEsbDJXH4DfregKGQWyKVvLU5V23ZQY8AYgH-X8rWtM5mSnkzJIx-m0-Jpr6H-iqaARMr4ufGl32usfc5Y3pFb-LYftm_GnSMe0Rew8tliNTGtChnooiPjuMsZR37IOo6vc1omfDU-ndJKa8g5O0abtpbAXhbBkjeV4muLfqDc6cowet6I9yemnJrH-g_KufGpEt6CGkwi1Hfse10tYrjEmUoah_BOaOF7LE3Jja6alTv8u0emdT7g4q-PTXkDpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAJAC-nAuHlhQ-rFfGcfuxEhd4tqzlvqj8fX8tkG9UOzB4HaZwWE7wlwME9nESTCd8BTaXy48cfiQH_zM5rc1D67e4_cgmGKoDuELnyivyp0LsGBp_KZnBR4wC8yh1F7KAvpNw2AzLrVuE9GjAWOgeebskKG7--VW08NOli4rzzE76S6n4r0LeAKJOZrHjKs_TnL7ZhAAk1Gm2itTh-z7REdde5ctKYToXP4LjnI7zAHvn3YBldVml7DYsPo95U0wYGRcsqghkJQoi79GdUzrPVMRUdXlmQkgN6WhO70OjuTT5XQNvw1DyoC693zj5W6lIwcC_y5qevWJWN9UJC68w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJNtrSKYUTVrny0f_BBLqQJqBWPVf2rSaMczWVE-C2NaYpMgIXMHiU6nzXqX7lQ0SsPHrFAV1_XtLsTCuWGec48-bogMUzZ323ap5BQ6WuOssP2FBqFzCbraC5pS6IDH2SnjDsKXBrnJHy2Ka9LG0gDtnIcXKyTeTobKDB_tjx3uo9iGaNXHCaoEC7M-5CJZq8BVo_KJBXOJMcYWI5w1uq5-xYPEH6wtfNcObvn0gyjlGaLQF-NEWI2RojJKLxZAFRYq6HVRxnnvewJIhFkYNme3EUYSdAw-56nJL34-0mwW-58--vdUjSopQQR5-PSY8HGRa3ujI8FYXL3-rg-hQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-cp8WND-XJJZXp813GWFOkwMlzSLaxKGxiXsl3Q-U-02ITRymxTwckwjWaq9uruuYSD1E9nKQGy93Q4fu0RUAY6L_0oJLh6Ypm3fr0hW0H3z_dqRlD_pB45PCjttAkqE8sNA2CHBeMj0YQIeniPdvxVDrAKjcT3J06FZ_wk4S2AcObTGemHUJYeF3wlQom1VmnwBEOQACbrGjMECEiAeRSsqB4uVU44xUUaDHAFTrt2e6HCvm0QjPCRTkPe1b5IRzpRB2wMEBOH9YglrApTSrgbURAzPgkTqwHJg1tnezwBDdFxA7VObHyP5ZU4wIJU-jHYF0qrLqAaOkWY2aT8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVnTMFbOmRb5M7M7TFuQUHluiMMMJb_h_FM2UTw6KmZkyHnVlDdZtQKQK6vkQDYErNQ36bVYEhrR5I7oEHLan4AfdvWD95w4pzyG_gToweqS5RmlnR-MZlZYqS0FJjGSOpLyqwrDImFnYnlPAVH2btPwuVKYPqi7NzZ-R5EpdpD4FUDdRabXy7bGOU0Lr7GS29absT-y06Q7pXF-FphESVVyu4f7StilzvZOkJ7egHsUAdDFYelzyn1Dml5CUkVaIMCelJ4u7yWv2cEw8eGfjc1s6zTw7F9XDvnAfo6piMg0fLTo_SSPEChepWZrxFFl4UorujnLQVpWTrwslcOQQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9w82E5X88bzKAsfJjFIzEYPYM56tfQsYXgh24V54PwKQkVm0snMMqT-6NZPPMdNpdBfXIgYs0hlPK2ptXUkwoLDD1LuWNe0L6-CdCsrArsWgLG_lVVUdda7wXx6ocCn27ngkPJVI-hyV2tQUDldZI2U-tMt8brI1WprbEVpqm2_8QQCW45Pm-56PhzY4yk6oJzLsqHAuHvlc0B-C6G8gy0jOLnpYoe_TYTMhM-Qt74Gmydz9bzTiUjR3ruKfg58cHEHBvImXQSZMUvAtR190ZtnYGMZ-B9n522BMcHypdZvZwEvuwPoKfvEJ0KtmXNGVfrtG473HOO1YrRWcZQ3lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb0yCEm5WvWlXqC_mrNMNVsOZgm1VSK2EXEkfupyHQ1wj5Cz3qeuFfLQgGIrk_EaZ_8xuu1eCAFpm0uhPt8RL-8u-RAsnbpe8tXj-vHlZNbCDH_Egy54Ds5NfYpMu6JdDYgXJ5PGfwVXx7tueAHtyThcJ0vU8LErNpooa81HETeyAojxqqeydHITNpcJ5dqhzLBd_Z8dojmWRYUp14GC2yqw_1HW9Aiiauns4e3jIQPdLmd01tzZN4krAcEWRwBh1OPpNObbGgJhRaq2TZTXoWr60-Kuvw4coeIFyQTXoonvrqp7ooYx-W-J-qe7oFKCcuHojmpACbyk_O8ov-WAPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhEfFji9l_lDItT26nTV7pgJ6R35ZqyAtWTm1IQ1UMrU0-M_22OSoZ2ffzJ6qq6jF2HmRs8DKShqvIE9-IjP8JrGdtZW3FTFdQW-jLnv6xdGrtM1DW4cO_fxEOe0UjK_mbmHzBZ69ZZRfWTQuwHgeN3XKjca4im6BSwEehFOpmxIpNilPYGKgrBC-yeRana3FkGJ-4Y2Ueg_UJScxLuUUQx135sPvzHkoKFF_PTutuW_yev9AfOZ2UnlS3l224dCPAX5VrFk5mE3mpmYiQuOFLTxwvHQ8dA7eT85DWYOdM9Bracp09eyCmFfUcaIqaK4N6yt_nJUa4xayhRlwqf88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbt3acECsyCUUqI9cAl4ddHPlt6gXi9DSpZ1MHuXLdGb2Xga8WFsNoM5I2wCazA7xfGevEPDvlxx8D4ptr7vKO09qaMGVVS-iMLHquAZph5jIBzAp-oPmbxsjTh52nb3775Mz66o7WYl6gGMp0C8X54k4wsmS9a4ZSdbOVExsJLYs3e-UuFM34LuGry1eR5qUOSA_ek7AXrxgqrq7VuCTPQm4unzd_dVFRNguOTNI8Yl99EaSMnx71OlpFgb5nl0P2JR-Nh3Wa_3sYMq9yp5aRPWQFcGgho4GprDzEnmtNBZCUCg-7RP7NDfwyeymAtfTLYXJ3g9P8Qxl1ffA-dIhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF9qy71Jz982cH8g1ziPKabpAKQPXiSk9bi-aTXkm5R2YDMOWArSzSAnewgZLs0PuuUVFMr89kdKYxUSFo3tT_w77uVf5jzWZWW6JuLEO032-w7oVGI0PuT67sn3EvEqdbEJ2VLysQYOxHS3SOjrKgbzy5CItIGTuKdlLo5kpTyCW6JnQDPA-zJl9mnT7Zt6dk99xIZDvOFoSJ2D65mIDBHq4Yp5qJ00YA-ey62RtnZjNg68LTuN5b_1zIgn_jQbuU4ZqMV6LUf01D_X_X_OPg3GAq-uNQbmS18zxcyTOgZxZTw9wS3ILjxs6aXADVq4-MJaF-JGdS1ZUjAq_Z5gAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IioXacyhEBAIzJhYoOagnU2HGrrd6FpRPaQtThTnb7S__FHCL8pg77F8iKZ1FLFIalYYC9edqnJCMiT46i9mSYroZmZ9t709P-iaEO-akc1N67W4Er1yfk6LMbBq09LVBlnGjouQyEQ4jlGy0cuPlknadt8oaJKfLRDGXfXrkwqvOslsNs8bW31QMITfcNd_ZG-Bl_aaz_kmUh2c7eHmyXjh9q_3tYvadVv7GqGn6PzlcdJpB9RicHg3pmAPYxqBJZQ-rnvW7a9SeyiGiQ7wrOwqv9fvuV5Z_J3B_6ihl0nFUwztdoypUo0RsQq6E4z7vhyDmz2ZWO9uJHZL84xYrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhb_AdQdlqIKoAhAOZ7WY13P-zqHsd48WUSE0wt2kakM2MBHs1vJCkpQaV5aQJ-MaiWPZ5Jvui_-nEXlSjCFTygxmbW559nZdd4_JL4_6VdaLuQwl2jwaANGqJBFV0A9-DG63X1GMBTCMmu6t1D16srSil2DaS-tMtRbJkCRYz65m4Ev6w1dXaXKJnvM6D9L6j278Z9iAG8hEwR-yC-sSYTaWyCRCN8RyNb8PcL5W5ozAiZvjMuKrKBnOMoQbGosprDp_0mk7Z4CQDDAnDqkNkytl1053erOIpL7mOa1sSwX2Ivd6QLNkJYyZ02Z6JEH-NvCDSI9vpEf-OIvaOWNgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqhuBiX4dV8R--I5O0AJtdiSq8FwvVDyxaIM8hLvEcnbiDRajWkemJO5nKX_LZGgagQKAUFoXBDl_wbmK1LiZU8Sr-lT5mGA7fi2kB3ZS7URKeDxbw1DI28rzcCG_4D-i26g7ED2Qx1SUXIYvUD3i2O7-fHmgLREbWNywO9rtW61_fkdZ3m_k5fRlIDJKxpT-inNBfeMQsUImW3qtZdaVn96EafXCPETRcCM1H4N2q6XVe3_1OqcKbVT96SLKku57X_3iWdxf9nxvCBTsaxdTTFPom5JB_2ZxTNfS3ed4gCPvbkm6bDdYzN5G12qjK8tMIDKdlb2H5A6uudSHnMRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBChI-SnXsdvVNyI4FPjRq-DomCxRUwC4dyAY9JXVjdATXbpk80pwiryOXabqSufL6IjDUozj3BAY_PlZ_ZyT7JNF2ToKlnA2d2zNIH_7pZSRSRgwTdDNasajO_U99yDEsXBAynhl_JvVThEaKyTUetAZJCVkrbGOhb252Pl6Tw5tI0Zpz5RFSA5SrFKE61QO0cEtK6tAG8tK7KOSfW9Fw69GspPELmbdxPKP-WSq5QsJnNm5GRYt4IdOZ6St6SWgFb_2N3BQCsfMU0d18DHCAnjaDph9sZWU5wDmjI3n43ATxSVgDGxkg0xd_5NioXXfCrovVDzDx_AFe63mXf4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZfwb-CCOjejam3IjQvn8YpMXbAmNaYS9W9NO7PCMTw7Spa8ppgYmFG6CoVF_sCuhqF-KSZ5YZU0_Zou54RcoW83SK507nJ0OQpfTCXBj6RtH5NVeVsodaCyMYcGcFSmcAsOzdDRLYeQPKPP2GOOsIdiGM0OXwiinJuLYjvQ9Ja-PbiEuHG-utn43OMlSjthl5QX4oUAZ7MKFz9GkKBPOC2z6QZpXOEbcB6GWcnOtMYIwy2WUxv4-Lg5gDeSxtYqZP220_qF0YeOAvzTz_QIU860aXAwy7_GWvUfn6OStNmhT_CfN9qQQbt-fa5idKhpC2YW9XLPqWYASyHqSvS8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GB9LLCTAeZIySeWWeY5eOR5UMHq3Krsm2tvWyKnpYRLlsFJwj1y1IPV73QMaU5htvmU5q5O5YZazdxDutu-iWNhaEOCPWIDAyt5UicCp9cZcJD7XkC_Z5018vlPgYrQJ2NOtkvkbZka0gpNr1alsxyxpyPmWNT6FsKOZmaJWsGX6LAo4TUHph6mQy9ucOVrX63XhpkM-K1nI84al2GDyw_Qjrn7bkPZOsi97g_39yfi28TfqYPyNQc_gbx4ZmkpjQelc1D7ggVZnPOyVKpVAvcuvyylG5YZAnBUXhnIXalYmOfdHbecNNLHsSQtqfTuix5-EUil17AOXwWCvvHZrvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4GK6xUAJM3TFZHJOk_Sn1v3QLGevztJjH27NPVyiap-SDUyL1-nmnkntUK66WYGgnaXRVLuZVa5iSHpISqyEZLnC9dFqXzyR6MHW7ohWuIifRJRXDY4powTZaObBRv4TUFbefIYZjePVFyYzevRu918W-hiTO_bXUBh60wVWzDl5RiV_j1gSu31pDB5G0vzxlMB-YyB3WAI3J_Hq-xjmire15QmjWg3ZL_F5tjSyjr4cR16YJ4n1PupA5kdMHAvBWFfDgcDsKqtbN31cnkbLqvXE_hmrn-KOIPR37HvlBlq1pyqlh_b9R-837HFxDCCDtHWwGWuRLMDW_Q-wy5ENQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMR_8Qh356bk1tf9tkvE1T9vvRVXUVPVOHawD4SFcoev7nkXZNfaZa74bEWmdQUsfj4-w3B70pE08enT4XIrWWA6dcOngfaoWB2bMagwVM7C1oOhpjMXtw54TVBYbUr6fnl1MSQm4WiOhRRAnqRWYNYTfG779EjKVNtyAct1PrfBUo8TD_Ldhi0KSUT9oRR_WCgEjoaRVkoWzaOtWB7v6ofo7Zd3K1R82RD-eTZLnfdSc_-y9ecSjwHkMaGBDxmbtfd2nQgxHTPRu-iV7XwCUl6rH_66Rf1qhpIi02CHJvjMtvxVMc4F3YrcQZ_9YGPOOdmYUUFATBHOZqYy53w8sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9A8cs0SL-VsYSjvGNXGnOsH8C5oTnNMKcf2yMgjh26RyCGYpffEjMxd7AYzV_v9nFHDTveO3eMAFIf-4Ti8ZyklcgXt6fg_N47jpwFvw4xTUqgQuu9wYhcIMdJq2JWHDZlDk-I1SGnzWziv7ZXVK_PzeGUXezU_ONvY5ltNiAjT_HeRE4d3oCN14svTPyLt71xONj8_S_SvDJXo6ZGED6x0p3C4rBEMvEafsTCk5xJ_8z9HuuwygOI7bST5OeRlUxHw7MOeedP5VpAOUNhgXiToTkNZk3cOL-xaflOCHD--3Q9qJ2lzZ0QcSE21c-ByCfZdqQYs8NqvrY3I6pOiGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcHEYqkXU-QBN4yD7A5RUWX9tLVKCWtCQ19xhQzrS1wywMQimYs8lXuC5RMX7FYkzGWA_fCAGmzmhUQGCJ-qk2nUHIb8_1wVVlBrTiJLVHogm1mUm0eI0N3PDdzqLV4Uc0llcldYdDdv4LNzCeI8sMcyF0JN5r6dBr0CDyt32hMXYxHB-FWjEARWUxJOA_pbn-Oqxch9mekjYxAKqP6xGiaGjGnwQpugDCu7B91zPbtabTsewKOu1hKvQeOi7cPZVU7hgBfE5v0TUlo_vqOFHFbPdFSsLZDQWMzCNdjplj_2zwL3ukxsPOZDLY5Q6GUL_mYC-H_4qFU5u_W16mR1Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXiRWUdbMrzo6jbMx6I0TIbxzP-MYQlYMTJ22Qapq5uFIGil1LV9cFGvnvbibW1uMVsdeUVKRyhFmHOPQJNdP7G0LCMdITYi5aPH_Aspm-m27iSBP6O-7ibU_wLLYvafN7iqi3t1ASspsMtogXUqC8r0BvFJ5FQUhgDZSIERWPLh58O0SNMHmI2bk2NqmwOc4KqQkjyYvzxmxIFIEgUs2CqSY4td5GaP-LIeUejOC56EajOJOGpcVFrg5i3bB3ja5PiCGdEbP1Cuh_EDzUlB5Wy55bdebf0m_WubC5A4d0Pr79q6Ezwwv_VzAUIHD66arSZ0LUP9y0iJT5QgcBOjxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCq19ZZ8nEvOSqwa-sMCTOMZgeayWOdnQjE0eG9GMv20jWWzETvOOcEN2Tk27uoI_sSIvruThGB3uEOGBP_1vmdni4xQfsyZrQesYvvXbzOCaObG3GaJX3B7kE9KgsSi7FmsED_pcMXsl3Wtzo1hRlLh7qq4RwWaw0Dx4jQUKWdONJB6lS9_i3cPeR3HHLYwewl5zI6tZkEUhg6EzKfcpEilcih4sO1Uetl_37NnTfHlNo6sdRO1oanmub7ZpfVjPFdZ0WpqlcQ05xPQqWu4cZ67Pym0ozuZh0Zr4lwFipFlpw9UmdIV7D9ZB5jHmNrFsFHnbh2dSyyhkHRE0vgGGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8iIqZc-YdWfjljPBx57s0jYlfywIAs4WMpJcqIJ20FHnzFxcWzbIJVlHck6yK_YNMvqLEMMQyKRsCtv8QdFlheujouRTCZnmotsMtEhf-IXmM20XFWf6shWYME5GKWJn-5Nr4coQjITNBYybSkp8DGHOvXiANBB06NhVIF-RlcYo4nBlk1Gs3r1EQ1GDNTm7iNwYWr3JHs7u6HbHGjjN2_4rlWMXskzlqKLnQsSHsEqMntIzj83DrrtTSEiIr7rxypDbawHlBYu-g4-Kupm8JXpZh2D873-SeGH-n5lcSbA6b0FJN0qXkiXfCaftMJaYZwztaoq9pGst3CfZsRNWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hodwbaz82YDahaWB0Nghp9tjBx-_n4tSbINsEwmNuXs1HIN8r2mvAqWv79ZoMh5ggBdDeZlqfXPzRatI9NqoV5kkWoAzhr9wx-3gZjLWWvWvnROXV4G4p_vDtFONwOWa_80uYIWzfynvNGH_opImO-BuPjdgoqChfmIEOpO9Psom3vxtn2eXKSeaiE4qdH6W2Osx6kK1bfSlqEhwgiiaDYHr7kTN1lAM9PEihm_mUx43aGFLEOph0hsFZl_y0JEeFOxqMrUoBvtY8S5FpPbd_HVW6PdbP0SiXkH69b64IMiT6vkFKfxTcHRAWHfwkVnfoG4bLRcUUfBcJQ-saq28gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMdy9W4FIlsFe5WTr8WpkxM2iBgR-Kwo_YkkHWbJm6V-FUGRJaLMnZY4o8rNvP380h4E2usBJqUIOpv8PG_OXhhv1qMtRuBpsE5UluXfQke1tzxqXioRuM0M0wdxkeIN5k3gxK35TmmsAYEvZPnocIrpNNOQg83vidkOqJntwCzsANgBnExkabaJ4a9W1bjCViEcrBXYBQwBhXDApSDrnB0BSmfWINcqNCLXBl7-RYxiS-RNVwW2A256bzLGWEzMC-SS7-ANPlBW06GU0xCPoVclCwtzTj3wfw6bvMk3DoBnFJKHK0Mz0QhwXhptmMg3BBRG4ZiR0ZZrWzGRXfrp9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPRDyYN6tP24PBqEjIVcnuTA5uoEYrlt7nj0M8q_vrHsKEziZSEUKhnStN4tFYfjw9H1yJ-OYuv6kf8KgzdIaP8544PiaioaX_QHNgcPaUS-YUN_MZaX2_lUbYGA6ka5cA1OeDe2JYe_QaIvaDG_N2CGQVzaCRmcelGlfywWMriBGLzAM-fY88-0ATrbrcFFubfVStxNgFFHQF_Mh6hQcAxgwPtBnPbuD3lbqIoX3z5Bo8wsEQmwHWenwEwFU7_tDfK21acUfpKIJqs5EPH24-CUTwI5NGMmNdf_XkwYvzdZ0C7W4KFO8OvPXcYjQUh3KuKWp_oebHJJzlLYjrZyyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEw8RXOuM88SQ5Gmj6xWaMihTZbixwpUSgaJO1PawIOd-U6lamWIcO8dF3yBO5Piaz7PALVsAsPyRmcp7jUzijL2X4F2ZP32zep6TBmeeby46bYfrwpZvxrgt5xFqpe7DNATojoQoj43mLWd0dXvhhMCcaUdCY1eW3uTyjHdhPDMlJQQX7RZ4K6AuIVRUQN84UNmiREAYTZwh4kxIHe3yTRW7_hngpvNVHT-Phs5MlfU8rnf_SJRbE_CwiXENvB5iEmSgFN8KOa8n6jkKCweQuow0FhwDWioVua3GGx81yV2V5eEbeb3sPplgR1f4plXDuGOhQFmcp3zQmVtb7PesA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxrzkWxGQGb9H3-oTdxrCwEbhQWwvfRI9v0F19IgJ2UvEEx19wbCfcWXyVvkEYvx7G3rnhVbL3Pi9xMOWj_Nw2aLpobZ0yvGSL4W8e09Ft6hwbvar_vByka_ycXMrOIWYAQT0TK3FzVVF99iET5ZMpgNqggSbTR2PRrY1PYJL10S9P_O2oA9DjuF5MqupB7jTLNF_Z5zigaaPmsNsc29reONbt9CxbwFdH-9yBgx952PesuuiKxwxEoNAVHE-SQ7GkCFAQlEmdgOpYq_-PD2b8gpkC83XhsBry7OF5mEMBi58Zrmnc_ZQXxQhgJF2uO8cPHCJMsgPNB2jf1l2ndeag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iev5ixidsmQ8pp8ucN8eIEK5GbxgFBs-x6SM3-SXkOdP8xPRY2gVV9zmfm0oEa0elQXVtqxI0YNkEgkcP-v-nBBRt7dqHZX4_jZTLl7k0KWfgewlVbXWlSC0pZnp2FvNvfEMT3OvbuScEGmJGm_UNHt7G607OD1uS1sL2M__ylqTuK6JBdjKpAssyQpYNfiCf-OBUBddC6cyuIeC5F_PzcvFor2jGabFzb0NjvtbIPvFp2m46r6xIuJv_L0zltTppW2y6aOSaeCfrDcbBbWIGZku2WIySQ5ZhBI80q0pAFbOGSiaQNo9JB30NPhlVCgtT_TLTbUvMHe6gO--SaQ6dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUC0oFANOmaMaWzL0Z6kENuMkKcm7TcL15wgn1e32KfJra2S6OUhDYF1gp_MWwluIvZlJqebbuycvWA-NmfE0OHY_trsrG6bdpex-GAEd8laOxRJOOEwFHlVDb6zZIlnst0XN1IDgbgApaexO-TczFQ4YpbmTvR18mrqRRenLHJjcX5YBcf9FuAG3UOEM9t0ULzTmYcV6Bu-1nLVlqHIweWdKrsxCkgeVnNzOIUL4tGnLbrQYQvC7HR5E4RhkuRJAAI-6hOOQDgGA-bzaSGWF3idyGP-XkPtbTOLK6w22WEPpQMxjwjvx24GmzI0XLauljXKXl3GKDZjwVRiYd0pjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ET6-kWUsBw0VOcYHQRFC5IbxW52cabVv5EwVlTsniqqPxqpgdOehE0E-vWKMrGY-1fK3UQqY2-kh4dPpT7rovW_EOKY59yreygsT05IB-iHzpA1JDOiJO7gEExyW4OOBErBCGZLyqIoVF-5BJqGBCbpMjOiete1pFUBnNc4PguYn496Q6B0VZmqwgezMnNYbeOW7Ecf_-TdAxpD_PY3WSxnMjzMGtxjbyaycdENzYxz1zhUTCbsn1Flz1k0fGdEkFDuJzJrS2_yoNbgLnP6tJ1hHkGxrqpVp9XtRpdFxb2NDQHiHGOxjtNuVtrw3HaKlR4Oj0R6smLa_sZvrsjHqVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbCg9Lo8vGFYb_uqXJ6NGBcxuZOWxjohKEseyycQdpbs1JDx21P2_7nqcbs3y_bkEZqp2tspgoe6KOvmO4AIpfic9gzcQK1IcuMx4doTjkHlqqVXZh_ftvEc9mKqnJYjT2zENryFArwKg0zUHceip7zJQPiWdEyjfcTkb2TQEyPPVE28lAnBtkWXhlfucgTVlen_CNT7CiQ4ccOTQmUjeI7vdjNzL2WPs8ZvjjSJC5BtHAPKyhfVLzIQ_7CUX0ikp1kAtfjMcrPBSzwTwSZKPJ5s4LIhWxMCUjh2GhKFz7QXzWg5gd9rJc7Zy0QaWVkqxgfKbqtmqkvNcCUEmm_zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXUHwb4Xkw-1MZr0mn3QjLC42sWofmth7MiuNNdfiybsT2BTPlNVcGp0IJI8lb844fTMhYL3VWTXg262D6J76Fj7UtrI8eYkUG7O_ojcYorh-BSHF_py-MB2aRmS-_8HhRGJXvhWn29w-an5k7V9DZXH1qBWwmGKePkxT8CGJslCGUHLhCJKDCe7VnlJ9Gh-vmzPsGiSN8yjvGFhgWnEWtEGpJYVBOMrdcnA3cLKt5PAF4JSUuaFNtH4AxxHssbgQRYkoFKjMHHF3ABVrlobPYpaGHv21VTO-w1NQzEccW0r0Ywwr87yUnom7tQ2AG1BcDzgbeTXvDSRuTqLWoLAQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7nbPQ8m8vpzJx6ZKxeOoepeOKAvxYe1bjGbSZeG8LV84GLm0Fbabd90sLg5Qx7_AWXyrASfefaB5SsLfdtEEXCG7TwidpP2VouYkYup0OLQETk088TY4M40voAQi--H5kaVAZtWtVkAnMysSc0xJvYCJXdgjpa2Qucxr3S7gBEfHPI26jRdhcu0QCay_7-_mzpSZ26Q7hdERvLzo2MSDBEY9Dvvm2L48uGOuLR2hKAdEa-MO41jgFRZG-rKaDhPFBklrty1qFEtNPjqvBRkmVnzS7BaaiTBbkeH5ae4RouTgTo0hQptPL09o3COalsB6HsoSz74-t_xmzTDIM64lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPTyT7d1EgUYYf6kHLNu2G5XD44SwbfhwlvwypQtXAd1OnKrhj_8ymgSIEFWj1S-1DUuwTVl7qXLqpJr0x3cWfY9jUFL-gJJTF71yDwAHzFY3kiNiMEc4YRdTDdL9xHs_K_cpQmaNsudjV6FAY3ToQ5lLSwc1uf84KSO6ScZ0s34h-z_26oUVFVAg92_H4CY0kzbB7Kw8y6YU3NQEC-14OefnIv1gzEec96vt5gdCCBNyzFmUn5RtrlQarG8KgUFZ7OPEhcV71Gg7I61FUv_iI-ETLxdByT3lQKhYwBlqm4aQKzyX5ToXz_oeReH66Ss692sxy4sA5xAP7yRExfmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ethIvWfVEnZuc0y3JM5oLgGNX8no0nGNQKa1wP3KaNo2LtTfwRt2Y7EWxQ-7bez6c-rtjuqyI5yz4wKitswjqwWhfutPK_VCrpG9cFOykuDNANUcfB5favVlRK3v2OOD_j0Ok9lXdi3D8KaTtTu8MPieOIYW0SfqTLa1xZw9LPyRNLuw1Sos49dOLllanUeqZ1LVpWoxxly0N4ytG12-fj3Li9YNA_j0-R9cj6zpGKx9lObURT__W7rYTGr-FDW4p4nl1LOiqHEqyuio-CYQhMyVsMPeWkEnJ8HrE2XOpxLf_WA01l7Zw6IhvHPsj_Vr3XlDctuhsw_r9UgZJDefNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvG0P4f27LXwtZqGG7e72us-XbL7ZWNdikRNMBd4WCF-lLS1xIN_s3B0x_yBE4ncImBeZ-AN-lh63pjvNfrOalnX1FSr0UIUchDfOkmTDxbdF__lPJudFfeq9vI2hQdyEe9D0P3KZOzhpScilUqA788Fkrh0DnQEi0Xs6_b9GCuL7cjKgYuUW6Y3ko0-Z2z5p8Ti_WY8aU2NiJipVtx-EivimBt8vg9_ThKT-JOYH0uPmPOQdwn_P66QkPNRMtMmGfdMHDQxHKCtTAGJQX3aIM4oUspfO_QOlub4gdy3aoFKJgE-ZJ2YkUTzHQSINJL8R5YptpbqQ-JnFB0XpDdxrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmlOhhrZ4KEiw0JpRFXTm-uPz2XvP9Q3SycyiGhWdUOewwVKzl4SluSU9HD4BC_88V859nbP5iekLoA2vtTtOo4vi5_Jk1GSSNvKIRnkAy7T8plnSW45qx-6S06WgkdK8qaju8sj_JpTcxzwdV6IqNV3a6QTs0c_DT_nDBGZXDRhytGfYbUzEUdhcFiqEP9Hks5EieCGnRlRkv2FkDeCWc7SZmSg6Tb8bWrHG_gmAzV-9Vyy7GiJchmB9riGlM2hg-YD8v7XBkBOfRgEmUfOXziBJsxes6WVLYVfLWG9Uam7pa1M2GMY48Qm-XgTJGigMg5av43FZagb6feOiZObyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbBU4MY90BQJqD5w9FFsnncgCybES54UYFBGrKTRU8irtJAJk8GHrFKN4qKRa3-r1BfKBUtfRIkTN22zYSsKX-GM4upE9NQkjZxsKcEfeRbekPUb_4YQXrwLPCy8oqpnWLN_uJ0kf1QWubtDR2e9aFQrwUychcqa0ZcmTldd96pWXVo5nHCq5yRqLnAqhmcMd0J20iuTuvkuq792QUyOFdVr-oDQ8MB17cYxxb_3ZeECQSHgspCRY4lukv-M0RKzXycYdX055SlQzIVINZZnvjR_0BpXKXyWIZHG86pbIxfXP7kWMPJ27DQOu73-mZn9c5qtQoElh7PBsoY_DJmHNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvtYjmbuWIUKZl6h2lHNhV6ElQwaTgv1GCpIdtrE2EwuWrxi62WEVgiPlfy4DOXEW9i51n5sbZOZw6SFt74Wb5IGVF7lBLGNLPjP2Wlk9nhzVRjNu3WMwhcZUPSe369Ol9CnVctGK8a7j0c_lX_jRAVbyDGnQFbbUCWiJSMdRyYkol2Xo1owUbjvqXP-8SMwxXH5KvAt5Xw3cprCfR9ckTR7bClq-7EMvt8HA1N-KB4ju9-wQZyQ7YO9EBMO0VRriGl7fiRwc4J8mMGkHUu_NNn1F4CXi67apLm4Ri3FgAnGJxVYkaDESPlkrszK2b882RKEGMGWynu2OYDFntOgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbl6dw09T849m4LsvVPvLH2uUtw0GqF6XRaJdf-XKJPXnnmYCftjXb0xvEpUonQbAwwPnMQkX2OrMTieTFHXoqQOSqVfaZ8WWw9LdPBwp2qBL0wRWukSfy77YekT1LsVuk8gz0uWW_LGacl4TV1oNfi5Knn7UjnIbooVLACCnvNrsmxirh9x-l3MuUWeUfIB3L1DZ4jRs8GZidlQ06_KWcRUp3gQF0goiQDsceoHbKONIGeOGDZGnu5noorb_5BYnKTYWIHWEqCS29ZImEjnmZW7LLAvZ2dlX1C9hqZfZ3qhO1taDxf-osMMyBiScArWfkxwpXAgxLuLERMVYe9MmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMK0Nd4Mz43UEPEFa5C6CqZ5AhsgDM1czXZgNldMAVgcBay3V2bQIOTeVluwc3TDOrxnLkUpwM0npuqMOgzoHS13q0oixB34agTC7BLokBl8lxUlXj8k5MXCuNmpWO5iu26xxz0j_P7iLUtE-llpn4BFpXKwITbRK6OEnk1ebuDK77og8hGlDDlHMNbNqQ8l-inZjVzMzZ0Af4OAz2vNr98b8QNw_T8njWd2wmLZFCapR1eyod80oBvJqO1pkWasMOx0ewoRtfumpNVyULzwEryaiYQNlC2ePYS8GQVxvP51J_XgimJX4C-1zC8nDIYNn6bGHUuZSfW-y_JqCpp6Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Ck_dwOsRaDSxO83NWbzaQJezpuePyWNzUrZC8x71ZKiT3pPkRnaaca-KCgapAcHOf4eRq1wAY1ewBOn1MUz8rawgBRhaPec-H-pv5VT8LhWg1vyhp8_miNSdBcHHI14-3zmSl_olN_wpHaDMobOE3IwRGaWAmJonOWospyAoGzDiUOK6nWIkqLaHnXQqcCJPLyBYTrpKIiGvePsDWK2DA-0SuxKgrLZIuu300z9z0CWbR52OwbqpnGSVniVRhR_cTRh2We2jCMpBAJ04kj2EsY13tFTz-hQHGWeE2MSlmmCIFOHYAiz-lrVTzUX0AZuqs3Z017hrC-RcyXVxTXvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvzI45YM6YrvcLM82iPnlLUaCaT1jKVDRbXblxlsWiWyw25mY5xysR5MyhSTWtaAkl_3EwfV1xi8U9Eqqft8dsWMh-Clv8mkiwDlYg2GSlFAwPdeW6X2ojSdOpxNCJuRp1FWnD3kKbCZBpjj9Dqt_2Mr5X6In-xVvib2vOd34gikdqZCDlz3dD6jDKbkn7E81zGqMbXOvsIgKEoXA0sP6Gx3GxtVW5gwKVlhkX90-IfkqF-w4u4VMmwj83Qt0cr2taRAtj_nRe9RF6d8Fp2AI9GRSjAi-NLzvokKJRNo1E4xw6dFdBXzHgODIlgPn42GSzOo_0apRWyxpmhfR7swlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOOqnnvoCIuGdqutM24hLynFV17AzQMJykp3xiBx_XhfqhtjfNRn6AG7LGLrvZkBsQdOAD5QcZ6t3pWljQA3GWuQ8q2Z4LebYFfUpx572pVk3uV0G_ad7zU1AiH-FoPAOwp6Oise1AlqaZyhmtUMIroTgcCCV9J_fipYZbPC4o3cFv6Cn6BR6mPZw0t7i8PjV1-AyY1YZBWIi-32KGgknUOyZ0mv0m7TnlwWGkK9qseFGhEgfm-NGuE7k0khZji9LkAHLS7Rt46cUKH2Cn3WziOq99KuPRX7z710IbZb08UuEUmyhp4x0WphSUrrSSpm16Rf0FEz5Yf20KQYFbDwIw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dFT8_qu1rSEtPWMlduwmdOJqfR6jipkqJ1QUU_9npSOUgXQwDvHAyg79TvJwRJVJXKPfKU08lXXX6aAu04rBelwzegiBbHftj2RcwBvqxiNo-qtsI0Y6knuoDZAh3fOp2MiArS2jxmcXd3aZ9j30zFSrwjiIJDAtbDY6IC440CjVUBTjk0epdrcB7M2CXDtbb2O5xhOLABhxljXjA8On0GkaqEwShntEL02HBu20SeW141G91DitvGEu10HLe6NwgwwjyDx8TAXsxyq01Mb1UnZDYFq3OFvDPdbPiqqyFfUHfJp69hahYMH2QaMlSXwerSYe2yvKf-wQui1lldpDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dFT8_qu1rSEtPWMlduwmdOJqfR6jipkqJ1QUU_9npSOUgXQwDvHAyg79TvJwRJVJXKPfKU08lXXX6aAu04rBelwzegiBbHftj2RcwBvqxiNo-qtsI0Y6knuoDZAh3fOp2MiArS2jxmcXd3aZ9j30zFSrwjiIJDAtbDY6IC440CjVUBTjk0epdrcB7M2CXDtbb2O5xhOLABhxljXjA8On0GkaqEwShntEL02HBu20SeW141G91DitvGEu10HLe6NwgwwjyDx8TAXsxyq01Mb1UnZDYFq3OFvDPdbPiqqyFfUHfJp69hahYMH2QaMlSXwerSYe2yvKf-wQui1lldpDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDHg5lwVpZSzVFRyfQaFIhHLBOJwecKI6DeV7FGKcNRBzC3lWZzIuRg12-S03Zel454El8XmgsG6D1nUK0OEu0kGVd8RGfHbJoSDxqfbV78VFyPbPb1yqWw1X8L_AiR0NC27_7qiWEx2MQ0q5CKlLDA2m9BsxXGESZQzei8H6dAStshaBOImGXB492zaxwcHkncdXeZJ0aKyYlSlQugIvgWJjittaMJ8otKNVzS3EUIqUVKGSJgyXlEluRqFcGu0XO4eh381uLsPmPZFdv-Qh3L6XPbdsvIgDGAjiMBc4fsRsWhaApk_tdz-jAFl1FH2ni5B1ByxatAzTYNQJ3sh6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfJ-WWvrqn2gZBIdVEfTlVEPHPawpulzoGJptgY1rmbrIkCp1k0lX212LTi3Yo0POKjYAsDpg9jZy-50mmD4IH7HH4aSIFVq-n5kFpDY-KGYMZKWhPeS9W3mP4gaZM9V3-JvrRUo1sgXl4nllLsi9WMs-zdXmm0XQbALq5ZLaQGQkyYpBNW4DuQxnhZw-MAEW-uy1qO8jhajxsqFhfhmI-3L1R9F7YsXKFUB68dUT9dNwYzIgu3DmXqn5koYbOZ5xcwvJHER9TzxO6TqgKl5KuFn8pWd4OB7FWheZ9FMKMe5orc8aKscPfVyqDJHr0q9w96scVo4e8TmdMExTFRWlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toAEArPodf1gAgk6-m67oUEMi38STJeaX7Hzb7Ev6nnwkV8CaRbchs3fsSv-rADS0tJigw3gWpTMxjcxtQ8_uLgeXi0YK8ulIMTM_GT_cE2xzR4uxj4CB7_y9o9k6Pf8kWjLQwq9uJER_qBqlhPJS_NLfrUPNF2Mu6mmSWdISWiX2UeAtJa8Wx-slCDAYQdXuvphUJVaamj_hMQflvuXgg3_TLPxDVMc0sgZvijKvhsEKkIbbKU0IC6KacXblX-Ns7gMa74JbUcOTsYxx3OSqbyEYGg8DC4ZN2HlzeEdOs5vns-1gJjqOh_zOqq-4LdKhH4xw9FQDylwt3osJY_9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJ1n6dfah36PEdQ8OID2mhgzTuigWX4nXxgdHlpBpTs-bm8hQ5xwAwka_PmOgVC4OcE4bwwQlI5RVybLs078Riw9OrmuMiPWhzKIbUok0AGhAaaf0MFoYG-AtZEPb1RHEa5KmBvEtKa_Q9GvOAHtYbJN3_Z5fahjZM7R6k4qvLnfue4TfW0oueeT4uktvANbEtLQlZES5uUJKEZbZYwI91StaW09E5XjJDD53MWi7KVIP9OP2A_3sve2vvBFwBUfytDscWXwu5GnmnwS_1s8YzYHfvAIbR271YNZaWCww6-O93YcJogEkHCsYWwUDNMQCLnLGfwGbEJl1850s1e1jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eL0ccm1Ux-6KcFxUdIzo1VvtSdarB3fcj6CAXMc6cEbEUXeVGvJ2PdXiuYOkPbNjwTgOWrH6aGOvs0hxiNhG2GxSEblJhohah7i-Mp9brEd4_4SgydNJfMqB5hKUoQAOGbTA1UA-JUNB_lFPg8icSnSkNulq7hVJg5v4GMnSeOoAXYrbusTIHmCKAcDERx0ZuSXLGgTl_ignnsO9EBe-n6A9Q45J7WKlTvP-nrt1DS52gb8KtHJJAu_gH23LB0sPRI7GDXpw_rllUtR9gwmASY8y-SqF02KUuIuoovADhfcAnM4i-QXbHOYYPl8vXSu4u4vKbaMFPVL0Z5DX6Ylpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWPfQgBEggOm6jnSRU3gghBrfsu-Or-3bTs6qFbBZCfl-MBYbyNxuOfkdE7a31ehXnF7wZITy6iFw99junlmTRgeSTuswYKb2jvv9L0JTZ7iXe0vwO3bIbxfJtRwrhPxuC_V7YCfzYfW8JKTvsDIrOfMZIRojzZ2ealggymX7jHHYsHEQpE_dCuANYNWWz-3BqGA4j7-pPes9Iz5NmQ-UCmXPXtVdHIIvPcU29sSDZGiXDk5We8IrBvY1TpPP7dlxrNCZ_AQ0aGITsWKb8fBDle_0QgivMh3x19xvyLfZ_dwwdFLs2SHuYTZWOHUCoBu3BYWEXorJM-EXKQCUxJPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyD2ylQHajMnaN6j9Jaukzfc3AIzjOgGSofhbrxxOPA6OrOItI7WzZwx9Ew-kD1BetTBgbpybKQBcaB1WH7jynIN_6oyBhTncmubSRhuVorAWltBsBVMLET55gGaMHkhdQvv0HmNJoDjw5MPMMcWbMXHkgnTmMDdCy8gGhahnSVn4EEuzA9wql7fSNvAAJYOqQ9_wPp0iSNQqItp-ZUQyoKLg3gk2WEkmFr6oj4ZO87Xb5Crghpn9LYqxHyQ1gz17a94pcaBiGyb31bVSqHhkYN1Jxk-FwrpWYDBx6tnPzFDy9Np3x1vja_oicFctW-2Img_TGhEF7JGD4Kld0be1Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=uWDkdHafd8sI8DHXIpPvjysrUQqKD-jfbSGpV0WXTC-kKY6H4u48WygKIZMVRm3M1_ztoONh6c4TKU5pUxz8uX1q6dBJV3sKmyiY_FrUY0epsFW6dHQniE6Dc3Q7939XsHwvO60muDQo61dOt-2d2KLtUsFlLBs1vD59XUvXzJt1j5x7j6Mk18UlbV1qc7QZ15VVuFN54j0HoM4u2Z7VplB7zAE30pUxe1xgeo0NSEvvqeF_LFvSZdwBgsdLfUoQGqg8mpVIatCvc5RMUFGZ07wlL5psNV3fx1IwEmjqS9fn-z4okQ2TariWULQfkP6b7xOXP6vlMDhAmFFtIkxpPL4ReaeBfy-ZFlO_FnqdyeYOvnqF0XTtXtAVK5cdvXCIDhYRuxbt6NVrufljviv18b3DJ9fdnP8a5a9fN4V5k3di-mlTHD1aIcqu0zNfAYCa3VyfkxMF8v7-rvnNnf1wUYbCSKt8K6STLlp7LjICfkI5I_0hccXbpXkjIYn141FnLXJMQrIr7zxvLQGli4TJlJWFWSFJgPG3eClE0pjnfQirU9SrdnxgRL9_cCZV6GH7BbwhggmRhFIs4O5NOw2eWhCNo5ZmHDHyaXexzfNyhLQcOQlFyTrg0TvwNi2ZGmFVnnWCdAJVtTIWpZUQZv3V9Y6zxMQASf-ZVdZNlQJ_i9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=uWDkdHafd8sI8DHXIpPvjysrUQqKD-jfbSGpV0WXTC-kKY6H4u48WygKIZMVRm3M1_ztoONh6c4TKU5pUxz8uX1q6dBJV3sKmyiY_FrUY0epsFW6dHQniE6Dc3Q7939XsHwvO60muDQo61dOt-2d2KLtUsFlLBs1vD59XUvXzJt1j5x7j6Mk18UlbV1qc7QZ15VVuFN54j0HoM4u2Z7VplB7zAE30pUxe1xgeo0NSEvvqeF_LFvSZdwBgsdLfUoQGqg8mpVIatCvc5RMUFGZ07wlL5psNV3fx1IwEmjqS9fn-z4okQ2TariWULQfkP6b7xOXP6vlMDhAmFFtIkxpPL4ReaeBfy-ZFlO_FnqdyeYOvnqF0XTtXtAVK5cdvXCIDhYRuxbt6NVrufljviv18b3DJ9fdnP8a5a9fN4V5k3di-mlTHD1aIcqu0zNfAYCa3VyfkxMF8v7-rvnNnf1wUYbCSKt8K6STLlp7LjICfkI5I_0hccXbpXkjIYn141FnLXJMQrIr7zxvLQGli4TJlJWFWSFJgPG3eClE0pjnfQirU9SrdnxgRL9_cCZV6GH7BbwhggmRhFIs4O5NOw2eWhCNo5ZmHDHyaXexzfNyhLQcOQlFyTrg0TvwNi2ZGmFVnnWCdAJVtTIWpZUQZv3V9Y6zxMQASf-ZVdZNlQJ_i9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHdSpoL5gNjIOJCXgmhTIp3gc2Dd2Wn_7MGsXxToaPOeNYhQECdhi2jxVMs7E0h8DkfO43ZI6s9Cut3CoViwghBeJxLWxprr4HlNc4XIjX48My1LGr9HWlDw_QtskdwFK4OXfYB3Brh97wrKh-FYeOKxFdItEI4aHDeELSb5omcPbFuPVapQ8BVf049wqbcBLh_ga4MvMkAqg93_pfM_OEdTc4FjrX7jmPo5Gs_I9g8UP1CgD7_qFCMpH4p4edp8s_H6Rtj5gPcvsWdE-IadBpqwUrJabXNy3v0J4pEQxChEO--jh2m8wP4kQeSl_S5v-hroI_p4fCVnV-T-pjUzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kF00RLsIKtaOXMovMDzJ6TZIR_AU1Th_iyBLPQdmL4BBCG8LtxVnDaB74OkZaaCnCuoqy8R6bDqq3_Ko21ySVMzFOBEFWQig25h1mYp5Xff3FWB7dJbNMP3pR92ZI_LexNx8dfKsUBAMP4IZC0ONyXX4sdTmUpGndRu9PBj_TnVIXJ4m057JKQjYLFPs1P4BJFTje6SirH3Of338C2yvc49hAYOmv00rTAHfDn8PeMEmhfdJAjbSZLvmJ5w9IuJ88EQgVDS2QNUmbPOHru4rxZRZEeatq_9TUgJrJPNF98zxJPByijqfo6pX7cMQysLMr6GLNwhRYxFPZD6ZWJh8pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GzRGEHCESDQHxbd1WKnDZ6W1N-dPc3wZebJQrO3Ls1qYQofmxnA3CtmepkFAMK-9hW296i6Me4eA8fQnfUoIngu5KeCFiYgrLnLpm7WkuLK1ZBG0eRZetwiiXxIj3uenRdPwaFtK_oVDMQO6WzaYhyMnAbaLkXJMYH7zUD-UxbSvX3_QA_0cTP1DiZ8wp1zpb1fsqAGpGViSu1M_A3iZQ3V5ToA_NA9ifmGbc16voRO69dI70ObgA5n12av4R2vKHBLUCJ7_byfH8gOhnQQf0YkCgCp1pV0RZHM413Ozo9IBe27CVDSI5x0tSI4JEm0FIyuq5jhlpCjItUSP1GP30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDheDCUjsbhCx09kch0ifySrRrPHLEijY6EhPXeruhaVoofi3EnO98HRM1xrroSG-fOhqKIO1eGfyKLw750KJSun7VGVs0xrsJO1VXFrplIw4xVXV7vhVm_TtuaPm2fSZZYJNhrkoDgQJo0IGXHW6750gIkv2ekceUV53nvw5Tc62nN1vUDKCvQeH4t8T68xXAmI89Pu7-wm1bmK6Am1Tti6dP2Jo4CpgMJsnOwwx2R4qH59eGZ7-ABaYDwp3MocAYXPU1bfv4Hq1-TM5JOGK-3dL_Pff5AjeVHfBN-tbJAnWMtubH7SfRdY9Xjl_BLqVSO2V514Vog_a6pOLMBfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxPWrJ35ZMuRvZ-YVGKlAvjOnWG85nPQ0WqMzPcKFXaF6Obc4x8HefBzOtsXCFNs09p2SyYW9YMpUwbfGfacjCt-t7aq88RHPVKKOTrup2i5rYKcIK8p8PdjFU-j_rBAB0CTXIgkNdCpVT-eaUt43y00R3V9kcl_5toE74KBLRpaupubINo0XMPUWSe9xhhFaEj2JPDO1-gmo4awpcg_u2E1sns-DJmLcv3lR-v3rQ32orTcozYW7K0Nne6kLF29_FK3fquSNaheCmQwyBhYuCYT9rVIOeC-N-ZpcFJhqrVL95hXN2FIUd8wM7nqR_5ENx3NVJ80roIlPoUUUJQ3bA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZUZUGz2hDDGGlA1azkY3MOk5cpSeKq-RIY5JO3EZKrYLslcYN99qxjiIwOSWk9_iRp82l4KqNjNHv3gp8IwhKclTeuEmwE7I1ro5j616aqXt2mgY9OAVYe8i6kyQPjeZRpasiKUov9ntyGV841RaNxHqh9ZJAMsHFkrnQtyi3D4S99spJiQpq7eICaUoZThMm2zuA6-fE_uVYNhNfQmkHc7N6S1u8mXvl_7erfIZS9BhFO7VUvtAQe-YFW0qT86Kc59HsrgZHshtPTWjMDBr-lFQozC-bkyi2bW_vyOAGFbZIH4dN-7X297mecLG-yT9qiOPQqzBO32OZoI7pGdCPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZUZUGz2hDDGGlA1azkY3MOk5cpSeKq-RIY5JO3EZKrYLslcYN99qxjiIwOSWk9_iRp82l4KqNjNHv3gp8IwhKclTeuEmwE7I1ro5j616aqXt2mgY9OAVYe8i6kyQPjeZRpasiKUov9ntyGV841RaNxHqh9ZJAMsHFkrnQtyi3D4S99spJiQpq7eICaUoZThMm2zuA6-fE_uVYNhNfQmkHc7N6S1u8mXvl_7erfIZS9BhFO7VUvtAQe-YFW0qT86Kc59HsrgZHshtPTWjMDBr-lFQozC-bkyi2bW_vyOAGFbZIH4dN-7X297mecLG-yT9qiOPQqzBO32OZoI7pGdCPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVB1qR9U3z4vOPuShNM9YFpvByRcjL7o0OSMxCXyVP1EzIvS74v_cj4Uw8TWMR-mneKIhNeQ1cERwozIBnkbxabIPX5skD9IZupoAGPiHCmzLe235OsiEvYh7nF8A2AgF_wUPT_86hStv5_iT-Fcrl2Cqd-DHjWdHsBy4kjK6qZqpiH9xa7Yl3COOGMMHAcQxElCnBg00Kfo0vC5Mmp4jdDQaGRjpbYP-6-veuyJs3qZNpjsLj_7DJiOgCaYQjpvb9UpdjnMWQJvSOXrmvIu_2LwYYj7kDWX2TEism3k0be6BFIgukEYq0G2KVtZXfLqwbQ7SDxFvGOLdTpqz1mTng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiUpxms4T2sb4qEyJRfgn2_09Erc4swYEuF3Ly-_YAMhIq6sbuib4GFHwRwPaO2Wx630GAP5yntSaYHxTQX9Wzsk0eqL9XdZZYxZtwsheu7b7wrHoT8hz3kwMm6eWo5OsBRbpVy_xfoJ1rw35RnYspcCw4Ll_ChYreM_Ne_UN4yupum73wDCNH_E5uAh1NTM5VVUMs769cqK56uaat5pWukldTtRgaMKuKtJlpxolRvhAAKf-kbupZ_dXxMOEQLRvtz6eV4PLjv0X7Ng-7agaMtcwXjFysxmEFj04g2b8U6IgqXg9upLfnZvmnZd_A9QL51TZs63hR7hTEuJyPo75Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvG_kHZB472SVW972vIbsD0vi7mD7dEMupMGjKmOovyPLChNiV5p9tdpWNWvt4cghEytzwyagRSzq1LyIJVDD4CgfYkzeBp0_hStPd33IoS41zQEM6fveHgRYAW-TT4UWOZAcHqLVQXJcZbFai5-ij2phSZiUM4fMXwuSuh4Mr9h8QiRSUytODk0HzET-LuXC9Y-vYArsscZq0VAriHUrJY6zFb9jPZS8Fz6jBJVpu-s1xwIQAQn9DrIXzjOwrW5oHlVyV8HkEx7nustVSee7sA3aVNhdVvV7C2GfS9-3K_OkTolCUhLTJ3gRIMCMI4bTewNDMLPt0Hm8FwkQmH_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqQa30gP8Mh6Am2CPUMd4O09cdhDbDEOIQvJJF8PsEsW2wHDlO2_DLkUTqEfJXO8QUQv52Q5n8Zt8poeevfDenHW_nBq3qLWHcBZ3RVRw8mk_UX0-xnAdH3y_Zj0JteCL8iXQf4PXl6k_Xgyw7Zn__2paXPe3Dbg1gsPxWVg646IIYOefa9vI1FqDmX8MxZHgOUcQMZQ3rL7YJ7eL_HgK9s_vJE7NBEXcWoSeKkjfrAaq06rTLEMx7VIXxL-waXuykMRVD5hd5YLqsXSYApD-XbXBHvli-Nkt3ZCfU37yzFXFxDU1or0naF0xCRiI55GBDKIhNt6wnOpgLdhnOuX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hio5ooFC46K2GwN_UGT5yBWnrpVzkBr5rWx1gWlaTN4sGMhr9dyK3VEyih48Rdq7p7dNvwrS04kQxZ5dSpvs0bzcovgeHKDMyWMYYpYiGXu5YfRCkWSwvb8Xq792at6nyoBaIPWNxv__8iSVIVxu7SSZSx7y6WuBSvclN7qw-d63XSaF2GBxK3jPnAFmjhxf5rW8Ony0Sxjd-cN3ZTQ6R8zInvZN3jz5JFGK81VAbRE9bFTHzwz4cAjnhFrG0Am_vl57dvYiYy1WnsPTGjaC751mPVTecFkQVZdLzJZ_fyQZC_snIbr_da1gth9NgLMD3dtJGGlkuovWPOahKvYo_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW5fFIvZbH4wvMvFLGuf-jVREmVq0DBzMrrlc0iJRL5xtCg-3dETvIW1FTke4o-wzSmIqN7Yj9dz8F7h6NJLmJ0Vj_O4AktAfldedT6XAGMnQac7F1VJg019tV7w0wcXiMp5ZTCIXm3AS2miggNk6ENJ8tJcv0ikOQpGZj32irKz3hGMnPRkHuCgqlZLP31hQhj0OAyCh2KJwT6h8dm_RzBa1XPne7yZYoaQ1XBdq4mGVHfX76ZsIa4NyNGwhZO0s3CNH06eRAU1obICdYa6SlazOL8b07LTfLzjO5g6nEY992haotx4Bjn183hUehnfsDZppgLKZOSAp0qQhAHvlw.jpg" alt="photo" loading="lazy"/></div>
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
