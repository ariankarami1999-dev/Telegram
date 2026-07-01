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
<img src="https://cdn4.telesco.pe/file/ejjMEcidefddIFR4liP3xfxdFzpjzMhszp877ZEVL87Pwx8fJt292ZDgBZoIP9qOT7uoEsQvfGA9SzZOOgkG8aiyO_Dexen8HMUtfHfJjW7DRH9oInkiYEXnLD8UyveO6o5T1BHjuyh25CAIWUhcyRjKukwe0dPBnCeAzBtGViGSUBHdbbSZrOQ4_lczRJJ_ylprO9PplV_UvMQBtlfQqNiD2AnzO109jWEV9jYA568XM8Fvdhdp3q3DR5PS-ZPhPOkSOeJ8Fv3Bbit_QgEHgzLd8gKUEkNnU7blr-MuiMB3tWQGPjiMVIcJlGF_3Xx4fn2C9hvv_jqwgjovq5wm_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 03:19:44</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 211 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8hv7vOaQzEU7R_u_1UDSAvPQ6IlHlY_sIEGXL1aHT8rEDVl1zorxER_XxxUqlO0dFsn5KP7GvqFSovsrdEgapxN4yo8mWKou8VnrjyObEZW8nKsI_NLH1cwm5qtGzNfoypoBTL4cOkUMJBSMtDfsUwzfSELI5QBGkk1qWwUOc-8HdMHqjKFBWrUuoKhlhKqJXKlcw1cZ3QVqfHbnEfjq71Ey-GxgVcnjQT4ZtxnqSMAkZBtXZadVGLmuXJBH41unKREaSQE4MktkKAVp1_1M1QoIU0-mqeKj05I7QigRCqrBvK85cKTSRgL72OWDjNa1suyzbvzGFVJOnhMHGXjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 454 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 625 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 729 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=QcOGa9l5osv8RXBWkLeGU_4L83AnmIPOQzW_BFtGfT475FbtPgxUpMmGHKPzUqZN19HOslgB6gH91unsyb5I_adYRD7ZuJG6V365aJ6x290Ai_Btb51VNIe4pGu0TfNvW0m0DGz9m6vdhCHelpgM1FHkXbUuS2CUoJyi4cIRHjOyGzVGqMO1TQIsmN9go3Y1FViCDs53TS6AMVdjs5rAQOcmNsfprbJN7xGHP7CJEKx4dW_LRjWuIUJ7re3I3pX1LCaCMFOUSdA4_tMwwlwMce1GAioOAb4cwHbf5QjMFcvcHAYi5mQRr0R9IHYpE5hsQpPTRzY4vGNerQgQi2XZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=QcOGa9l5osv8RXBWkLeGU_4L83AnmIPOQzW_BFtGfT475FbtPgxUpMmGHKPzUqZN19HOslgB6gH91unsyb5I_adYRD7ZuJG6V365aJ6x290Ai_Btb51VNIe4pGu0TfNvW0m0DGz9m6vdhCHelpgM1FHkXbUuS2CUoJyi4cIRHjOyGzVGqMO1TQIsmN9go3Y1FViCDs53TS6AMVdjs5rAQOcmNsfprbJN7xGHP7CJEKx4dW_LRjWuIUJ7re3I3pX1LCaCMFOUSdA4_tMwwlwMce1GAioOAb4cwHbf5QjMFcvcHAYi5mQRr0R9IHYpE5hsQpPTRzY4vGNerQgQi2XZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCuJTivSgCWggRG-A6JwBYMlecAsKuLxDiMxqqjxGwuE7rH_VbZwUCpf9-OMPWs1kUfTFdP_XfuvADrRsEiY_OWycLszHpPRwrfDhJUwyL90HI7Evx3Ig65Qx4STaZKV6a93XK0CvI_qnT_G2_EE7xTXYhmkQoU1FHll2ahygVVT3AbuvUHsQDPzrKW7e0ubmFmSHN9vjl18zHRH-kBH6IcKx7OtoZ6cHb5NPwembgCndnbtF-wDw23Xjfcaeaf101x7OtN7Sg3rRqPhSqqjyiQ97sWIaa5hIf7XB8Nx19m69GkQM9aT7VpJnLZrpLptIycvpNjqWFeWbOEf_opvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 622 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 846 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWsNfi9jRQepCX1e5gDV4QqApUloUqiYjFkhcB9BVtqa-JrediIDJA9RUoBE-Hyf3g_G_LdT-j7whZa7jDreMWvdNpWL0q-aryu-5GUzgRiIU95JmTlrAUhfuREInxYeP2n0m8I8sEjWwqFsVF7QliMoajqmsnfkayNOD_EpjoJvRUYgp37nCfaFJRPUePqXdJw7E3FcWag4iguF7mPcYS2s6neOROx2D9cj_GNku8dZVl8GhtQW6Cgjwest8hfEzHiYtuJcy8PiGBADCpNTcd9ocAa0M-R0apmTt3cTN4hO8FmbDL7SFcPIPudtDwr-I3et1Oj5Zhe542VzPe3skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-vnP5aDAIatPGkeBpC9AMVkOMbhdnxM9doEZUFYaCEI_2WVUdKB2uVD4jQMbRgPzniHCIaHn-DSXtsTpzfacs-nI-D4hPznu1pU94GMCEOY2xl5okFIoLkvelvMogUvBTrzOQZeGmBm-tjBn4COa9svLq2GLIJDUSfmf2e-mq0b4N5R14X7-d1lxpKEyecvpyd0zcnTcHJ6K-qGB7v66UgSu5Qy4r_HSumUy-OXtVG-LWBuG43huJ399CvYuhhYsMFiRLM8nvW6Rc0OrbXeG00lKyx9WCMFmM8Q1o_mPveh1yz68LsU-o81rGyE9ssf91p5Sd7nBK-UWzt7R-VJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To-Bw_PhBdPoNjYrn3v6Hb2IpWAIeJOefPkAXDANQj-Mrnk07ldK2Pc11acuXQt36UJXUrlddwGJbl-HiWeh0DLgewULSYwfSoseK1X8xxhUeblfK5aGtzb_BIe4YGDany1K6RDKTNT_LobCUAANVW2-eAdYX2M2vZV4VztihNx_pbWd-BJ0Byo74JeLZLKTiwuuLt_oDxcvBSqruYb_Gevlj2I0Wd4uHJKtmhVJPsw6e-3NPJOeHmxUbQU-9mrUHsxtA3V1wwcpBoIHCXwtI4PgtFAKI1F9lMsFF_UDhyLOx_K5CxbxwN5yUMTkHC-6O4FZ4-OPu2eOkffxpemk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzQG7v5rsN_g68vsL42rbgNcV7-aOFDWlSbFchVPwmcfktRag4MzeEmFqBw-6lt2_r2-tq6r02gUEF0esIA6B13CvG4R8IQlSHb5yCmxuJxOdQqDA800YuUf6mgf2-yS8D0YTlrXBCLlCj6IjNC7LZT2Pcri_kvMupTwZeThC3QRLTQX5QXAcKCIHI97F1zY2e9yqIHnWwPyqRi_1X249D-gzwa_6rwAE-s8choUdwSH1AB7H9VNFPrNjAaGJkCbY2e34xcWj53uz_KK0WcA7onFapP9jsNeguaJ1RonSSJ_C6ocnvX0TcrhBic_Fl_7W7NUtrijNCGN8KS4kf5ERg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Nx8cpHgdttHxjICt1w3S0hvTTvVwPWxUB849cFwAWTDKn1zD6qUZANe-5knSwTLjaiJnHhMTY-4p1fbo-qtxcWMkb-iCTL6XZbs9ztUQAKIfDIraiE5cXomQNQ4mVUnyifms4xKB1a2z0de0It760sssb2A7JXnc59zuaMmnGP7YqlIXqyw9NJduO04hpcccQzRwSjAO4ZS5gecVk3eTeC3OiALuH5ywAQ1k2i59R9kW0hbW3juNXevn5mpNqyy0qnn_yBBPHUDoJqRjPTTrrkEihyXq84I92KXjMFzWYR4WwdSwMCFXC6Id6ZSnZ2sf6VuRQ1JG_H96-DqOsogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieFHHeGcAcodck5FELCB7WrpIK0JnS8GleYLCT76BLRruPfxgy5vfTS8uBm13b4qu4JgUQwBUtHkrE5FQL3iwMiyXsaK3k-09hYZTah99iwjno9AhHilCEtKELm9WvlV_H-Pd5QLlrgr3dxrOBmzTm9dyl0JFIeex4Aqi4Dv-JMNkJQwRDZMxakwyXJ3Hx1kRBqpuQjqLdbhpFUuh0dksUBBcHPCBUdzhcs6AfmhPXoC90mb7d6x6agUS7z1TPgdz3JCtLFpEPlw6FxifMgCteyoS-QE_eHQAk8153Z7zd3rSU68m_qTreKVdW-i_3XdzQUOdVvI1QsuhmEFjfhmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAT3WkJH8O1ar1EwyX1Q2M9wPDM54iKGrNqe_y4u_i9l2kB-jv1pzU1gXk-a-WCqb2Xgr7klb27Ps9BafcWT6WNTrbKYdFpsFlO8Sm6mktDKFq86QZdhFhZ8MBo4zFJCtRFiUwMCIT7oFk7ZylwnnF9sAkuKnNYsz_bqClfilo2ko3rook9-_-wVJ2otBooEUSfj2_GROXsjg3VEIvNaEPJWMH5RQ97HVy6Mu6RNRq0J-F3hRSAl2dl8RAbxg_fNH-RsdlM2PwrEHJErpfUpTT_gkrwadG0WHkjCSy0b3WJBWQ8r-g9jXEU6krLDqYGm1Ha0b-NFNflON-TDYz5m3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRFcZIUTTwZF0Bhe7wIQb13wgO2gLsRV2sQTcmyoUObZ4RgRpAN3A94iSjCWoLOiTOmffr7i1MQ3TN7kXO3HtXGRnq8wmTThbYN6nn-8INMJjVfQrcch81FqXo3-sKXnYMs79ciLEZmpuJO35JoVIPSyekcJRHZuKoNq22JfAP_we6TqEUpyn3urfC-L-GGs6m-lHmY4Rxbcma2RjQSfoDynl_B270XH0ns7mPbEgOLoaInGGB5lpbTd565I_uU8mrQ3MBu-_buVeBb29KaVRDZTqrOWaoBBcZuez5Ilso6tZKDRc5ZmMycBtf1A8Me0B0J89lEZUwfVEAPlz3-uIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO2rwzMxTPXWueCjUQjjHK5xbrRviZt05KpRib_5v_IKqn2yS8UdiRW9Xy-2u4MetSrYdNk306Zcsq6MZUshc1UZlOP1iE2NfYBKMvku8RQce6NNONDD9Zf3Gq9lMIYk9uSu7_F74aB8WxMgyzDKVSFDl3jp_MTNHyi6yP1K9H9LiZ2ThF7JbmSuUQhHgQ7UjRtb56swMOetjVqIPJHxSNemduCMVqwbKECAXKjWe45CjVOgHRyoPU6hiWf4uSw1osi5_tYnTehoio9PjlkvusUWJOUTd2RqaEHVZpFWkTPDv-3h3s_A8s_7I6n4kh8QixQ8sxGqz3dbRO-9Pk40ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmSj-tJD2YtACvYcNsdSIVCpI6M3v2EMIbpArfmu80KTi7nCyFFbohmT4c5oad_4n-igQJLvgRBcBOsnm7LIeFApA2zLH11ez9YypKTa1Z-_UVgvunf-_PXPIWa30dhasx8KMqta6DIDgXUFm_MGFg-ULc4ryYwRkGNxxKAtB0MzNuh_O3FHYGf4JkXFmrFqG3db56dSVvM6WyCtNy8V-G3Q3yPu8XeAvz7PZBEmKZJ58XX4K_Rz-_1IpvLbnYQiN0ELPW2rqsNTl17X48QhVcUt5rFiKMq1H0dxQdZOwxaEZf6SB3a_p_kmgexL5gK4x1zSMDCw4JxtYOhQo1hPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 829 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo77NCieaCgwO2EUgVQkXj4-un0nEO6e5nhPHO_LpPCZg4glrNKzf9636QhCD9-yDuEN8veA45rVQgY52_Oste-kjbZAIbp6IbFi4NB5ybiU8fD5UoM7hTPzAnTMnTLcoAjaMKHI2IFqNZ7i2o8bTzJh3ysPFYYKX1WhcFdnudo7fPkyf5l1dEJqBpIsR03f58yDAittHndvWYbqpIU1NrK-1I8CI0pGgilCN8fHGI_hnJYUzilXgqFqQf6EmjoMr7BwDeWiEZfV7QrgwRnbpeCIvqmbhqh3M8Bb3fT2FRLdpXa12hahXGKDF05z8F1r3XkNVIC2GBac9PxmMlNFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auV2kPYIxF8ST4w9-kxkpZ0mov5izu6JkyXH32j3Lre8iVkRr8Mm0K4bgalM_jA4lWdys_EqUtlmYZAnwiYZ58S2eKmpeO6VEhg4kzoFpzRCRAq2K0_uGuBVwJ2LdLhvP1i00UZCcQndfs-jOp6shY5MXHOjhPHXWJObORLT0rtDLy9q8N98AZwBka_4bEXrQo5oPPjtQ7bod8WYA3nymLz87ieKyIuZxgD_wyZ0u7z906P6TxABOG7IivxVkKqKiCrc3tIsWc4ALlnMFu7R-exLtWx2bV5bEsar1ufW-3AMdDvWpvGrBraU1znmLFbm6YUYmt1cN8wyl_LijkWBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/poOwY0lhsboPwINZL_QKpjzPesq-9nvFOi6od3bPpbkwN4CgbbQcLoMViuI3lFJJvRFSX3U4tW-TLSsanQhf8ZV-5fzOBwdEMmiX9VSbPj5yKO9shceLulOA6MtkE6NeEz8jfXzyc4QpQ3UM4Mjp9m7Qe4clQRHchE_YdR5CSYDF3Sdjj0sIL5Pp-qrYwoiYSWlgap1MN7zUM2B9QgKTnwiUmh3pnsjJzhSu8kjjz1vCexD2XZUFZpJ3vMVcROjCH3giqgIQaatuE1xl0CSdNdJSTtvpkh-KKJ5rGfCc-Oroi-JaPixlyUhM3eGd1ARrQ0FMo5olC3NeyvNx83kxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxZ9GNHtzbUnXU0gjXmT8E5GtvbRD0xIpVu1xR-8bBVyz99HMcKfjL9uj0YniAoqdbh_aRDzD5eEGlYLtvrYq92-0IKltiMwn-AHIf9acvYvpVvzquRnxPqXqCVPRSjQZ4WIEDg7RAD-mHGaZXGRHzgRNXvH3F70NgRwNXqeDzCR3d-Gw2Te8-Il1LopV0obAG3f_Xm-DD1CcGaoj9iARBE6GbUE_Av4TWok1M2oFlKn7s7ALxijNpInLypBw361rk3cEljcJDYrNAV1wPYpeYcZhgD3yxRbYPlklesoTZRe6fPfhNIz23gwFl1ZAf7BXbYkIluzikBT9Y1UllfZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnlsnvkY9L5km1IayzX_GNbtBtPG7ABxkoPIbeRtSW77QF40YNNHwMcdcc7v6PRBHitKqsgwiEqtnD7tfW39Hsa8eSaU_S4SpdIbvK5mW8wijBJVIj3XcfzPubaM0YpRBGJnSL5Sa4a2SEBg5QaQEDsgnWEW_kZM3cDD_Ep8QIadlVy3JeQ1gOzrOKy5h-0SMaQ7ucJ16jZQlgfcQ9Hf7ASr9mUx1P_xZeOX3gqAXXm5Hg3zIYgmeg3FGzqFcgwn1YLeDY3DZq67Eai4MoCtCeAmWVc_J_AoXQgbvCnegB7oxXbTLq2fxLhtTsN-niW1p1edTUN-pRdiCU8BXbvD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2nSfaF67azFBmRwXhd3y4hpfkd6KIIJ6fYtVjnYfu9cnUwxux3-YqtaHcDpg9cDRyZ9v-LFxwJsBNtwC6Yel_d4cMUew1upJ34pe1esQbplztCO895xPknyiPuzbhxp7K_ytEEyMfGu0gvid2pRKnqlO4ohzia6FHSOyNluQmc3gOiYKpkASEdQJtSqyx6cvMNFZ46Kbt-bMTW2t6FsxqueQRK6BvjmfeJlKKP_mPb7ZAlT8mKrYD9h-k0PmVZNs0Dr7E7dVkhcu-9W8CeJRDn2sQRYpqDERI3jdZjD5O-Cc6YE-uYNL0eGDku3Pbqfk4IxbbFgU0_ud1nqnDVGZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIqmvu9mjw-J2UesbdaE4bLMMdvmHPhAHW3SBsEO2eTDyhS4T6qPXZkI6vrwr6XZPzHEO26zdv04l79Qu1vWolfpEUwO4QGmeV9f-aXbzYNj5gDKpTX2bKiBpwYzbIvdMxqxJCvo1JOpsvf5YuC9HzCtgt_ECXvs0tHOLUwohePYNhStYjTFHKS1czwNxtVCgaC9z-jrQn0tVQM5x_4gFt146nFxw_TB80-bRok4iGb8fhLEwM5OVXUYuGvREXwd2wsWCHQ_5tXg_APFzJdMIYoyOoTh6439RsArUPoOmbTjzjvLv68dUUtqqvdD35huAPxm7lJ2X05mA7NLF13XPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ElODVkgLSX6_MJhkXVuU59Rs4F5z9f36zkimRz7uvcKjx42o6PxsFFQ0s8OxgudhZJ2QUMR3dNKpODXVCoNk-2FTJgS6Bq-CkpINKG26e1_j_r_QCAcqkIEqIx3mg-_wehaTq7Z6YnIqrKSKydYZa6ZJvIowNV-4XA8oRScofDBdEJcEm9rlD25NtZVp1snpLHaMzhyBBpj3w3lGKtdxboDvnkwnDyui5OCJpjDavFapbjaXu-gs4GzkjHGz5TdnPlrbeBQy8_gD22ztqPKAUNXOwyaerdYkVO1G3WffkH4m4S1oQ-Gqm0YIHkfT8VsMn8WXnsgotkKyDJGZ4WCEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ElODVkgLSX6_MJhkXVuU59Rs4F5z9f36zkimRz7uvcKjx42o6PxsFFQ0s8OxgudhZJ2QUMR3dNKpODXVCoNk-2FTJgS6Bq-CkpINKG26e1_j_r_QCAcqkIEqIx3mg-_wehaTq7Z6YnIqrKSKydYZa6ZJvIowNV-4XA8oRScofDBdEJcEm9rlD25NtZVp1snpLHaMzhyBBpj3w3lGKtdxboDvnkwnDyui5OCJpjDavFapbjaXu-gs4GzkjHGz5TdnPlrbeBQy8_gD22ztqPKAUNXOwyaerdYkVO1G3WffkH4m4S1oQ-Gqm0YIHkfT8VsMn8WXnsgotkKyDJGZ4WCEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpgGPzKpFcIdXaL3uDNPZBMHTbM2B8x_hbj9Z2HtoOFwHECebsWs-yF_YgipHl82d_5ZmIukYCAUI-XRVWZMEpbLyveJo92aKhOv9tOTxd2mgufCiKwvM36qWNWuL3zLMr_3p5sM8HJw9nn3Sixg1gKHFym80HjprFV51Pf_6tzayMkZElsGAgRHM1qawnuNyj5nveQodFG_PHAicw6C8f16klT_vYRRZHILLhmmsdj2SqMNKgi8dMnEqkvSklx9DgLLHIwN9SrR260wjtv4be5ehpv1R9iKMJ4gCyX2n6tXnNjMWeRFcqLrt4UTdXbjmtvB0M7VLK65CHt-OSH9Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 933 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7a0nYiRyw3FJfCEKm_mOFDTuc055RxwYyQpMatBtOsiIfEJHYyJ7fNzSUj-OAU2Ii0pE1qUqjyIi9exNFjfd1ujX_Aki_UFGEKq-vI0ie13GyPXtEttbvzK2ImEECaDMGLS31gnmf2yGMY5jNHUxCGYYjs9ifUat_VXH96AQ0-yhPWS96AojHmUkNbxxw5WQLd1QkAol_fUhNRaByYIWFhtpmyB13x3G6BPXQQgrbOGd0SanPZiOigDpHNGdCHE3iuIPcdHTrKlIIO4-kmZTFA9TisDzOKHrIhdJYTSR_2NoDEfWX8cfNUUU5DlEZjwhxc71wsqgB9aRVvPH7F2JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYmI8-B1tuAuph9esbYLMZo5U57C9WnvCFpsTvWhea3eI45eJGBdpN5qjNnRaJBfZFriBlbspHtiQd_Z1ACW8VfXTsV6sK9Sji1Se349-4yVqMQEWDx7fAiQz5HSBFOAqjEZ8DMETwsltZQDsXYYJyuQ6HDXJfCdvPMwL2dPqddzk61zGYZ9Um_pBEXqVJwHhcZirlisss5YvMb1hQ2CT2xA8SyzsBdSULc0IdHZjF6FRX83t9WolDAmGgDg-jMOFR7gugxxfBku30jUuPnqxwJ1VErLBeVOlWWpnu93Efvq1-W5_QoxSdfxMCzF0i_Y_j27QJ25LSK3KMBfCLifew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnZrtWogUbWFLmlG351hpf2ljwTs4QXdB45ZoBNv3C3IGMQcaAH164aCrDakS9YYsu_NQspHbqS8B1SVVpwvhl2OGw1C--iJdiGtmqEfd4NRMdFxGK7mnD0D4v0UUPbQfi0n9lWp_duBFxvbLufBs4FEnZKYKhAORZir_bl6emdr4PppcIjT7_5rAQRUVVjfZ2IZ_4Kp5iTquReNQjGWG54sy9X3Rg2-BVwZiXOUVPlpTs57kJmS1iy3apKrwa1MOqcXd3RLEVUbCZj0yewOiSycc7nrk4E8KxuirTod5Lew1rI7lMElFbq6Sd6TrVfFmzVqtQ367EQRe9wzPUp0tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 990 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpfK3VmpmXg-SrFdGD18TAOlr-ufjN5-cdF2HoL5Cvpfka0tFqqpjLl2clmH1Mixj1FJ2IHwJJScRV8M4eWFEaKswOKlyycY577RqaKX4CjGQ7hYhavY1_d7PZx4_FjlWBqR20YJ06NqjcmG3kGkCYsH7jY2pS0jcEy2dDmUC0zVgFZ7uFwzBQhBy8wus2I2apFWd42WU38smIPKlhXKHlaNjJyxKJLH72olCYVXo5JGIjU63UZNZHm0IYD22mc_Yxk8GlFv3Av2A-mjGOcUDAZuUpsWKW9bHr1ij9FRsuuP_w0FtQnCwaJGYrwH5BtUOqoHq4pWMr0uKk3gWXOzSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl_KcbcPiBJhesYhJF-_6TayfkzKiDT7UBvhRQ9CBS0QnUfoBtZoI-E6eJlTX73bXQs4NOlhIlybNWnB3JcZoNrENE4LFvoTbbbnh0MsegX6Y3Va_kJMTJooKBk5O9sLRpPf13NMyRElLsSLDnuUm9WVCCOQB1EJlGkpErp1ZY2O6kRY6YlSw_4zLJ60J_2Ei3Xo6nVtarZ4_U5Aq1aFZ1kAciKBarj5lXnzx79GuXMxFz80K7P4xYCIGyyoh1ZsxE05H2_5gBrgA8vGTojk2waltN7RIL8PrBdRw_JDxpqjH-NqC_I5GTNrjcN94TxltvFQY6GqL60I5uEZ2Fsdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBIk1joYoyopl5SsT9dV7uYRZZFepPVa9vGatCEm6cD96mtHetjYsMBu3724j2X-1kSJNyjClDIptPLp7wEXuXbDuOJIOwU-4weyIerNZMEm28bz9mjWGge_N8VT2MKeUWGtEz-g-iq-FkSvKBitDA0aDTVAResR_WSl-1O8aGzCOhKRoDZFisPsnE22gMWBEnt-GJPnnpX3djr0a80ydzzYtNguDQcpfU56qBTEWP-2oQrIS78nUHobtmgRmpxdmMbbP5EzIpMkYGcr1JQbjan9VtCKtRag8xutQbnlCoPaCDIc8EJjydViB5lEmHdfN3nAZlFRcMp5wSKCVoPYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGHiwN-q6xdS4E8lDIOAvu3by6zfp1rHFGLP6xId8YDqlfCmOI0Uzb-596Q_0dbBqgBV1jKQf55PtTidsXxoVMu-KmdQqWpYz-ucstNNuyEhRpTC9-h_7YZ5iQiCCsuTBqesgn4t_DKhJbrnh0sGEAm7Tf7rEu7dpZq-HLDsRbX3CjAhjbkJRne560jgjdQinpGYWfkc_KKgEQTwenltyVC3GgK6MBS9Z404Z13YHN2FoCurQLtF1qULG7wTCHS349O7wMLxevABYHVqyWRq3F7rvfOuQ8wJ_khuFUNd9GJzK3uuozd5tiVdXXzwYdehlh6A2pfcRhnUhvUtt1B5ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3x_zifKwOBA4kGGNe4l21_K6A-CMFEadchMKv8XHKTGzzxthqxRV4hJiMoU7Uw6fW0vhS8YTLUzUJwn3NopjWMjT2OBhh0GS_O3B5JpwQqjkQZ-l-23qZNNd5Q1yanvULN7B0p-cABg2jKfdh_QBGAdyrKLcHr791XyE9W9O72TDHkTTklxBxUrmYSUmBqm8C7TNFfYFDVcS1-RlVza5kvVG2RlTdLt_3mqYuR3bxj-zP3hw5KeAbvEH0ZNbY-30zNU0pSGg2eg1jm2y6kh8Qgmd5U3D1ITeiH3SOc-2u0CYXP4BQHJIcDe9mqxP_7erqI12YjshTfubGrZF6DQIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il6WGxRt-k3HaOlbG0yTdwhOWMXxK0jj86JLtJ9w8_99grwr2IS5dWIbtGOoUA7TfTjThH9qwfHUHfHoDLQlE8W4mUdx4rPAyydVa_ch-J3lDosyG2ChGratUYUJq9xQq423dVh5NRchi-WftdyIP3kaGBHc0BPxEOPu7OhQeh8Yd5Czu4HuWArXjU4_Lk2cw7L_EfxvOgAiaIBPHWod8GhaKeWz2M6Bd-2XoRulF9cp1BJsUkl6eDea7WLTkhldgRO414dnQxePeudrYICjYQLnSxEDyljLAu6qemv2qyniDwULvazFwR8mUwWTFXUsZsXHzpKra__pDxBRMAjDvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6o-f5-z3_VfS4lAFR02cCzeFGOGCNouXAoaX4BUZ-ZlYY2L2DctMHERHq_kDnt5NHoXtQpOoF3HDw2cau8lT0XYVjotiPc2CCsVJ165awZv4gHS6mN4x7WLJrndtsr6qFb3TD414WqldZ9GkmM2UpbLY1okyxIKrBNLAp-LT5EoWxdJ0IXAwqCciGdhkT_ItVxQ7xzWQ1guggu3PCt11UhjLyBibm1P1wzfer16HSK5tTzAz_bXyuKjaKhYXOBQ1IXiWG2MHjCeSnzRi7L_VjratgulHqAnJGP4cMMK7PLHVpY92GOiF3NQbWK5jBByN67JhmtuYy-xadv8lIFWUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZWE1cmy6Bl864mVM-KMkfyI5dzlOXRo1yoPHWBmU63PTTiw1L8Gdb8DDWufy5HYpMpC4lg6gC1MOwy7oJ9Wt27XV-FSfnucNFfIx9cg-tWfT9nlz3amMFNq2LFCyKbSvxbg23YiT4QQq3HttjnvHiNGqjO_O-KAGG9vcZV0kwASw702wqT2rSURotdFXgAZ6_j7i31wASoU8YyoHXIC4GlgazVSf0u4DVLd57RkjzAKzc3_f5mz6TTpszMXWwQx1JzsUvtL3HgJ4SAmsw9eqw0fFvxCLEN7K10YXtveFsXxOnpQSNOsE8OcSPH7hVomrBOBdkJpbC_-0m_bjxIkEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kH023Y37wmStmXXDYum_f7AevZYxZl-bWh722WeX2HCn_YxKyRonZtS66ySyhEC7RboSVBIkqa6uXXtwEV2EIc7lmjdfTfBKpneOhG2Igig0zBTpytkSotJKekuAZtj42RLU_Jgk4ksSaHfti3g3RSwZ1aHOkP2S8ufWx6OhLHaDBrYO_0FdGWYRtEbW9sDJYMVA2deqmtbMUObIv-7GB31SEg5DiK6lf2yX_SL6vA4xSU5H5uev3rbd-are27eBhR1iVCRywS2tUcxpZu15vRUe2aZMpf4Uib5cCyq_YAfJWW8q78JVW842hVpDlAT-aa-s-2PT8DOyzNjqp5IOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrM3PcOJLEkSWT_YnaNfxDPkn5cFwIWRDSC7q9e_FKTqKGsDuoW2HbVrlT7RGnae1nJ-64khT-10OY8rm3ZKBusrmyDGohHhxCHALOHuphzwVpN4z-mChKBOCJhTQxURM8pI7JiiUbqRrn5S5y0N-Rgxl4NDr23cdYAOXJj6-aDpFTkvasK8TC3YEcKreHreO3w55Oh-iJ28E2hMTzGrMx9ruebqv61yUoiSrxReipqju11HWKWmtH-eEq3esv-LVlFgPIA-1xmtI7qsiKBXxeI7dXZNc0XGRW9-TPSzBvbQWD0PeTK4L2s93tZoQ2dD0myhbpIZothvclTsYJbtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZrxrzmF1m7AaIZN2gDrDccqUEZ4fys5DojUTB-sICHHoqvMh0YR1FNfFDCgbE61665wk69fmfsZpFmwWOqMvn8akGEWmcvmWYQ9AXACgdKQUPPX1kOH52S2O9t6Lc9lZkGFVdBKEnVm6vQaxeKOTlbpBdh_hWt05LGmxad7ILZhRURkuxz5-Ur00ng06P1F3Cmq5fFvmoFimwhb_5pK-JVm2SNTDVScfnLneUGUJrUumlC4m5Eb2h4DuZdL_TGkCq9qxYCJ5inTmi-s5x3hDyUnyYRIGfhHVoi0jGe5dMWKkPhhSVlBhB3KCv0B0Hx1vLdW4BsI6SzQbVXpibWVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxY-Yjfv5pmB2Wxd3SU9nwRWDt2gZfSjLDGTLD_orwcUzmoIvu0ZLJkgEoYZvAIDwQYcL2CcYacxN9CNwM2gNuf-4Icldwirz-8uZVpKsPP6yvBtIjYI86nEb9cEFRMwr_lEzlGn5w8n3PWLoNX7waYNA1bfUTDHm1u4F677kjCPPTopLD5yCnLlkGlUcZvhY9qsN6B2IlMGAVlsl96sA5l_jNZxSPNmvP1bMAZpDN0SW4ZBdPkOG1ER5SQtJ6gQYwtH0YNWtlmot-MB2BU4s4vIPlOlnMBV39mDH8yevA1b-jNMfs23lvoy16XfEdC5InzYY9_vNyp7iZHlHxQf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQ4kFmYKTFk1cxYQFt9PJq_20STsIhMMRc_6xjllFT29H81qmfs7YH4vcj4ueKB-tew3o3RhYR7EbiPaxt5K0seHlSU5x-2NG7saiTTzzyAXvDZZh13CPKxN8JBrx-7MAGQuUOo5kcBm5D0jygdRLfCTTEd2deP4gdpY-7y-QVDzc_fiL268WZeZ7mathvWJ5h42c8zlbrUok2s8wpSfMGMX5oui_qYruFeEkebCzO7A8W-ucbekvv1hwUcl28WDkx9zp8gWvsTWu3dSvtUPRT8kuT-QhOUaBvxTyR_RR4LT91_6q3JfR3J__B44qp0Yi8YaMsLFBruxbz3uJ6mXmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guseeBy9Q6WRyaK5jafEmg3w7giUbSu5aFz91H5xA2oA13E-BFl_IVkcwnzI1RWU_nKqbxP4En5w34JCgkFYJe4znefPesIB5773w5GkbcTjpZjyNbJsbXaWJGFR2dX5m6m8-D6Zx50w9oYklRGXDuBbabzatB117E_aTaOsc_6DHjJwmYn0eCkcZxFv0l6ZULSbHtl-BNrXBMmw8a46jJ5hGzAfa7ra3509p3QKRySQF_WTEOZwff-lMM0039Y_PyHypDYfRl6IU_Bwhb3u2Gz6tOiJaqImThx-cHNjF4Kr8rS6M9138JMOJ9GeYjQ9YFRJTFivszavGfEgSh9ayA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 581 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc6_LUB3YDO_ceDeShI2PE4IfX3EVnwcaFCKL5Jpy3FnvJqJjsveeEQQylUvOTpRql264ZWr-mUfBJG1_Le76CSI6fko6yGf_19ePfg1wiOWW6BEbT4BgSPudc46SrIwDm9FNJwIWGqtMAuMAXZ5MDmII0gMPOZ3kg1Uqc_wxikQYkqGJJRmPSeIfaVyZ_hcmiVpJw3pkOCSzH-NAR6AwwG9DdCaZMzbdvvMYZrbZwXLddjPIGXbj5S2MN_PVITMU5RUArSJXulUTEfVsxmqzs42nGzKC8opzzxRK0aApWG0KhofHhYixDmBkyeWGBStuu1HxCY8faxzDvchpl8yhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoPZn8M3a1icGWoyur5xzV9zWEsSw-RjLVRdO4uvdhVb7J5vG8zEdkAhla1hS3MTgpMwIqc0X7cTo7Ms4ubip4s1Ym0Mj5x1p8sK-N80OMLegYyxqGeYmI3Yo1EbIrcrKnc7L61HaCFisGgHRNPZOwBDdJHPeEzgZj-H1nRp8D6Ls0KNA7eeuYxlzrRiJeeIMQWAT_hfcEDkeeZDlfYjDzaLolugP01hAGLfdeVHhTPEYikbPb947cq1CHTPB8e8G4DLUpKOGEUhAwR0BYYbijKpMXL9GEKJNKlmI8kFHLzVMT7gkN46YxDjSTRWFJkil8-66dA770QRwNwIwir0Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODy5kZ0p3VAiui2R6y73a8ysASvG2-W9nksWz_cqL4peDh8xXU6BQmM_Ap1qVWEcSY-PV4ONCEyoJEpgB_Cexz3zLFNWQkoP3av7AqZk04d-GqMDsQfiG_pNx7ISTG6X1pOvxntD4J5XtWI7ETmbsqyFAgk_Ru5OEIqh_BlYCCjdpmuVoVbHQBCWAblYfYUC_KcjQJCtrSsNqNdUZ_iRg9hErJkPdQdanrJd41DyVzcj5eM-J65DY-TB-tq4TXUnyAU1dkwyL6sjkQgCFZR1W9KbJn6TgQtcpL56UzhWFMoj9Cml8eBIyxadw_UVpQ56wlhaAUJ4pT8Qrq4dX5iSjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0C8VjZxExrUIPKUIK5tI62OfX2fiJYIo5jRFb-1LxXLQzvU1ubPAZSY-t_coyiWfxVBqAdDxKABMQkfUhDpqRBHCF49iE8me2TVWGBbD4V4kc0oojneDQU6HIImoFTCIezk8epGwq9YVxMZNqtpT7zF4u5EKIuqcj61aqeYyZNurVvhhFObi4_iA4-T4B9qEHwx6y7LKplr27fpR0-9ZzscDcPETIxYaB_E8jf3qeEI3xz1ouLM0bz0sH0qFAAH4zoQyOyGjiX2BNp0S2TDA4bbSarJp0sJcJvv-VPMKjg8y5CQCwiEALj9Y5cuiplZie6sqvmGFNKlMNRWATBrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 714 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXCIA3r-GIVpN0ZCt5mALnsQurfkIQYEqrBvqru-Vo051OdArTcobYKM32_GvVp4VmipoSnpHCl1csIieLjTgeoLic-5jk5KkJeU59Wd6Bc7HkfSlBBxGY_d5_-HAdmrJW4HHAnlT565tTFe5CHWGmlgxc2MOWe-tfKHxlBEF3dYUV3GA840h4iY07lDBYScbbf1fFaigS94v14YZkxbvDsO4VIN57rtvkJJQT0mOI4qSwgFvFBy2rqnj4_5wv70i8o4DBv7FtFFmTMOaiJ8xt0usO9_Bh3hJZjvb0HLuT6OZnoYaBaxAN77EY7oxi3UPUUlfjJaQZtjxZOfSyM_Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 612 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im6ZSM-BLXHzDuX8YamTugtXUQfFcU67ulP3MMlsUlXlscokIUMXDlcFmN8VFWsJlzkpOru7i--dDLtgbrzLKOBG5ryLgjgskPnf1EOeyKh-9bQww4QygnthJA5GPvjR3qgvz30XpwXi1t0b5fQ0Arr5d0SCQBTKidqSoFtU20ZrvJfV7LOUhbSts_w8iqLxPsEVNxKp0HurIdjstjbx8ZXmFMnX4wZQYbl_5B_7LVFeWGS9hD97nGbOaO4F09iXz0rBCLnB43cOzWZ6EX2bMl-p3LbC4Ia3Ev9fGFYjOEmZbjA97s5pVILNGAfWsKSp4nDjgpkrlAhwjEnQ013hXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4zJ-54Jm7H4w2Ig2UQpUHpgmDkoH3knXfvx3PvY1SxajCN1ef2MzJXPaBayeLpz5SAgJiiATjZn5_kxM5xtz0Yy-SO0C8tElBNNDHOxNlwuswHJE7DpMvlXtguOTMRowQmReyn7ORPYTKMTjBcWMKoCbP2vslQwqLHyuX9JBeACbZsoAUc4vfQxZAuj1_dfXBSwr4l9sSN5WfIgIyxray-WbFfGIWeNDfIkLhUPiEHPnMkpDsTHR2DFv2KSJ48vrqe6Zsi6uQKrn-wzaCdv0_uMKggNR-BJYcA12UJK3auJmTcIP74GSvdT9szFJP7SxLHgq_rhqO5stXrgnCGH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oU6-cSHOB3D3E97o-NB3RXieRtLqSKJu66dRGNINVg-66xm3Gg0-aZfDscPXpd8WjyWQTXg_TbgB9M7OeAFV6wLM0b6fbAs2ZmBk2Yz38phi6ANVz6rLrPmPJiLNsaApgx9ZY79yApTzPBq53FWju9kPNmK9PVTR2N3ZfTQ5RbkORAD-NvxNM7DH8hEJWARay1aWLMBq4MNe4uKalrauZ9Jx2GCm8H0LVqrnhpe-oBPSfRWhifvHubQ-1E-KKKzl60IWQHvLhm1ojpUk4xU_DjDYSATGPqX5yWqyD0lYB_-6o6luDNpBJJgCb0uoI5YuqAF7qt4oBUuZhZG16HHF2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE_ebCffblZrk6KM0jilJKrPUB42Jh9vdmaPNV894Rxa472rwK22IND8iEn31U_2v7oRaKNKcuRs8UxdzU3wDqk2lCGeKbiIwuaKEh5EXmL11hZ8QDum9Ow5yCXrdNKpx7SIK4G9KAorrWV5AvB_ZPqGxOz0z70jpf6ClpAXf56xSRVkxcZ7zQwOdrfOb68zT_UODylTiryW6pKPzfF8BmwQKXIyOPPi8H6_QESF9e2oFMjcY3uDTjvBjodsvGM0-RMzJ5nAYyaS5x_pXZAJX87lMzvZnGkoCvfvfHP-1zamLax6mf1XUegbZmy6x6wVYkhztu1tWMtkUoLGXm3KvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLxu1N0CdrcLtOjE3axa4pZzRyfOjfNNjlcGInfgwerVEYuAV4Zmokr-X1livgAHgW5U1iuOOYFhqsFazSb48tPg5SfCy3dLcWuM8tJt6fMluw0NVe6SP3AGjhDdnHV6zolVgoD9XMBkevuOIv1VFd291AmZXGLKrong3SkAnuGCz1nBVpMCld9O_C6R4c8TiGqXPHoWsijFA2cOZjvfy3PLlmOnCVKuYzkXem8Xg3oV3EbVUvGj7qE68mlaQmqqb9l9FJBoVR2pPCdJQuaB0H6UTLrpeAsL_n5HODmQ4rhpzxRZGd2D3HYEpEOt8zZbRhy9UzDNmwjR65jPQJvUdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUF0_B0gm2JFGqhpDzWBOWPdParwkRViJPrBt6oXa-vLZ5OSvuR85VEOrqATUjeblSXRV5uZhqkpQ2VqM1tbpNzOpwPbLcwvB4LJc3pX36IWQAdwb58k61APr6BtidAwm-Bu7M1WkVhY3UW_oLKaJ5HuvRuQ3Sc4UoWVvX_4wWxDITufy5zgwiDX4uBSUBr2OzdPOHh044pxWGYDTRDnN92eB9sKE6Zhq23I4g9ACi4LYAtoV4eZWHNnEXRDKdE2j5LoZ8Gc9AkwDEz1zSUjdJ1ylSFqQT1cnK5NU-bcfw9tH7Zemey8l_c0jheef8G53dkr1DpdzGpcrlN8C7-ccA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkFIw0cE-2qMznmTb4eyhU7qtohZGNyZ_si9vx6eF9NBUK3KNPldgNZwFp1nhcHF8Eanv2qYcvumFF9LRjHpD4y26L-KUJY_cuWCW-jOA_tKCNvCv4XUijMdUxV0I7sb0HlU0WJeEc8hpfmVbmI1cCrQUXcqMz-B9A-h1TXemWTEmRNl7gZ5lUZFj4d7hYvuK4zbihmqWgw-zWV9qXTk4ZR_hYYud7gtw_RsX5ovmVaoGl1kdUOG2FQPp1RKgyQ8naAThW-tDsTz951Pn9ECbmHJ_ATAus5w_FNcK4GHToYZaEiQ4pO7_zfWtzBxBP4nq9Ktd4c913M6PCIxlb6_pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYKxhzBXSxk3IerX2u0oCRNX7NlIABOw7-K4_BfiRS6VAcPZ5mM8DFfYCNGN0g1yAEgxW75nDlAWFCxE2HxO9VXcJcO07xq7zEdkFPvr-hFlUH7ydm25sVupPcIO54VfmNOAaAM4eo-okpcX7QCx5fSuEpwI3dEtHDnxEYUot3j5dM7_BPxHn9mEyoss-HOjyA_wklClIuQpJZw8Kwi6SBbpQuSNUVSpbuZ5d5FyqkwryQZoJRXYf56lz2jpSY9jrychAnnhX9mgTzrEqPOFnmUCjtUKSMtFiRnBMyIR2PxcxLoypifhVQqxSC9JJ8wqwWydft9tbvRM98C6YKAxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUT4hIWX2f9cPJ-CN7Hm7ZSwcBfsBu5RgoQYNKeewJJnwWTyW3-AXsCxFUF5KWP3pXLfcyvQ9VIMT-iW4Z5S32_DFNmrINjLH8Hjv4VDRyUZcdA3OY4cY-12S8Fh3SvWTqlGd0_Wl6RvHaN8Lgw87XVx50fUKRv5uKaGAHyJPkgdVEK7IP8HYXeJednJP6eX7y6rZ14Leq8iUOyR6oRx3ttCgPUsu3DjpJwxEoJZzs6b0T2O62Bdiz0VjyySGRZPskUEu-JCZleElPcoOOHlGWRYmFKh5_PFy42qAqH7JLkuG1xJNctkUza2h19TOcoaC16qWdncMGcbFWNAqMq_jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8G0wKAX9TSwtz6mz_oSZgL6L2UJc_qaGwDs93rRW6geOqXvRWBYdVMl6K7n2blHf_IN0dDRVTEd_ufgecCakES_lz46DRsLWG8p8gbk7Eu_kd5WsHyU9Rtdx-lb0y6QUUzQhmlB8zoMaTowr4Pdd6n7m4YF0VV0Us1RclOLX8uTiEVJTzs8-Zaqu_Ng9Nr1uVzhiDMGcn8iEVXKip0gUdbAAKTz3zS9sSBIoXcUnZMDPIvksGS9WMy_drJPlpe0I2rU_2zuYQzVpBR6fSGpZUvjhSJGRmlTnQIgltwrCN7PbSMG6nYkvBv257pjlsE8W9TWo4Yuppz-hm3vcL9tyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDnWi8sU72sc8BOrt8R1d8eJLgnVQyGwyE2kHfFjn3CfsBMH0p2h3qcgT1PqdZ0ZaJ7iG6I6pR09y7kXhA0FZVxUscfbYxldn6e3FJYoYLounVrSegmvHjzkAUEVJYSmpivcxsX7FQuYo1vSA1c-1sOkk5bB6MyKiP3uInUxPIRTKkkJKFF2mr-xfl4Pcj-7NdJbRGonD3uBFAW5hRW3N3U8ksZfdsEYMw017qSpi-fg1UuanVeCH5XyXm7QXxD-ExAxKyhGH0nimlSFDB--8EOoDMAoWNR-4FbGY8Yp5mBjqoeGhZO7_JiHQT61PWYtzsI6Mx9A9cjOqAw-O9UqCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d96NwoLsj0cj3ZxwNZapITXjBamj2asQ9o5PfQW3oV_rFZeMSXve3KZh40Qbo3WQL8VJOw0b79S9PwqVtbrnVHGd3f40mPfqINKqKMPwU5K50KInONFbKFF4Bm-JkVeOQgl3dx1ieiE6b7H6C8yG3SbczZw2gnw0eoMU5jH_DXt8jiXAxuCqOZBcJQRWYIDWXnvicDYaUWUtbt8JGmgBFAoQLi985ZDNDrONjRrh02B1odV3mtOHdd5qlMDTuHP9FW5EpP9jjmmsBi9V1bLNG-0Pglx_7BENbIQLUA5Oj1kKRRqOS4lAQtdrO45Us_QYkuTPar-Vz8o3moEu3Ic24Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHfHm45Ood6dWQKfQ-pRnG6uXVgyM3qiKg65auJCFkinX0vzq66PsXaK88ELTNByZ-AfgVRDtigM3NJ0rNc4kLyepMZEnu0Pyo9ID7tswGefJ5lLx2HM_m6W-agXCEZKsOHAqJd_5a6vlNFl9KzLgWMo7BnRnfW9yJeL1VXL4iNqLXyCbNRdW9TjwUxNafS5MyB4CbRFjQgMMupNpE1zmUd14yxR3tmqoQIR4FchCgXqHFAuPXe-G8aGoQJeOesXxsr-yXH02QqBryPjJ2fJy5ywUfv7P8yHeaR6m59YmGH6KrQrevSHsyBU0SlHva24JhS4lHNaX49NDZTmk8TQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsdc9Cift289bBX06ccxm-KOmyRLiciY1TlnLiPWzRj4BIDT4ksiujfonnLMEoGMGGhubq8R5WXDYJYMxyUtefckmgF8G9HMvxVrQXlJ_ylMpyHvs41WBgEzwGPhvLZEu9gC7uSxOB35Hu1776lfHwYzOOErBCsVlLS6t-SafyTQhggavWWNTKg1cf6m7q7UOKgjD0Y4J7TNPgBAU6_ACaLCfDYQadOXCNtzXCJvUUWrxpgvWJ_GoAW9Mn0IS3kshOM7XOXNmYt2MY2IG6hp0u3KzAljEulfaxfEOQLpUJbyXKbtDcWG7P9zgerwEQKPBDQ1ZhNu9J5FTVP4kglVIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCnLr4J3ciT1OCELxfmIWxhpTsk4ujSd0rRSPmLXDzFhow3qq4J4LbWnWN4R9NB8q7HCP4SgRkAgJng6GQH-Xt5nlJo6gxcrRCeUZeg_kuzgt3xbTcV1ZfXkOn4Z3PT-LrDm1kn9j6ArRotIETlB5iMXFaPz0gtv1nOxX4NYlj_muiY5gEpb7yW1Xd8ucGZY2psTYQP036nJpxAKrfjMK0lrtFb14RXf8dO1YubTdtJ91KY9vL0ZEBy9jBkjrRr-RAaQp2Km5s-2h298TSSsL38R6-hWBJjvnYGkZNclMxBVC3oLwiPAdMosasWyOw0IlRTrmonsdZbxzX6euIKnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxUWFIcQdvJIE4QpVmbTtfkSrsZtc4TIBAdb06Ozv5fBeGIhKg1VrZaYd2Nq4oS4co-ENU9tTLbYYX4c5y6AGH23JpWC8jVwOfGn4S4Pts2y0hcf87TWKB6TLbMVGGvPmdCUCdyNbjhLMJUpTvPSzNh3FJYwNgeTAw4yOMEsGTugUddRn13EVgiXmTJPdI7rBXTaUApwSWbChf6lCzmDFQVZnJh3mVmHGtU7_WGn1Pkp3hh7u5zo68A30xYpvM-gJJyCy59P9_qJF5qZqtWHSnkXzNIJphvBYFnrlAflB-hPRBx_McUwJaKqMogxc_fB4Ir6pzNAOFAgmOOcDldE3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4SONnEWG3iOZ5qOXM4UffMMVGJtbGfM-q5Pa2GjdF7ExbDOLCXaD2-Ah122AESWOeF8Dc9O0QZQID9YYVKvJV5f7tY3uoRZ_yCcoC_o5aF-sGw1-TfPzhPXGkcWXwd5gH4qIP-OtdqHSUaLA2Cd5E6U9st-wLIk62gyAGZ2HAdRRbz4ZkyzlpgXpXwtyU5AuYUUGqQYETNe4U_4wtWcLfPgXK3mWL-D7O8QBF1iDu-jdO_9O8KaWhvWwQh5CC-JmN_lxRyO5tXvpVc-9oNEoayP13TwQzmmsYHT_KudWGWQweBs-RqH35Ec45dB_dMVnGFLJAFs7UX4efCssr05yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cY6fhoeD4LLbwGEw9lAFgx8bRKKy9O0zbtyo0Sr01--ewUmRoC_BteTBHd_816F6dJvyvukn3Ctia-LlZvZI-qij8XFanAD91yAxEj3lRrBmNdE2TAjUfrmRhNZuitc1iCehptO5hyCMBfmSTfAXOUd2GGUveXgg0r7kOt1-JH7O02XZ2T2eX1NYLnb8k9MCj2WGTC0_coY5GWu02ruErLs84m8_HBrJdelTDe62eoUpDVZ0qhN3evCYNWdZcJ6YmtQhYENzZrZKD924qehyYECYdVZ3IXZn-n4zTFXHWug1Js3iyJkO1OQ55gXN574sDtgNp_kVxdohSx4R_1bDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZ5MR6huvb4d9OQVKQN57fRPwZTyGHqIpKvQ8b_6L4tmrfazbST3hSQN97nfgwLB07ib_Q2vKeiLFUmtIyZi0l_lV2-sv38u5QOAWVOzMnhArAOcwoROqK8Js0_Nr3rAOjnxM-t5CM1vQvPK5etmbqfAsPcOh5iY5E8dX6mzWF1gLjOzp_-3ioXQgVPGC80FElA8AJC3QoWFseCvaoHLGNpq4q2kKB0Nr_Wvb3vcxsr9JTV_klp0d2KDVOscXMXQ3SRMgzm5_Aw-1Qe9THy7CqfMORwtNsTTsyeQXcqT4NlPKhfz7-k2SLn3Fy3FMkyGEImtFjG8Pzs1CA6ZHY3SpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJP4C1OKyfTadpaLeU-lCd-28rJB_mdibKRWxRk_DG1yLSwvqiaaXlO9FPVqiNiFlmExoOFtVMpY1j89esERIywLSdN0r79e-XpbYxJ91aKhmellvqaxfDuXt9K-Pcty0fbvUbXgvqK3-SMtCdj1OAD9PFOffcu78FY43HJbZyy-wSGPccvPA7PhlfFd4xEEEgZ9LUtBUSimhNGbDieYNiiHXG0RS6pU2xUq4yFL4tfbAxiwU-khIcnhlD2WJX-6aKDQ0N5Jc037M1GK8DvSHGs6XkM1xfBNxDXNAoL_p-scwFRr4fBOVSgC_33irh6qxIkhPZHtjj9jXVc9dCVhcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ9UxPgB_tKQ6msu2MkTAGYZMDqbizOvF7XRMRj1dPL8NJz9nuREu2PmWAR_gCNEw_EMsQZHpQIG_ZZUz9OZDEvMe1baM1ZCtz6nKJsVcCURLMEAGe6Wx4QRisfktxU-cjx6MCymlsZIju4bItCwwPYfsLs_z_oXK3L9iTZzpzJxmVs-TeTcDJ9H7G-JkVnczTRejS7G-aNvLMKni1PXKXnaoqYA4nw-wSgmajiUDvw3_WkCrXrJXhBeMonDt3WE3m1m3XvOj1ZT7p6W-bjZ8PSarUWBXId4bc_1I6WnkV0lTo_Vgti9QsoUX8H1N2H6-euvTKyeC1DDdvzLB17-3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY_UYthAkDUJ1DtH8De51X9zLXXH-8asAC8fZYI6KCawzEHIeasY_z4bHsge4oGRZdiGV8eJ0G8jD5NmT7hVhtF7YXeDOmtLrOdhxB6X5DmL935pmQNZvmI_JhhtTS5IIZB4ojARMe60k5PcPrgjwfsNQDqX7qg5k3kq9tXg2CFKyFOP8ItKoD3jDVCB4M-lXPD_TE9S6ON9jCVd0myF17NLpmc1J3kQ6tTh1Mk6hbo1Sb1_vrrgZCjbdaLOAvtLYzghfOxphzhquQuWHv8FlNJkHV6GjriE1jdm38DwUa0VhK8Z2m0w5rOF0ZGW1CGsL4YLGMGkherdHA6Ce-VVwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDVB3qL9eprQvILfgJ5DLn4aQLI0yOo6W9f-C1xJmGawfiD4EizhgoZhH_A5J7G0xyOIN2-hiI075x1r4D_IJ4ixKVeNLj8CGqnmHg9y-sXPzjQi-xIM-xsbdRm_OUCHrKrsklQc3vnhxyjuoB5T6VjopznXMPUC2s7D0jkL11nfRI6i7P1FeRq2EhESydLM9S8nT9hqb0paE2TzvV-3PVt2B9vuy9-DCH6LtERuAgIGDK6qqrUzcl3viF28hywe-rpcxDJhM54lp8dwq-E5xagqfroAWerKanfDaGRgY3ujH9tbmss7IGv87o91-mqzaYrpTVIKszKdN0_02qHykg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=tm9eHKTfedYjmtqjlS14srlj7LyG6BPmUKQnw_RMSZljOTuz9b5eJy_oRXa-tyMMqZX10IHnN313xvdEzKni46tzgRUd8B7REnzx6b9x847NkxWNp952dKdYId984XrejM-uFbtnY1PDVzUrm67yDNrLc8_MAGTbIZmHwbDPpDOT83r_mnDD08fO5JVdNUXkzQ9KR8ixYKLcVzrBYA5MDRRb5LU-dIlYx4AuyXxX7gldCVyRCAog5nOAh9S5YCo3tV7SobSM6KZedVrqGY7kOSL1INq71KeehtLvvOZVsv1FZP03RxlV8Gltj6pkLPWT2wejt1EssCZPhEWU-MZkBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=tm9eHKTfedYjmtqjlS14srlj7LyG6BPmUKQnw_RMSZljOTuz9b5eJy_oRXa-tyMMqZX10IHnN313xvdEzKni46tzgRUd8B7REnzx6b9x847NkxWNp952dKdYId984XrejM-uFbtnY1PDVzUrm67yDNrLc8_MAGTbIZmHwbDPpDOT83r_mnDD08fO5JVdNUXkzQ9KR8ixYKLcVzrBYA5MDRRb5LU-dIlYx4AuyXxX7gldCVyRCAog5nOAh9S5YCo3tV7SobSM6KZedVrqGY7kOSL1INq71KeehtLvvOZVsv1FZP03RxlV8Gltj6pkLPWT2wejt1EssCZPhEWU-MZkBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTS_7JWLnMJwxYhTMLiF3lAF251MdroxcaVX5FCs4NW0ayP3cvo2RPSxi0gVLRl5Ze6I3TwOLp96tu-Eu6mEkYJyfl4YxFOeXdwb3z-jkmX2YSr5Rq1l02LyTyGCtMnq4cbuZiTGWP03dAdbWJglZ6oLH6fxoBVE7BuP0iSQxdioxnlXhDPkycWyXMOzKCPWA41sas91U0ue0VoeKXUKOe2GhxfXZ0LQ-ANVb7gouSn5KhfpfRioZOeFps78QsGFPgnM3E0Up0M8fyBybdx8q5AnBDIiYTEJUdQABrAELseZKQcHzysrHdL84rD1j7UYVoq87-2qPKrdYnw_pcPNeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyvcO4DBplitfmrCKRdfwrB92HoaI5Xq59v7rSRY6whlBeOtnozg0c39eT6GZmXAMWqZIZ8KRcWmT6gozBJ5wja6nxo9xKGrV0r0UYHdL0x9gFT5wrZTRPZSqayIT9b99C3Ty8Hc6lRIt_4X__FnWT0K21VeUJwrRcKJ3969w4FO4bLyAGaPGPm4CPvVDNENy536G-NKoetqwyuCLJQSMXScOMjfGdUNKZLEwF2VVeW11nugreXAVkF6ttHVyQ21L9QHH_EWzBk0hvLvE2mOBZB7NH5rO825grd7-PMJXBdOfyakTxxZrRaq4V6QjsE_Cfn5oC__mfZXL-4esid4DQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPqHdS42gZFewbFrR_9i3H7jxEcV4svJR1LE2Dfm1f_a_lr13N9Dw0BOGTCzOmsuq2TWW4tx9xiMU_JrAs0uNafjoLS-K9gCF6Nu4xWTr3P6lQgx1eHfKfWsGjn0k9enUBbMGWjkPYYGIuq74ZTRCAj6ca58FtXPJ9nGpo1lK7vksHBdduYPdO0fTUOShDLAU6b-4GshkiJQKPcu7Q6LidYX-RlCJ_ipijdD-n523KbCYRf33nzG1qq1E54uCLB8mJtgqdSB_d3xtJsCRx_yjiAc4csXQn9muoJCOhdnAupm6M4thmobpq4Qp4RSvfBZiUXSThFLxFi3HgbgMBH7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpZujaE5imgz0yTPUDYty4H694qfwUuXbgIqbxvWX3XQhZSblrIBWZwLcBM-WvjsKM8bvNHukMUFKSft15G6czBmwYAYgOkI5x2Ooh_hGxShRdmEKGz6bUfRNVhymz_vKwWbx86AwsfdIhWVKoFu4J29sLvkBemg74_aqIEcHUhWknzGe9dgWvv4tpTqVPhuVEwDWwzQ1lYPT10ArEExUmhZoGwNTIDmd5TbvqH3DNaF_hdBPtuVrDzpqPNmtcF3oPZKnCpX0JURGiz5WNquMo0xzfhII5SE7i-k5NIZo1OfhTL8pXZ_hbxKgFCtAsBwq7ZMig6y8WZDTZz8PuFgXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBhQqe0oLi034aFQDAa1qdKm6-cOXQrneJzC0hRXS6LpyzM2hTLAIf6D89g29rwz3_P8T2s0w9gvKKPgRcPUyYnhQml3m6zovgwSjRwHBvXBm4d80pTBnT3o0k_oLLy6prDm2vBeDGIu71ca6hYqrhEyGXT718eVYPefiaiqCylkcbbfzmifQ7xbUITksWu7QH2QT-8eWD03-f4seWBruUNC7mtKjHeXopLtRQfQfQGFCgPu8lilT1hArfU9UWZiDV7RPsLs8byZwqIrwR8EOqg8sMq7yahytY8asXvfWMm31coAs_SSyvcj6xXZhgOSjuu1abLFFkFJFJRlr-jo_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1xizzcqQbOSWH9VzZfdirW200wGyBTvDwYv92A8Ad7mNscaGPw-VitBuQm1l9dARvkyUZlUGhYHQw0ULvd3SNX3_EvCaKotWvQw9nWtzJ6E1QXx80ALnZhFub8m8hNzlPTndWsKt5z3umjme3AnVdO_AMswCMremQGoTHWelBWrnpNc40xXp7f3y2MPh_MOy5GlBvLDRIlsueQrk0zEWSjH5E5wP80jVuq4kY-UycXMcWnQGKIiILa4hqkKWQNNZ3AJWfFb-mQW2Fmxlzhp_0JUy9VH5gYdTyx3wnN1PCREunESgPzKLKm4sRTk6J7rZY4YOXI7aafNEl2IKSkAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmxrRRg_TXV76uwWPepbsQ9yKsJAaEIwYC4E0It-7n9ijbwMYP6ysmNbHc80LHUS-a7KJJ2y3JW_7paxADR2jKnpWvj17PRIaoBhfJAx1F1RLtNuyr0myeeDm3LbNXZ4Lc-lmNtcK5AyNSqek8DCfwJZblRNcnihuG3r8_vBT4maCZrYFhJ9oBBOyK0Pn6GmnKwA1qlXVz2yHNBcHnQM_HNWiGVzjLLlsWOZ7mOAz1gwM8m2Jd5tK761C9bpstJnKMKmvbzbIwSzd3Ry4RopINmZRz69FqfXkSl6AKVY7DtZzLQa38_IIXZKQt_kD8SGntz7I1zcwELSVGDx5L_vmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=k4onMhTQBH7OSwgDFyMwUeixJ_HGbpD7QnJH3prfH1ZKQqhLWgkrxb5s5Jw9ZOjgAQICMiiq6ACLM26h7jwIpr-eARne-Zz9S5z3ICGWY8odvEWEL87jqMplZmmyuyFX3UwK8ZvslbDAUV9LuNfkgyL-ravgieAXrdagRWM4d-voBAk2ds0ExRHAWyZ82SqSJ5LujAzQKpCkm9U_q7eH8Ju_9a7cfNP2qFqC_RJWjI2QNDxV70Ropj9W2c5gjFgBY1_slLLxwvrLyp_8jDq3E10t8MS2Kl87x-_vYbCUZcLvQGB9keA7SBgZX6sFaHvu0DDxQHZSl2BtwQQOrgnjxi7GXsc3u7NVh3jmwV55JMgLbEUS3dOj1q7I8avMCIkImjc7Yqcxzu2stYAj37DnpwF8rnfMfCMGuWK_k3dLrYiUBbqXZ6yfD5tr9WRgT3MxEBslg541twCs11RzxsGEPMK9eO6mM6S1DXPgS4pc8WoBVOE9fMrrkfngx0neeZp61v_LpcVeXFF4Az52OfEvmQWEPvrfH-AKMVKOL-sxLH2dqhxQDfFqjLqTsWhoib_Xv9DKsiMnFuF5bGTurSyMqwNH7yIEnQvK_Ck3OlPwNo-A5FLTcgI8cbH53kdW20uCFoYgQu0jSJ0m7UyrZUfD4N--BuhBGJnA6rHL2v8nsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=k4onMhTQBH7OSwgDFyMwUeixJ_HGbpD7QnJH3prfH1ZKQqhLWgkrxb5s5Jw9ZOjgAQICMiiq6ACLM26h7jwIpr-eARne-Zz9S5z3ICGWY8odvEWEL87jqMplZmmyuyFX3UwK8ZvslbDAUV9LuNfkgyL-ravgieAXrdagRWM4d-voBAk2ds0ExRHAWyZ82SqSJ5LujAzQKpCkm9U_q7eH8Ju_9a7cfNP2qFqC_RJWjI2QNDxV70Ropj9W2c5gjFgBY1_slLLxwvrLyp_8jDq3E10t8MS2Kl87x-_vYbCUZcLvQGB9keA7SBgZX6sFaHvu0DDxQHZSl2BtwQQOrgnjxi7GXsc3u7NVh3jmwV55JMgLbEUS3dOj1q7I8avMCIkImjc7Yqcxzu2stYAj37DnpwF8rnfMfCMGuWK_k3dLrYiUBbqXZ6yfD5tr9WRgT3MxEBslg541twCs11RzxsGEPMK9eO6mM6S1DXPgS4pc8WoBVOE9fMrrkfngx0neeZp61v_LpcVeXFF4Az52OfEvmQWEPvrfH-AKMVKOL-sxLH2dqhxQDfFqjLqTsWhoib_Xv9DKsiMnFuF5bGTurSyMqwNH7yIEnQvK_Ck3OlPwNo-A5FLTcgI8cbH53kdW20uCFoYgQu0jSJ0m7UyrZUfD4N--BuhBGJnA6rHL2v8nsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI3YA4RlYWdxqLES4sHFEupmmZ2lOtmOI9DBOjyf65oePXA0K-udEBzCUFn4GPg4iScDEODCDhuX3szJu9Qrc-NScU4IaqgMxLdbX0IUVJhGdwQlX1g1jRY8rqi0KnbheoMKfvIpPQ89kHElAOlfQsFcfyl4pzra10NbPiM_LLEMy1HsoGmVRztjg3y17K0eiGr04KWWA8IsUkT-DlwNlV0uMeGO__yASjnqEZClhQc3_N1pwLFoEnCTcbyOgok4z6T54nZYV4-11rMlfiV53EQuCr_VBD5cuu36t2TSe_Tlr-RcEd1AsMn4Qf8NSMibpU6T358nR6aUMaVoUTv0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW3sIGt_XK3ssG_ukAjRAfvuwSkkz_tlF1Nl9loUpd7D1nDB4zHyNBEodu3EgLpfC_EsRqjuWocZBuBYi481gBOyEnYyscsbBV0wBaPJN4OwrdCStpIz1Vb2L4QpTMVlzGk5xPiKcbYlAJPw8nBmICDnCJ5FPWpcuCEyStFgFR8R-Q6wWpBxkhL6j0EHHtR1Ig39Up6dPFox6wOa0h4fPSiYk7TOIZgTeZUKVAA22zFN3OEYuy7HGfqZ2Vt20Hj4teB_Z-mD3AuKx2F4OU5F3mrvaFnrWDETGegC_Qrq1UQiGoYO60wg4y5zjaI-8bU_eZbLHc7oVatdB7VqIIuc2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDbi5j0WtPj5clFHqqZyL8ghrRwHcKHYuo6Qn3rygCkUwFjCyI5Q1pn7H8ozldjlRkZ4w4WoWZiAlsj00Z4GbdWsUA2hJgO4saK-vHkXmPVXKjj_zibGWbvuw0ieOKjekClzdtyq7Sq8yI6NnC08Dt99mDpM5TJQfQl3BV6vEhZYvXH3p-15V0vWqbqsCUojbXGNkmOOm7VFHnTJgxfC2LX6X2bQIm10xvT_N68rTX-9DsMhBLGONwO6xn8GAntvLCLuEW5MENYMu3iGVBgrZFQ0BKAVftvMN-xvKib0GGDMV6UnMhNG5sn524oLYEpHbujg2Mh73cbhgunw7FpVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXvSc3RaeCMVAAphCjHutAaMYPJzfvvt0SyUjkEgchDxKt95oLU3ZBbXtcC7T6m7i1eTdekUe-0ND5YvoW6oFm3hf6L8c4T-ngyBPUbeCLgspV9DBMmj4ch1janu3EIMC_YU0Ty_Jw8WSpGyWGz3ojR7IBQxO2Ubn_cbDKj1CbO0CLsqoYu0HuAz6I_N2hkxKa9Rh_SlW7iPXmwiSrge3gMoi7fYEiN0JJXtdfrLzdbi6VZOt81bw1OA2aXjEhouPPmhKCRdmqvTLp4JxmUkPqR_epYVfSSq09xLdQn6ALjaNNKNl-Qz2FA6BAaVFZLlHqnf4mr35n0YJxy3wG-P0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iykAarUkqRb02dixb6Jea8FxurHub5DcfqAxaLP0QUi2fwMHV61rv-1JivqYGK2qBeC5XTbdetB13t3mrY9H5hKh7hpU1u1540HH84OHmBeKIy1MAb_BDOmlmbi86jfsX6XoVlqt4B7kF7IKJ6aXxRP-ivW6zaNYZVHVcNVzeoUdXZgevT8Fhpc_xDjVmOVTFFT8sSQ_vplRXpglWweMMDHS1dssuoMn9nFanirLET4pDlFsDSuQxEqBn2oEDuz4kM6GUPSjgYB6KQQxA39LoKh6AUI_PdOR-VSQ1u9jgJV37uM8eRASOQkWp76Eb_oMX6IKYQ9OxOXrXCc1NxuN0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUWE5ERrA0pZasbyEdpdXfvl_wURv-ELl9g-YL-pAhOMRl8lXs8MLbSIIhnaR2il8qqocP5lOCQafSdy4ga-H3izAp3-THduBO6H9q5Z6DIAM0rdYvf501lesUTCs684I-nas_CHuNHwVdx3N7mbr5dZlilb0SQTROGiRsTZT4qHL-_qqRBjOaWD0Mqrts7Z8zGgd6ga6J_-sHlQDzfptoe6T28AF_kqAIsTolGQPxdOCe8qNpdI1YqCBAXU8YcsfBnEVartU9VpF7qfxxHUiEnow1wWfKvCZJ8qDKYA8pW5nAJU9zkG7Fej1IJJ4SMM7_bg0m8k1vmjGXtOqTVTxbsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUWE5ERrA0pZasbyEdpdXfvl_wURv-ELl9g-YL-pAhOMRl8lXs8MLbSIIhnaR2il8qqocP5lOCQafSdy4ga-H3izAp3-THduBO6H9q5Z6DIAM0rdYvf501lesUTCs684I-nas_CHuNHwVdx3N7mbr5dZlilb0SQTROGiRsTZT4qHL-_qqRBjOaWD0Mqrts7Z8zGgd6ga6J_-sHlQDzfptoe6T28AF_kqAIsTolGQPxdOCe8qNpdI1YqCBAXU8YcsfBnEVartU9VpF7qfxxHUiEnow1wWfKvCZJ8qDKYA8pW5nAJU9zkG7Fej1IJJ4SMM7_bg0m8k1vmjGXtOqTVTxbsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed3Z53cwq8l1Ye7CjhGxSE0RU-3WMZfwwte1u5oWeK2Wq8krKsieJ5YmsbJORpLKlBc7ycluwjLKCijJp32_skjpLsjPUaAbbINgotMrVKUTLKZ_AglmzDRRHvrQ7k-ZYCFn2-9obX9A5cg5bkvuXecDQGXKuTaquQCAwunp0gJX-ezHoS7zwO_MWyty3pQ_prPMDq19YaUUJ1N0NQdwpSuI1pgiw9GdjmIodq36vKXqsBdNE3XniOieiLdJnMaJ0kUu0RGlBEG9jOIvgTuzCU90x3wf65OTeN8kE81XX-x0F1oDV8Yo64ChQamg9tzK2d90Blqkdycb6gkzJRjOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
