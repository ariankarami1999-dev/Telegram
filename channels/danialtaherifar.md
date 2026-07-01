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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 162 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQfxsTQRD1nT996AzZtqP76yNlFWX1uHh1LoXhUR3o3haLD349HEFQEBJLbilOQSjZ2kwrN_2FOlz_KdTGzBY5gWgKNEvvpJSxoIjGKkC9YqRLQYWZVDaqG7apW8EV5rWjuIe-peAgEPAnacKFd-pbGdgoVa5H-Wbh9nkQYXlLoKkEzUHqEJi2DXi-1KP1IfwuFOIcrh_UA8C7WMSciKSaraqSQanKzBJ8lOMwBbnAylh0fDZeLus5CJuIwmmIQmyyCgjsxRbC6lLcbbUo6_M7fpWG9TW3hhVzNksswAn1pjPCcLQS2W24OtCTepV0vcvXioeobtOZ9Llf6pPmvVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 412 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 596 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 706 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 719 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 618 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWsNfi9jRQepCX1e5gDV4QqApUloUqiYjFkhcB9BVtqa-JrediIDJA9RUoBE-Hyf3g_G_LdT-j7whZa7jDreMWvdNpWL0q-aryu-5GUzgRiIU95JmTlrAUhfuREInxYeP2n0m8I8sEjWwqFsVF7QliMoajqmsnfkayNOD_EpjoJvRUYgp37nCfaFJRPUePqXdJw7E3FcWag4iguF7mPcYS2s6neOROx2D9cj_GNku8dZVl8GhtQW6Cgjwest8hfEzHiYtuJcy8PiGBADCpNTcd9ocAa0M-R0apmTt3cTN4hO8FmbDL7SFcPIPudtDwr-I3et1Oj5Zhe542VzPe3skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuRwQbHBviguNOX8xgj02QvS8vdRDimbMM7NdkAszWY3AU8HcOigtmz0AjSdYKCgMcTf6vgI0kI7OVXZ5RYRrPx7CKTT2hsqDPQgaP8cn3QDnaADFRGvrOmftreO-szfSV4gUQvomHLUjPpnWKzPZR2A1vQwkRP9J07jBdIx2NldlaYoWbo1bX4y-c5M4-hR3QnBVoRpGqSqGWoZ7FybWe6OmZBQDroPLCCMn4cvD1nm7W3uoBL2L-JSHECtrYefpbxZDsg3ICL8cdkwhWK6Qi8NF1J82yVn5vnlomfO45Et-0OoaFfQPtiFBiLHxurv5df3-P45tzK3hDrKvVV_vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikNWJv-4ggFsfyJdtfmYWaJVm7hF0NCeMER0C06xK5sqHFDX_vFY4s8dvAS-QJsbuGHvZIrkCSxIsAGrWYLVtmekBji-bC09VHHiI2Hwp5GceSOfybB9WV6YvGOPKzv59iHSb4QEa37wVW51VKzZVnDK5RYoRhPpwvRlmfa0wq6yOYU4VOPYSeRzW0jl8_BPzqyPrSmc5JYHIfL-GCaKf-2ppSDT71kJPelMqrMLHIOaXvgTl5PyctdEfkGy4M2yjYnZbAP2zW7PPLqG-dx3NEHw5D7BSmmLiGzgj0pGQ41DlbgZW3-oBZhQgDcj8_lVaMeeX7fP5nzm436MnE-Rhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 905 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBOn1CT7UwSI78h3KahIHIDKs0KiDrHvSkWWU0_Rzd35KFHoAPGxIFpgfNTgEkP-3A99VwuBP2EQuvKudwwWg3TrHAFMFNJwyht2jYwmQRP4-UvisVhr2a9aMjRZLw_DbyYCEKtWF4nOaDKTbM1VTCKgClOr7AAU2zamfi4JT-crj_lKLpjRPs6UD_WEGASBJMqCnnARPFvrdlIUPdBFOocNVKiDoqu4Vm8PFuXCZXof4d5dI14MQmxFfKsVI4C4B2isyQc-CNoF6k0gBeAvzFrnoiTy2B2-Yr8vf_D8F3y0aNDoWi0C-OY20kiF7DFrojmDT0Zo4h2vohqJQYL4nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANbqBkl581G8pNNkx3df4K8UlOfXqexbYJVV9jr3VT9QDPczfBkdl55vMPLfu2rsMJZEzOkCD3cpGOWo-t-npRR4BSaAMyZ068BIUemk5GG2uzl7qMnTv_85EQdMhvoMFrGLIqVBW_NqBjsvMCfDo0Yr8pBOUGOUpoH-0jVzwlm2jyvPYyCaChRVoT-jauOTT_R6nNU9grUCRjDlpPMlqUurgRQniT8hEFEZ7AuJQHEb3eq0ArZHoIQkFeNfcG-gtughzFuMajdSvJ3QK4IeJx3XCdxJtxBlRYknm7d5SCwg26BACxO16aVctR9YurrnWw2ILyHUxq8Jy_Cw7POVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0NOeU9z2f4Q8rn7LHM6jJmRbZG5y_KXPQQecligtQ_73R-wITcvv7gBSH8UmvTjZDmamzKb-2DALHNYUYtfZhUbkRYIhwkbnwJZQTqZ2UIDXdHgeymo21hIdUhnsORAPSdBd6nRSSNp7YagOE1r0Es8nLlJjEP58NrGCZFtd4JUPwQTZ3E2Htjf5XdOQn9pV4FJppePi8wbv1RqIybC4t9PhDn5E1HctXS85cnNymp3RhB4XSULa0_YteocIIxe_nqASfgQUQ3T9jUmD9iBvgqb29aJYN8HZLeUSnBkqBPj1A7v-FoDu8ldYwkrQSpKZW7T_DWL4bQ6RFf4X6bWTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQgeCsUk8uAMxaERupnluXZT5Pe_I1Fou-JvNR6H6wSPLZjV50U2Hr60cBKF4LuVY39F3xQJVMv5SnxfG-cDP4QXHbHqhqevUkP3ydgmcAFEXbK15f3XB8FBI6LxiNvkAovzjQ2Oar5qlBkrOL3-_xyEE-Pws2qeTrIpt44zuXTUPBtBENC0g1OaP13od3YqdIt3ixV7C5Zwowm6aEDLRmR45qbMoxSa2bcVw5fY2pqeXdULa7TvggQDeTvj7DRWeWL6NUY2XROCk3svZ_04jtknXoP5ZEVS9YK9d-OP3fGb17zNM4S0za0m7IRk45kymqkxnKsHvAg-MSDet19qLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 956 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM17c-O4I3Xi_e80UQlmQrxIOTRQq_yeMiJaabVmupGrhdSMgRl0eDQsltKvAMQP6NwChrlQWCrJRvm7a0_BOny_2Wv7ak11VDmTxsenTuKM21QlplT9h1-UW6v41dL26xjVrkwVDy-yspfJ0_X9I_2f93tgyQJInFaSIHf4fdOH0hpfrdQpAVyJuEqDy2O_hucxB0yMohfalIBYNZ_MsazVWNqLN1Tmxj-HirvgsP1sIyIYXCf4USmpuBDNHCER5P0G1ciBfbIM8azfbKbGiCDR32hBHVK4IP6CzejZrwAIdnZIhLa19fFMgAzofduLaz2qkyOhduywTTX0bbJOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 827 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e52glIkRFoB5NnyprPZc-OAslOWM3RzL8dRIbjghDuTF5dvkgrrYkTFpZz7CwpZ5fWyOU7KH_b8gBjZiT7d6_dNjabFqn0BCqsul1LVBHLGNVZ9rLGypYmcE23Tf4oBF_fdSLLuXNqqQqHoOnomQXqGgCRxXGFWZTu-LIug2MTYmBJdCIdoBKIYqupg4FbBUxN5qVuxY_vKMHD321BP0sseOg_FaG9--vFx66kDFwpZkmMUilgjqmnaNStsKMpNEYmNOG9jxFpO_HD33A_m6og1tLTu2GXewFphwQG-0wGgk_FdlgNeVXZhVojHqhYy5tuwwDbmFWDcTKuobyUea6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 687 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSBypQrenzCIcSNWpusYJFdUzPhe8T0gHgv0O84FCo87B6QnD6muMziITFRE1vJSB1YGCg8QTrPs6E9q6rQvl2QjngmQH-ZX2qgMZ1M2A9WPbGcPkhlrc78ACaBE14gAXzFR9JliDe9V2Q_AtGV1snmoBeDDOh3Szw4QzlLAvo_EAXOMhhkZgFqIc_EB8S6XiXdfDecKGEUmd2hao7d-enLVwWkZhI4eGcEOL6O4VPL0PbmwfGc1yN61AoLX1Sc6bVxXiC26BPadHbZ4FUax2Vrud5WkbHAeIkhx_1G9zHM_fuSphkixzQT9Lo93b4VLGb4auzr2IZgz5KZ7Ex3d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkvoGAgeM3J5dYBU5cAfYCtJeQhLMjRR12Bc10aH2XOwWwfbnfmrcfQdGxnfU-2aK4dwAbKxQXKIZP0suY35twqUbqZodw6C0K7H68OBvDqIoTK4cpjh8sDzTf78tmjHZLkklngjzlaQZNMxQ11coiAsOGDvMIe5iLDC6yZe83HdG5wMZoX-FdnbwWnNvG4_-NaNXliUc5K7ZUC_RCOBysC55ELpG40L5o9YoI8s5GF1KPhjjLPrxNC54RK2fUx7Vw0zRIhvdNNriUcjsON-X_ylJyuBMU20TFT5mKLT8og06iSiDh0jv_U0QOpUml4_l4Lb65D8FKPGF1_AXQt7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQ3aqFY3zzuRIfheaWyCKfjz6R_smy2grfmmWw4N7gc6zEtt0YnQaFTUElqWBqgs-9HdIhb-EgT8qFE10yAKuZ9CnNOGINNb6d08_Y56Q-Xl5YESZQR-nslL-D2iGfj77g3nvkV2ja7EsQRoVh0NbhP3u_CjzhGaBuDhtvZTGdJR2gHS2unZiCjcfSnpFBBX9ODNDhqUrYEipIwwgRgjn8af1cjJtIbfw_vX7mqPwbGN_LEV7iUg_isjam_D9rtt2PnBicTUSTZknxYassK-TApIw9PsaCRwFnAuEQMRiyPKDwV1phwIONmQ2zCYdrrPzUsmVDD3oym49YtQPHDRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQxVBnGJ9nqJ-oJ0pnBDSjNMTSeSlGnlDvbi_jpWmMv2nCT2VwYH5UlMS8N8cy9jV7s-ESMjeWOUt5iDJh_KreMaicSNmy0VorRplZ5ug3Npy55ylkLyJqAZ9-2vfZlSylDA7ZrTsV8SXUW9Lel5s-C9__GjOJYdd2VAy735q2nVrb12LPH_vt7pn1F1miDxoSUZJDXTPvoxM8lV4Zh4kWDdWqBgbKONq0jGGgPkFDVkLmPTB94C7urKg9g6PMHT3rwyWHGaddH8hy5NkwQHbIGIPuPEKA-dkvr3bKBEXsbUrRflAlOKzxl0EaTXCKZ2ettzavB8GeLd7Y1YFIqUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFUgDmT41FDgq0Lf570-sx99Ix_BSxojaim-rAMqJiSXNNXHSbgcZhtCdu9XDu2O1k06HH1lH-Fq9SwvfCFwArwNRrm_D0LELCobmYvpAVP6wTq1OlgFQB_Rc5_xG3PG0wKsxb8GGbgmCRZcJ6wczhp2aonwOGKwRwXanjs_gLqEhTYRmaxyKq-KE90yDyJVHwdSY8kuNcXKANW0BJ82G02mLDjMiIagnjm9cI78H742cGd3hJPoE94Y7jgEDKpgv2Ri-R2HYgSe7oEHZA7YfdNwjf0bDhJY_wxpMu7twWG0KHzvEG4r6dQMmXGF-8IaC5X_N3MCeUS-f2E7dtskow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rn2JD1EBkxdZqcvaMlspcuwft9_O32W9bYEcaLQlnngD4TU0lsMJ6EXav9vQSn2CjLgOQEHH8NvThXx9at1y9-Cr1BUSGEAmWEPYvdIxOhk5gaRIxAR5YTmWfklusCgKlzMfRYkwlA-FsmyGEDcJG2mBC7p1P95nU40bLZ_BdOUFpmSuQ-MHOpN2Bzk-HJNyk3ktctZ29dIzuQAbGZT15c074-AfDs1BjCCitfnuHoFJh83D6MGASbL5Ytlfpp2_N9tTOSRb5_a56PKlBB_u_xuz4D1JPG9-g3o5cR2TkuWx2KqHWaoYhIRZui-giG-gOTv6Dd4xRCT2jR75QN21EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ctEC6yjT9q85HBipb3TjfQNGUJVQxO6myPFKV93BM_rDVV69XpSqrRN3drNhSKDkVd_W7hZw4FI-fIJ3_UyBDNGQEK9Z2OnNuofEO5ZVPCZzCxqx1TAKWRLwP02eoE0J4TUz8QrrIK6s4q2-jgW3w4Ows7QPHpJ5nbc72H630ljBg2C5Vcr36JDg6hd1EUOvgyEvPKDi1LHr7_qL_uQg5ohY3g6VMvJWtREw8Gq0FJtcjHxGuUSyaEcTRXTxTPt2XXyQ8UYDLxQ-L72BQlAD8NlZcmGgXsW5EVzP-6nVV4lwCSbv16L9uEmXzcJpawjdJt54IADezfr0j57HVCX9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ctEC6yjT9q85HBipb3TjfQNGUJVQxO6myPFKV93BM_rDVV69XpSqrRN3drNhSKDkVd_W7hZw4FI-fIJ3_UyBDNGQEK9Z2OnNuofEO5ZVPCZzCxqx1TAKWRLwP02eoE0J4TUz8QrrIK6s4q2-jgW3w4Ows7QPHpJ5nbc72H630ljBg2C5Vcr36JDg6hd1EUOvgyEvPKDi1LHr7_qL_uQg5ohY3g6VMvJWtREw8Gq0FJtcjHxGuUSyaEcTRXTxTPt2XXyQ8UYDLxQ-L72BQlAD8NlZcmGgXsW5EVzP-6nVV4lwCSbv16L9uEmXzcJpawjdJt54IADezfr0j57HVCX9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNZ2dZ7nW9QfBV4tcfsTxlxpZLO0x0-X4KKMDzQ--v7tKJR_cb7aavUHkKvnzn_NPpIgnuzpOiZr7-6lmfs8ufXs__WITVAUBIieylcRFaj_DgD95zeXqZSRIzMOXzcmQl10MwxoPkFKtQsn4_9y6P2uQ36c_r33HJ_GWbz2XIQT-4Dcca12lxhBElVk-klljEjdySwF4nmN8dSkPHa9WrEpW0s-AZn1MNimEF-ScdU79zckqg4RNHgMgycVQHGCNuwQlCOz2_YqcoibedemonpfO3k7eU--9uD44w4VqJseY4WVEjozYTlOFW6_pgHKoy-EtSfhHex8NPqh3ZP94g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DASaKwu1GbhYF-ijXSsdyzLfQqxN_ABeI-pEccJuExbNfXG3JJP37uRur-pE1aQ8R0rzyalriJ5uLvOtbMT1QP0dvfbHzaH7cWejWGk3ZKHEObANxd6jtAqvGsn3CLlOilvNoNDzuO6kZ9u8AXMQJLgNhxMdgoYmlT7RQWo_quKUIyiV7_1xrUwQ2-_1C3OGXNuYiGfmKDWdSshAYD01zI1Mfy-btn_UzVWiwLGp2wSyuFXB5AAaQSuDdC9GDfkWCoDhe4BmjBErUCawjoOlNPaiLtxo8j_HM_Kj7kOVN27KG_qlVfhrUkIH-RO7RBwPoTaX78aCaSq-aKUm4brbpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVyz4eCHDLBFpsjpdS0W-fVHEcnYlvExY-qwonFP9BsmDBr-GxStc8YDWrhXQoOnJSywjrUtIqSsm3p6deR7_g0O35qV-mS8ckLJgjL-FrNM12J5745xGCRnCpJ_oKyDtj0RZ45ko2zp3yx5SC20krDc6BWPuOpbcU_5v8MfW_eyrQ3HLOr20nzLh3ovUfSkPzfb8Y5F9mJs6bOiZ4lpVEkkhhm1Ve2TDQn4bCgrFwNhj9aq1ouePVvfGK7MPppp52GPNQYtshMJnwP19tIjQuath-TOVCMvDjd_OL1KkExTEI6xrp3xqgSUzoBarfXhfl6XA6y2iTHNTZ0UuNdBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZeoXYB1wNErR9HgfjXH3qo49QfKlW2d92LTNla7-39X8KN1oNiPCz0ON_-wTOKnwXpvYgP9pjJf66ShKHZRDBFUQCsdYA27AS6g8W86gpV3XUligaK696yViRjELVA47LpubF0n_8IuH9Fv1fV5Xc-UBd2sFY4MdSOo19WBto3KdBe8-a7ofoaiTW_b9Qovb-J_y5YdYcO0a8jrWDkNHSRPC9EVXbVc-gb5CIpUIP5dCctb7JS9vl03PFJvUJUF2k6m78Wxx8bpMA02f4Ua_vJcTJ0UkJp4_NHtIyf3uKg3P8ElOxW1Zg4ijH-EScADhlsgd_rb1GFdha62KRF7lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
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
<div class="tg-footer">👁️ 988 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ5jtazKW4KQY7v4vPR2bBhbr94NkoyQBZ5uc8TqjncQbKCRHr4Nxmmv5MRCXeZo5TGQc_D5Z1m6_p-AKUs91GAaFqD0OORyK34KZ-modYiQaPxYluza2HhizcjSgfPlPANsY9Ev0fZAoIgrQKE4_QjQBACpj8W5NsODv_k8Y0pKWnb6F-qSMwkwGWRHYgJKIXspWo0-ccc1OBJivO-2urZc406rXJvGqi-AfERy2unH9A9ErCz0Nl6T8qfoj5P1cmIlJ6C8bcdPCM-sJUkIyi-bGfb1yLFvDBcNnFEphWC3XTUMjPqfi_5ZiOKElhvJh57UOMWE55-iwp7ooIkXwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR5akwN42q2sbrKJepKmUVzmGtMbkN7XGWpPWEhBF-nLrsJq71_aysxcyK-CLfh_R7K0g1mpkyu_aZoT44h94Gvi9SAT5GzzDE70Jnt_xX71MSM9NfuBt6pk01GdN_rpZL1qNvY9apN2wgkPnhT5_6TYUMrsAj_FV4PfQhWFzeciRRP_w9hJAJSpizYaTmf6Q9iBTFzsPXYuU_ETBecnLkcWg5-kAOC5TvmaHv_0EIuyPG7_5i26ZHC6GKnr-JeIjbsZDc06_NufsJ15pw8F3KPF_ZFCwJw8Os41pOeTHUmx74nh5LYCkonF-Q4CY-9szf8DY4MIycPP8X--O79n0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDMyaUvUP3TQmNnD_9GsZFgKxIKv-lrzFGpjFP_NGA0kuYHNvpOmRA-iL4tWthtPag7UAGkaAb2XQ7I-F-l_Ks8HIbi5CZk_F6ZcesZOnBxcsT_T5-K6ilk-pIvCCnzE4HUycwFI7in06HvVHpZhwmRSEi9jVpHOffFMPCSq4x_JAnrNLitPGPH7Zee5Cu7cV2rR7q8lHIc2PRUaCqYHXEtuBiLUQx-XM7iL3-wSNaJTJiaU__IHDV3fsinpdtdTRXB6sZeOmISil2juIiVJYray9BV0MqwJgg0eqA-XgwmMqD0rANB9DmMvHhNVUOKZtaj4ynO2RvvfSy2Xi1i9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOFuFv97gVClN_A1pOM9Kb2Y0g-bXsDps21gJ0gem0SxekAWMy1_RodYK8YB1YEcuuR9JmoWJTg18Cg6sEPLU3zV42h6bUxvjO1Z9kVdMbZ4zIz4Za7lI5MD9dRenOLqXj-QwA0ikJniiizXG5CzlzgY45eJ-S5jfg_fr3EgH78-JbnxT2ZUq29jRMsk8CKfY8wan9TfbY-S5Mdm-ikKZlRUjgzPyasPDMW1RTqwcNhFq5Ncto0bMHsYeWQM7ayMcM3cLBRkZWsCBZB5R75K50Qqk3ZkXPI0lPZNO7x0GsSQh6A6pmFVSFHp7vpC8iefo0V7t1hzcpOs9EiYOyZvtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z97yXRNRUdWuuWyUUkDheYe3eDxH9bC4ydRfoBW7UeAxRM205m24zanEz2jGkXulOYp8P2S8TfOAI-oIZ_83a5mf62uxe_PontVbBmvi7m8zKakNnZX60FBbNPnfT_Zur98-1UpqjZuxYiNRPK4ihxQuMf49TU7U4jHvJqNgR1zpICaIfBuZbadzpUd0RbbbsyXxb7hUbreMkcqMyWgGk1vwQ2Y57dryYRyy_91rD84Oa9FfhgXXLfmpg4s8NvGCntkCDWn1Id9l_JbcgpTulFG6SddB4uBL2yEvKVieSUW0a36E3KcvckXooOvOnF7BFP2hOSfVtMtCwgUFSrUc2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
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
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3zuPa7r93yQnNQNP1MV0tchO_gOd44CBtxFFt9Desf1sotm1Ye6us4ll756laR_5YXD5LIT7se8dFIr2Um_1SuYtGJe1OEUw2IDg71yPFy26UNnah_Oo3LMEDYKgvylDy1eVCxFmk7P00W8k8kV6PJ6trhFggLxm7993u3REG6qQpjor-oTZE09buuns-fye-wCZO5OgPZ_Zyutrf3cwA3solM2hD-MmcQNXJio_lYFVPFVHfVjnAI3tfmvuJxO1tstTcp260tZlHxDYPI1skO84CNuuv96ic02XF7Htfzf_hv256U9TXitqATY2qtHwS12EOnSUvWe_k2-hCV8aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiG5pNaOoBtfyF3KCMjD40jTdZg2hQ3gXINrYjTBZnyAJFgmz6u4C-qFJxW2YWKZaRPIjQF1xz3MNMWeNH5_o-6ntL644gL8ciDN117EDb6aUU-7_MMbkpL8uGuqidNVZMCyVlE7hi0ERG0HtASKAQHtqFTeVeG0inxKhchAyF971QE2UheaCrra2YuFkykV-BupDkUD5FhU6AodVRCF3rturDcP8XxDxtFYJLM0AA0n0Lwwz_ts1GGAStd1RTjUHQGDRE71X6HZQhSWoFhF4tpm-VPKo-Noonzmtw5kjSfP9NxRu4ATQkBQBWgYpYy-DJ5lKWCVu1TI8Rn7QQiTmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D61vyp_l0LMbXI4a3KWG6K5-ayTIBqs7qsbHEm5-ZeVv-5r06Ou6GX98C-l-OFXPvWRqrtNe5H-sJAoRz_I2nKARs2MpnUrFd-8sQCOMpG2daZj32Y1vIwRpuTCEfs9hEXM0x5pXTgBeM8uLN-sBVm8_k91nNEjvn9KLZYRTizlMmZ-zRedSGXTv0quP3rW0caA_pXC9u4NA23YJTCNX8v5mSuVTy772Tap9NReEBeK9OUwotFI-OMhdfIBloYp-Gs2xvrrvEK4gywyqkDd0nQlk-oKj6fuACK0ls3lcb8xOO7wHGynFhA1IHb0SoYAMKHsk5vUSl-QWYOA-CyCHKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 696 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
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
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNVUQnLqw490nAaQxbc7fP4YbANh009xmBb4K5kUlur3jiEBWGQhkr24qpTtSgSW3zhdgMI_RR8WXKeP7ePAWg1vcuZmfcAxTU4RZyfHmhxgM9ArmZVyw-rrpsVqepixuuRzvwPMhPd6wiFM-Q7TL_YSpruyR72AbOMDmGDv2pCuVfe1Z6KrphG_DGIHoCA9rw8LMcXFDNVnjP_Q7T6dVfPCrYjuWyqbb4OEnIcKDvvOdvb5nD2JBfpC4TFw82uaa6gZHfiuypka7JpFzmPR6o4upQVgm2RWHQQXkWEKvfgS9Ny1ntXeQvkYzswVZ85iByUdn0LVsI_qs22ZnPrfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLUubLG-ZD-2C9iBjK5VTlOmlW1G-38nJyvx-IVFm-YIZjH55h5M7GlHo_gcvpzSy2O2o7XpQcCmMcImjjysu_pxQOpVRX6M69trVpLcm_RM0F_w8qZ9seCq-gI20cUKWcUgm5w_P6l03Qp_DoVPUChXNiabuM-eLTkjRdoSDq6-joXayJUFxmjv7sXHCUzEKzjItqRMipDj7DJ4D-j8QqQsMgAES0g7wDcGyrQy9lgaNCJ8mByZoxlQoN_vYjtoHCwkWhvOUQOs1BdTqu-e8Dn5zC5ykWP6LGNGj-LWMY_DiHpwsf7YOoxWOfpz6Tt-yalEy9zyRjOsiReaatd0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYJWmCDAnygHkFo1HzPBUxPkySHTm03aGfmZwOOTKVBqZtJBevW1HVUQXNH5FGwJ3AdEHFVNZjOguIKJGc-QbAEHfUD8Zm5lUI3n1jG9-aGzfXIWQNSGLr1o9MZORZukUfHyi7SlTiIdAIEW7Cznkhv-XliAWPh5ok1SnCtZU9hsypYHarQ905dVXnXwdW0uSiInKLqXPtR0pFpSIx5B5O6op5_UwTGH4XRkJOSUS64zVkhGHFm4Muu79bJOL1GYxLSVu8kmPEsTU-GmSkwRbGhKnOhmFVLtzup-qGOwWWgAPMUOn9LoDTMerkjXgldw4dpHh4innXVEhoKIIOZB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqPpQ85FqStPyXU-JU0cSYF6IL_0HsQqMeS-E5VySFFIXFzJnsf2_Urq5Yy1GQ1BDxwGTS-_k0bmmEuBMlijL67NciDstkgq6Lc2WLZNejj_8rik5UNykkr7PjSNMmUvwirWiXZK41pR53RE-zT5GjGCE8PPqnv5jy1q8K7MPzQ02tAp0250-x8YiISPEeOE53R1XDYME6oiFzTHeatZH8Q3Ox4KuYN2vLTNMnQpE_s2E_sFMLJgDedK6WCvKHabrS3F8o8Um-R4931McN3iXz6r7xu8UjHbwd774aJLhZkuf3PjdZ-_z1grpJ79krz8WN5hYOwj_9Pmqfcz2tE18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHMRc3yHzYz6F9MqjrEPvPUcPELyrPaVp8IEJ4iGYkkSQxSORrMEmWfmY5ooj0Go_d5EW1UNlDlP61cnJJsh7Q_ZcaeCD8jV6IMnouG2ThDFXoBZrQey9nH6vxtJTwuCP6WhQhATtFDy6cQFfWRl_w8PSEMBgDBHUJ21j7aPV_ruqvewzOwyRJeGhrMXKePBUOvX2_rAHd2wL3i13IlJkbP1FfzuTVjC3jRwZ0pH1pAIk8kYrQT0HWlOTjOPB5dFzcgpq9pKeToaUUCgQ584bEkHRKaPVwIPiFbIPnAZjjUk8n7wvlNMljHP5QZgXyksSh6-E6BZS8il1Lg9sw-mSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfZRqYoKciJcFuYr4SsI4uizlrZc35InZZv4RbJ2amQzxXwzZNtUXixqU_2krkecOApyfhsghWdwLNspN3i9BqugkZrNejQbFf4L3QawucHGRFoZI4ZPRGyoMPhs-NmkUxbebKZ4fChQHhdb4HxQ4VgpM4QJO5gmfDLxAHLo2O1OKoZT8aN2rADaySnomXUpXDDMNfcqmAiODF7U8b15D7qj-5VLurj6UQSrNAWPcd_UYOpsREby0L6Ky3gyZN1bFSCAI2RT7hIZBQ4F8oz6NO74YK5vXOlxdJ-WvxyDyKIqh3glAeV1yseSba8AjCQiRxuignkStZ-H2onpftwlHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 580 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTyLTZbpW5XB_6v8amObP807WX1UMkHhcefR8ggL5lqc65Wfq-wDO-MiwKcxR4Nut0XBnLBOCNOUE1eBWpVsPBU392zfZbWz7kXn6x9QZynsn2cu7jeIfv9z1e_OnpF8zQCnocbBlrpuwYOBYkCkVnl602Y_teo74ScW76-Qlh7H2C9v4a3z0Y4g7Qhm7IBmqq8WOHl4SRqEI8AUQ_IVDFK4GUGKVOSFzEbFpv5pVRT06LNuQTIyqoKhrn907NJnGugINL2iizRxODSMaA91f-zcoVrlaX16XncCVCptIUCEzikeu2Efn8N0oJNx62wYh6wXApFS3IJ0iHmt2A1_EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 592 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axUx0eSyUkOR1DU6E2OjqPXDlVVRR04oOpaCDlyXJVfxJmTJtOUJFq-oS3rq8W3_Jv4tmYNPqJJqH2-uP2GgGwQ31E6XWk5UkXEPDsFj_4UcYgbyhYndr0lPoWVNLaCSlL0Q2K5xCn1fvOKBwxDjyiBfTmIyKXYHRRdMV6b_KkTBMhPUEKfyD0V6p_u0d7RFdTjJCqGNopMCDaUEd6fsY2OE4M-bO_2-QXkVyuT4NvnXzhU39SgCk4t6WNw5nsi0umpFyMqy7sW-jsVN74zCb-EMBvN_6ZhAMGFRYnb9J4qjw38SV9AkfnBkEW237NsiYUREaTn-k8wSxhqJycdmDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4YYTGgCfxYAQo-Tgwa5YkKGxBl-ngSc4IItptmTmlEBfe4G0zWUSUV3FKgUfCM_AGD2TbS8WyIozBXIdB6mCpv-om1FsxpJD2DVQV7mNMcz7O9-tXJiY9GeYW4hhaUgdfextSqioP0JD8Q6tUJSOAncmwICKgNnJpBaKFLlAzeG9SsVAXyzbQD5p8l-hNOtgGQU9ZmRmLtjUzZ6LqIT9_FcMOFq61yGb12Lx73z7uKDJ1oXwKCvLJt1mGbvSvI1KWrRE0ENSKB5aCYkQMcwGnv2UKDp6qOjgLxBc9AFJpQLb5jk7GqqJ_MBtO9M-ANoZJcT0QhcGH8DwkuTLxGMTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsn8ME0034Mg2YRgH7YfQb6vltwhjGf1Vb7w2Ad5InksXNMdRcKU9cg9KCtShG9KNCLrrQkOko7Eg2M3I2a67pQD6TwOL4L0vQY3RhJ0WUBYslyGtIyfXreeCHu4Ga_8mgbDy4kfZ8hS9D2HeeM1vpSX_RtuKPIx-ysyjecRxVNPLAwRZx1jBbsxOHsPcXP0l31AkCDtArccVIlFOARMbtxAd81h55wvucWqyAftLN4Qb-FuqQV9pU04ZnyvqzJN6iOSYJNzyGykMzKlqkeI1ATyTvg4nlx-amOPOKgBUyFENbSlPXByfBBb8vUNneHt438XFd1PUDZTJgXdDlnMBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYBPyoLilEDLVD4yBeD-mV_FJKP39dZ5EeSxiaS6sm7_sDwd0Rn-AeTdFSHwuwchCuqceh5lgi4ziBumhBpPDmaL5UYzsDOMyFA74MFvoBUxO4699flsypVfLJUy3fizygCECaAHajEA1r_gr5pnDXP5mRWmbjj7r-etsvoxODiYwg1ffrSo4WDtRfgCd9K3a7uFsPg-ESHjqF9fVZtNuwmkXjIX0yuGkQB_LOJmyh7H8_5R7smkXN1aHc9VOBeytoiZdV45-L6LYIimT6mXtntdnI_GDdU5LQDyJjc3cMIWIJCvjroByZyk2F6J1x7OeZWTp9AnBwsHBCnXLNrX0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2A9BdhyUIuU6h4K1JOxWuKvPbzFm8Z1XbiUnUsIJpd7o9GxVyd2-AW-tq2PWnT5guLy6JuHSki-pkdtLd6QX2EMo-cy0iD6PmhjX-hGaQjoSFP6xs_f5um0kPpI8K-EGClSdpAGDstKbB_IYA41XTvtxB7YJ0h1Uj6rE0mc0ctg01HcyDEG29KO35xXLdu-rGs8tI-tix3eoP1XvYfBUnp--1R5Dhd9yQloTZBEWw1V-dmTFnrOiMqY0lYw6MdTvYscZH-m8suY0YxZkcrmruJ_1SnT4MJpNRk2KTtfUzcmx1lb49qRidlPAAWBrkfdmenJvlHl5wmAAmwbPsQpUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHrR90bOoVy_YqdhkDvhyN_HzAan38ENOFp58JNGqE_aBaNjzTD67IF3oaSzEDD_Pj3er4eZiH-i6cuzHdxVTBiIupbjnZXKHMdRz4QYhB1EnNLbPOOi9_nPEDqRQYvnVFvdaloMHm8YfpF91-w9LnbaKCN4ddFhQNngt7zEV9yGVBqPFY344GMVzlAofGYcN_yV-aChU2l_dI5YLr9U7q7AOC-tuG4MpalKHAr7od_Ut-5lEYvnZJJV3VDXLg9_N7f2nij1FQe53-Mak1_EfLhBDUPWyX1M2knJ4kP8nzXvinMrTyDaLSNMENq0ugjSmjg7tz3YHq8cT2ZdqlO_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsQsoealbX5xmtZWoONybMbjg_1ZcpIq9E16C-JlsF4rQkR_zO-RHoU5tM2sSIkBQHQ1bauDos5PsjOW0dbbdwxyVDGDt_L5F7PzFgiDrXwSWfgKPaOrSULB3K2OL5_Cb9xYv4a_td6k_Shx71JDV2d5VhmZd625NSv1Ts3crOCALW8lZgzoLosfQCeWJfp-Qe1EJcwJANvAH2KxfkThbaBkEgmmo_tJ6u-9-uYS4tylPHVjMkvI31_wMHf4PxHy8yp94Nu2zHOuKjxgxKXhz5c4C-OpjNks7ZrdZmEvk9St8z26WwoS4qqQRu-DKPltR-QsUyGWL40ZS27CEiS5VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqvq8PKWR15acR2n872pPrUj78SbGur-abSkBsBSLnk6kk4AoGWO6PMtrpjRErk0i_UW5yOMH1fD23Kci7ETYEWEy36aIzPF94TcC_zuvy0JmBXwcWvPDOvzjhqFNe5aWI2yhox6HAP0q2nNz6D17V6HpbG9i1lLxBEPCv7BYzsMAf-SJ_rkEuefI-eQpIqa2atFZQTD-QS5nWZLiJ_R23WeWufwVDZfPNgtUC7epCZyoNrXbaWZ2JdBtw-4XPF2HN0705mq9vEOMVfH8Xcz4__pG3H-NOFt0X_TFr_oaEbkG--Xgg9sXl7x7AXAHfGuXKgkwSaIisHwB2sVJLAuGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcI3wupgx4PG3zB8xVZPq8FNf6drtUeFBoTGQKrOx5kZ05t3Fny3LXM8k8TEGF8kTPvqKRz2DK4MGpGo-bUEBCmtGQ5TL_WmirzIb25ojTUU54mqEFCl2MEP3ZM3q3tPjlORt21masC2pbtvoD0bKLCip2yQ6xNO8NLkQ101LoMHuCWzaDAQ0Iryl0dwjTJXKcS3ZuK04cUsX9bQf5uQw_oLGQ3PJ64uqubNQSjSSOQePj1kJZVP-2KDAKw3pXXkMdqygNOXBkKltlmhqjL_l-Cej5jwAGJYPJri39C6unMQclJtHyxHshgcH_MM0KeSlgwv86sm5fUwfTDMI2Hftw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2QgTDc7KzC1FvJORysV0DiS3H9eKocH9jOxO-kt__-ii0S3dDPz2XEHbCbyktd-qqAHp0XTvZg-E9cffRYcutopTs0EF4bcdyKYV3oo5umbJXc2gRwVsZDwHcn2qeX1U9k8OaxYQ-xr2gCyp80e9HN0h8Qmhh1tElrHEFWxDIK0UH1nwz7iEIMspIhb7dPuykC9maz9dOvAu1ccv5c-VDCoup3DGclv2tRhczWRstFHNgk1lx6_eu27dB_gqjRDLkWbKbUrFrwBbCjDEj70pi9aOr3bdJpsn9WGolkGrMw8QypmAKYrzLXIvMnx5mCE74wKcUptCngXLckGkCJh8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVB-LJU1ObkjfsVZCuE6k8kIGEfLnP6qk2IGkM3SjeRmRjtcHhCDSpOwzvr_V9PyuVxBs6b6XUOAeCTZ-y2mzQg4xlZZhDxYCTQkaG1TDzgZomKW75X0hdVFNTLvDtVHdKT9GC5Hur-zvuKqrR3jbeKiFq-431wPoixGmbsu9jaaVCMxLvCU13ifE9pi6BOiQlGuzaMYgbiH62wCzq6P0flg8COtV5RcAwQNegSq3mwbgA3x5ZasY9rYVZ3tIvRz_JzXgJgSOFmlehmaXEtUvCVoBxHDMyv_0_-EHl5B0710es4ZjPRokkQJ-EkZn_YrypW0AkXMzwdeQhvBur_d-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSpAQjpC8WsQukWNztZzOYcp2BZUyR4uGSgKS1qfuLJ9fOLZ2N7kkSc9ZqV1AopFtYeCZMJwE4UgrOOGtLGxzPFim-8-BHuFD5044MZiNdm_a5VqmDkmN2c90YX1UlAAMtev3y1AWYLsB2oPC_jy3AVvMBKg9iDM6MpH4vpKOkasN0RZtZzG1qBSi-DHLx3yU8vi-zpD3jlFwk_KB38CCyjv16AxDn1Cco1h9TVBYaRck3nsnJlmei6S7o8hdw7LCTtkIEIqJXRDJAHymeEyb8O-YnC6_1bUQm0zvOFCgC-WOFBsd_s3KDwdHa2q28I8Mn9NMd-NjKNTC1FYZqldzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQsvP8cdnWBRPpiqxIGW2DwGb6uHBqzYqLYJ_lHLOMzDWW_BQMQl0Qf6TKcU2Nd4Xq1-CN6q8fduc1BcVatTpTXP7kF8QbvUVj45pXBbVciyy16D3kN71diEvFAx2-22rjz5-mB9l7ZcTyp2WxMDXEs3Is7Y9mJLLUy2LReibvHkZPcKkBc3gYeWa-omJDMkB0G_0Zjy2JVpWtNugO_-OkNo6d5fK3sS4to341Twzd5ROmhRPM19fpkJXdwwttwBwrgxr1ivg_fuErvU_4H90foefP5MLmDmMwWG3J5gdrn4saJwtg34nlH89mS0Ik2fx_3NGxxlbC2UM0odaFOleg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCljfVarbY6sRy9bF6tKd0mlcdJlJuA_O8t2-UJxISZbNDWjpL-J9A5y0SLu9QG4lrAXnkth6fI1hTcgcwO6QOlO1lU4dlhapOxkfEFmGndmWStEVDnEkN239gv4hYTTAU1QVzOF0SgYVoCnk8Lyfngio6xsVUqHI6AU93MQJo2J_V3Kgy9SZwmw_VPslAYEvfEpNfYjpYZ9JS8lraLpVkqdDFeMxgjYmZjPbee1ifuGkXq1DyqNirJ9g1ZXDL66nO1-lPjmecBOXMa7tJqnkMuhYpOM1hrfTQuPCzYRdjiIOWkVCmQFANIVlvu7_5xe1d7t7db9qfNANPQAGFNh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4sdSxdPm-hJncc6VCZhpSAmxkm54n4GDu06iZ5qfc3rhd9h3yH-279EABk1ZdYk3CSaBUuQOPZd1NZRG5-TKUyshVcTejG43JkJVivYrp_ecK12xrBOqhh_lZfpXfis2jpTA7YYJivq4Ekfmm_l7-UIUgpPgMoV2lK5zTcRLAVbgjkZ2Gbwi4f9B1jMtNtykS0o648fVyKxYpqC6W4mUCCw27YGYNrrZA5_tRPXMOt-GwZ3wVyHESSzbGPiMUhYDXR5RQhr_rzbHmElPgzdmOfhdAA0n0cf1YaiER7xiMZ-2SrSgrRS2VnYNJrA7X9gie1yNrGdgRpsXsnWj86TAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZceCAWbGKYtkUeIzjI5ktFRYGwg5A01tkzLdLf9AyeE1jsSSE3aymkF7SN2ikUVithsofweuUtl1WiFgabajfubAH4xNbD8_kydxMkZ0DfqkcqUKs4nPH8RZIrL6iyZFIgOtmhPnUgWbAD7nzXDueVgfFvIKYRj4jFOVc2wL1NOF361735AQX9fuL8-005GQFicwsWUVTLuCWtLbL-munGDrW5Z2KhWXZJMmf0_ePHUgABPJ0TeAQcMAuDD3m3Y75xvHJp19z7DyZd2951LXTows2yPdTEp7pd3Mh3BeeZxmIB6dTu-VzXbO9tDSc-66zRKslUZff8LmbSYM7LbhvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VosYmXM3_DHVkrE7gB4iAYiWiyZ2beesa4yuVzfPyAC82hDWEEsAGOWOozAMH_Y68ht395bpD1Mt1mPg64R6bE3hoRAPxl9hTBOUcrZR0yt9ED0jtLyXgM4MC8eCUcFUVWIQ64T-4QdPl9rryKAJsyKThFuU_KhyV2QK3atrBaXgndKacWMFkTl9ZtkQzYdXLVIjCrTadaoBYanTxIddZPzIiuVn1H-edINnGU2iGkoo-UpAr1PwobcSGIKx81Nulbm8KRwEw97qF3_I-XLxk1knenE75jEQYzdXV_F7mFbfovlSjjS_O32rq-WwlbCOVqZY3LlyoPan-a3_eVoLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOg01CmKRPweYE6bbqMYsuBnj4_mP6U3DrzIVgvq1KsnkxPsO4XhrKLnVDwzIW12GLIr7e4X4A9S8LzNvUeJ7LEr2G20GKhPSz7tCjytNDfizmTKhSsFBXj9Gv4fMvP0DOHef_OwK5yvqqbuX5CQu2LUzJC2iXIqDC55Nsq5HRGQLEVZPiWBMbGvTc2YUILNDOMTB3XVk4DXawM3ZKDKoHZ7DoB2ZLIPIOi8Sd5wZ7kUCBflElnx1gBNTDpcoyJ12Vr67n5tNiRQPWyZCyt-jizlCSr58axFYcuiEdbKkfrWHUNMCCksFNJRDy7xU22Qs2qNcwxBKTTzAfZ1DYfBNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQqiSra_lWr34R1o2NoyXgOWsKho4RJEhjp6qVBlsdwXpfFimD_KzRm5F0O4a38mMewQOaShGzH-5EhitDjw74gx6-2KPK7CnUBmtfVISLKJkGOy21nAki3bjtTKnjrLNdFW8qdcvBWBdbxwTtni5rntg_pK_gKQJBFsO2TbZjlUGyt-7uUBeFgAuc8HLe_C3Ic6XDvjyYUKII9qXRJjKMo1-64hPvBx3ypAl8rHKy4Cnpc-d9Z7pVezM8yN0Lxe9GOCTBEAH60vchaMQN-ET7Ec5oZc5VJxgI2AoMEZkYBaQXzATZRN1iGc9LLF30Tlqa5nauAWBAXRmB12uxB1cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIVE6j9MTb7Bt6Wq31g63GsISG1MsB7O6d6j6h7JwBExQrWxVTSfTnuwptEjQDCJaFDdre39wOB6moyvCRYt1xMZu8o-lFBkOtpo1Bv50ergfRtkY346i0MJScy6Yf5ayLGLc3JGEa5K4I56z4BBJEOrWYlur4OhchbLNcMgBTT5J5G2Ts4FStMFfnl9YpOCEyCcv_kWCC6e0SceJ50F224kJ9FwPVf1ts5OhrgMY8Bg9LI33nUZ9p1kWshRIMawTzOlyUM2_ywLAdvpjnrgFlqd3AA201T8n5VvO9AEhd23T28vFFHkTZZhXTCq9754UehK3fKmMz5Zv8L2L6VZHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF2g9xPcVcmfT1k1vftyttGFcHFWXg-W30vOPTkIJcdUWM5IuR-oCu8EeFQlX64Odw_RCrc9Ji6Jb4-KtQew2iDcYM0HLywzlwDr-5jRwOEX9fG11JvlSlMsE-voeo-JOhQt7qhWI6urz--meITzjio7gvZI2H1e6ltom_dKT0MEnt8TmgYdm99NJScFN8kOR4PGwxHMz29o0UMw1qgdc4FelDqAlUKoHZQO-_li4roXfYVSGiyQ1EW6SQLvh3d3ELVf2NQpYuovmf6DoBwb7vU-RiP1Nz9PcxIRjyQKX0VRhrmQi2FAsT-T203y4_0d8QfET5GWbuk8YSWLsIW4mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpSTAdxjrsBQJH0v02UG4D9fJAoTJM0NoxAlgnWiAf9y1JCp-0pb9qvBAVBgYpVKzVVr1Q1NNNnBy8tK6-PCs3gIe70alqMpqWKNicfueNXwlS05q-KZ-tNv8ux4EbMcPlhYPvDq_I0SDkVDhL6DcSYM6XqBUixfuolxV7Oj-8p0EQaVKy0uuDKWouKHBsPCyamjLS2yRforWCawrNVfO051IePpQ3D9iZpJcUz2zWlPN1frWRm010sJQtM3jM0Vkqf4SAcNgdcnGlMSQho-A6t9mKsO38ZO1Yy3L39Xvz6N74wcLUJgFcyY3xfaIZqo5frYjdzzHsddbfZtcrgYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwK3A_O0ip2tF7j2dv2B9LTEW1hI4BhOmiN06j6rWUlltTNaTOPMkR4e_jKsAgXISGdmkqAZaJmNnrHHUaQmqYd_AubjSdOGLHtxNhnhLb9bJ-NCg_n3qh4JwQqnR9WehzCp5WEBRFuVvCV_upX8i6uF-bn1u-zNTUT08cbNhnM2CR5-ZF9Na_2R9ZaVnPZXeWnRit6vtXqGN2ZNFWZqjvXX8hIxI54PJN1A-aYhUdqBVfozzwlS5PX_1qoq9eE7BruLeDnDu3i_K7eupE9x6kLVUVbvyzJfnWp-1zQ7EhR8mpXUqOO9sZ_W0mAxi1KsrAQAIknhomF0L_jdNVtTSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr_uKTx4OpBqanivazpUP2ccd05f0H1SGUTMh8m76tcwvaabruHcCspdz1O_w14PH_Cv9oUlQeQdHzNfrCBFuCz48MQtTKLVy_kh2cI-NvmJz6DKstrS9srHc3dT5x4GnNswxjbEr6K3plwomBwPHw7kyLdP455EPxgVC-KS3gGQtAJrAmNqDCPZ6_5Sjwo6Yeb-9PPMYVPefqgr6yHaxOCGrL_siElXp-Yc-iYNSdCsAf_lkxciArbnGgoJ-P9ByvGYvypANuhlLvVLUJnhyiNS3J6b3veiv9RHVSMp72n6AzabCf7Ji3ZoiM026kn01xsV3ZojYkD0hj3lzocGJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpZ6MH2m2FyBRIFUKDMd_LTPcy8x1sfE0lrn1tu1tYH8GAXxwBTUxrIvmSZGvdEUdNPll0LehTIdXXyWJ1B7PKJNYk0BDZPHBoRX-5PpPhOkfHIy2tdPDeJYlgQ7_fCgDHtXjXsxzKN3nCJPDlTYUFhH_DK7coxf_Makz0d-Gi923vCpXzyIcmARZFyY0VfPP7JyY9fXY4YCmgBMLLp-MSL8maYhX9BJCIWg0W8f_2if0ouAIguL-yHcYz61CIZUq-T2b__fbRcPm3RqRlpi-nRfwrHPk6HbvHwsDhdGsQBR7cl6bcLVt83_e5bmQ_zsFJvy4MFxFXWrEKpZOGvo1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIFn0jbQ0B4e49JfNx9byoWm2HJJ5AtCqK114ib2cTP3BfdM3__EGyzwkwAEATiQWUdGLP9JuO96oJfSJ39r2u3oOUozEx6YjIWHIc7X1lT2SjYFGoqs0OpO-cY4hJYepLYEpmnNwKRNHdppimNLROhYQmyiIFY-J_JvIr1sekQNJbYLqrfXZwys9x6L4TGEh0KNGoeSZ2HL5zdsgB_DhfFXnQPnc3cmMDOuOUBC6u2sojqoQt8UqvVKPFc2nF8miNEX5eoXcb07E14MtLrqPGFxfTRaKQFLhfUNV7k7Feq6RFJFH7J75e8Pbs9dGmPQOVidxZaMvsUi9_MIZ9tMZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgvgaqK7jswjla3CYKWddJ1Cw6GNVwcP4cJMUj9vNqbfZt_3DVzWkBrcZ76rwyFRneDL4j8Jy4NpvMuOtAgAB4JRqGCn9W3XTkv_Emd1-8ku08pNacvT78-eg-haVOOtZsOSkM05k93NRKrf3UYTncFaxXPsGtYu9IbRl8jSRskygzeOmOfmw6slIqGoYsvJTaYMiMd2Sfs-NZGUhO-35sV8ccol5skUPubyYxoeLEr_BhuBkZGqsDJXWQ0vnUin6qsyhmSaCsr8wL11GXkjH8cubUBEXxLBMlmr__CFDE29jOvKbNFeyoZ86vj-Q7o3jitEFEBTtRiy0coQhGhrjg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=rU3aysvxM_y4iNF0NfYUcZf1v4Cmi97lyPo85adRyHQHo-K1QGOZLQPGHCrj12zAT48DJNS3_HNFtEZqrPzG4_7xwjclh9kw1zXzHXP5z0OCBtqNVxV0ZrjRLIoX7JaDzxw_fLSRj0Kdv_7F9p78kMfdadmO0vVV7_lyQbRRXqPsjONyn_CWBxM1vlIsqCGAKYms_IaHQiMlIB3rgt0_XkNd4RiGKk2R5AcX0K3_iCpUKyJGM1IFgkfpwesVcxgf78griUhdHGYq0eP0mqyIp6JmELtuVZMW23n8CXxkGkgisTRWrdqxgqQ1DncVn4MUB6pcAMRXN2ldZ2U7cC8R4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=rU3aysvxM_y4iNF0NfYUcZf1v4Cmi97lyPo85adRyHQHo-K1QGOZLQPGHCrj12zAT48DJNS3_HNFtEZqrPzG4_7xwjclh9kw1zXzHXP5z0OCBtqNVxV0ZrjRLIoX7JaDzxw_fLSRj0Kdv_7F9p78kMfdadmO0vVV7_lyQbRRXqPsjONyn_CWBxM1vlIsqCGAKYms_IaHQiMlIB3rgt0_XkNd4RiGKk2R5AcX0K3_iCpUKyJGM1IFgkfpwesVcxgf78griUhdHGYq0eP0mqyIp6JmELtuVZMW23n8CXxkGkgisTRWrdqxgqQ1DncVn4MUB6pcAMRXN2ldZ2U7cC8R4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpRtnxipQM55G3I6RWwIF0QxgnNsx473imm_uDrzT6kq1Y85FS1AMlVLwYa1U12sjHf7Rzt_OVCqtFEfkGdZiInvUvmUM_MBi_3ZhJkiou5iphYu6-NkuhO3GriuTlTHc5TOolIW7c54FXCh1M435d3m7UrhYsXmvpuTRJB5Uu_M3oiSXIObSqXW66R9LqMCKSFHtHsniM07NTyzYn81cRjs11k6_loFycTPxuNFLkjD5qoCo2jZpR6jPjAruo4KqwuTNXX8U3wGhWuACD9Lmuy68lzepEafoN0mkuqjLWHl8T_VSe4PT8MOFsCD-txd_zUbMT2J6YADTuZ7oqVAcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIhYHhaN9il-rU-4C66JD6hSXBth-Gb_rPokV0A3Ak0NTx3Ro21cHu7Vv5sE_s9--Lw0soT2FZor7AmSEoO2z9VM6HvyNE7Qm_8QHx3_YL_JCoCC1vGO68lPyMl_Y9EK0utLEhqYdkMRJgzuWYZCSn7XSA0FtuMqZsa-MaUQ4qE6OrCpZCFr3Y15hsxbUVx_4MqrHqnq7-nXsnJ9AcddyzP1IjX-b0GX7eJ2f5Ky6PjbPsCbSLHHpzaUjIq8HVbybSilZ1fLEloa4ibLrq1OY2xG1nCwv57zZd1DRR4b9NLghHsFFyOx2eR4gMqaoJE1w3K9jkvE0rUNXZJN1bmv_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXiNQl2cYvfHxIeYrIEwG07HDHdq_KzwrOIRoWv4BXRyR7X1pRd474EEuYVRJHcJ3uoqEj84vTCbQWrRgnFUfZ5MXUpGUxQ6jEPw1DvI2_q5aonRGmQpM1xioyBSjwQfWFLASBGKsLP2KiWta5Rbu1csvw_4mYDLb1bgWtNNmfWL1m1v3bHV3z3bsqC-1WRM2eJRZrQLdHgoWCnflyXgd5IcS14uLRGl3KY-rw7st8GVwe_zgr_Ayj2JthP1HfQ0_7OxL51Xl5j8Hc-U0cyJFRb4atnyiuN-Z7mf9rK571ErZEFwZzetIByHaPWy3dEo5ZG1qDKk3qZBobb3hqsliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5YpkqAJr_7lkvvpYPCk61p9cTRdvRuyMtC9ZEQ3Ac-bWOUI_p2OjPvuSVzGSjXN-irjTJobgKIgVGsUFwfQH5MPd8EQwZ4hatHti2QIGDWusHe4jQLu-FzQsFTjeOg5kPCwB5Y6_ixsiArdT5FkeQZn_D35mWyrXJ0f9PUmZOIXGnpGnBVgbAPvA9YNdVbJynd9vEsvns5Trn9jYtId5SODpuHOZDM8h0D4Lx98DJkPy459v4Y2p4KGaKknkuFRHqX-9rCIgjsN27JPDiUO-WIoLGX4u2ujaKDuj8FE712bpO_jPRjdplBJ_dy2Z11Jl3Gu_Y7pdi9atgNDB5kdUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibRPYFm1abM5V8L-kuSC23BlOchvQN8cUVNyMxx1EGGfbkbXK9kB8yVO2KGyFIgUbGFFgiXAnhYeF1y7Ewb0SWzKdaZQcnckEujsdMfBFNBLOnIK5XmQI6WN4vfvbhiSyUs7yYkcAUyGxzB9mQ26zNJK8m90SLVFA3SkOjHtb9VT9aaAr8JtHJvssz0kjRVURZP7tphtPGqe4KqBLE4_QaXV1_lXUyEbLVWjXT4JBVDCPFBkEBGEsdMk4JSat4hUUX3QsLSZvhpNUwQIhhY3WLZP8B2eqm9FJu_PkjVno2DAYjYbU7fNC-p1CEBFof0E0xgXBXHxvxw4WVjFaxRnCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnve9_zCn0f_pRNKTI3HKRag5VlxfkKMVsHN4apjLj0AM7sE5K9Ta-jQafapQAob7ID-cENsd1ggk6RBfe8NyK-h0EgqxOxwJIZZDF_MrLBiKIQSOR_q5iXjYIvHmh9hhQq1_Kz_JufPCRbg8SPEE6jOTO_MtpBidmbHbsaxqUqz-U9aJjiTJSVbtlOeSVnF2B7lzgA_oTsrrG2aCWPma01CmcPgX-D3DlqkgCGFRefcMYIgEjK5zVwbTlS8cppucXi0ZNTYz5itRzm3mfrPoLj2e5OPfJpFUEqOYsMluNpH6oxWnS6r66u6O26UvKay9siSgeetwWKuYptvE97-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFRnpn5t-GV4iZSxCIscF4ljJJVTyDkZiAoWRKkek7ht_9gShkJ0lnq7Jivl6e-N4n-rcbU1E8k9WWCTok_n0jKjyABWmnnxzqcl8X_LvJLlAfCedYfXhM9tKa7I9PgUCYKIyD8pwUcfPgDtPHTTcqT9XA9nfzyF-vUW8oN9yGUHIr2WepDbUwWvgOfCThBtGW3bKSeSsBOGovyL9fEMzKFVa-j12Sx2oq1pJcy4HxiYT2AZfsOwY86SKreNzfnuciMt4xHtBsyfi4cEejfJT88FUi9JIxlipUyGseCuv8j7GzrKuahdkC1tbXVopjrzdPyPSnByp-zM_G3zJ0ZWqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=bJxL-lsQkXrqjSBL2lG8DoM5dPQFWyN3InAzVcYbYoAoFda12TXHsZsBOXav58husRXIVdAXxPHyz3KpLcowbR_2VLrDPqDalyPYefwMN_YnzRmzxvEH3yTXyMwjnz1BdcHC51n4m949l87InvUKoTjAh0EYghtA6EcAPAe_JRCsBWIXxHmpYIPAD-ESKpxbHmvSBDiHaqP3YKHUlrSy0kdFwaxIB5ilyxUeAika_r5ydxPUFAWZpa0mGIBbles1aQQebInH8SuWuEsrN67WqEODALJ-hGX3iCYz-rIWcXpn_F6aKC5lC-8xVr_PFXoLTE6g8_dO0y0SI-mW31Qe7zp8EmJO9dmzH3YcKPKt2OqQPgPSXDi76ILZICEElJTirG-WZFzjItKQ4EgHL0YDgSRRMVpfNatQ3cacMGwazFxI5Z7TueTW6fIOukPSYEE87dXN8Cao9UpAlxWoOeLk-wZUf-zIb_d93DKte4_BHdAGguIroeyqrmzWMZJ4-N3BbBWrySCNTCIPBuLPu_cve9J_CPLUz3Rgfzsv_wpl1IiZrCtDFult08eEpLejGKimvoA1BIpeeVqNO-apVqLXm-YZPTsy7Qoz9R-ppzd7pKruSOLo2a0tXYitDO6mmAJlveLJ_vcG48kDEtxpvrWVzqRv19B579XlcAYf0_ws8Pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=bJxL-lsQkXrqjSBL2lG8DoM5dPQFWyN3InAzVcYbYoAoFda12TXHsZsBOXav58husRXIVdAXxPHyz3KpLcowbR_2VLrDPqDalyPYefwMN_YnzRmzxvEH3yTXyMwjnz1BdcHC51n4m949l87InvUKoTjAh0EYghtA6EcAPAe_JRCsBWIXxHmpYIPAD-ESKpxbHmvSBDiHaqP3YKHUlrSy0kdFwaxIB5ilyxUeAika_r5ydxPUFAWZpa0mGIBbles1aQQebInH8SuWuEsrN67WqEODALJ-hGX3iCYz-rIWcXpn_F6aKC5lC-8xVr_PFXoLTE6g8_dO0y0SI-mW31Qe7zp8EmJO9dmzH3YcKPKt2OqQPgPSXDi76ILZICEElJTirG-WZFzjItKQ4EgHL0YDgSRRMVpfNatQ3cacMGwazFxI5Z7TueTW6fIOukPSYEE87dXN8Cao9UpAlxWoOeLk-wZUf-zIb_d93DKte4_BHdAGguIroeyqrmzWMZJ4-N3BbBWrySCNTCIPBuLPu_cve9J_CPLUz3Rgfzsv_wpl1IiZrCtDFult08eEpLejGKimvoA1BIpeeVqNO-apVqLXm-YZPTsy7Qoz9R-ppzd7pKruSOLo2a0tXYitDO6mmAJlveLJ_vcG48kDEtxpvrWVzqRv19B579XlcAYf0_ws8Pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qbc3kARLnRvTdS2BnjXjwGDPItyx_NAXK-Ngr9DiwwrFH3V97mkt-Xz6yfCQaR7tePJoljmhRxfXHQcvAUgIsj2gNHcSLi-BVMU66Y2XHJK6RtVk-HoqH94OOUfUEp9otZNiW0YoUk6jtrU1FPFYOqlBlGTp7KY6vp7vGBLnkXuge82jz3FKPVDuCe7QNMRYDH7Wygf3VfN24MK-l_1Bm6sM_-Bk21oc68nRPBpMp4dJfzaIPYiFK0rea_D8gP0A8sTQu2OM6v8JI9K22pAH6r4JCVpDienmJ5C0uDxQsijR0yxS6zeJQy96ZNseWdyMLap_8rVzcWGWDArF8eAsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIraJlwd0ni8J8JR8kIE2ut83-8j-xsD4ulARcIFilCmyobTGpcmV7dLNdM4CIW9G-N35TIUFwWW2zLhwIWxkdEDjdcZKOrt1PFRS00fB54mTS_VinJpgRHjFJsHydwiQzdxB22-oAVO15jI13uRUhGkmXgvnQKkcfMRK5aT_x8rSBbzQCcS_dju8Af4pVrEuTw5kBmxn_O_B7W0SP2GzngFLpQLHIEXJmvSPM9ey26stKDSqY3GUJwB2oXZvPhg4rI78bm9SsOMAbC8rSuCFxIc5avnXBBR81m6r13DTlcAQBLApygyNLmv8yLkU45RWOpWJPzyW73m0xqy2hn9lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auDKdHlIgfAc1oHLZr8JPr7GtvJcPRFvCKTInzLiX_Ea2HU6TQCEwo6Xp509BG_2vU2ABdvZc1s2UB1OJic2nKVyDceO2-Zzu4b4bzwrU5YK08Kon6J9ta_Z-WFRGYABhj63OijWOGl2pe9JsTTReYrXNL-6OGXwVQIzC7HVgrI_bvES1EZkfW7CbAKJ6r0EeNwHuvVcJ1BuEwQbVLj_qlajn_y8bFoafCkhN9lOiomxmbUWcJBQvcuP714DUu9GAwsOAwXViiF5RpHJ2AB87lzxA054hqK1M6Eh_O8DYY6B0yGHxSYI_XeMfxXWG4gCkROlf7TbAEauWD05UKJolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bg6VSq96_26NfHuiwrp_DD5LDust1cWfGUuZIjjRN6x2euYDz39V0ITpgr7C6DvF3t_m-8YA4YrgqqGrLVd8Y2CeCJtXbpoVEN8tgcqY_XkajBRVaxBTqsuMVEWzQMDF9UxI7VlGzsjuF6tqemrmirNBd3OkEUG6PwYOXq7DKtexrOOExuVjGsjk3PJnhmS_KW0g3rDnqTaxgqVJmqMvU3XOP6w3YOrF0xDRkrSvOGMO4qu4GgrIYmDPblCd_lqELckecG_nDXb29V0OoikdlIxhVcP3dZ1YO_yUKJsc9GUixQboQvIgtsUQ5XAVBdOkXC4S50jcZwjskMk2CGtBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt89Yk9MwDeyRSqUBlZNzV_lGC4S8Ck-_bksTB4tHuW__1Ctw7-msAjz34mAowdHmV81JxDeL2xnHEiwl1lEwBn-fdvIoYWYh-X52ZhyOyvtwWMAEHOz76cEHpOhHIrCkqroMR6dWR4UgqbRIqv5h1eEhJv-kUp-m4Oq9VHC2KHTBgxTqpcvtSN2cFXT6I4223QkEibx-IWlYj-q7QZi8OQGZqHuFwIxOrf2sBLlyPS0LoIu_bqTcTaFfpKnvJoSNu3ufHfvVikST5n29GSo13QlM2SzFCRZCimB0xQe3Cy5P7mhztctGYwCdaXSLU5QJaPHWIhNKpSHU52xUnh9CQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RWB-o4cBPzJRRUN6XeKwL5E7ziByx6oHazBigp2KBYdgQlvKiRcL3KHIVA5YU5PJPSYnO42HGcRTrMN9KSntFFsBUYo9UeyWushct_fDFN-0G12NJNaX1yOW3pDifiq4TihhGc751w7EpDNdXvb1LE-vO2rZfCJXaXNodZKJKBWtxvXqYe1QNzdKa_diYKlY4o13U5pKq90UFebl0wTxmRk8s6Kt3KyICChiHTkEQFGPqfUh1UEJLAmrZsfyoNs28sPutXDWNIqmNfapcDuTp-DCRpPX6TWXMXOYhLa_cyTcvSTzlVfozBCA8i98oYVf1nSNysoaNDH7nRE8oxr2j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RWB-o4cBPzJRRUN6XeKwL5E7ziByx6oHazBigp2KBYdgQlvKiRcL3KHIVA5YU5PJPSYnO42HGcRTrMN9KSntFFsBUYo9UeyWushct_fDFN-0G12NJNaX1yOW3pDifiq4TihhGc751w7EpDNdXvb1LE-vO2rZfCJXaXNodZKJKBWtxvXqYe1QNzdKa_diYKlY4o13U5pKq90UFebl0wTxmRk8s6Kt3KyICChiHTkEQFGPqfUh1UEJLAmrZsfyoNs28sPutXDWNIqmNfapcDuTp-DCRpPX6TWXMXOYhLa_cyTcvSTzlVfozBCA8i98oYVf1nSNysoaNDH7nRE8oxr2j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMOBQvybg342dIzhlbr74rSzau-zT5PxqxIJlMpfcOAn-2ovd0s6PHo0znJ6Unn81ykQ_UUWnORFk4IAD3zyjy3KEs3BRaeoJFYuaRvdq0hXf6Wf0c7aEXQFjNvzML7fDmcNQtB_Cf_gfY9QNdc_AbrFI35z7W-QvbvltPI8i2E2gEma84EzQFpArimoF77JoapOayTg5oKSm57LTPLn1jgQIRo77yrS682TYJIbVDqlq36ISLdwMUWwYIa7d4Q3WZqgCekXapJMpoPYwPIq45PIKK_ocZInWfPLH0DY5hHg3kX9Rdd72yuAkDZ40jGkBOO0tiCXsfOueGD6h5Q8sQ.jpg" alt="photo" loading="lazy"/></div>
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
