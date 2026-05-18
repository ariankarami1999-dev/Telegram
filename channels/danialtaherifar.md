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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 425 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpHXDD_Ak60a1rVqfjdUNLov48stCOJR3bhlTviZ7oCEanYujaUH9oX0A5O11BDWUW6Kg4kpRnjtGHXzyLy0jKamHJ29kMkU-U8YRdKWAN9yYzZ1bPG8pO3WE0fqVZBcphiLVDUzVx_g6FG6KQsYNE17pJjTKp6g4-xz76g6UcmJuUpKFnNpBFGPgxOfPJdXsqTM9BYp86gdeVsJFWzfiXLWqZ_TFffL_x5xY2HKeZYhK4yekJePOEhkpP5Fu-RQRDh0DJLVgIhVpx6-eeMd40CphdvHZJf7Zl8zf3rH7qEXdBw8s805uhsUOPaylz77YS6JKuHVAH0UCKzvs2W4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 430 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx5bKwxSqe2MpTgpOtTafPClEGQukMac_FjPXxxmIF1zhOUSduLxpNK9Mz6cnNrsr0qX8gnjE_NQuvvFjYn9ez4P0sPDzR8jc9xlGkT8JXQv3qscz-qPTOaUvus-5OXFC4B4WELm8VRY_fcBr82uNAB6zb2MSGpgekm66ZqtNmf13ajuWHJXmxsDmPRKQr7pHhkcjvB22egShaS3D82o4NG_HZoFpUIH_QPeu39a1Kx4TecHPsY3QXQEoB7tXZvL-b6WP2YJ_Hfkjc2Xw09G_qWzK6KT5aTGO0T-ZEtYLHQkhhJYtPqdNWT990k7PpEvh1Gikvm2i2Vn6XAkl_EDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNyDAKNqPavS9gtxJObNRIX1CiTq3XlVpaI31YciIathu-upJg6BuovRVdMsHB2i1k2jlwhgyeubYCMRwT9lKK4-RndERAG7PSQFYeg11og49elrQHClgsQHvGmngrjik8DPMAuAPkTiF2nK3ikm1tWgaI6YYgntJ7QSbJHs4VL3mwe83KFBnYtNmKi6rvumNVMGIpfJqCeOx9FtoRdRjNU_SqZBvUoV-JT0DKxtOLUpJyvqZ6gwIyKk8zXbNoJ2M3yTQLKSPPrNUdzooF7VzHk_pKgWu7Y9Vebmx4asnmbeDNaQbUzIUPMYGsPjk9AVaXIQ0r3j77MVeQmgiG_nSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6WCl9Xyhgf4oepoldlKah1eff78Ni4b8GcMB89YKr_qd7F8rEbbARf85kSSs6aNTyGMaUxukke3totb5WSbTUEwGX75AJfznjFuxYoVgP4wWE3EVSTFzx8DuwrYOo_khvbS_HxtqpOyUibCew0FGRWmikZeu0HPTJWFjtZMmmwlbuANncCXY-ECuvf3hjJQzYZQJHLd_5ZxJNb6s1f7IRWnNBoA8Y-N7gAt0vNIuS_CqDD4I_0pXzIaYMWgICvN9hhPj0W98Qb0u6nX2p1M7bcCxepGpgx6mI6kLGKEmuxUwBAOFLdSCo8PuucpY7ELvQRbRHfZT78_C3BKZnnHag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eETU657__A-fi1inzMJucHjEpm0bTjgKC4wza2nZB8lvgfUvp8ReEmSM_zBNkRHgL_vCIOSqgyZA1YSJTS6CpGzbH_3CLW6KM4oAw03ogSHMPOmrzdrMYT6BCENSr3V57v9CtEYOXe2eHL-K1crvS9aer6g1nVpjQ-Xdw1VmdRJ-J3zk8uVRdI6VoV5mQ_ai0baF2cLuSbRgTxwU6VocB-j7FE4fHrNtfwq2cI8TKrcYFKu7AvhRzk59BtiXt3vGfg_aZpfEI0sl2Y8sLdiKmzGrrRu3WpxCeL2gw7logpcQTFwCYPI9r03yNeSrOJjo2W_ud4FmrA_nH8cMwIlRMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtvRmxt6mh5yeBvQSpeCIc6nNN_sLlxKftOevFTFHYcho0IAPjXZvZWzlnL8-R8BviiINP5Ngc4600GaJ0kiXVcofdn5ZE0T4-b4_rzxcMSspU-RnPMuwJDCpgeinIJaTgeN82pITCPBFZskogNxVFXyK5xIO7A-cVkHlgoefo7eaIgqmXyYm_2Z9pfo499gorj4sJbtrhjYCdNaTr3F2K6GyaswfYl7H7z4sNcM46B8EGr_n1un_Kc7JXpuGhUGB1l6f13JepKrFchw52WE6pf9wn6JXyqgDpnBpgS-bLj1_nli42oWWonL9GLTRiUw2bi8Kn60YXFzuo7c1O79dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elHeuPR9bihxWEUSgbUhBGEXtogAK9k3bF4QdKQQCxZbSLORTtkgfpbEhXnisGUwT7OArVTIYXJWPtNzEZ4fRf6LkCbsEU8tULgnYJcvIBHoRyIbyZEn_bVpHqal9OHEf5GpKhqjxY9SbHfGjl9JiqQOSZjH9f2uDesrahzMN16KpmNflcGFTiBrT1rKOGtRZ6E-4l8wQ5NQhu4t2trIP1oLAwDc9yUUbJX-Rax5VH3cc0KBIEQYSaLldCkau4MXJWkbKlk32_BaekG3G6nfOtZKcWyfU96kXuvB9sk933VNcFb0ZB95U0KjjVDPoj6AzqteeYgaaoMsR3uhzY-N6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvRe7NbjcDwkZCNhzlgKgMaFdFbSv1qjwLXw_0vlLyOA8fRKHoBnES0eXUNbQbRaY71UaftAu7olOfs1DzokVZ6puGDHuZAbg6ATrOXfFGi2SNwPZdURAY6OsHqCF2ZRRBZVhMP9_G78uNrTr_-FBVRd8S-hSNBUeHkkd-5lGID5yL5lOoDH1KLqi_ZNWOC90DEx9XngaWe0I9bEDqLw4acu2ZEBXX4yX7hyuD5hrelZmB5PIoDA9b5yqLpReA2nsjawprNanHPMW0VBFzzEQArGu7HEt0SwZ08W-u9K7_Wf8DBTbR1w4iuasLqaCS-FbcWS5brgmIs8RP_mEgsM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g32cbGUdp9XOw6Fd95VEMlcAo7iycW-hIS0xf-l7c8LXICHWkhHH47V85no0R3rSBHQlQNLtDejI4qwIkC-TGpZDQYF0lQQlleQiUozwpfIo3iNk9IEMV4ZyLN-Hi_K0nDp3NBgYI-7c9VE3_JL1z06lOu9r0cNfSVDfzrTP4bQd3LdwPPJXm8vMlg7vx5nmoBoRPavg0RI8u1b7NEdC5lKljdqT_FDQtIfnCQyCTTXLEspijP7xDXT6e8w7ltJMXm_0pdlT8gMZBXrpzLlQ6fxvCLWb2uF280pOCLiYQLXE5l7qKkTIXbpdwH_k0JntD38xJak7BYr0YsH47go-Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXAtAHOQ0TqPyKBGBlLJqyFlSOzDUov4hvep8jjTkmrgT2DnPirCrTNNpmepiWmosGh0PL10tc23F7nAiqCg8VxSpbTuyL13R4o_ZRAE78rP1JIugDfAzpTxpVvWObTRQ8MF-IWx0dnlX7gPQ1Kj5EgYw9keBayHnjbBYGS7wKmqKOS0pvfZFeLO86R8m5FxNH6zD_3_3pWSNLZOPIuuuKh2Ix8j4Nvgq5hlZu5GlplXRyYyjm4G8dNdOX3VhtKy0Y1w75zIVpiyljCAul3sETQBiJprokl5FNxC4ZRR-gYYm6Z8eoKNXHJH0lzWToyGrgwjwNx8r47Yul2H-lhQTA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tjEbGsCSGersjydHTvDCWHk4HEFBXr1dJT-Is2GZjPk2rFpv2U0kd_E-Bv5VscmslMOYXLIXinCmaqE4Vosyq-na6hzaCdubNpfJ6f1-ySM9vArYfEGOBQxsDcoKH731Col48WUsTpuePUIsFD-iVh2kVJEZSbW5narZOhAIr9HnBWlS3a6FeIT4R-AS8evUgZxgQtdP7yaPzu670YJu7SPhMEC_QGw4jeTZZrkk4hiJ2LbmAQeG3xaKZN_Ng_N3t5uZrGoTTsyy0j_qdchI7LU8RDDCbMZawRNeJKKYPcDzg80Nbtgg3rIOf5gxfKqgAqd4S9R79nqPdnP9H308Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tjEbGsCSGersjydHTvDCWHk4HEFBXr1dJT-Is2GZjPk2rFpv2U0kd_E-Bv5VscmslMOYXLIXinCmaqE4Vosyq-na6hzaCdubNpfJ6f1-ySM9vArYfEGOBQxsDcoKH731Col48WUsTpuePUIsFD-iVh2kVJEZSbW5narZOhAIr9HnBWlS3a6FeIT4R-AS8evUgZxgQtdP7yaPzu670YJu7SPhMEC_QGw4jeTZZrkk4hiJ2LbmAQeG3xaKZN_Ng_N3t5uZrGoTTsyy0j_qdchI7LU8RDDCbMZawRNeJKKYPcDzg80Nbtgg3rIOf5gxfKqgAqd4S9R79nqPdnP9H308Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD6zJwyaI9ge9cTPzMFhbBozbLgJE6i566Wg24wrYE0cxfyH6P4vgXBgwUIDV3C3ehISi2A3zZmgmy7G8JeXjYrP2hvCqlOI9H9SGwOGdylp7hrqFZOuhz6k22UMTZEP-m2qeJdk7dYhsb5ay6j5KFYohDCX7dwB-84l5MsCIwJviANqSN8g5pp5jgZiDZdTExYCGsKlQnj_WIeGhkqu49pL7M7Id4i7F0sWjGkzAUzskiO2p-CYw42npj0PpAEzJ82vdOhOpnJ_P3FKZv1a72eRNjQGReCmJz4wtrGuR0GZuFRmGOb14_YSDdRtw-edHyHL3gH-Wd0c8b_3afr4sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNoQKsFe_cTX7WYfXIffr_ac4TZnFMB1bVFqBtqJS79mzTDoBnhMPmu1fWRruL1AJC-c1e3LhguvGE_2aWKqSe_q0i7PvcNvPXhyvNSRVZbZyQMfnRlQ3ZZrvIZNv9E4ccJjAcc4ch_edG2TXc6hXIP0aEw5z5AaaH1jI5ppOGyQVo4Xr23VdCZc4KrQ2ROJRf97K9pZjdN80dcaJ5YAMhuDlmhg5WBAMuZVDvN7OQd048gKs-X3zu9HfhXrnZ6TxYV3TvvXpPxlKEb8XsO2iPPLtFD9_qHkmzvW4ZfRe6gprbfuWfv4iRwWm9fb-MLkrmbpwDwx-YkT8e7Ne99YEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qfcg8OMAn1aJpTdc-9WaRNqIc6Ut6XG1DMlgMctdr67vVrXMsSfZEmS9dWw9quRPrk_xe3nJg8aOuaYImfqaCw5FQonCFaWxWWXnF7n4MuTvqz0OZcFhvmb40XrrnBQMLqVmivNrdfRAzQlijPuSier3WH3BG380GYjaYhdwKGTLN7M3KWtcxq86ONaohTe4y0V_phQYcx-eoCog7YM2zktFLI9vCwQtKHTmtrm5RdmoHnEzBurMk7t4qAiTsJ_P_4TdzMAAijbd5nh7zruBp_b4SUJ8BqLWo94y4T1gze7Aafx_1AcXy8XRDttGpd2JWKMGlen4OhxFCS4QnpDt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5M1rmLCj23B6AxpdS-LbI2mJ3Le38FQo7eP1x86JWk-cpT0PcSgga59P7Ey0dEZjRil3n94Z0IH2knIp8IAHtNcM7FAJQJluDnrvW5QIEfO45-Slwv4BZA8HIb2xhRDI4DF7JMY8F6Qre68iDaLJRB8OVbx-xyzrzt88LQWEj5lVKnL6Jxzsm1IPPsU8QDzsYDnTEOABB7LjaVFtQFnZQhVo-gwiO_CEkyw397EcYPvRdX6gQeHrhwC8T5wvDo6O60VnTzsKGKAPjmg6zdWLxiiE5yPoZuo_w9t1VmlRDFVgt6tHQmoW60fktZBuih9C1A9bZd0ExeGt2z0aNm_2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAcO8JWZyiIBI6Gr8TetRh_vJqDvnM0v4ovb1O-xDlJEwrCVwq3uJZpbLIstoZBaYZs8W8afQNOVxk_rPrGYW6kYU5mq2jiUgsGDnSGTa0kxwdiQpoi1bJc-YB2DOdHwpWCMn5QNlTl6H4Xx7yGjNabKCLkq4HgwH5rCr2nn3kt8arXn28sKHIvokh4sz11C4n5UqixFgpf_MbHc9HFpFEKn1d2UpqU1DggiPnDey55ec9u9xGuYFlMRlI8L2DK-kjreaJkyjLGmO5Zd4OxC5rWLXWEKoCxn9dofqWYQBCmlxbMUGVcZNQol4HlOzSYl3lXWrBh-UYOB3zVJBbqTbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbLCYF8ltN1SfqqT2NPy5xf1CCyBZ6yA4lu4N_jj02Wqw1_EuXqjM5D0JFzeiFECP04pnsGeIqfF4HFfNCCsqCtHDrkNLmVLjszMuDdwlkvAYIdW73aTckPoTXFQi1dgQFtjd14uzVzGffg_sViCVpeqs0_EldBVZ1uJRFYrHuzk9CmtOCwHbAaEHHXRZCJetiSfNRLMof6bMPS_5y5PNEmJsoCPYPP8NcJFOF7fAtoWHe_ZnTKyarfV5KOLIowx-Flk2K09-PwBuW0hslzQo8DAzLbH-2JgRRgL7J2XwjBAp2YbC8HzN9shPTVIgF4ZCqpd7Sg7jNQK8Dzsx1AYLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkMMudmI7_ywRfC6UpCVju7Q9yczU3kCiVJ21JyhSsP_VIPEFx5XjZcGiVTfidpNX2psmTcUetdigaynU8cKX7ZIk2ULRC0IFIXI40cJkZh-qkZbzTw3KztPV_T-8ybUPK4q9oSsimBMskbD6qYz4eaFszL3FsZ5C1l3Qlxp-MSKStr3xEZ7JLF54LsvVft6Y0WBO-3hnj6NgaKWgz-BnC1tHVqDO7IuiZCgKlutgZHUn7F8kAA9Fiztnz3AypBB8bx4apGGPjhHTo4jYcB0OKuU4OrYjSn04iJoalj3vgGRmiRw7ERMIY5ZhXPldu0zYqao7l7ZXa1FY2-jegYhHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJxb5uZ6VmJHrt7PigwEh-vR4A-IBQJooL4fxwy5uAp0OHvnXGl3hqNBwjzo-Oqlu_U_RqI0RZNOqkOIrexIoTf73-BHM17LJ8tZgMq8VP86e1cHEwOAo0sHhHYYLF_WENJHrNA6cwpMCbM-Y0Ab3OUIIPxOXaHUHEknzsFhzStu5Jy_Nm1zc7ju_NKLhZIItnxrYlC0OCIfbdhZJuluUchwXPBqWJ_7dPcvgU21gXWWr-Q5jZqnQN9eizv8BNUKRq_gxdIGbdi_x6XWY2zMIVEyOD2-xB3dBW_EYdXt3V6HTw8F7zWCTEtbrr6mT0GDaqyyRUCw25Rdcf2352CeBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwLF5ZnpeZvMpODSGKbkrpy5MHjC8uT9ilvvVcHQ4QAqQFM0iQRDWk1FXloymBUGMkY_EtF5bEKvnsqftsBpa7yh-Ydd-gPV-qfmwHaBoSYEnJz--yApp4W5vqxzG5l97G6XbnjMcoF1Zh6byh2aRx3vN4-Zyh9YpdzgursJV-y63dADu9Rpe0OwRiM0ln6ptj4By1S1AWxZ5jwNXfXVxWE6VMaztq67OrzXtRS-DC8VPsZpV-FyYBEzbY516y0OtDRI2hb4FBZrFBbRQ8OWiMzxWlEjRZQpceTwerWKnVVLytTuUPoNwngsx8Zin5rgqyHkU-R1AuTRoUGmXlkseQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFPAF2OIy0F_TbNoaZf8ZDNghtt4OqOj5v1bYeUePlz8DQrvJtHhbE2ugj8GE4n8VIjpfkUY1i4E4M72pRFrVjtE1DWIoWPx-_Z3ziKZ1ZaSnfNqVNFmmRQO3sLH1YC6dn7A5D7tdsv1bFnqictpcBrcRONKET2O6Z_qZ2VjYgEFqi6HBHT7-LBhPp9sGYF6iJYF48co9POqek-sMhnz24itgEwiKMg8E7Mc9qZNHqlad-HfSGP2jv527L2LRokSDTWdz-ssLWQCzYIRFClGUdbroz8DjjKJvf3aBusuZTjHRz7gy0rMPg2EUk4qYjQQtFfpRIoews7f6khrhnjmCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwMZWSo3u5I2erUyrRAqlqv6AaTRG4mo4rOB6oE7FUC-fOrc8C_eRMm40xtvtiACOQqkhJkRwlKtg3_8ZMGHRmTqUEOv_FGbnBmPH3LrULv14vzNMX24-ogZPGO7tn6lqMbMyaL_IPSKw3Yc2JJMXrXds28PLtEAx4vS3W1Q603zxwhwEzZJOlY2vM30Nr7DKdDJ2fl7J422d742kOJfZRMiVCWXcxrLNmSG3z_zAViCgHTmNPI0v-wpqAG15M3NJW_1JW7qpoppWop1IfwILLC-eCxO0ZF3rXSqLGh9BS-vezzchMnGN7Gl3qDOo7FY86zefM3z5drAwtOauS6ZKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jteON-C6kU-Kux-v8ctHYia5eeyX5BddsInPkrFo0Qxsbeljwwh_qV3daVX9WegOi0GxMhE6mHr-9OG5JFzqX8bcrR_nFi33nKSUw_-Zok-mqbhsgD43coW3cg0i8zRdHtyzoqnxCyg7lpRLt-RS-8tEYdY7wREVnxxWLA5NQViQ9WmQ7RxNddE7YtfIMx8CdnSDAQg4-9Vj7Wz1QlfqjzszNinJuKs3WSQRJ2GyAt06O9W5U_Bx-le35mXQ1YzV-3anU6G6itTKJuKNUZV3EohT3MhIuVdiQO6d5cQdD_GoV-pFpHy5Tn524Th2hdK4JDQ3Bdls89g8i6pmIIbUzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3qZRUuKUTgaJO_bbeBpdmgPOBkJ-79SgZIdOM8kVMwAuliMR0rfXdb-ToFkMPZUuBPUY-rOWWCvMg4Kz7Uxw0mPoUiGX1u_KE4psOffJ_BF4SV16L2qUmFG5nUOcNzPr0vYj-FSKLOp25JS83BZPalISmupRjVa_DnbPSDCyI8TjW4XmX_mlsCJy5SfBwN4fC2dPAFpldlJmLcodMuIn1_tqJxLCHx7qQW_7Bm6ore6J685TwCoURVDbCH8Zxyqyc_lvFUgzn_0v4mMerccJiabpvGl_ATAlIlaxGHNXrmVrk6bi5HkFsGRoVrsRDl9Uzk5zLwhgWQK_K4B0Lof8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdRp_cWAZESBrPAflTWs-rQZyYAEZfhVsgeAsOsvqJb9ni1HCEPNsufWJKrlt2k_RyoAY0yrbvQSWXguWO7B-i8VuYvE-IA-T8d6Itk2Scv0arnZHDBnk84pHQW5dOjLzg5tooAXmCfBSh22brCPH6Bugn1pxJt-QGRpPUvNxkIeEj_OcU_ng8HCrrPKcjgQqagXsANFk4oeqssdOud8WnnUcDBJaaR9sif-3CQSqzbQmwD3HJ5KE1obVKVRtoyqtzSrA9qPnTZoosJvvyy5rE3KF_1CS4ho2vXiCgyNy7wemE-zzjjJFPIsxVXUBl6_hz_oGL-TZxvlNnGcHOm9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJBWKsCPLC6_V2InSfRC8hAThSvpVD8LW_-1RVHm5G8m_Qd2Vc8cldnmjOPbyo2-HlZAuQZr_F52dJs1BUhuFANoif_AZMnYP4d3YXgQ5y3aaul83l2zQC2nFJS2-ehErlMaPUCY24OSFN-U4qH6G5cqNfRcRMu1ka4p_W8jYBwKs9Bltw7bnmjDHYtSot0aDQjcCDq5hK7Ctra3PCUEPCluGTzXk-lCBaV2gE6eGYqkrvCgloJRGj0QceOY6vqfYPrByv8k7q2WVaUyHutix0pfq4iNFB5MTBfz6h4DZAf7ZnuxqlNNqapAA-qHyNmH6lDJd--DRMFF-6gU9fq8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzF3pTtlOKGkUwOUOzCRYXiwMKiRizr5T6cQEyTVDV-7hSf58Si203raq7ehim5GLXGbthH2XXjjeCzGjILsiCCKkqRjnVSpbEuMBl1eqhty4BIa6abQCLtLU4mfcyYG_UC2UsVtGyniNKI2ObUi6ysj8Uh_TlydDgbj5ueOD_MtUXqvDxxvJxyjlw0KDaMOINJnI-NhZhthBk9y7PGzuU1Dkit1jG7Y519ljTu_sqVBhJer3pV7JpDjQknDzOQz_q0ywYZyzIGEShwzJ3ZRfKLQLhiIMWgQJdUDOIDwYlsFzzC-B5Kldi4m4tetdF5ucI6iBqGUNyETzc35H9_kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWlZ3VSEr7Exiu1klwG5DjLKANPKcx1IqYDI62X7-O16cU_bJp2XBCTrqdZ2VQPXBFe-T8A42CVchKXuPDBNGitqNm07hJHNnCnrlUy1Av0Ygqv-6VPmdjDR3A3wS4weA9UpV9ZqatxCDdSH3O-LlVlu1bsgyysSrAPZlstIRD-15S-YKvXPaZAHXm5I0c6INdMxfns1gwnJCN2L1Z042ngK1K2nQORqBp-ayMMhwjnFO-47L-Cn4XPPLRPlnKMlfj7hHIbhC2_cfFclPnMIeSxmyodJDeZsVuAQjIEuybY-5rN-AFKpKkRyWV-sHk-vf4RosjIHgFZXYLy_Q_zx-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPBRW5yZIzh5auAYLe9jRMgCHxF0D_ARcImkr7E8Lngk1QUkVMUe4ZIxGa2pYTXSnPwhGDKMjqbEvA_mcuwVaOBKTLTm7hTaSmkkDT-BL1NWMVDP-UmdF6HmtylunuGfP0UHm2XowhNHx7Y3R4Y9VYyQXM4sRWhk33DgzUAy03voZXQsinmBNWR_NqegL_QJ89yeFojMiuP1SQ4bXAgUaB8iez1rXjKZaIs82A0sTCENTZ2CAcQ07s5A0IK8A9qi2UNjZaxzNI0x2lCyQ_HfUEqHxLfwgQiAJT6J6YcVTQ3OWP8mtwfg_tniL6chp5f7fWH3ZthnKnictZrsUpFm7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2rnsnejTUPWeDxHENr0wIHDbvC9OcYB7sp9It6ItPDzinaasJulKOzc9ofpLMn8ZwzsobLYwS5RUFLj2nEuwhgYH7UvSBhlJsa5TzcQErxid5SAuSPdKQRJaz9B7s-2CMLt6GD5oPWnl14q3KqdOnKwMZ1pb_PiVGjvDi9Zs1tyFxWuXJ8CYs2VavE0mRMOfYqXuzMdH5-Gl4TzFDxHk27pv9Xa6LPef6yGTAD8lbMhoStVAfvPofehzDAumkrG5cyZNdZUCKdoPEy5ffRJdc4-KQWpHj1k1CLLkThjqswVS14U4bS8PCgw5sh1Ej87qKoTXy73cd80GeUdwlDZHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oElZlj8BNMeIRsP0XiyZvkmLD5lIWSKrmje55sPEHMh2WNHO5kiLYiwFF_GT485Lw3Q2GfpT688Qm2Mz2xAb1etB5eZv8P9pAhNzRATiGs7QKR4c4Y4_mkCCUYCmnS285S7eFVWh85yVl11SwpLsPeTaZfdHZCA0x2RKQq03UI5llT2y5yLROOKVZ_naBgQm5zBFQiEA-xnooyD--8msLKEMeIDHTB73CXw9U92zu-nui4XfwzMvI_FU0lSh_XXnPux5pA-lJFnK6rMPkdjBFfagBvmuXMbpHBe4H-xfzpJLnV10h4KW31No3VW2XZWYtbmub45Z2kqYENYfJJA4ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7oSUFIwkmegVpUoiOEIZjtXM1kgzOIFjx9mEwKWr0-6do9WR7ucv3efwDAbZqBTvARBupVVrVm4wPYtbR7_9gQZ8vnI4qEGvdNhj5DmkWgR1s-6Wpp6E8GS-fT0iFEE5GUta6vTS2YKzn7-5BtO8TI5y8k1aH7dd7Beo1OxVgmHezr2s0SfLEEt8HlYPkMJXY3_DQ8RiSikPNJlEqMRL_Iwef5NSK0wGsCYraqVyEmO5jI7ovFc68ToCk32KtjKM2jTatx1ZPoM_scI9VhdKCN5N1bMfO5_FVVZsv8pTGc6FX4AIuLF4aYxvKn1FX_3E0e4GEDZdIReOHRE_lF_ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxn9upBpByAEp-SWw2urWjfNgUCsh3jc1DeqmHu9awCldegXIH-0iL8KbQDrYWBPj3veZ2uNnhC7dvoH79bUQHAeOQVlZo1frttQNjdtxnpFOAvcymygJ2aJa0uSIcm6hFIGqMY85eWly1H1Ma7jNapVWN4bKIkNx2GLXC94hkHIYotS7dwh3irVr1lzpxVEEpPX22m5Flq_t3Ue1Al4VnS50NeFKqdte4TnlBVmIYVWGZ5M3yqVoTwTcngjNulYPdVFI6aVcJ5gICZNc8vWJ8gpWm_oKajMEtqClsqUgXgLM9QhFQFHLwuLq3li__DlgWr_9ZQkODatO14npWGTqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDTAnXLmNPE40Zk2aqTwBkxF0LEDVTIa4AnmPnW9aUinkvLMRfh2GIr9avWFYXpADBZwCoj-JyTbxQ5j_2tlrLOG6DIT9QzCbUU8Cgd2Kr2JM_msduewL4DvSFL6_qpCJzb4BVWbgNcVRshYsm3ppQghH7-edBslxwCiiPTGdO5_wxDcQ2vgkSIX18jW2gMTyBShQGM31G4fsiucmtbTK2_Qk_HhVHDEabF7JGjFm5BldUxAEQmRApW5N5oJkVhJB5ecGMq_0By8i5hTjjOQqh9bTAk2pRRpgxVoQOt_PeI6SYRxkrsFiBJ4wqKsdykNs40JZ8AcN4WD6O1SNjL58g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOSpl-NsdYN8XEbLLFFKLsTba1a8A-WOJstTzCwsnR9RJ2iskhcxRA8P90kh1kJqBsEFBVvJgxl287EtgMec-yu1hCIhMhHlU889_KhgE5Yds95gtFqF1_-pnOoLR35h4a0eHxyYOp8lHeagHjLh2gbU0U36Kg2tvdHEVYCAid1WkeLMO-ZrA1M8YlGgYH5a4-BBXhTl91lNeKc9RvedBApN9iZVN5pCltAv76TL9V3zdxiV-PJFaBpX5E7poEkgTd98gKi2YdEEywLo84NY_-kHRSCZXJ3os8IUHjYACYZkF3J8WYoo3KY7x-Xr6qpfxNKxmofSg5OXa6c51qQeBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLKVzaqeuSYb85UqTAMpJAkc_KjJlc-W6JL9GyumxbZCt1wBckEHFMaOWkqIa3MA3WBmHaIMN6mPB5ltgsy32tY0EMPIIf0C3FG2Fsq00HG16Bo9tMDm7beIYKh1krypSSEd_YerLKzgdM8z-WUtWRL2LyRCijJV4UUt0whXXeGUOtjorOSWGsXWeHBRKF0MMMgS-ZXYJpDPwiAElhNnIsmL-a7nyB8qEab44gmVPqLbxpg_wsUfBw0_lJqeu0dNvzSAYjGBqypjfteJSXHxPKf0hLsGSzz29nufZC4MKobMkYH4nnOFv15S9mo-AmV9Kw7fHsxj0ytO0GqkHzSZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHDFIDkr4288fIRtcMmbJ5bj-G9h57w-9XbXZwkG4GRqZHB-2ypFe5X6I0f9MzHDxfS4JXM6zpw7GQR5Ml7Q9kgtlEfZM6yU-ew7eF59gUJHvekFryVpkqYTHweWAXs3nSxL7Qw3DP95QCZRcKqjhPN7FkyV4lcX68TB6_HvVL-V6gJDEWjw-yuqm6_n66bOMdP9bPd0T3uPBQ09PLkRLadRT6FIb8wezbU4O1SlM2g-mZffoHz-Lx4Lxb1cG0lwHKypKWP34DOh5KmpXTabheFHkZNuPYNz6B5Kz1SILdXiMA23hxFvcX3lMlZb7JpLgnT7Nvj6RYmOf6Iwj5h4Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPL1jzcxnpjpC-u_2Y0jodYjRqLbzbHsyDd9_v59cXXUUqWoyvedHPDrg9C5Jq7DxIeVqvtgRnXOK6cycmX2L8MsTdH1liG6if0uICtIDHJ8bpCyqw_jHZJkv8NWNvyU5g9pLe2lVt58GS6OdBDiXpj21PDngwAXRPafl4dF5FymZHl2QjiT9YFVqmhBkySrLjcwcJasSugHHk8sxEBa3QTRocVOeiu7NtyRgPwLO19dPF0wb1r466RaKLJkv1nLcE5_QYg5miD1aFyWM8Dk5RVefZ1tKLJ-wuuyYAqEnNJZW0OuZacnmxzBSKBgeO98XWkSjS1OM7in8p4CUFeKxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8SPDGGIItYQMUfxudV9fGSUCyVs7Lvxj6hOoEEASbDoJML1YyE56fBqIofCgviBRE4JLoNz2SBEBDoh-gfw_guQDtqEgBopGuLsJaeDAkEvLqsCxDPvbh_cFaYex6Y2PHW7Fe8YVE4MvhBRubj88obiUQdkZX3hr_wPZmgO51QbwsQ3SFqrVLWdyeXJPrGlHRr49TWVZ0tomIq5ota14Jrx33qRSRvIeuAhgB4wyo7fFTzRCbsCRhUjllUKf5WGOWFC4AZ9XByFckPLici41R6Et2U9tkdgj8ujHQDxM4wFeXtW3nM7r3lvTYL_EFx9iI0Yd5rVNSLEpSxFHBdyng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veBXXVxZNpVfprlFsPdw2zx60FbSBQboSAqAAJonGxsUmiajb0T0RgmkeGMgNivsHWO8EpmUKDPsA4jEP1xIe97jfXX-WW7gRByPW1lU_zRKku25v0TwGPjeU51PuRbDhhp4PISyrr-EpmZ1SPMIJBPYETws0PWzdTDlccnqG_7GttvgFODMwu8nDg7rOgxbBSnJZpPTYlsqQYB-B8eTK0TkhfTAV2gp8ToABma-Rw68OZdh6TslVCJ2m6VdpGpdMQB0AqSKw_RVqVZNH_lU7CJ2lv4HG9_ADcCvGA4sv4FweXGSxVVwvBkcVzy0A3x7F4vbJwpzzrHKkBfDoBYiaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_o1JM88pUCPALBTFNJeGgAvBHpcqJzKwgKmvM-9DgHkzKHAb1UEQkjF59hrdWUX2VgYcLXfL1wEKjcPjBSfgYanbPrELb-gC4SoW_QWMmKRaalZd4V2cZ-sAxfoJnQp36u_V7rBROxarSKfo0alljP1evsv7eZQi6jPg4iZ56IiFTZtdhYbrWF-ywtZTZVWbNq04Z5oMIfA15tOCrIMABchAsK44_HIoWYX3-XzTDsZG9RACSbRcpfinaUP0fCouVpjgsjoyH0Jhd2zBxTaUl-RKYjmXEOq57PWQTAh0RLwDyFd8nXtuXJuYtHf-1g6_cQq34kP_G5ALHR2F9SPAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbE_acoKTq6MJkvVcKTQF-pNnsLwhfmlpZikdzHrTJbsgRjH-1IdCwQPoj5PK14WsrvR2I4TJX6TGM1Odd-cBBk56ygZxHghe3FgscXH00e_DCumGoXs2aFgo6zDox2x0n_s1spSTy9aZKY2QaQTHLvtWrxrga1Srtxcz_-UWrEco_xuB7KwjwC59I4x2p8LzvFRubFqb6C0wN2_icEBZ_F6KDDNd-gV9T55p_-QqQFnxCl_6RYImMTdcUMW76f9VmRC5hJnG4AMx-6uDj8lGPap2qXUfMU6r7mxEkSTmpYlXMZh_ffZMW1JSBIt3qeoj25oF_ISOGGeG4sRjNrG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxq81tafB90ytJ91RZcXi6iRGidSJvStLaMG3Kd05gir-OQInnxfUFUVe_SH451iVnRvpG6sTbrfRwo6rP954fL4Mi8jEPvm3mpsFVmtrU_c1faJYdETt4I-YYrMIHFa__TRMFWKAX_-GRj1G5gxY_7XWq4kJcWW_LLee24n3Zq3i3WjYLc03-jQm6kAmWUkMIrmsUo-F0jgFc0NojaL3OjnMxA9aJSC6pFMTwNGW2jbZnB2CmQUrx-v3xE1ur0f95JBDqo3iRNIcoCgSoKf45qfcJWvaa2GA4j7eFh-6k_6w9w-mp4yUAi5wwLBfN4eTfKF8DPdcbhex_ZBOGo7MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jd7H5OiYlD27A6HPf5oigZuCMeSB8OEzYeOGc9BR2VqIRG4FKQaTWKW16uArtawN2jztIK7Nau0INlHDvuT4xmAolXXnWY2NzEtlqVNTCqqcRv28zwcM9Zqrr8cK42TSwBpsYz3igJy_OHtl9ZqjPagaYzKlkuBzZZH9-_cHf-GS34BWEWgB2vxm9IouoU6klzfj1TSNoG7_MT1B8PWOKkoyFAJJ-AlOSALdAozB5OxzG88ZN9lFS9lnMKL7aKnVU5AlyQCFFfpWs1BRcQ2XA2gZixpBDOFAtvz61-ZNlTTdfh7sHWifiJzBwMuNVVcMcQr8PmihT0mckCIYMlL8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJiCfsErDpCkmwfhlbbXNSQ2UvITBdWPlcBpNjk4n3fe3KEcM7bI3BJF9e1CEzb96oS-7rqwk2MEMRqi6zbvd_oBiGEKY2qtURzzCN4M90TvaUE-evw0En2R6h6JlXLZTf67ciqbVqM1HzG7QKgY1PwJGMZwi6khcZmSx5CLiMQaV07FZBDMk6iHcG62G3N4YYvgeuQDVEjIx8XKu4eCWwlAD6K_MRMUrwGX2gsP_xzrymyO1KTV7030iCidXO2gZNpsU1qPE2U4xvaxYZjUokXNFtR9pI5R2mMzqVzG5sF2Odh3UrnJKiKtm0oipzHsX1o0yOKgTZuk2NpTr2odFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_HGn-h5CGhRbO2BsXVGbXlKEsOH3ha65Tjz7zEW3jssfKJLplEWv-zOVp1Uypc8bectkBGFml87m-BF-ElK45z_rUiIXdgotQf6MouNcSjCmao7UNVxZUwWM-Q3vPMf0tjGTuO7eEjmAApdMu7rYdf5hgH9OZyWFSyDZ0VmDQMpMcHzkIEjV8ZvfVKHK-eWFIyFjjbdfPFn6wKCTpNKnAYGM26ICM_r3hE4hYvuF8pbfBUGjzuJmZWIJlBU_-VKbLHb07_ZSgWZoGnW1S5yA7PHG-7zGipOvf4ZnHWfpJGA5hlgnXl6_-BcDYBiKHi4Y0P4A77_nifU6NBdyfp-aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMWKAeHqNNR-bksgwWkrZI752b9NLRKwIOm-mwnDgPCST-Pz-aIdTowSZE3YvKAR0ykyxH6wwf-P_P-VVMOq1dT-FQM9kUJwm0Tov5yk_cH-NGlaKHVKi9K9IiEQiSTIrqFHqHHogJiMBt0oVUjLKlkRP85pclL3Dl-m6XWaV5s0Se9W_c9suO6ulZkZRYn_IXz5HM9fpTnPYasjQSf9vSEV9lHNVc2DPYygpafLh96A-2zz-E54W601rZDLu2jLXmPSxOP2NWvSwVc4FNJzE_SYvNNubUyStkmFjzhnpJ3WkH1XX64Ra0vrgEhZNBRCHKvWc4R59f1N6a4AhNB8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TdIncVX_La0hocON7bF-B3Cxrud75HgK6uPPV-od6KTIT5QU_ReHRrQPZF7gkU784FTqVBnU8elRgQoEQwUtchg1k_MWv3itKuqEptrnTY2pWXnc1K7cqnkMGbmTfYWfnVGT98ktbAFKLzUXS5CUtBqjbmmocfDvosS3vFfYA5vnfT8Bwbo0MN-3eZNsdIDdAdPJ5yEp_xh41atbqFiU6mUse19ck8_BJGhzz5BGSNb6v3U6MEiVy4T7flE2RzbH8AkWOIqlA2agaja-CI-_ePno9kaSpHhP-ehrtfz0L7GjQbEUv4AN3VbQTGtb0Ct41jjkiZvYY9e4HNDaJnTPKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaAKTZOPVszKi5Ox7NtJGp-8DYidoHOQSZyeTwHztY8JXPGPqJfKnypXSigfTFmClSx3QngX9hnLxS1GZAPCFtoGrTZU4d10DJqzRdh_fsdZAJe5B-0xynUtmvKT83Q12Awg6f5Q2W9oG_hj4va0ksJphRsu2hr-TL8EQuNK8Sjr0bam_ey4BdUDfBb0dCNYv5rc1i0oWHmKDuO2d5gWtk_qYrBSBjgZvpyJMjAy7gqVCCLnh_94jjK2CmOFr84N-vD8Ia341b7jezcrXc2cEONhHpAW3eXHfno2RMD90iWVLMJrsdc_FAG9HemqN2_vJxyOIzOlNr0r7BJC2ynGtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb1ZrP91FE2iaa_By2zg7j_uC3c-K75dsBPsAdnIFSyrfzgiPfl3P5a8qQPnc_mBVgEWTxaPqr527aqJ-DqJL8GiSLEvd0r41fOfBRT3EiCeervHtP1Fx_wZQ-URu_hTnkQuOr38gTBrXJHfJsEcYf_3aSDpawlf02sVIAFBhMoX6VR6n76Hrle7EWZ1e3_N-ftLAUuNy8rHNp8z_6FPoDg-9OkTCOpJyMMCAbpZzd0psmvL51udQPDts1-SqzCmjoRnlM7viUKtRL5FlUznp6sMuWnoeF5aj5Jfx_MoALj9mVYsl1FR0Hv8yGMnnpn76Iq7e3xvB98a19R_c07SoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF9cwtQ-jMYtqe6IrmWNZU4s0RNINFpPdJIODnjyavOvhggQJ2aS3_5FwAvdYecu-SeSF1cUE1MCy7dyxvC7oG1yLX_nRQvuXBGwhABNZ6ZnX1Uta_w6I510xZSip6PpbVECmJojrnV5aNk9OE-g2vVhbFTFv8Mx_hOv06x1lyNp6Sv4qfrFG9e-Lj-VW76MhIwRh3DGpfsYuroFr78AavrTJqR3dVnbaL7mYIai4TYkt_3190SrJsW1P24BBJXWjSKFjQJkLRPiOM4BkNrq5UhBTb1mTbO53xHK7Bd1yGWTr9RdtcsnS7_mLpg5lCSsTXxRqy-zGXnIF4ASt4Kilg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJmVgftYtR3dApsVGMGnRZk2IBTsMkvwu1ucpKt9PX7YDkqOTttySoUKbGXXE8D98vw_hmchdwu2D0nrxkcSWltT1IpEjGy5tCwqR0L8-Ifo-GJWrS08xgGfb-Je2TqckR-7Fqphz14m7CYwf12I093kpfOHJOO2K6k0LRNRBn27igEUdfeWinIvdhkGtQF-f9SU6C9-zmjSiSEXnpFDf6tk8rj0FlKN_qYwLg7TeCeuYRHEmmlVpy5zxrDPZ-4FMdkl5oGjRVxsO9zcKQvnIqDBY_c-vvSsdEhlx0dvIGuwJ6HObxdpZHKUZGuYRC3Kct1E6OQkNT5tLp4eE9p5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idNVvTU8bC_x4EByhg4qJr_FwW5DfwmgthMNvuib4wc466e4-uSluG0lE3TO0P4atNgMbrVxsSX2GGxpRvZeexbCBMULnX90qVITd0PRNYwN3rOmFDxKXr5SpHZa0rB6KeTBZJpt8BKhOowVWLLbRHppSYQU6T-kRPoiqVUEfls_y_Zkr_ex9whp8w6HA2mXAu68Pwdb4Olfw2BmoV3-a0AKxX2uDfxOSFTuVUVsC6PmxjRkwDVZRUNObAjVGWI-Af8gAJcbB4sf9pFJAIMF7ILK5D6HlyXYvolbSgp97bI0haTLfs19MKdCB-BX_DlX4ROqJmC0J21X3xJQGDWoaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzRUJ4819zieNiMXXoGZ4o6r2Aq9AInbABCEzEGGutyKrpx7GLZtPMHaU1zG1OeoNh1A-QjAq4dwZH39fChZmyPe6ZFdniCeXLvFd6nLPfES74HRMGnOq-LQsKqos-xibfM9qo8IceE-Tt1fQ84kxloi5t4C_pSZYhy0vK8ps_GAcTKN4vWQe3dxkP35OvNIytAXvvjRyAllN6TYBKs5P_bcwsHvHplld7fqJI9dD3nU9mMTmP389xPnElDUizN70n2Pmm3TM9X_ItHljHTm29sqxjlqMsE97vIkOYNTSFgbi3K1HyOmrmHmaBVTA-meyzkQPDoqBT42yz_Mq2KtBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUQxITrkSbmpgEOWT6HNHe0Yzdv-BZ4e8RW90MxVOuenRanAw6AHI2_2UrLkUsL1so-M_ETP-UqzSpi3O2_8c646GLYbvbK4bMsJQx4yocDqe7ddUP2wM1uSPuqvbADgrAi1sdPW9Rl_FhBpyj9ne3hyJSS19nsMY2zqL0E0pd_fMdo9MR2wuyJqnzLABYpnzo8Yin0itHFJqR8JRLdcsxr4jcmoSb3w5uLw7SeSRS7C8CMzO-yJ98Pg3l1kiK9jYAmDvACz-lxoYfwEDVQuDZBye9lTi2X1WJ-67B03w6Ul1wW8WiR-uIp33UaQOxOHzODZ4oAW5uZPuLreoMwzjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GygDeKgMSQ-lrYhlv1UFqB_ak7cUIB6OdaKPZiINcqXV6DuDnweoHHV3XaTJy2vMaZhp5zHn3uwDgjgDfTR5aIwBTjDWVSxJb1jUytpT86i1bBYGge57JbHlSj-h487erg_B7xhR6Zoscgn8y8HmjtDlJ2243bjvFMzLSZYsW0iKs0EpUsCc7b-JkH_qv6auzHMPcEyXKy5jpfJI_DwmZi31dv9BF2QSDwbBLNMQvzJ6aGR71vRXeSWiDcO9yaeeqAYlkzEzlZ8s-pYQGxH8Ubmxt7vd2aYSgDkInWGtEAC5GJtr_axZxy7PqXtOoctZTzzWh_wnbDQu-EyKCAGn6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LftWHrIZjel5A-7Rg9W8yP9m5JnQeYjNYO4gRk-a0-JMOxqKZScSnoNFB16aqXw-dNScfvXd04L8OmZ2YSLbwSTJ-nqPaHu6vDYPqB1sApGB3AnUoHdg58jxPr643DkGqAAjsE2WqqzIUxzpmJzGsftIvSvix-VKgJuPdtJflHDk4nS-tHN1_SQR-jlvQ8xobTQhdHJQ_ZdeMYZyIbSCjiWlDS6lu8J53PqATGsbdEiEu5KbVfnWcb6eBc2ORfXNNtaIKpEy0ph55Y0llv3RFaSKOKp-9-MVE5SJA4C1qgDhDAlXGFHRm-90lezr7Gx9tS0GHfZWwm5nVwDdulyQtA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=YadFlJrS6gJb2V_O19P-OI8TKm3rNaVke6d9a-ORjvsVrl9eAte67zT2-ZzuBKQs4HnVNm_7JkFxE6H0Qv43rdHEEW0mb29CuII3BRH1olHB-oB9GHFRsZGDzJ9GQZGHlJbq3CWcMlgDAXZdo7JB5MDJeixhS_C_RYcxcLZFMJ9PHCOheHgcy8lUKsutTkN2AbIHIlMQeoolfaTs92o3Eti5RpsuNuh1xS5-oNRMm7BjVwbi4aY4xSrMFmrtb3yhsbVrrX9_cqTRQ0f2Rl_Uv8sMl6C9K1nm1RB19kVEVJ63m_2o__0lQMe8_Yuy-80AGSnwIdifwcwaejw31R_hAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=YadFlJrS6gJb2V_O19P-OI8TKm3rNaVke6d9a-ORjvsVrl9eAte67zT2-ZzuBKQs4HnVNm_7JkFxE6H0Qv43rdHEEW0mb29CuII3BRH1olHB-oB9GHFRsZGDzJ9GQZGHlJbq3CWcMlgDAXZdo7JB5MDJeixhS_C_RYcxcLZFMJ9PHCOheHgcy8lUKsutTkN2AbIHIlMQeoolfaTs92o3Eti5RpsuNuh1xS5-oNRMm7BjVwbi4aY4xSrMFmrtb3yhsbVrrX9_cqTRQ0f2Rl_Uv8sMl6C9K1nm1RB19kVEVJ63m_2o__0lQMe8_Yuy-80AGSnwIdifwcwaejw31R_hAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/je4JR0LdELmOeilTuMcZQSAYX76yRfrFZfugMFJRJkD5vSKaxsDbkt0jCktC8TZmUTSmkQ_K_rHEDGcMrv056ExAv03VXFaoW0q19qAbNoctfTnNMlycbaOSBOwB9TpVyTVuvSQq1WC0bRZ85SnmXZDBSocD_RRYf_44k_X67XHy_KYvJXSMt6tQmu7DzQ-ncIpJYxQjX3MHSfP_5Dx7RbFeCFRasyOACljfi10puEzrMY4S04sN_MUzokH9JIL2mYzNgNiLfRsD8fv5Rk7hQDHZncwmXP6NDrGVrG6DHKPAD_AtMjzPmISBdz57_h98aytCd0ehw4eLbCYCQNpArw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXhYMo5V-BI_JPm_E2lBPiI4Bs13ZTmfA6lsd25UxilH3OcqmEKIl_MDH3RpHfe0p1SwKw6zaqC-UMOQMfAIVKaajBoKXQRfTj2fHy-uIPaMIypv5vkveV3Sh-rKnzI83jPs1Hj_lRauGIa3bmaowacNFUwEMA6tWgvnRC2EiLwMIyxbu6Falun07t1XKtOdzRMsHmDtAOI57jTmI15KAH--Z-FWiNXQ7Ad0REkeJiSPMqBOLcT4k6hJFoXEvK1QWKKbPQwOAqK8he33DaCLUvUQpQfQUfn_t6XivPm9WM-oFO8BoxQsp0JL9qVquzmet0SrsKTzVD9j3VJNBZ9DFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5TrabuNso6rbI_pVuDZjh608Sr0FAchFQARJsoaR_iktBFlbi_AIsOP85K-DjTous3j3ZsNwLKGCj6HZTkAY_DV03pypXBt0apBgvsZo1g7rp0MnlmQNVuDCWnqf0-pvz7LnrXt5s6dMqW5MoZostAo368Otg3RHgaIdel2MRxxu-tKJjm24gtWuYw-99TeXHhMX7YA3Dif8tRVXj7cfW42TRELRsHdp6_XJHe2eIYtzR1vIJMtAkC26VpEaS7guCyCYmPLNVGfVDZT94mKlbPPVcyoPbw899lO5iKr5N1WDcuzriwsu37LnHeyXe6twpxxiAUvwWwkL0AmOzeNew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkk-Y2qhd0WIEPYwSTBxDHqB9z89zZvhwt7CPYYel5K2-0pR1lE8zD2WwF1Wo6tqa5-vn1MM8UXRjzjXalsfXHI54wZ1Xb7mWy70HTwrqmvpkOf9g34DO2Iv-Y03jrnD7DHFzX3nI70Pr4BPlp_2NLvdKinnytgkQkIQwz_bNLt3tC-jbEt5Ul-4GCkyfhHSgLQ0YkBAD7nLL3WuVZ-Fg6jT4Jgw2jgI6Y7CGIuGS8rsyuGp6FCc4TV6foUV5xVetSaNFChvZGOGDl_7zJMhoIWJFNHhJkPKXTPAQkIT_kp4KGGWcjlbfYu2FtdQ0UjpGueumNr7Jj_VKptCkCeRNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5wn0n18fFZsPsmssbpofyUqkaUCEYezUeTTBO0Nk23NgI0gzAZxBtFoOVy6eCm2r3VmyT4dT8YJflje6t8W3dyUkdQ0uIGdeRFrAcMpPKZ2u6RmsXKGHw9NEZx1aYO5l9ErIIBE9vcUREttDYht3e3EoSnNFGEjFVlOwAFfTbLKk1kmvk_JYU4eGkAx5rGDZ_ktLsq2GlOoNUg9aqNpUf5piD7JnUIDrLY8lhSfUeqVDYwIJpeZ2Bskym0bZzSEBL6wFu6CfxLE5JLVyxIPNuwJ3yXbsPJR_g7jG91SNF4Q0izEhSKvoAzieAB69rnxPdbINmq2H7f3VRvt3PLDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPWsz5FFbLAma9_Aw3a3qyyLi-v59nAuErAsX_l4QTndusMMryA8CUua_LkhFiFO3YiMq6bk-ENKaqP-BZr71s8L5tirDMcRH4o-RfLABm02ZCY8ZfGmTwQ3RSxwDzF9t13vdK9Tp7y6OhqZ844KXcSeUUiRGJ4srnWPmm4Z_U6kEZyValgKrGjSQTRY4CcqELce4DK1Mh5PZOAtyK1LUES_eBEiczpAyedH4P9_-OSXynpOxMVVPin3jYaG8oINmBbyJdKLN3tYsVLV97FM3UEd-ZTafS69eTCnNEYmODGXOGFomOORNtDHUiHn0HPEcdVLlb-lgCT_Y3wnfNB-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVV7KKtvVUTrd_aDTGQXBioBfwZj3CxPCIVNrubbykpt3qTDPWRIdeK3ao_GvLiUmgKhlByQSnjsnwISNdwB7LQVO7_OikZiC7WWDMMv0aux4A4q18oMpjyMVMHnVtAu2FBU7HeldrOlIURj5NuTu5Lqj-yhR7zWJ7N8qqI4DW_5LsycSTF4s4YfDprjTtz47Ih98V017bqz-Y3Ygpa-zXijCTdXvpDmuDngxzxYWFbswzmhtxkhmsJSzMbfubn_JCDBwD2vePDunAbrBL_dMT9tXZ9RR7mkTqZLIiIKuek2-6pHrbWoNX4NVUE7esya_RyuJzqs3GO7MaiCs8g09w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Nrz39WIzFNbLLuaCvX4RGNQpdDACBOYmEaXTHCu-jxyZ0gQIieU7_qlxyPxdPDgcricaHSBPxB6pamjp8afkSjh3RH90CGXj80HwSbupNW_LGzEkqWlZt1liqljV6hNe2NBviE06DfKPIM8c_cmcTu1BXZVY_BLEv2sN15cZ0Qaz6aVbW2PzJCLhEx7S8YCQK_JxWLOcttboby6557U1Y347AsFAl_C808H7K8iJxpc9VDZ2RMorf9VSECLI4q58Q8QhG2lWP6x8NIQBYp9aAbFJ9sGOBaIo2DzUO3eoRBZY5rvsbFECNF05foB7125D1PihXPfT48ax8eBdwZLN6aVSbHfWTDpkqlYc909CZuILULatuU-i3msUwTp-gemxmEPj33vFQ2xBUhzlGhy6SmWeT5X_OOxyw7LG99W5kT81i-Go8S2HcT8IQEv5svKaGESLLpXgoUVj81I35pj-dLaUsK9o2TodYgBsVdEi2f3JGfW03Ld7Hrs6eioh7V6gdXLL1cqUEpwmO6bG044hPEimffnIrbYu88Gtw1Y3CK0q7KzALu4ne6tCC_jdo-o1Xd6-n8CjQuEAVnPt4ygEKGt9LbcIvbELCvn5mvQaCAUaSWQAHS60i0mIFzVhr7xY7p-vh7QfF3K2C-1M87RNo_8-PeaWBrbgLbSKnnK-6wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Nrz39WIzFNbLLuaCvX4RGNQpdDACBOYmEaXTHCu-jxyZ0gQIieU7_qlxyPxdPDgcricaHSBPxB6pamjp8afkSjh3RH90CGXj80HwSbupNW_LGzEkqWlZt1liqljV6hNe2NBviE06DfKPIM8c_cmcTu1BXZVY_BLEv2sN15cZ0Qaz6aVbW2PzJCLhEx7S8YCQK_JxWLOcttboby6557U1Y347AsFAl_C808H7K8iJxpc9VDZ2RMorf9VSECLI4q58Q8QhG2lWP6x8NIQBYp9aAbFJ9sGOBaIo2DzUO3eoRBZY5rvsbFECNF05foB7125D1PihXPfT48ax8eBdwZLN6aVSbHfWTDpkqlYc909CZuILULatuU-i3msUwTp-gemxmEPj33vFQ2xBUhzlGhy6SmWeT5X_OOxyw7LG99W5kT81i-Go8S2HcT8IQEv5svKaGESLLpXgoUVj81I35pj-dLaUsK9o2TodYgBsVdEi2f3JGfW03Ld7Hrs6eioh7V6gdXLL1cqUEpwmO6bG044hPEimffnIrbYu88Gtw1Y3CK0q7KzALu4ne6tCC_jdo-o1Xd6-n8CjQuEAVnPt4ygEKGt9LbcIvbELCvn5mvQaCAUaSWQAHS60i0mIFzVhr7xY7p-vh7QfF3K2C-1M87RNo_8-PeaWBrbgLbSKnnK-6wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1Pwj2jlJjQPGoy9c62Tb6EUTE4YF3X8VdwUmTD8lQ8fHRD4Px0OS096bz-s5ODEf7D6ky35GTclnY06_TO_C8XrQd-aF7ZWodDsctTCWK8gyL5qxAX6zKm3jXA5Y1QE1sQdD5hpSiHxVGXXc72k3OHgzUhFqfLnf8QX2GYZ23twZwypxnDXEzleysWgMgYSjvPeTQw7TX_5ACpw4B4ZN89kABAefbfCE4F9Trom8OUTc84vydA_utMJH_nQvHnjeYU2zTShL58Na79IIo28QnXRluprqK6AG5BFZNO1RTKPRXq4XES9bxAu45Avw0y8Kn8pDyRtIAyus8jMEf6cOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brv4cTNY-wqSQwso3Y9Qu6A2QF5NKV-Rn_5BbyYxEXS6f-wmlsN0EIMevzfSMA7KG0EL8YTe-gUq3obAf9LZ4sfv9RypYqQ6QcZVo4d9chktTjfvJRlkx3eHtS5sBh4sWprZbnSuvWYfKuj4GRUDyYVDXugSw9D6aybJtN00b3OjSOzUW6b1bZeO3zO1UxPcPXmRlv2hInuslJjfhHxnx3BIEG3aRdK_T8K_xUxoxxB3sUvn7zsS8n_-WD166h5rLYAZM9Hqt27lmNn2258alOfR5DyWg-XZ2StIEYr0WSkZlAT7i5sPVoC4dGg2nm5yEMcO4umiiezN2H7fHr5p1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uu6mEi3y9lvVCiHKcKlrkFJaskzON2VTRTJFE-zFHp9WTsvIsU-ewtC52MNBY1n6NJdTC-pN-A3YjN45_ro8rTUU5x7XEtrkPifbTeiWmFbq5uiy0Vqn2egbeVg4Q11PjZgpuXUI48vz5RBgxE58WDMHoj4tqVnAyb2u1xIqAIu_wNvjMAt924oEXNlKLIPbHQptfOAQJpEBnuALo30mRF-VPPjosKYGmw2IigsNCUk3qXNl94Yq_xzburbA7cUKati8xvNZp-bm4nda0kyThMcuguJnCNQ4VzV5Vjt-jzt-rtm05yxNSTU3m_gelrsW2btAYIs2GCDrR8fmC6yqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVjEHoGVeMZgiiyBhKqpLMYoVeVKC2KhMSp7fXxP2ljhw_NFNP2nrDaRP5OKhh0hgQvJ8M5csaVW21BTwiWwGD96ZkQrM1fMSft2iDp1ZArH624rYJamyz76K7XYlhGy2GD5IhimZXK_X6ANXBxkJPdVKg8ry2kB26mmIOOfWB0NKcdzhFXrTkcKzQRI1riVO2SFxhjn5O1oNFyBdAy5ef_eqdZ05dthJ4ugBRDhQ-DLJX5qhhXyo1iq8PATg1doazNmv-Xwjv0z4yBKe-Lm4o6prmy4ncFG0sPWjJBCzss8IeKoIu4op1B4v21lUTlQAGHz7QqpdlT2K_I86V8UqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAR3zNQoV6bsZeM3VzFZWg7wt9veJ0P-foI1BkjYhxCXjgB4MISl1e4PAS7ldwCPtUQPhgmJZCrUhwS8mdvuADePTw6QU0jzLP3Bx_ASVomA9IR0f9Qcp0mTmJqu_G68pGs2m_bpwW4XUjSUTTH0m-iGuo1ubD9Tvw414xRJvLNlChwifg-pxpn3iD1b9wz5CUjyO2b2i6Ymz70410l5jzle3ep5Lm1DWFBWEq0coSe-GngG4saooWFL6dt6h9psalJEloadcpVqIOqLIvK5dkRGR6pgli0gTsJQMUxPnRMe-QobmOUmXwNz2HWhg59VVzFTdPWwl-7iByjSjReS1Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Wep3XtLIl2A6R4hoj7q_mFK1nBnkOO6IQVlbq4-AsZiqOnY6RZT_b3JyTEteysqrIMhHre4bsiunWUNfYNWJ5-_pl594VbWbMwJJAVb7CWgdUiM-Iyt6LlNzHCXZOX8Xu0OUUQnkaB3Wvm-7ZnfUjdObC-2vyJR3C6DhjKuGdv2mOWPfdqSzzfOCKwmdJS9V2YBqDvpQd280N4lsyaFsRD0Hy23Pn33GTr8iU1FeakcLLRJkWS8vl4DYMV1J4GqCI-TWs87EjEw6dqYVGjLAWyE4r-PkluKs-WAw4fNWfuUThcHScRVq-fm7b5CF5zipTfBsw1dj0rVoWfXfNTnIJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Wep3XtLIl2A6R4hoj7q_mFK1nBnkOO6IQVlbq4-AsZiqOnY6RZT_b3JyTEteysqrIMhHre4bsiunWUNfYNWJ5-_pl594VbWbMwJJAVb7CWgdUiM-Iyt6LlNzHCXZOX8Xu0OUUQnkaB3Wvm-7ZnfUjdObC-2vyJR3C6DhjKuGdv2mOWPfdqSzzfOCKwmdJS9V2YBqDvpQd280N4lsyaFsRD0Hy23Pn33GTr8iU1FeakcLLRJkWS8vl4DYMV1J4GqCI-TWs87EjEw6dqYVGjLAWyE4r-PkluKs-WAw4fNWfuUThcHScRVq-fm7b5CF5zipTfBsw1dj0rVoWfXfNTnIJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7rSxGlEvg-ol8L7lRlrhJKRdk19HfJ0tx-lrViPRT-cWxX5YZ5RcGbYtSa2P-biTcJRnjuZaOZk3K91P3eqOlhvqueQ_MgL0MR7XZpxI1D2VLWpu8D7ciTAlhMAWKmKU2TPU1jnKhKuTYivUKVATsVcCwQogn42iapgsMs87RSac_6sT1IO-xFv56AUzuF4nGIgHULePmYoaqzdZymr02hCJAT0znyTsjHtbGAFVhFfAPWw8hYg1t8zItQ3lsoEtq9t1FWm8l88vkS0XKC0Rb_LpJrUaRfX3haLMREOzDNfMkjSnucqSxp9lvEgqCZZcWpr-NfN7ms9EjSf0qonSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_PSWLjDhL1Ah3ymvY5o06bFTDuIVv7C0wKxBRizLijAjg8bV1E4dCzGXf6DxmNyxs3u6dvB8IsHzct-lAto85VuXaPWYkjSN-jDgLxJ4XgvfOMS2apsYfQGXmeRO3fMFZAd_lE9DyIyIVc11zMjQ6h0NFd_dksqTcG8BNZv2eMTFKQH1tnCejqCReVSIs670r1HnusII6Pp6aVW4HLQXbkSBv4TkGZIOvW7p8pd8SeEXjBUaBF8DGtLdVWFWGWCFvWWaGASmjz7Snn-ofpE3g71n_mLjr2Y68pFJusmAkVioQMLWQTtKoOvY4topKd5phcBKT_19llZbgicq_qmwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUPdvbhGrtwr4B6nIbRPF5mOzW4Fmrqig5rUmQ4BfmAL-f9Yg2DGrEEQVPOi3cNrYK0jbYyXxifazbQwxj-w5OhqIj4nQKmaXqCAhLVNC7gmUy9Jg3ki7vdV94CNhxGufl4sljKOBy9vaVH_ifccGK_wTBPay65Mqb4kTfB_DdTU5mnlqeCrj0LnoUqnppazkJmbhU8rd8za_x_bbb0N5pW_nrHaaPhAAD2-SmVAxguleZWmPVCNdLaHQ9ql5Dt0wF9c8e1p1EUy02WEooX-hq4OGAlhpCNSIXkeg-8m2t-cNmslpz0WTZZOLDXR_IPiyUQSAv4WZoajENHQlwRRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MViV1LqO9SKFO3_Iq-lnwBO9KIHe7r8ECWoQfZPexjKegK3QY5GgOsM32BdOVd-yODWPGhpx36a_GocKMMSS8t5i5XKFuMwQT2A2YJOJ6uVXjt6LmU2XRj38lFoqJ1zUTtgByX_-Qm8UNLsIwCMO01q1c-KC-8fF0YlsEL05cTL7lqcaIWXM6d_JHffpc3eVLouuiYB8Kdr4d5b5F3IHItERSxcVA7rJdiLC5hfTJSCOR7HW5ER40WA1LepfIqwf6OpYTBRfJlC0CvCga0uNrK0Fr8R-r5GeTh6wEBEirGYSv-wjOTxUo1Uv0nbtjsj8Fc_bvn-KWEzn4KIMR9dV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugDlaA-3Q-DDOrqN-dnqfKIoor0j8NVE05Kk2YeoXEG1S2FuMbg4qNLj-Ssw9VF06t1Lc7rk5gI4-Z2-Dw_gZCO4-xDtICgCC2GKrw3qIjuLYKg6ank62aQpc-xlBikAwlAv_8Nrq6B1H1qJOAa_WmGBvk_rpxVRbkzPbKdtOIPjxGX9kKToEgGgQaIe1tcoBf062My8aF8doXzKdI-wxbK3DuLzZUMoJp1qtKO_cvzs2ildozn_0QE_lPK7E-4iVCvWaoToQuXsNkQOnfi4vCsDIgx0th4X1W77wyx3rApRaHhnOL0-qvDM8tq00FOoJWt-DDFGASjWHKzflEzWog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQxanoZCcGLfcMXYfMEjD22ftN-CFFAdllaxzrmiUZbRWvgZ1RhT7NxBxw2eMVN9oH4ZXc-88mVraJLVH_jVAf9bgSVrvypWn_JyL2tPmfMk7TSVXskVedEBru6PAc4XD-lhagZn1uZ4qCXp8doEanwFtbAUinnAPQnxnobt2RVBwbjk1HkibK5qojjklf3WtchnYXcAD0kvWco8-CbejHt9K9Bxx9iwsv2xRW3OsR4ctQhlyNsnA7qwkdqUC-6xsCsnh1jDVDXmlfqIRMXPiEuDRnKItyWdsaoj_MAYHF9RIkJe6-4bWszjgxdTl9gVG1uhIwqkY7H0v0uGosbg2g.jpg" alt="photo" loading="lazy"/></div>
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
