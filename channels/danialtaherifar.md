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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 191 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8hv7vOaQzEU7R_u_1UDSAvPQ6IlHlY_sIEGXL1aHT8rEDVl1zorxER_XxxUqlO0dFsn5KP7GvqFSovsrdEgapxN4yo8mWKou8VnrjyObEZW8nKsI_NLH1cwm5qtGzNfoypoBTL4cOkUMJBSMtDfsUwzfSELI5QBGkk1qWwUOc-8HdMHqjKFBWrUuoKhlhKqJXKlcw1cZ3QVqfHbnEfjq71Ey-GxgVcnjQT4ZtxnqSMAkZBtXZadVGLmuXJBH41unKREaSQE4MktkKAVp1_1M1QoIU0-mqeKj05I7QigRCqrBvK85cKTSRgL72OWDjNa1suyzbvzGFVJOnhMHGXjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 443 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 614 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 731 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 619 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 845 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWsNfi9jRQepCX1e5gDV4QqApUloUqiYjFkhcB9BVtqa-JrediIDJA9RUoBE-Hyf3g_G_LdT-j7whZa7jDreMWvdNpWL0q-aryu-5GUzgRiIU95JmTlrAUhfuREInxYeP2n0m8I8sEjWwqFsVF7QliMoajqmsnfkayNOD_EpjoJvRUYgp37nCfaFJRPUePqXdJw7E3FcWag4iguF7mPcYS2s6neOROx2D9cj_GNku8dZVl8GhtQW6Cgjwest8hfEzHiYtuJcy8PiGBADCpNTcd9ocAa0M-R0apmTt3cTN4hO8FmbDL7SFcPIPudtDwr-I3et1Oj5Zhe542VzPe3skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyEhozztnQ2CkiYC3eZITlgDr6qxYxg3EwWslEVSoqDJCb3_A8XClFp1IDD4LqQpyW2cc7e3Zbi1ElnBq-vjwRrRTVvfytxNSi3PlJz5JMZdEJ0_d6uhRJbO5JwLKellZHMUbNVniiS5FwNV8xPOmSDpaGRRaRU_jevFPMYOO2zcLb-C8UFRu2Im6qhIe8bOjAcbEDC-c1_KzGOGx8V-DDUjHiahasHUdRf8rPVjK_7gnaAna7mvALbEfacNvN6sQynsuL537y5yjmxaIKYrmCx1wRp5qL4rEtKu7H0s-ok2US7kqRYEkW_zMp-LlXKJ30qVlbtFpWayidJX7jLeNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 946 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 906 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1bfLvwRS1jq4zTO7zf_TpVTD6w_HujrFH36BY7OhoZQLoYfYaLZP4jYPb7BHxIA2TZOt2p7_OSIz4DQm9PiRC65Oz3rCvhONp8Tk0oBkKRZNGRxn_5oWGwEvGGUDw5drdBTDI5VJ5yGtwm_Fz0_OLeofpuNTVTo1ArRMRgZQ6Wg1dkwdycEJDpzhsFDb7bZ7C3IZHVbUQ0xa0EBN5tV6UgW60rXs0mfYYgpOsD8xPCOzWZkx0QJKjnNs5UeRDhzkEbf_-1jgbIbYBKXzs00LlKrUygotl-3Yz9O6GqvsHW--GbRBUKVD8PV9yPYev-D5mL6Rq3NaFkwEKBIIHw1Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0qj3r2ecHEplBhAHK9Qsn4TyO3rsUgetS9tLn44NyrYSj8ihVCGwFpAqG1YwxnHCwkGVFNHdbpoC7EReL0ruWqZm_KMCc8OYuhmB_Z7QJ95VY5uvWryErQ592lJgitkyqD85263yWvFCUAr35bu93RLBhbjIShT6VismKgnK2leZBDTn3cUsbDjtxF7j5j8Rn19dxcADU5cgJuJseA2oqXn8ADMpEgp-oRoxmwtiD3nNsyFVLidVaE51eZmMtPmMDBkLBBbhJQQwR5fC5SRaUHaaLuFNyEIdBm2u_rEBtrPIF2rtK_v7LVPj4kCU0JVwgfe7_mzu8pQ1w2MllPoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrMTUpo5HklcycmbSotmSdJmSJSEf_wiiiuCVwpQn--WnwTYooUYxKE45pemmqm8xb5WPmRKBzOX7uD8uyokj-J4APXGOVScyxTljLzbGIzsSgyxIFC-84H31zOYAcwCmz9lJ4-YrD8pXlQ3F_bfRnOcXtYz1LmxZV6tZ2m9Kok5Hr3JdErPZ91x1yXuBzBEkNd0OPvPhXP1InAR71zuK7p92f12LUXa3_f9NN1a4LA9gmWFaKWi8n5NKZzfHzomOLjfX8INkkODDYE7Y2D-wC8-fQ09mnYYAcAoDXTWe7vcx6ALrHBvZxtWt1gpofcvpUtH_tCZSFgyzJLOzWYaMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVfSCV11Mbv3hm2fwj9WTPf6YL-FlOOnslOU2a7cTnhl8R2p5_q-KMWkOuPXwbGvYcqMv0JpQ2Kgma3KF7tfon1spg2odx8fRubiU0jkKZMJYTcv-mjf3FMXm_MvZlKsRIPCt7caZ8ThiqhkJq2pTx44U5UiK9NZjS4iRcJUFl9s1CmvoirNT3NB9BKAuf1bdffW4BZlgUYHwgVobzcejSWs5M1Mrudk-88jOKSG43Hkg8ESV2vISvBZaC4tGpmQ0FAasAcAK7JoF0uR6trSx-XV2rR0OpEMRIkXgS1k7hut26NNN-HJgmbb-bqfmWqQOcqRKgjRmKcupiWhI4enOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tInaGsxgqg3NlB9gax4-92qqMfZe226NxiGEIoc9Iv496PaYZDhGaRZkw1xu9s_hgitjqUWFuwfs5eH-JPy_cmc0behgzh6WQEFIu1MkoSpbmXsqX0sARHmzihRGmD8MLIZrJvDYiPNrArA36FDENKFrmdSL9N2lhmJIleCUNoV5G5R7-pymFeVFQQb20Zo3sVgxePqHCmNRKrgHNVbVampKGYIJOgTAD_dP6uEMewlgXDWvOttdE03BFYoRaNi7vQ0llvspt7DK5_tN4sIzoFhsqp57ztesY1pVXlt1avPgGQJ8BWaZ3r2Rmor1A4BeKX8QLVC8amZ9s6C9M_joXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqLKB_Kg_QtR0Z5itm0niXfF_aeQ2Jy7UIfvS64bua4CHqdC-zALg7Zl43wHEZI1Y8L3TDOM5mq041-7o7waFcz8K5BumGTXX5johqAn5JwqPpqYvOJlxAGIGPL5S-ZNslv3vtPmp3-15EuouRbPv04NSBqT0oNtxr2v_wiuxZ8HwK4byx7rqwTSVOBbPcajJrQIh5N7FxLFfRjSnC4UJMBZ7A4TIWHzviUrqRwk_eg2zOR419PZRDcy8mtSHMpZH_qbZ4LwBhfEhgSTHq7ZJYUPNB3odivBmpWzKy8utaAz5dX8Zuv_6yUKRbvnBz9yIyqZot6x6eE3SQ5TWqqWfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYTgg4JjxcIgGF96xNvzXnP9MB99DNKcePkUBuevXXK_enJt6yvSGOUm_QmaTFZNuTw913P5p679SqgFnVxRsSAuPA6PzbXOBfjadSBe17xkZXe7wB-_bVHMjWPnwvNq4JGq05oUY1PQW-K-MOSkb6oYECoQ01fcGCw_UE5ws5SPkwu17NkCFkXCZIeGzycyzWuze_J90AwN8k-HvwjXzSthpmjfjICQXM0FKvNZnY5a_WMDu4GIK4GM3YBkS3TZu32YQhphlp4d3fGiks90AnWbi6tcuX_ULUZCQsSxGBIonaZjSf6KzCL6XlxhCrmslp3Ua9w_L9Luxl5o22eG4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eswwzk5b_xJforee-vUF6jdJhpifFq2X681ohYfvLnwgDF7uRLGvutjULmOGN7z_oi49UDkwYFohZfHzq_-IVDbjVGt9a7sz3tuXT5DkLMvpgjL93Wy9_2JTnpMiR0Y3E-tHNI5yb-OW83zDZKMXtP8SopZLsCuE7gMit70Zu6L_5uraN-KvSu7HRe0jCjQN8rsx0Vdv1wEiK6h-UfaOoC2EYpm2z3aAcV7POueGBiVIfisnkD8TN9m72EJKp6PydUwSWA-dSAydmNK-l6kj7BiVr8idiXWwGvGlJKIKS6Msdg91KRX925tm32OGJ2eWqCTIrLEWUoDsGot-eTUuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAM45RfuWc7YYdd_-D0zHAPkoagWjbmKuPmhDXV3Rrn7D70p1u2oPH6LYsWqSzccs8iToUAe2l80AF1vrzIbCip5GjIm3KGA1Yrz5G3h45TNjt1YNda7XmbL1lc5f3KpdjP9sKtNF_mH24eP4gmkQrx2j_sv4zMRqY-TXn8_dPV5S8ucA-re3tFSffn1R02rE8QCtOK7nOau37TnhCnIDPsVe_PzlLZODPu3KdH2fkUaHGlxVxAlUXxGmqntwWMaRhhzATKwKVPMU0YD2AUWbXKAQ7tG7-PhHG2LMSqr01x5mg9ASiom-qLm4hytszXBYc6fmkvJiUxTdVY3N5zI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reC3YesKkq8sNwuN8Mh0k_RtNJgWqmCE76kudHcNWxq5cQUVc7VDq2XfMZrjogixs9p5buxXH9Ekrry34_tP7kkD6A7aJjrZGAlZxiR4Z3N1FtgrEvfiAV3p4A1tH6sqy_3FA2xhJdCKbDSndRShXJ1NTDS8taS4oP7UI__N_hRw7taw-CZt9As2EQF81a9bqjAalLj4FGajsIMYv6fZWodZdHRsyPHpsxST8peJur8YnCjcmo5pMtXkrIgo3w57Ytg3hTGMJhnA2fACj7TVLSvpUMFLTFYgr01WByBgJaYd6iVmDrlYNlGduK4FWLcMXY8LVx51Js1mRXzztFpYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oT4xhJJcsOFX3n4Z1C_HCWkgB7HA4MP8YqrJA63vNHa3vuUlYQE6807-l0DRiVu2UiTZIVi8To4nyCPB4mQCDceiKXjy3ZlIcU8L43L8cGcegWoRH8MzapYk5TzGumIkRIQpYwxZAIX--5-qOE7M2UbW8LmiVDyFepi2D8mhUF0dm773G8sErPMxTQvvhZ7rK6g4TYP4Ua4lfUg6kjOwObhSoWoxkz_SugPeKf2gOHvmbvxyGyMSl2wYyLy4GNH0QiDpUsqfC47J5vkhstlEHqB8oeUxIOxSCSB-BeaWWH8V4WAjpTpig5pA_-7cE0pRNe-wTIuiwCFuKWGMHEzHmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBcMJ3PXrwE8Is-ovGg3jo7H_rC1HjaJf-9U1SQco9aAr0qRkGE9CF4EKqm9160PvuYwSjC9V5ZAXpjT45MpfmU_h5T6820_f_MrtBBuuR7pVrIZDxvXcd6zJkv6oNjJJWOHj63YdoYbQG18_uUB41zytJ9qsLlllYAx5dihyKUCAsVpuZc9TK8qe70IhZLJD9VQMQmO735uXhO0407UqXfv6yN1o0GggtYcurWDrG8wR8jPkYCK1_y_nDJpuG0pOgupLG93fAl-WShYdT-VwO2z0HJwANglefmfM-wbt4IlRFTWjI0IzYOLupUdFaLW58iJrrz6erhoDvRBhpX1pQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=HXwcdf6wr1Eo2VZyRDNBAF-aPEhuEGGW_00z86FvrNF6AGK1fW43lycvfZYAFOg3wtTBnI3YmcH_1Jd4S28rGU8R3uyczcLpAG2VAeEb3ZDBJ5bBsd3wIUxC1MGp9fhIiB9cjGxq5UcqqIF8qTTxUAtap8s8D3k0ErrQ7jKWjp-4Xh7CeX-LzWmP-95F2iWe9RmvdhTjnu4CDOqb9buxVhWgpb86YZd-PBLHJ1mz2gMJk0bhRnHnszanE_TwnRpTntyFtQsNY37b4R7WSvbbAHeAsy5bp1BeqDTMiEKiGYwve3QkJ4HPfra5XEOMXr0dYNfpyU8M4Z-ee9poMrnCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=HXwcdf6wr1Eo2VZyRDNBAF-aPEhuEGGW_00z86FvrNF6AGK1fW43lycvfZYAFOg3wtTBnI3YmcH_1Jd4S28rGU8R3uyczcLpAG2VAeEb3ZDBJ5bBsd3wIUxC1MGp9fhIiB9cjGxq5UcqqIF8qTTxUAtap8s8D3k0ErrQ7jKWjp-4Xh7CeX-LzWmP-95F2iWe9RmvdhTjnu4CDOqb9buxVhWgpb86YZd-PBLHJ1mz2gMJk0bhRnHnszanE_TwnRpTntyFtQsNY37b4R7WSvbbAHeAsy5bp1BeqDTMiEKiGYwve3QkJ4HPfra5XEOMXr0dYNfpyU8M4Z-ee9poMrnCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDZaPdby9OYrWBQqA4ztTERqxuyhdjpREVHFT_iHOkXrKuAJeqAz-DsXP2LqcyFzsaZQCyUrKRFa7NeDC9uhdlQVSNxVQFhsdskOl4AfqDELtEU42uOWaV-IdCZ02dBUClmVz6sOWguteU27A8b5UlBL0HLpO-5JibOpTQkL0Mbi7ItRI70cwhI76E_JT7KobHLj4J9dzYe56nJhKEvOG4gpFOwOk4WM100OPlF-JnB3F-oB7bofd0kgEkujLOq_CEhKJBGrA-mVPKlyhS19-O2S-H33hAbDh_11M6BylgY4j2urOqB3V9YQm_u8F5WSewXMq_hgnh-2V6aiEuchkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ-bICf5tLgrdz0ex--Rycc04ZSJaiIIVMTfi6wxYG9nq_T0y1sCsrYzBp9pkAdsWAYCPNq-VjCmbuU2AS_LojZTDvSBNGSB1T3b77NsoLfF-suNtl3dkl0Au50u2mFtvC5yJU1t7XQ0RlBJ0TCwFQxhGsvb9uaL332j11QL17XwznGOSwK096iSkfBr09mTI1_hvIh16FZtDAQmUjHl9L9wWeff36ddL1QMmYWs08BHpPIgbGYLUceBzel_fCxw5vbb91j-nubCvFvB4LdwMGdneu4X1eLaY4ZFkPDUf8p58a4T0zU7tlmySonHNNA7jEqgn7Z-Qswizd3WsdjZzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esxkQuuJPCXNwlQzWAKmrcVYGMHoBt_TLpu2cNXCZbI2rz6V7GrsnXYbAghmFLnB2P-DOClTWYWjW9xAzZqR4_N332Qlji4S6jq35axo16TqwfC4jukNsvgrqa_OYfHDj6sDEV0UYnReZYigpKjFRtGXGrn9qvlSFJddrDOf8d3HtaGAZShD8wA_gh-wuhCTi2dfEyFjxYn0iY_6aoswkvb-fGCqVtUxBrqWHMQtKjuF5EmA55LZ3EnR7iRBjmNkiwhDiDKJq3-3XqNJAYV7HzOCFdy76DSJgKYZP8jjNHLKFyv6CNWA7LqDqyHjzuvOnby384G8hMWeZAGeBC9J7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBPBsfzq5JoGtB3iOJEKZj2QtD5quKxlx3p9twW_HmAL5vApLpo9YjIF7S84gedOrOjPDHoGG9mQ2Iu1pLf3CA71336S8hHCE81tul-07XmQMNQpHY7etWSiaffXIbMk94lr9qz9d7kXNHV6udMz98yzHdbBsUSRQ_65GsOOojFINul8krlVMRBJFImLieEvgw_5yzDO_HkNXsPCMosABRxtHeCQUGu7at3_J8Wv6a47JfiqsknvV9oGlX4l9hfZwoag-a1JRVAxw9lQl6voAnBZCmMF47eiAbQxozOfLn9FGSvi5BQ0kXWuCeOP-wGnVen3jhunjsNfKXYIkL5z5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvbdb3Dombk3WLENFMNKU-CpwfYi86LEcsbmhSMzXXTBgz3sORPHV3ZYW2pfDb1ThmzLVPAj2SpTeiLulJUZ0hv7TKiqt4cXv5vFp82OIzD3ydDP3HNNSjtVtEYIo9HSUZUiPtV1zbyKUy5Jj4dHP0EV2Kt_PK2vGvdNcgnXsZcyazVGTKQJLqoBjzVhj4ypgMNvm62876KTGhdscyz8TreUjK4uBY1kN5SU4gVpVN_KLzXxLcXeqv2NcmuSQOEUYk5OqvqG7z-q8gMc-RpX1w8mWLWrNB3G4ZqQgj0l1ahb2_39ziInd502-e_YLLMbPm-YT_p3KePuOi6ogeAuAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ9r83jKpY7sdACccpBEHpgA8jrsRWza_JWMh-PmHOhsWD6ZqohqAQtqF6kf7ZyLGur1geuj0uc-Q3YxkBczYF47CaVZRdq2fb3plHc6ElgFyUnuoRotz99r5jimRNXfEh3PmkIHlznPTypPKZd32tvaQ-37SCsirBupmeuS0rv_PHsnr63yBmGjbFqxkGITMiea28anSaqc9_vysAJyD_zEky3CRAe-sB41xDhPrqYXpWLlnb8eKIl_hINgk1X-eNy6uCEtue_R-ZsiznWCjZv1ZpLJYGWcoboHSFofOt7cAQ8xz0wl552cH6t-Fr0BToswNA3PEDxxrHvcNYRPVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwDQZPK4H81vqtdC2aEypXEQ_8j99HVUtDdWTNgKYWUe0KFTdo9gFWW32nWmMNCHEC_OSxWQIxip6sHuJLtexnWZCKQmliEFdFDZQ1CySQvHga8MHczKc17oKKgOWWD4y5QcH4KDBFmPznbeoTxfHApO7Dw9VIFXjZh7tBmYgsBkyXVECBQy5-cFV_QJTsM_yK1Z84tQ9I3RGtmkBhzy2idxk9z4hNc81cAlz0BT3jxFzMNcRtWsz26sOO-BWgKxmm0naicmek6I8WBstwlu529Qh2KLQdmfanrjUUgXaZKzzwGH6i8Lp_du6Ysas9zUTspfIOaW9EtjP2N13ZhbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAuoyT2g4KBahQr_GvCYuyRw8VbwekCz0HIgYobu_4T82Vhj9oeNPclQT9je5rai03-fuTIiQJVne82HBxV9J7y5eHPXXxYnOIY9NcHmLBoZgQhwBLQgi5u6eq5s2jMaXhKZVwClzuPXQkxK1iQc9N8pJi1ts8GCdis2iXATG7ANX4DBrAsWc0W8vOrbYF3vtaslgC7iOZN5Bm-t46W9hr5ft-K32MjnmegkDXL1PHjBA3qGf7uqz5VsZbkB1ptb3nIVSTPpJtRT1PzL_zrO21hWObci0N6B9CzsE-8e722x-T3WfXF6sujRsLJYPJOJdY_s1fhHBuEBIOy6XqP25A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeRCn_H751I0hhJo0CagCyrbHvJoXDUMbpQ-7xExvGA6BXAOA00fT-xU62uk3galpWXvsrb-vGbIZ6rRhMSc9lpdo7p2AfFnmdL66MaOsF0uScfeW7bz__2FoDn6EmLigCmpZOVwJAcxXzmNmG3cMj0I3GzyCwfty2LEdG02pRxjsGLSutLShqz1qz8LZgv9pjrStzSAaAv5QSrbaPOhNLFPvzBqxTRHR7vd81Hg3sqH4phhygM8QoNiXBsklO8F4oNG6v63Udop2enWW9vx4rqSfygV4D_Y3_ZYOkDv_yLti8PfXXSoeH1J-Qt6t1E1UUCaQmcyyw8sYmAfQGzk9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDzWmPk7buBQCJ5zbzZkOtdJrExHjZmmVXfd7lq1CuxAbIHT67p14XQuXT6JKUj9TOMgFVqpeC0N7a__pv2kTrFaRJt7OOjEqt_F7sfDhLrjZ8EpQVEK40CMOnAGB78ftvfnSTsxNOgWJaD27gsPX2-tgkZxSM4BB_eEl3UEc3SzZns7an0JHLRMBS8ey7leI2sDBhU7CC26QBhV4DmzAX2_3KX_3BoYkpm4nWMq-f4d9pbbsRyDOLi3m2vKhutBzD0kM5phSQIDxtOSr0h1psJC_iw7LFUmSp1AgyNrjJw8-0WL3YlQpJ0H0rWBAlIPpu23hqL8nac5qlHTqMdFRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgLSayEgGIjncsMyDNVC--m6_YQMAOzUUMWXHAZPKeAeYaGwIJP0xn-BOQ01u1h8T5gjtsnkcgTY3wHxNlmYLsUrzoIUzSybFEefYh4DWomh-T_Zvy10AOL7FTPjHl1IoIKM1eL67xQ7-urLUjm-4w5DiwoTLpy43dGMtXkBoP6UpRKHOdXYg24c615GJLyO8aTBCJ7wxKjXKHedy44sHAeQgeGRemnW9Bx5oVUhm9nh8UKAJ5Vn3gjPy7qqhW25jjRugq_jolkvHRmk3leVSXF4WXca64vljr3K42m60JDqAbsB1WWgTIHOgUbTak2It7B3WwuxedM9qHwJAk1rig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN1aOIERmXiOGP4cjkrwdqsA80FOCzF6EqNc-5lwvkMxcYcFWwqwnjxRavWjCXj4_wrw3rMjTm13k2hAifnpEOcnIdMYDgi3FL9ASD-QyoEwvfqKC7CaQp9ZnKSCkO4eiDqOCsSAoqXMxhtMONqD6TydJdI4psUXXQUwICB4b9U9j7KksVM6r0Kn0DnaTin4pAIpJ1pizWSnCsUKnlQS724-QOkOoHlXE5C_rTEaWR1dLCkY0vViM1oqGM3DPmuMTvk11zeOdXu516RbuVTqpZCKpH9dcLgmMtkaVjO0aP15IWsh94ce_lCaZ6aHffYDm4F33Al3Kyn-qng9AT6NaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBB3xRnxZsuipx89QjpCP3WuocDY0p8sL3OrXeXDEJxH2dV-uDGOOXMPVt4l4sM_R4UTSKSAWMpeOcz8v8BIXzxSbcDKCGBNg0TnYX4j91nxyHx9--gkX42xqoJeE6o6HjA2KyDg6zPRVql3txwnJeeGkqx-sRaIGSuk39w9In0In8Pf1pcsXOehBd3RArvRSnO0G5nJJzAmOPsnPbepsBolfxzqOiqbgpyuj615-o9-JhY9Fmupg1Vlpeki3wel2G1nFV-stsW2y8xr1dR3n8z6LQLs-gb_lijcWFGNsQnubitBYU12QHoLHPn8kw323fNtvCdF2TLIi793wRH5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tezMC7XG4sCxZvWZoACwChVCGrZLAWY_2Y1jaTZ4dA9yBswsV2GcOge_zVmSzFzk4ntVLPKtjsxCAtsPlgrOIYAj50oHPeMZ1TcOBE8uxTIJIeB6QBSUcxJ1zqQSfmXsdjgj7aGoJEpUg9f9wNAt-zkK-lMd7sEtsLsDEm3Nn1gdaCg2H9p0POKyd068YqgjixHYT_wHalVfyn4ZxwT1VTuSXhiXHRHEBb689tCcdcmU9ewVS8E2KXKXD9MRD9tWlY10AJ-1gpZil2mFBaovOpFYR63YL8R4rG0iob-S5QHFKWexUYI2FfwVQymFfnVd8iSDhoIdRwRwrrCLMCPRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PngfdliCLK_Mg2n99mas6ZwJUf5Wt05NV-cejswnygS5hw84H6ko4yiR-uJXFcpFL-S8BwtYrX81KtADmFepQ_HXbVCTbiE0R15aqYZQUfebVw4iEpFxaYjd4OlcuhC_jIz6a_luNwRafqTJ-C3097eEyx6U_iuDeJtIfNmpm0UtLpIwsd6ZHdPYdrsCHs7BRXtaJzJaP-M3vJhAOHw7kw4a_gk0iesGDPQCTeiR8in24tGYR56NYOOYe1lhO60U9a3YmBjI31QAajH7lpOCsxcgnt3_FgIrw6ZmJ5bpY_vPG4vDV5396pQLzr-6740noiADhRIuNb4A656I_5J4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaQyd0y_b1cpu9aBFexKGbNP67KBXEYA1lKlDudu6D_cSGGxDkqtu-FDC77RiG-GgPO2bRW8pEiTCixx0LDYKoTo2kiJt0YbDnEhZ2mr4LjdpnEh34WkiZdsZdsdiu2k_6ugiPZ5X_14pplGkmHT6zybc2KvNs8G3XRxXi5oYFdpgrwoWxoyKBwpK01ANfhldezPq1Evktrf-yOm261oTIGn52NsYRSQfqT1sXt3pkSYh2MYLPAQRboSIacwBzVF6AA3cY3_Cz59DTGsjzTnNpvluBUW62E0W-bJFIbqgkvtc2f8ZMFUI2MLQGxQxKvovRV1A9TDCbAM2cN76ngAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsbrCtYmOqu5PG_BDt3nXkLJb9wycXreepV2NIxKuYO-5iy50WgqZIHaOfgV4OWtoVkbMqtWr0qjMc3RRHKmno8cyZd0lee867IvKl-L5Io_z95QE1hLlWr5McsR9WyiPLv7DmBPiN3O5wTEfVLQjEOlipJStrZ2DLGl21lNmiIKQIpFxcX7FsTmv8clTil00we2W7Tq0Cny8319E-yRYc9waaSEv4dW_Q6yBsTdEAqf9pe9pcJS5E6Kv4WIczrdsH5JVQVB7YAbI7se7mPT4cD_YkvBonllDI0SPHv0aWiuRcfDr8HsAn4wq1gZCPWVn4o10rYt6wRuwYqm07-1WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWDbGU2ucxpvclg5S6SVYYYru4yhOf6oKNuw2VvgrEn__m5Bu61RRsyZjwCiUdb4k0v3ziy9shwpdwa_HxPQeTkxLtEeZ3zLkyPHgNSHhQUnGtqFJgTGHH2UMkEWUzXAiJl8faTtJH2jKe2Lw0bHk1eg3ezBKnN27I3IP2oi6-Xopql8bxquW6MEzCLBpnbGM517TJDpkMfjPovtli1ZqKXa_xQtd1ZXkYhUKnTA7u0EgUvkN3ju0c6FYJaQZnOf-yq4yQuEsg4Nv6sa-LljGkuhBpqr1bXLpTJfXjdLYcHu22mhkFaX6VHhWBKNks1uFMc1acIBQK3fW0Lc5K8Z1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGKPAOZWOSOD7OWo7ipca6tFIScNpt0_Ugxc1rYFDrf0hulWG9g0il--caHkXefMQVhHqXtazpW9nAe56wJySb9HPhp1n7snnruUEvfXnGyRTZYL5UKZ-PvYHXQCbyfTo5EcLJTS1oq5nBTw702U4m_sy9pn6UjrKGSG-ph6FOWCS_6a4xYbIAjngtB9chUH4KfFd0Pai0RokD9qL5_3bt1SiQTjBBKDeYf_58uMbwHTqBioNWEdlwiMqfcTP-DlsvcoA8dSp0vzGaYc12BCcVy7yjahBqgchFpmzL5whkBm8Jx1UGIy7BvZAVfslGvo39qperfURjWrSN3ifg5g5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKcv5MYKJJJ8hzUTZTKtgDYDQpjOguW2eMU85SZGJNhc3SaPfVq-sNiN6JDp4lFdfFi5aIzWt_-IFFs6dLeJLXzXt34bfMEELQnozoshIfolDqY1KUIzY31_gMkf8w-ljmoeHFxKl4-TdZGLmpRB1xqyElNu9i6DxYt06kv8ao4qZgdGqzsKjUQDV4KBvyEeUzGgpbceFsSmHcw09DDPcuYpu2IW4LOyofHeo2uWjla_DSgnWsF76YsvMzvZchr_aN2FyACiER5SulCtRWjYhlwRmR13YimznWPBmyMcWWf4R5QhCMWwetq8LnxAcjoinl9L_9zkxM0D_-gF7m1sbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPCOj2PIxXs9hRj7VNvBheXFfhkAchJG-6qxz33vmO9m0HmB8-wzi26yvxf2cTF-xTLPQE7N1QMI4EswFZJUBQFP329AwHNy3vbsEl4XfrE1u5DcYNXk0gtE90BXTIdxnlG0S-7t1r0u6XE6goZNAcW3G5JZh5nbWGRTI3J36bkcFhpEVMt_GslbXDWAVyX4jqqS1Fsm2vw6hk-t_SaF4pKwQJO0TRsQFZoRfkx07hTQ3IwV9ffN3-rbQj6rXe069-w19vNN8wFuVcE-BjeQAC9UWOE7W6OQYD2Oc9ASo-0s3BlC9TST2HK2tfFHLNcmMcCeqX67-NPTKifwxon1MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy8TiRrSYMtEWrpk16BzVXDxAW42oA9vNArKu9sryzB7FouNXxkFquRUN_OFgb-z3GaC3cHqOmvDIkJC7rq5vgU5L08S6TcIfIBdMhsFIx9jr5BayuUU-fZVVU059PR12SDx32pU9-sLAmnZbgqekmsYpAgfuTSGdPbnZCny4x-syMkGrUpeSyFRGA7p2SicnoR4k9glpN6SF9k6k1Wjthwf3WHNs-XFMsXeJ_gqGPdFfZOX45cKpRqa5KeqxZZNGb9L88xRRljH--f1Rg3RhWXFDQz1wkXbuZcqCerwSgqFZ5uFDYeGXKS53aqJ2beneJaJQEoQbArCqcKpHy7_Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOLiTnE5zdWAaIoX2bOvkYtfDm9aa8tD9CW6Zz3GA31j0YnLIXMze0GqAkidMee9cyY2-wMrOS87EC1iBfmh_LUnu0EUrsrGOcN3CseVY6DnCXwiHjiLtoPDCxG3O--u07f8JQCI3GpzozJb6eDzhwsjVwkwEohCzp3NbBXknhS_q9ZDe11Jedv-kgg5hCe-aoTWpoqCpPc6OwXHGFYKoM6DwlVmGJiq_IKum6ObjimWhXKwlJ7Z7uEze_egcf2cqIhfpSGlGIILbBEHxNsv-4hFE_CyOQCtFiLw2he8XSsZTfnMjjzrlQFs7uB5tkBCGgGHSCnhVMM-ZmhcdO2TmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9RB3e5PCM9zvRdxL_pRcEu1yps9pjHHn0MuNBz3DeAVQZGMW0jdJ_jsqadMnRo6O279DnLJo0oWyp2Ik3LibyWa8InH_zTCKfZ-VrAcPluciPawwuCPJflGQ3ym-Uv3VoRC7mA61DGhvWehpRqrUufqnsBbmwAsw1_0cGa-SZUMOqnQLnF3mRhsDwNKN5MXKLuPs0DSt1d2hWRnVnWP_18KdjwesvjVLkhqgup0dQU6f7YMMZ7wmSBWayoV2nbmRaKZeikS0tRSNAPNDRUR282r-qXC3n6NlB4ZhlrDX6kXyFLuefIOOZqxTPa-ivNfPPYa7nkTbEBnUY8Asy6pZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivGehnvcKIRnnClW_3fyJP5msHjgfUjg8IWpCFwCJQ849HzEIQ2Cx8bWAVtWqhwihmwbNhdTRoYhnfaodhbtAo7PfPgZY-oKkrbBnX6wUJhy2qxAmMcqOnG5ytWj2WzLDnaToVy20E9jgBOVUwGM_4XL6F_ZwWjdNTuNC7hhrY5gFQU5AAqVwHFkCeFpFZUfx-tu8KJrYZjUwPOA9SdVteO2TlxvZxKQfDyW_H3ko9K5xZ5CeyCpqiSSWwe4KykVRXBIrohzVQFnYZ1aB4lZ6G9799o4id-DRVx86yz0mOdXR0Lto5rnkO33h90sbsFyorLLyOUXQLqTeKiDzkPeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_55Ne9CE5kKVEzC-0sLRxKTvh1mLHqI5MR2pG500MXnLWNqIvBka3MLcYBGsHTlQwk6vlURIYiWN4d627IF_94UEKd51AVrsDJxbiw1KmFNNZcPqR1VIyt1YyOv1PYOLj7GRGjWwT5eX7hnN45fxufYUtTdx9TZ8ryAS3gW_UW9ucnAN4eh6XLP_MMeuVM5YaT6DqYsef53obh2zbJN1UH5HScrQ-RYAiDXucUTqQRxT6A5972MXh44pZC9_OlpNTN0f9pc4cRLAcdVPrWOYcSSIjafxaFSL06-0TaY6sQY9ovfz-wEwi7-XldXz2RcMre2d6zDeU0R3oHCygCWYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJCec9H8aMDyTLMut3UmJMLp9tZeJS3ZvEgDp-edY66x3gckv-44k1njYGyrfdmN87dseCwK8_c8tuti1c8m2MCfHm5W-TOsl8EUqFGhEkX1rtm8W0BmvMdMIs8bz9OjBogC017TL4RcEA4Dx2eCxcvxLqFoRF7mhMiLNIs_gpL9bBsPd3BpHPMEPR73Jt3P36IZabc0xcHdQS2Q8AOu72hz7hT7J65j8SGj-NAskOcj9g-Zh9k8FhX6AQwOCCjYyQ6PI330HYJ-7DIkNctE4C4EWOvYV3h9x698xWnNQBq3yQS8kfnU7b-siU-1sBLfP2pynlTxrtKHf4Um8Ee7lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_T0sbCkCXnKGtQ-I3EUJFo9uAFr3YKQwlG4F89TJJWMJZM2eQZ2b2fY6bCfmf5lB5d93YkuwbXnDei_KfafU5SCzUJdg6qgB98sQ1AuY4AoYeb77pvEar-xkTL3XXwN4rg7_oZal7xl-C6tuhbESj32__esX0Xf4HK0fFaalQdEbAEvA2AB4hXYTXFZyCHIILGzLagbzdRF0RVehdSpCiJjZruXfz4gpmKJqGaPefChs6PRiPjZLNZ2nP5pWI568-MTyF3R14zDXInyRo1CrnB1cOWZxJLpzCe1M4ne7psGhiiQZpovy5oQQqNXYP1rzGVLmr5iEd64isp7EywMww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en0oVBh-bhT7-D9pg7JwtSa1z5xtGE5kfbdc54D7-_5_zfon-RmU7Q6Gg51PyqGym1sKhGVXDrbR6CGaqPSy-tgT1o1fwL_sI26vieWZi_RztwLvJ0T9CnUpddNkVWysyJtMtnQRsTJOfhDedUbjZgzWdBWIw7vyGVOFm50cCXLAMCzzMnvOMXhHq6FNapioNBanIRvv63ANvf2vmsqiZN1VJsVXYonuO0ApTYoM1-p_9u8ygY-5Pz8yU2C8DwNgkjfWgrmUA3szMixv4mSn_jYABhS95lGOxjRSHvNJWNXfW0QWc6EppxlOUm2T8PojLTGMv-IcPbFbgsdjlw0sLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1YJzv6ycPPYtTONK-z696NjI6XZ18r6YO-1YZhY3TyT_iRmkZNUVS1yDWDoYoiFSF2UXs7Q9d-PaVn9iLiwYMtu153seWuO1qxg3ACvsI7EtxtBPZ3sRZKbVYqi6p2_gZvzGXPwf9EU8nLwDal8nTojrIHLjlmxxCI0QpdHAJjDZHrMX43S5oi0bHQa08v4xIJPxrZkG4wKtklNoinXNEHDW0a0s_u0_uSIGvJn3fQqM6S9e9xW35GbEJTtCfhowuoZzKzdcnxqVMKCpB55m6lFtCQClZwCjcScNKXW32jSnu8Px7CESQFaaf_bwlcievvWustAEC48jumzllaWfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1qD8NdVp0InrCpeHrw7lsRN4_pmvUquuKrkxNxsnJ96MwXo01NqTpoj3P9cgPnjt8hYajkC5AR_vJLlnDl05nHABnen0f-UIdrb-5I1OoUayJkD7exAxU8CAvlpowfdqIvZEOFKsRSRcTL2HuK0RofUDerdpluL8bXbgPTHkOUhBNRTgtFOv90W59YzVL6nBEifxzLMV46QglUobtSGbzRh5wEQQTLFDiDXlzke_53_m1kEOg2ajA5W9gXLVSz-hY_CiYlXH7s2tIP__x4yLMvhE5hDx_D6m0BeTtqlpKUsgPObaYLtJkM6zS5-wHnagUs2i2zIYzFXcJ3BZ279UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBrkJmKpS3SOTDRTV_B9qGCAOb2dMfFk3ImtNR5ONRzVLLk3U-azE4jv1skTe_AUjMxOgCSIWGh9dod5sG6c2Qy2HXigxmR7qaErGp54D88AX5XrXz5uqR7py-2Kt77iY5mOQTASxIhEEuOZqAL4FFD3vdZV8-CX4W87hk91E1ft2FPECYXxpvyq1gjcHlfdwAxGYjMGQFGkptS2LQ__FhNMoemx6zi9S_jI-D3VU26ddJdcRxu4S5QbeL0rCKM59sn6eOT0NEqLxyhVwkM-SweaDH5sPNqtDcJ1ygLVukOVBV8qQ1s5Dk1GDtuITecXXQt1tECxFrBbn3BeORztXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgfXlYDZj1Ca_T4uBm8ZZ3hrkes_IeZJxtyTg8AOKHkBEPtwhEI5HLf-_knziegaG1vfij_7wjrCuuugqyVelgNW5e-UEfEdIu0d2HtJPK9HOFJYczaQLzm3wc1O5a_LvBI-JJXJpqlWa8Pu-Z9vB0oj95P_su5Oz0_ef4G634wD4qeH5Rk_TzCbjvuWhwv-7MSNm0Ur1X2EUFcJ94iv_TOT4iR04K4kyo_oM6fMwR63BHsXoYvNXpIlSs_i6wnkm5KnFdXd3F7U3NgZdZ-0CDkyh21QFe3UHisR7QqrRRFyJs23Q1EH3rp2YKpg6bdedn19n-prBH8z2DkXyy1jEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzBX74sTFeXpSrqbtnSSvrTSQrwpTeNijo_6YajlTdTEE0n_m-z01FSj5sOs-WKMz05ML6o4Me0qAzyEjkZ8rP7Wa5JEeu1ZTqSNI_qJbNNl4StmlgBAvnDmhg_D2WhJ19jI4IPoTHWVpo17IO2Rg1qr_VHvWhlPvy3SydiH_sCViYgIKjVPCzwQxEdwG0BTbW9Q66M1QJrWE9Vw_F_N4700Rr7tWoNH-VFvj9Ykm0F6ooxPl_GB39f7Piy0ygL40s8u0YBUHk_pnEyWqhQe2ACItyBpWA6708lcLC5r58U9O8A36Vsz8-8uMZ17mh5qVAFOTIVtB2jE5EOIDHtLJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWxAfLVYyJJVnIc_6qjeTjgU6UkoRJFiCC3NvtANmOtZTTWZcgLdyJwsd-kbX_9k0zJ0VTdXxnR8-R8JeVyjgr6znWtZtRz9la0i4SDyt-UVDJKuzrXjRWISJMwPPh7tAfojTcDFiInggTToR54mGkL1L6Uo-L0-y5hjMH00cbC6mmTuiwyXJmIaV0E6lLJj2Hz0Tg90bR3QPHciRVZL3N1TzRahuKl2jMyNAicQQldrKb3WQ3VKBClooH_J-I2BiQbMQWW881UPeZRcwFUre50GnfIV8Blj6S8iKuUkqxhWF9cjgfSm5xBZYdxsNnhpRg98PE9S-BLMuYRrQsdIyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJT8rdfMu55VEuf0QbNh9Oky4dbhdXfc0qTMrO7AUP_3Dka7pRlUZ2iASQB-gzVdyA-MZZcHWNtg3GVvSxrxTtf0lG20jN-OxiwoS2iGD7Zz6xMrADfjWcJu-zjRHoaohGvBzQHxjYoXKDu9sh901WX-74MF2b00ERA5le6HC9xyAN95_L9IXaNOOfs0B0W-TUGUi0q5UAZkngeZurK0FQy6BDR7wc2X--JYOSmI20MTKRKVricRa9fcy6W2RJvQbXTi3JXqaFBUsH0lPoLEm0qXyKOFh_Ib_KrrHMwn7cBnSW4D6P-_t0knC_0kisahm3k5C-0mVb8c9uduSojWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOu1t_wpBYgyhnF9DghP-L_xDvnNIQnoZUTESw9uVO3NM8aFrPGrBL30gWrZzaLonNh9j2zb7Dc8Ls_BpzOi-2zO7hKUJMtXBfDIH_Jmlygkgm8ICSTlSclsNTHia8xMj-KefS94YrhvzsC_R5l-10XFmdMlEjOhSgy-8QlR-p9Wg0GvAKiNYhRrRPZXkrnc5s6vyHlcKPGNsG-Fqj3i-td2G5xsocQdxkxbXL5XVYdtn63sbjGBycVIjcZOidUpdkIKY6ZXFAM53U2f8No-jEBVLNXxCm53MjMZqObnzLmP0aob3fVegKCZ9k4AANpYbrRWBGvQpJWJere6rbeTQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quDkWrVtYmGp2OPcoDWbtaNuB6bIPj-mcKhOx3XWh6FgJ2dOx57rROKXSUqXKkbCDrBXzImpzwUE_eXpcb8kBE7fBhvwU0_wCmShk_vH3pglu4z7S9dzAO2aZ3Ol8XNzyRxggOuuQfqzMyoywT2i3ZZRCbuvH3oYC0JyyF1l-sdw3oFxUNoA6is7maZhRCc3cljnDxlQQ2S4RKhhenatY44TDsaopt4Pmoa2C_4zxAL2GXnX7BqoSyXsyLIucCu30JOELHNL5l1-loZZblwohBfw-PyVdjPYDqX51980dKm3WzrOE-t1-o4thG5zrwOikKVgPa2vERBpDQJH9ZqhwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBo98X9mqcPrwdN6scRf2kRCrYoGPfbkb5SZBFOtyHCNz5bpGT29loo9O0A6tVt7CJOPnISHoDgTeAHYB5DKdwuPbf0TiSmNy56NuZLhFA8cMt65Zz8H8CMXkeJhGr0DWvZWJ5A02uBYGyJEPIUYUMXCgOAzONM0eyzXBdzMUxdIkiBLsCsSQ9uS_HRkqP3OvHJGd1P4roO1XprjW7DG5etXh-PY2Y7JDceKNyg7c5rZwSu-EkEOvKVhFS4YcIolbAG7PRuWRRwUB1qTDVVTKuiZdkf6eTmwKRrlq1fK6QneREPqZg7NyjGGsmKb-9IX397ZMELc4liie1HYZM8A3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfhjUM1U8Jj2UGxLGPzwZJpwJka5oBtx13g95BXIxDClIDGwHJ5gGZ6dFykANdgRKuQuXtqESsdGK9LFhknnno0nzfMs7Jk-beRMyE7alryRTo0qIxHpP3aRp4lB-SqgiRTd_h8j7z79p456dqUOGbXkadGMiyia7PbxZ2BCnv1cfvu8oji60w5Y1wlcNjH59TtaM5bt7qFGfebJNam0feNr6X1_U0-dMIK6k5GrCpPFlsXz5byYyZhIv-s78x8XmSLEQ-zlNag181Bk5ke2ndUsXM7LSxWWO4quSfbsQoqKtFEv46jxPb282VKJn0LQ69CsD2ogG0fjh7xP8VcY-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uruOk3SfivOzDPBNThxNhsCvN6apf6JuDE9dJgzTDZEji0MAjI2LyCDHFHAXSZyQ-kt4ZN4X9EvujplMUoWTIh5XIRd9_VLZ62UMfL9ccIxr7sEsJ4Om27HoCNqObtS9LaUv2N3V0NmJGIjJDHxPLkSBa9j-le1ZLaY2suJUjHfpnrLhi5AuUyJCEVHW_7vV3m6zRuz14pzOXl-SqHX-ax0I3b9Ax6FS4VJsjXa1VIbQfcr8sl3LVL4dKvT7mzLkGguEh6vziLNYOpluNi1cKh8pZxq1T1x1iNPmQzY7hm5hqv87Lh_fagSbUmDtGdVoipJhxjfg1frgj_tRz0vfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITanulPbMC7n3tDvJAUxjjThVZhbSooOi-NDhfsLxDBvZrQb118LGRV3utTmImId9FDcAB8AcQ2anBv1GeQdepPn3SQVd4RDnc5_1B6UnBM8B_fNFRcDbr1hi9yNGQ4XLtDkjq-UyKlNLlhLXZj3GojQ5gVD1yAZrNUTEKsCfPJ43f4PiiBHh6M7HuMqyHLFGYHn3u78j70EurWVHrGcGpH4Cb3zkncRV7cJGGjmCqFHemCbIP22XaeMO-LS_kkxE2QXZQD72D_88wqLvRV6BLr9rtVSbHBbkD-mAeS6LoNCSLXGl_H6LnoiRbpvhd1l7nGjNg9yjZ2XL8ona7wX6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlY81sC3YJSSz-_dFiePMyZ1Db-gKOUNuOaRBa5S2kvcnRsJ97Snl0phgmsKqwtQJECRGitMT8-wQFw8v8mZFkKihKZgXReTHH0JaTPM8V_EiA2kYTZ-d4sIM9x_-Cem0PZQR0fGa8-ixF1Ky0q82IBDdoTKkhIYUcxAglsvdJwPz35MYfffbZpFdGTfXFopxXAbmG9bqg9OuTHO5ha7buGKZr9LHxRCt8fMrnknZuembQ059Xcup9xleAn5-HE17qd5Y26M01XOQ7Vku-MQTTkElaj7PswBs6U4HW_ifOGGrTQ4Fiw1nUPXSKL0oGxKSlgZbIl7TT8PiZJTQ9dVdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnSEdxINtNOaPO2RRQiztmsMPB9AAn4S4UZxdU0ym8gMGNchvWB5NRQDmCRRfYzmeqOjPfQygLH_NT9FgXCxTQxYFFxW1eHtTlmvg2z-tC0zliDDmp8_Ul_htvALktPs-dIUOSKmKSkH46GsjvuOoF9sFfS9Hw8Zl3uhWpNfAauygWKb8fNxEH-Lrm54UL_ZlXtmE1PO4wpy_QizPmeLTPLux-Qcj0tw80Xf31kiuOjpOoJn8MY6zTYOhp1IFCzJMPTGT5Nfkzi3fcNTd-IjubVN5fhwbyco_OYj7Cm1PtEmvNwlACl07s1TGdgsQiwxCTbavg-UsMzTOF_HB3aJ_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euQlWZfdrFTW2YAjOOtCImOsu2OQ89bUdTcT4r9-VYj9tiP6x5GAx-m-OkHQE1gopSFUFZh3hYs4qgCAmHBAIzNE8_cCF8h_wsB5xH6OYnnu4gtruM28LJPxjqMQQ2fyfCBZOuQMSW3JzoxcwO9NMkhsNkAsO06fFE6Ld6j4fnzc6vrw-T-3kzdxfDeD6ajRcqaW_t9VLDeas8QhybhhMSojZWjLbRJofFgyaMw2bVYk-2_U1KBhXU62H5-qTaLKdIhdix-FRXGvV_w9PcRZceIj-5tgY4-Kfuu8WhiEypzAvZckN5cBzN_7lQmyNRoRlZGfVgG2ZLjUs4Cah4ASSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfNmzWa5KeWDXPhSn3LEFxnI0Ce197Ija20f2pTzKZgmE_sC7mD2DWiaFqO1vq2YXUm6DMwQhMG7CZFLGOIESpx8y1WzyDFmvCpK_Ujc3zSvjXIKWotyS8oQzvAVCOgcsiZyvXLmaWHFtIp5oHs6yXpiebIzhUTS8t3bBCS6oaBbjQ1iw-r2W6H-vptRZvSV5oMitUNUwesXs-3-NPBWyPKB1Lc_96JryUljMxRPhO8GkgGG13ByShqxs_qmKGlHZT7aSS6vN_GoQVRue-eDOBuq349oph1yJpCPo-7mb2aHiP7z6fCyzpuAYmYFGGF9d2Fu3XMLR4Irxavnq_F6Fg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=AZiDcndvCtxHhero8fDuJEkQRkzwWjA9zqC8MreyyWg8c-eGPKNJD2KRDxh9f4QlVq81TTElkPhD08h0vfnfyWvXDK8UKpbHczrjFVYNSFtL6pQeB1A_8wAT6Fpoq4mycUOsw_fa_zJXrvqCAmTZdbMyR1AxcPwigQyPhQ-emChDxAzN1fTC5V56gUkcSwPfCNawBJ0Upif08udH-Qlt8oKUs6j_IU3uKVy1U4XgOVRJrTwhs8tCRsTRYDfDirBObC21I44K_2doB-qdPk2Ojo0Y0wNBCruXfW4S3bZ9qjrjK-zXX10u1BbwO2hZ7fxLcSOU8-SODWw8yFTMVPKJLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=AZiDcndvCtxHhero8fDuJEkQRkzwWjA9zqC8MreyyWg8c-eGPKNJD2KRDxh9f4QlVq81TTElkPhD08h0vfnfyWvXDK8UKpbHczrjFVYNSFtL6pQeB1A_8wAT6Fpoq4mycUOsw_fa_zJXrvqCAmTZdbMyR1AxcPwigQyPhQ-emChDxAzN1fTC5V56gUkcSwPfCNawBJ0Upif08udH-Qlt8oKUs6j_IU3uKVy1U4XgOVRJrTwhs8tCRsTRYDfDirBObC21I44K_2doB-qdPk2Ojo0Y0wNBCruXfW4S3bZ9qjrjK-zXX10u1BbwO2hZ7fxLcSOU8-SODWw8yFTMVPKJLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfL9lXZeEhb9X6LhhK-hgtTAzFhMaHlM9DFjNCH3vDet3Ut6jBasTqHaxB8fSe7fba9f_RORVhl3vrXikAzbz3_aNNMwaGh7DKhVARQgC2CocMduMGVndOcRvxYLruW4s_6tuzf8EPsi01ibZjnN6QeXngi-1zr8KmqE0QmXG3YpRphn1C7KEoXRFDRay3MXEMgc-P0EjYmVbXTXipafZrVEx1-aONhflYI1BKR-7amXZhkKZs_3ErqB07zKfNPOr1Jtp0msuJgTYyhrEXiqOMPZr_0loISLFEDVAd9NQFD47gWxXqXLbgienkygGlN27Ik3rUopw9Dfgzrje4Pubw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abep9_f8RnGj4-tCOsE_XFDG9Sd0-wEOn5493YXe0nW6g9fGDKnnf-LNstZZacnG_PUExe3hVfE-jAwxgMe_8ZC7HhlKaN6f5bPQdp1P92eYT9NPphhaB4EODXhRcRaD2ac0DohaKn78ZtJI2Qv8FL73myeXIXOKnAt_P332McFaqpDCr8j9LbYBmvlCYP90D229cGh9rx39bbahcy2AoGNc4NkWvJeOFzibwNQ5ol2B8Pte39oEwAVXRIPsnIFR-Eh6GAndWExIXOXvzzSjuXyukPZUbhNXbpBH0QKovx6nZY83CXoWr7Uz3H5JgfG6qdOjaoTAdSL9XRvLl3UXiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQQCCY17_EJucr5uqThm8Sh4umHAf9MYgPQuUl0FeM2G_RcZz2FkDFSICgZK-Bl_O6LoxM0WbFX9aSXtsNUKI0OHtf3tsFgutJbJ5QQ8yAFLoGW2cLByRm4j6d7TzGH6ZuB5gtSkUqVOb4ehELhA83mOpp3WMwz3l9TO-RwklMgOReBUKu8rV3swSB14ffyIVouOhGZCXZg17vhVnfSHRasPY5MOg-Tfwd6xycxVcPB_sZKa4B9ZyoldKdF2Wo8XcyLPDDqqMBXseaShJvZSUUsJDEztWSgt8bbY_cawZo7gTmxu8XKZ4NRCzUNc_r2nZPF3dide9pHnvwYoKe1M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWDP4hT42d4Ianimx4lIHOYuYygVFgbx41OkN6htOSlmUvGXy57jXVpVkzoj5G4lAdyr_gnKyYC5n06Y7PzCjRYaXfK8dhvScozZEEXly5tS337a99l4f1rIrNDpPZSL7Ks9bXhTCC9kmm2LoW-q3v9KY8yC_RW4KSYAxNpg2K7GhSj0m9KdOTRhqsjAH45I_9VDR9-33OV0q4qSGlhcec_xPI1xPw1QRHBtBvV-fB9fVZCdsr7TmRJ0ajICW1qBceIqdYDH_VERYnJn2ScjLju-F7L42TQ7CJH_iWqkuChy8zAB54TmilTPm6Dr8jluM3ieudsdrFWeuJMaZM3nKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGM1S9ik3CMpgVnbFstLdLi7U9X-Cw6XYxQCnQvqTuzm0oPNvbVvBqa6m5wmhoe_FaRbVa7h73pgW-MFYDFOqqyHhOkXXTorc1Sw_99cmooeXEr7VwJJi_NHNWEjIhZ30yTmiZw8Lr5_onULuHbMX75b5oP7mlHgR2sBOtw6TITIOL-fgBj9LzmKcenzr124rrSpnoLUnjZsVSH-1UEd0dUCVBD30GymdLs9sNnCwSwoSx-iG3OByhVNQ0JwKhXiZJEERNoPuKNmTUiVw180x9AkEEHf1cCA_Vu_OcCWuBgbfoL34zEDHsRHIu_EOFYIGDjtIFoFCOTwQpcaXQknlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reI5gijmM-mkP9_6OYRowV70tEyKm9A2CkkNCnr-dClJGvTixFi3WFPVYv9e6XaYi6TRWeTAGbbS-pLPF2t5OmSuPvCksGvPIRzR1j2ajJf95pgHctUXlEWPebbPnElTTUc7M9KbxxB1ed5zmBX3Ts9SiUjqKsoAD-CSvA9aIj-K4SaMpdGhkOVZ1cwPa1dzGbqqdCr3UVOq15_9bYlmDPhSLID5Uv-iXz_KOgbVo8IWmkxjuK5QuoE9SgzUL46L6AqEdqJxqW9GlND4d6LBMnhUBy3BCeQd2inznqSwLkfUHmjLpGAWyY5U3I42abLEel4wR82GMUqng7Y2IopQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0nHkOHwRbgKoV3YNfYdZnjhNVCxbZPamzxNBgff08LFwzCZOKXgLReRO5RYkKQ-CdpKKs8vQ8MWiYVb4hErTBvKe8-hPLQaVh0w0IX4Gu63s5JzTns98ad_gbG_oeWUclJWbL2N8hWnrucxY_H1vG8-t5ZqITGaCtcN99fRY9V3Z2xgAKxjPz7yOGboe9_D3vJ8jFjAe63TqiWVe06Qzw5ec5y9LkDW9S7zflJQE7yxQmeHSX31g_W_Li3ZvLmVsjMSIvYskiVn18v0sRymuhGIG8oYOwqfPRBf5xEA5AdlFDl2LHhGf2_Ku8gUPQyvsmCFGu_P3HlWS5o9KeWmGg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=tEyvZfIUdJPaJT4J_aX6sktRZcAb4B1bN6vt_FGVBcl7ywtECyIWAJ-fQIJHQK7fzOdia8gYw5AYxEytrEmI-oVPItnr0M61BK_H4GiJND2Sw77119J5N3lm9T7qXt1aqttuwvOWERdTITEfPYDlztVHW8RqBBKOCoutPl2ou2O2L5FHNuyKtPUvVXQJ1aCDU6q4V_v_XpxEW7SPmlapp0nG0Jz9PHzf2-jp56WY_9Fia5Ld5SaqvS2hPOeCFyEgnVoAKk0aZCggQ26_mh_IZMujd-5bIbqBQEDyYYiYLypbnmxt73GH0aSxL7IVw66il4a6ALFSEdYlFcwYp5CclUyKxk2DHWUl2ttv2_baQTHh6u0Py5D9Hi9-uOM6YPaMs5CiG86zLj1uDiMHCoZwL0C2ATSzFm9m3TiLXXHev_3OXL7SmlqBVgUls8LWohTFmVt4jE6_OOEkncb7ZqV5WdvMHAIK25PN5878VFSP6JOE3Z62BqucHKI61b71vM85_dEIfWHSdt6V8PfwPEKOkX30iJamx0Ar_tMRYZbfbt0tZJEHSWHBI0HYRw4HJoafFE6KP8gRFoxH8MrSGvnYEUTdMZv-DSQHiHG8QrrVdEYzw0lxLxGtkqaEwfPDScFEgvc9xTfQkrSeV2msoWrhelaGsP6tL6klG5-4tyBEqvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=tEyvZfIUdJPaJT4J_aX6sktRZcAb4B1bN6vt_FGVBcl7ywtECyIWAJ-fQIJHQK7fzOdia8gYw5AYxEytrEmI-oVPItnr0M61BK_H4GiJND2Sw77119J5N3lm9T7qXt1aqttuwvOWERdTITEfPYDlztVHW8RqBBKOCoutPl2ou2O2L5FHNuyKtPUvVXQJ1aCDU6q4V_v_XpxEW7SPmlapp0nG0Jz9PHzf2-jp56WY_9Fia5Ld5SaqvS2hPOeCFyEgnVoAKk0aZCggQ26_mh_IZMujd-5bIbqBQEDyYYiYLypbnmxt73GH0aSxL7IVw66il4a6ALFSEdYlFcwYp5CclUyKxk2DHWUl2ttv2_baQTHh6u0Py5D9Hi9-uOM6YPaMs5CiG86zLj1uDiMHCoZwL0C2ATSzFm9m3TiLXXHev_3OXL7SmlqBVgUls8LWohTFmVt4jE6_OOEkncb7ZqV5WdvMHAIK25PN5878VFSP6JOE3Z62BqucHKI61b71vM85_dEIfWHSdt6V8PfwPEKOkX30iJamx0Ar_tMRYZbfbt0tZJEHSWHBI0HYRw4HJoafFE6KP8gRFoxH8MrSGvnYEUTdMZv-DSQHiHG8QrrVdEYzw0lxLxGtkqaEwfPDScFEgvc9xTfQkrSeV2msoWrhelaGsP6tL6klG5-4tyBEqvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VigvUrsAhNquC3I25vk4qJRBn1Qxv65SMXH9PiVyJZpKBrhdXJOjO8FH6Tuc_vUapU6j-5Qm56cY1u_gr3IHtpGsa4ziX9pc6Crq3Ni8ewWOH3yJk58wU8EvIQ1MbYVuX8s8WvP0At-dA98VnCS1FVX-rWc_Pz7TaHPuusoIgbLtzWARnsY8mOHL_AoVTN_aJ3ej0Pk2Ad2i3AMCSukAAdj566mfQ_VEIhxWV4p1atEQmmMa1YkFKhn7HcE3R3CtRGTTqQmnQa5-gkTkca_CGDaatfJRN-hl8otL8RTKd49ekU1T4pfhaU8dwW5YzEMYko9ilGot_4HAvsIe6Jhv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLgAggWcKLc8Rv1dC8nusSzQLMmhzCmKDGFBy4IaR-W9xtNcmdH4Hb7cvDqTiuTRf7Ai5wZxK70PoRB_xvsw9m6IIPb-dSU6EcjrFFIoqCe_8O3j-zeh4hOwhJcvQo6GTX-wU6pSAmXiw3oialMd4wjcG0lkcX-NSR_iR2Tk8wR_eqkzp45w164t_g8f4wv4C-BIE-6nNf7GZ4_IovZyzfRgsHf-KiRUUa8DMfWzxiXr_bbS4xv1oRhw1wrd2WqbA9WjSv41JYnJNmpVIdpMFL680ljx8vioq6VAwgUuYfzKMlRTlUTO0wS2X9AzoVYq3iLRPT5pjVfmXedieO3Fug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCKcNIMcMBroIkI-_1fR2NHX6R-zxPg9iVpUosQ-DM2bMHnD8to6djewyXdLJcwQZSBBlC1uCHJXDjJX0IEKdWN96HBEMrKbi612vt6SJoLXandS-GwHpuvjPhF6xstbp98dOYJpXj3yyff_JPBHVXwkUN3Hz3QKpLUyIfcfj8uhRzgXSzK1Fd45sFmDJm8taqdWM7p18hLoSPhco3bcV1ONXQNLfg7VLSskvLiDp0Iloa4WlqWwzGoJmi7MSxn6pQkt5EDN63hIH7GhmRRTQvdcr1PRzKsjr7_zo2DEP74pFYV9Fuxd5Do2JKWdp5L9evXxoHgreaaO_IF5SoDMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNAax6q6pLziRt3AV8TkpCACnml4TpNN8SLrVXF9_80vpYWHEWr7KvLVf-Pa4u-cv-j0jsoLOncgMih-dBn4JK51W3bcYKYiZa47XMn92ELE8RwkYFON6arll1oH2B8PXNlspEkvMMAXgtYuFMvuE1ZZ3rYJRiXitrxCviZkeeL-8ybapcBA_qC0mXLQKZGvtcj0Tu2cS7UFaDX79OImQozHPaDxpuPt_K2NsI163b_z2T3UHjX-77HQs_oI5tSIW8v8soF-KeZykMKCvQ1b9mWRovlMa3WPsoeyXDr9zLh3LFzToHkaJw5G2u5HEECZLnAJlQ0Qxzt-3NSHLgKIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlDB31KrmZaVBzMDduqvg1cP7AKqSnmFh8tVTD4wney3zihkvDmk6fiWy6lpHIh0vO5JK3f0H8d2Egp9-fef3d_QPm7i_PZmSvZ7eXD75nwKtpFOeD0m9mc7iVrecjIxvTHt46JspBRkdY9bxAp_WAUJE3OmrRMRYQQfDCXfL_opMWA7LDEJQYP23VVUFWLd5ci5SL-O9vrl5ZQPsFeJ1zJKWo6hdxzoOxNdrvOx-V2dhMOnYBuGv31Gx-zyGWvsw0J44ughw4r8JEN0ofGrAVknW_iqeS0iRKHlxb39jJiQnkbQ-kKvL4-ZeLJHYt36nIinu_6oVRO8mgRtkDOhLw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZUTO8rt3lTdgzBKQUnEALDWXifgvGsENI4VQpgGyRk5jyxvqc0bpSiV2EWOS6fYU6kHs3w9EMhms28P5uQgKnYjXzK6xUXnyg8WQbzAsV2e-r7J-btWub4jjKC33_3c2szifCF1BpMPSC6JPX0saaD8qps1V8GmVIjF_MOR56zIkkC7a0G5zFUHxGizSHCDR1Y_lv7-sKwyiO50jSd6_FVEAMHBdeh-ld7i7OohXVhWy6iDJNfz3ZZ7j720SZiWTF-W6Lu2M-1acPCUaW8yKi2grc3H_e0yLOGAZu5A1aqdXj5hYCyZYiB6cF9Tv-BPw3QWSmtzFXs2E-h1n21-SDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZUTO8rt3lTdgzBKQUnEALDWXifgvGsENI4VQpgGyRk5jyxvqc0bpSiV2EWOS6fYU6kHs3w9EMhms28P5uQgKnYjXzK6xUXnyg8WQbzAsV2e-r7J-btWub4jjKC33_3c2szifCF1BpMPSC6JPX0saaD8qps1V8GmVIjF_MOR56zIkkC7a0G5zFUHxGizSHCDR1Y_lv7-sKwyiO50jSd6_FVEAMHBdeh-ld7i7OohXVhWy6iDJNfz3ZZ7j720SZiWTF-W6Lu2M-1acPCUaW8yKi2grc3H_e0yLOGAZu5A1aqdXj5hYCyZYiB6cF9Tv-BPw3QWSmtzFXs2E-h1n21-SDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrO5gpYeSwpKgxYyOxxAet_aDlLq5D-0Gjboy_eqr-JVjbp07dP4ZAb4kRkZfxnZPi1_zz5Yq1emTxfgA8Ar_m7vjSVclOU1u1Mqr5GYXXwQ0OoWd5jWkG0JcH31h-CWC8fD88-FW2Y6D6yHS1PlCeeygt1-K1Fr6_AeS9fqIYMzzFMH0zowcQ3o4eK118sniSQeSzKw3oHco3K_bAuq4bEc1p_ELHTThR_fRxZrJ6khxEks47ABb2zy6mWRP8XNWwNGCFoetwtjC9NNxMWzNgdpx9avGgT3PXTvEvc3LGxSaBFD3aEVyrXmk78ctHFggxH6SsJyyYDs8AGVNwQ2qg.jpg" alt="photo" loading="lazy"/></div>
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
