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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 213 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 323 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjo23T3WfQyJC4_Y0FsQyFDLsI4vcqkFJyxNYEz9Ky9cgjJqbai_LwtqjS1cUw5MYlgCQmRuJyPXCt95YGV9qaj9J8yeBib6-mxvcvlnFBD0_8au9DuO233fBc1-Gj6Qrg1Nm1MHvQzzfkpC2fU5vUKwN0cr1_slmyw5vmD8nUTVU4_E5qWye7sNW-rGzjVfd-0JgyCsxqhNTtR6WJnt3wQXo57sPkKVQukt0vuMW7OTKOmtyubjO2XXbk_UXp9BmVhn5ljwfVTle-cFWqfwzG9MVXzg4B2RKvKw9u9e7TS7NjpVCVf9C8OXWM4dH_HDoIkQx1G69tVlMvBQnP6HXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 421 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJuyrNgW8fxxjYgFzPlovu2IQBBwC1oRdKh-Xat0MU39eINtfriJaHNDmDRpzDVXzrmKW5N39mwA90F6rmze3q7X0EMFXZCkHOZgP-Je8mdc31oC_4HTOqTuubzbXoKLWS83_yV1rcBulH5uwRtlRQaHCeGXGC7BP7fKPSvpQ975Sn6XMjMobNQjOCEzgeG4uOFVV0OTXuMndl_mMNXf4goIj2ie0XceGZwqFHVm_1rgD3x9kWCzDx9PiyYMWZGhbKSOuMgZGrMCh8Jqlj5onlrcu7ufOEENl7qsuDJo3bGSYh2VVkdrcyra3fYCrR62hlcKfELCxEk7H-CFprj2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4hmM7S3h9mqZgG4dw1zbIwOqbNddKP_FoMCzNPm8M5vm4zHCNQ4j-Twywxr7E6PYUbEEYYSYDb85NqbmgMHu14aoFtuLaLW5Azmc_VXE0Ocw45myzARWYjUcVodrkxFGzUjVwu9Edijt86wa0KiB4jdmcC9S2Ui-Nz0FVRLB79hBzymdy3pbumw1zjyyyydkM-k4DtvX6YdckzRTW1JbuzoUdLw3Fno_u2rNcn_5X49uSboAdLafCN_tz_CjAPoUEj2w7W2EGaCqVFWZ-9AVDT89WeB0PardgDLo6feTe5h3muUd6GvAhUj3m_l55rVfwpFmsh64zVG6sjQsDrh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 995 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCDTGAaxUox4hAccN21px504-Uf4vN3xRpzUntgLYs7ZMWcx5VCmw_WIqs-V24kJdHGB8d8XZEB-VzaR9hvroZjB7-v001Me11hj4ChYb-aUUpQFCixeUZpmnuHM4TUPhOCpsBPHaLjrrhbCg-njnU-gZU8_aghqXeo2EvYmcIuzxQmsjYaT7pbYc6thYNaQn_QbMyyIDpJ9n4NbMofjQka2vRCTls0nm1YjFEkCx3a53R0Q1kpN7Zimy1ERNsxLmEDmRlhRNjqpZlfBoCamjvgXgUkbYVYt71L8qWzD6GKgUoURlQDPUx5BEn-Cc9BaEOVkTWlJBbTtWMj8pSgxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 755 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDB99zQ-2wMsiwMCr_9SVo8WmqtBdvmuVUyvHEqUOtZQtdi1U4-gBcMscsIQKsEySBVWZmG0a7Ic_EIIJgwU1EQT0iruLTEkKgUw2SKmJ3GVFYyglNAneylTapJzBQtSYOauKoPDgRN6NDjfNlLjFYHUC4-M9_hPLK3R9rpYSk93bDGGV5U_w2HeKgayLziXs_f2hnU4EwRqlmkVB1JjW65Mtmu1NVBPtgRzOgVP7wTyP-Tg1kymukjFwAUT87f1hWDCaueZIvT78q0gJngHYWBqQtL2qOYoOlKLPea0rPMx0zZWQ4R61jucZHt4g0jvpLFN5LGQjYbSXovblRqaYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXt01-AT65D94QBswy9rMyKl_uqXQKwran97CkT9tCYu8zVfsT42k-9jVV0i72fWdvvDIQce8LmJgJ2AksgK-vr_KhxAZ7Twtz2WiInH-lVngZ14i6_TsbNCJd2LNs3d8nI7BV1OjECKllE0osjE0vgQCFTWohWbRz4ruWiCtvW73TgxdS3fzoTJKWgLd5z1HSCq9BxBIGUoSnPOqCsSEk9lF1M63Mg10nPUHr9H7Jo_dmSJcF91HcHxIbz1X52zJvB32ES7oqxjcvBOBsNLwqtlPdyobTho3VN31jPLp7X5D99_61ACo97oeX4hkTO2uPTQiDfl9xSZDLtl1VkocA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_pZVAFUeY80BZh5C5E9LYsAApCBTTfJ1fC9BpcpH6tfSfI2QDeH2sdFD35_BlQ9x8IGd60ZQ-AXD2YchOalvj2axJyGHuKcz1GsnJr-jwyK2CZ03BrNL3AR9Rf2Q6cF8AoMmCiLAq-BVGuA6IKgAyk-pcFR3qrZvrpYm6ZvXALWnM6IWxCa4axJbBaI30pu2u-zbEfbqRB0dmNNHnmoCF6TsqY51TDzNuu3tnAvYXIUDAU91kc3LskpLMdOIaVEe3rq33KYkYQzoVh_VrJE8bilcc5NLq1StsLmCA_yKA6y1bd8uGexY4GBfiD6C5MAIjQndOz3Kq-adPXsxQqp-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkNPt7eoiufw9pdvnyPUcotXuJjyFpchn1VACo4Gc90Xg_xf304d8RHgaq4B1VmoHWVH7owNZ34SHnIQB72uYBF6XL8kkxW6uLNNXxEk8bEVhnxPUHlwX1rCP6Zss5hLPkUDgwUT78zIuM9uVlgLJNU3It-6rRwkPPr1ewXjG8ULzetvka0zFK9gdIBVEe3GkR700dtJnocjFanjq26NrdTK_eErb_jSxAmemTzDI07NR6aO8HkuU8vUAJmGn9c_M0qiGQuEa8N0w3rP_xQTN88pbGyy-eVg8AZVfl3PCsKHRjCstiFlCwIvBeJ8im-nf-VyQd_LygpCvtILNc5slg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BywnywAvdJguYTazNhfqtRh-SDXdzz9RqgE0fK3Ndh84GYtqZpXkePPThra7scFKvcY9DthPbolY17dM8zLNPVXSKfcUutR00hEELqMdAl1kjpNjduIYX4oqhp0uQwyCr3dxZ-AedTLc9WGeNT6alFXLIrDtFQ1Jw8LfYcRnlQmfwq0OBvjdTpLAD7sGk7dwx85DOMVCo-6YDs7SiFOYE9QxjVehx5EG8hvfyybqpPYAnQ9gxpAZ408RqykQdeaMBYZ6cpyIIdWr31aXdc_EAEsEPCJs6JUitMby_h5TQ62VE6LnBSwPYntLoEFIb5OaYKoXZHkjE5ZfIEwQ3JBoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrrR7xDr3NQwcjfhy0O11aYL4nEIHzWM-0VHr36o85evxwsSc8YWvw_DgEQStz-bXc407aHW1Rax7bs_XxaXFRBAoLqvRbSwNl5fktOre2NCTwZOCpcjSWfAtax-iPnry1ONm6GGYjeMhRunA4rqdjKJea6Tg-uCQoNFCSSCPCyt2n1m6grPC3ckK--uAy3dXBaRLt47oRBCqvEe7g9wM2pYlTdIR9k9ARvdPkcFH3NQ_E6qvqkAPMnhq_QJUjvFakVUtIc0RD_Qbml78rdB17Xq8zcoqXRvVkoCZixMlLphsmncelGIJO0I_zuho2CinzGk3vdisFbuujpAEQnv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxrENKUeYQeYvDAJXwJZ1hptPKBTP1ZBfzmJq73BiqTlTO8ntYV54AqXWYENNmmf1PcPJQyMU2AqDZoslHutWhXzIe1DFyAe4ZwbwJVZ1nOCpxp6_bfZeHj0ryILH2pv9KmtQEK_95GffY0yPdb-9shQaaaLBdMQBmvLDNT4g67eBqhEUqohv4ZEZNR4Qql-Sa8W7JHt0giNRxtYcfEHcvAsnamp3VMuvXNwFbKf8P81yWTFU-Zz4Y7F-7DqJ_3TpUhJZmrq39SKuA_pEbJQwuKzHVJxOKi4bQLgOMhPUAt5A2c5LSFKD7Cf5UCHA38WeoN1NH1dyi75dGqnLw0Ggw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W49_OQXX-26ufjkQTZUUtdOjsGujEO5DPG4iqFGVscy5PmKlBPDRc4UIy4NgXzWZfRcjaJOvFnf2LAk8AVkvIBYinj2QJaaxUXrzGJE4pLgi8CcQiHqOozQ4QYEHV0byLU4MHksiX9eu5MUTABeKed7ZPg-sM0Op5PrGYSWgjcG4xCyGzZX1jdXZ1QIjqgopDJN3V7kC2cTR4O84n1MkVJk5_NK_RnQOoOmiH7tiq6m3c0ws-v7Jg_q2_-di9idt91XsklMdhfqgh1kXMMmTWAgc390EzPO_OaaXPKLJ5cApzS-p-InLIzqZDhaw7sgum9ClbwKjVm4Czl6mqExIDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=iOaOnqN9Muf-QSdi8rv6OVLmBErsRUD2MObog58mGLAUcSlUpvXCLIwokg_MAhKct4nneVyOPg49ratu_c8_m-KPI6pNRT5hLo9UxTLdge2_OVr-XZe9AkgL84gY52M6HQWWq3BDiZnV4e5enrO7eGCJUzR7OVM3U6oKe46fwhTGN6CfLX0DgETPN7_HOfVfUkJux4xl7s1n1xa3mB7GRvkGUzgfTeOgrvHVugtED4GgSN8yRo1kq9wc258ghBYkNqRUbGRv57Q7FD-No_yAiS44JQ6wSJnv09uT9AE7lqajDt9n4X5u3fjDTrw0ZOh7BKfIHWMJH-6b99tF6YTyaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=iOaOnqN9Muf-QSdi8rv6OVLmBErsRUD2MObog58mGLAUcSlUpvXCLIwokg_MAhKct4nneVyOPg49ratu_c8_m-KPI6pNRT5hLo9UxTLdge2_OVr-XZe9AkgL84gY52M6HQWWq3BDiZnV4e5enrO7eGCJUzR7OVM3U6oKe46fwhTGN6CfLX0DgETPN7_HOfVfUkJux4xl7s1n1xa3mB7GRvkGUzgfTeOgrvHVugtED4GgSN8yRo1kq9wc258ghBYkNqRUbGRv57Q7FD-No_yAiS44JQ6wSJnv09uT9AE7lqajDt9n4X5u3fjDTrw0ZOh7BKfIHWMJH-6b99tF6YTyaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzSdtY8Z5wx-KHUJBvCUhIGAm0Oknn7-8XIBk8dgXfJg3tCY1bHxHSCoTPV97cHIO4O0xLV5La86Fbx7XnSAPJsqBFW3gUzwInyritXJJv3chNXEDMSt1m_W5kbb-fxuFOYasP2XdLN1OWEhrcSVuM1IK5so1soiP16pJfi2G355WTHXPrzjlvf8xelQ3yIwQBPKYqNTYOe2KRkpgUXMNOjTp6mwyFmQFftKH67dx5fF6-LJeh6Z43_4Let9nC6NCKOp-_n9iW9JmNs1Rf6A5ud6kGtWDSyQzaKHHe-grkRnHGNN1OnnSHA3aTA5s0KoTRLVVxayqZ9z7Re9MakRsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmcGG9YqM9LRDkaGrzQPFoZnilwOjcz6AKyC22UPWzqp6LpFN23xb2Y6zHhaFD4haT-SzLz1mY7UeuAl3GIN6BYWV0_jyk7kY_Ne0izuBHp5zm0_lufHeibqYP-zewJ-2GaOjD5NC2fFk9ArPBcy7rbAqzaqikaCWCT1JMGDkRJcqlHAw0LuNF_wp3ZQtAR8uvfWaS9Xrl0Ph6i8uMVuZtaMrwjiM4QkTRxwKenmyzGFNoCmmfJDGdDgAwIxHxhR1MuIoz-U6XBQfLD3-1qVANsf3ZHcogOCThjIxah4sXDVVfTqMRgazbFDITe1sZQlR8HDkmyFB6LKnB6wPsbyXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oM0vkQAEq76RYN3OFXur95E2CB3-nIveoBgLqW2iI6tDURt9zUTbsM8PcmwK6_sM_apUiylU78UJbv5Gb2ljVs3x45530VmRtMF9tF0gQZ_Jj-VlEhdswr-ZKlXoKtcTvVsBSJLFC9r85Y5WXhPvCYtcTyv2bvZ44n7DGIAIwzuf1xSTo7aSzzMdFikW_DGBK1hU6T_O3VXHxKgJkEulmZZk4y1CjZQilFQQkN8WrZ3ewvx-d5y-HnBjCuVHEVrkmaZSCfv-3SAVvYS1cJVfRl4woHOoKEJUuLs2WEGQoUdir4NyvbceCHb7cz5boknM1xwUtjoTCePqSTbFuiT1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwZzugPeRSeohlBL7PdlM0QJdJGBiPKeXVcbnef01Omr0JerW_WCwzgDHERoN_KKR24A5Go5OJEuRCxfL-UJavfk3TQkkJt5vkjCFpQ0TzDqDfzoLHjum22GWGbcgwOkMxT740BOiH_1OLCSil3J4VsktWVPIo-552UOr_uiF405IhSNoXueltojzmxeZ-l8H_Q8iHSqwiSu0IssJ0DJTm_QDEpHAWtMteDZucDXwCt7FK0ZuIC3jyO75P0zBDTvbGPBGzvOranbg7oCQ-papGbzPZLrt3ecfA95Hul3_qajHrZTlL8p_WPsmo17ZXcccjtDtMl65GFh8lel7Dc03A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee7TVknavE-Wcqzdq4eV1mjq5zXll062jsBtzS68wOD4ftWY8LIQ44LbMfGql4dmsb8s63hfLs_WG2ryYgvpFjx9L387EfOICsXx_xWWVVpt4dmxSxS7ORnTdsELtelmHcGAul4X2XWCokgs89WGL-00onxCv7pUbNUAVHMcimIcl8Xb_cFp2we3jZ9FLsC9wEXgzgIMJscJdVD29bg7CvS13csSx0-gPdFwKb0NKRA-aTrMp_f9jc8E2wUMhjG7Vv-ZY91wu5rEP6PFhUFPBFh4JIsWqMxkDsi-xH7Xlu3j4iRZ7EZcF2U1ZAJX0pneKz_G2msVl_MTd1lL70H3HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiN75XBV48CMmRkm_0DViOI3XSd-oA31pPGZe2lbJ0HsWvo2aeM9klbNaCAhM3TYS7xOM7FfkmCN6VTr7PfrPKIH7S7KG4s6IsjlZg5uKlP_r-9xpOSopjZpmBQQKPOCogSeLgtY1IRYMCizMdwsCV8ZIKxA1gFMpWLkYletNU3WF3OqcDxFqbrJDdo-wGNe_i78R8Hkot7OLZ4eNpcEljS7Td72kuYVxwfgXxFtX9NIWS_Zj3P_tVX_cqlmplFP-hpTblASv0VjBMn8pQEKzb77E809wEGtVHI7JqVTyU7MSeGI7ccOIsG0wOUaEeqcvftshqstX9PXjS6WsVnhog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N053STlEUhlGb7FSAmYnDdvfFIFI_YNGHN3ApYu70LPUoEhWyNbD7kh5PDtGb_bL9NPCpCHT8YtFnKZ1Eg5wrZZy3I9JV9dPS-1KmcjG-0WCGNSXGcwKVsSIvCAhFG7pbvKAhjkYnx5eFyh-8g4H9DIqK7R5lQDNdVwbPHQN2JYor8yv8QWtS6UhRUTJghiPEpK0uIJ5aZW2cBO9352jmsep5kyl30GjA4aIR8Am56CR2TCX7p-oPeNd_5vACFb7OHnApLkqHcWNdhlhi9O72iq7OmENw9YFwuwb7fOmFRL9lITaQdqQaA7-uLpHEiUBSloYHLB55wt6V-rKuBnaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkZ-ER_n5_HgNCYm539ZDra99ihK10dkGYdLpFJ1FKMxSD4okxrsZzemtJhKbfy-OrtVK_7X5UoHf0KCqLNrJ8bqmxoGlOziDQ7gSTe9tPkm3jJ_CQKHV6KccsIRWRE8Rmsa5eOM3IfQewbzaypRczL0sOCkKk8L0B6l8eBzZOxC7bJtpZkoVXjXgutVtwBVFwgPDiGkGO436rvutAF1tZSvPy0BCPVDmGRL441jebnZ5Tm6uoHc2WVh751twfC6Kvs4OkNkg6iO6Qt0MwrClIfAt_I8WAyFO5rOmldQA77z7Ka5e-0eWZGemMxSgElGhor3sAbNhsqJgngz2ZLcjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIjCcNgWOxVPx9JlXXo49154O_kG4Q8GaEDwewvBGRNQpDnLTJYbh1M1ipBilnMycZEculpqc9AqXg94zGIDLuxvdQ470AjGPNhUPqKFT4JYRcANhlg1zCiZmw6S-1vmWI7VEq712DVD3__C_g_d6Jozloqvq3vc4AaOgQKP1Xk2tcx6lCjEPitrH2ZQR0rtnUtuab4_Noa9C4VzaKvgh15ivUm_hdx4VIGgvq1e68wVWuwcBLsSj_Yc9HmUPkpaPZx4_5NWJVPmnU1rX2RyShGj49xfTMprKutRYxfO9YsczPm7ZcvHgrh4fRM_kgPtlL0jFXjAnzMDmT5egWykyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDtpBtyPs70KUHJ5CHHKro0-sGrZkT3opwmn3NpfIX2IA-VwubAoufjdCu8OLY1LNDs04883XpcQP-pomyCNGahLlcwgHWtAXmG54fca4ToGsX-9iFsUHNZB1H6F3unfvoWXLyc2nI_48zzEIcdcp1WjpLfKO1YAR4WhorMUoTjytpkVODlzYkGdJGUoxui0XciXNzBOa0uY1V0TML5370VffX_iItktCOUZL-VEkm_yietIBkJ6hYrJjpLKX51PQz0q_tJ_Xx7-raT78isUs9G3n4n_J9E6kdQJnRucnr_89NxW5BY2NZldoXmYnAoppysjIvif72KjxebIfJUBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQuPCbkl6YSjbktKgWEM95t23aU5mGt76vIrad00x6BDXnfdVvjWFAiMr_4DPlspeHNZ1-SgnsgnXzEQRG3aqKoLLDXk_bHv4EZKDycFbWIKZ9s5pUkrShsEdfccLND52lykvzOQW_AnGNT8phggGM3UWbizCMrQ41nl1WqsB6y9tcKaeWHlk5kSZlRbuKn5PSlDpM2KmiYKT3ZBs4vaRAyHKahKjCRffMw8_Djnri959m93A_Ex3_hO3a-Bwa9sXs16iVLn0TgY-m7BiDPp2de13STvhg_t6vZMUE7fRSB8cRdX_w1hdKH2wlWXhGgJG04-XSfktn0rtCLVXlsC-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVgG_PLUSCOc1Obcrw-2GYX-K4_57rQCesFuG8oDLkwel8KQU3TpKTunN1HLeN5q3E7i9fw-SzgdFlRGL04oJwY6jKEBse_SKICTdzMYpM7RSyvR1taWd6a_65PW1kDF_IVYCu6M10vuUNb3v08bWj9JJ8FgeOhBEcF5a6oYHGAgW0GBrUWPvoqStUy3Mzz5QFWbGHJCug6dYHv2eLweiBCxPF_SwAvYw4RSNC7zZzNkMsj_cClkiVZPKxvE70RzkPG0HeaYYyymQ3enp9NBTYR59G0D1V1IaxHEwC3rMwqeciNUhzjS-eAoSoA5YzIQvXqNaUwuxBmteMQe7zgQ7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtPuvOoUhlsYjQwxRQBeWdatEzzpXBSFfNGgsgto-er0v49v3g_LYvVyZfgHFD1uSXJiLcMOY7yA8XnDbwP05AlGzz2hIejML4bEc5y65csONjtbcVa97NlyxQotBWBR23vaGLMM_zLnhbpwjznFmF_XOVzfbL4oj4Rf8Lr91mtEzfr0uJoZqy8GX0_Usg8VvfDLuAeYD8WvxwNho8WKi-lhOEWmItY-F-K2jL-yUxD55CrPypYOU9sledSABC77HL5rSx7kJr0qyqqtqV-ISL-GDrrWlFQ_L5VfUggr9TZrjZRppgj3U8zG7VjWyRgKlg6yl7oktDJAGTHnZ-ea7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyL3O6yTfawyrriQuAm2cgAF07uRpH9dLhf7rLEmrgd8JqflkGjwXTk9qoh6IwKD4WimIVNNYjUm3v9WksM6zfHDWIS_LCb26y4C26TMz-eM1-YnwR4au1rIUlKlXjSMrGpRfV8WgCaXB1QMREgpchJ-DLLR2sRUtkxqIJzdKWuR_yEnj6y6913z9JaZWhjrice54vR6CuL4FxkgaffQiiYw-Q3PGiJnk8CdWiv2yqr9qQqTUg4dkUxEAlc0t1ikaqGLOiOy-rc2wq1avl3wYX_LDcfU0QidJ6Y306Q3Gyo1fm_5Mf4D5eBvYZMBQs_KeSp8BQQ9fRNfiKG3zZy_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-NVkulI4e31j4r5YKY3jIQ3x1LGPvgKW_F5nJqlCHBhP0EzCXpWrcwVKgIrpADz3wvF7Q5IzSQFG89fEqO77IAMpgt9h-BYwDWFY7qWqLnqoNTEgsM9w5o-prA_b2e1mmhXncywOWqZMAuZ_OB8CnZ0oVZrQu2VXqxUoBrNI-c5jFDID_T-f4c2M20Z2jR5ofDDBqXzB9FGsj9lMTarfzsazBfA_ziMEHTv2XH80w0jvHWx8or0U73IfKks9YYitlKFLvadZjudsJ6_PSVjnXucW3FpphVry5QM1Npvzj2qAoXZvPF-FCiU3iCnZ-oCIdbDVFCYMD2O3xr9wXLJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-DMmsfNf7k8DBagRN0iv7bCB8AwnDEefycrt0mgO3Z0tIlDob81tYVUykCB0pwzIU9hCVFPABqNOnJtRw1iaQYtgpG1g-0J40uERQPyAeW6STPa1IoPC50GU9jg5yH1U26xIGXaoCnMEbog7Hayp843xe0T6HNovTCEvH0NFtCvgznFBmh3Xh5xUYSdGciujk7lp1v5_PAxfKXu_azzOeyuosZBQRdWUjVBeIkAqefo0vUeE4z99-SHxi0uMrWOe-xn4CE9DTS8S3_GfpsOiofugNw1HFgDvGjGYT0-P1xroTtaKgr6d_tzApfrJx2MW-N6grtPSmDEiTy1exeXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEpFZjeZplnO4B5P_2j8zoFwfQ81NyxK-eOkYRylNtGDYdrbLVpmzjQ-TBPSe5pnEVtPevt-Xnvl6MRHeHQ7xQwgEQSfG1pW6KR-E4bUhwcueeQEONCpZxD7Y81C00oq1VwSQ3PWaIu7M16ymcDVF38gK-AgzC468v4jM_qrxFaEZOF98G_UMgkYqKhlKFGih8pGks6IUw42xgx7sgWhjE7V_H8u2U_aKxdrcyYhTvTkFdURUDiKwqaxvuq5oovd8aLghZ2MZVScsSrQeH6zfWasBmXVe-e6Xr39eeFuy4FIo4s6rCtl8p1A_NPiJMd9Fq6PMIghDWFij5OM6GZwCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlWDvg0uETsrMwo7jaoarE0p61BNHVMuAQOWuKcmaQV-UijE3yQUcmpeN2laUMcAEKqYgTuK3l-G8BlDQ1B6kD7WJlVEf6X_KwqwFv9WqGn3WqpEYBmljPrRaRTYnE8OG783i2Q2gJdB3q-xY9LUOFqefOfaNs22y7sZlxnSDPKRChzIGSj-jyup1lVcEfETc1LkHQ0v_46Sl-q1kuCjqONgdjgdpqwDj-UqaBo5J-5Fpmy6sFk-2AY0P97oJtYIWsSS1kdWE8u32YR7G_-dCfZ-qUuWs7SHoYrcNs6UWjU-qG3CL4FzmaWHTKg9Q1dzB_HexdJERuKN7rnKb3_3lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCmF0io7yBZRFdmE2cq47UWkHmA2gsQvTsuQw1ZJNFct8MrXJj-2sVrlYS4o3LlVdmth-ORi1TBwkFQzq1Dd93Z0G1267BRZjoAMHQ07mTlx_02L2Fwvfj1wEu7wO7ALAVrZMxa2ugc5na3kJSXKRyOCAKPNWuCGXV5fqBBCkjLUy4cfioAlfZ5hRk6uClkmEcdbhq8Jku3thTysV-H5KFRWvFgR0i41USOESL1Wke5DGBOAP7ohYKGGMnaGmGEZ8ZL4Sp9BrsFKvV_cm3RdJx17XitPeKWTxyPtoPgp9xuJKPon8007FU4WFbE0noG3qzt5Yg8mbBIqbTOnHBc_MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU2gkYvBf2ZOv3lIOdci22OWuvBzcPSsHOHg0lxDDjs6hLHqkW2LS5JhDPp8BSdYqT6XuGnSO4TugY_6CSeO-0RZNxt2gmzUDeTBGOIYHrjDUXeD_nDFc7BpUUCySPa7RoOvOlgDdkneMh_T-lrY8Vuv7X4fivXRgZO0HMOcfQQSCqUEmkMdgq0rj_SUpDW-r0VJ1BKZqIBKH4nJNB_zXH_b-g6hQGMYIlPE5g204ztPnOAYHiPQSzxK-Nx3PjP5teKNYfUYyuH10Wkv75hq4YOI0A58XXtTB0nouI1oIg-K74OSfFUjXmeLmllv5e8a449nJ7Is3Z2l-65loIcQ_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgAOJnVOIYrYYN8GGIhU6s9q7SoZ1sAGLBJnFRvk46AxaeaeX0tpSoj5Qa_qe-c4nZ5Mh-BPT92q1OL8htjbGgLF_CfEXmzZArk7H8lbjb7dbbweEY7Iu1D3-pQl-jxWbSq5kV7zal-uVuYZeXBwasBurSOb2_OJyOx5L1_OoOlZOXVttjKiqSn8aLAtvNo-LyV5Zlx9f4I2PmVsi-dg3Hg8QlXxwU4ToDpC7BNzCe588LqnbPJiQfaGRwLFQ-CzjVN6dx-ty7VFIcFgUWF8OniEynVb9V8_P_M61DfQ7spWDPUOgpMl7It-PlGBu9q2sC94-xd3nmX6332XRXQQBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY6X2Pl4X9yb_xo4_j0_ZJXFFLVSXzZAXQPStdzIyiNNUjpEPhOCMOuiyCJ2jkfM8tLgqvwZCTNkkWSMtrIKX8eokb7FEUfi1Wzd15R4wwOOKoMiLAMqdvmfkWvTXATj_GMyz2Gp-ANxCZQAUWxVkys7CBz4No-Vb3qRupO-hOXFlmd9fc9mk5WUvQEZiI8JU7lnFk5760K6Tus1OhbdsY2erl1hVVj8eVyaNgrZr8WlgCl-dpeFQCRmUYuSiMV4jXW9I-ydFk6A4UjyiXlzKHUDRm5t8sp-rVu1F22p1DFMPl6sCmRHUFJY4wq0RfXzyUzvUw87TJSBA6_GUv8M4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZZ4MIVgUVzKk3uQI7cmlTlDmVRyN9GAcZpkFLvrbfxeS9gzwEXnu4jHfgLJxPGZd3slurHCEQI3CbTTeCuvOJtJ4vE7si_21yVAaDNhOwCFChpvpgxzm26L_gVEIcc30eZdpOIdA6C-t2258JoJ2VVlArghn4IMOkFVdORNnXQCuSRaXXMS7GE58rUdzXv-iMwf-Pq1rvNWmHLBfPQPHAuj1Zoh28RNGhcglT73Pi_qsh6vlPUiVhnNsDE7figzITV7VjbzQUsZzn6e8tLnTfhleDC3ww6SfcPdSF8tU0XEuwMaAYrt2Wo5pqzQEBfUA-JdYiSdbk7vd8MXIJbz6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4UCh6jnxt6RVUVVPwm7jGRMao0faIIl-mFL8epecuiW3edJ_sAm06htd3HtX8L6hw47bHJGvQwbfrmuOrKVpUAJJfTiF9GdAb8cwNY-zmHojlIdyzC3Z9Now4G097vu5b8udwlcwIZ2uzTKS5eInUmdff3Zac3HFVlxJRQY0gbLa7FbVBIWIIGN2bunMvJFMV4Z2m1rEFwEmXJ37C8NrkldGF5QmT0gdOtkJas-9Rd8bFCr90SIidrjhdmNT4AR4-FsBsjH-inkk4I0JMmT-wAphTUV5heJB8WPYmxZQMY4byhs1w1tAIhqbHsahIm4iVvmMALNeQ9fZqTIVsm4rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Muc7zRGD75YVrNtENklUYYu_zJgtBd4ip5vejERkiJpPIpJUAI75vMszc1Iqs4fGruXf9f_846Hdwl9S86GIKumjJUZ-Rp8eZedp3hE2-ShBq2ONw-dcFs6L4ejrcq4apwHOtRDlcQCgYt2iuYX4nRPGBBGhueciKKiHSU6mnNUHiTg2lTWGsZn_3dmsiyyAOVqtHgQ7EBhJ_cFf1sH40Nf4yUjle89Vb6JRUWFnaGd1CFLGwBMaqxNTor0YjK5FnfjIK5LhE1X-YPq-V3Tjm152lEH582CG7sP7437hdAGLCgkf0rBzU4T7W69TzExtqQK1Y6awYSnULxocE5FMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8BNYE4hGO4JWeGxOeyKjRGhWWoDdudzRHH2lES-6tgYz9PoApWqg_Ch-dc13FKbDgwhsx8W9oYFG3Wq4E_s97IllLcy3q4nPYhIljKMMVmOYEKVL6Sy-VgZczP9xbaF72NsZk8Y6Ql9_y5hySVnuWK8lYYOdNIFkKpFfMpP1ff8aMff28_nuCSjoi2L3iNyjqc9aI_jaYOIO79HPsjloVLVutwrUOT4D0CjfkuXY8DB09q_XWB80p5dJLHwyY0EhOmODua8px5WvYDd5hAXBgjWvz3wEGKP09kLDuaary7d4T9v33SIbO_bAA-sNKN1dQHy1Zpx8tJWDIcR_SYP5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP-F5zuBIp72gG6U7S74J2_DWNyjXuHpDt3umMyizElaXYX1wBTWcYRnvbHTT6cpWSsZDp4aRgA2ydlskao-MVPH9JDUimPw4lSqbYN8TI4KZ2YpufK2v45iXfDu14PXp_ULgAD6rvBZRATcKVYw_nG9tTguZAthW-4fgAt6jIzjefq8BKNU-pRHlDcfuvXp-Q0oLeMzK3TZ424xALt043z6gzgtWAt2EzImchFNfshGMHUaX0gS1XgJ7QEMBU8jVKtV_ZCYFz2Qu9GavB-pmhwkQXR76tQAPx9UMubU8OXP6PfOE3iM8QmOrqK0ZeMHVK8Gnk0q8KEjMIQCYOh-ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVMfjDuDe8DDEMDCOrZeCOGr-qd850N9-uQpInHCK91wqKmTvF_hGchSl8TBcGnIKHdmqvMKDNRwMIweyqAVYMEYxpMjmhsI1sFdEIZvLWH60yrqcDJlc3Li1X4E3JLcK-LjB4CobvIOnD5lXYqx24K73f60xkzSPtNAQbBSqGcpMNo3dvfBGhvyZdgRMBsBFELIxKkrQkjKNp3kSXyxPQkGXom8OiSN8Ft28L6EhiiYjrrM2Pdqd1NmdTu0mhVfN2jf1dqTDGQJJgVa4-6CvM6UsWxXmpK_Ky7v5ixjpCLJwzMtUWbgPdB4nENtIM_gbz7pT-o1KjZScsgTKrF6oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxr5uLt4atvUhw6fMyIl7PwVZr1m1ixn88lE0czqZMkRWlGjwXsxbpuy_sBUlj4pIsg_eeY3fl1EzZmMjP4PG8788M7dLSLde9F2p1M7E8bM5Ri95_68r3hZJk92k1C1oEJrOj3chR5ZqslnALSDotPLDz_ZnIx2h1l-yrQCWRCZLcRf9RAL3WhCjx4Mc5KzffT1KUY6UXBaqlxiA2UtwCF2M8k9RMdrU_ERSgGtYNy8OJOmEEMVJhFxleAOYoH6ISDxEdibBPIhS-iCZ1d2gohts-oEPEPeyqv2PBe-BUxSo4Tlki7rdFGbgsPmXW1lxr3SuareRaV8hTkCM41cSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBJqpspAlN01X-m_zWJA-G7B4xxTNz0gv7rxBEjJPnKx6XsFDJyy5L6UOiSfR-F2E1ONBHcHuzynAp01u1V3OPdODXfgyAlWIZWLC5BcDFRpJFJ539nikx2BVCbLnvaNs1BZTIMrYBqJ1t6BUDgImCt2WTy-wqi8HEBNtgFxBIoknsGfaetTYkv-L46jdEcdskyQFqiD3vPohYWqQTyqMke6xrUk61tUtsFhMACx4DLG1Uwyv-xGfon8SLf8LBFrURcnJlDEmsLnxF3IcgfHtcPbioK6wDJUbh0Zf0eNqLeflNNKY-1Hc6EZuwdqiGrVXx7fWgysMhK0pdTiz-iC4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbFTsYS6XzqwRgW0mYKc-_aqg7VJ_Ipl6tzLwyGL5Uv22_Dw2rm6CTZ7KWKluCU_bAXh6DNIoZGoZ7A6694YABUMiI0x4U7pg7Z48leRkiWe9LFhvAqCe2EQ-D2SLeBlt1fIFznImh1XPzOSNpnMJalRD89PFYN6kkfZpTMd8oJdFFOrgcIGuSVxNmGOP2vtFoudPSLzg_MWYd2Kvsjs_EImfO2kfVsU3Ep5a1tNXB_EhRjTYL4xN4mSvT6heepktwvMgPUgomjRi5uHT5GHsREjqAGLrRiF1-cFAZ2fUVRiwb7uSDCw0vZFHcqZ8enOp5LpPlTRl7ID-2EkCgdFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuHIfj7pzdoMFksEda4KpUiAizyIzKd3buif0FJaJsmKUtAnH25rUsUD-8V5XxfY3tFDHFFUtqlbvYWcMF_DTbNfnMNocoDTwbJOGp8qfJyiTNCveXze-ZwLeDC8leLOPZAkGYfBQ5wQN0VdrUhlHlKUkOF85KCOTxypBxxkLWLG5iSeSxvC3_JKgP-dUk44qacCd5HmEl8avYCZswhZuM9UrCpI2zxFHZaZzWvTgX0cNb7hf2HDGAS9_kbyruLD7kmwsqbMMlYARTS0loY_etf92Gqj0rGKKY3eJ5fzRBHNejlmHN39wE1rBJJEepqEOHUGAA8sSae2AX_NJYfkUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NruL_7oINRQfSkcrYg8fRW32KY29p5i9Ql7HDxkvz9rRi-rvqwE7QO1WpukDpY5Txio8hMHDASWt13HmfvVTEIyuEK18thTmGOu0vXeX_3J4liId3GHT8WQ4EeJLuEOmrZIvudpcjscvwlsvlrS6AKBiKMUIYM1iOFXfldhc5sCBeEU7BXcUn4llEcwDzkAOld-DcCantwYeOUxbfqifGnONhDRISLYCmOuMXRxEmq82Yatjqi8QIZO69JSz7iGzdbU87Inq7zYxmCmC_ulUmMSPbC4gkGfT42ruDl2oKIwXdD3SSTTL6MNERIxA_DtUkm7uddKtxgn4ernw72WOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMT6jasZESG7H2yTIfqUOrkWjP1sgrByBDzjhRa3-4rmFASruz2niwyHaLU37Qfd7Yu5fORcqDGOUPLXGbWse9rbNqS5V9MTDhZBUR4Baou1GhMf4-Y3vUbDlYTKPvGvWZFNolkHZcyINz5I3ldW112LcT-Mo6a9NCPues7Er1KhpRMyR3wfkrbGdTsbzBoIij7U0BtV_z2er-tyiv-sCqKLsH31_ERgEqMh6q15ZQZwvVOUUe3hI2kBmR0LKhnra0TAfSiyOY_zXk_VvHueiLOMLN0y7Uav7nOKaBSrZ1e_j2EbJ01pTJA_VJSLWwNEQ63QJggs2jJc0DWZdHUCLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX7Ncq1N7rLXLfziDScWElp-7nT5euyXKk4xnI1ZmyxA25HczGven2CR5rmCFWLw7BhJ9vUuWX_XylkMKJkH5sTO7ohlcbvMPxlPulKwTgfkhQVKQ56LqpYc1Qj9qU59wxxWVAvoMY25LtBC_rf_qvtZv5Tlw3fB8BFDa0v_7cpNubjsywmYmmvbnUM3Cd7GWXpUJea1Xk-nkXM1TKsa1LTXGrDO8BIrEthsuM9cFru0sK9e8ya2n7_79tnznxWXH5vc97thkBmuF6r7rcZEAjkeyD6Oy2tfoVra53qBmgY1N8dsdnp2Oj8q72KJY29pfLpg53F7mzlz5N0A6gcwQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cez_BkMjleCq93xtfJehjIjyCoHDTg0vrwlefQFnB8yiOWmqcjpFSfq2XcvtFxcXzYZ8EcwEFS2jO8crZaSE66_UidmNptSe2IgI6k9HSjtHeSY9Vo4eIkaVxLRpw9jwZuAcH9a7lLTFd3uGaGqAcQf877rpre8R9mow8QVly5b10H2AcwdzYuxXBrcQAmBj0FbgZN2iH7_H4NBJWRi1bUmFqlnSqOFkiSuD2VoRKnD3gCAMqsWPq3WRFsoWtTwCSg_ILBmyMwEPkB_gxHIaul7ZXS0xw0R2Ve-1b2U9V19MIMonLffXZl6B7sweo3P-xm60Dy17fIhFBnOBKAQKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNEk_wf1Cd5qFmifUJPVHwpEnZZjftnBbpmBV0GYCktMDhWVPw4jtJnTRkhYCDDITjGi-WYhNp1G5rj_DxGe4La5lDF3L8JtzKKOFm86RH2cy97wAlmXtk9NqCnAG9-cS-EwqZyPZUZHNc4yCPmdFrtD5N99uVhOBSHC6G1JhkDKWN6PZt0KxXA2VIYzTH_9GB5kIZaMc_3voKP8v_cShvZiI4tFlk0VCe20WkUVGYJWPVP91TOz9IFkN8YDeIpAP8GY7w330mBixE_nvUGl6jMiD8XKwIUcmBOQWiH4BFhCFpT2CkYT3tgyam-94r2KXQaaKu10nyUDc_ekkwCRcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv1deBwBZL_rPhcltPX_xLcWFGC2ZL20gwwWsYJbWlLvPNRsn0DrMNoa9fBkFLaDzfyktlBEl5TRoyfSBu6eIrwRp4YAlBspR5Wo284Lpr5HL12Rtb0SWYeGfcIEeVI7b00oaUcS-FiiAKBLpWPNghXIgmBx1GWsGBUL2TMw2FchnWFESB7FV_z3XJzx7zbKh2rcjzV01ZLBBFW13iHoFQlIwFxzMZpViY5Rav7E5NpXzTR-54bcfzhvNejDGuzS-ytFIL5ygcVQBzUaxSXXtyB6DUQN1JSEj0CGC98O-pTsbh95bMrGJW1zcg7IuM2Fb9J6lFrRVXNDBPlELFyLfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4tSzKigwQlPZR_q-4udPDZyvjndFNW0_F9-INKuqN9EpELBUyCgvAU0sBihV917JoDzNS1W0y7M2afdB_AQji0-b4CPQyD7xUiqMn4ivSdAa7OyA4gsUegZMEiOKujeNjSm9n0-6VjpGQtlntPjPgP4aWg0_MieETNs53UeMHsGi9DCjQegEladA-8WnH09GYp0NKcNG08K6MG1NTuhWRZRuFa8OvISRGZiwWEbT1rj2bj42vlEx1cPNrdCQOAEtT_G274EN7USxXjqSiGjxYcVU3hOh727G-6-pL5srKhmSYQ8FWpla6P4aPvHAyj9Czp1JngBTBBrYjtWaT2pBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDsvQhy7iZz2uyBOS2bMIIPjBKcVkR9bK8MF3ZtIUGuJEhMrbl9ArrjC_lr7bJGNSYtovYJyzV4NVUeAl4pUI2R0c4oXJUXNuYGiHBLjJhYB7w6v5CpRhL1ob7u-ZKRrE--eix7IZwNJk4umxHckrkdKJTUPaLDNUjeOMC8JYZXzLr_arNuoaWiLmA6rdWp3rLxvVPB0CyxL8_zyhChT6FA66TR_bs8T4OywkxDU-qpz29cyLr8bcLlFAIseaBkJteEmVbxP8Y5jqIuKE5W6iTV3KLPcIfI0vJ4npL082BpwcmbQuB4Q0z0FFnOQisMlRzC1Ds2lhsQs1BzEpVT1kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxlkHGgncYWVbdsfF8D4_OEh9c066SHbY7fYRN0CQm-6nWm2E48S5ILQJkTNaG9YqQimEGoTgUebvfkESs9k-JgldbDLod1oWN7BwzZZounAx77FKAfBJuVRgfaYcXpmOaM8_DnKD-_gQArgIOVr11nlyo2Y79osZhNvPjUjLX22LJNXp_SCblwdLmkZUsrXUiIMVZHHZgs3RonQsjFSSlQVmpln1nTCqf_lAu7rfk1qQdl32X4Sxb-Mh2wkqZpozwOzEyBA4aMGlKM_Ec_ryrhqzoI2qelayfd6GnPs3C-Qr2fosn0jcIvHhOIuzD_500UlL0MAJND1vykwXiCS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NptqiY2Tc9Cp6Q_6NEzwzezAMxRxzHDEeIxeh4EC-0GEOJXCviX0kG2L34VRIQWkxU9r2yv-o2VpdzftqaqxpQIAax6DVZzAh7aPDtxJ3DI34Bw5OdaGqUZE3RnkmN6KYbkvlzyN9fvdmyWtDRWoE7phfoL4UZ1MyXbKcHlyfzvGYeQoTtKB38TmvPJtQ7K7G-D-hhO9A6VBfhN-qQJK3YDPEXU305gCv0PdTZawrukhZpsx8mhR1RPM5gppEai9bhiPbV_3Z2YCurX8j8LiTz591lk5oceqw_Vd4t1jbwNoq7uMEl01kqr9jbfgh5hrtUVFiofUv2XLAgJjn14Q0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjamNXKYFhvqG3Fsu8S9EO4JnmA5BQNIUQJUBtLGM7D9S2yLWWD9p9dsB_CXUhr6DMHuUarp7Cy5nEXJBetrCqv4WDFRhdpFOVc2v8D2NkmgK-iJgiwYJ0f-mF8dpKnbqmNBZPsyRPYy20aL_g1ZmN0Nc8jGnVgENpjJ9VDDD0MqZ6yzwi0iCzGodoLWJimLsmti6SzfM6zwlhzrj17KzH0dmC6f5ws5Qowrb7HBxAMtet3HBD19vtsXKgUlhzc2leoWxozhRAEXK4pd2eHi9fmxWSCYMmeEu1hLbtaLDAbJzTcu0xHoJ0s07R-cEdDFYjYfsqLy5L0bRY5J_R2esQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Byz88Bz7KvP_JMHsz7kS_cGWvMIBoXWEk45uiqKOxT69ksE03XE9ANpqFmBWiWGnIhUzWboP_q7U7XybEEPO7O1QuZ3ZmNhTnm9yeNbqlHDMVyBEk7bN3rcO3ks8_ChZJBFeVWD7qaNxr6YGeXKIgiUPCZZ6-izs7mzrTOwZYT3WharIoxCRBkTlmxP7OPfScJA3kWucelE-s4LzAgFAJN97y6HxasCJdXJXGYtwGEFwUJe2k4acRx-sCnagss9Wbdd91zUiEdMajSEszkfeWDcAmekl5dvo8cSt_hWgdebpYgQFyKrDQd43S_CiBAWO5i8HpQdV9utoGFg4Bai2NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8GF8x7pZnxq7tjhWro7CggE9-3fkS-FIR_mO5r7Eps1VY5n5vxmS0UaAANn2CPseaSB69Y_WADS-r6YdHtzh96nBIFWY18Sw27wHcfqxS_401YHdSUFzd-yScA6beVzJeuNIo-OosJ94YSZhhmvlmf4PwbKBNR86VLhBf90IIgLWxRfvz79j2KdrOEtO8EeBJuuX-pMJQfMum4pRHGCcTlGCoZhcyI0qwr7hQ_Re-KNqc-DF-I-AjJo2gLRy132l4MfBJ-eGXh7rH0Owe2bgBRzs1ESEupTkeI8ImKoa0T3iMIf4kBRYGsW6Tmjv7GF3p76qemFrzLbnACJzSquCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVXQJlHQadjmcxFLQ2gGcY3wosphr_C3obrrmiBMLKJMpZfeHSg_CEFB92YMr0jKuk0gvrIi6bCYIWNF-VzghE1bXg8Kdf18Pmx2tDLvC4Kt-SDdIHyTEMcJQa6l2Aj9NKwQv_oW1bRUKJZrSqVNmyZhkUCKA5ggBjaz2Ej_Aw27YpKL4CQd2bCC0oQCBq6gItjHgtq_UOnscaEQWLCRjq_lYX-nso1aG9zBp9BzYaGj27NnBFOCV8-SGz6Cz2GuFSVBhGWxm6MynC_8PwjdmWjtE1azDK8SSSLM8q7fnH3duxd0UdOG2HDicezY8kQjuOExO0vKEggjAm14CIyCkw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=FUE9RN0gmrtutt2kRCl3U62C9tQ5Xg_nThKwSkr2AnZ6lEaasZoX6EY08fgrRbe218dAsHo1wCBGZ_LxcslwkNAtK1iLcnnjedqsGjItK5uEoFc18n2ofxnWrEkQNs8uOLUBq_BCDBSJOXBnhXQZxMSQuxDTAYvdAbJB3zTu46nMlG90EckEMVfqfCa2-Fw1sg03Z2vk5r98ySuXeg6IUtcjxA31mAuVoLJ8x4BZBvJnYqGMwYUXMNu7RwJNX1M-nGZwc_B_6JyBXLFrBbE6kibU4DViS-93QEmM9ifhjpf1ApBO1Kn5gtn7XIfjqjitiC2jEQCc--slFoXXCS4OPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=FUE9RN0gmrtutt2kRCl3U62C9tQ5Xg_nThKwSkr2AnZ6lEaasZoX6EY08fgrRbe218dAsHo1wCBGZ_LxcslwkNAtK1iLcnnjedqsGjItK5uEoFc18n2ofxnWrEkQNs8uOLUBq_BCDBSJOXBnhXQZxMSQuxDTAYvdAbJB3zTu46nMlG90EckEMVfqfCa2-Fw1sg03Z2vk5r98ySuXeg6IUtcjxA31mAuVoLJ8x4BZBvJnYqGMwYUXMNu7RwJNX1M-nGZwc_B_6JyBXLFrBbE6kibU4DViS-93QEmM9ifhjpf1ApBO1Kn5gtn7XIfjqjitiC2jEQCc--slFoXXCS4OPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8h5RlqpHaqPyeLUA1agiVyi8QhcJ1gUzH5tU9cuw4_vF4JrkuxFCpXncTMJyNiQoWoqLzxkvuUfpGsc39qrxi97CLJPHxDkhi9g0b3e6dXdtEBajsDL8zry6iUhDcmuT9rDQkhBGeoifJy67gg4WdkyCeFSElmOtsVJDmVt20cIjytT7X_BCfufRtqfYzaN2lTSOEPi28UFmi1dxKOLDXl9aoP3dYBHthw8XHnH_wMVFA7SwM3tb_EkpqcY5AetPVrOvUnfDgBsljvp1EIsl-qFxdP40fJ_57wdcBuXcPQt0UCMqE9k90mdpzkHw9rRQNHPTyLusCLn5uuqmrN6EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjPLYzWH2cB_qBoGZYwUVzAFieVMgii7s88CCsCoMCAqxM_1NGS_q9mx1q0eTaT_4jvj94YccpEiV-PuyMBaS4VhBFujmwd5OfufeqPzN7CmGgeC6GkyO5VOeU58Sq46lZFhi4-zsWu7tguh83l96NP1xCuj7-Q5e_91RzAiAZQbNneNwYcAtIeBncqLg3XnSVVTA6NBIL-2fKDHFgUqoKtlziVGaAsf4zevSBQ7TKknEJyMq9Y7Ip0VLRaOGKcAWfx1r0veKLpBpGShEuCNE_FqnA4qrj3pELM1ZqsvHW-i-Dtzx5PyOWEiDQRKBgr2C6guzw4p85cFp0pWa5pIZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLIJIthBDwR-zK6YivGqBlZeq4lgZ86tKeUkSFIiqq7OR0iy4X8DledSqli3Z1II7H0433igu2S1HC7EB8HQaeEVJVtEgWiO4mSuN6pWra4feLMpSk4jJiividqks6Ul-TXc38xb8tlTjUpPv378DbKyxUBoap2hUULD7qY7ty-9px_hSRuF7I853Dm567Uh0cm7eDUbi9a7yzn7HrBrBkEqI2oGW3BYhtLWJKa7O2A7F8vr9JN2bl4IgkmWlUW-4KiKbNvGP9XxM78OlwfSt0jNOem1Tyj8Rfiz0M0nXno2kCXKtTDgKgXye0fk2LqduTt1D8sQavQr5TWTjNlTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRBHlLZFSZHJzEhHBzGxEw6H0s1LJkJjSkX5Hwl0EAdnNfBGDdXAF9x0Ap5zAWPj9qDPrIKmQ-HZ_igheTukQSBPAMvXgowFC_ysCQfLD3z3IFQKKu_nIjfZ8JmCQXhtVRAHPOQY4OcbIFMAQBUmdYqb4f6DqlPOIFXlnQ0AP9AzNbPrusTPy2xyxP4TzWKD46HFWQlHOXEgzaVf0BngrPKVXIy7FIND4MMYe9LZv4rtvOWDCJ6ukHJFSTJupMZX0CDVSNdLYhoGdDD5RGwMQFQWJ7-UDrGODSIhuyyBVmziv0dPIqxNxD3NGf2hI4LXb69TWV_MbOAFqKVMrBunDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbbpdhBEUetfZ8VVoNezWxvHV0qpD5lJnNSTezMulK-I9KMMQMldIa-1Q5SwAMryjhi9WPKku8texTtNBgKH6Ud6xbI4ZvX4hLIY0fTgzxRHFPbJjYo6kocoik8Rymkko5wVmCzxS8-b7JJIIcYAHLRossblhMAX3IYxUI2B0J2imnBcIo-PnrK9BKMOBRppZeI4zgbatzTg5QsB1hXMpL_WWoQbDvjgBpoNl1HSgwKC6Nl733GZy5JJhM5tHFkk6r8-1adWTiynRP1NisrgjK8LJBO3IsM7ftRGfLBqDt4mvb0v2tAertQLL7cZFAqFbSFTH7Bv7-ZiKvg0IcAf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVMj8OWM2cVd6aKxbqLntZO7Xa7-MrRh05_2P1vaFhWHqyCgKBDrlvZiRJ5SQF19-YusbzVdHlE7FQXZLvAk_PKksD9wYBlXn9Fjlk64-MPkfzObqbZqTuWrOHEQS0RKrFuu-NsahHUwxkLbJobF60iDOfCuskFBYc6ijLw4KEurMqGkCGJ4N2xazs1rYDaZLpANwiAJDw3eAMwWA8SPR2MxSOsBSHUx0iwEQuAuD3GKBdPkV-bG63BYFzH8VmpLo_PkEXa2s2Ozp0fdXleTaq3jG0MhghMLk3GSw30ZjB67dudbYG4EjpqL7E7RhmxrwwurZ2qVrStkASsf-WA0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7AWSAEJt6BK_3TvbHeh_bnJc1J0guFJSbc_uOWM6AysKsPQJhwtFlqDpw_m9Ijix4ZQgWXKfd_xxWuX4Hm8soHYOPSlbNHL-IQl6hmJnhh9WUMv8mzzZs7NYnBqZ8Qa6KgkhBT0kauUm9JLg6WcGkrqQlmc8njijTCw4tkAF6wTMpi9Zwq3TrBK62FfqSl2Gg95P_dUS-4-Q22P1q3-5wBnr666ATt9I39pQdWW5UH8wuHj5xLzeglNZZfGt5AIH50XerSqJGAr0fUznkpCXtkDRUnM1au7dkSsLpbQqmHsly9d0Smy0X7HQuRcFzxFafvwKiSbIzte6jYTQFvqDA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=UgzRk4JNkGDMnNPhGQJAGx-RIOxMdW4e8vyngAbo24VCDFKyi4YkoRZdVZBjImNQbXpQaWuI6ANQTK59_ufohOgM4BNHmdbMCcmOcyD6SoyHIgfmqXMlHSEws2MvPGMShb6ipAC0EBBf_GQnNz76kk6nfcAV5nUWUk-bQDp2Xn8QcHHsOJUSr5jXZ6Fjj-9WN4YyFGsDXB_rkpmOqot9EPcN4AAIgEVkuIHBHth6hS9VZhGlxHZeu0vsxkvi1cv46wLEQes-xtml-IFAMyQIMRJZtUwCXEjaR9nHHWx5fBO0tgIPKsDcQWlCpUbc2s-AtabgvN_mrBdju-klKOzHaQqNZuCgw2UGKZFEQbIvKe0RsITA_m9TFrCTRq3-Qf5om-97zuhEuQ47aVbSh9CbXdZmiKWAybF8MWpu2_Uxdisuoi2ESZ2v7Hvg5dDSgZdW4QnCIC5a1CSTpuEckxN3tCGZNTUr7-FqKPJCi78uwVBySqE9LR4MMwN6nxtjrQ7XiA7jVS21EpMu35LmyXEqdunwhSR_k9Hf78lQK6P5Kx-PcYEJxHuoZsZnAYw8VuwRaIeZKHXBqc_ZOOjzTAr9MCJ0As6MMN-YaIeTxCw8-DNZZYVPqBQPgaQm1MmroVm-VRv6RtuNJU7uBpGDnIH37Hx2YINYD44lbosGK9CBAJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=UgzRk4JNkGDMnNPhGQJAGx-RIOxMdW4e8vyngAbo24VCDFKyi4YkoRZdVZBjImNQbXpQaWuI6ANQTK59_ufohOgM4BNHmdbMCcmOcyD6SoyHIgfmqXMlHSEws2MvPGMShb6ipAC0EBBf_GQnNz76kk6nfcAV5nUWUk-bQDp2Xn8QcHHsOJUSr5jXZ6Fjj-9WN4YyFGsDXB_rkpmOqot9EPcN4AAIgEVkuIHBHth6hS9VZhGlxHZeu0vsxkvi1cv46wLEQes-xtml-IFAMyQIMRJZtUwCXEjaR9nHHWx5fBO0tgIPKsDcQWlCpUbc2s-AtabgvN_mrBdju-klKOzHaQqNZuCgw2UGKZFEQbIvKe0RsITA_m9TFrCTRq3-Qf5om-97zuhEuQ47aVbSh9CbXdZmiKWAybF8MWpu2_Uxdisuoi2ESZ2v7Hvg5dDSgZdW4QnCIC5a1CSTpuEckxN3tCGZNTUr7-FqKPJCi78uwVBySqE9LR4MMwN6nxtjrQ7XiA7jVS21EpMu35LmyXEqdunwhSR_k9Hf78lQK6P5Kx-PcYEJxHuoZsZnAYw8VuwRaIeZKHXBqc_ZOOjzTAr9MCJ0As6MMN-YaIeTxCw8-DNZZYVPqBQPgaQm1MmroVm-VRv6RtuNJU7uBpGDnIH37Hx2YINYD44lbosGK9CBAJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jb0gfTM2ACx2HONmuQIo-z60HsDzSV-bDs8VFTGGiYaxcWr7SxUgz_sJCG4j-8f4h5bmM9ctNl1_Z2J-x8VA4JFoCBtKu2zUjw3FGmjo_Jo7y_SzcrlRTN0MijJ_bvpVACVgUZ6y5kuYFodPfXmehmOGHKH0iYW-ZBLtUrFULdHLmxN3AqHyT86KGh5Hyjjjz1w7iS4oqZ6FXjI34PWwFYuLkrII97SHkE1ZTQnS4XyekgEZePd2zv9fArlJ1AFDAZslxg4pq-_LNx74pzrBt5nzcOZymEuMwMBYGvISEnu-U1eIaqK-O8M_GeHzHbU5x_URM31AEXoz_DR-Gbrpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4lxGgLD8L4zjLk9uDfpwnfoO1nWL2xRfta7s6oMa_QZhg-wyWT67wRQxD04G7JQZTztQfyc5banFVDPTw_D9rl_rW9nucUR_64Nhh5gwi6VaI2WDYcSpIHrIYhzyoz8CfBmvTQHbySCbFpzRf8QmCXIkq0iHLv1AN3oHFXqsCzmT2nJQa3laGBEwzFtNcVpIUK8Sl1RndfEO5NzRl0p10VMOVGw9f2Y9dcrUIy3QFmxNEifmFrUCV016mnBPW-V1o0nO2_eYqqpcOClxHL00QXW36IFrVTiqBnXW52JTeWR6yWCbpVeZsweEmU3JMHSilheE724NlW-spUAU7eY4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf7-hCDBNlLz1NixmEi4Hk4jJCBz2erdDLOw3QEn8nML0bRz-6ndRDmH-C48v6IFUiVmsU1ifdrxoyhCEyMH33ymmyafcQZt9Tt9rmPYBzdTwW5CSihDfAbCTCXz85aox821wEuj1veVWIMRYFxYX9RzgAqOjuH1MlFrOVVB8G8VR3DfDNvXl0iD-nLUm4rNIgS6dWk0ZcYmQws05jJSQ--O7cyMITWtDTj2C_BAE97TsqdljdZHX2OflG2NEDPTaXn0Vkr01Xs2VemzWlbg_DYbwAKjqfRb0-3hZ-NZy_SPpF1gIKJjKrjopmT37FB_D1MlnJDfJv1Rdi6P8E4tXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jex0STOMJxXa4bnhiCRxTu1s4m8I8YZwsq63MH9eq1zhIjObP_QIHgaMOZ225WlF5ATdZ4bHfxv0IQgUmssHk6tBUprjITcy73FLLTAjbqzrQr4VXtFu4TQ0iG07-a8OhqPmaIDyuMTBCTZXqSyf7_Fn4w4iUFpi1adFCsfBgrCBj837FMy4TEmVe9Ul6RJfbIlhAf6-G5SMiWZ0UInU7Exxay3PlYqYgzgdcYis_erpGuoLxNJfTBm8DY4Tsg073xDserC3XrVOymMZn2nHdHDHzJjtSg3zdXbXPZ6YbzlR43E4GOwHSRlwBiL-N5UqaEVDt1gb0D09Lf6-N-9P8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXZ6WwpKZrfUQRpbugN3O0kLiKFwPLLL5Xix1ew4KaY4Y9u2i_kHowl7LsqHYxhkCcOcu0jn1dCkJmYOutTn9qxMJi_0RYOcMIDndjUF87XxZ9ko3AhDvJUwsat8a3zC_FxqXil9TSctnGYrfKmsjc4P0C99sJLxjdRcw4791bhPBdxFjV09uJypVLyxj2P6mW81I1ZVBtTeRz0q6WHAow7RSwTqVtihzxY4Tje7I0IxhOT_JKE_6nvleynMmcpjUytIGArAaXfl_VHNCZbuFLxNxcd45ael5dRbwaluU6S4ziLyfNhdcKoXSBqmS4sDAu9ABsE_dwss3thw9MMKzA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0XzNTpnk7v5fqoWDh1IhivuPFEr2k00zBQ1o-huCVGYm_BtNXgQU-AOftyCx8f-UHDCofLJh5gMFL4tukX6h_0ZZjh5GMk3-17emclwIU5rPm7k0rlT_3auR_oLBlJbNLV5Cga1hz-VP8tkdAQU_8uVvNJQ8XGcuShfQpPZRx3Tikzw4gBL28G2a-CU8QqQriRkXfJ2JZy3L8dt8qYvM1EgpD-UsHOowjtSLZ8kSFyrSvavPVIX12NIW9D-w1YQB0U_A66FAU4upLZ2F9NZmSs5hvHGn0hfvi2pzMP69wr8yxNFj-vt_HOba8e0cxUNVTNcCAs0LTVbxMOo3tvByYos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0XzNTpnk7v5fqoWDh1IhivuPFEr2k00zBQ1o-huCVGYm_BtNXgQU-AOftyCx8f-UHDCofLJh5gMFL4tukX6h_0ZZjh5GMk3-17emclwIU5rPm7k0rlT_3auR_oLBlJbNLV5Cga1hz-VP8tkdAQU_8uVvNJQ8XGcuShfQpPZRx3Tikzw4gBL28G2a-CU8QqQriRkXfJ2JZy3L8dt8qYvM1EgpD-UsHOowjtSLZ8kSFyrSvavPVIX12NIW9D-w1YQB0U_A66FAU4upLZ2F9NZmSs5hvHGn0hfvi2pzMP69wr8yxNFj-vt_HOba8e0cxUNVTNcCAs0LTVbxMOo3tvByYos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk4-45j1Y3MMmZBZoItj__kAlhJUGjTvnueVoZQKEBRWPFbYXqvkKF1igqcrTIXLF0FPmHNtFCy-NfqkTA6ZNtNKybhpNF_oa1MN0n5StcHovILWVFyPP4FWOWVGYMfUuRr0LA14LFF10i35RIBmZ6a6aQ9xJitiMtPmo1xeH6QuqpDkpx7XryvrleJb3NvYq1tot97kEVsU-_qP0-Vy8WgtQzT469bb3xzZ84hR57sbA4gclYETxRdWlJ66rz0Tm2sQlRq46l7jpHnBWWm1FJRGkUe2IrdPym_sgb6t-0VXvd-soFxNEOC6KBmUJbW0vvDjyC3CmPA336TvMPVOWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaomlK6NRGYQVYoR5h0R640FKYDacV5DIBNTMh6jtI3YLkD8y91Y66iJu3-KTGAjHG_1pWNEoCn4jmcDWVREOOuuANFSVIIZ7yTfDs8nTNxb3LXl4T4tsCuEKvxn66IgZy1Qr2vQG_161k0_bjgYVsYhHr6cR55Dl98hV94w73NvXhqy-d3xP7EGl3rP2mID-h8GITLcufCWoPuqrr-3ZVYy54dec1BAkcKpwRu7nHUpwOfloJx2uQWb0MEMUJVhj3KlaKiyPJA7G9pRSWvnRwOLxpIo0uC5KBPeertkGK6X9qvKJn2M4oQFrzfOACZsjvLaylMcHXmL2K_XidG_mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZerOV8RYR06MyFVclWtsnMJh9Jm9l54pUsMMano-gBaWtB_oMJY1nysJJAFUzwBEo5SPl6TFM0yu62h8o-lybVE_qjcQO2lROWIoAa3Om4yPCImHx3pULv4-n9bUt4wwKsRd6GyqHVq-Lz-JEwzEXP5Zway3m9z2aqew8pwdW7JX8WrpwbFl9vI3KCop0b5xv-LZDJRzByX5ZB_hgEnIkHBjLydg40ZKJNZgGn-wNqwGDTRlU3Bzfy1JcFAq4gkqiQ6y6_q6eh-Qv8fROqEolj6ZliBr9FCeTyoqHVL8pw-yLb2g5wjN_tIeWeDXD5G4j5PuvOqZBSL7Y8mGlc6R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOyUOyIceQ7P9YkME_3t5lXmPKi7MrVSNeUL5n0G_cKiInka-oagnfsKbB9UZss2vXj2CYCcfGVlIDxyG93zCBMEzwKZgcJ5-fzWMOdI86ug_-fVKua46DHKVLMQliyQHSqQM04KrjNfzrzC690YZ2ZSkxi94ThwTXnnfFYgsjLdKpQj6KNO3tVWRJ4sS3_M_LJdB1OTx7Atms1h2XOIVnMg_24KS-N0y8sY_hTv8zeCY3ensvapFf9VMQgt3d5sEmrjC0SK9qnGB0S8JdVoxB454I13z2N9qmHJjCSBvN51GhgnYtFuGqWEupE8Kd8pkUpnBnYXYpcGpv6YGAkApw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J73oEEoZnit_dIM39d5qFvlj5qvlHz2UImGBJj1f9d-3xdjWqs7fyt8zxK7TI6bquqx9kuSt04c4KMSuFhmQAw6DdRGbVOKPAPQtG6NhcKlBoHeK4GAO3syN-SGu7jaA1rZ6bwkPVexUmkzqpwMqRuP2K974B8OKAnPorgtPTd7yquQ7fyDbNTV79uYyYt8GzLACX1ZFjhxORluSMsD12iQJBn5JR3KztPLEXi_z6sSK87D-a6X-N1UOvZlj-q-FkpHw7GomlGLSzXPTQJ0HrZ15bxHHl05ZyIvWReIlDXtFMdN-zNtl27n1I3e8N1f-b3cAiyAiFX1DQ5x2XQGWdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er1XO6y2Igv0xIiR4buufy4Ux031OrcNEMPCQthsp0f1ezZYUIKuGSf74cM5lXdOx8eM1n1OEpvuXwgav3g6wiEmk59pyb9ZceTDN-eqaEO2VGaxOjnSjbFbNemPrrWrFZelmPpvtGcVlp-2nHBM0jTFd8_NkNZ5ekCewqHrvss1iLz-db-6mwCfEraJiOA5bxFS89cNVszQnz7-I99k2Whyiuk7Wz4GmsCRNOa7V3aDvXMGiuzlpvAU7PEgdyiFQzwm-4lRQP-Skj97VHLVZvUjFgnf4yQUz0TVvKm9-b6LYfpOoMLeUW98C9jTc6eXbZ2u9z1tviVlCKgTNi-CQg.jpg" alt="photo" loading="lazy"/></div>
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
