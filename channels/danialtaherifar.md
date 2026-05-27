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
<img src="https://cdn4.telesco.pe/file/QXrD74LnHiZ5L4kJwjVb-sEeH6R0J4QcO5fdVo9GUNHXdQ0hPKD1G0ye-OgLGn2Qc1tWCiBKuus-_ZS98UrWTJbZgvhkrCDDBkx7mBjAHcVnbylP_sslpXlXQhayYvP_Bf0A-H9JSCLQEaeP9CPyIZsyN77HzaF2FyA-1-9DzNm9BVKA14imGjksTvNexV7n2DTRb3I9_Fmj0X42M8P6rByyzSdfy3lv-M1Ik0xWH9tzu9bKqYBJQOFJAPmGUaH5B0FCtvxt3Ef4KVcY-4qy021JixqV-2UFXkM3J67wyoDWNHYaH7cjk6yT9C0yMVONaqDS71TGFbV8PW9VRgr9JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 227 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 330 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJc_CKadHLiBq1j8ZbKM60kkrSbKWEkABQIqFH4uxqPRUi_PEx69YXmrqFLGrLgiWJFfEX0Rxl5T6XsB3CfVnyktUcjHaALGBqiYzFx3t0MjrmnIicyu4fEHhqFunUCtWEqeRGrfcCuSi6oUnUTi2fv87r0BuEcc9KZgiQesLChJVGfSpSwQLHKIJa73WqXncjftdUt84PEyNuI1TLptqVwgk1cbdtAfTy_VPCV2vh8wJmuJ1GKWuZVn0TIGx3R2YpsvQEeU1CUrjYGOqNDoUfrGTfg4t0twFCt9_T65YWdzdiVq0-9LZhhDpelENv_btsCJluCf4lQffIbT8PyUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 426 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RinpQfzWU422E8RiBuAClkzWTgpuHsvN4h3iA9hrYADpsCv2Mt6bfHHtACavANU9QgqqqbiJh9NeRE80JZC8D21KnL2SL07RR8KDk-IqDEkouGcxas54te6-UmVhnZrxJkgtk2-zreI9cBFRDs8JonKyp2sOcLmv_VUac6V5AkjY3fvsftyIldbbOykNNUui3ooJFYAwfQXgm3wXU6TJNRmm0CugyQuOfHDD-kHCTJ0mXXoAJtP9Ay_lLRFeYPkqvU7U3IhfCgRHs71914DRd6DMjUWJT1IArJ5TUIg5ZNFfUQMiP7vB5D0AP3rz8O04EbZ9lbFvbYj_9iSnsYeJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hmM7S3h9mqZgG4dw1zbIwOqbNddKP_FoMCzNPm8M5vm4zHCNQ4j-Twywxr7E6PYUbEEYYSYDb85NqbmgMHu14aoFtuLaLW5Azmc_VXE0Ocw45myzARWYjUcVodrkxFGzUjVwu9Edijt86wa0KiB4jdmcC9S2Ui-Nz0FVRLB79hBzymdy3pbumw1zjyyyydkM-k4DtvX6YdckzRTW1JbuzoUdLw3Fno_u2rNcn_5X49uSboAdLafCN_tz_CjAPoUEj2w7W2EGaCqVFWZ-9AVDT89WeB0PardgDLo6feTe5h3muUd6GvAhUj3m_l55rVfwpFmsh64zVG6sjQsDrh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 988 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dK3CsTYoWNR-jGvp4LqK0Xl7WDgjbUWt1WF2j6XSewEeDMCHfXafmKlBCTCCtPRWIgXBzSxoQ22Vmy44CCNL0uzhtFezuLLNKEMqse9h0P8TEWLK0u1N-MMDgo4maVhthA0BXe7paA6zZ5LCOnTPmf6CQrRpuXO6OoS04qS-4ZCo2YblwB9YaZu3H18cwzAOZcIXDi-R5ps1DHrv33Eb14qjRNDRzuEqNOsKefvQw0HYTjoQGR7nLfBH6-uQcoTc-lT-eHlyxJ5NFKiMg8gTyf--hygC25zd9LKAF3bDDRT3ueSlxxM3Ye4lacIEY_LJiFhpBBX_NOsXVPCpkgMP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwfQ1vxHzHrxYfaVUCM8iOPRsT0smZHe_I6a3QeJoep9g2UK3ESyEKvNd6v-iNCedlx62Ce55SWsUtT1t0RyVcerpkro67MRCoVKx09mDrd4sd2rvyj1idDxfP_hDNSxvSmZKvnYABXnMTmbOEbUYk-qP43P-jnFDFaXUM4Bjj_QN-C-ZNccuel_X5VOAU_seb4UN23arDPIXJGmXmE8Boklb72G-wHDWPFFyspHsrAHLz-s851qQmDNLA6ShGa3kBqB32ag7Qew9TP6frSMStjfdHZq7GtFNo0NXA_kXqdqqIFGiFKFziFnCWKwL6pI4q4ddilQERu6tkOMQtTqeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuCTDU09T2rYbVBV1bnsTV_4r9o8dopurxTjE_z8X9CUtnFNVUwKuvCqu0LVue7OSD8TKODupPyHEB2RvYLw33Bdnzir0tdW1mFAR4k3jjRWJEPc3gu2YPWGhPfZq-YxL7aKr9Y2d-Ez5R5AyQuxqr1bEcUQOaFKyrid7_HIfNiRh2beE4VdPKJWAVv89OW1eVwJ-rYRa9ENHRji_K43STzpFP-SyxkvWgzvRB8iWtLT5AjneqAbm9gpabfZhM0ihvbEAUDN_GVLWDozvVB0LzJjjiNjoDWEuuwcXmbVIchSANwb2yqZwKwaEfU9GnMV0MKkidp63u2FSy5GnfhC5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7L08y2Kz8OpoNT70jLwWsggZ-t_8OHg5gsUuZcGo7SR0EHa1t2HKXH-gZjhRenlNopOZ6uwGusgjPXl74HR9QE4xG40POQaVjbkH0IqkMpr2s7c2BVIvO5rA8TF8UJbm-Z1ZylEeoZrOcdEK2TDuKauaSjQte3UQlRycHd-7n7MsizySf5P7HHRH2snmfRCHPiuoRTkkAXQbp-rrFubAD5ScOdujFMolDqRVALdWRU_1kvixXbkfcLNT1UTuML30kWwqMVyhYiTeYYnY3OiBolCUEC3QT2KHhjoPv58PBwDa84p9mABdX4G6pMVQhpa1veHU7eRljZCRbJGz2H9-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMDWmyS--AT5fgCmdxfsi3nu611tjQW5myiH_RQOryY3uAz1gdliJgNmzpECAR3bGsPGvV7rrpNUjxtnJNbG32M7tXmJEwmeUX5k-v8YF3Lx0bgGdIPUjl-d2vvE1iXPZhw3A-EXCSuKVSlekUXBllnc3JZscKuUhBa9t9CssflC3WMAkw7HAc1nHZ4DgQD4PQB7rU3-eyrbvfa6uZ0S5rbhOg-3KE-bCR_U5XjidxXOsjzG9wQF9Irmsr85aIxz5rsTMLdVf0jarfoOGI4s2zbZzF4WXCrpIcjwy-L4pmAfwy5cDcWwbQ6ob_dDvMj_W-6p0xp5q2Js4RIUWwWoSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T098PdS2ld7GZpQQ9AvzB-SoNgClo7LQip9mdl9oMHQGy5g7qpV_y5nsIJrwtmmeFpDmu54gBuFc344GLOofXmyHX7cl-n-rP7C81ajD7Aaz7cEGmwdU3Y8xvhKB38_UkT-aDPyFoyEUR0zF9LAPuUS_kXgR15aNdb5fXSVXu7pOYOTI7D20HAamBbNswEj-hwVj6pvN_DXa78Fv9VTce7fUHZKelNthZMDsJVoY8ZD5dtWst9veRgHglr0GFOXJkX2Sb1miI5UZd2V2uqWASgzIGXPZUxUOHm8Hviny8Ue5UikRSwLEIB2Ljch2CKjfPQpLMHPPAcvJ4wtj5YQDfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6Xi7yekqLQGkuoV0WGQ_teM-EvY3eFJP_zaLlHuQX-F_LetlBWjHzeGKmH5kCLyIUbcy0ycZI5oYnJGw-wYuVY5nvHh0c0pvQsmX-CX5jywtx7qtQ0BNaKLD1uWov1M46N_nlOrnOvyf2lojg3apPdgPDCrVjZ50CT9UhskhmTXe9bipDql2wlVoIzL_pHOm0rW-lEcagBqzxakzajNiAEhjKyFfmo_k0GlIx9JeQlXpXntJPoYYT5XQIRKmdVFXT1N5EMMr6xwDQWTcj5LxaHIaE8_UZmwA6kbHWV0vRNIebDqYhi7coCaKxxiW6TuGus2fouqTjShe_YqpyP62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuAzmEGuDOKLJmoILKwzSbP9fpq6cPVhsydGGYELZI3k38V_GKde1lXeBEiFDC8DfhIzlBBYS-NA3zSRN_K3clS7WkwpPdOGLc5ajr7rkTSd-x1P4iXiZWV2pwXU3_cuwQA_Y3or8gxOedhcKBEM6MPwqxRJFPnQZxDbhjHnWVpw-4BQILwNj1uw9KFpnKupwbfsjVMOsAzfRs22OvB5_VBPr2MWqREHTdkDLA6PompBUTnEIpKT7FyAP4moRt43eZ51o6LJMt2liL8wD-ev_hnY6iJvpTW8pjUuxw-u4mLUc7XCrdHnddmtjr5a2K2UXVvtdUSDw6paMIRXdAxJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_FIs4-lU52-ZN06iHGwVJwtZfhfAaPo_srn2rTzTmSQ59mVDOKIvTcE1Eb8Fk2AIuImCyKbqnsY_1KLounYtp5goQNYQX9kjbUYrxf9fBATE9FyaRngmaQPd1oxxQ-gEGiiiofjEWpjll7P_HAROzmYRWb7pXXw5GQ7yYH6x07sRLkm8F8dBcp0cYo1axQBQFTMmqtKm2q7OEnxMCsi-Vta4UPyz9aRUGiZH9keoGwWpyt4gKWiVNH1ZCRasfXfOc7w9J0zHopLwVUxXOjkyX_RITnnVelPeDVqLVHWVDl1w8jefpn_-F_RNttjuXZFLM_IRlo2LcnF8PE8oWENeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmYEbWCRKSvtzxxQT-j5O6NGXGigBcZON8cw89NI5bPxKHrRq6kl-4teHGHKoePJAWshMjMr4jsP614sygatwruAQj_I5D5ckEK7l4tBjRRHSKwJASwpxtOEY0uyKWCQmMpSDGD_SxTfR6IMw89Wzo5767QYN8Wu5palBQ9kZsiXIb26SY3onznks7DDX64uZa0uay1n45LJemBIxLK_5bsPoacCPdMumdM1_QrKK-H8mlSwf_1Yw9ryxkA0QJzaYJPIRzS92vjYu56D8VzOZAym9aOzPC92A0R0W0s4mlfBTo62WVBsF_5uDZFyXyalLOm9x3MKvDvZjYjTX90PjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC_CKxNqrHWqaKWJr6VswvZj5-jahCn_nNN3m_BvdKt3G4J9TPKwxPHveFB0K_mlQr_9rtDddFr8VRmhunIF7ao0Zei2Wk9JlngzqJORtUIa6kXnaOUOkHTc_xVF9OR73_FaQgcWJ5GB_WDb2dZd8ivyavwPR4ipWn47_Rt1H4yIotH9zozIGMZXobpBCIQbMW7Vc4rPVv-59C28Fznj0kUHVEf9dca0q_YOBO3KvgdKOTa9KXAQmL3iH2OcVLu5Rg2xbTJbRu_KhSce2u3Zbi2yqYFoll77qQ6RsAgZ1swMrppkhGm4-lFEN0z2RMNq8eUCI2ItoCRMHGG4E3zcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=lMCWKjnS5j9BsyOZ-Jv3CPXkqttSaIvjUKMDmXukkTZpCt5y3SCIhs2rdLG9BlHHvU7XqxVdJjxKqavJ8D_M5uxTkvTwmTD-CSkPN32lS7m-9xBLDcID3laf2A29oqHo-aNV8SkE_dEMgPhLlkKdmAdmd7PmE0KWdibPWX6IgQuvdrIRtr3HKB1D9z_EHICgG8PFvamZ5pvleeqVD105NSj9w6xFJIAz85H68pxWrin6N-gZs4yQ0z4enpfUIz7a-dl4IWVkJUnaYb--zX00LtYyoIYVerluSl_dIazenSg5zkRHOVPNiC4kUf6D-R515N5U_Z7zvannZF3gg8CaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=lMCWKjnS5j9BsyOZ-Jv3CPXkqttSaIvjUKMDmXukkTZpCt5y3SCIhs2rdLG9BlHHvU7XqxVdJjxKqavJ8D_M5uxTkvTwmTD-CSkPN32lS7m-9xBLDcID3laf2A29oqHo-aNV8SkE_dEMgPhLlkKdmAdmd7PmE0KWdibPWX6IgQuvdrIRtr3HKB1D9z_EHICgG8PFvamZ5pvleeqVD105NSj9w6xFJIAz85H68pxWrin6N-gZs4yQ0z4enpfUIz7a-dl4IWVkJUnaYb--zX00LtYyoIYVerluSl_dIazenSg5zkRHOVPNiC4kUf6D-R515N5U_Z7zvannZF3gg8CaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyFsX-URXAGJI1jad6ngE2e_AqUsFxZPF7XRqPR7rYaZRJgNRv-WUiVau-M1EmV_8g_1GwEuBwCJ-9MWSbZ3-lzcNrR0nHKSYc0HlW_3MaPl8wjgkzl734RavcJ3xEdhkzsQ-z7q5gTUqgu2yT5CTalzT8X_iTTogH_GxmcZbWNNegWE9ioxL_pb_TutWWm3NKYgWdgHloA8m-16Ks4fJU3w9romNUKXVOt1ndhORzv3_5E85m-FSO6iM0P4BkjbU4KStLjudYUemxHXBgnKt-P2uWfJWj3uN6kxQ9jiz1lNrsI0PSfg7Ppm6VcxlOJNiH23AH0GSzy2NVpixRK62Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0mdCErgXVaK27DrHg9OdwaLHnmbThOah_FhkJzikDfYfm9jBqCgyyGA2ROmRGJRycTtkZ5QuZAqwdOq5eKkbeq31J_2ftUAfG5Vx6yBjkzxNa03uvevO4Nu3HPONNu6B-4JLPXGSU_NdqBmzVmKGHubmQahHKkzFCobgnvWkZrPPXgRlACEMELOoiq68tXOhNBuQnveAsHmN8oe13zFwmWwfTfiyDSCYVH0XmzZ6oYOt6CKE60dXLLwtzIfDcVzr6JJaXF-S-UVug1URMURHvIoL0-Jf9HWzhdaPTZUUGCvQ19JKP3hMr6ZqgK-1WDX06GWtZ_PDdh9_rjeOY5Q_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLgIJHK98sfs9NJ6r241TjRCJbo5ro_6FSZ1fUH4FTDwq1VodfsrRV-8hGTg7X_SKxZ04Rx7xCNr0yRCRrlCHt8X9g8IQ0yX7YtZPQNvGdJ4hWnZv1mw-cjaXYZ4ppf6vVES4bnj0donficof4OL3YH0P25mGYIHgYNqvNHV7n6XsNEIvh1nFG6hehau58h5VZkp0JURUKpJqv6g7JvroIuTOYSjtAfcJS-pCsmkAa5u6YvV1RVu-c6tb-FHjW_H_DZG-hGE_gFgdWfGDydgnVJlUf5oiS9jqIBWW-FIrXW3pon8IJNPZj6HZeRDB97w4Hxr5Ihl20lgdv9aEj31zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgyALk8R5EwyNK5l8hzHo7EiNVpEYNbrdlQFeofZTgU-U2l9-T2YawX_N1xA24IdmYr2INPs2-RyzbaY6PJOfVtEw95nSf0EMiM6ELH3ccN178cxbPS0m54mixdoZLUU-uwtLQhIrMO3x5s7Ctll1-mQyF5molqxgKaA7nC-2wUdHMrTmfJtlzr8KD1zgC9vPbw8EOv4dJNAZThdzXkPfPIsCeczN0GUcxjo-V0tSEW0RtSmiQZ91BHlsU0l_Drh_5_1QSYquW4W7xgjGP7b0_yL2W9mICu8KIj9Cd6_-ZCFgyuHlg0RgWrVOjgn8UHKRAG0VDRyiBofmEnBLPdxEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmCCPxO7jop6jACgneccAyq4i-MCSJ07PXfePF2Yw6d5u5vpcO9FVmqoMit7RSp9YqqYt8oQ7bPGzBFKrA4AOKKDxAnqlpO9v6T77U7FFrF5KxynKsbq-5GEBAWdhAJB7P74i86QlbKkUmS5qOAZWtKrXf97WK06tTFgpuEtwWbTq3UwqYCh90s6gNAQhd1VhHn_zgWB_1vkOG4C1uHj50Ps7I2xp2zrJMz17nkrrwFyDU9TrwkXSR4dduqs2DIQAkEAr0bmQwqwyohVL88FGl8kkWimqnw1eofYgZEBahxwGlIr3gn7K5EN63_-oCj_pCgqg-Z_zyPVX5wvGD85Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZRFuzAM8Lks68KTUVd5HPaV2kh-gYmQpxX0M6a43zEO960Vodk28NK9TQ-sIt4NGGsQj9apG1ust2fJB8bt-50dGJysEOcMo37rRvMldyNLP7TS4ArYVOJ3CbdQ2YcYOfaSt6EEzWApCnz1Fzcgnk4i6KaR6QjjK9_fWTqMRiInOXYROojhPtUQNnu20iKAzhZs-54pb1rv9hoXa68ELEL4GyeOZtJvB_VhYC1ye2iQkVLRTuoU2bD4YdBiiHTUV9b8QsD3n8CxdSi9r-PvlbszsY7Q_AQWX1QqS-4PsE9s-3ccVDdHBRONQar2UbdatG9iLDl8Zp_TpkD3WH2kNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgoTM0OyLoWkJQBeHxHn9B1H8mQDDHURvmd9-dTaWntF2ub8lKpzu8NbFD67rcvZ4JPTzzQKaCnWTJU9XDyvPLQCbs5fCm1OYOhxQWYsN5vkvRGIiEcP3f-sH4tE6p8LpyufWAjvPRPsNfJo47Ueb38ns25zU8ht20nvNDxYe1NN4vTrQWJetOU8itIOuLFQoRMXjSQ_5obvCh9EGWTjPuFJm5nUmuWfyeHc0x0NlsoSnK46BGP6CLKI3bsCJ0-wgQC6OWet9xm8bHmElmsD0QTG1fgSGEp8zoG6UGxwuB2EkGML6NMPQ2MVaAISASkPaO2JpXzIV44EwyC6AlT8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFcKwvm7pwoHTXAgvCoR719yZrWFJwjmMdNpfeeSmu1GhSDKY74tRDEUYNR-N-tbe69xEgfPlJF6qR443LcPlc_CoK2uLs2KcY2mK1D2aPj_Y99YXYqVLo66nz4xpPZ2zvRMW8y4gRX_F2poR5RSax3E62ZWhS5vUS58bEx5ksGtM3_AwLabG-EXnfewlBKyGqt6q0aVnFh5jMxXEYKxIQ9qAsQVyKOpESPG4RMpxRtDnEhFNeX0nlOwx1hqX3H9In_Nt3aOjvsUw3Y-BcnRitiK3DtSoDZiqKIBZIPKG-c9n9ncI-DfQsfIEso_al3IL0tPN-arn87JcsWTZGaHAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef1PiYotG-4Oe-2I1Z4UnyKIyNA_JaapIgR-E1fhMSdnFPdbC30iPkiAwRQdpvO7nnc7mbhPNRo4sREWzGjf27KIdDNIPImkvPl19k_5G1kErPJNnEr8Bos7h6KXvMghLr_UIndkfqHXtoCHN1nXxuUjkHc3hgt4pM8AuWdueZwrRYLdmA64Nd10115sdUvAJMBdaBOwwb1WqGcq8bv4VVfnJw0yOpKQq6sZ-mp1Vf5XQItaCgy-bnrgXFmQBeVOiXNbpF01obM38l0G16CI0BLIhmHYie16KVC7ohe-x2GH_KmZyjbJchgOMtesJiC_GJjYev0xmr_THm6I_dI-3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g271Y47SD7eaF4Nf-d9A9zqoMmrCkOrhtu2j-sPoZ8ukKtXQbKLXxjMeufGOC8pjRsU3D3w9FwLmE3kXFMC5vm6BFLRRr93n5L4IarjQFiOImagKj1YnKJVe-8UfBtZdk8QOxF6d2kcdagoo1EZ32XsrwnqDubDyBdSjzeFbzBR68koW-GxZirQ8FovVgc1XjUnokI3tbRjc_MCcpXQ27C6FsyP55fKPZ-78qupeZuxHggX1zP33--k6UO6VsvzwchqL0uFNrrBhE_Saqd6Kjm5ljmWhC1fn3MR236tsCqaM6fmvNqyuQJAKUAKB9g5yUTcDnvkBIpfBR5RAJz5LzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvpN8DPUFV6FetLlfyMWstHb6STAC2cmybEknkmYsqu8kGK8zNDW5vm9JZKuYSHw9Q5inH49ezNCA1UH6GnSk4HHxz9Uq_b9Legb-YwD-8P6ysrgKZ5WdC3QovwEsbhot96Aal2ZjvdvOIdoLPESzZFFXL6UZvdVUdcTAYRMteD6UyI4dgzzadxPwJcdrJsPRvwIdqneOr30I-Bf4qojhLvgD76sjem2LYt3Kp3AlJR_SXCf6RRMJNOSlvfsndOVuqwCJfZ0I0yjCgnthWRMLEhZTj9HB-dGaDG4PFCfX45jgLM9pwnMP_NTJaxLwsQdpAJNNfEyIOUcZScHdJ_FAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6_0S9eai-uunQGsoW3UZqXh1mP-B5gQzIgNtKEXXfmEh98M6qF1cHbXAClWyuLhMeM9xLyuGFEbNolCzfaYG7L37mi6OewQPwnG3MEqM3-Omzqr2xwk03XxSMj9ypwPTN6uhD46Z88C1Xa5hnRR6fcTVYnisDGoftnIngoVgVzG6IXcST2MgDBPeVpJVImXTLpKAV-liZuMLyRtcUpih_oXvT_DfdzqPG1geF368eAisa8Qm7YTleGLU9cxS-aWT4blUx0oTCVPx3hoLEqp5jVUD-tVpkNsbS42F7a9XYb_LCp2x94T-ycSwAP415FCyxRmUHoKms3DW2HjY59L4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJ0Fh3035FtmBuALERn-fQzrwPgAzRkB0HIaHFg9kqiLZKO5ETUDnSLTot4JjTrI6QcqZ2jxX50FBBJA7fjTREDDMnDt8gQ-sl1VRYbz4Ra8WUhS6lNdWNuWAFBTGSbWbzX3FP3UvGcaBZ5Tr8DjbfFymL090uQC3cA1jZpysOFA4FEWTnwX6bwVqEEz0phAusqzW9qUuivtfvMfnrR-GHf-7g2zShR570RBodtTxzaY-e6juSIBaXzVfmiwiJLzcrWYzheA22nnJ0Cx0kGdBfJZhuGJHBTkTgFbOiHYGMEiyp2u6pss9SBEqIW1jXa-MZpDI3UvM341ypSYEIPzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uV1Fl7Zm87oyt9XQfM2uZTLJeqSLXKRdV4dOMGNQQ6lsLWK8_LUTmJ68kxnpJN4yZEmcDIT5fNBB3cLO4QSk7_zt1xcfKryz5DCWuFBnMi-7jdluYIIO0lcMgJuAtnFVU57IvgieYZWou1M-TKT0Puc7kLGW-l8R9GfYSquD6pJyUs3otFgfmo4eJadWIm4jJjMZa52tBbrZPL4Bkb9_ikYMvvIBZwXYJRkMQEPdfowSpej1igsjV1GL-lUkYY-r1DS-yZUvD7uONRZDeEG3GoOn0I5Jgqcm0jXIP4KmYBviJWTsSXyd2UFKvFhA2nqIuov72h6orNZd1V_jEzYdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMLxe9FWOcUdaBZBCu3T9ZFlrHd7p363VXKOuheb8goJC1hqmobth9Es1ZXGZ-CmbAT2KRHirT5j4QaHP6N_flMELL5Eomvm5o0z7tklazc_kI5q4BmtuSGYooxGdFDANp3cKnnEiRrI8OdPZV4av-R6kGuOGJWbWe1DzBPHglyoH7iOd-KX6Mw7gafe5cK0Qay2NJhaSZpI37KbGddABqZXmBWfVkSiWT4mNZZRCF3_HOacjG0d-Y7tIgsQMvJDnksw2io1flTQtpQRbeeHM7Qls3ppRANA63wVz_SjDb0XS682BqgVx57dVkAWzIM23n1cqcDSu0xJ40WqlxSbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su0QmzVv3VHM6G5JuAasdxoTID6fjqtxjf5Q5OYSdFY4MZVnjyqVjdrGrtgbQrwo98DbDPUre3A58lV3q6_0ou71Mv94kKAWl3Vhe941qpwGMqfIxUK_yy7bv_e2arTeDkHBWjARP0J8mPDAxJzYJjayQUsftMTDr5DkuuTsKETpaBMm6l0oo2lHybu4_ibo4UE2z3AvylTicrLlkzdxUyQu4mqiqFXNWcb5yNvfBjokEd1D-G4OvdmxLmKYCAw3ErjuXqXyoEx0sqaWmhgUx6J9DS7BuZgjcqoLBoGzXkzWA8yRVZDPtmlknw7OtuXaGFZPUIYkwQPazqJN7xuD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHyyyYIR_jbBqk2OmICRmx41cKYBHkcmbeZdi77_BqA7nFK3iQAZQuo1K26FRDrmXXC9rWKKi-vfHhNwwOnJQepYGxtemjLe9yzykhT1t_yxqekNkzOt5EoF-lp74kMHgyJtGPKuJBHuwjvEsspeJYi-kNkNeK_XAluMeSttma03Qw89Xw8phPUyTOgVdlfityOcDUrzNei35nZY4gYUOLQoT60DBI0r3wOaJGWMXhjA0tBqy7ENR3ukkq8VViVHfK0Crxf3OPdRLC592dPAm5w3MJijpHHGkHeh-_W-QfefTsYHXBDcfdnFiyOkXV6afFy5_81vtq0Bk3r5Y8Kr9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozi4cGcstyuJb4frsCs5u5qwbbunL-RhQYzBBI9ZcqOfurO3McXekj62IkwKOTRqPsM_n0VP4zvPg6twQlc_L7IRLR8zW1AB1-NixdtqervICqEeJnQZ7kyj2g_xGZ5-Co6FwUtynbKhs5qa2uGQLXxRdBuy9ycQXs7joUyIh262HyQIkBvDhtEtCNSc1BehP-ForQ87gKxXtCQQqTx1F_4HoyvDi70UC34TTAPrv7Nnlh3hfOReA79wqFTfVALjlBZ5YhvFAZw2gm3Y6sGKCqq_ry-5KsJwULOD8bjCiEPq7drQHdJqHhh4Lp1RM1PEH43PuX-I8unCexz7I0W1WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwLaK9Vh6GhfnqcGcFgRxYA8g1vocswnXw4WYHtPiBvYLmCg8v_VoUDQPi-kqJd23gqOrwmQmk85sr8qYIWj6tGu33_-C4Zw1S6fKkVkHuJEQoN0PN4TakiAx4tZ8TJMWAmSuMpe_GWjIyzKyrSGGN3tIiepCl_jSVrcl0tIY-DL6frksnv3EmvbjbpluOiQwDeph_G3JAhhLC5yGQA4eqa1ZCvXKhZj4kLpXNLcrQe5SSMnyLzGzYC1LBjPmhZSO6RFkfvnxQCXR-UMvGXcuyAvNT8nnK9oP9oFDazl5QJG3Gg2JqBheNoW0hcrczeDmmgsqxKLszvk1ysfKVqQVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9o9KGxVbNkq36awuPqaOqt36weCSDeAHG-_3pttgJjJA3bI8GqzJSF3dmHWryjXzJS7F5lbrezHyoYlcCIk8_btpXPnb7EzMp6JBZOOHCYfd22gwj9gTTxoxJt187Bdbq-hu8sSkLBS4tatXR6qOLkYf_k1Zj0HggWqCpt0awno_utKLzNy4SnxHJLjfatkrebcSMUqS_W-KTMhnu8himm2e2o_r_R7dt649aDQIHVT2Dzk_9pzXMB46VIhVTZFldIo416bGR1dpyIg-dCZtOABog-Gty6GJORzrXexZH5FKgWAHOhofh2JHR2r8rZJmRkf3i1yMgt8xpnudoExgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNc7a9g0LKXyANmJNQePYU0EBabCutnsfLENTqlX_y_H0i53uw-mAqHKdjnbxDNpVC1iGXN6rhXXv8mf8WJPjPALYgdhc-iHkZTJZWQyZ_Ewa3wN64miHBkVQZO4vR3ZvAg6mlo8VrUvc_xPo36LElsWD8BkXE0CcxyG4g7w5Ibvekp7TlzOWLyM5StO0GlzK3Qt02RloCuDAMfpQCbQj2ZCBPVo_za7uqC1Ej2KTOW66sXTNd3KIir2cVs8WphPGo3QpBUSeuuYm2Y80oGvEjamd77LU7fpBhPjqrahPc0UnDk26L3GKcgwBWc-KX80OpcwVySybtuFoslHBRgXbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhcPjuSdomGlGPPjAw6KVDLF-yVGEIErFfbwmXLKUFj10UJpkskU1htDryAXMcMf7Cl7l8nqSz2ww5FBUruPBqFQXYMdSCb8TLu8eG7AV_vv7DE86nTPiuAOn-zR41aAdvCI2-MwY_1kETtlu85GI9NPBxUb9UVVL1y55PVZn90U_KLRM7mEQmzZr75DmTdMsvk51XhBnVdaXxyAvQ9mQVLXvZ7IFjmYrM6G5s4IaFIgAayd76l9Nz_QBrM0uJ50oVRoJTHGuPiluT4EOyeBHaVA3vGLmH-IXzQqN0-Wk3YMgn6BH4yk7EWPcMNGrIrj7fVJaU5ecp9CHcC-Vdr-Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icdAB7vF43B_Kq2vN4l5PKdGZaoXkhfp7ORMIB3Elt2adD8LuokTBFw2YL3uOmY4OUub-DJozmaOn0rGRkiIbsfxTtavtG6aV55wfWidlDXvxhKeKiN0HswVP_7ny-ovtba-5s2Lq7rE6FM4m-G23MjCzNUnc8JzPgKGZyj6eAptrnqmketebTIbD4iyn0cOsFFgYsy_BzR6tJiinTHcf7zbLHXDQVpmEf6eJjKbeNWf0Vn6Pr_kKMGfOwYoi_v6cBZOr15e_F8CkRbNz7zzb4X_GfHuiQhKjqkMVcX1fLOQ1uP48YlnZVSyIdV89rSha86Kb6WKOu4W5nhu6yBTFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMTwr1osEDzAp_EHOLjWqaIV_NmZeoDOG4wvirIPbqCACUA2FQOp0HZ4vQ5qpJP7B7m369oEh3b70P4YYDpS51b1dzAFdpWROyr1mYgIygL10HaAn4XuYMne2gOFCOYwO2pOTu_sQ2ZHvY16hucBvvjVdbSxOqN8uQflqdAe9PHngH8OMm19-m2LPSDo57wR3hjU_QdM6vswQJCThPmNu7EWwF73Ax2WiJNmCY18xrLf_7R4y3RoUOBVmEMWKUXG4nDxIpdLR8V933TJ7kuVgXxQ5YdYYEKP7IZRWH8fJ5HgYyR0wM_u2JHAaH3ZPpl9RF4_v3hw5uvozKifL7eESg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0Q9bKVe9kKMOTijQixR-FuJx3epGt4c_Iusv3ZaYdz3v3eetox8oChR6Fp9i3A7IIR8WZ_bSDJREzC_lhNqvLaaXPw9HUzk5_6b_LHTUGCawbb4DQLlAOxyJhUESY2h0m2oPr7ITslw395zNl6DwSDTzvfrZ7Y7k1g_h6qKeG6ZMAGTEtxSHGEBQMkEkdqE0aotH17uDju89_GJkY838iKB_Z7rEyLEIScqQKiLTIqico3A2xsdYKPUMwZNkOWiIfo0hitQJfYqC_cwKJ6HE_woc-I90X_G-5Iu06G4Lu7vR4rX1eAdcKteCvYrIWMNioN9E8QOSDfLgP2DIR3Srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRqieCGJ-KOWBRpaMkXqZNyBnlcKXa0Fv5-DEK5lbK_3TSIoTDeBBJchR6EwO7TTCBBIdMqKG-dWTH0Ac1xyuJaA8JuNDkWlD0oi02nlj2SwUiF3PY7bQOY0PUNIdT_M6za_nlrp-B5DbOD8d_1bAVqh4rEeZ3TxX_v-A3myhkAR0AvCb5EBUZLYznQiumpU1w0AjOOtGeJdHi-zQ70u4grOB28DW8tG7H4VViGi6AAMvjgHOr-_E254B7DW2L5C4YBWxJ7EdZkJinjt_3R6nMW6cYM1rHxHLnchc8GGdmwKkz_hyY3HCNSBLhLMAXGvYPGFviXYmWlhHtce6uKiUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYAiAtoMCFNJmDgPfb2FZpCbgzfSl_l9PC088V2rC9KYhhnr1DxWWILy7tKhXIq5VGw6lqjBkaM3b6D7YA5TgxjXdxH21cWWlQjFn1EwZJuYakZdGfzPOKsSLb4kvtIzqJm7kyH91GDjyDh1Mb6w-s7POjKyABJTcMvmVItQHxZvBmzMggK5OjxDBI9WVV6JQNPj2Uizd39Ij9H71IfuNONdfGMNC_d_CWYMC47GOhVwTLq0yslH-AJynqAsblxnO7e7ZO90uRInA5Ko12Kczt_ZoBjqWVmdXihmABowVv9oS4pYSY6-AgYtuLUAGmOF36UTBMbBk3DVqwTLHw3FvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph3Da2sMwT_bYFyLzzIwHS2e2l2nYl10v1vAdvfYfJhhNnhosnN3h7Zu3guOYNt_WaedZpXlp1tZGldvTIG6AhAYIHxIx7ff7rOt8JGoNqJ3I2t_qhLx6oHFPTKDQsHCjDPnuvP6r6ZIFrb2R-WoO8dMTAa_xvdu2s0kkDlSBfG8xqndqQaMYK-SNSHTz7qzSiN6KIwxVLNdXA1brCcJrjCe-LHC6w1Ydm-uou1-oYg_oNgJTeLFsoZcra9Iz7T_OVVuOQyAg-n0RDO5AgweH52SdDK2zIrLfQgNmT_pJ6qfMMoZXIoMasrVJGhwsEv9kDZpzpOa4H8uW0cns08XZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAzc1T_B5NeB23GiCzMGJ5CNxxnhWnfSFUxGSQLh282Nexm-AJjW7XYko56Q9QXBYQxaG7IbxbrI3F6419VJXCEqr10LvKxQm28FeIIxPI5E7SCAveUuiI_bONmveOm1zI9lAyVVcsXttJA-f-pLewR87tPPIF3-a8Y-Y6pCwSkKnSTkNakPW5AGL7D1UKC1wKmisrXUNQ6jPWnTcOoBeJpvHWEkKTggiHRMrWFp-K61jIbqpZSOt3TH3FodglN6ODsNg0tVjEvtoc6xd7fdjeL7Xi3lbv9b9DvaJBAcLiWoxMzrhDv2420LqBHKOO01wxlxZJKcbnrNq-8z4W0bDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spxvgjbaFPzVoDnBEVTbF6LDYCzkaSGphPQV-qAEU-WtKTQeQa9iSFco9FnbRAF-YxC4Jkkxl2shILGu8JTKrx-efxw2btPG3AL6S98PlRP1ruL-yz7hqn60SBfnrjwJGXhKLT3OdNOiA_a8-uRY50xZnttkOEePx_vnQeKzxSfXAouakBXlVE6-CuXRv1qNxs5e8lzrF8pL6QNfUpRieIcZ8POnYLd2CBZkGbKN1x2G-b6jLzCK3DEeJT3R3cKuHSS_VpN1xTi9jJ887cSIooD66ficZIWK58z_avhuy8--quyUoQnJlXqg-64moNtq7j5eAAmNodkWqA-uhFro3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-tmOqrkggzTnKhtcXsHStCwkY8FJChhEyO0EpOXUePk2IItoGZKhYPfJh9rPuoKVMEiwudCuVP4KbyQY476_sxuI7t90bG5ooGJSeWKurZabC4mg8cLIO74Fep-07hxOmp56G94pSqqRvMNXclFH-z3qGQ4__5pJNMACyKUGKHImjVJOmvfpxPK53IRpKdY9jr2yizJd8eLidAzMW-PhMZyRcYxvSaHfyTobfj0dE9S0TVUhDfiK6VW4J0MT3sanDwGtHnmWiCmxH9zT3aU5D3nORs9eRaWdd68MK0R3EA5u5ey3yKRGvVTEAmyJa2FC8WPx7VOfif8OpXh9h9fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_9u2xqQY-CmWr1ssPUs6_oCW4kVUa7LWGxCXpuSTzd7lN6H6JkDoY4bzY2SrVDm3ULgR4iZQzCO-SXq-snY4VjA8dVjJpm0eWnNIg6gMKvxHA3Y-tk0t3h7ogPrbI0Kzwhx2vd5aZCso4Ehpn_V3ydo-hdIWmAOiAiKT2HvBOkX1uEPEH9oKVLVDLNglQjIWk2nbdRY_NrySc4TtuGYb7990RUUuELDguMWGGQHgH0Aoy7aQ0i-qfZCKYOAZJ8NRYktQwtWyAWa_KNcropWzbXt49erIlHf6SW9gS89hOfOmWubx-gA7JKs5r0tNFI5D0KFLAb20WIomaKRTvGV7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjH_qUftf2JWL8HqdzetGh2wCpPHBvTSUITxXMUAPksN94tir-_j-r9fw2-sMfKkQQhxKlSumrQf_L33DKAYwyDnpiaTKvMBDvdLUkZ7jJxsYOEDuHeLZ_WR8nCcKOJY8JMmL2T-ekbCxQbxh3tLZsusmbJsyJ_jGP05sRsSQTPndX_7t1PG8nnVZM96o3QQIHC81LPUOJHTTb9X1ClmikKJVbRLM1Qwj5tROwui7uMGZxmAT0l--0KNxV7UDT_2ZyqV04wlQoACGfr1KlqA-GwLOXnF4h3-A1xpONRyvv2-aeXj2xB3w-aBWarQ6qbd5ApPlyBCeBK12v6bDvTOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhfU2cUhdCUtUX6DFPFq1EcCiKJCGFbyagSQtExzeFY0GdfE-z-dqtuwQhiSJnAqtINIAo16BDVqfedZlTOw45jef46zQs3hQUlZG1G_Cgjr71iWKEczdG-ZLbOsRP14umcNTh3bKENNWGUK43ZCdtbYib_T3jJRCDkeI0MSwdC-lKt381sv14Bo8RVDBmn57nOvnkIJowaOcQP2pVDTsjZ4GTtNd7w714fG0CT8bk340g-WRpD84-UHRhj_FUapjLcnTDAIuKdcDV-01OGWcza6PIrI07woxEU7G_yh30meIZYieujCvTp0D6zKr5Vbdfqg3AK_G0P7igVxAGCSIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etth94DfALgYINesSNP6QHRxKjVHk-C_s0bFQgbHF_v9styUPNOGowWxJaTpp4bkCwSSJkLXiub-LdYtOXelTeywVxzBi-V1EljLlbBJ2Stnd80Li0wLK9JWtou3s_-nvWzU55Wy3piKd3BG2LsCEYzDQPLZ5I9XBe_06tkeb_mT-MPtu9eIFPA56gbuLRQ2nI37rgmsWkR8VvZSPvCYSa7UIHc6oLxZXK3cTz7gmmhGz_fuK_d1HhDCTvtc2GasxGbF5xZbpabmen7dkqDPlxJmdcCJ8IyGBBuQxPBzoMJLkmuIq9XyziLHKHaWhYfa9eK7oQXsF-cy9XmbLMdIyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2azVhQpneSEeT8ZpygWWeAj0AGAZo4qGB8j_LRCqWVVPY7B-LElTN1xsDiX5GsoSv2hGjlDtLRbUtjQaM0aSxrSmGuDjSjMVPtQFbkcMQd23V2NIEoyMmhPnmj4dRES3Ma3UdwQwjiZ0qeYoznK8Zg0Z4NHw1wrIlL5GSTck7FCCXIEP4E-vX9i6gQoU3CAJ3CIyfejGaXebzuM4mrSIkqkUrM3Zl0Lxrs47wHHbjEnfsDVvSlpEKZGgLHYKzvdl3mnA2QEpq8fn-hRoXiLvisj6fU-hvGvHo9AWaLPVSTFvcZYZ_RNXCaMvIUq1qg-8gdP47ZV0_a22HHUyTvFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ii9ieE9pw_AY3rs_1OsqrM-9LuBfp79_FHkc5CvgtMOEW1VOEOzV-PuG7ZLjDWmqDO0AQiI10T06mdo6GX0MLYvoi9eZcHyK5-0xAHHN46QNRLq1UZcEJZJx61GYuiMF9dg2iboEmqn4MJRlRG4Y26i9TylhvlBFcLO-niicJzUYNpxhP0Sk1nrSmHpWhIcDImf3oU5TbucjRC3D51NUBbS94iRmQ8eMnuaosSQOk4SwXYH5GtnmwuMdO6AkCmO80Lm_8p747yaB25v8QTXYFRxS5ww1wMawe4PfHiqJRa2wUwGL0_TlSbD-fI1WyzavKHo8CGJid9Ql6zbXdG-9MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP6A41-IgQMQVEqToAVkXVoO0QPmxWV6cGwo5IPnqPEisudSqvU8P0BDEWgYgLeze7u8DGEak8Wu7iIQBVDsgac_ilwvmVc_twdBOMA08N-LmwXP2Ro-_15vRwDngZB9bcYa2-u8cT0_fpjnMdsB86_QjqOxxWEmhWuoA-lJA5vQriv9OX7BtoJPXTzTit8hLdL9O4KFqoNTz625ViatyLjujapusQdOtf0i1YO2JRWeT-Eis-PVDPTafg8b0vJVzPV6Qpc-8ibXtQlXrLu_JEGVu12_0JB40GW4LxcZlW1YP1e0ETQYrS5_fTWF8a4qhLSgltaIykdlOLkeMIj-vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JACL-G4Mn9C1EMoxRXmBJALP0olCsPIL2nz_xJPJP0p3VG0wmjxdoWkFO8nV56QWEerJQd7LF1M8-s3HJTkF0X8xhYzQk2itIU0jNyDW9hiEb9ATavQ2bTOcmTZEA0DCtQzpL2SqjfbQUy5aKWzRTOvWkVd9Hu0hvqqXxV_RAbFfVkEMLuL9XYwqzW5fRAnR_vUPrpB-07LLg8yFFC1hASaVOKDb4DyoZ1EyZiLBB69Tf0nwnUoJIYQ_mP0k-I3_DRQ-p7Klj5p88Q6hRKCObX7Zfxgcv-6IPQ-XA3RbkNRfnGl4Ku2tNq_6EsibWNc8yEj3fZuh4KgNDtBviKQHeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-D60iD-LJZ3SYLlXvYomGOaJ70W7dVsPsMZDBimLRYVy7y3y8_L5AgvLMlnCsZcaIOtXYH2tK-uxQJPcR4uWEFPWAhVLvLGt-GiJ1OPOa_7MM0GWxYy8yTUPoa1n-IoxHh-uB3vqCt0Zg3B17CuTN9-M9KbFgolNa5CJqA0BgrvbJHHEUqudk5YapdzE59GHnSZXVZlLNqui32H6tVs3TbB0dDMs_SvnB_9Lawf61rv2aKuB-J-p2H2SXQftym8HGwsdTAmfwp3t3HDk2JxBcy44kREuX8m057goCpfaszVxc-aw_qDAmqnzi-vemRXoeFZwig-G1HSJDcBUGGHoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLmIwoyMW1dv1Fd8oDnei9ONlOjrkjrmReA3ajtJ3a5m8Qvoovu4utGNvi-K8EfJHy-svSp7MfMVCRJXrvlxj9chH4u1RJ3MLOEbtqQcGxeoFmycohexTNjpz6Lmivr065kYugOr93BpTCMD-g2ZZIvDuS7Grmyp-1WkivTpjBi1Gy8DPsGSniQTHRXPP3Us-qsr0z5dVWoZbxXACOSFu7NrPJz1-hkVyRvo_ykd_j3qeCfAHWs8tdD2CBRcJLlcz88-_MijXZ4lju9RXm6DaKENOvrXNRiYo4DEYk585YqT_NXSGS-mwAykcyAZ4oYz8YIg-_Ku_KlI8WuR2DW8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYA_JYg_7n8JKnWqdo1k5Y21KOjVa6WxS4IqlJtDeTmd_zspYr1igr14LZCLcMlmSfef7XbSQdEcudiWscbLMCKtUJhU0rpFIBfqn2j76t-wm41Dv2OzXKL2Qx5Fg2LJQex21qiGLtdevDRtYGdXOVZnJBZzbEjSTynt4wiDwns5Xe4ZufySUO4Z1cjUfVpMJMMdwEoWP7HtN29bTs4RkguxHK1ujby8QWtkt1kc3KZ8-WcRn3r083qYZymyak6dlj1fkUhUy6lWLMLjq6qVBthznNPT66yhFnhtJvjtMfDd2ZF7_cmLmhh1_LWWScEfNkas3eX80mOIG5rZ1zufFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXerN0dTnqtEsrB8xxeNQtaFLw-fu6TD4fwE8895htOFjq5CR7stBWw-50IfLl2nYp8yn16iMcmqKkY8bUwYZgxtPf9XUzXnkDwyeNwKO5yPDGFxkj2s49Z5rGA6h3f1YK0h-8xyagUJBUZlEliT6qVa5CW2IwDI30LHjorh3bgGEQj0eMV77Hw4EJtcSUPUxg2KhbBdyy8c38iXr83sOo6j8JV4y8U5T3JhNBWzTb8jdqp9wyzYhTFSbOEuYUSE18cf7cyNp26_F06Fh4OGmHNjMX5aswipHYc582wQQyE62reYpmeQ6t7nE7_eh9obMQliQVICA26zzFN_UFJ_zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys0NQJpmmxW5uKNWdfrDAbGdjzGwNnQCXk2zqZ05AehwCus9KKwGrVfQAWYDZIRhgu9fDJzexAac0rF2W7v1GEBu41diZ-0fgtHYjfNV3vQBYg5Wb9x0lSaH-L3Z92PJ_jDFLUdecE_KnbDwcBB9WCh6Uka6r8DlOPkzNYn7_AEiMGwOUwuRN2gAfjIrIwzVoDORfLoOxjVunlLMGs8UAc6kqqRm43CT78rpqS6KvKPahoZRIk1Y92gDlTun7WjCpvxyevgd69vLAtzt9R1SQcxf1LTSV37L9AOy3GoGFggQ_rL8xPZCLxQEUuPgOg6DzTYo_jFk-G4QVW4tLMw4gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqqijLOSM0XVqs9bOaxD746s7-tK-qwO4vyxKOkSXFS--N2mMmYUfrFWg6v7UQWFUhn7GNlm1-noxQYDvO6unURnC8Vn8ctruxQPl56Wfxy9VIr9dC1K5u2FUP0aVk0lyVlOUxyUSSgaBB77tZrrwcyMoeimLzUAu-X3F36YUg3aWO3vgOEUeaZRxfYBLeCdp1vomMRA24LP-qtvguClIbwXUaXzqh27DqO7_AcljtEzLKx_51u6xOkb49yrV-1QwbOhEEQh9YXF-hXk1huv6DqiWOIl9k6Ir3QwrFcoKhr51XSlYnGceSEs2w3ioiR7DURNjz12tCUPANXKwGsn1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibPMlL1h5rB79x6dFLL98SltZvro1oQHVFFLCRV5QSJ1VhxXLmIZvAEYuFvxDh8b6vbLKkThwLjAj177VL6Di8ENiNCKLOW-q6BSK3nOCtB2w9fYQF5IZRdk2SwX9qsZJAs5OrgNXOjW5YPbEVgoVj8vgXWj3yeaC6Kv99qB_7pAyoqoTLn3AZr1v7FKwLBV7w5B-dEbvb1H7oNffvueL860msJlzmi8uhcNbhcswoNEtZBy8obJkODmelj-SyRT06vKLbk0QOQVSA2pfJONW7EgSwJMc7LJOM6emZ8_s0UWp3uuohBgk6ECREfeEVBT1eFuausrLcU8GrkzpHCqXA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qXD3Dxy-X0nRqWBs5IaGJ2Nx6IfyO3uKJz7EGNnCteouhxbxXu4rFHDtIwa9jaakxWAsSGbANnHjWX7cy-v529YymMoCTmN4OgxCwTND27RhqKZaWv4mut8X4y8FSJxGVng_ERJEthuWNPnWIc7K_ocW7lWZ59MPC2UDT0Hdlm6BL5bn2cfI7rxkFxkBCBpe4ZOSOo3honZvzTyY4gKg4ILxNvUB7hiidLwlYQ9MC_VcvmOHrGBXM0jdRR8hsytssOkrZ6pgaemJsKk0TroQR3vhX6-qZJhif7DroTRd72WNdMyP_krEAlga1RTpZGW64FGdQY1I4VBXANnZDaA-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qXD3Dxy-X0nRqWBs5IaGJ2Nx6IfyO3uKJz7EGNnCteouhxbxXu4rFHDtIwa9jaakxWAsSGbANnHjWX7cy-v529YymMoCTmN4OgxCwTND27RhqKZaWv4mut8X4y8FSJxGVng_ERJEthuWNPnWIc7K_ocW7lWZ59MPC2UDT0Hdlm6BL5bn2cfI7rxkFxkBCBpe4ZOSOo3honZvzTyY4gKg4ILxNvUB7hiidLwlYQ9MC_VcvmOHrGBXM0jdRR8hsytssOkrZ6pgaemJsKk0TroQR3vhX6-qZJhif7DroTRd72WNdMyP_krEAlga1RTpZGW64FGdQY1I4VBXANnZDaA-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln4wVaGuxcNNo3AyB5YWMJ2oUSVCin24kZegEqnPG_8UL6o67uqFPPIQv3Q4U_Ykrjq3-o_6_mmA8ehgSQh3ZuONaAy8XOX0SbD_yiRWOmzMt52uIiBkN6JKLB2MP6YG_SBRrjAx8rCQ57ENa4Rl5km2_YfZx0PH-hHIf_5c8iYG3yG9LOb9kYQRHg5VNBnJ21UnF0QEu6BEnlwzRmEFu8dq2vO6w5ZBfXoQav5Hwm7pH4ceZZKqd_ksIqcGvyY0x2re19GThfIkdoLobAARWjQMGZXhBfebJ_78SGQ5wmB1bllrOsDUndzuugJqfkDOJZQMa4nnMV1AIkOPyfcN9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5q46fGcNt7apMkmCDeDz2-PGxC-LQvx26RzPvIwSQFvGwLmMuC-XwKpJX5zpEUbei3u2raFVNRhmqZqo_-aUf89i_d_WYz9FuZgeslZWiFZPdYcXZ1Xqdw4d2KFSZKnhMDqBEjtipZqr0_Y7d-5ZPKcevB4AkuDU9uPp-BY6uO92pLojosZqjZdfFjVpOd-jv1wh41JLBUq1rkgqq7GKFFie4rSNOqU6H3FXkLRqAAZDC52PJd4qSzbC32Q4enJq9Dd8SpUS50OHGtBydEnIW3Wt_0ykpJVHtX064iP1jFGnc0JpJQcDztEBMWzpSL-M4asp8aRc_Vfhcx_4oUE2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6BfL4BuZaN8LW5USnKGDbbQXdlHm02OPFnPiCTll0vGI3Cl3UQukjyDYThZ8QZZiVZM4f1IF4Q6B_UOzCM1xvxcAeIQHtftqOZx_Uk4NB4yCwu26yLzHsEHj6zeiCDwZXGx7PqKY3RTka8v3DEnKJYu1LucUywBzU5RXs7PFQemJZDAaoBqr3leVj1nJ7ymOOWj97nOy6nzaFMzM_JcpJCId2CzH6TJhZHhQKhkTrHcPUQ5ErdQbyofhKiFVsxoI36IKcULE2wTQsjGF8jhFCBJJkOkiCUvQrhY4cSNTTT13Se-TSo24qYTa_V1q7G43mrrgWxMBH4LiPBF_w-yTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DH6iM3jhhwyHeBEdci60UqemRCZJJrhutXVLOiccoiS-tOqTy6ZzZbZ05XgLM88Q2cgPiQ5tMP1VlHf7YI-difSB5duwin2RLf8hxFVf24UsSPFtrLagBjZKIUfQU8L86mH9SJv8M4X6dtUKrcfBtjednWJ8jqlkrAXgbjAWjmb2U6u0wMjL1AtvU_EAw9TwATim37XTXHYpq_5bi5tiz4rSTjIwWsZzM-jaeXbufSmshkRTbM1vh_1F0h2tOZHX4KB091onRsBSd0ClzwPPcrgw9JQfMeiC3gLT_X1fAzYGijdjD3CSWX2jLwVcmKm1LGHNE8iNLhPOmAcQUmyjmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W26gsMTNtlZUtG3wCy9xBqqR5Xe0bWrGMsbdBYi9q8tdUQ-s3EJFQnq-MC7spNb6gHkeXlytA9TBLyxN38KAgexYvh_EdvmumyhPjpDqAHdXeY0mPXYvef78xnqjg-lRsUehPJ5K0V-FhSChTf6d4E0aDoEydHDx3kllM0rLNYYsq7K5t30Gk1SsM5e5n0nZt0Y2O9FjBFS7omgktSSIW1vqfEhehyMjL30-pyJAdJZd_uX2eptBJbysABtRLI1gR97HKlNG92j_o-FT5cdznC7ZS8smyJeHii7KFFbhJz8ifFkzDGKI8oZWLKibmFXlKtKpDiTvd8azn1qqaaNwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAKzbuHyPyECjgw2IDDVUyNDdFcMy9AV1gE80tqwRFlcNFdbeQwxmIcIbsHewOOEMpCcYdkCpFgcarVVJtdZZwvsRZLEAgPNeOtToAX4QKLDYJiVf5p7m75aaFNtDMarrPCicZgCIB7VDyPgA4DSFRtmhHzXrIi6ye3wog5CRSPE62IEwXynZ8Q3dzBxImsqtpRzcuQd6Elef00oQ3Ihq1dYsBxFxLLn1TZdsmvkxIi7T_kBKg29bLMfByfk-uTdcLZwKlgUGZ9EONwAL_gCrcv9aHlq-gJphN25oxyAuj2q-rmmaqJTv_gn4tpTkWKCPLm4q1r-836ASPhPGxpFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLO8PKKFLlCpAbnncG5mSNY3XeTIYaMcYW3ZzVj2T4V1jIkisEELJPMTfV63BHl0xqRLhiNU02megSxeP0WxvhgSQo9MoDjArpddXOmD6ge9exXJMDpviETizDtgMzpKw8ehXxxS7gMiY5KI-qe6Al0z_PYpevZHs225zAF8qGqr-YcLTUaNpjRkW9XGcEidpC4NeoBDIZOCLwz3pTdhsctrq6qExdWMFkSxK0zt4YnRPdfXmLA8MGC9nHX0F6-23EIrURoD6gYXxbhHus269pZuCn-_FKWfFuxmdP1dje9yvdFxmDQvK6_yZ7BBJhNJcq-9hSUkEezHTxsCw6dBIg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=RLSglSmmZ6w9MP4E1fiNBTmx7-Baymz9NeX2iLS84Bd3LLpZICqhYNVwSJdh00SpS3gu58KM0XRbgdvYIS33QF97xhWKIitDWqLukGDnO34oqcu9PMd2dSozWwtG1tv851UpImf5wO7_WeQOtMPuxIANSU4sYOrpkAIZhdLjV8QuW-FUjZfSAdFgRByYvME0SSjzKj2Rs4OgXLCxstTAKD9XjJRmKxe65mRCHxRPV6bJqPrz5ivssA1QlPe1DtrHI8JF4lErW6R-rHYr_nJFqqL9NDBoDQYCMgn2jbC_ja7wmWI_o9pTLT3PaPAn3-7kJy2IHkgthf_vwl2lZkZhdm9yUg4aYBJc-LaPg1X8-T6XoTgoiIpkj-zlKpviD7VxN8x-tqGTVD6fJ4PIHLnyvV85WDWvo2eYU6VaB7UApxyMXAVVgF0K83zySw5r1BjcrxaYKYURrvQGDKugBXNxzUIALGcf0JTMMjK9x6fSKsdhMmF-5vNnsU6jLbeXniVjKyU6Av5uIgTVIm_XIHtBB1VrUL52ex1HKBCpOLMRLcmdhuST-zyhGRzQ4r_PFLnbhH9jqZJJHWuv8h_qxpvB2r5F3sNxhCSaK_1twRbdx3WRWpRVGqaA10nrxWoxSsr7SVCi6Ot79Hky8DZe9NtStWwGuPyrSJ5X21yWu-gsE60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=RLSglSmmZ6w9MP4E1fiNBTmx7-Baymz9NeX2iLS84Bd3LLpZICqhYNVwSJdh00SpS3gu58KM0XRbgdvYIS33QF97xhWKIitDWqLukGDnO34oqcu9PMd2dSozWwtG1tv851UpImf5wO7_WeQOtMPuxIANSU4sYOrpkAIZhdLjV8QuW-FUjZfSAdFgRByYvME0SSjzKj2Rs4OgXLCxstTAKD9XjJRmKxe65mRCHxRPV6bJqPrz5ivssA1QlPe1DtrHI8JF4lErW6R-rHYr_nJFqqL9NDBoDQYCMgn2jbC_ja7wmWI_o9pTLT3PaPAn3-7kJy2IHkgthf_vwl2lZkZhdm9yUg4aYBJc-LaPg1X8-T6XoTgoiIpkj-zlKpviD7VxN8x-tqGTVD6fJ4PIHLnyvV85WDWvo2eYU6VaB7UApxyMXAVVgF0K83zySw5r1BjcrxaYKYURrvQGDKugBXNxzUIALGcf0JTMMjK9x6fSKsdhMmF-5vNnsU6jLbeXniVjKyU6Av5uIgTVIm_XIHtBB1VrUL52ex1HKBCpOLMRLcmdhuST-zyhGRzQ4r_PFLnbhH9jqZJJHWuv8h_qxpvB2r5F3sNxhCSaK_1twRbdx3WRWpRVGqaA10nrxWoxSsr7SVCi6Ot79Hky8DZe9NtStWwGuPyrSJ5X21yWu-gsE60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOHFUUjTaBwJymVRFjOVxD4jGQnN1GB1mCZx0QOoWg2QmOmq7je0e5F6LtBqfrTXgWGdjIX3bOD4Dp_PwubUbSiCCkOu-kNG1EKWjBpGn0-NxXlfJm1gKkGs8MfXPZBmd3OUJ8Uskm17C2zbxy4gEV46qfutsiw2CPNKdWCSTqx63gNVUneFJVVzbhh232jo27LdjhosUn5fXP7Ch6iR-X1uTyTeST-PSnt01SrnUxxsF3HDZKN-Nugki7iz_XV4zhW6vjGBNHgpsH5tXbInRC2D9p_u80N7nEAPocqcWGVGHq4mcfReyUzlmdNdkXNVXc1DRCF2PYgxb86Y4n2NTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN-qfyU2wmDvVZGs_yAo5nLVmS4RCUHY33jEiNWDEEVlO5fORm8r9NIBD38XRgUiWaPNlXnyIkmPddgXLsiDayQAv-qQHnynLSUy8gERDd3X3zqslMsi4tzKbZZ5P88wgxhFR595GGh4xrb_qT1_wnKBz4uvCLtfXxrxyMEJC7sxAlPq_x7G6VDmOuqIEN5eRzYvc4nacBYnyYd90nKKMu8JSVsWx-8E6dvfx_YwZQzILcNj_ej8v2VPOSyxF5_jBKxeQqpNWLzNFIVuclukOiOGsI9tnMQTtfeyGD8Fsv-DFOOE5mIzlLOL4pJv762vY84UEAsuWUFMh00vVvKpxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra5ldhyG3UM9kbMOHOdMy4pbf1r54SQ3K_TmLStVmHA7vPDaGjDd8CnIAcm8OL1bgQQZFYhluraOjESQc16PDy-d8dOejOJHtXhAQLYeuhDZMtCnFUQSrqfwUTqhfmbvELGHxvcuFbpb5z7cwlw51eVCeqmccUieFL0ffMpXTG6Z9TDhwF0pNbh6Ij6lu4a5dVfs307rjicHaCRi6z_qbMgfe2XdLdysYcIe0N1QY05iR89XjakyTz7AbpuD6lXgquORDWl1tCdhQMClkt2mJsaZ6eiZVssrjPNtDHjMJUMnQMaKZmIqxMdme0tQnYVfCqBrZx2CbQ5nx5u9vzPHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofXC22XgaoiQgHMHKyKZtoaYa8FfMvKjjrWXoQddiWKJdgC28DJFlbaQYw4bMrz3d9Fm3fLwjUDP3mv0ZbvC_jPV1rvbMUbs95Dxq2vHhUyfq1hJhUBA5-6MKzy37Zzs3KD7xGyWdZuYB_qwpW-_oobu9P1sJOHNpolN6JGKw8ba_Za3KAgWdgpBHzJrjWZZ3A1-olXNxh7kWtHjh89lRj0ubdW8TQyEyo7Fu54M-Ic0eNqoROlhrmputdEvBMpY1wZliuBPT1JAgEhyiuPdLZmsJsCJhjGpzC93rttoUxyKvDn-_Q4rCSKb77qSgUdkJV29cvgvxjNXkuHdUwn6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9t0S0kB2j1cl9zFRwGciB9lcxZmrzwbn6YQHtW5Ihb19lYgyJOH8jGFf6Nd1L0t9ruqCJ33z37Y2aHrU7YxbpfYe6StjwPveTtDZoc505qqqbf5-ldGYxJZMgVoR_UBW6Wq9M4QUh0XUwBkkPUT0UsGyUCdb7gLjBCE7Ac5kXNAV22FWWW8kQaCa6VIag2ckLHvFKOUANC81_hzBXkbVFi3AbR_duimSp8E6RjQth-fb1PxY6z1rZJ16zCnSUJhNE1k5IZGz5R--smHw5q9S4qLiTAeKRy7-atlFXhkJojGxeN65jQ_a8nRB30hSSdHb-RngQDQlMiwXqyShtk8gA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUV_vIL5UvRrq9Ar8c3Pt2PfFbp09HMSEbQmZZqyRx_y6H4WdeoG1_XXXGj6-bXP-FZEp0n5z-rlbtENGBpwsschOTYE5j3ZFQOif450hNLuuL_ilTWFzN1EowWrfKBO8uJld0xo8xsE_U8ht81jstr5pJZ7XFB-AXBIUGffp9wB8YqpcgIAK1KNAxC3S3rZaTaU24g4bRcoLhFvKq-mzRe83-qJp49-X7Y2xGoKPlJYL3bOGFuT5LU50xhnMacuDbuRGTrUcE4rCo67OXuZIqwemtEvQ8PcHfTCm9LslP6KAgH9er5pp2vb0aY37FcoQpurC2lpNMr3kQoMwpz41DNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUV_vIL5UvRrq9Ar8c3Pt2PfFbp09HMSEbQmZZqyRx_y6H4WdeoG1_XXXGj6-bXP-FZEp0n5z-rlbtENGBpwsschOTYE5j3ZFQOif450hNLuuL_ilTWFzN1EowWrfKBO8uJld0xo8xsE_U8ht81jstr5pJZ7XFB-AXBIUGffp9wB8YqpcgIAK1KNAxC3S3rZaTaU24g4bRcoLhFvKq-mzRe83-qJp49-X7Y2xGoKPlJYL3bOGFuT5LU50xhnMacuDbuRGTrUcE4rCo67OXuZIqwemtEvQ8PcHfTCm9LslP6KAgH9er5pp2vb0aY37FcoQpurC2lpNMr3kQoMwpz41DNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn-VCeUSOoMXvU5fBkQIp7hISKYWWnzt4UzKKX-xvcdDkbQct4ny9mZ-EvnD-drGl3GCYDzcKCsQnqFl4zQTtCe21vasK-Rz5GS83QSa9FOCDLiDZRbZoJ_qHjU3jfwQPyiratPfcXgL-vmbv2vvwUZxc8mxNrFo90Z3WHOj2JTpAR3nA7miDv0yeaCldSUR9i836_ho_bzOgvdWlC4aL4LLWW47H_eVCR_mheMfYWQl1v8-0WyzDnNIMIyJgXAL0yJ1t6V-7MCPRDLYNJmX496nwmLBd_NIe95yqwLjjBsgH0Wt-etEwyCk6_70e6cpfr4ZYn-Q4tHUHWk7iappsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldSsJGVgNKh3Czd9O4GR4qdmAnIuBpA-SCBp3fxKffUWbCAKh4U4cWE3Aqyv82KhIK-kd7dupldjM9Y6KlgsVqYYH057BX1nXGP4Ol8oO0TiuarIeuovZfF2w9RJVE6T_wy6E0LC8X31jaCquF24xU_HBQ-J09Y24NjEnyty21nK6lqaA5TLGiZdBILpXwneXg4BH73Ncteff3WwbJkukILoMef6YfOA8DVYfbe4QVFWuKEF7xZ7jTvBt2lAKjtuDMXvVinTgoWzCObLKfawhiFuD10m4GKochOXbh0OGlOd_n7A7bzbHXxATVs5PWMFurtwzslp9xkg7bRc2SR3ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/in3RxE6Hk7zJ4cgfbRwuqQ9-Lgzo5noW1TmM-y2UbU-0g25oKo58z8DplJzIY5Ga3EdBRhMjnpRFbsXR2y2Sqthj6sdvCrUfKnkIj3vhx9Pqj-xB_TJLibmbEuQtbcXp4OaA6zZQoL2I4J5iaERqQVu5iHx5M4vuXoLRTT4QSHcQlC74zxItILqy8oC-o8O3Kxe40TNwGpQ_wwOuMtiOSRvxz3CB3S3YKtcOca2WNWmwU5rUZAn3SPKl1c-2VXZ1EPQBw660wK40rSTAObLGGJ1akyLK63P6yEAh5E55v8P8ARCoZTQz2dvuwCRwI98eG2pUACM_C5XielNrH76Q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIelU-8-Hc2bNZGpGQHrI7coQGaIpKxQX_EO9qyAC0dyGHEgUxOLzmQzVAP4zS6GewuvsUZFQOJsExhaWZ2o1cEtGkz36Atb0FYjrJ9dJWlLYc4JsgDwhapcM2DgMXKYeA1rmY7IxL3abu_quDU7jELlcAEXMeSPNVALIsc2DroN0VEl9gwvtQ37UPcN82mKILkxIuph0HNUQaw-OEFSD0bRGxlz9NJKKCT7I23iIG9Hy2eCytuA7vjOGlfmlwPoSAOW7FGFNJZg9VyxUbfiRu0YNh9wgfqqnXC6nYIBirjmzuA3RhLunPvIIt0PReQIOetILnGhbqygi7CcmlQyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqlF7kGiSmpN4EVUKA705laxuQd4pLODhNWWEa2VyrmowAeLxAkRll6dvWoE1UtBrbsYOHnGFgal8QfQTntx1l7rLtjCyS5c0BJ0rqhL77DMo2SvJtjjDq47RqcIpaUla36Klph5uUbsTIixCBdpxSA8Fna91w1DuLYFpSAvfGDlM4LG-DOHDuZMtSAeaP3MNKZe60pHGDMGqxbeOI1wujgK3KM3ILS6vpaSLE65SmVTjTOvx7o3oghpdRoBv44RjGmll_gaePTMoEYSqUcVN32K3WgOErqiR3u9z_iQM9m_Z1wMJbrNbSfdT7nQ_lriDHElZtld-cFzdXN-2KR-ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKx4IyZ1hBirb1Ia52rjR3Kc9dNkMeO_9x_2N_BiCs-0vt9ATACBz1D4Y5Rg7Cy6_YEnnO-vCiMrNCOY43QvA5bVZc4wDYykt7xv-yFOGlwz-zuoLDzu9tKI0G4USglPxIsjxj58qVYpvOey1oRvuVbPPxtPdt4q3pe-O3BxmtfYKwbEuC_QS5S8J7wzd64RPAP29uQrawQx0wRh9yuJvff_bDVvP5aySPDOy31SRvChdUkqcrSpklDo_oCmXpelrMSt5WoR3daCRFtz7L9bhdTgZYKij_Tbf9WwyZ-3m-gnLp_yFUYCDWFMynwcTB0t6LcEYKqI62tQEgJERJROdw.jpg" alt="photo" loading="lazy"/></div>
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
