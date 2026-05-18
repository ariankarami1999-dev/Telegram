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
<img src="https://cdn4.telesco.pe/file/UgD4taVn6tasnNnMPlqW0VrASWKVMSO_K89Ti9xtekBRXjLr-jxxCRd3u929sFc9Tr6g5CGI1nsU5NCVjIGR-kTH4ePf2cOuGHyMWu1YjMp3tJKVJa3dRHsMK2-HhRjwa31UVlFQefGfAnPVs4FI5wWVmnSAMx4TNQmsztHlpqjmG91a14kWfUcM7Tt8cB9IIHmw_tCVl2-D4XN_8ZCyRbzpr-5jECJfV2-Gvc9KdNIAZzWD_xjDzRdCnl7JoGtKDVtMRi3d7UfKI21av-MCL1Xo6OVjFUdi8Ki9bmaS7mVwJNkuoPvVM1tCTlAThCzqNvXuZ9Dnv6xiAzjXuEDE7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.56K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 09:11:25</div>
<hr>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 422 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3C_wJO_aO0GbVNf6BtJGMebAY97wIwXz-KDyekEIPOsk-6mQP5OVjPrjaSaItYE7wlX_YJ4WojXBlUyZCDSb29cATNdoF8buMHbKSlzuC6YpvTgziusby8XpNSnRaUUGpYmZ9E4onB4A_cp5722q1TtbdJQg-Pp0OSfZc0xkVR2onFm3CMLrTR0BaDGs3XXGTTYbypJzoFYajLZPsnjQB3gu-7kKHOEe9HEQp19JnaJt05G_Oub8xomIqBzwmacIu_kB_5p_4zZGs35OAIE1Pd273uH64Idb8qt2lcDfYAC3WoeUyoPJfLg0nHbGqjaMExMzm9g5RW5_BLKV40VrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 427 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4aZCRlEfCiXib7VknfzeopsJ0veajYgOBLMS6-cpg0PqtSt96q78XP1tuilpPiZmDI2cv_QnblZ3zCN7UKsAL2mR3uKZ3T_6qfXIvs9qaMPAxEtAOH8EOKKh7vGRrQTR6pArP8Fj1lEPATpckzPr5dmrWH3I5e0S_Our1Ix3Mzj4KzYTDhWaezoTrV1VCJvbDxk5bsDkaUZXH4bLNmRZYQTz5xQvkZ1nW6K73JyFrbGutwMan34DK8IDkmc2fPNVVyIgZjOg2lzLIgqIfdESwWQoVbs9aTmv01Al2Z7k4eUp9YGDGa0kC2f4aTWQtYoeMXR-3DjBRp-C9cZICMKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0w5a2ZTLTaoHNmnerzOa_saFdICCWUi6UvXDBbQT3yd7W6jSWzf7togwejxK9jH1eZR3SkJ07F6CIjZlS08GDVkweD-8zsE5fgPaeL-tpbOvA5f1nOzbPuTm-CLxnL5hYtXOz7ENg6g849B5CQxoVorP6rV0hXj87VUgqkMt2ccDe4x4um19efCJCeKAoB6ewl75xFqO5IQYdVG7HyP52URe7e4U9wXjbG3crX7CAYjLt1eto71PRO2GwMcYXwOrsoKwkcORhr3CIFYqTyIFdvT-gau5b6nNKrnVXunt_-f32mezyP5-D90ruY91F-TJRa4S9XR-glfBGg2heuGJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeA2YYJU3cVodRYjRFFXor1I8WK3j4d5IQHhjOWCQG8cKAbnUW4gbSMg8kqAiUhkQLI9sJJPrwpxFF5efNtpWY3PbFf8shXOKrZ2eS5CRBxS4fPmcV03h9ynF4EyuoD4QF9_loC6IGX9bN5ZCAv9K1tlhVl8Z6QkZZuizbGIaQWnTfIEuwb2g3qoJnv5zcXJ7iZ4FeNKJhld3i8hn-M2MNwmqZM1_UDhET-uo2f1BHAVpMLodaPkqmjlc6Lb0xXFmfWe8YX7_VzEICbb1rlvY-3_jNdY4a7wDrNZP3D5TAn6s7khWI5OaLeBm-wvrIG2udy-2My26RpZGDk_GwfNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 742 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMa2WHyQDJu7mHK8C6YG3snFJ_DTyU8JCHQL_IiFFBmOyxdIOsN6aTP6M2zAZoVOGMroPyarKhXRR8USeQll4N9GHINQB8RTbl7W6UiKxF_pm4OpShkPWNG4B5M9sPBeXcoo7pIXMiOUczIZ0i0hE76-sY32k0Y1ThWCE1lfLRWPFLjI6e9oTDR0XY9D6jglfd9W3g5O2dIbnDdRag-ownwDCRY9tO4HdFAYEBa0qUeyiI_twhWWeKxAAKM3hPV52j66VDvowVhjmHcHoiq8n271kd9vQ3_BihU5-bPMpKacoWCQj6Oe_uccaJhlymuTTW6tw1P068_kxN6CsuzsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oobadYoOv2ZkDSacXm14KFXGEi7xfUMMSIomC57XVUpwfKY3usQoiVBLNSPwwEblukca3TfwnloJImc5VFIluBtPY1hflFunmNuwNTMJBpAxpqqqxZJnpPaN4txvqDkffNCi2e9OKz4HnjaA72bvfVyjKk418UEgVbD9veg3Pan9qeQfDaKBHYNwWpMy2dAUfCR7qGC9UnJ6SVQri-GGUE57h5BKIVcizDaC5krs7YzX_NFVn2KnnFnCzJPtQZbmocHtPYxzNv_MPIYEdtSAlxJ9a076lHMCAW_7ztukTaUxg5r5ss60UZVJz-AI7sVVfvzZmZV4BUQB2mYA3MEong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JchApyYMsdvQREreP7ZnDDQo7f89Alzb_o0gQnMcSoFn6VzXKmAZcbGLNzupo3fVh6nNVF5rgS2C9YiLeQULr4aolPEJP3eJdwp5WRAE0sHyVJ7eHPCGC2tTza-GRX3LIKZndrZFDTOwbx78mHTyXNcO4dkjnlK1Fv4ufB5oha_O1dWHIC1_s4BHJN_p6W63T70hLJOR7nDvlVO8jmM-r5uEffVDp4PWn4CFBhWIBnXncXOMMc8_-oxFOYdbpRip82UhKcDH5lgvJ8J_Vy7bODN7vkpiaFDGcLW2aizltvuMO2CJui-8tl_poeCisfyXdMwBzCNxZlTdkSmF6zICWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R937dAd9hW27O2jwq4o5oEVTA1Hg3ubBEkHFSvyXNVUuybAnFIB0R_tqNK4mJw7XWty19t3O1E6BpXv5JgKY6jrkGWLKFOb_9neqAcSqLiI84WxrzHIyiWioIrGZ0B9aDmrFKH6WPzu5chGGoTXa_DRkwwd7aRNUdEpz9qCpPeYqG57ffQFBqcM4a7mcHHvA8zaTQ9PGiHaG_aavbFLr8CjpV2dXBHrFT0uBIYwgFyZWw5AjUJnoqmI5imCU9zkoO_dAm5rLbL1_EB4wZkMhfyV-Tzz4XFCoPSvQjnzzws7Asv_JHS-QyMEQBtRU-5_RSqVuGeNhuaAEY_Vif-fDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmL-7r0piQdFDiGTgCGsf9LrVwGXkKQnf6Xj6Xq8NJXsaHvu4W8x9D9okSe9U73_HFt_pbdRk7lwvNWFmCDGny-TRILfiiBiBpSVkF5aTsNsZLn9EwfgZCGVU0LcO0cnz1cmG1nlQiq7VdIUm-v4rvXt_Kyr5Mnj1IFOxghB5gZ5xPrGENoX6fhkUbuHm0vRsyCLNd1dBlbb9p-g5euKr1dotY23RR8ziwpH8xNmXcmchJfzPDYbF70y7dRZqhdV1dO38vvAbs1EyOg5wk_aKXXti20MVA2bpccynA4PHUkFHGwwaRko7Q4RYwtOkuI_6gdaamY_mOdrYOeBV9v8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJjqwmyvHcNu7LkbyvyXQXQr6ImMg4y7yivBnbcwzOUZaGA1Yn6fnrOKODFAp5iZsDtWBrMiIXX9DrpdPCSH9Ce1PJHXU2dY_bV0xLhbk_pSyQFTVhRJSQ-MgH-TInyhM-cOxms3rKe3Yy7ZeBrjOFtZmPXI9_qyLp9YwN5CbHT5XG0d1iaTzhwki86NLd2mngO43mfHyBvLTiA2zWyob8Psrff89i1LaJo-OD8DAbederbRpop8E5pa72YBN0vg3mLmqMfnqL_r4LMl6ctM2r8XlaWRbjxmCSMNHHQg_Tm46lZffZ9bcwoCIt4-fWoFA_lqLhwerknscBwtRUxKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPlnwnNrzjgZjcQHZUJWIwyUGrEFr4FOGvhVYQTZy01A9U9FpasF8m4xB8jzfyZg8FkQNZlHGs5f9NCDm9e_IzIu40cj-5rt_4D-wR-dpSgmVmQ4R36U3AFr9oB4z8qBWsIMCdGLp2aRDYa0BcQuoGVV0wlq6Uu4X57ODzoQ5n-gCrjYaPrs1b-6e-fl6sB2ByH-vMaOVyIIhW711D8megquK2MlMhb5k_uwegE_Sncn7N_HGpJdJoaCCQP8TUmhrWnU_t1KPCK1m96IcRB2xIeJe4Xb2C1Gf8MgPl9xx7eRXbUbqlwcpxWLApQ0NOOy1GqWfMeX_6xdEkyBe0pW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjEJ30ifIpbq64fcAzKGnE3more6aQf55vCJ7XqCCExrDH3EUqh7vnYrTor3aSdWOyuYYezZk0oR8k5W_2NlpSUNpWusbq87nY2m__CXftjW2fQ1NLDk-GRLFnQQWjM2O2FS-ukl_mKaJmfv9kcKDIet16jnUHHOW5TNlroVvrUprG-NITH5ol8C9Wom8BIynrGh0ynAuMRZqOy7as5wmKrOxRprsjUoudB5i7T9CxqlnvZfvSGKO0mskhXAnncR_HAW8BDJW-zKtryR3pUp5EvLJvu8Y1xQPUOllfEj4Wre66a9UF-qxnORLlo0Q4MpKWVU_L8-stGCLqln_0aU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmtaPWsu5RJqObwBS7TdwUptpsN-MuR04cSMfHFgg-SsF_JOJshXZDKxxTzroPdH7Ph9c5Dh0nnOjSFiRvDMHy5Agj6OFM7A4Uu_LouWv44FEkmXG6sOyhCgKLEQe0x_TVHKmKtWSOVx6QCIHuQzo4NdV9mjdLhhb23w0HpPzZ-lT1_BdLVR31UzGE3HFIUGSOQdd0nVnqvsuO_tdpdj-Yvb4D_anAGPqXnIEjNR7mzJtHu4cWhpaqSiSBJd8dcR5luy0O0Q4vlP20-Pm6CcliihrubHsLWiC5b4Zhs8F1sIPqQf-Dkyha5fCu2BGmpEXE2mXYVomJfZ-xJH5CtJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niA83kM56A-RpTnJbkWYWMwyBIG65WdVYNV1IKTiExwYRn4YjfXknvg1rHMAvVBniN8jrfiM-FPRvlqKdDCQTJ9keX9H9AhU-0U_bbrNI_vDTYJwHv1sfZPCebZInPPLZFfVlOIZsQRXCuRvuOEoz7xFDUI41HiT9HUVWQvqcyE9_c1q_6hqMOJfO9AyUeNKBPCotmvaBxY5weDPLPGnpaCQD9_pwIA6FkU4gVLamluHi2VY2Sue0A23kzZEhfezkGKNip8MvoAW6Fq2JWzbF-cpISAbSmLleQJKXXqyz63A3im8oX5D4AfClomKYWxrvRA1rhXnhvEwWl6v8Ah4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQbgqlFt95ceNgEfRki1rnMAOgiA7JJ1ptQtL2liVaiXLoFMpp-r8BElTOLYiATi1aEb2cMhfO4kSkz_84HMX3b4jt5gOon3hfJ2xt-PZByv_MHC0EUUcVkIGA6yJ8-EqrEAF2mb0N8qJ5daIDGM3hyFBcNbcrsgaVZAalbMM1ew9KAMvidZplg8k5ZmjIZqFhs7A1ojYA5N7grsrXfHsnWufjkhIy-gd0aKnWfR6CQl46U1JEZKKhiTYdGic2f_9VPn1Un0qB0aRjRKzLzZ2_-SXW085W_PEdH7Fs-A_UQE47DzKWfl8xK83mVD0MsABSsz0-MoTX9jm740_mLGXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3t6siox3XMR-qM34kDbhF3ntjkpW7YW4JZGCS2v6JiBC4BJQ-lOSvZSC7Fa6LCiiHHq5QN9VNQawRaSBb-7ZZrnBnFJ46JYcTklNYB5qnR9Hm61LOj2NgRJ6fww4CHv_gtapIYKwmCZFTwnOPFVKaCQk8TmsDLfIZWbmh1OZclYdcNxLDKxIx0-JFL7PDRIjBhbV9jSF7vt2p43cgpnC_ygfSL3JzkdrZI1VPlDuIJAH3gm9tz3d3kIpezzsruw1wLnhKcvtIfeE206Jo714PlOV0Pv2BQ8JsZl7Faf2f4GmSQkuke1OdqTt61BssSM52gzikCfX9SGnfEYoeoMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Zhv0F16X9mgpWX4zkZpncw1biA0qsEHMGBvnB4kKlUvpKj3fPUTiY-gvd6s-UiwbXZ946IJCk3Y5kjXMKzPxcn2yKPYjunikNA0IrnvauPe0qYsHve6dlIyDWBE8tWko22t4abcMToqUzCUX632ckyAcPbZWR0i5vJYuRC9eHa8RSGSqRkiwOd-zKs0e7aMHDtS8iS63BCIl8aUWOeVTXqCPx1asymiOtuD5_HrKCx4NrENgHOfWwJE_dP-cPjKlnANshVtiMJZJBEqeek576v4uncZuo4_RnIEnw6YaYvhMB68wZmWMmhZOuDh4xN4BlBsGmBPxQ9Ae7fS6NXqp9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Zhv0F16X9mgpWX4zkZpncw1biA0qsEHMGBvnB4kKlUvpKj3fPUTiY-gvd6s-UiwbXZ946IJCk3Y5kjXMKzPxcn2yKPYjunikNA0IrnvauPe0qYsHve6dlIyDWBE8tWko22t4abcMToqUzCUX632ckyAcPbZWR0i5vJYuRC9eHa8RSGSqRkiwOd-zKs0e7aMHDtS8iS63BCIl8aUWOeVTXqCPx1asymiOtuD5_HrKCx4NrENgHOfWwJE_dP-cPjKlnANshVtiMJZJBEqeek576v4uncZuo4_RnIEnw6YaYvhMB68wZmWMmhZOuDh4xN4BlBsGmBPxQ9Ae7fS6NXqp9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_quCe82WPndSH8TdK7cBl0r3ftPRzcZ6LWgO8FWeJwVB-1-YoEQgCJharbPUEh_PNGGfPIJ6w7ZgNEaC8-NtaQfMRWPi3x9X1BeEApqETmFm6isWqTjBAV4QB4iVipcj3WgYYhdxBWThx0cKO_ilAFyZuL0oS4YIM6B3gXN8lm6mE_crautocIsIDkP-sWkmm9RRZqN8BSehPa75zGfYoe0Q204y90KGe_3S8DepcZw-KhONrzcubnnrHZBAk384SZMrdGFi9HXW19CLqv6oR8La4DzmfjhTHdattcpGagH0omE-ReupdpevqVXGJ4WR15BgifRJA9KTVdRh6f5sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSPfhsDP_G2tVgI7y2XlaH0nHH-0rMPCg7iPVyXdt9V2qpwju20NcUhI8ZtZGT5zTC3AZEIfSmNoLbyLbX9VxKlJ0XN-ZUDyaLJ6lVukVscifSKN79F1EHyWLnQK7UdilwVPAvUY61L_AMlG8TLV4CYQOtTv1S9GG9tQQiQt4x3eCXMPaVGPhkrPRYMaY_mocvGQuPstQlDlKCLl8O_gid5-H9c9us6rCQgrMCYZ5JnAXyF9066ssdgCdmuT1eutj4_bSVsCfZqqyRzNqzVEHynv7kri951CvGQqy2MJ55uN1TnwSUSd9L42DO7qBhANjT1MCPh3ELFRBPvko_oq9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILdHpOwovL5tfqIciPZn1ai0BxKhEDD_ZlimCQhzeMvxwskBZrKekrCbph0a7bJv0xpfyz9C-o0cOp1vDg39cKbdKskHO1UlrvaPHsxWKYh0ZqKWMfKxLl0VSoGGd4g4wQuS8MAqITVrkjCVg-cIV8dSRcmok-B_-8gjDV5zrVIkkv5_vZUJHF-iEnx7WriXBiqKCkhxPEJLa2ZaEH9XhiUYNf8jm8qPz-ZqlW10Kz9bXLMzaTkQBzOXBJWkGyT65sJchdjL0m3pVFnHZM_02hpAAqLsYAWrSb0DQWuAyFUMZ14k5NIMuFrnzbHP_BdNbHoL-4g8iMSNaveDmtBx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YT5PlsRzVpvyADX5Zvhu0JDpjgFo7brkubB99ZQBQcmsuakaAeOja3HEVBMADM4EueMR1lAzGQzja15iK9hClosfoZhPXwCAfYFEdPGumzBu1YD82Y9SRJ1jxTJMVtiuFMcUaiaSC5mwsR6hh33ZPIsI1nZTPJge8Erpz3dr5I1fgMAn5qeEBTy0Cnn_dV_I5Chsmy1R136f5e9Y7NVTWazNiRgM--epdAnVk7ULUu25raHrjTdIEkvlziRebdbk9Lpqzmwm1loP0tJdMeORguyCHEpqaDbh5YDzaL86ZqBrqZ4EPOyG-miyeSOXVFDdJjKB0bl-sk3lzKphw5LOlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-PIvvGHlcB5RzzAfMWfsw43jNCADxEVzD9WQjq88L7axkEjKmM2FB65eL3MVZFbzXlBqSuSOGC8xng6gqv_b9SmY9NadBscEWwxFL5ifxSqyNJcTW2WcVMaMDz0W6PgAGOsEEzo5i3biIYCU8m6rSqGoiSszS6iq3OVZB2Tc-K1xCisn38Tqv9lUu0fddlZ0fu-CsZAMC3HyIettj-2XUwaWmKy1J8tRP_TSmrTuxZKOpuh_dVkIKbwuyUmQu0makwRjX-srDh2FeCHzUVzHtFEWcTV-QkNTUnfxIZtIJ74sytRcJ5f5WCcTsQjn7iP1cQUYt1JURe0u19exmiDcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUShD8ePB6OfSlW2cv_yUL-czYCFt1N_5HMTtvILM01NTB7Ch5A1_1pbY56IO1XEp0OhrA3YBvMfKq8b5Tk-WxSCe1C7i3Bkxy2V3lAa-rha039pbSmHiUWaLSq3oW0miH0ewQbegiFRA33USEtw6uslJiYqhcF5NCqWPO5hmtRdK12iZB4XoQHA7RoW0v-isOhp6m-GbZxCpWm3_0tv1QnMfZo3CrgzQIgCh0Gzt7PW2GDkYHy3h9Ccd0pnv2KS6OmjtFadhfK_4N4YDgNZABSR72sjdZq8V9l0NzkyelPDMur0jIzkFgR1Z2L3d7IQ6oE2oyYiTcisM1Z0W4tOrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qn6QXuzSf0WXsYIKEWDdnBxSnkIlPLpupCL4wpSTZBwiShc_N8EbdRZ4mowwjnYuUO2kGTnaLooKbQEqiQqvF8k8Aj7Lg0d_sJM28I_7SbBGkjbPBnrNPHxxzoDjrcmRun_XPfy-UC3DirRic0KqROQ7MC33nVIbijLfYUUCvWFliAI-6CePt07tnFWa4TP6m1HSfVrFoMbk7o6DviFC0SweOp_rFyIu8mfMq-JC1Iyis3LTRjKnpzwv_QftiJYyTM8po9yTxuTZSSZ5h1Qgid5KVMaDQhgWcQNAI852MrNWSJfN9JnKOWXwy2itaIVmtlehaFMC0VDg35zvKt0kOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwRVpMzaN_i927lMgc0wXp9mR8Wig-FmfZs3jmqT86ftLmyoXoyEi5klYuffQQRKtyeUS_7TRjZp6gePrAFJnPnzTjX4txSWPgpOfRLl2QoEoGMc9WeSQv6K82WwjytPeLWIvOdgVxgRjMgnv6lwu5x729cuVvljDMos9KidA_2rgyommthjRyVsdpd0hGp57lKFD9R4to5w4_I0riNNFqH7-jcvbGHx8RlbQi2GQ7I5puoiDpCqb19Tr1aSoh2U1OchDv98PGgZgZdAfZ8zDhKejfKtv2bulncdPGwLXlwCADHRjCY6aeIk6GS_vgm6HuO5HmXzqM8K1aP8OkIE2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR29onYrwnzPWtZVdYUvbgAZcyMOvDx8OTCNj702zVDGJTh9O467bsPYX0VhM4yuTX6r9PlKX793r0EgM2wUDP2CmrN4qJODhp0l1DVb7y4wAjVoQ8Tzn0yt6AGQaQQcakZCmdvGp6bslxX3fzjUojejKJijp4OQbSCsxM9jbSe5KNc10YY2kvH6hRxImdIl7A3scabLxgI7coC-WdtwHABbSWJjJVxCmuatQGl2jQCaUIjNGzik-vD5Sly3krUh_vd57OAqW6nOrhx9q4Zi9ik9GYkPdP2Wzo9F7gh0dkvazjnMret5h3HvD9sZAxbg6-dpmc50MdAO8X_l2WjVwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eImqc8pys189vTxsVeNqY_0TphA54AUqbaddtVLyIF1zBsNyeFLsay-Lxf34G5LgAlIyc7_88vWmWL404OmZL8ZCPUz53CjhTXetHQD9Q5g0_K5nLTFFDEQPsxRHTz304YFwa_Cq9jwn1KMH8q4fCqbzbtEodUQdPULbsXvbAt48OkVmlyYpP7FkEhFnnzFXepl_o8_mFMIRzSrIMk5prKDC5QsTiSGcSnG5_oYbBTQgtDzfIz1up9rva14K8V2bGNb6Uz7sP4L_-roPsapn7_Zmba6Szot6lCzjXrzzyd0Pv_YuP8Q1xRfPJk84McjGMhbkfTXWCcq7laJjzBA2jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo4A0PQhraH_RIZDjtevLXar9UIfRxa8evqLmV3xh0CHnbFdiUHaprECD2zxog1C_fjCJdnDFtslfjFC_cJEhyzXr7UpKjpdo7I_J59ntcuhtlKHJCmswsHZVcoG-we5mgKkvnrhOGTDW1t5_kJO5tZ5G4TkfQ9kAFhiqHodgFqzuK4lrThItZGG3xAGR-o52QymMiYkB4DssDNC4FqUsrW79yXUbCvR6UsPdjJsRg4umuoHUAGY0gxZNUjAfrnbZhEiLjSAqkp7Loe2JMmaeTXpnfuR8V8jBwUZ0CwMJaWUdo2C8MfQudWbN8-fPKNDFgf9Oipo1Qmd1Oj1ufxJQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sya3XCokrTlKGhZsRUpomdVlXXVcqpIFM8AiSIjGQeuGhq4wSCLMZJl6LmaqXgZkaCIyO1VrR1YiDhkgQw9NnNDNuBKjiiqxt3zIeNlV4bJD6m7xXuw2sNIk7uDdKU9X2Dm4AFrbX6ZivHmFd2WlJRuurFpxBQrNH__S96W_SoeL58caQajM-L8TdO6HArzJeA7ss3Vwc9Se9GZrrAoqSV-yV9ulrMVqMYQdxHP6o4rJOYPoWE3tZ_7P7ssIJj1FstsSacDJbtTCa_n-bQ44FIltmJ8ZLMIlXV8sacu4yL4E6GXtbPY930DtEvNR7jyInYzvaBuruGeVV0POOEklGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKZcMewZNFYVb2S6UOh9AQjrc05eN8WWPqGAsP6_LmESNBEKn4HLRB0j0kXtGZy_Ls2XbepRzJnhdGvRpXS16u8X4ctORsVNnZBHER5EhZ5ntr364s9PZ7_DKjfp3qtYm1Ec-EneS-qI4Nhu8aCML29KWZRh7US52sIc4QP9_w6kD5PYJlBvGD6L2Djl4uwBla1iCn25D-ky-wYDyjl6mrnAkgcoHAa0tSpVOOsQhroy0gs-1ovOS1Z2TQ16mpdyy_eJyXpGLSJxio9pAaWgYHf_YJ6qSdf7GyzWB6cEozoBWOqmw2kXME0llWxNZ97nfeAvPmtyAqlDWh0IoHUzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1FU9aFw1NN2VRnTgoXM72KpYGZg6Gw0U-pphRP9hPA3jkz4ycsL0P9kli_0r1WCFYv3ysThzPLR63YDNEkarwD2arUw93E9i-JWOtKZP3c5e1JlFBvPZCj3OkWRrLuQ1jHuwML1GIXEwh3JTJTeahFivikso4hgZ4VOx0XdFmAJUy3YqEJEAqfuPLotwgAhmQJcT9wHHnSQGACwzhB2CYLvpz6Yq9Jv8sfR2ItIdESfNF7VUH1soChsfvkChVswLi6J7G1qyu9Ha2F6f33EV3khQtvOfswicmzbTil5FobWwE-gBIyVCnALxR2R6XFMNH8--uE4Avb5Tpc2zGzNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFE6j6joNMrIGGY2V-XfYO9vlcYprHN3uNOOP_U2IsbOAVYWa71mR_Y7KBeRk0AHBRZuxn5h6PD_fWuPVbTnWaSmAwuRSOSJG6p1W7Ye93enfRgFLj0nyCMLbLZr82vmqGoB9vAMpVI6LNLMjCG17qByD9azH-XidF2ya1SJsaVCqap_fZO-c2seSRbZPJMKmpFJhJIPuUbNrSHMgtp-GDGM76L-2nH1F32QupjzBVh48DclLxOXNlNLymvF4T-rSt2b8LMEnn2smrM8WczqC8Th_K0UgTQR9QHgyRTeAgkZhLYjlJuNLla3n4aB2PcvO_asokTglSwV9oMONIa9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPErIBTIOBcI9awm_YYcg5iZjx4K1pteoCO4paFn-tGIMwvq55ya2O6ZEVvoXV44gMwkKAZ0gAZ42k6S-_Af19ZAfTQrnqkzVKtfjb5iq_tVY6u9KpI22znnc381LzYo1rYgK0qxoUp8miqR5nUs591Ixu8hrFaSDDDny8WcFLyTR85Q6x74ZTJcbAGxxZrKFk3w8_Zmppv3WV-FPhiYsRzV028fDelO2kcJB6J4ul5wWDq0luZ1V3h-8ZlzGew9CM8bnuLnS7jjNU8i9J4vh1-ADhDhj2k1UmFyWlPoqcZ3oA2aFQKWh8kmqc_BhO7bkklALOAl8AVqDzzdwh55kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5dHRjOWjxQVkx_dz_VTX6TPo8puOuvXj4X9eDOx93msS0PTT_KuzkHNOYeV_Pbrrta5Ksfd97Y1_J8U3cPqdmsk6HwkSP5BdAQ-f1ytu5H1jlJxsuTN2K5xbiZUqNUBLx4Q5_ix-kSvz2oXcPY_dfCMkCZXk7sO1W8bA829AAitLdAzHdAbmxHg_LHJX4zCy_PMp_GXioN8f5fe0K0HOqXuj6DNpbLBTMqJXWr9jlVd0gnocSxdcGM9brgSXwvT-l_K8MbC8sz-5jF6adw7rWZnrzAxifdd-V5p9MDgIgOdKd1WWb3P6Lc9FikGtrGNZRMiBJWYrjL2RFYPQCxD_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0LM8khGFWWgsgvWrHn6RI_5JVz9qiiEyAojVxDZFS_SgIXVreMmfxy1bAIPkX99xdzIBtQtU0xURQx84vzlRsVkOcAxwNgjnxyL0BIxD3yBq8vQ-qzm8XJg-UTbGYnpPIhXqfaSnNC1sGzQfpX49XhYADKEKqLQwYP_CS5Q73TqYNhPMWXV5kQRj62C2c7JbBrVLHfYPkAncaEq3ShGJ9vJ8bAXTjSp808yI7rwJtEK6OGAFICT7ne_oDc2On5Y8_CHU9g1pVFDf7iruUl4qUsZiDTWeY2m51jD3rmu68zPY2z0gE6bM799mEaSVPS24vX7Oz4ctf0mSb3tG_bJ-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuFxCBiw0oFtYphSLg66Lp3uy8WT20fTxP5h5_d3XqyRfCWXNOSxtglca-8Qe1aD0wYhnz2hJQHz2R4Hx8OrDQlXfGOE7OIY-ffxNpbY1F0HBlw7nw3vkzpNihQo65S_F4WJfZXd9ngm4upOiGNLjYLrgsS-NicvUVs7-Dm-PTiJibKAFvqzHrtJCmRIzDgvy_P50ezZNHJ7bLTVjHwelXNg_C01rbjJ5NwZ7Vh2KqXnerYwJjFh2rgVFlNXvy0gDYlvPzy_yyykZ51ZkwpBE-WVWhjBJK95Rm9DdoQS8kzpTHW3WBMVe9L4DbUKuJ2Wpj8-C8aenw_lk4uRWkSNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNMFy22f2Qfs-hrLbf-UpBBtRyIcXV-I7YDAfKvHyzY-TWtCwIknXT_oWmYIacr4M5a1JUtK5qoedd1YZCYQan1JNdtxICZQPMxDiMCxL_pev33Sgn5YbPSfS6rLRHNZwpGAOz9xzTzzlbL-XHENvragweWc1hUcd-3sBxlhDFPjcr2vohH9QVHYN90EXhtgFttd3XAKyX5bVleg0OtyeymAusLQ-GgxS75WTdo_IVr3kanCTDY9DYtV-18AB3bOALU7LMyGGdNkYPEJQeHZF9H_3xRijKJztsbjxa4kOY48NWyjbhguXL0SaLWnf-FEGgg-Rk9PPqk8JN8ktj7MGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8uVt0mjHL-fgOA9Digzl8Zrc9AgBe6JpBJfSddFkoTLy9vbnHQyIUr-GJkfv17AkzdQ2NdGCLV6NZmMHyZMDlHCU9oGupTdwnComDRg2LViRhS69HH6vIc-ds8I2uS5zb4LcQT1YralHc0RMoncsAhB7lyaXY4Vv3D0njXqwjyd4lTo82RSg1AgfybI7r57Ftg9m5jHiLAOzZBO0xyXsuL7tWtFi0xuJVkmMEolUr1Yj5Lh4PWUjugJpMvbTseHuRB7zOWNCvUU6YpQiL5mkWdoatlmUxBTqjKnFr_roOhkeTrXM9ndqVVFcJwVHQU-g33maDuweZRX-EjihcuT-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNUF9oC6o1E4HeVCIUyvZjO__aPuAtvmAn3vGOApMUQjHMvPT6SnY1yXxEC7eIoA4qLL6TAocVJFqwEUSmfZOo4CTJdYg1NfqqzH9Vxk80pyKHprMMgqoCSDwbejISZHsJOs0UkaevRpMgvVWf7V_FV76-WXxf49oucYjtRu1OChFl-T4jAlseH14abITHysXN_bMxUpsP9pk2McBrfMD-_JG0KIhJQSOkG6bLyc_OGxf6eVO_vF6Yhl6uAuVgeehYt5azrqsyVetYPX78HWsXHjEJmR5AhbOQKI-z5eChhT5ZmC-f_M4Md3xVsGubHZCIo7si_KpD9x97-rsPGU-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuHoHNSdeRpBK08uHhXb7xpuziqjrL3hiRZwtcXZRizurYn62GxLA-aMemnjEGvZQgC4mGP0pYS96_GGQ-fYcsrUM1jn8i19LYaNomOutAyfVqo924WNf5rihwfKuyqXZiwJDaCYYdSnxJsiz09-lomo6vwCe6ZceccpkZ1Hrdnty-CmQVl7pj1XudfE428gTFcOv-w7BylzJ2A_kwlRiyrrUXKSoEkLa-UWaejom53AwuOUKi1EzuppVRQuLMxZ-I-r0z5rjkNw5uHoAVY8E-M4-TJSOPP3GF5I1vRxgQ5DjaWFo5nWyHlGkjY5YGfJzGwNN_kO7AZG-LhIYOCQUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 606 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PncYSmkHdmXSP-1RrTbWi2jg4LEIM6buLXk423ssv28i7wilKl_TVE5kDRLM8QjAPMm6n25OYFyqbGloXORoZYW8Iogl9YVccsMLT8bOzc-ouhJtxAJBiAhorjtMIIbO5VDKq-VRMEHokmabCIZZWKI3fT_zfCSDw_X8nsWsBhwX97f7h3zusYac5fZUdpReAH4jsBfYzhOaxQaEyX8iPqFhihjQWC6qDKhud8GR2Jk8tDUBednBBgtP_kkqm2eKp_kWu8ifJzcSCqfiaoxnah1pQ9D2YgVCaDM6bv4ExYpqYh-U9hQN5G7APpzNUfB1z8FWKwWWysS6ppP2CTGiow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYQ4No7eD4ObeDVUzioI98a6WmoEIMbuCd-WD8kkkYUZGr9nGtANkWCCvaIaTWNHWlv_cXYmwkgNqG1kmrqXpgqmHPvJIYqUTLJDGKCxHyqmRCE-OxUJ4aSowDYpOCN00NGYZ2Y9CbrZu_yebjhhS_p9qJ43eIAbfB9qNcby-MV8_b2u6uwE3neyRnX6j_iP2NcHkF-3avvedokPALUSwMVi2pk5cRgrXxTrlpMsYy-ni4ooumla4b_MVw3fjYulTc2mcoXA5sAL5Qv6TtVuLRB7U1xy6zRPDFPmWvhFEqRuQ75pNLvNMDD_YS7uNOeHWfYn3kcczFadBG9ml2o0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpRRgMDGON_afoeAM5Mp349DeyWeACbvbgMSTwU9LLZUC0AGsKAWB89Zpit3zUWg9xYzeqNDhiV11j0XGyDtT8FQMtTXKEWUKEcBToJm5UH5zbSLfpSJHQmRVNVau6JbRyJndFDH2msTZAN8ceA410Xu8gH3J4KHaCKU_kWygrByR4uNurdj3dTZPFa1EZxRffCza17O4X917xzgwdU8RZAl_F1AnsW-T3UAyfExWYUuvaUIx5igjW_BVnoNBV5GZ7ZcoCXiH_MTKKiP4OQKWMqz_Ai6d7bBV16WBkhiU9CFfwi5FO1Ro1M9eTrySQtYLA7BKer_MZxZaDC5k8IfqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmb6ZCWYrGtLnzxZh24D1bE-UaWTXzWe-RgN5X4NN74Ty0xhSRQkV9yqQTBBmxNvOw3Uet1dmClpM32cscgczPbICqHqCPtwM-p-WKapX5iRF8bgQuC5Z1MLf4Aj4MKeh6WaEdnBeTT3qYZSo76bk08h-uyzQElzaYIc79RmRI8DN-sGvIwKnb26RFEcHiG8ohD9BC-HWmnmK6WTQ49sxB-ZRPyXQT4nLGywGxROHhjGu5wZ32YXiol3YQBrqRaX6d2YJTrF5ma7m2XQ5OwEoB-NIMexww_UhRq7pS7laStg1kJIVCS6sW70do2U9MCAzUDp_X2Mw3ncgNiCfQ6f0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTG4ov-JIK0bbHAewCNJ1Oi_D6L0f0-MjcBZA9kyOqAzd203D3WH_imeefadTrI3td7gl_nqZB7lXm5PkY6vzZTsorqUE2UGRdIcP_P6IhDxCTWVtsVdDoOZQfCVBwwkyW4xgDYGLYgwRbBPkSsh3HWOnVIT6zSdThtGnjdreCGwRrg6vnU14hK01qwYtUA5hmas4VvhLNenKnmuuwlAAzE90URO87Q4jBgeqDl31sYtxbJDWCtRhnWyQUv8I4PZozTz4lvfvBy_ou-8vjjcOmFR1cIn1bQXGx6DB-lWZDbYemYHgSlXvGcVPtzaOFTLv9UnGxLvjkzEmIfAyTRvKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 541 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOHq-lZO1pP8kvkiR-Jvp-JAdfL2AJutTaSn4OYFGrP-Z-_4vtUU3MJOtmCBcCa78fBOSoJ9YGZFH133w_1Dh_dsI0gVPXlB2OJ-AdtrhcafFgr5-1XSCOod0H5m7Hj54GZQjw_OYG9xPya58uDRJf7Ukz0WwxecoO00SpxEaPhwAaAmlu7OfadlezBZcscuY8V-qUvMR_8ZuCrJPcG7Q2Vp51Gk0TYVYcNIPvM32BS2cbgrQaL1KRs6C9d9iwk-6n-1NxDrE3KWDNYVW8RGkBd_9Vo8V3QNlvJ8MXlZibA0G6MKVDBbhXsnfgRoBoB1HY6egoGn8avQilThMk9s3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkz811LhDUGv74WMZ0EiYl3pxkfWHCMUQovgcAulI_lIzP-QMsT8WFGhj2MYEtw486tD3a-KSUk3RXA2q7EG3PDF-MEPM6QgNkzgHRf3gCJqRalkVVvi_IDXg9k8MEyFuzP0biJ6P4gQKvbwj9ak8EvuKKmIsIFu_6gLRxVq4moRRQ7Zn_6RzTmRh_fCWj1x3Ft7mPsOpnZor5dfGo5UyYJU_DeC9pnBPHp6CWuCe59CzjRr-u_YG2er31p8VytuLbtou9sQnd42sRqoa-UtJo1tYBeeHQwfg_lJ-HQO70iNKEh_httMfVWJrlM_imyirflkNW6SEqzhzFJusEZpgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgZqcjXf5CPN4SHdjyObBtvodgW-m6r4yhyZPUplNFM6X99DvXsN1JlQ9u-HNwD3bTFiUGMzATe5ivKxHAS3ZfHOdFujP9zLKrVFjOIBKb3aApD6pVfO9ZEf-LtetHBmI504iXQUNZio31WMPynPVFVvLhqk1kQAQJSOvoNgV-G7jUqouybX57tmiBNH6GKyXynJnAVKSp4b2rRihkjRkRzA2b_2YzslTdZCOz3uyK2lvGHoJ7ua26CRM-yWpMVUw2OeAcMXmyZ0v2Qkb1E55vdHKWvlr02K8XvEMLWR4ztbRzoTBqozrldoXJNB-060TvsDJlYjUXF_E1HIaG_2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMYmtSKsfpz4_S_7ez-2g6ueBry_ECw_Wv2grcB31f-P04y6FQQcSw21Gz7VuZ_-32g4f76enIR4K97Of9zFbPKMlsyyXCLJXLaO1T2I2-PsFuV9HJDo0xPoiVXZbrfXhsmziwMZF5JPyI6zbLFP0Irei9VR8KDrUqUajjI90PxG791J3fQtXq28U97A1iVuC0rpCeqK7vpbaQNWCCpjPYfqTX3eLrG00ymv87HQoU-YRVDlyKJ5vsopW-2cQlPBqua4c3LPrNk_8A22tXT43pw9jFzwWre2-1WNVDlzYdUrfHOIVktTcbOtVhz_hl0-podG9NlS2cYFSy0rDJXFfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEbbVMoi3qCNMPJA88oQT_-A6fTg-X5Bn6Jf-Tlvk9gkFwbzAzRRCdD7OXFRc0hOH0XrhDIJUU0nDxbBjriJvzr179fbPoSh-WDj_MehGocU8jdTdVO5WFOaovWJGTw1hrrgIurwA9C7tazA6lQe_6cY3S4mahw03Bp2adNu-Fefz0CndZx8rmXBBIUwSzdRBYK0luMg2J3Iq-sfgy45UaZ9YvZOolyMyKGSRiMbAjSZHaDQbm6CiZonw1_Hy_hSiQ-QfVycMqLYWpe79gjJXsnw2-YVEUZWXhMbYmT5m2D8lkSjf2ysivIf12q3fOfCLY6mxq-UrPIp0-Pw7ObzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ7yRhv_f6mfhqu-LhaRJyubtw0wpGWsSyfF7x3cqP9_ZsCCYDaFTske25AuyoT8TFonIgM3LY1nR9fY3aKx_CXxRnRwLDDHi-E1TIwjfqqHR7hnLCZ6O9Bu67BGwRa0W4k_cJpHLSUCnggATN0qBHpN8QQXmidXNu8zB3f0NQ6TqrKaRCo9YNHwWdQVBiqyn_QQ1V_Eq6RDnmcB1G5GLky_Kl49xqm4RqZtEXOybFT9MEEJp7tjJNcmAyasrYd3o0FwCT4ncE45KIU9LqrEfyXNhS7ImgflaGLOMpiriSumaSyTTXcTVmYK5eeZQ3iTZ5JdMAMpK2QRBJDDX2_PVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plxxFKAlObeqqth3d59KMk4GCdSNVIxRzIYs-GeWqG0St3mvU56WF76h71bAiEzEJI5Fri9mS4MGwkhvC_bKW1VpjmcCKINSFv5GsOUHS_vwdaF26Wzr0ljEmuyUFmEGGWqpUY96zJEC3GJE3CUMQtW-MFDmreUI2BayIxzGJDlQNEv0kDvWZ4hopHaacymzadzFajtvoXhsF1N91gYKjb3h7nmNk89BWBzNH0kkpBKH8IubCmAZ4ukaldQ_DnTdb6HOBb4EKA5xa-CIjXnBxMJPqnUSZzHQEbga-hzrDut2KL41TInZwkFgi9lo2BBQN-4DXuD7ZPLblJ67UQ1f0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tN3C8rhuHCmLd0uFgyJspAnZE_EzBS93EFncFkAR_wXBUeijke_udzEMqGqFdystc-4GvNU9Z5Vw6HyJB2Gkq0IRGgSnN-eB-_gdY3EqA6Wbbnhq0PT1CUGCi6jyUUG93SPK7z2hECu56mQftZpW2eugxKkD49zm75z_T0hGl1O1qgCqQNEzpeCAdzW-bzE2EVBqEDZs8kSRh2x3JEP6o7bCbMXxZREgPmcg4ZuOC51EiSHZXyhyOwZXvxaZfn94swYJzynzTSLyoWxO_XIpA9oMqDGZJRSkkSyBQGlgutRM2UYxdliRwks0Nscrzvt78sZPJLY8Z8nSsL_7bG9ZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRA_ypuL_PHl_lvSzaAZKdpDsucQgyb66l0IOzvgD416C1sFI9x-2AE6KozGb3tEqu03mcROGBfjWzot0wgBF0xhxjrMHnbZdHcIUwed1BvIG34CeR2SPzYYOJtDEb3UgQmTGs-_DTakMNNH0rwTo9ey9FOOPywvwzIqqr2T56FSZyzVMlh7Yf6niGD2RmDYyHLJYuTVraIazbFmdT6sjrebHanjIY26jZ641i4dULt2juFVEfWMYKpOX7w_zFDKLGtdxgT8K3iefKRffEkr7meQ5AKRTnFXKgdKMYjMmCQ368m_KPrOEs9gOxdbs_iDKwAsUTrzYcJ3ZnmvkpGceA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5GQ9SXt9OVROtcdXKFLjY5R7m7aLWvZH4oYKyxw5qaZTzwIrQAiH4C3L-ulrF4uR5zJ8rhTfHw0n8RQWROpk6rExbpjanxfeglPcAn5zER0scy9Lo6LKGpc0OjbPXJlGuPn2AVTni5Juef0VK31hA6Xo4MCnQbQsqfBEP13zSY3pwopVfGJfUmb2CD6yNMZBmuIMNLBWk_KBdoEsRzUhU7mL-7nSUqaf1g9iartOJ2ZjW8sKFTONATXTgfjMPmkR9ERKq9tA8JVdHmuMHDcmZ5-hQYCT5Fu44aHEPZpsnNbbGCZArU9nSAOBstkHE1Kgyj2VLEbBEX3sD38L7lkBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsVj38e49jfOpYslbWjWq7JbZJQUt_xIst3AiVrknMno4KV8xgHoGlY8iyC4TuCxIuQZu4P4jvMP12m0h-ejgg7n4ndS8xDdJOjHeicNXVn9VPuusuzwm85hilJp6rscehbBWyQPy8DTKVvHCu5nqGFHAV0htJv02WvQ9Ef7Q-RE-lj7tMCIRRdM-3fxVQTG1MjCkWwnlWnqmQvCYkbAyxcNlUfDjcZPkc1ChSz5cBIvhVkCDZGSDN30ZKIB_WpAr6KAU5GgRL4iJ_pEBWO1t9MdwbmHfDCuv-bFcho_Oeaqw4X0tpDl4QiOgvkWXsKR3gwpTVhkcwzv2pUnIKmqRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1pxkqPAKGAQ0o2zdUJfmK45TPyxDIXGOdD9q7V0mQ5FiiWpjRJ-_KXEmYNECNWnm6uG1I3VMb8jkRGE2lNrRa7XY0QqDnBZupsITHnH8QhMGJNtazcEftSJEpVCiQdWZY4DGGPtFYe8b4cYGwVXawqMh8L3uZ1F4QKmyE-ECwjOsD2nwwx3GTSKboAXAOxNW9p-4JnlrYFJZy0P5kVDTgJnc4HocMdyW-GMRx_RrhcFSY4Si1TXBac1U2DP9UBFYtzV8SDtemdJXqI6VgG4NOOnDE7EyeaI6JyieVp_wjUdGmBLdz4WYoY0ZhMcyOM-HN0fw1Xqs283UZtbiq0H5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 768 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMBdL2D-T3red62ISqaMROho-5kebY6vNmP76YFZNPpsKFWFLMGoX_WQ2HU2PX-yZPGNQOhLFLYNnEKjEHfd4IbuIt9_gIUPwHSpFXw5IyhbBACOtj1PjATArSW-gIl96ZdJlDYLcCD1MXaFofZL8BB4_qkXwX0VymjJsFPgNmsaKENze0ZQBFJ8RPnKLO3mT-Nvpwo1FRDeQxznK3SfkgkUkZerSsvm1FmBKAputOo9bjZ_KmPMlO9CmMZLYdoSzuynxnFqpOoIhkmWJDGZNtZ0opvuHvwpk9Hx4J3Z-BW1e09QS0LF_YHJpvm34FlWi35NzVTFwA_M-6lkZNIqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSseeO8Lm21fvMk9wcoYk6p-vGtKcOat-R7_tLfYD95IM0Q4VBBL2zkiBv3VGdJyvHdA7tLD1cp7hxMCiqAD0otpBxpjrYdWL8q2b8bLJK7hqA7IUPkizcl_sGQzw9Y3mzqrSmt3Qg6iIv1w579xpeybJXwf9vsOkXkHayZdf-98NAbq2SLVhxwShObsU46DTbFgKJHlZ3TZwD3xIHLWnEK1W1ffTlIYWQEY9_caZHABV8lb-kUhAo9WYcFlpdWqFc_RpUpimtpTxMdUxeOoaYb0hFj4WKOfV8yyauOZdWidBGbAczbx9uziBy5NUCLJfxTWHRT6agiTZnQblG7vJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0xEPSdMs3U1GTKRembfdl5M5HQZctNN6_Uj25bQwjr8MnVBuHFovS7kHpsjW9Ol42thCkQmaqPajJZkTqOaZvbS_MhXxBc_PjoO1EocHXuKr7QVZUVCwtHbhdzA83nBIOmGZr80iR1kKdMQ7XD_JBJXnu3dupHhg6vD3ynDDZVpIza8z0_j-E96RtSA4qB3s6yiQolAqpsCcDtLC-hEw1yOtKVphWGK_IveA8p69XnGCuqMsg2Zxifh-YigS2KFtbyDgstVjiHtuK25ajruAsWfW8kxN4AMega8_xN2FnpshbLaen2Q2gOCUNzYKcvjvilOmVabr8MTL1miEQjpbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 620 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drIgqUkyfMDyiWVAXeD4vhX3BvrzkeB6aO5PNrk3RTOD6pLklpKN7V6z22WwAnag1IhGnoJuz5jEavZTd7V3RmL_-A4dFiiKpvdD8MqHCE1m2hZp5e7be9z9ENXOLlYk3rOgQ298NHfNAWPmrD9yVQgkY9qnugqGEV49qfj6ANTJT-W38Pfg2Ke-O49oKNyoh0IBQANbbtONrEVs5bvcydYmQJSB70IiXBWM6zP5slfnREeCV5mdqf_s6TdPY1ZwNSHh19jN15euwuFVJWh2t0bmXyV3dArRdSRRkNyphgZbRBSnXxxDRaN_ncYmJK_PSH8PqrHMCGnxUtI31x6YMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8neIBFveo-AJJc1eJXl_0Nny8uZNJbhFXM9qNb1p3bJ0Ur3VS8zvlBhwuSivGV0GDsTuL1nefP6MBqI-FGrWWrzDIJgdWoGBiG5XtDIIEVcbOcR8X5HhcXblm2MHqbG-MlXCYO7-W77CLjSMcq2_s8pIgQUUQtw_twOIdiNhykyR10Do3DYDD-CKd86gVd2YXbrk5buhBObnvFeXA_82D9IGoVGY9OeKo7Mw80gIK3gATdj9gG2wlIN67Ylu3qivhJ_cKcNSnoraCsWLgd5CxWfbuVYh0IX3iJdYu7ulgm1LWp3suMERNj2ZxZo01bQC1hxMFs9sXeRY8HtIeZ0IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFsEb6GjVm44woZT0y6w89sA7hiXo5Rpt2BGULS_9B-PBfTsverBQDKVP-OYoT1V1-uF99yZWN-TLWQ5I8XdmFs-Y3WW1GtxaGI4bZ_EWUtbxuCktR6pzOBrUGnXNBf04SkjGQjJLr0WDRrbz14s2L8vOmlRxy6V2c_wFR_AQcBMxIN7nv_JfpyxehNMMHYQtxbTr8K-vaULf5gPpg9J27YOq0LCtsxsmRXnKfP95HjpvrW_kJa4X42U7lNLFSVcaB2K-FmlVWaS2vQb5M73DEdpt5E1XSd7-G8NycPrfkeBZrGat9A5hBksI1_8U-7XtOHrEQhiuRBkBW5FpVGYsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qxEwG71mWLB6NUMDIv78Kgo1GkZtA47MdN_ZwYAm-n9FVe55ymG19wDPHtNBrB7EVfcmsJ0b8jzJy17eC-ThsJNcnKCHV4iRDkdmJJi5LyOhMfcBcM-cATD6sRTlxzpdjTEnWCkEoud54TA_pED7EYwVeL6nAVsCK1JeG47sUJ-96YQM_WxbeNwKE_c3pCXg2QRvHM6UB_Z9GWCn0OE7V4rmk9Gw-OXb6FT70BnuV5Xv_eJeikc0ZDNxVh2-VjQZpaayeWeN7VJCFuaou1xVDybZfNGx8ZGkhhCnyS9FjjE8o32Jj9WuMxPMwwe1BFBHRWHv4IzRVxMCVESPTbq_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qxEwG71mWLB6NUMDIv78Kgo1GkZtA47MdN_ZwYAm-n9FVe55ymG19wDPHtNBrB7EVfcmsJ0b8jzJy17eC-ThsJNcnKCHV4iRDkdmJJi5LyOhMfcBcM-cATD6sRTlxzpdjTEnWCkEoud54TA_pED7EYwVeL6nAVsCK1JeG47sUJ-96YQM_WxbeNwKE_c3pCXg2QRvHM6UB_Z9GWCn0OE7V4rmk9Gw-OXb6FT70BnuV5Xv_eJeikc0ZDNxVh2-VjQZpaayeWeN7VJCFuaou1xVDybZfNGx8ZGkhhCnyS9FjjE8o32Jj9WuMxPMwwe1BFBHRWHv4IzRVxMCVESPTbq_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZitgnTceXAKH-63iz3c0GMJCPJq54C6mokhJI_QFgzGW8LLYoWL04DoWQHw_Ru8NBvyphj3J1DFWgIiJiA8lGIA23R-quXk8SSjqmAShrXVc-vED66VhMi3BWFB7v-iwi1TRQWlQEvPwpzgHjOrE85uy56qYrKpqXLF_J-mqEcyBYAtv4LODwbyvALC4dB5E0ZmObmtzDl5b993NGLZo9QMnKuElFNbW5J4P7qTv4034N7jaD-5-6ZaaGTrwMxMlCY62msJixHGup45k0RqLEBomMhLtgsdGinr-U4gc5kXhIaZtz0n7nPDuA8bKwTbQc9DmtLzEt-Zr0V3GluGk0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl6KUgUoWJzs5Cn2ySadb5V7JF2Pfbozrjh19ko--qbKev1JIhgtuJleBH76yHx0nealqHhcQBH955GiyCdmmuX6b1fJKgZNUqN3dqpw6pj195l3klRZ1JLPqWXJgxYgIysZ8zXvtNB44ppu4vkS298NqiOq2V9vsqgmXboiYkvjecncDLYUxmqvsD2Jn9d8zQDx59ZlLq7WaPe5NyQ4wRaYhAAWjFOMq_84RZJk-S-eJWtqTRiIXhd-KjOD2zTF5j5hjZJZ7Av3WMir-BY6jHdPtdVMzeBuiaYoZU9GvxzsmoN9yy_58nxhrucdlOoGCvVwjaO00SUiBAXjGd1Q7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FccRAsac1HtpxdkXxUdoD7cQyKaNTggRDGQ8PxpLix8LbHhkmXa-J8GKR1jxCMs-bLQhS3wEDmHsCi0Y2SHt7yt9kdasrcCzUuLy7ICp7-FYocLmqLhqnHc2kmQELfl8DnJLglPYgQh5hHmSKC8v5_3HU6LwYRmGH6HSq2vNVgwKctbljqJFffVklEgxlbwu38cNO4ZqlCrdOZ0zJkFZlPW4u86v1oNTZt2VtsInEVfRdL0bMbYHebN-nqF8i5uUO08_myMIzUIm8yZc7B9WCDytV8uvURhj7M9RIyw8QQTtsEkaYj_LjTLZD6gLehrT452LMrKsHtRBl0_r_8ZD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQ6U8Ar4lB1LYeL-hqK2ODOrUtoK_5J5lGiD6o-IJcOUOUQCuwm7P9MwG5g8bOru8yPvejF7r55P4b_3ObKdtifctENAXUjBgYfL71UALAZaYV8x2kPDNRpp0jDy4LUFm0VR842jrbQCn7aVF6YqJGeeqdOwiCiX7d40-mfZG_05iH9Kic7-MlbtAh4KpG4Q9l-sTDu31usCYtMZeFSDVNsyIdLlY24niMWcBHN8wKxawKrjoqHkMT19_LKtFyU5v6JU2EPUsJE_cCZY4rdgjio5egvyrih_LUy9WVUYNQuarrocTTckavV4tXj-CFZwPf1WTCQU0ZHi_RC91IRMdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSheFZe5bYfYB0HtZN00Bnh9Y00Z6L2_U4V0IaKoSQ6xP8zXNZfuFG8BoYco-0vxPJ-tdwEErBdunyWYSs_6obWV6VVIQ6IqqLJpNgKes83IL_4_AGqxoYChfksXsbzDvxZqydTtv6nRZdMMtlbFDtM56EFd2q8_xJjzIITAiK5DPppCkhXGXvDlcIplECz30T0yREJn2WPuzP432m-C8rozSTLdh2T6AkFf8Hzo7PuLVcb28W7dNcMWMVhV6DoV6wHfKZc3wVnPSuh-_VXunuXNsV6EGtcwdwlCNCIXOy8hpANVE2sFXGfHcSBIYqy8wHu-MmK75wP5vH50meDwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5Gqf1iBUkYWRzmMZM3yLpUvyz2Pibf0fVQ1b5mm_xSU75qbsCpEd3E3cZVaO-aXySnIgd2KN36LnONsNaCWszFOzyo25I6inOMeLindrOq9Rt3g0b7BZaBW4mGpbFJXO0Ro5eVN4NvT0NRhzDlPoOG5eUsb1Q-M9esKQLv0jYwvipqBu0-Ee-6XxaYeu8vqFBrYqSbVsUV5w0v8eA6ma81MwFTtKnLfeE35u3KzE99dU3zKezQVDTAS9tyPwAOBkMrVk8RDCmWDWpqlfKyj2twhWYNIjAZLwBzanCqLqZy2PUKpF-QUxMkJ_ElVR9YqzN2Id-QEez0cZwI4hD1BSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqP7YNsrUHJ7fZm87SQLzPa3RkVBGa5XkG2Uh4wS71Bq_LPMiCfwVHyQW_1bWYDkRtzCUM7BioE8TvQu58k61U79Ue4vvQ-5r1H4WrO-CTzEo4aoYhTH17btn1rmQHgrKZbJxZUgr1Nh67tL63BCkrtVMpYWhz1HrrFpxghr61Iuy6cIcQ-HDzLwI1mUPORBPwLMCZfkamz8wbscKHPY4MJLA9UKtItpswD5BqDBAhdcwx7sCEy16fc_MoFpOLiE1e69RYBxlsUB7RicQ4HZJbLu0gHNwRO_gAYByp3Xm3jPp2uPUlb9eMvYaGl0wCjx0KVUgS9fDeP68AkH8QIyXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=PtkhoQNKA7RHgzLrywLloz1ZRrOBbAkvUoN3TPi3ENGObb-0E8fFttbA_DKxltCzPdEYB15vPl1kjGBupOwjrTUxIwCxQ4pHqLE5OCrt-B-QYDNp83ceVbOnKyD9RXVi33oxeK4uh2gYeaG7AvhZB0w1X9Tq6ZKNJTX5H-oW4EKEmhRQ_ge7lToOZ-etbQmYbW0SctFMha7qHk7MR-YgqFX_jCmPxbl6yGuORsJeCJB5_T96eVItw_qmrVObWzSBOtCg3ewOc9BajVvtUc9EJ3CxNB5mGhjTDi_ZzCC7s9ONClZnThmUa_tMkdtotZDByRl8uyzo8UTO-xxd4o1b21yqxrIHJIIcabKtUWKB7KzViosga3R3fFsO9QTp0kjmxrqyHYQ8WjEy94jLXaaoBu7bw2TeGHD0rNJEc-bLanlfuqPrtS_gNPoNJDc57anCDAnGNZggPfZlQ3rdSeaMOnYk4cJcew4nzly1mnZw1fj2hhlbAvArwHDC9IMZqSQPOiQvw93WX-VRn_QoMh5R8K5QDDib3oAHQl7DbEwx47l-mWrQKiuLdFNlOoNh2U4e0RxP2M5wS6FplSx-W09WrKvSmxZ6d0KUXZLcaYX9VWnff8T1N9a6ohBpsj_zy0THJFYFMDHVvibQaMOJGSAE-LrfXx2GsfnxiyQrkvP_iac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=PtkhoQNKA7RHgzLrywLloz1ZRrOBbAkvUoN3TPi3ENGObb-0E8fFttbA_DKxltCzPdEYB15vPl1kjGBupOwjrTUxIwCxQ4pHqLE5OCrt-B-QYDNp83ceVbOnKyD9RXVi33oxeK4uh2gYeaG7AvhZB0w1X9Tq6ZKNJTX5H-oW4EKEmhRQ_ge7lToOZ-etbQmYbW0SctFMha7qHk7MR-YgqFX_jCmPxbl6yGuORsJeCJB5_T96eVItw_qmrVObWzSBOtCg3ewOc9BajVvtUc9EJ3CxNB5mGhjTDi_ZzCC7s9ONClZnThmUa_tMkdtotZDByRl8uyzo8UTO-xxd4o1b21yqxrIHJIIcabKtUWKB7KzViosga3R3fFsO9QTp0kjmxrqyHYQ8WjEy94jLXaaoBu7bw2TeGHD0rNJEc-bLanlfuqPrtS_gNPoNJDc57anCDAnGNZggPfZlQ3rdSeaMOnYk4cJcew4nzly1mnZw1fj2hhlbAvArwHDC9IMZqSQPOiQvw93WX-VRn_QoMh5R8K5QDDib3oAHQl7DbEwx47l-mWrQKiuLdFNlOoNh2U4e0RxP2M5wS6FplSx-W09WrKvSmxZ6d0KUXZLcaYX9VWnff8T1N9a6ohBpsj_zy0THJFYFMDHVvibQaMOJGSAE-LrfXx2GsfnxiyQrkvP_iac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9fyvrTxOC_4LG42gWUr8DzABHI61gumwOshnLIOgyU7LVeqVq9MoLF21hMnfbHPWwzLXbubg4EbtZTvoI19rccm-1NgeZv_dRfGY5wsItdsuwbqmmcAk8aCD7M149IYcWKpsIXTQPfOBOyf1bXaF2LsEOZ58aPQ6je2nkrkVRDFzdP0iKNWNtVdHOD1g5hCjOLXRoU_fQMBXld_Dp6XubFwy81hl_JwBajk1bzzBFyJkt3u6Y6JNQNmIuctlWfNVDzDIxg-ttdMry9xR2016f5tGuWy2nv0wZbOXDC17CCeSIpu1Psx3771C-tg74YmwLuU18-F0qf8JG_H9tNb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEwfBwlaXQP_65-mynEUNYQUShGWZa7srl8Plr_NirBkkkIJXJmxhqVWXMwSiOJSTMOej6oYcIUEZD1kAHbp7G2lNti3dGvl1ToG_UpPnclF5CxyZsZPmrVViBG614ELmsb3frm0AnV1WSuDP_XA2PGgjSo4s9ge-rWyTU3tX4jmRExabc3C4yX9g5Q2cXJvjemuLxIh9hygOmz1uiOQKZSrrA19f4DC9Xj1Hy6x3QX1apw1t9iwyaJx3asJkSc-G8evpZ69IvfvVj8biiI6PQTba-AAPy8lP8dTLuWMWdp0HVUbpMy9og-7NvNRpNvLiswzyOEzqCw6oW9mklQiBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrLjY-CoPXVSVCKW9lngEp7pfPkI5V9rxjMUt33yEvDxv7akGMyNyH-RCqFKyd4crN-3Yz24Ux7XjanAqYWuSTyBACJ3jFrmHsxkQUE2Nx_V5Yp-4bPBlKxz_PhrirOkW_gcwP4doa8RboLueHV-0WGiDgna1ZOSqZ3E6t1lZgWEwRCR8pCwsh13DADfEPDEdpINYGD9ShdpjuWjnv9EK_T-RbKoHfK5sRVnd9WkCtRYToK5dZ6v5oLv7oofQLLh43SxgWIion26l7mqobeVeNwjCdXE1SYb4iH_5avpPW5vKVc2N27SRwFnjmPcSNUd2VdpyXogjuO0s2Y2AHm9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMGDuFK1tP2jPVo7bzrWun9EloTjpoyZ1cB8P9LGBX9fWAO_gtJQO9v00PqkkfceW7tbKaKgrhekudjYw98vy0QA0CqUReZggpbBKPCmS22o-droP7ivnbMsavUeZ4OME2RKtpmOxSUVGdqwGxt1U8WkVfWEgyCqfgsmnccgpw9Zyr-pwr_uvNUy6jjj4wI3fRIbKFK2VlMSAxBrWQsHL4-9WGiNCF-gHgilm5Eq0VK2SFS3sMkoIneFX57BLi-1eH0EMgfqLwLp84SSNOvya9pAvpRDOIENLsV-J-KQ5QDMys2MiyEhzuDaTWVBgQq_lTmLw1DPZ4mOd1UGWPphQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJcTxm5FKGYW1YHx6QN07Nej6uYT4dzUnsCc-iS6CfI9dliW0z41Zj0rU3mDFb8LuTbZN-w1BHXoerDhtl1IXHSXtb1jwAT7DLKbtM-k6j1UOpwN1dyDxTyrLn0eNLYqZBIlWJF21LAx-O6UAQ0bLpnADVc4c05wV-T5fBkYDxNDvy-CMhuvp5_KTMMQbtnFH4Bm7n0xuTPlZgN_icUwqmk8UELNiB88JvX-f1dzVpcwQkCyc4L6M8g9b6zHUjd-nQ7csXgHAFKLlWdDxNTxT_ONUCxOqDKfRRZeCgI4rEyQ2T16TiUOHMeIKqwY3QOAwWQfHHFzemFKEDWP54nXwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0V999t7jKupCroxP_yJyAs1bYQnrmjExjRE55q2Eq7d1iVBFSU9zd7evmI9YybqNSrQo9Wkx7bzaakrU6z5Yxl5_g5F5e66blXkkJtMBsqplyKhF3OH-y0u7FA8Gl8mtCt3-Z2UyQRq8x63uzTRS1eXjEe0Zm7PLN9qpqiD1lC3YoZ5qHtP2FzZiNnGKBg3oZNy49EfhPb4_rXfhnFdC89x08N2KQDQPfKwu1Ncbnl6pZV1-rAF1NkNiAGN-W6ItgsMTyF7kYVi_YQjRJLkKb1DumehP5R1qmAJWqjnzyOilcAAYLeS9uZJuL5u4uDpX8WtNm9kLcIK4sCI7f_1PogE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0V999t7jKupCroxP_yJyAs1bYQnrmjExjRE55q2Eq7d1iVBFSU9zd7evmI9YybqNSrQo9Wkx7bzaakrU6z5Yxl5_g5F5e66blXkkJtMBsqplyKhF3OH-y0u7FA8Gl8mtCt3-Z2UyQRq8x63uzTRS1eXjEe0Zm7PLN9qpqiD1lC3YoZ5qHtP2FzZiNnGKBg3oZNy49EfhPb4_rXfhnFdC89x08N2KQDQPfKwu1Ncbnl6pZV1-rAF1NkNiAGN-W6ItgsMTyF7kYVi_YQjRJLkKb1DumehP5R1qmAJWqjnzyOilcAAYLeS9uZJuL5u4uDpX8WtNm9kLcIK4sCI7f_1PogE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkyTx_pukmTHnD2cez1Uv7F83rMltAdW4q4MIsBVF55sZkKPSVAkPTKzvxfUYMeuscWX0kGGSfw42x5NgbqkRjyOeUb2D6EKZstR6jUCQcZhaYACM6fEpTJJIyss2m-oXmV6HO8zLVUxiwwPGWcoO6AhMFKINKbIctnW-4X8q0ST2b5ecCN2OtGMtKpIQ8I_021BzgIHvyWIIlLxe0LpZVbxV47w_JgLjih6JHghhekARu3xewrM77pFXXoSfjVnqNAlarPgunk7xUOmrv2RjpRoDTLw62VSh2I_M6RDKge45kgSZLdqxl6chCmmeN6I_HfO1QACLYvZE6tJhGK0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfsY4Yrr25jBt4ojKbfA_PHiPwToDJIfBc6IgfNQf2md8eoPJLl_XSY1JKivK3wuKpQ_fgX5pElrT3V3x929cZRrkG2kYnk9ZsuAenLJ4WYxVwDnkmXIsP7sABXrfD-5E61VdXOblDuHu4tuKsmi59_wqfA1X4NqswPCGwmsmLBlZ5YiR494fDQWacDL1bE_Jq2_BxCohL-2ccI9CudKcOsCbRr-u2bDgENkczbqof4UV9Q5AAlaGwIyBKSC8bqlqBAiQ1UixQZCM9wdLt81Mvs48vVLpncZAKsYL9SAOvok0gS9PRGF9NsV9hIB2BjFbqDPXAT-g_wfPPiNdN6j2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMEfmurIcIUMp8UKvDhbFcfnAYejGAQrmcdjMuA8p0qARfE4y4gukJd6liZfsGNmHvayzK9bTqvxCbqXaF5gQIR92i6c-0mQ3z5OSz3qh6GKAJSklBU-Lg0SUNLEIcCAh1XMF8TANqaf0NS3LZR_KItCxuh0yGGLXmCihDZyrRfwHvvmIIzDUjUBDahpkjMkemJxo3kiVvh-YS_S2BOGMxJTX7-4a7tvrCtWAleGq-I9_MYhYdto9BAruwiXUnVWetWQLn5JXHUBiMVrdQL7ISzNIY2ViVs-DG8mY6AMzZfDj6H7rXyvXrdbHUtzoAFRilFdlhVu-bTYOdM79GKNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRCb_-m8ktNR07_6oRf1Ff-YZP6XdZaDLJvRNlSR_drRMRtB02N3rVU9W14j5GsqQu-lNO-7KMWa3nDWRWMeJrgARJV3HR8QVQrIrxh4a2NMdYEedxR7crnIlucSYCMHKWt1qwJqjbCn9nlhoUPeI6whmL58G3zzOucEcIWu_hAN2NWiRWr_GSDn22e2rCv-yafT0FqOYndzDomXG4PnP8XWy-ADS2WXtFoEHPfsKxHWwAZ6Jvi7i2aBh_JGuGNezOMG04Dq9z_PH3Q5s21BwFbhbksM-GIhFvKwzdWyEtNVffNbhNzHVFx4NEozbF7Y5oJ_D8rM9ZFgwtWpXgIElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3X2vf4FcUauZEMpfKGm-pz-EM9hCyPZX1r4q1Zl4r1VIt_je3sAkQEME0n6iERQ7n5nU_FyPsfX2upAB-KiVs8wOjCGqZGlu0Ld0RRAFXmsVXXCShYCs1tFY74difFP1O6ExYtsmiMHpJkgHGsbiKJOENcY-wTKAaKwILK5V9TSpW0llqKPWxBLOBSAoexCT-PxhPPblkcC_fKexJhEI1h9IY7bXATB4AhTzmGnhddP5pwTeZ9vloQQMioKY5PT6NOZd9ri0DRqEU0dH5V225aOFD4tc9oHbArlPrX7c0dKXAs8_e6FkTcwWoBFvezpAwfZQv18Yz8wAOLuCn2mPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uboU8aEaY8cqK97D6FNZDW_0ZwgBGfmtqgYJf1-J4NKPYKa6nrymzdtrtPc3-uN-yawxRgEOPlxtti_6YzMPIjRxPY8BglAY4FI7M4Ijqv72uz1PAdO21ZOMG8F_qYC2ybLg4r8WMq9SCPWj_VHwIkHFilRzbT8tZyMBUVUh7FHeypCwV0DbBKqoknQmnCCIDUT2kZhaq6_Wq6aZ1Z1wuvUQbysed9ZwCg3N279MdgbTH1Mk4J299I_Orpuf_2yJGJhl_GBOZEa0OIO-wcNe4AdChezzSDDGKsO2whkJ3ybwYcb6RIlhDGhF6e-t6sXnrxwf-zS78TJZtkS4lW7yyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-rocket_3.13.0.1.zip</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/danialtaherifar/799" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه راکت wp rocket- نسخه 3.13.0.1
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/danialtaherifar/799" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wordfence.7.9.2.zip</div>
  <div class="tg-doc-extra">5.5 MB</div>
</div>
<a href="https://t.me/danialtaherifar/798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود نسخه حرفه‌ای پلاگین Wordfence Premium نسخه 7.9.2
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/798" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-schema-pro_2.7.7.zip</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/danialtaherifar/797" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه اسکیما پرو نسخه 2.7.7
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/danialtaherifar/797" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
