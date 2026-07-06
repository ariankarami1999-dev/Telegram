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
<img src="https://cdn4.telesco.pe/file/Hp00fGNqJ4brNLJ32JKL8XrMY5jozcHN-WVhhJhkB_POIutSpxFfnWZlg6AyZcdP3OgYMMrDm2eqTRcv-JD_Kowajv7-2kcXuHuKf_78qrdpqR9AJmjZ3-Eu-SstAGXpFWqdVduYjStOmfkFRIYRQqQhDgbCFFfuUx9oyobLRkiex-ncgajs1LT9Pc6KsImbP3oLzfbbARLQJaanEP1jNKtN_ez4kZRj0-HW4QAjjDsodL5jjmK3frEEHZDGOFVOcoYS3QqaieQqo2qhs9pffplVwLRPe-y2AwEC8NuHz1g1ZefQas9ppNJNlBt0oY8KuXXkdP6f-tQZpVrCZ0xWUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 385 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcLHuY22rwk4r1P4vVQH4FvjVZpLB7l0s7QJxe-of_ttkjuFtnExKzR1J3JlRGDbAH99qijJx7F-3O7h374pf0mLkyGrXqux8dMUg2ptkhT9EkQ_1149CMKsjmNlQS3elxrEnjFW6hXKtsFiKNeRmCO8hAn7JDjpd-07mCsBZC3BdYyhiyPL5fcTTOzvwsFK2LSPOx7DLEiMPsRPxRs5i5nuozTE-RLfoEsMqP29dTJaE33z_rcTmOtX8fvWdZZQufUqUJhPiVfVeVx6C6rKQd0SXXGI_EhUAbaYAbhoTL4WAc_aKQxBvMO3krrJd0fqHeMSEvRFab2kiZydHKTBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 591 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 742 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=tEG0fcMic-94yRW889WJ8HjB7-ercLDvq3oSxqGxJUOsvoQkQ18gvsMP8pIPf3kxeYOfoTU5tvK16LVuPCo3AZ4UwWsTggP8_A2n8hYOW4MDIC1l2Ace_bLXMwZroPCkhNAHDN47Y7s5pJOTFzbfPy8fs1DAHWEhkINuMEfpPiBPh591nLQ6uWo45otiNblovUWT_NPKEWsUtgPD_pK5qjR4bt5reyZuqAEV0MWz3kHfauVMKfi4FgOfu8zNjdPFdwZGqRaYlbZDeI2notcN54B-vtkOiD59Yx40up-llOa28Wq3oEm3Ti3emsHbQlYW4CjGmgEFy_U8cpRXt7vzzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=tEG0fcMic-94yRW889WJ8HjB7-ercLDvq3oSxqGxJUOsvoQkQ18gvsMP8pIPf3kxeYOfoTU5tvK16LVuPCo3AZ4UwWsTggP8_A2n8hYOW4MDIC1l2Ace_bLXMwZroPCkhNAHDN47Y7s5pJOTFzbfPy8fs1DAHWEhkINuMEfpPiBPh591nLQ6uWo45otiNblovUWT_NPKEWsUtgPD_pK5qjR4bt5reyZuqAEV0MWz3kHfauVMKfi4FgOfu8zNjdPFdwZGqRaYlbZDeI2notcN54B-vtkOiD59Yx40up-llOa28Wq3oEm3Ti3emsHbQlYW4CjGmgEFy_U8cpRXt7vzzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvtjbph9S5fhM8FcqZ6XIArH7qM-NOUV5YshojBPa17hGzAZMjZsJCpcSMZ0vTuePzZsrYhpMxpWdjhAcq8bcQ2b52aB2rFDITpkOfSCXdW_bSD53tKBwL0jeQdIf-KTgqUgkTO5-DjdieBaUV5vEixkDmeoTR0W_SPYk8tEnYzTG3Sxl-2uBCdEhiwS15LaCFCnLrK7rofSR6edC2mjGYlH8deDRr1x3FLC7z_6HV9Ys9mBLDcHNAttruFGE6KAy7TOGrHWc1JTguNg5kHnrCb4FrmLs6QG8MrZs2F_AVMI9hxAE6dzVyfxQMHKKG9fIwnDV2lJPaM25AA6-qDpIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPgJz-uwlfFpI0cuIocrdQogssWgWGDd4xh3kO3bDAs_VzxpBB_upIo4rCI4lugzlmRciOU32IOoRUqPiCdbLIvjW4V81ZlamWPmD2jJoIfyd6T_ykvbAbfIteUEexQwurVmkRctmzksQqcZJx3nQ8komS8Zclq1VuZeo4v7GMffAnPHiaGdCOMFkh6V9cV6vrYj38YxvwLAHkaOEe6eyD0RMfkG7eaCZBnYPbg10uQwRPFpJkgBkMGf8wrw59-Jf4aHVYWM8owjkQqVsGxxpFA0stBZUCjd97sfL0nGOUAslIQAim7K143Asg-HfADR1YNV9Oyoc1ylIN0rVREmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSSabcoBIzVEPpR5hcCrEk4Eh9J3AcbA9nn0pdOyW2rerYpa0HT5HXbe7ALGPxy8q1ePhyjRYE7Eqc29lFqDy0JCuCw4lyQySJWlynaTFe6dJavm2GrjV_E6SMVPZLp65eDGn9zNivAstWJVdwpLc0orImccFNx5jGF5x0B5xJDNASg4OAyeoLjnk8X4Hir_6OOyxxC23lr-PskZ3DeNMsUvSc7At9P42yA1PEoSoUjX6UjQ0RKyb8UdwCw83xGgsaYcxu2vchBAkE1iaXPeCpQ2oQdrtFt6eys2xuLSHYc96-LL0NBosuaSOAOURpQg-ff1cbj-cjiP5_X7099-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhTjvSVsKDwF-GvXAIpm0jHi4BQ8VIFfAwxLEDbUAwgai44JDwkOQ-nfjy9_l7bDmj34nBYFtzHYwNqroxSpGIQHgD9w6DkEh1L4WR4ybvUpbhkHW0NOtABFO7AmZjSyO7ETmGZa2iKOEpwWQGM1EvUZmvoMvR8nQR7eENfn-DgrQ5_OgJUASmoaXk4rIdmMm5cwStNNxKAVCf-QWhDrlMXi1s39QF4YBizQx_KAffhkK9jRgabtOIXLs7AnNNBjCVhO3Y0RlP4if-xPGBofBwxplX288OIb7SOpVpJWpSZCFHMHIc5IO6LNpvu_A-IxssATn5AzbYs0CAZ1toHOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlnWKSWSp9izEVxdPqRnoUvZ5kYL24Z32S7nCxyA6ezQr9V4MTQdVWohKRcjtmIthVgKOEIYP3wi86iSrFHmCsoVY6SKYop8bwgbTb8x6z9lFQKPmdaSUJWkt6a8pIYm9egiVposf8K7U_LzyHumcowKT4PKZCcK5Dkt_SzooVuTDi7ONkCLrjZ-OgmQpkq_A4Fls_2HxWkGdM0ewiAOvLg4iOgnbxNyUtLlwdUKf2Gx__jbP2qCOtYwJqglTJ6W7vkvkv7h_Hv9YnNq4n66vY4PUM5fGkFh96qRVRyRyahdMweSH33006txSIvDJpgUKbLYUgb5rU6xYz47TTQUaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7CuK6wmiyFCa30O8yvhV9zQG9BX4WM8nWCUqeI7Wg1JGxif8sw4qOwzkBHfUStPWWClNYuJIjF9SOUmtpiqY8QHN6WHc7GYfOZama8-jY1O7NV64Pb7BN7K31ns453v5YjCBURVYMI7HZIkk9Q4QHRtbn2UeR6wSk_l1qrXL1wEfvuhJTnFVIuB67N_WoggmBMYV65mc971NGs47FtkJClHlyONjH_NZ38BcKcXGiFQdW4ytkhWJSWN5A6s9zZykmfxj2yp5FRfzg7fAwF9s6VlL1O3hCnYYu80ss3yUWcJvS25E4doynnXDTICU6KwqjUSejhMk-N4h2-oCdjolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OufDB5nW0OkEDfZr-kOPOjeiwe7UyFjNz-d9kajFg_8o4MqPt-DjZaVKU3j5PAbWO1Ic98PwoJsmquH4a0Ts0XX2C-qzDzmf9mcbrLmdzpBwjHs1LqoJy6e8yMI15-OCxmgyBHfu9oncoccB_0kWAzT4QNs1qHSB_1Q0AgV-VlQM3qCvjf2G0u8VtjiB-95gDbnTqEhTExrhi0pHpY5174-dKhIYBcIoQJRszXyfKfnkYGepepquMwfAi1z3Ye1KXCPs-6tAZTTCA2KK4C4CgxROcWzUQEIe8vr47oLBLbS9VziBG3r74eg5aqouWFBKWDvHe1swvJ3zYpP4FGeEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1r2GdnBzS-qpVVEUjCbTJUCAliu35y5jzFtQuCuCmewWzG__pG29Q8A6dN9w6bL4gj1pP2LBI94HFM18AEmHMNRcgPwWHkMympau_oRhnBQhxur71mT5n_O0cGtEx_mAR45iS4SDsaJI5EavjHWOP_aRIKHQuGgRV-AEaDKGq2Rw3xNmG918REpH_keCDxeR6Xkdx8pWmG3KKu32gWYcgvarVrPYt2coleodDeJgAE5gsI7slU2wkZq15K5YhJVwFGYt5Wu9kYRBVKytqRCetKO9fumq7CMcL18k4gQjg2WYy6Uuu6P_MkBRG_Vod2xRPhe8iLGLwCi1bAYrKEd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZnLvkZLIZtMTJqKNKZj4ged2LwV17F3u8Eas8-RXa7aWA9XUwOjoNJjqXPE3I3OeN_S6xXQe9IIMSvGTs7cDLVTiszMSwuL4QYykiOKf6TyS3VF58YsNnbrnWPvznfGSfl3jDpP-4dvm_e-B1yJ9wVlsDG77VIEul_2YWrlvCg4sy-Q5Q6Q972FMBmMicmv9z929f2adEbEv746TB1mGGcJjHUyP1jlL-ERVprCg-_Nt-TB0UvOYrs71RC9_kW7T_jO8du_sHxJ7PWBFz0m_fS32Yx8TlIh317Uvu_KbZ-8kE9_U3_30SOVfb47_uY91CDx4eCXCjM3bbmxUTNfHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5_-jPf4gth9WUTuMkb2ZNOgGRz6DFKzRi3pDc7GjMxj-4I5vXIuenIwYnoEGe92YyliaUDc-OPteupRDxs54N8xiFa88FhHtKXIBOB7bfyPK4PtV06FPli1vXss8V9FzKx6p23v_86cQwcgfI4fvYNtEyCjsHMO411QAulPn2J-mHLtVHUoc2GS8ExF7-WZrrHCl6nl1E99AvxAE-sDSSIMTtOWdpNU2ctmjG9H2mamVf5cdshPZ79UkAj5B9H-PAO7xbr53znhHkGh9D6W0mZtnaF9me8isMYojv2MTQ3mFNOZvx2GA3b8xRmXRDv-gEkSOwaJIB_Umst69SDUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 965 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZ3WGGoK1OXM-BjrNINqJ9T9PFxz4YuAIWseAcXDlPBYNUOfmJ250W6FiB9Pig2uo52pp6XopwqD_kYOkjN1fQUQIYRoR2TDTK42e8GFYmwQO6kEwEQvPTrUuH-mQJKhvv6V5-BCIK6E7-Gu1_C1mHviV8CF2BgKIAiBePgiZXkaUye3jszJDOHnoDf1rC8UHuBRHGju61MtNWLTBtlP6OZFM8cfGA3e09as8AnWxaYnXm4d463xPZtJLwcCTu3RyJig3UeGL-DuGlmTBGRyz2ptyv4bDZyUC68S-qOnyxEepJ67o52v1_WCitgdSPbnlXUs6CGR0Y2CqAwSVZ_tDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFyXJ4957L0b-wZmN9kzqmXD9UQNUzen9OAQ5qQPmOfuVuaD8JfZpuB7sLJLgp0LcnQaTmtvGarNXHsvJ_5icE2cc-3o29SfUNg8xj0ImgkPu53rCP6NNAyJHsZ0SJdh4gxkdS71w43L9W2IRQ9ObXOmVdE2yfApuysZF4polD-Rfl2uJmmgSdRWWPowFVeVPRLJUmcOv-v0I6g42JHLINQ5t47rTqcerKDkIYsEGN40Ti4VZ-eG2gI1JI8GT7-C027qwagHpKNaxVYzrh8URecMtcBN8l6a1dlmKNfzYwV2XMgcfY71hG-til1HJio4Qjyp4x2gpHNkk49XgAuT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jodbfw4KiN0WC8ZdtM9dyybQ0FWvyhvuAEnASbGfeOyf9joE3WL_Kml_6VQwMnY0pLDf7g2uUTIEYx-7GZ30ehkO9Psc7RYUGFnzK3Jeso60Zz1X1HJx6NnyU1sxp1Xo2j3LgvnsHOKVRAfp0GPFiKqW8ej-0kCXvbbyfuyAcpcDiFLoUPclmVqG7qOJ2YlvUnCZaH1QE_u2DOQ5cQhYVpTyX_BSQw6z96_EX18rBwAlVJzjzDl5OsJHDNLKLvF4J4xrZyJIYaw7K-JwtOWObfdxiSbFZ15nv__xLpw2vBgCzTsJ65jOzAVZg7hCDALBlw6c29Pc8rdF8XuIDutyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdU85Vjr2E4DsSUX9R_4uRH37RFEJoybYJXymWl0yHhci301V2beuK8tRK0rZqcFbmJW7Qrct1eRpYlCF3DGsyzmVFZpU8PTvfHw4fIPaQeZJ94j1VtOhdplBkxxZCfhYnxvOybBrItS5pBfiINGXnned4XZ0eMF5LdUJkI5LW0Uck3sY-3vOQZvgNfTpHVKFOY4cHQVgkaDYoKeCstef4rXUbAcwcBO95rvvnfY9kBGvBUEKFrqnJ_79Z02NFyAEDxV0uwpe62Afl4pQAjQCcwA8Wz9yDJ4sEcmFssNf49PFJLv42mn2f9Jcn3fsVA_tzLFa8g2U67A3Be0Z_a8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUieA9s-MLgwI2f0AQQGcMZa2xzjE4XYte9Fn8l7xe6nVYOVt6OqJ34nsi_AYDK_C9PD_4laZMUOpbvACshfWud6qfUX1q9STzROw3vE89G-RJIETaOM9uNlrsvZLhe0QmCKcqVgIybYMqiKMkzx-ALxJEzVLIDW2qFZOV8lhWYKe-NspqzynDX5oPAmwIWlkHqnTJePeRFDivh-_Zv3L36vdPd39ugrdBVB4GJ7ThWcAdn5bcVEvc-rfnEoklpuxnN6pVNg_VItNArLOEvWgl-60oR1WZ-ucXsPSpwgK2eoZ_Y2tFn6JMiDroERBx3HzqOh7c1stT84iY3wk6HPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-Ptde5EJIV7XVP_EPAkNK5qnR5D0vOKDOdRkXbVEt9zNZM1W_scqW3GGYmuvWgvisjFMi76UGdh7UxNhjRCbf7UJxS1DkL08ZiE6L63HKpHZjGhRqD4SfM4BP0AMEONeWl0CHIMyP-IyTAYnWq8v-p7Pus-2tevaDq70JnN3qaZvKYqtL2rQ04mqqGk3h1BBDD8wjcS8DNOxZFJtIKKo1IznoaX6lo6RVxtnjOEBd4szYg5LJ2IyP8OdlbShDQ0ukDKn12g1u6NKsuSFmlCPLNgrEz_iswaI_Ttuaze2rY5JCui2bKGSRIaAFDQ7fdjcUq798Pqq6ZMEsIcwCfuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkDNLE5IY7qJ4Wm8Zrqy5gd5C84fYgtbeXRIn_0OD-HyYY3dyToAANIcNDQWftxNcq0zU2UqY8PyVTCNy9Hywr5GtPrtXDG_EtiLr1sx7G9CwjkeYegtFHSOQZIiHSELA6Kbmj83-bn0ji9ATlgt-aXwJklLXALUN6l3Vyzp-ziw9WR-h11rm6SreTNRmGbeJAYssWEX31sP2TrciU_eBZJs0u91prdOStL_dxTg9hwROmcUmPYz0O6fGkC2yrAaxpIlI4cdXSzWww4fb3IfiHfqKwHhWL6Dd7kOaaRUfH-aSruSjYDONNcOooHIydyU-06a-OS6u-S4qynqCnTyzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F44K9xXP1vtr6xjFR3XEsupzlNHgqInuECAIxGRv8Bta8jg-AkoBaRQeM6tl_kILBzxLzWfIdNHZtNVbs8vApbhhe5Ji0IvOdcmafSdLRZ0eL682LuwEfF9_wJYJ_d61WLLjhCFexGeivaBieVKfBQ0V7eBAXeTiXktChEI9eDMg2KkOFGsVo557wnGFdeogFXw6q_RSG1aQUpZ-5FGUtt2BxxWRA9NcaZWWdKIEY_k9anXZdtgpUaPw-J2ECN72_B9ellrhhs7f9VSbWRqpHgDGY94DUnzTKiG7a028WvDMtLemxJQCcuYDVm4_-4aY7U_TIQkplObvRpx-1ia6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=Er6qlh7dfT-5QpKcuhSuC4ubSCFIzKO9TdAiHyAVH_UaMc1dRJ6oFV6ehIXZvLUO00qv2ZMEt3zq0kxA6epaoFzDA1waPIEE7GcOxoeitYB2d7aLl4Ct20PakLMUejrPHcE0kkJbOE_7XiRpuFQDbMONf8z1xL2HfucB5-TAAqOg5bCEFxRM28-Tz8mLKuVY0JwHp5-57NkVjbc8HXO7bxm7LOcXWf1J8ACgtY7h1y7B_gvLqK22hXo4BMKM5MPWDt5p52RiJbrKBFwqgBLnODpDTqX7AHTVOH2AvNZSMY4-SgK-X_60n_x_zrR53H-rSnvHh9kUG21HPYx8o5wuQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=Er6qlh7dfT-5QpKcuhSuC4ubSCFIzKO9TdAiHyAVH_UaMc1dRJ6oFV6ehIXZvLUO00qv2ZMEt3zq0kxA6epaoFzDA1waPIEE7GcOxoeitYB2d7aLl4Ct20PakLMUejrPHcE0kkJbOE_7XiRpuFQDbMONf8z1xL2HfucB5-TAAqOg5bCEFxRM28-Tz8mLKuVY0JwHp5-57NkVjbc8HXO7bxm7LOcXWf1J8ACgtY7h1y7B_gvLqK22hXo4BMKM5MPWDt5p52RiJbrKBFwqgBLnODpDTqX7AHTVOH2AvNZSMY4-SgK-X_60n_x_zrR53H-rSnvHh9kUG21HPYx8o5wuQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piynaI668GMZP1e9rtIPOuASAMdkkkJjLOe9IO7S5XkzOkVCaTEIBaTtlzLuM94vzwAb2QurQaKRShXowPfDKH5WRS3j05kRfBiKmT4BfD09GXwek1_Jv-YJPuY3NP02qwlrW7XcsRFHrFPgn0PNzS4lYPGn_bB9_SvgmvvkhK-atItlydbbbmsx0QdmZYOK15tKIHrntJyjhpkssju1vn60xwMg6c36K0F8qR5UTPInoH4z_0umSKxmYecCDER6ru4yzvG7vt0HuRqELUq-K6AggsK8ohjf_wMwSnM_nT6c8w2G-BM5FcKgVdUN-AJQRBS-XHKtaEJpvYf7LOnQZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf0wostxN8-jMfe2xpEZl6F1dxlIEXQnMOpWRvv2Bq439uHPapKOroK3csR8STc9eM1m2BoVeQMVxAKMvc6vKJuFFj0NjFBPl_lRGDPDORlI0b18CP-F1akDSHZRkqBqHzX5R5x2hyWEksiCGUfsfTDipnWn4kWECIiOiNtX1cekbHWu7tlroVwxG9GXn-8seImGIIS2BVX54oeU_HcNWfh2VBTM3A3gkvXfEBOpa4LiVVb-REJ1ATVmxNhurXAKWQT3Zyo9uiHBWxVDU07TnUuiDwlVVzqgYAopDMl0DriWdQuaukbf8PgWiqIhwHLE7IqRorHp1J7FViQGPOBkkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIfzhuQNLgqeos985fLx4WSZw-Ot_RbI6ar0z_jAXnd7-cXipcuicmyYX62g5rR6eTwKWPEPQ9qflSCIpZ3N7Bk3z6s912mPFCoXunLq-ZVeaGFEOKwUDzNiQ8s4t13gMj-Q27W9Ipup1oO4nVWl3Hp__tIS6LjYlIQ6mDQugZoX9mqIOSRaGp8fdMcHkjM-QzDy9VUh3cQcBsPmC7VER5MkLDTw9YFtl52blcxbsEK5rVXr2ZVkQgrwGMxDF3hpAzZ5ZJFsc-BtID2TSwM0kmlwwauExZqSJa0OsPATqrgoIFpHENza9-aY3tcGc4zLYzz5UMfQOcuE9E93Fi-T-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUfUkw-oQOB0QefOgMmZztp3NhEh_7f6zH2aBAWmyNYb--gBh4UMz5HdzAVlksIl5OMJOU7qCQC7kyNJaaL6d8JtYPemOpUYyQPWVZ21pccWpN4TvMx-JG1gwmWbXEGcv3j-jsdsuV54kjlmP-oD7JeMP4KNtd-1wGypdsCXLhKkx0Iq_lLq1x-SR3z6tB_wx0Kqd3w5Fh3PACOM8wKCpAYHMC7fHP6YCTSGnJmTiZ9krG5c1aonsNaT1aVNT9CwPGdTXW9jrP4-znhTUuABbdghmHXbiajq-X86vpfGWnf-4ji0M9afu9nX87v_2zDoxn3fdk7kMhmpxwOCWHejbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
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
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAzYHrOsWqwI61bE9g2BBjkiVQ4_sjcagQiMvAwohVYsfyXdwp31qcjsdn_tpZHjJFBDIBEtci6-O2B_EzVMUYRoH0Ogd-nv0gV-aqueirgxr2_woGFBU_jn2QpUPwD5OYL8Mq5lLP595CW8XVjd4Ic1dkb1IrydJ_XnMnpQW2Gw3NK0pdaw7WzvO-d0ds3ooafxkBRQZaUK-5vx_53byP5br-66YLFg5YiMgqe8_0ebFF3hvfnj3Wyr6Qejpb3tBGItT2N0qmpeKr7DcrwxIg1knZvXeE-0llLmE-I4K95cj9G7HONx-P6LJFKRjX1n5dQ4kdlfnoiULpNHS2DvHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiThAte0A93Iu9W2xcMUPgfbFKBZut6DDR_pbYfcKQoB_4tFFKQfvJS4S21WCeehb9xW9Mvnx0DtMTDbuo3OXP_OsF7YYKahBrM1nlkpz1WhXmZGZegRsj3n17ErNh0dVziZVlSBxvYm1-rtq42RgUQ4a6SCqtvrf_yCuFkvwsuAY-O3uCIeVhm10oG3UlQ_uhazL30S3BtaHI3e9lf84N2hk58uXzR3VL16syLJvlnf6Ne9zoghL-UreOCuwe11ZgF3D2PG-yseCrsC8UHplx4Swpl5fbd0wyfN32LQGCGpLwi_q8lJnz_dhrcmS3JNxslTGsJ7Qk4xTerlYmTT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVZT9pg8SngPZiYyWTCdX7AH1pmen98YGht_j0acoOtQa0NaSxLjdO_4skEpNUZStvzSd_w6HxsyEetc3sBHlgQYdNpNlgUwcLfHRY5e1zBvILnUxYUp_oeVPizMRDSQSc1PAVNR48MBGhaA3kJjbwUTwRX_CSJI-u6sx5POappZTe2rs7NdUgou-VznCsEq5Pv6t_YNV_fCQeynv9LNh0SWQwufWZPNnjtxHm8cQMcDOvGI-7S3Qh6yfcZfWjU-1fGhZ9LA3263ldEZRiUUjGRP9Wbk92pSzvKlvlXi3FcTHQS2GWrsFySiLDZYGxTrIOjwKJ4XXGF9IodDxw5eCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgZgU8Vp8utNb6vDUNrTBMbaDKrU34j0HAd9b3zcCnKOatvfE4mVn0nrQ6tKNep5VAOJbLo_cDX0-JRtPwvTias_YtYdzyIq29DAHv3VWs0JcRwF0xkUfUDtkvoUvp7tvRmJraSzDGJ5eH6SvL0Sn8eyO_uU7n0A_SqE0kpxbqzIFADBJx3EqourN3EA-aAzA64uqu4LQwq9aUrJHPMMfZNHKfWmsJhUHhwkZqOoKj_3K1KgHpwfIFx_xBfvV4_W0zRYygjOmQVR76yhJ-ud8aFVJKdEOAZiM-0GgC3JCFT6CALdRalsZzV9KORPDR2Rr_IRMT_BAUqIkN3W3atluA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyLw4O56dfvWISxJ8WBFhMqlHxzO4ZTeXYWH8_KYNyfnGj8JfzdhMwk6n1wPgKl6I1WQzaC58-VVAW7BHlVXuj-W5TvAVeqpk_CcNFRYimF_-tI2erizFHnhsH7ZqO_fi_23gEbUBlY9xEhkcJNPSXfnq5Ur7gzr-0T7NEcN5Z-YGZwK08DVlDHpmc0GCbUPLlHRuBjdy1FwX25XOSWZAWhMsny1jO5KUIcftnCyPrwv2bPoCyi1oP7leCutLm4Wovdpyc0957wORmeAsIGdWf7TphR0oVx85mc-9YQGfDE66z45lRGEQqngNN70NxlJwC5EZ4H6WwgEG5KsxbA1bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIi4ia-ciKdeysDOTxLPK5Cy8Yt7AXXAGexXhW0XsmyXrtS-xxOWuGyNyucr08sS4ELKRDWAOzyy_0qUY-GHXPF8WmOd-rzZKYWz98Yi20rR9HaLm51Dt5ZYYqNzPD7ZjZXBZ7bRqtSYy9cmJ7wgzUeRflMsphKbKBfvEN0OOEe0mlBA1wtqWjKQukyqHn0_g7GaL0BnWXdKFHM8vL_2cLGRyE2pSsdV5OgLSVnWnV5msETa-z7nOxZNvgXJEiMNNfrsCe56_hdrxDxj-ZE0YkbY4NL-PS5lQje2UskrZ-d3hflg1gYl8QfRKm_PZm2X1VdQLaOSYBPBNW6E1W2Osg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlhBdbqdlQoqGUwAE94c7YOmE1yuLwV_45J2I8jC3L16qjmBkWzOMXY7oNEmcSS01LZU7BWEd6oYwdY6dB3qvbQuXzQ46RpQNIprfEQa_Y9hxnljjDjztDn1dl2uKBnngzv_0WkDmCQXMu4dUwL9zAotO1hegD5Jm2iIqHYKYyEJjEsft6lxWXu_rUemJ3s7T8SFjNpJA2ER6oSlz3v6RcChzblT0P3xTslfZFDb40VJ4jA9jspiSwg5vbgiPeCc8VzUM8QbmekxGVdeGvJacPlqtVlGE6GKU-ieIRfWZY-fgtJtvee0KMFszHd7qsxlkPtuQ3J524ltPUhBUTecQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy5EvXsIgbIIb6P16v9VU7gbp8-UrfYHtxUTQwoo0_R_lZ0ISKatumd6MFc8CItbY5BtUmAw_MpA_RKy9EXoS3f7l-vAaPq6HP3B6yxA7UFtXV9kePWk6OvjVSg0yEINrOM81tnJm_fqHZlc_Kzz2Tv1g76JgUbkHKp7OGvuNxXIMGgp-1JTq9OjtM6tyjg5YZd3F_JxGwEdMcg6qoEdDPxp2TlluLdc2VzG-DsKPJwqeXueQ4LySALlXIqwcglPhihyOKzB7_nWHTZYHBaAFU5GKi7fuTeLOqatwP7lFXuxAGeTDyJs2_Q4n2-lqDCVEWS9KBocmDWan6MaZY6AKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSFDhnWsY6yqC9kUK4SSSfFJrGxerflYLin6dRCh3Lk5N1S7cDZEcsrJyh0j29TwoXnMRDRP_5tWOZtQljsl19f23FraSHrPQeDdDS3YlKhZSQ8wGnjYIGxpcwcfjngMlXlWEmDHa2csBq2V2guxdF7LChhUx8iuNqxLmWbFwGsXEAuDXpxtXbgBLjkqI5iWW--nOPuHXM5Yi9xU_4_FP_Fd8AlyBaNtWM1CAowJ5Dh1PpnDYj5TzpBSxAaoIw3kQ98bZiQQqnkZG-v5dM-iCzHXDEncJml-vp2e2KOk-sFbxU0NKFJOKOWSEw-H3HSWKZeAeplB2btl1yiierLTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heEmKM_qvM8NGNYY8_ueN1dhed7JkhzXS8nD7vLbqIWgYw3EAbNPOWIdDzEGP0GASC1hmXYkR_U1aqTLJxy-pvsHG0hX7wToqdPBi0CgMvJLCxO4C9mb_d6oWOVEMTD8Pl7ICMoFzFQz5LIXeY_1C0ZuJaPKmbDsS4N97iNCtFe_e9IbL7OGqpj3IzSYkAt1xulhrF2AiLMx8dXYJ3lbV976vidPAOR0HgBL7nmJSLnVUYulwHL071Z_wKHhUvFrhuf3GQx0DXnaEX67hpWl_D-BnTvOp_U3px9iw7XsvTx-gFWzAqtbknnBszDeMTQEFULMo_AQE3in1rMS4IzPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QrKyLhjqvnCkMrU289dj2DMjOOdeB1exiadZKYDHwvmYyvw4yFpwIBSGPF9rqfi_X08RS9dg4m3I7_Zj4oimjEn-Psvz0IPWr89yVPxtTez8wZWFcRa7F6VopYnbXz2fS_YCa1Q4opikA0LnSVm2u_1bT8LimP9TqEpc4guo-wXNerwz-3bVUjmqE_M_nkuRirlOJtFzb9kQT5KNnnbKpLLCAc4Ba7H9N81LqdqVpqlN9pGzpiNkKI6qSlTc6k685ifl_Jqza0wVP-Wp8z-G9jnQlbiX3hdZN2JXqJj5yhouhMSKvIjLn7CnvgteGJO-OtS4cdlUPKKijUtsZ0tuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2rHi8S7gD84CCE22L5aRmGN8EYeHOBDRaBXqr6pVITuE2x504nlRWByB5Gug9auLvc1fr1pGdT9j8GhAh5EwTqWO2hLH5ZrbaIS6j-k8qIpCthEGSeZxiBnQPoAWuDYJKuchHsM3m-X-GiF8aEMHQQ4iGYSLTlGuA1P-KDqwCad5U5XhSItWphETWcBhZqi41Zbf9clBNeoT0YIblqrPNMqPM4dQ0Ak6grVtrLBoTFRmbx5UZxhLS0_c5dhNY-4jYDP6is48ejDxQbY6X7NcMF31MtoYvYEAciy-e1o2R3cvcNyGIK0PDZsA5bQvG2dtOqqmgUbdG3g5TKQZ9cWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MqWTzu4v68yCAapoUBoBr4nSeN_GOtnoqpGauSvm5epyUFsMJoWBUS6xokEg5Pe29FT7NuIFKjg6ABR7EONwSqbMZUykTAhnJlqTnkinCh81ojFSz8RuRluViV8eZNL2-WhWisQo6FiU79gWwAZfdXoblQ0OhI2yrqwZjK0DMzt_pmbp3I-DLrmH0MtuXFV7sUTY5taJf-LIP8vsuetPzT81dIDmfYBQCKdJu5Gwb_tuPor8QbMReZ-RyxDtCb8mXeAOx1R2_p_FH5gifBlEdQFDc1oWfIOpZFjTdt2IIgFlEO2_H6xse79VFwEYpkdsTkUIH2GYLbwVzjdRkkFg_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNYOyCQKIjhstfWdxx5x3wIKnXDe0XFDIEHw8uVb8iJmdE9a9MUMMXkrRvGVgQjKBzTxH5IuvbbZhVgnwjtA1a5Lm5-q_vBFSFfOhzK9xb3jvZseieGGp_hZ_76bSNKOOIKfIBC4OHj3QBwl8PqnFzKuMcMbQdz4eCkY5_5cQtJ7-GoHg3upvtgaH3Xxg_tfAyM74s6UBy1_SqmvX2dbTb7svCa5G2mm4B8FD-sQO2tN8tS6ay_xmC2Ao71vrBNOQEXjPjbGVcjb8NA2O0qfe3wUyslpI5PXKYIwPAOkseuexyiyqUWagvT97GxyGoo4XVVtaJ3VsghP_Vh5y9QOAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 582 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcKPnHSQCS6UN648_z9sGUKcOXdSmkKeDNNMHAkU_TcYzcKCVNDx9U0fdsdH7Hhi-wwDPgp8o62yG2d-_1U0DnBqnrbS67oSt-_EkX2Fh6hGpFLQguTYUGZrdTInJVWADoekpulDHW_jqJG4Y4yEoQw15QewqCZtMu2aEZd6ZyCivCnpj21fFfJ8AnVt-4D0IyS68f0RMv5rgaRGMlflpAFGQaQruiMRlC1yDcKKzQTHGCncby0BpB1Y3CDbmBGZbZ5MPnyYYyr8oO0J13Dg1Mzm9qDerfvQ3HY9xXpbHmqIidmPOW_sroS7SBb4TL8XKeoNV-cP1TsjIDVZlkZHAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 594 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwsfDaAD0E5pXDTCsL2DpJJQY5LOBv5u7CHna4e4jZj7MJtNawHRNhvu58aIh2-fT1lx-bjPzU2pUPIoYdss2Zmdn8YvOZsP_GszAoS-l472H3xCmSSjy4ZQMUYK_tTDxNnXaYHN7pREtdTpFmZD6mpar7rfr_ylmiQgp3lBeUH-5oyGhWVe59AVGKceicpl35g3gUI1fqvdu3m4eKnNxqtPNWt_NY1vHjPl6rh4nSldDJmyrOeg0fFv2bvm0se1VXjURjQyFJF41zeYDDI8cnOac_Bnjbl_9-INQvGkw9yWQi3ETp5gJx9ZmVSoZ8JSezsroB0V-MeqC03N1cMZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuolmEB6-YDtAP9_gU5Io7ulDImtBEWzdLkn6jgrvktcEzvMnBrRk6Re38a89l70RKfu9v3LOz7uxnqbp6nOut9rjG_F2fIx02HAqMRwUqzDIuI5uCSvQbOH1BfPStq4HhgPoj63p8BJzjCL96SYrmIwT9EMmwiJsvYBudlYIUDIglB1IBhT6_Szre-mbVdmHj1m1aeI-OxWPC1AF9gzf1g37o1HVdU4BDO88NixZfGOpWGuNGiLCn3mnzyF-EpmV9NSCwnJXC2Gm2kiqf7drfSIxa3wJBKiV2uLaAYTThOv54T2KFT9Of2B_BY94iOF4Nelbg3GUvWY3TJcTkE3kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 647 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ki2qxc7LDRfXyt0K68h9H5kf8ItIfwNtZsVM4qWYGr007GoMKe70D0VPlZ7SdYGV8gBg63Yg8rE808n03bIVBo_1dPzIlgFirVWBQIqyP9Ux5Ygv3pvEo6Dn9nDNBG9c-rDuYqTLHf0iCHzfovHHwOrtaD5gPalDi2mvUQJz9jQQ-OEPNIy_SMgBlhMqjNaJY-04EmGEb7xhZjLiAGx3LXHDBuG8GwgeyTg0hi_OHL17D_SXYMctKj7feGuMbqalRKZ5ps6gQi-8abGTMNIHQq1Tmpfry4G_r5-h7bV4OE-n9d3794sUc8N-4r4wSvL8xJtNii_yTxh_KceJEp0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 715 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL-unIJezrlYZEAKki_gTKTx385Evvzj8DfM5lA_Tq3wNYGSQoS00sStIIUonPOGQDDQXOZalR5d74Y-WmCx-lCP55tWOBIRwvyW8VslLYVbWYam5ht8r4qSDOCuMUek2g_1_wpC8CZuo241lQLtQHEUbr7faQEMFYtqBDlzvZywJLnO5q3kSB_Fx0U22lT-ulPYW3f95QO1EbOfkUywT_bS94HuLZko75H-W5fqEs7adrP5EKP3tqH62Z8bPdEICrwfJ2BVpX7N2X54csZTkOLAgjjcJr8_jlVLjNLfABrVqZtK8PsE2CZlqBo6GAKa8og7vpH5dfgGHXqh2cd4HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkfR94agGHqbFcRzWnjXh1pLEnICgb1rOuMQNM078_Jo7ZVCBl6JkJ--GHzjdhSiRUdlntZUYcfmmoVWlMgSYCkkhFRVNzUsoCgyF3yfYOGA0pJEq2pUS94aW1560f0p1XmVY__fb81a45Nn-fims_VBI6K0AB-pAOoIqZhNIpJ8Qwi3tyx7APeZchPnKVdV8eZdITyVa9EbvNOWt6trvTBSi7t77OpSGS7YL7QncXAinvIQGfjJojGOX4sSAR0gI6AY9l-emHMWXcpjLoM-oh-yZepY-0MlfaZhAnr0QwqfimgUOStSz_u4w09q75ZjRU6VnLsKdeI30XxENrI3CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKyGhD6jhw11fG_zZYnEqH9XuRwpr7cIvLppkaQEDRAvpHUYLtAbbTbOgvsJgGgJBN8h7fhAWOLZXejIrdDTuryhyNNSaYZ0d6JwsAsIZggfWSQc-yYmUZ_EZSCxKUVfX0l_65kx_IaXqZe0sGHHcLFx1sT-tv8Rg29oUbvZKglToq8vBw0HCDYYlquMPtd8bZRLpN5y5OI293i4aVeAv15f-3TI29rKxYrobIYxzggH7fG_2aCQnP_VQ5S3FuckMurJNiKWpN-HH2I0M9AvBsIa2SdB1X4UGskHr_3ivcze_BfiqkzHouTDR_wNoHr7v8LtZ9UyhRxNeUn3ddWAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgFlHIlJ7L7Jc_M7TSzqiRqWsxPQrjPj2GsyAqwFy6YtO9cIOliWw5IVDpYZf17Xa1oIopCv1mncLgqGvYOGhNJV62O0SN5KdBRFDneSgKfWBQz0s7oSqgbrzWWH3Ecrg5g6kFKeTlHjD180I422yexjfujM6V4Lf7Wqchc8rF1B6HJ8lXgtzxLXWuawy5dUiVob75zP-3aydjy91dnJFcR5O_AbTC9NCjQ6gUVe6g3NtO3RgBMePiRWiqqUzmuwxRuT9wmu6eJAM1rSPeSXdxx-32rPNcJiF8yISJEm0rWZ5TtoBnDG72UyJgE_RO1sRAD6IoIXsWdl5x5bFMFn_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv4gGXV72_Kt67QZHWKOIrUUGL85c5PeWvqFP3KPxOJP8SahjCI_mSEX_n5ZZ3gQTAy5OfzL2QRLDjxXK2pWl6GbwHK_tgB5gCLKd63Y00LT-yKjPQNsvkG1XdlvlGNfzqBC-90JbuM-z8t1x7jYhQVK-LEmFHthTYyDIvCwbSGOiZHRtzsBMlBALKjSjLOhZfC_tNG-4AMKfMOCSmjoViQ1UyO-bunWakuYGRwKtUIBTEYk5o0Gqk2s5aX4CsNHKBXYOo9SEEIGLahQL-VmZVwJX17UXcKo9HKmIqRQ-QtXMAIZqlP6bjuhJlwU9mUKjnBj6ZaGjcVvmhW0lPIgbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 546 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAOU9yYmKQPIhaSD2RrsFqpl8xaLuJYYdwcqSis75KEZStUdpSa1DSthtbfba0DnqWvNpjae8-IEFSa1JXKgTi5S0GpZi2PjHF-23fvkj9S9Inmta4vdggHpJdgCEzSYNm47mGyVVDSSU1hhg8gokWWKWh1XxXKZZvMHUuwRpsybPz5IxJh_IidwJpmrk9LHQkQLwzqUyBdFycdmVQvkic-8f176Zv89xPPfw0BLm0aAvTkTPO9KdiJ6nfLzjh6Wi-mbuuCVSU3r_lnlupHIq_VazVFBz-Z4au11lcvvEtZShZ4-uywkVoLc4PYWAv34BGRkFzCrTNSerivwaffLew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njrXJfMnAX-IwUcZrNIOeDdpr51Fa-STtcJvUvNcqWQ5VD3GnUtAnWE86d5GoLvFNSInatPdrt1ayYwM-1LUPzqf_yaEOZJ0a24PD8WymQGXZinr5ip5KFHhbXjy95wr3Gv-CEIWotcmuhI1dcAU2f9asXEXpbD_Kk2aNsOhbX-7rMCp2HxevDCG8r24jaJkzZcaWX8r3NXtvTyZclyJufPWc6uQYGlw-WIxUTd46hjUeYCnGNXHwSOHOLkfdpK5f87a66xUlkR9-vbKOcY-YgYK1wLHAfX6TD3BoxAejITOyKOS5gDR0hF_o0LTJdHdVHZhN0uMSwC8A5MiWJrmzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7-qg-zdSjG-YqkX84f1tVYxqTXiw227vyHQyXHj6_1vjV12Z69wF0y_sWnIwpPp4PRwh7RmS95joBYPpaDWBKktUVDg2vAG9iUmNxlZy5Zdacnj9o3vRG2HmMWKaDLL7IvJrstEef5zMqeFiP6R9N4PoRVwgfkwV0boa8ZSG33ti8Wz_dE8uyppIoc4esxMq-m0DE6P-5XerspYL-ZmvYbXS33PYmKrVcwkEroYpGm31c7x3vieasCMlOC2RhZYOjUu7nZtI0Y3zE1JS008q8ybi-cmuVT8ILWE4dRlBOQV1qIukfNdGCDZke-ZucZQf6jZbRdHAUJK-ABmeq-zZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
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
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
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
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p58burgxtPdhBjbwkjYsW-DoPIs-lThhdVxAm4tQtlRTLYAtHQZuvKk7CmhOS_mMq8udTwaZuVtKNMODurHhCrFsXQfP5wqRYeFT0mc4pubIFUW4BwfSaOgjgB8tzYqeIealXbvXW4nxG6Z5yYvrSw0rha7do1Z5eaMWlA-JFmTIyu46Cu3qG3tp3lq2y6JxHmmP2pMB1yqsTX-Sp2M2PGtSE3m03U4Eh7cA0lV2-agwbkNr8aFidtoAJJaGksIsCcUMWHxArvD6FblEk0TCz4f8whn5ky0GXknARVt-MywjoPZHwMVjm1nodKTQGFsvXviETIVTEjC9K53rS_48uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtFkcCPraI_6xOEkgw8qskRtwssM3ZjHqQyZJCNH4wx42bdfD6G6er5WHsBWi5hy_VftxWD4qFNvHcKFD2AxONJqdwDJywCowjvNqbpUed37-HsR9JJIBtq3KiKvEGs4UtTCPxJY2u4FjzPTsPEuvpnKo_pbZY_8qbjy2DQ0_Kz-2yL6UFq8ss-MQejtj7VOhoYVTN5wprI3SqO_xCt5BM8T-93o__29n0qP01XQSLAL8zrMkxJoN2vKcYyz9W2o08IqPOr2G1s3pVoHq2x68gBk3-dUDGqmYchOj9ilZ5NJ8G-fYJHdqttedBWJvajyihtk-fjNIWefbpYQOTd-7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/em1Xoj4lG3IEozC_kNZvnzuALvhY19NcstO5ya7Foar46TApKVC0g9_SGxLK4wtD6G8Xl8qstlRwxb_JARjn8uMRSQNV-d1TmiVy_iGoXun7sdurwHI5s6jlnLbAb29ZFi7GpWBrx5bMQUSCkin2Kqwg-G155Er93TWuhiyx0LftkQOd8tXD17EcdYymUR_TnVatampQnGtlhPv0GZwT_WrEQX6Ayt8yXt8BRUrC_NS0Bi9nKI9koxYOjMmmFho4Kghy3t-ARija8F7M_oMMzkClqr_BTS2Z-Yri2EyNUn3RGX20FqG-wLNmcbIc3c8OiybH7oEaU2_HIHyxMsJfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLJv0QgYCu7Jbp--EzKazf6joe1J0Dsu_2h5aWg7HNxaChouRHfLFAIB6clQYjO5JhjmKj9Q9k-XzbuW9lsO-D64-bQQOI8b1s9ScGqeCbyX9V1h8Am3EMjwprsV_Z4v-2dMIJ8k02CACjNqjc-ZP8KUCtYvdPx1c3y8JmlntVXL5Y2wmVuGP9OroHRJCCO4A5yhf03NccqVHRARv8tm4McIiuhXFwiZ7yelBHOjfLGn8iL-YJjVwDzlRZsSL7V6SU4Vk04fY5s7zoyN5Zso0xIcHWfvn_08Cc9wKNttO5tGB7yZl8DEsP1HiJy2AkQriok33Yf3x4IfoaOM-Y-ftw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdHNVgivWEJ7MnufnpPnzJ-fatI5j2wOG_OgUMfLBlb3viR9-MHnbDanD2XPQ1HXSysZPYMJIkea801zqzxpRT9eMho53J7ZSuendLa36FAzKuvIrdK-_O7ao1kINB3gVLbcmpV119Owo9cfRWCZZ1wabdeagX5mD0SrFMB9NBBJxOGImkwMM5fRVJLcUFp-jpDWErCxmxTRfq95pKOQ9MgwVSC9C1HXT9u0zJgpdJWiKpmuZ0XNryK2ZFonMZzEuW9_06HyJ8Dg2gq_VUUnZaBxzmZbStZcEwHF4vjaYvglzPIWqgmFjLThjxguniZpHQeN5ZV5Ajf1UvjnLmwQqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJTyEOHL2a7UR5K-jSAKuiKPuMYiewxPw-qCPF3TVAvzfx0F-J0T02rsr2lHd-sp1Xiy3zarjCPQQ2x-ZfkqpLbq366MNTybIH6FPxG0uroqCCP8L-x7Ubj_3G2NXHAmS4EHx4n-6mz6Tc-usl59JecnQSXzm9JY_g2wsk-6IJiTWFfPksRRdRocPzWcjsHpJ5GnVv4mmJks-syUH7sNRKod_d8nVktFRX2ki8MO4r1eUa1DZt51IHjpaZikHJAEEZbkjZkR84CNkRw7c_c-QomBUoaeH926eizmh91A7g5ado4njbETXesLy1htt712yVded09Q3cNi6X9XA5FtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGmUNLsMu1kGnaA0FikrbCSIU8L5lhbP8yXL-nK3D7CEYONo1LFmTLttoDYKvCzDFeAmSqJaqd_4Wnw0xh_znZzkJl_dLIs6Q13EQ6nsUXySewK8KjwPnFXJK0rnbuPlFcqbkNgpnutj6Xn33fzhyOrXffavIVc_Q2E-BHoFW5ujEGlPvvclgW6q8rEZkZ1DhbyC2t8UGbCPe_ZgPyYqRpsgaEBFAu9evYr_tRgzSnHwCf3KkSzZ_3OqdixCVqTsKDq5fy3PBa8iI7SCmUn21N51vTD6-ZNU2WSlqTDggkWhy-GPdtuqhrQ4XGpk0yW-XPwh_wjSlSn-Kbkw1Jg1aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlqSKwu_gsKL8ChXHbxCrbSZQeQ74k3ewfAaKKrkEx6k52kQtYnbJ14FZPYnEXFpLakqi5tKfyNCNuSIWp9gOeRxP-XVTovCGMNxlZtQrmdoRfr2junSWrsIfclU39JvhHT23nwzsGvc6ZAIyYZEwuvaln3PxHJBmtbrJ9FfLTlm7TfVT16c7Un3qvJ2KEcsV2sWfXyy94c9gsjGn5mV5wNlvgdLWquE-1BGyq65zdMA0aOOtgX4KXXkmhTA9ZWo2u4VnMCPTsRt2fqpYmb_6S_E1HtKVY0vfj7ygZ7EbV61m8z4YD0wMUZTvCp4rnpdbwvYvpycB0uEGSGN4hGfLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQcJcPypnU3rc3huoA6r5PT0raDaYbt66lH6AFtvdHR0pdKA0mBv_mNIyMZpKM1YqxC9TctifMOix3EqaMyjPokfbv-tBCCliHKBzhMALvr006bw2wTqRhB46B9WWjcMfLognqa6AFuJ8_mK3lFIaufn26Z8Hp_TFWFKNvtT4I1LYo8zrzmBWgX0mVhwtbHjC9oHyZoZAOiLX3cnRNviZ6W5B6JyT8uMpoOj-x-wwRAs1afk0-mGdETUiGHp2tE6wXhwtMeabhVj1mngtVXDkh_CL3qpI-Rh3nml_N3musU7xQ85_r5DpzXP3vzom6ncrgHep94vZPLmil3sZhWbPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUOX-NbmG88opQWhcHrklRJpw6_kicG-9WUf7VXCCoQexUl7QEHrxDi1Y4V7WMg_NVseZRCy530QvzVH26tWVxQGsJWoRf8NyexepcMZSmOUSxAjyAWTAP_PWm8TpIcsy9WrKHUXxONBmk74R41Gz1u4W5LnM4amO7QdyvPPs3H3h2riQLuWytVJpUWMfEYvp6TlYv3PJS6k5c1NmliAoiGNwDA5Icy_yiXpv0eldtXrMWjZcwSNH77qQuvVzm5Bc3nTeq5Z4OOnhpFHac-Fgx-ct2MkdINOAIU1sZQrGtOj2IBH146r3QCEBHCIVr1cf9VqkwD4mWbQCeeh1zU7uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMWLw6pVK6jTtilODlM5MJP3HidBx7rLbb-kUUbvWe9NkeAMtOGGssownoBshTgcFPsFBNhJOeWXbNsKRO1I0tDZECoefFMaKmINq-x1C4lop06Nr_spEns4r_9qZezB0fEBvU1AbKZPUs6MOvycH-WcjRh1ybwv80C2eh7Auo_HZblfLdwtUiF1-oYPlbOb_Fq6LJdIxehNb-yu3nxy6dTdQJdGXwu6wmJfbq-5xr45uDK5hUIocfKWPVEjU2hxpnaxJyesww3ylJu_HwGOAD4QMKEvUZ-8tD7_wzpogOaxmIJHPH3CRmbxxdaRnLef0ZAuz2h_O3YNudT_dl4ZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdbDhZLVt32eKDywVU9fLA_guLBNItz5Lj2j8ii39xJ_XQMny8nx-n2FJjWRKDeV9Ky-JsMFHZxJoGs--LdXA1UpE_C0ctDhvCZDbHXIBk9_pq9XB1j4WsBh6NYYa2e3QAFnOaq14Y-8k9LNB2hgqJXAjPrCRkhiIRbKux2TiPWLK-qn8C3mZa0YviuaIwnccQH_J1dUZ8cpmPL79pwW88AbB0P9K9p14YWCxxbSaGNePPCcEdXIxsAOgrhyUAdZaN_yjmTLyb-5c2K1TeWPINQE8UGsRTGtPqqn-fFg9no_50eQepHYVoJ9TwZQz0TR3MZ4kCmskHaQUgdLPFWjxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyOsKVH3mHXCkhpqtMqMGeGB9DUKsBxO6kOSwS5TORgtsVXcQtaI3M55FjHp857ImBzXOFlKdOwcXsFXQtTmKHouWxxPXW-iFpNqvgRMuqgnpgq2r4I0O0lHDIoKUL1KlYkmAKlwzERWzPjeJioMzyRGfJHu1oOI9YVzeRS9RU2y8evtnvHI-aUhKHfACj2Ssljj2D4PzLy7vTr7rkePZtqZp96R3sPFTdaVOHTSz64hS2qdK159F4ui3WykKqhK-UoTRlKmjavjNtithAnoBS5cZlqmH5gzEgimNzaPHNOux3mdnviA6z1Y0FP3RJTb7QswCeS3nBfEUiDtRndoKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixcFp-snMrumvP5aphSl-pfq4YP-f90XLD9A6qum0J75oH5ZzUjcKxPKh3uJovCCaDe6dXjAKM2C8pMnRijG52h9TaxO-zIj0UrvwcFbseyhTd9VQYOxdfOiNS5ZFmla565Cv9-Tkd2DKU7k9FtIJH7e2fCqpZTxuxT2MJ5PSSkS6pYripjpVGbAJucdjFYWnRK8KF9n3hsI6cKKengXfGnfjzzNI88FKMhCZsljyMlxyk_7s0rIt3Bxi7Dgf-YYkTt7fhViKQxLuZXJK2GHBXrl4_hYtBBynzJhrQDiM9n6sIpS3Yy24T3HwPMxJtcKBxfF4mfHMxIq0jjXoetNAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1_7_rIWgTirAR3uWGEuR7XiufjB6GuexFUDtLDjfR-bzly7qX_oSfpk2OSNCtNxTRfNyYDR7qY3ynxUvJ5cosRSKqyU33RQdKbfHr-WIHbFJ5-N1GABFBRsGnyhyE9Uyi0B9LlT3vJculXjS_sjj4XGlP2z27ddWiCRARRPpx3z_RWYe4y2Jy-kqeokYXbkjgEFI27VMrC5cA4H_tnxzARGf9LqKBuR_m5EFwe6pa0F9ag2flC7wq2MTt7sXULqyntqbEfkC-y8q8mAtqC4y4lwTO7QtwWWG089ncC6QOKT3g3_H7H6CNZlEP-KW9ALpfObKghwBI-xE-2ZqCjMCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpGo93yixT5BPx1BBgGLuSfqdcp5Pvy_6VyhvO4FuQhfx9WzNtDObfBpeX4ijZmVSwuUWMqj-lIj_4FP5KygUOA2UAK_lusUioAgZzciX_wiugC_Kg84pDFp2ha0wMqskbJHIOrIed9u_ES-_qaqNc5_eoehmnz1CZOUO4iJgLS_MY2Ya3DojpPxj5A-IbpScoeOGQKkf8wzyII5izAwqDtjlVjxfGl1n2q7ZFjk0eQ9v0OMYXJwapFrgNe_fd2Os2uAq3EKbc2gA9IiFk4NWSwsIE6oC0W32thjiuaVifEh9S_WrsTBObx4Hp7QB8i_bF08cWzd2eDEkNGNoNy-qw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=rny7EdAoCTmdY00tsDW7KFvkE1JOZPtE1XDgSzCK_IpZ4KYfAzqlv8J64CjsuC_61o40twyDeKmt0mULfdIAyloZ2Qw9LLPzM_h5DBqZXM2fZ2F7JPPSezAThi7cK5hf2DaHweRET-a6AEFAeWHbm9cwfnIV69RwHzMWp-L6nYt0cjwjlLe6M1i2vm083xsZikJdi5AeGlH-6cQe6CdqTey-XCF0alG2fLsi0YbAUehLvYu0xFFltSx-t691PZg1k526dVKch7NBzHLKYfZ7cByOfwIqq5RESteo2HHQexP3YBxQKi5eKvm5f1efJwFtdaqbK_iLZnvW99XIeHFZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=rny7EdAoCTmdY00tsDW7KFvkE1JOZPtE1XDgSzCK_IpZ4KYfAzqlv8J64CjsuC_61o40twyDeKmt0mULfdIAyloZ2Qw9LLPzM_h5DBqZXM2fZ2F7JPPSezAThi7cK5hf2DaHweRET-a6AEFAeWHbm9cwfnIV69RwHzMWp-L6nYt0cjwjlLe6M1i2vm083xsZikJdi5AeGlH-6cQe6CdqTey-XCF0alG2fLsi0YbAUehLvYu0xFFltSx-t691PZg1k526dVKch7NBzHLKYfZ7cByOfwIqq5RESteo2HHQexP3YBxQKi5eKvm5f1efJwFtdaqbK_iLZnvW99XIeHFZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myi3DPzDVHUTJ0XjKK5gTAdE2R2F3QHNSe7bAvzD_xl6cH0awuNP09AUav50tQrPHah1M4kBwfy4LSgh1S7fBEGQfBtDqEqL7KLOywcdaBnkyqPfYPs6DSmgC3mwctHrFEyKsH-VtVRwDwA4QX6SUEtc9CL2z98gH45ywnYMsjzRvshyBjuzW0RHpJ6hq9WC9psT6QFktLpQzX25dQQ2KBWrQZK08clO6XLlCn0WOfd-5NZtwXqQIhN1viNRMowvgcJ2inj8DUy5vr_pxlN9LRpMI8OALRt6P86EPwSg3AG0h0VRgFBVMeDSFNv5e4O1_bhO1wSPfteTIwKSHVy3mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_cAeGEoT0CSYRYNDPJskkvE30OpFepLx3kJ_nkdT9wVlQX8ZnJNKOzYhk8hA8olfemAJFfi-oAyrZGh4Ef2mwnrs3SeaYK2YH-cscRsdzHZ8910anY4NRFzspVyUMY8O7KLCH8mVQuk7aTTP28yK2W7CSb3S7G0GH4nVmNVkiZDWtck-4VqyVKGn_ixh6iK1_UDuyfaGAPa1avw5mI3xTfniz9_mmFD9jybGmoKF4i8AvF3OOMwYMDKOIo1s_yi0ZWeIFxBiLW86DCA1rJeuB3Kfmb0ouVz1OA9B4Wjc7TmTQMLm2xWLqcGMWkxruySfmggH5tBfR1UZvVIPVHPvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMNPC9ydSqBdqaQPvuuVcreyIhy73BjEmO2OeIVzU69o5ekLM3JkY3XTIATL6vdZk4Tn7JUiNjyoN6-RONzDXa4ga1tvc-A6fPS1Ii4Ib8SBFFbO2_VS7BsRThshfY7Ne36NbAaxi_bzzrH58IVeYeEOUu_XuwEPZnITL8rs3jeNVPuARcPdGjPryvOKeceDW0VU12Hf7RwwJT9W0WSUg2sNSwdx3l2w2afikz-A6rQZRCtVEWIaH2MIkW3zGNpD3fP3sBxyzQKLxNElBCgq-0HqHAHJghWOg6IK-Z8-Wk061jFlEyahfsUT5sod8WCemEF4_4cpoVv9Y-rVhVxZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNLS35O--B16F2a5c2BMAux4IxavOmDD1WzS3vNrOyxQp8I65Fqwt1jQ6Co9lzqMoW3HAb6xvcVjZ3G25xIRQx48vi-_zgx30O3e81cja1ex7dveTefHGYsf_QpcSp7Q8LOQU4-NcPFJ4DCPQrIzG_ARua4nT461iTfthB3uflxyUftqdd3voW_ro4wl7BVskH8gNkoTpzF8BQhcDvsDoWUC3ZwEH_dPqi7-1KZMxGC5NntexZbPKLUidjUF0YRB5fviOyffHeuPtqvKfBaAolErlPdBv35Vcy90BUD__uKscmAKxyYvddfe-n1ZtK_YECunJdAM4ZaZQPLKdJktSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-gzoR49ecH-d-BxRZOvenlZfgkjGczLZrFKTN1PyDQe1W0l-qoke5t7cbwRzHRqcyEC-dYOfeOKlfxDATSJnplhihyNGG5-QLf09y_91Drz8rP0XtmhpMyp40jwSIkQHcWt4lrlrLCFNJgHTKfwbSTp441Rh1iANvqPPfnRihcqOEbiJpu7mRvvXVYlXxBsXTcA884QXaNTCR7IEObrLNg8MTzrubJe1JYguGToIrTVrcqMpzuRmZe9U-svX9OUtmC4BNOTUxPP7WSwZuqZdc56jt112Wqb2d7LzJ_S76tSqljswBa5X_WJWKWuOP8AYM0yD-feAM2H1j8jihM6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGNDYgQrb0aOaB-P0KL4-hq9s4inzFfG8NOTc4PhUYap0_Vs5ZPZUbP4D69OsW2oFHLBi7vXFP9h41EV270oeFzgAF_jm3Sq92zvm0M0FTWTeTXj5LLr017yNDiyx6WLW6Yt68lnPwlRxeCxUVosv9CqAPXhbTzLGTE9NTNut3DGUyIqq2rmC0FhujnwIqGW4idZC9yurHFeUAOsNzjSUJUGk_6VLeeV9OtIwo4AsBWLeUIfh0fE8-YtdFUrhPuJp1YeAl3oKEY2Vd_9pUTt-6LbrwR3wqid4-052o06ngmMPmbWJtfpdqAuQa-MVWQanYi8hsx5yeQrdjdqEnZz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYOfIkJXF-5AB1DMN-DbitQSUe5S0eQtuCdmrTB_aBl5Mf94IGjgZLNMHEvqW1Xzpnh8zsClJjHcfOtySSv5cdbcSm0lwnHTBw7JpCHo3_Kj5Pq6CyCCwcPwKGDGXcA7hXNhDSTEqbs70--M93xGXEezgjxgNrirfNhZJHDo0RroBkg_eCQCBpMXxrTN9-xncHGFD2kDz1J_spWpayprhVj019V66EYv1eWstbvo3Pu-Nhxxvuqpe3MLCKewS8C7enZcHYogmV807EM-n-LifKiGWNKdWnlPpC-p4o9_tbuXBueakyDGVWfzuo2Csr8HIayBilbwiCgrZrpqNCGhUg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=vhGYAITlPChyYb-24SckxapOxNYbC0ho-NuH8TMpY4fbAvyl9izl0MS2Q3P8cRNDrWiQIijuRUP7pbfx810n-Tky-fJZcO2Cx9SqNEqiseIWS9__ncIIpqtzU6YbKNYxvYSiiQ9xMDZuuQESHO6eKIxQaLm2gXEtn-yeDzDiNkqE5AgOsFaoxln15lazwVyYWetZwbI2T709AITDjx_yaQcaOhknAWVKe5AhHP49dtDysvOD0U1KGLwyAkecC-U7n2u2-wtI7CwMBbFYrJDtfvVVO6MAskHd1ZYMpkVo6KPfwTJ_I5l-37qXWyb7tyiL4rRbCjQdsxU8LV_7YfUwGqCN_rUGuAe8ADFooY2N5iyDEIbGdx0CzIUGLAILS8p-19-pciXRk5Ti_bdmqOJS_l9N98KUnO_MG6C4Zaq4q6KGpjxhXmuHO0HYnKeOvLSLCazOoWC7QNE2xyxq2jam8rp_WdhmTcKgSDakYYGcSoPJlq3da0sUFM51qJqITh-kvbaZGuqODjhEDjRSNploGfxpfvMYighxU-speQ6SwVOm0SJmHG4ElXp5t1s-I4eRcOKfdsZTiSvP91RXTDxC11GD4UPBEFq96a2dgYf_4hv76byzqQeJy8p9Uknmj4caZiqomoGcHRY2sbUq2I_WQnWGPrDIS5Sa_mkTVkXCqxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=vhGYAITlPChyYb-24SckxapOxNYbC0ho-NuH8TMpY4fbAvyl9izl0MS2Q3P8cRNDrWiQIijuRUP7pbfx810n-Tky-fJZcO2Cx9SqNEqiseIWS9__ncIIpqtzU6YbKNYxvYSiiQ9xMDZuuQESHO6eKIxQaLm2gXEtn-yeDzDiNkqE5AgOsFaoxln15lazwVyYWetZwbI2T709AITDjx_yaQcaOhknAWVKe5AhHP49dtDysvOD0U1KGLwyAkecC-U7n2u2-wtI7CwMBbFYrJDtfvVVO6MAskHd1ZYMpkVo6KPfwTJ_I5l-37qXWyb7tyiL4rRbCjQdsxU8LV_7YfUwGqCN_rUGuAe8ADFooY2N5iyDEIbGdx0CzIUGLAILS8p-19-pciXRk5Ti_bdmqOJS_l9N98KUnO_MG6C4Zaq4q6KGpjxhXmuHO0HYnKeOvLSLCazOoWC7QNE2xyxq2jam8rp_WdhmTcKgSDakYYGcSoPJlq3da0sUFM51qJqITh-kvbaZGuqODjhEDjRSNploGfxpfvMYighxU-speQ6SwVOm0SJmHG4ElXp5t1s-I4eRcOKfdsZTiSvP91RXTDxC11GD4UPBEFq96a2dgYf_4hv76byzqQeJy8p9Uknmj4caZiqomoGcHRY2sbUq2I_WQnWGPrDIS5Sa_mkTVkXCqxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAYZooPR-ia7BOZGgaLKDbQpGOFNEYH0Bq-WVppUxTVM15gmTcpvDAErKdcaHctqh6GXNeIa_kGwRCgK6aPe-cUI6bweldPomrlB84FCkVgYm9Eb7XT-kvQa11zl6rZU3a4IPgky6mN2s2KU9g-AfO2TY_-xY-wDKIF0tcpbEL98h4vjWKDjuFhn1dK5EtjZBAk1u8KcoHuTYlfxThaLHC0MY39nkAXU_kCrjNj31eZzMpLFD8wJLpK-n7Ej3TQ0ecqlbR148EpyH7EKSyC-Jt3g0cLmVmgk0mRP0H3WBLxED8CL8YkzFmEfAwKRf1G7TW-8p5HuRgi1BkSDC4PXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5somc5c-XMSqfy_UqTRilXiE8p8K1NgNhVl9Q-eW9getYHuFCB3yWD-Sdoik6344Cxr83FYM9R-i8MfeeYvUtFf9X48NirsL1BiU15uJXJHSW86cgj9aVMcTqTQvEXod41bHA5Nz49zeDiI0UAU-zKXSyjIykqW3BQnmFifrf43Ha1PULwtEHDlFI5fMHLYOZfAJ88mm2OjHv5F9ICuPNtxoysJWhnyLVvk-eYIM2lchQDgiAmVsAw6DzGjYM3QVqoweLCjnQFeyM7hsrkLUAb8ifU_a93b74pdjEXe8PbjsS0nnE3bnXMX23r-2ErOvx3G00SeTGC6rzrJK2LiZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzNXbZ99bzhEkA20F2QDA0V4d5DLnSk9KEj69G-dv2KU7x_6WIiPNRig9s8z_JXow8uwkX2qc6nbWN7a8JhQ2MTH6DoPvz4BpO7y3P_LHCeHcur7FCvKVnHkdFjL3TKU9B9CRsDNOVKVh2X9fQOlbl5fsr-58GxVOK4GClumgd22Vxup_tyXqxvEwf7I3-STQ4Kbrw8vwSvoei-pKvf0n5yqNj7hS9lvVTJyYep_TzLmplqhq3Ejo6_R9wPU48K-0GZriZva_yRwun15VC9WT92iya23zMZ1Hs4rSbivEdXRc5JsI19HGJiqIniMvM6ce7rSnr_PBqbuMys80fWfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VODuw-FpLz_AdmgVJzIyJNkQtKOIZrV8rw_E0lFMiMEIHZXr0Y87WUPXBGaR6iA-Y2KGkK6X4y_pdivHA86j08JQ7cSMNGw8O8ntS78N8rm9PWy7xaFDFQhdHY4f6ep3KmEJ8J3FekH_US_fkIlxwBp630ogfNRGkHAKg8EWbcdj_6XEDKuzFAB2z7fzMlt6srqmAYb3sqGW66mSHsCwpRCbFkZf-ymKha9bWoNbvH6L1b38p_W6I9ch2XDLdCJi7PO4aH2eEwqelMQgFcSFEAS3NKzK4PAwmYWdbX1QzkfySiK97uKMhdizEaU8p8BeM0J9sRtzAv4VyuFVrmMBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYdRSwz9x91sZZE3Fawbk6BETnQYMNMiR3DtMoXtsWgMVD_eFGtxfI5NSLTgNFhbtf3AofuOxzTa_2MP3IT0_SvVDZ25FR3dzOGxuFTCAT9ltqOvwiTdnNzVWjztQvD3DR78b4krsjwOKa6yDxf9-UfGolodGOhwWOGIbmsVh_xKo6XMKRsuBQOcWFJe3ObLVAccCsJ9IMx_upgvdK_5Gg3JW-kfhU1F_fGEVxsl3tTlo0q-FYGG_1N0U9s7HIg3yF83_QpLvy_zWoiP4WJTdX3lqDd8hnNtug-jhMIVTEood3ydzeXF8n8ljNG4MZfiMD1c7p2nUDyzWRywaDN1Gg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TktmoLmJVdK38ftbANtPmpqBqb5HHQ3rXxKtPUqSDc-iudpe13z8aLKGjHpmgRPJHwtveZN7XV1gMi_525J7f5RiEUnpO-PZiyUNt4r2ZPyiZfkDE4SMwStc1mcT3SkGnoODvihzsH6y4Egv1cYLB7ZTYP-MQbzX0-lulyZYwmj_2wKi1v0_cOf7A7d1hjaxs7SavEHBl2-yHterMs97P2ExGjYZi8YQrySG3nWFuWR4SOH1-YxOmE6WHTe-OBqdz3B-0ACY_Mxl_91vBqln9tYUReKIa4m7YUZQy019oaqbx0D_CV6K3g1EIFeTY_oIY86vF7GblJ4dCtwm3fKawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TktmoLmJVdK38ftbANtPmpqBqb5HHQ3rXxKtPUqSDc-iudpe13z8aLKGjHpmgRPJHwtveZN7XV1gMi_525J7f5RiEUnpO-PZiyUNt4r2ZPyiZfkDE4SMwStc1mcT3SkGnoODvihzsH6y4Egv1cYLB7ZTYP-MQbzX0-lulyZYwmj_2wKi1v0_cOf7A7d1hjaxs7SavEHBl2-yHterMs97P2ExGjYZi8YQrySG3nWFuWR4SOH1-YxOmE6WHTe-OBqdz3B-0ACY_Mxl_91vBqln9tYUReKIa4m7YUZQy019oaqbx0D_CV6K3g1EIFeTY_oIY86vF7GblJ4dCtwm3fKawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU-wuXrhYcGt_sxQRqduKFqd-ALozGo_O1rf6Bi9_DiDdtOe69c2I9UKiNmrs4S_Cs6uFD1xUT8ybAMOQd0fsBabtpBrXPlBpp7Y-Wh0DcZqvSl6MedB5cnb93oAz2DUD5ZuHcDEd51_-Kh70a8AYtWTlnGsMnrJE_Gv5McEb3kfdFsFfjq-c6Y6dUBwLiEurg4H6mWzkJzQMCPKveic2eYjTHeLTagaecLRyxtkj-yDnnpfQcL7-hDEsiaJqgV7OE3IYj0Fl1R8bz_SJg5luiHrJc9URWFdLuspPZzA-po9TKE7816LH_t_Ufigrh7aA8OYm-MCvCYvoc2iT0CJ5Q.jpg" alt="photo" loading="lazy"/></div>
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
