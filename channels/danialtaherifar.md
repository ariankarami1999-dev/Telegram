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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 01:22:22</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 386 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcLHuY22rwk4r1P4vVQH4FvjVZpLB7l0s7QJxe-of_ttkjuFtnExKzR1J3JlRGDbAH99qijJx7F-3O7h374pf0mLkyGrXqux8dMUg2ptkhT9EkQ_1149CMKsjmNlQS3elxrEnjFW6hXKtsFiKNeRmCO8hAn7JDjpd-07mCsBZC3BdYyhiyPL5fcTTOzvwsFK2LSPOx7DLEiMPsRPxRs5i5nuozTE-RLfoEsMqP29dTJaE33z_rcTmOtX8fvWdZZQufUqUJhPiVfVeVx6C6rKQd0SXXGI_EhUAbaYAbhoTL4WAc_aKQxBvMO3krrJd0fqHeMSEvRFab2kiZydHKTBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 592 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlWvJZTyiKPrrfkOmi2rbdh2T7odAbWA2fQIKiPy1YiUlpCwLalbCEmGVqVpHk3YFD-ucp8-VUSRjKNLhH549rKRx2b4GMuKktMJHaro2ws4UCfpV1iDlgDvLpfQd_U6YDQEa6bnSJpvuWWlt6K3nYGkhJbxxuyHb1WjosiikNDEO_wku_om4OMshs2OSh45VzEZwQ2ldcvySV9XbdE1mL-7RrgLXTzKQcdxmG0CqJ-MX689yLGXHhHrZi0G00OCC1CetsYvjno3opOculVgNhsxyoHt04uZqmJLnsMU6JEh8eLPBnBvL8dMbMKLAVWSnYOY-kM4Ej5Xnk0f9cEIUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAap424XE_xtF2ze7A30M_JbNvaKtUFcKXMcb1GyP44kgFhyWVT7yCc3CYY0JZp0EwuzNGpsEwwJOD6psvUFox6cPiJXQurFVXEtG9lhh_oOx3eaEJwTwXLRn7yMCCM3WUvNfLmpoXz0781n5J-QdKhLZgklv2iAg_CVUVWewsRcX8X3fLUNS6GfHLkWaUzAmo290hynQOBr34F5OOJn_VKw-UGNTVj72TvgTeXAEvX9ZEqa1klSwXlIoJmhrf60U09NMTsPzEJJu7gwf2o4Suo7Qc3YwoWKB5nkFVBxZB5_7U1SRAqgAK_iNgZZ1dJ6ZNE9VJ8ZblbZD3HEL3cjwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rB8KU6IUEGjwycHi4td8zE9nzgdgy-k_0QS-uInm-S4ZgZHNGq6hXoL2oQ24QDX5yx0-ps0tJzNp9d58oDQ13ySOyeOm_6_Ir4q7AvzMEBy9Ba8eHYmuHbqs32NaqzdYt0ZvpciNjnZDuuTMncnCVQ6QR1KjwpTkYF8mrqYN0zuGSemK4nNz5HGnzPUoVahpJnrmTJYJLIslrx89ur9rzTC0w8mUjANKD2YjY1nKlgU66uMIzmguIE1O-TEIYf9DD9Wpiw7a_8fnA37_E2H9s_5g20Xxbt15fPKkwoFB0rPvYsTPDlf52BilvRJnc4loYXjvQRJAgmE0NplZv4y5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghtokFR7Ljb7RVGUVZSIGdja6jzqHdFO2KiWjIxRKbxMbXTZ_TEv-bFNcVJdyZOIeh1U2fd8rjxDbQk6Jt6jfOuRPIzQFBcHL2T7vTWPX7KIVOcsKx67EPwirO56jGRjBnX6pzQbqyfeVMUHH1qyncsjC_rBRfn4c5FthrUSwXNuubPDQPopWZiW4WP5hMn8oJczHjid7xksEmedXF2JPKm7qQnRj9yFwJu4M7zetxaEd1EP4DBHcu3eQYgktlHuBSTNCFcEojQ8mzhu_wegrYOdIGVsO89yRqDcHttaMXUkyQVECFtkXckCKZ2R-AHBA3TICtMo9bbuWAVI8L7s4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjwZL0N4IS9A7fP_qAr6VcUDxhzy-D3nyzFaYiOZ-uPJct428Y4Pw803GSjJzuN0oN1GqSuipfNRCVuSJ0cw3oyEVuaErL2mYHVWpC7F9cEbp-WjaD-WgXnjTv2TXa_WRTqUsqYqgw-v89GBpIaeRwTo6B_n5YvhbdDQ5yjWnMiNtNe5hQHY1tqhpurH3Pb4RQ4Si8OdpVtyrLgE_DXh-dPGu7dlMYyY7a6vLP41zvq6jfyaYnezlku6JTRi8ju0DZA2u_bzkwqxx9DHTLbJyq4Fu524BA2s5zH-kx9LpqgkSvW01q6408t_mQwB7ivGtpNamY-T7krBZAqYd3j_pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPmGUOfyLyOzYu_SMkpFD5SIyCpajhSE4QyRL2txpxnOImZPx9fPpAjIwddBhlPyNxK-2culb5CnPDJmuScPbznDi_6IgzabB5NWZ8oIPRIGTBjBKf6KHdOfXv_suKLcDCIdHwpWKN9GJDZApuYV3nXky0UV7gd94P6FHnQAeGAXDV78k8HLS4DEeyzwvRGR0NAe57z-BLpaK_Qxk16Q5KLp40PH-BtTe6Nx2k7MpkZVuf4Qn-nQr10d8sGZiSo_FctWQBZoUUVmwBFIv2a0wSECWhrNDaY4-3BPPM38Rkm2zJ73P_Jr82PNAFi1FOjAs-aB9yZwegylX6T478xvGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAYZBMJmZvdoT1s0-YE5-hlaKkoQYIx8mGKSsBOO7XGE0FXAMtHXCF7B3A7-S0zEqGqmNIWburtMoaSwtekuczXFayGWpuRdP7mnG9N599Z7VKvtrBMtVzIx5o72CrEvLr4_KkrLeGKn6TYhsFyJ_KEH900I6qdEi6n8DKgxGoZxXKh96_71Ca_weMygWOx0QwuAE6rSdoVBXigA8FWHxOZRLytjshtET80VvDsDZqfo1HgWbZz7vgcTiHGo8t3QsWfcs-yDfbjQVQks-Bt9-8jQgIHXnsat8ImprBCWe-aXWr6EplmC-cEffF2KGy7fQC75MoilwhTdIw0iVjtjnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9ygF6HeKL_WgtjxGuRdxCPDtCMLgRQZIhsr6vMSh_o8HLZ3jfi6Uuqw5i1lHEiATk238pj87kb46v_jVWtPTkq-Rb83_u9nErT_e3uuSEUCOfiTbMs9XC_n1428-EKIBWuEjYPoFDE8m8kCLY0LIoyBn6VOlbKFmiHLQ2laordfPGWQqvoG6Rq_bppVHrPAS6NqhVjahXUdXFW8-tQdY0Hgws8sEuW1hScUPDi5xT01r1Ux50MVukunRDBzcsbFkEV5GkZrmyO1O-HEiBkWlBAbekE_bi8EOGwhnBBaZq58_hxfVc91k3VOaaKRjUr8WTjmFIk_Ll-uOUKhlL_qNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8KDicZvVpF0af6A8s0nA6oJumn-htIJqP-gtgwVbBnU5napIdFWi2HwR0DsrbXftdqXtmZlRqpaRBDBf-wtH1UtamnKMneVdruGHlIrXTZOsFPGeWcngFmJZqJmsWVmfA8Vyu7hnMZR2vtpMbfBA81uMEtfENTZ0b6_cII1mDPytJCocIJ3I1_uTTc0Bvm4klQw9HGZT7UMOkrgI-QSFyIDrZ3j6mdudJ9lSjzwt_hheMtEaKF097zEUNBXed8nJLmq11KW7RWUvOuIdt2VYn9Az60f36BbitTQzfFAIZGES0cx8IVnCmXBiqclJHxKYmwLLZ1zlqKgUMCuMWn5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHqPPf5eeucnqbCXYK2tPBIjGNhfj4GbcWiph8DiiK5RLJ0as4irBPemfDISU5eNaniedXnfQeKeg8HeppNPg2ldtqRs6WzV5TPHfY1mp2qEhP_dRca2D3GdD45oF_PebnaL6ACO3Cgm7osqilWMJVAFb5CYgyz_FUwg56wzwB-GG15ELSsNuY6YEgLemXNQ-npW2x3xyhrLErL4GBFm9TkaLv8AG37BTvp-ptp5O0c-87AswnBt5vUS_JEzwN4lIHkBo1JX5PYg8Kblxg5WgbMXdwQKLczvV-3i9nnwU4X_EE3akdbct6ZjA6LY7fclkMgOrZNjR-VE2XtlAMezxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TddX7GVjcJiAzJ3saQXqEf0cuJbOfH4ILsgrGiO49R22s_3D42TtYFQPB_TCu9ylhFyy22aguiHw6nESzNqm6v8iRY9GFwyG-LI-pPyhq0VTDTRKgPDACvNg7e6e1NOdrgczcNjTSDlL09ooeJcixzQHYCHSNlQxQGNcSkjVeKuLmLZqA7KDFhCAoCLIQSg-hVJiPc4Ouj2lVK5JZwLCR_4LOYtnwdiALqWiOjaodW6ERhiUSQfi2wJV3KfSW2UztV70TSw6h-8UjM3xKBYpnzXky4DxbdzBjZub65K3j6GSwEs94EUFeC5wz6nCqbvTGu3JE8Qkx4q8mlRuSVhZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Txqtx8m_OfD6YusV1xv_XZcxLbvBwYTSkGYBXZge0IL_iuY-yTXqUTCB4xQCYMUbjToHEG-GsAhA6GdbNoGjzVk6KT8v4GWHjiUL5KEfXAJ_8YlFwyvMKOz4552agYznT_EwM8J_O-cfR9pXxmC2FVByiqv7hz-NiUlTlVfiQru_3sEIYDOnjn1G5NKmmIHSNsNR03W_4SwK8WoMoGQSD7saTGK7IHK4cX5w4P4Km2unpQREeuURdd1cf8TJGT0VFk-Sld4lL2KaeW0iYsyxrh4Kl06FZDdDEs1nntn3Kajn4oPNC3YEySBX8Z3kBWFDy9nm-z-H19nHj9E1Q97meg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEuMQo4OQ2JuDHbF8PJbKcMl8pP2WmKZ4YvIs9JpwzUAAPqzeHiD2Fs3a0y3nnt17xdsDrG5nzuQFKSizprZ4GtK1RU32HU3XFOkVWs2RG1wIl_vh7_O8t02HGFyRAWgQZetmUbu8Ma5uEmZdkSUMyAwzLgUUhwL_73YmCMW2MRVkIUHBbZoXGkLCNnVw9DrbVeA0cWzYF_vE0EQm7flQXoAurgip4lg-PQ6DDSt6Vx4Er4m6ZCVIeoIWciKZLHBDXjWQa1Z1VHJX1VkuJ2e9Fp3h1ls1wvAU1-ptVnhAcAfErlxqXBBQiypzP1xqNFo3ffMkxAZbzm_HGlwICeYxw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=lFouzwFrZe0VY0_Eu3Dy8tcDh8oRS12cULfWVz9-BFyABTW5IeZgC0iLxuHf0PJlqB0stj7F3DXr3RyL_E7jtjY11FrvhYMcjYq3Ec0rvNPoBBIAb1zr4d_kJqT4Kf-6JD54-XiYm80J5m_PwhV54oDJAIQlTwHJnQXkbqaydwaGEHoUFWOmkAuVa1lwiQZbJEYpKiIAxDzAVf3szB1q5SefDk9DiHRE2ayz8AQS3m1xqTGnQaSiDSF6FFD1D3V4xvoeOfLlxMJUOhPPMdB8vCfCAvOV2FWjKDpFHaEzvPvkKW2Fg-BLp19tNVdfOJ8v9MHLlYJlbm0bTnPLZPPP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=lFouzwFrZe0VY0_Eu3Dy8tcDh8oRS12cULfWVz9-BFyABTW5IeZgC0iLxuHf0PJlqB0stj7F3DXr3RyL_E7jtjY11FrvhYMcjYq3Ec0rvNPoBBIAb1zr4d_kJqT4Kf-6JD54-XiYm80J5m_PwhV54oDJAIQlTwHJnQXkbqaydwaGEHoUFWOmkAuVa1lwiQZbJEYpKiIAxDzAVf3szB1q5SefDk9DiHRE2ayz8AQS3m1xqTGnQaSiDSF6FFD1D3V4xvoeOfLlxMJUOhPPMdB8vCfCAvOV2FWjKDpFHaEzvPvkKW2Fg-BLp19tNVdfOJ8v9MHLlYJlbm0bTnPLZPPP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo2GSZD46vN2lCK3HDpL_esjCT2Zhp08zBqo7e23BqnqaLp-ZJNhKDU3TxtZTec3bXm_48xuzC-4qC6JHO6FYQJ5XwWrsUc21Mj29_F474qcGsg74rBWRZkpc4kh6zCfgJ5AHsFIqiXTULTn_T9rH9TjuyA2PHMg8LBo7d3MWRzIxp76zNztNgLygvmw-YCdBCxlkZGhU4sE24_BF2HRfWymH1kaMJSRGAkswlA3dfIn7__ma2m1wcFACwNaph8wdaaIMug58zxGM5iZp0mtbzZw5VzU4Sx2o_yWbP8GDDpWWhS4-1pLjgsAMpPHxoh4X677fi14rslePz3vUgUkzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7DJPiHOZe_3dy42gIrR4K0vGBu1R1WfUu6En7R6mtpzLKHINVhcIE9yk5CsMLr20d6X7DXBQ4_jUH_thsI_zVCw4_Yp_DezLeWje5zAwLZAAGZrcNgeW19jWitqKml9bxE2UdRJl2gi5cVCfiqEDHsAHHjVXtkB6nxWKoW5ShIYSuKFitOiarFeVbPfObB8D5IZ7XNS1tSZKhbAVhtNRzEF46TI1xgSrKF67k2D_s30NEHqIecf1fPYrtqLy51DJDinRSnA-Xndj0zVWOZ2zBJkT0eJfY2Z59gFEsN_YlNS1p_w44jnrh0WY4jtIUAy1DMRc5P0C9_DMXbL8pumIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guFs6lcp4Mn8qrfaihIgbdWUcaEDdYFdUFay2uGzTcvw4NR-zz-qD_F-hdggRG4sbt0elrnA1tP-Q5R2NxXQL0m2YmHZ6BhzQ-jJCpdH44Rk7p3-kmDBLZSh4CkthqppDNrngd-AP4YyInuyEfGMZG1WSZPgrVNO6VFSZRJMBLt4OTdqfJvd8hSwwau0Hg9UzfmaPFb4v3Z6ZIArchC8WrBmMDdYe5nBD4JhL2k1Q9V7Ty60hP0pj6Pe3HyHqY3BCd1FCgbzIHpsiJ8fizubEUbg7MD9d-xlbZXVtKjJ1QE8LVzZbJqkcZ4Uew_A0VSpbTIramiMZ-EKR3LtKoQFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxWSEfvq5_A3-TcwQqgKJu9Ehk57mjksaa7T3T_9yZcbdg5aEsQzZWqR1DDa9MbR6K9oia1_pv9B0Vl3d8mQ2OWvgtZVA8wQLiFbD7MstWvhhVix6l_nJOHtdVqncghmQeYpWiD5W0FLspCqcr0QTLauwKJ9El46L8XeEzZJhRptzSGWnXnD2TAOyuZcuK2eEIeuB3SOls7BQyKlo__C5DQrICtC8smzqGVI2cSo8kJgmRkxwcvUvK2sRb9_zlJPw_dpTMPzYUkHUYD4xhepLg79MOjAiPuaUU_loSSlAiQl6TjXhaW0J0FYQu7brAQHLgzNkWzF2qjJ3a5wmasWbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqZbtMfkBsZWiG0muazxRBfpghMyyiKKTT6KOi58iIJEsjBRrBCiN3Sc3ELzEiO9_OHnMANHrZ24Kb5ufA0Bxstnp2MsYs9U29RF96JRo_23L50-xSqLjEHnR_LnNKwu6g0juOm0c5jHdIR75XfAiQZv32L1N5UjLTXXUPJiMVdM0PN4OiqHWpQ16hcBx4A6jT-YHlFEk793FpgQsd0h2TWBBL5YE6JhmKESZlV4jI0PFtoc8EpB5NVfdu0RlucCPMcYlSmrb1_XuX156a6kj-nd2W9iuFDCG-z80gPS8AYqwjVISFeuvH3kxZ8-T9SG7A26wrCFNpEN20PZBMr2MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQP-hXV0-iFbyIB4-qQD_C56QXm8Ttp8tKEUdKBlzRoHePfeMNi_JGQXGL42ECkTHhPz5ymRvVtCFa978D9TZbUftoY57HiIKBWDhXni7qYbRPf1zVrjeSCIMKW7xTsCkmisOQKzgXSrX0LcdcFqlnMuFmecI3TQRCznJNrT0aNObSoqsSS2JtDIXS0iDRAQ0BTCc6_4FWo-tLWTJekE06Su7I_D9Xr56tWq10v2pgAUzZTr198RwN6PRxts9TIsyANjeIBdLRUiP9gV2u254JwaKrZY33SeaNGnBk4eLCnywJyAIcpg3kWc9sI2ny2frAPvVGptJnrsYsPvPMp3LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4z1NQzuLdSEzeHCo2xx-USZjQ2f4GD6_jCIf2vUuuK6YEZDv74Fjrr_YpzT6KMQM5RSLpJXT26sVHONts7jUoFA9_b4PYAwyOMt1WSHBn_eW1bqaf6gpfvLjF8nw03-j9o_NRdoHZ104lC17mSIkleajQGo8ZpPLyxFoPcfrjH4nY9qHJeIezGu6DJaBy3Or1UD82eOxPua8Qr_DozNROqU6raiU8bgTbgOX8sdTqMly0b7KCX_Q8i3EIvdHnaI3YXW7PbWCuWrJpjUCufDeAIHDbXVYQ3y7nWQWpb6EaxeFjmNexGdqCdUg4FX-Op2wt2SRebbEveKYPcWdohvBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9ulrbHrrBwxg9pCbuYR8NE33BYyIcgpcAtGDsfQLCT9ZMAA4iFRAo-4wvleMwCmrLPql1ImSF4IOwlZZE59UmyNKyEX3QalsD6VLgEPPK3VTG6bDSoPWXAlZarrziC_PpblkU16eTgzyUtU366RamP4Wm5piqvE_4FOP68icX4fH-Fz5KUUXoelDSFQ8lK8kgEiryzHaNW29bpero1XtzfATbAnpvYPsKKqoXMVA_je8ub2hZI0Qnsn0ejQVn0s-tdWEkFjalqE_D0SblLrTEFdTcq4pBmsf-hoHL1U9hYvcAsKImTvO-WteLalG2xJsf0s-3vhE16aDSPik65unQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL26a9eV6TmvJYGS3TS5qCWuDKgIxNb4UxSWx-jFn5LwgOWphCMXQA8wMacxUMNJUB2IyOqouAlwOIe3HOt9bgM33XO9B_qwWPDXWL5U2SZDLfHanicNIKpxRAj3JzXBKj2lSO09g7uVgMAfrGw-5wKd1ByiXrY259ZNggQCalv4DAkprY5Bl-BwIaDiPi3L_yN4gHtW70kEqbExdcPGEccrwHOZRxm4bHld9aU7UFqX5twIPMR-T12f1u66GPyrV19HPTfpGnHfOQogjl9QRFssVRgMUKA_EuSz2lEespzzxhU6B0Z2J2ABAkerKqSjXb1V41MZs5kbmGJniCM4KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH2J_iZ717bTdRB4XZ6rZcIz1W0xnQPVS1-5cTKVsL4p8qiDIwebjIero1liNAxw7ql2vu9luwFn-xqoBFeKmMGGAgRIAYX1q-ZwmISy7yB9f0xJ3sfYa3aqUVZpy0L18Puqc9tbXrdwnxvRmNRjHjxBhblHriRJeOpekiYX-NO12_RyH_gya-k-aswRXsB4UiV2zGlwsD_t9Wq5rVq3G6Mk5mUsxi0ShMbpbrJcS6v6PXpdC1LAB17HAbAMYVfawWfFo_k24xkF_kyd-ihK2SScqDV01sfoAY79bNO4UBV_B-3zf5yfbYECX6LpX8Vn2bP5sPT633zFDYOhfwXraw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTrshuQ44yLXr4Vje74O6T1eD2g1-OT2tXwB9neRMNv6UOO027-DkDnfrvGVfB87kTrKjNBkiwDPnjrbhK23L-Wg3EEljKL7TiD2YcHogULfl7PwN7oIN4kdO6vGEz5W-P8MzPeNyjPwZgqvdn1BE82knw4i3vvgLLnVZ14aGVlkyAIwviqxnNdkgTTD5iCnVhIMioAEbBDd6rhYdDU0oJtGwYDWURA5dgr3ZNf8_TZJzKgW6Ax8GmBziD_laB52U2l52tRwdudaIpY95_G9ljeqj_MOsqg9_kdZPNeczYXQHddb0UH_qWLiAL2ruKFXK-r9rmdNv0eMcsjVlf7tFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHYBTkiFXe8rCyLWHFXHZKjq6m_sx1NOuJF38-swGrEOdMkWBaHLueI4cPA2YV2xu-MzH5HoCrkwcKF0FleZAJv74DJnOyvfic75dTZxHmOOJ_HAXkR7TlWbWGECUCUO5PVmUV7zE82_ndcRocv3r9oWk4mN4EAyX4D92RlMJyONSykhe8TsGj-Sse4xYKVae1-XKbkwbRzlnwJPzw6RxDyQ2wGjpBT3gXDtkll9bwvoUNo-jluB3w76gCCJFr8Mi2sapVrsSPmlMT92mJhcCPA3aSbMrTLpRC5e3WV9PztuWyXGXbUx_uwT0B6YQzSybBJluJF47vaPxNjV-1HOxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppHIbEDSSOLB9OA_GQL_EKubWQOp27V-CKo0fZsaiSLiFgYrIyTZlFZzpwMyIJXbv5VaQanrE9LtboDW2iMTCqZ-lmxCaV-nyEgRwncW3R41S0wI2Q0UTD_RUpGG7fh12o3enSk_yOS0t7hzcZNvhVm3YmME3kVcepFlWBvE1l_Tp9tDXNCthKtX22mC18rWZG6NMeL4lnidgw-uSBksPHaG4NbjmCyeQHSHW5DQk70eKDEymZFE_VPn9rHocU5BoQOa1u4uC-ok8qioRX4-TXYWZuujOA0lSZguXO6m8Lu_1veyq9e0bFP3k0CLRFhKrKfEcL2qkdJEAx_Ej8Pw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ljT0qvILpfJflVWm8k3SsZy5MkdHDmjoJSvWFAUwZlJxcVfSYYKDSzOTytRi8aGrZhsaCcLQEkjpW16BOtXypOhhi5yK0InQbQGrhND-zoQjg0x5mWasBESd6rxPtu9wtS9aqbEev_CLYMcY2Ns4d6Fdp2VpaQpoUCBWC9udNy4GjMLR1dUDi6f9IClqQFcRSXBMaYGJ5cnfWKjVOAhSwNj6_VXYQXWcicCkcdGt_ZLx8yVlQJHusAsnr4VGppfhLuy4ColRap2j8mHRW8C-JC3rWmQPj4urW2Po79sbCTu4kS4pFS_E2bJKog4QfErNBq7XoBG9y75_xD4aWQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmWflJD8l-YhmWUOuQRqQZrRCe3riTTsMnsVsm3lJSnsYmPSdHe2SoUF_Un54Ka0__51iPJUi9-IiDtFPgqQSqf0mC9JKWmTwMPtvn26WWHULumBO5rPNPcX4BrysXPXsmH0wFQIhKCqdaz-1UHiuaoyjLls8A1tvDBCrv8so_4MAEfNdcYPuFbQbio8HVqk2uHz_EPEZQsU3uI674-jC5iOTS3ljWvoeiT228dNC3aS459zQB5D_sK8Y-jr6P_UJLwtpky-4JOVYhJ8acmmrSwlgxi1U55XV3nF3LMCdqAcD_sSSm4dKy1GLoqcJ53kW0KOCnJo2btWkO-A2xGakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiZixlNWSxOo8J6l9mV23M-6tNWr3rCmg0ICHcHr0wK86rv1GEJyLO1zi1q0e3VLAKm047MOijkwBuqbJEz51-w6ulBKEhI3ub-Mu4G03yPE-U5EZTBeyMCPa8rkeLnQ4Iws0HWtibmltFZTDC_uzoyMB_tSa5dO0T7ysGVI6wVWeNxhjp4CQljDqDulF3Z7sgYw44UnOqhKX8-MznhyowDFEskW0LGdjLZkDyvMsI10-hzIfQaWKfwCLOmNxf1xGbnO8eVambiRS4EolgGiJjjr0-HbtR3oPwVnWFGVDRlRq4iLy71YonUVBYlQy063T1Bob2oV3o00NpuBvFflEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXY0hL5-LNGAAzvkK6Z94YW3TTe1ezzdTSrQcmwzP5nosZm-jlFf0ytCluAD1xl2QHpbDvVugBS4tj2bQ-EMA-k6EGkArjA2pHbb8ZM0DEsz9XPiA2XwA3kjr7eSla1rwaZ9NlLR7nfBPvuwNfK80pGLRzIzPtMUHZ_HPzq3PnTfD9wxKFBh7KIYQiwH8Rm_0lxgGKQSVzl5p3jM3GhAqNnrzGW5ubqfR7fh6vDEETBc7m4PaOA0QEvmqB0Gmqcm6UqDMvcdVpHphJYnZ9LIoIjSTPPYgnO-A96yyx8caZm69qs542tV7Tv3LmWiCbk8UNTyOFsJqLxocRZjGyzcxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4VrWACGMv8KMQXvf3q1CbguWc2cEQUSicNrjfhEGHDtAWybOquESQGtpgtVIs9hjkp85p0WarIhEmsPXPz64XDqEENNBnfEj3SJGB8X3qxCSu259DzMI-4Nlq9OH5DG8XnILkj1q79__idesdMtz0dy4St_gZtO1de-ZPFwVQIx_iIdirLDMXEnmiyDZuQOntXRxcVEmTC6nnYVmojEGsp6_QvQYiIGQ6xzJNJiuCrWeh6TWhfOh9ox6DpYH1zCFbpYjtWfFfd9EpRc_RtDeSPNZ9rEU4S1UDMHEKnblukWyLQs37uZOmLHi9H7jK5SewUVTSPfcBmpHzUaeBkoUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1B1vkyU1g5NUmBjwXTAGiQ_Zpfc_8bf2y2SrdHBCiUAlPqFs4mI8OvAweOQepLpnMdzoE7ysTUEdumV7RUzcN51asA4uABh76iwtWjWDBrJdRmlOJxE_e7f_l-DI3QCX7LEchN_EsXYu-lXnSlUyVgb-WQA6q3Zz1a_Eca-Rtc9kLdhpEmzy_8AwuMN1e1tXOyuCrOVcv_gIBABtebjanJ5HIQAi0asgZJoROhwNCp8FIvZMml2C-FzevL1Bi75FcIZ6NciCrA1exoGhHQ956jE1dia3FO22NMbFXcywcDEGCmUW_zotOwe_ecMOAyqdxxwr2CUrtZW3vnaJnlskQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e45NoHX7u9Q02QXXbFojiNTj2j5dE-iZ13nXWnmkCIGz2TezyxkJ8kmnu0hxqyb3goVUTdwaGvlVTZKDOMTkCMmdyuVXeXBVdhchrOgvbBWTLxsf9umntyJp3P639uLEN5ez1es_hThFNmnifYDOcoezLzDcon_FGu0YsJ_-OJ2YOgo9VlKfX-hiCuUbYyTS-4WfsYgNNR0vlMolC_QlOCqzuxisDFZ3h1VVRXZHDW75QlSRGN_zwMWupb2mQPZk2WO87y4j1P0hx0vW2oPAV8zBqypBAhLbK7DMvVub6HvPzz8LhVH58WEMmFjsUawo3LyAY7Jmd_uFcouuvjFjJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbS_WtgGwFtEkGtrelyMSa6ZJWhuxGLggPSWoBdvDJ7ZSOCNC4gyr27FSvSUVOOhvXjQqua--Ad2U__LN5rB4z2BHcNRzwob-T5rof2HhS77pvJP1DMn7LyripAx4gfBvb5OZ3ag8fpRquN6J-LZMWwjoYOxkvd4E17898Z9KgZQeLAhTDYcffntTecXeAcCMyYHg6aFrTbdcegw44eHL_5dJvX5mh_TU6DGpSCv4JEtG2r2yxATQU5CGqXaJa_1fOkUJs0tAtQMi71y7tRCDlYhIS2BegQGACx7QXnnfFivSbfMvLGJ0nzU04i0WEDAv-vgaiPCHG-SpamTRKk4-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG0IKG3f-7FQIYZSRMP4Vg7IfxLgZd7sApCWNhiS4UejNPg6qIeP5frVWlF8mAiOGJFhYaSdXjrabC_3sGlhPLpJBMPzxCTmdNo9qYDrxPuVRbd5jlUFfVHpZN6FK994afm_TiadoAq-jnoxNSw4r-nTV1UP1kcXtqMJL9UAs1x314gRtfXbGKN6sZY1IDSbvc1w-LdzeZPurHhWVnjTrCg4WlA6OAV1RQeQm0_kmrTW41acMermVwbfb9Sqz7PvJtexqWQSxvKQqPwVa_OsdHbW_1U1FPFps-JdIWeN7LfHtqHGVSyT8O6PvcqYw9N2_K4lOQv_FXhh_XfBQWMJ1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1hCIHqE5LOlP-MJH8k7g469hh2g01ERV_Y1c9xIDENYQX-jqWZYRTsrqnBWyeKAQdpZu5EAfOW2Gu8QArEjpMYHEPvgWwfCaddiGAu3N3QSb8FF4IGXF-uyQpUM-aDHf2ihisYNh2yllFdH3TQhprIVT2I0I7lPPFujgnFukMfrJHnZ3mgzMdAFU8ZZ5NDzXDS8ubwa6wr3i-gnJLJQh9g0V44AwY8713oHmfx6xjv-73DjyPP3TfzyztwadwwA-MwT4kWIiDWYWgLpI2Q9EutEXF5Z7wjbd9VMrBVDiKLSWP92ZgWa_ShXsJtTXKFLWId6liK_pQN4jOE6UTpkUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQA3V8AlvwdG_MHP3dF4R9-k1CWrQu0gbKSlbvYoM3ySeYqVsW53vcYHbWmXAYxr4iZwLvwJy7FOLdCgtPaTJepMoouhLYbIgVkQOWD3zgFZaQztGnzA3uJtfjcueTPHDTWP6461ykmoqEZVpqOAXoXuG0QPjlARqk4hs1G60t7yqGA5Z8ugjIwVUJzRbGpg0vcrCZtPWa6ffkOCqSpnbKSrB57bDrzKZNIPe1LZW6cr0HSMUSW4kxTuILRyu7DWioFSUxZc17NeJ_jUa5kmZVg2BGmMItHVcPTB3173eki1JuEmlEdGq7N7SACb1c7SMNs_oX4WNZKAWyZ1zpc6SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8ZlIm0A4TUBwHk0YA4MWtbG_rnY5w11Rp3rtrpO4nqfmWYv23zk3eyq1XaoYrK5afCp6URrxtHjFAJPrlDM6c4kX3yt9ugXuOJkSUey60HOB5dJhAGMXMV_ZIq584m90g-FxrHHFhZtygdo6vEjGAJR8hFdAYB9eY7J6hQNRbgfkd9aOVn9oiK7AOJtsz7CPc72iC6RDB2pqucxt7v3HC7IJ1VH9mc71r81efEQqWZktRurRi9KLuM1gn99oZjRdpJuTK-2wAGnR6H-c1ZbHyt5Yf8L6PrBBkHh4liEO9DXTwb1fWY8_fyLXPrBYPnW95XYWG0dHA6DtQ7WJIH9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dptU2XYR1du2P4dMBEPhl1JF6iVyz2zuO_TMGlp2FFggMnC2no7S9cww77RwSt1TJ5Y16aoEI63HeFYSVMEJByV_xp5iE3LQGLfYD0g87wfvNAIiP5U2_R7z4brsnm6nzdWf7JCEzTYwHQK_5zxMp5uysvbQZC_ttqWqsOFiyeT00Iq16zsTNQLZ9h-TD5g7PI0ouEQyJFlYzOb5R8nppD9DxchtiLvKnZAALljmPnaHYyhwoaTBoMiR0Ihwcizc3nYLPK9ByeDa1kJsoCtni5dO86ta5Xcgf4WaPybzQw73_R8hc1_VUjPW07IIoyJflpBng_-9qn_P9dup-PzBVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfCbHbcRjUe_Z1jvps0IIpkxMuAk5op261Mf34Knc0n3eGd8cjCK0mNgoTn4f85ybeUmx6oonivWJ_ayRFmKdupKmnulOph-jKHzK_Brynbcs31Q6EmP6cvLDu4-CeVeHA5cGAfwilOofLlgPh5VKuHgxaFy-lY-9sY_T6ps6uDeZY_UvBXc7B3SgbuI5SZIp6KDz-kJ36YvtUVK3xJQ8m5eFJ1YOoO0GYgM8W6gdNcoDDo66qKsgoQWnHva7x9KnQuPOWFaP2AJQECLoNdWuzWr6Ar_jSXAd5mRZVGznmgiE3ISMAXiQ2huKg_ua5QbYIUhte6QEHuDatksGQJTzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDWwrpNlEZm4xJ6N2pk79A-mDT2KlLB0z8fNgkZtvaAxL8xs0yZS45Izzh1rXYdvmUN9UyP9N8RZmAQhzuSVDh93j6uvI5MjuTAm2GgjknIWTxnAv7JmISI3YgFW0UV6t4a7ltIiCYZ-EmDKCYteeArxmTjX2-yAXXzvCLiE1A9v8zN1eh1JiA5jojojTcRSoW-j6-akotc-BI-mO8gK_FVul5h4HVWCAdfX42JAIGQePSOsZBxJC1a6KRkYdqFcqg4nsCU47q91JpwyPvoSx9gAoG_SWsmE_wQ-08IQITBzLUF4D3ofviKiXRfao0NUeJXCubTzaWN9bQPdenGYLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRrreT89ZK2WruMiTFyJKwnPGn5tVfmHb46wbCUMfR0HiGDUo6_WR9cyla3BBjQW842_JO-YE2Xxn5TtsnuAbe9hkDJ68FBHrTWLS6nMqwp_6tRyvLV4Cc2JpbQTTLNxwr8x8oqj4EmbjPUct9sXLLbhAvCUbkelYNAipjNuqFfBxiQv7NFm2fRY848liq41bR04h8V5tChkb5FXnag1IXfhG7G4IGiytayoV4it86mDXkEYtD3oHpJ3FlzHT1ZhaucJPvi5S-Y6Uh-g2Aha_Gv6c2A-XkIY0bYNIiZDwsUAu_b8ya5Vho3cL-sY6Acpv8AAYhCEJCALzk0975ipWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_3jrSOKv6_y6jSRTKm6roj23yVkrkhYC1kGxolGLYbj19c-HCrje80df62JPHK1YDuj295RtOavOjxAnm1u4jtRvJTzSS8XuFDct1kAwWtm_pIV_FfKswBZ4qcK1b2284MwsBiViHAlLO1Ild9_3zN4Oab44nNaMKYPTY9hqbRNTIR10Nh1bTpnTl_I0odMJ3M6lEonObSWv7h5YM0yYmxesVhe6Mh1HcQolD_5K-sHZR7oc7iTmuylfie9cRhiqf-r1gg9hjBPWrQBep07ZIQyYWF9Yogp0w1HOQNSYRHqcDcPBg71f9SZBB-qMD0NLcvcr4-V4Rc7znUP4y0lsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UK_oJcfL4fCgg5Snf3D5B50kligTv82gsYS-uh5e6JQ78VXujxPK_i86B5Mz-ESqaxWz3LXIZl3NADQ41OSoFV1owOfgJLb0ur_Q6drTDJIP3LgUfyNgut7alZn3oRW4BYQs0t6w8i5VGg5iILeAp5cyOfjtxMWUQF0zNXSIcw-I9PvDzd18nBCXqe_2XMwRgpmiymFAV_xmzV8njuCz135Vqw_G_2kw50MIkeIjbgIDbNRYpCNgtXTM7sXiIWzq3xCO8VukgC-FwaPOl4V0kHsz-MADF-DhBWVKAvBzzFEYdeikNKZBLptcCBf0PAU_5C68rkXzNfXPpHWAtYEq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnRRe5eDaGsSLZl8JTTa__gAyeKLifnRvyZBtZ3cgmnxIAmONyqPytZbfJjh8xqRgCIJkhVye29NlHcr8CAjDB3yE_8NOYiHv4SK6JX_oGeNrAHouU669XpljiEXqCrtwNEp_qEt6wvvIx_Z1V2FA3fJ9IKM-fHnoa0KF0TSceb9DpzsWYlOW0Oz5VprAC9SCzTTitGyUMhAyxMVa2VJsNHfH8AUvArmj_QlvZYfxmUtzKt5HmdjAudOF6WwTNkTBRPHpgoE3ijJv4EDDmBYTy8FjSJuPfmb3GKVcakV7RC7ZfhfY6DZruan0EkJiiT6zPM4FVeW_jZ3fLPqUwIThg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6eLPlSn6BucMNZum1pm5eBX5W6iW3qVHwJGkb_pyb_W6FXycRHCZu8z2YA8IEcSXFyC3YqbcWbTPRUm16gHVK1hnG_cdVwsnuhdjVW1-yEVrlakEUgLtvj-jdC6ecXZ46HrY-FARc3YIFqTfiVoCStQfo3jEQnfdCjoFq7wBzx2pmQYaD9kPY2A7gaSczhl-biIxGqzEvlHt3B_Alsh-sLONL50ZkRe-GOrzW1kW6v6ChlefmompJ9JLK8Z_ipzV2Of-avSJ_58xEXDKt-wMBnDGKq55oAIliVZRBrV3e-2Q76M_l94nT8_2F21GHq8MeHY_WMpZSVn5khE4eCn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XB8lGO2SwgQIcsPaYfUWa1nSaxWG-TZdGfcnmtiZgniESG2I1xmF1_HNlnGyeBKhPg849Vl_4fszM_zcG0MMUc1OWCfhrHA1BH5mZPCEpKf1kta3k9R6ZhOpS2R63KkaowUzGSd6m0SVtfnur-irRvGsFZKpRMjnIWf9E_SUsYG4SHHX0PMz0LYUzNwmrZMkNYlt7g-IQvxtUVyi47fF8dMu_QjwYP2dYLlKQl1VTRRDZCHKnXc4iBA7g4iKknM9147MShUCkAIKAKYRZehB95BqiEKLoUW9mtypkC5cXtSoLQeSIsfQjhDbcmIwkzQEMuABkrzOD3vBLqgx0FQl0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCaxj52VSG9ePebb52BrAy21F5RY72VIEilvA7qf7q8nqfeW9491fgPSBWGRyvvZeeo5wE0poc19_R86X15Qt_-0oMpJLbhQ4oC1X5mB7TkHSuMLmnZ5SDHS9f0ectBQi2pFyG56mDkxT515yshS2z5oThYmHmHP7D3VjflCxA1QRvSIbVy_yACbbQa5DLiEbXdl9NAjbDtyL-ftiEr_Ob6xqLWRgdohHMB2wUbBRrPBw9N-Aa-ngfYEeBMNkNDNzptguKgH9Z4XP5cjatkwAUiNhzoZLLmRPCp-tNmYu2gjl0uPH92fIkN2kzKfGko-8QZoHQgMyQLzTiQBJzN1Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CugcA_57XDmBBNzkn8pbea2MHxlrJAZh6IZDKiLDh_2rkCGFnp5Z0lAvsTeUzVMrPI_2wzd3C--ENQz9W11l7i2_OIM3rLJROE5Y_AVN8CGAC4mr0IQYLREIpLDzNec3bpX5ksfgVWF9osL1Mtz3Cs-6uZQJ7ivTKMIiNP5FmPKDvRQjJpYpIgl-g_F6JKMdN8z3K9aNWd_3MAiLXZa5FMCWYBL3V7e8lZf7z4cVdAFXi6Q5wod_-60iOYDTi4ebuMlSeMzqWWBdCudvtDH0CMcdEFhmZ2cCyheABgaSuzH85rElpTE8BhasC1tMetL5aBVYIiiHrfohhSTTyMl02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeKHNRUgan4fK1JOUutlmuxBa3xdZACzo_z9J0E8BTDxZpF3WSVEFQEgBN2Pz1LNz9VeV9mtfO1sHiSriPbahDaunz4RzdJ8aittrtScb6lQmAXalx2cX5VB_ezg4jck6vCEooZceSf5fo280xjxkgC0H9gPSQna5-rbPukp6dBjZ_SyffNkz_5fcvgoHxJUUAZIhkgzhicPXAWZDQMbDpIh4WXOly81HGZTrYCjNVluf7wM45uMbRPsLKasaiZnYdQOIqqZKfl5X_FlDy2e1iJcCsm8Rhjv6IBd-qBtG2NmDNpteNjn8tGxFWrzpCoV7X-B1-lCPbTlgtSBw3xnSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-R-wKZO9ylU9sBbHJRPLR3XAGFJgPqKNmpsTNTa_3DdS2zQR4BDCdV_gfwjqejzCnw49GS1WgdyRSJ1PypP8N_C5xPVzAk9Eyy6P8LllmHsGXW7AIu56DA7R_chyQuSBzfy7es3N7za25GV86ZDFHm9DdDJpNt5jF6hg0WSfdnbvO7a9BeG_zQkT1ihGRPF10eRBosJMxVGtB_yNOt1_Nt6tiO-BfsdFA6V1hjKzA0-AcW5rL9R4XFnRPck8_Hws4UoqMo48NNEbhVdFaAuJvaqRTt4-KwFIGDqolUfgl9UQARrAqjNogXzMLLtkqvacqVLusLQWAFlOJslkpOveQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGpZNnr4GHioxbLO-9tSVT__Wt92L93CE-f3X6dNybHOvOiVTDiNiwnmO8fUds8-vj3VrwSTwcI5itfkkFvkW3loz6Dd-YBr0X-g____x7TyZhM6kuBzdNW_HwDVrdnRBloqHIoFYn10Yv-GUA9vRf86UrPKL_PeitEHMOH10-fMrm-EIN5OV6dDc_v03p9H1aWdkflis3bEJFHp3XqNBfabqyD-nUSFTjgweFc_3J4ILpYSEsmS8CHKcdMoiLIxl1A76Gpt0b1wPnXra6GQDeP9MrIMsvZJT_zMFz9RsOfji7Ybe_uNAFtryBpdfTq4R-WcUwXqmwAjOilbnDW7PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwQx7QQE8wCq3Kqgo8FcLuyfWQ2PVpyYXEtlLmVDP7QLdJ_0j8T1BTvErrq3nFblkJC-1r_M6XVo8XJqlqTvGKmzLKmUyextGvrU0Gx69r-dSOIqIyCSILThy2kmOsPrrFnN-9PVWuD7ekExZiNRPmVKU8EjqxvtgM3FWm01qgjjVPtpZnOnnDXeToELh5zFd_KQreeEaimmf4Q5tKekxnyUat0YyQiJvWW8V9Zqdnmg3P9akrKDgJVMm7L2N43lqjJT7P54G7jytW_yo7OtfHomZeRSIYt3AyxVtuANQVi2BjqRnd852iPlhtglrTDxDD4MUlghMjcPd5N-KUAjXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx_qomBhhbuAsLo2PrlmKPzypV3cg6MIGNYC3SMXIP9S7e0t8ZoyrMXngMxCFc-EgHCVNg4aBkzdxAEt-yYoouFOiWXf1N0esCsBit8FumWvloc5Nu4AuJty0V7j4X7u-YFEHEKJC_NaZfjjMY8MADgk0LBoJsLBmSN6pgWrC11cuoAhV1OMqNkTmvB_wUvkRxTnNpYMZXIUm7gmSbr3ue-EASBXT6mTRhWhN4BRQ0eguuugajkMGCzqJacUA9tap8QgzNML5GTE5_kxMI9O5lYKt9WyP9DOehnMOPnbagFWdazngwWKJ2aj0k8CY1Vti-__VGyAo2Sq0rDBXIw7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGMHtam1HjYzqxEkch9UwmmsI-fpO1UWUlyvNQoogEQn24D9kOFYgJG_5VgnmfzrGhgkqRTxQ2_JRdJzqOF_ZM2pwBT3y-tGgfajOAuBMmMLliAWOU1G5h8eQwTbDTe8jSTxxmsFruAXFwkAUMgADOx84WFGRddS3-tw6CAC4koWnH7FyBQvceSKoKxZualg57TGyDptCw6IiOrT5x3n5URuu-J5FJie8t29SZwqolEKKVbCMr4XothwDhHND1HJ8E1onpx3ceyXUG5bW5AbPLNs0urGVYLekSQE6RoayAqoV_GzQjFpv0vh56LJEo72uKmmHVJFSPkQAWXWdmlAkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCNksmEHV2LIKSKa6PLNwrFGgRLjGwu7FfOUNhKr4THEBYT0XDLrdNE3l6UGdMBW7FKsiDqjrQwIaALUknC7_Z-Yr548esx0v1yHEDulASkhOXYibzgGVZa2Ynyt8TWGX6sWUWb_PQfxFWYW3XpZhqPkH6PEFYT8kcoktq2RspGRsjD4QaVfWAgOVzairE_k-HiqABCLHVzXAWVlRczmtVn2uycw8D9agrRnEJYGtcrRrPhsPA2N2omROfOkZzjRoe1O6ApwUO-3jECqlWec_UsTldUNISpgNBLZraDU3ZutZW_OjfKlb1D_R8ScVlXoIqLnya5zOKYGg1D1FHWSPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3_jgP24tSEcbKDs6k8qZzjyEgbGCulz1UEWDzeU3WCP1uKDX8sRUTZjsgbo-vxI_ETNuCWkRuMYsWXhMVug8sQwwSI4kj_Wv24knGz_S1kMzZ1iblqHQ7L6wUbCoBgURYjx4Zvvc4ikI_i2FDZsQbhVijyIjttlXHrvU-BFy8489SIN2ZGzL8Vb0t6tjks6OPWUp_UCd-wUS-ax1booviKAbknF6Bb7cjDdc3PnZz3c6WFrKxfvWbkEiu87bMbAYRH08u9GZhi7RTohn2yxkS1JkAsQ62STZcllwXcjPcjO-vvm_2EDWNK_eFyJJFPtHiDpGaJjLILBMy8Bf2ZPsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF9ZctDUR-xwoOrhrICm5dA0Ov6ir_sZW0WCYoeI7xG8R178SxbBMXS4c9kowg5w5cw3EcjyYk9koxPSOC-hIXHFJ962LCDBq48-2laetFr5FlEmXAzQwN9RQ2Vw415nKS6fqbTVNQlY_VkfdJBp_GLAE0vRkeFjT9sCwil7Q_JX4t2eYvttdwlBxbo0R2W5HFBzu8k7JFBMS4mT18KdzZF_Ks3sov8gJtvw0hnHkuVmUMFW-1PvbbPAAic-nrWBhJ1Erc_Mx91DtkqZ1G9Pw_3H40tLUQLxtzb62u8cFVWu9hQPo1HK3FG5w8xDG1hmTCkSi7AY3mFJ5N7833M62w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2Pf7hwcpWadlm3Rr9SpSV_TYOe4gsdqs37YMYAnqNu8l19qA37puO0wgF7C8EjUdhKTVPoSnXQGpkuOd0gOvx6DVtMRSyRrvjDCdgY1oy0TtQDMyvi25TaCCWauNlR6COgWjPjmhKJujGzWaMWq-S5NPlWE0KRi8VZwt-fTT_cjnGe6zsap_uuJANcpw-9F5jFM614Ai2kH_XbadAfNT5u-nxhCjVcreM2CRrZfthsuLrHCztu2sSZU5WdFcQuOavCK0KcCiEqwll8q-A9FjpBf8CYLOspD8s-IbeQYtdff7WH-P-kAnfZbgzkDxYYecvUTisByUz7ovptz-ERKNw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=K93o6lMrpQGRw1FCkP9KwKzj-9zWGLwfOhoWm40JKr__66mPDqNP0r1JP1sjpvVCTBppI3sFj7JaDHzBH6ys4ZegysyKCBQ0BGZ7vYXoHhf9kWVlxPryhcYNFPlS-jBCoG7MJU1EQ5daQub-4XfjluZ4ivxC_eBHsQVwOM7cOcAjRDk-WofWeBCQ8k58dNmL8V8DNTtUgP4ba1lkKibOMmBEStWLkbS0zcmzEjdfzF5H-IrHC6QrDuECpNsLV43DzBHo-r4okw7T4WDO9peTERdwwkAspO_BU2Sjpc4Xf5wydUAnlL7eYVeJYDYgoqgTNjWxlMoL9IVnf3diicEJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=K93o6lMrpQGRw1FCkP9KwKzj-9zWGLwfOhoWm40JKr__66mPDqNP0r1JP1sjpvVCTBppI3sFj7JaDHzBH6ys4ZegysyKCBQ0BGZ7vYXoHhf9kWVlxPryhcYNFPlS-jBCoG7MJU1EQ5daQub-4XfjluZ4ivxC_eBHsQVwOM7cOcAjRDk-WofWeBCQ8k58dNmL8V8DNTtUgP4ba1lkKibOMmBEStWLkbS0zcmzEjdfzF5H-IrHC6QrDuECpNsLV43DzBHo-r4okw7T4WDO9peTERdwwkAspO_BU2Sjpc4Xf5wydUAnlL7eYVeJYDYgoqgTNjWxlMoL9IVnf3diicEJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJqvAlSPljq_KZ7wKBsnoZp1t3gkeBrxB9bfu62Or4Ll9dFwPosGw0Z7TPX06V5f7ISeRjeOx4LDF13nAozog4e9hcZPQzoBYvYLUloXZ-0yYCsnvUvDcPFeqcvz7CEwkLLXXPRao6YjhhMW6UygEZUSfn7uPpe2dmsmgO9MVwN-KWW96RkvvJYmpoPTAc6wZcHD3RdN4hxTB_Y2A1MjOEKhjWr05E5J-9G0LAVfAIA-k05KnQNU_7dF7gdIIbRGkjsvxCWrIAB-9USmSK9MQjleyiXqepUv1yH0ZFv_vPDsKjcCpE-AViyejOsn7xfO72qTwk5mP2ZrPyoy020ngA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPK_7hi3cFby1WLi8-_4Hn9mhI40SdYIqQND1KM7epHqvv2-SLeLDXSWhtMYCsrmk4vCZVJw72fCeM6DF_R0qAsQty-XGgA0g3M_ccyxxv20eegglaLrh4p2WSZeeeNRHrstdpee2brUN3OmuKLIXiGyOemNY15UntjK9uB0DhDiegPh1IVJxXlgkDXfJBYyQh1AhD5Cmo-Bx1m2rSt8IpYwCOlHce80JA-o9FGx8gPb2CCII_Ik7WrOT_11R7ML1GYbH3Xw8iKX_jlsgQfgLF9cbyBclEztQb6obqbNgKPbkGjIP5qygMzjuaQlHki4HHTiIiOeBWKVGBkZPjdEuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxP5xKc3Qhg-LFZ8Xo6F_KtMSJnSQ3X5ZZPZ2S76r-0knf_r1nZgXbOcWXob8yM7ET9aLBE3xL6S1Rnfu6Cy_364aoskpAGcNp9baLF_0Cd4DvrfmrnppJ60PsehsZAmPw8bU1bTw8qsWBzLp_p1qlmj1ZNJKmLsqj3ray2CIVOGiLIdcDEOepe7nw8Gi0c2eYPqOZHOM8gb02tI9Lq0m24Aq-BfmkVhgV5po3emWQaFOljM32uwiif_ZqjSUPbkPboCG4D3C67WTaIGppZhUYZRy5nefkhpyqkcBdN8W1fmM9KWws0s3GjCUAPhG-J8MyFZ89QB2V21MgmGRG32sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqphC7hJxF56I5FFotTj3kjPv8EQZxWRRCx74thixDjkpVHjkkOuWsvybqWuk5tAJamkKQWd0j0tvbShumZmaBb4obG3gUWkbd00onmcVSPcbRQhkTWPeqsd9nm-W3wour9tw_xmVE79G2G-jCD3TMWFIXBVh-G7XcGNvnhEBuTu49Yc5WCXccioC-niUNzfXLlTJq9Eo_iI6uVtcNg7SKWwujfMa1xrPM4NGCcOink76xKagsc6EBB2rEpc3E2PFongwhfVtz1YebwfLsocLFUlQeK3v6Q9NDzS_-eutv3x_RjiGOIuA9tVxEFcQ-VOtni8kAnMs6l-6eJ1Gvfqgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-aHfJLLuD14Wjuqrx5_tM2R77CZLSPIB9t_YyjWN5eVxT0hTQabvzcvKSAa6p6Zqn9ihmBZjNJNxlu8s5OgPQW0ONnOtiobr9oKf_lqnWMDWWkIvM55YBEX_h-4KYCCLpIp6bvG2ut4_WkXQ5ZszDN5Nyel3dgJl86NIt_T7QfMJRdM_JJjkZiPPEDqNKdbwFDyz-VZoUYcfn1TO8iGf4UVJUKZPokdD_Woi2253cjYxyPwJ81UYZAqKaUqwWJsYHHQ1mMCX1TgKrNSCOJyXtFNgWmiXyrRHjCaw5O2GKw51VEYqiXMQ81ALQ30FoPbBh0nMbRTt6nIcEpLxp_8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhppTeIqWC6fFdbmAyhuSMYhA2Ws10W_UdvkRlP-jz1JJwz9peFzZytgHEXFJ0kU8AF6revyRGs0tmrCfU3LassCTJkFPjJN2kCabupIcbD0T18T2NZ5hxU-y1YDWjjmKTeuzKwJVjXkgQpwWMlh49kwDAP1Hah6kLHLmTFnTvE0uDWYWUNq3wCj40bvEqOHJqPOWzBiadl07fFLWU5RV-f05t7vPT61yxw40jhUVG-o6jPT_7oHnU8Yx5N_Vsqv9LQjfxMxEIFI8N1sz0Bc2EM1B7RWz8qjN-C1PhXQGer4gccE2z82lDndHqRrymHIFBYimrB9sgQkUMAKS1b5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lapAC0RwJvz6ujRWCpc9lvQ8kDDNSJatY8WqzQxICbllWimyZN7DO0VZ4kwESoar1SNR6RZO7Q5CDHkMU8Zapw1zIVg9P5y2ror2fAFkgpeTKk-n7pUzMHH7Hf1569DTeKx8kdjAGJ3qOlCpNmLxOojrdQjI7LjRaMmKNjAJPjng6Z5qbyRh1SAz07EtS0K82rXXFzSmwPdAhABmCuqcWJs9IchDAhgJavzpQ2wrQayDo2-xsnh89giUXaasibbP5qhXlLnQppW6EDAE5A_OwWyz51uIdHKkCvzRhZs318hD1z99Laf56F8hvMjmzlcVegaar5rWBJ7gwKcckiFhZw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=e9xqvisybW7KaFCxeeCzYKVOGn6wBLfh9xkKigIW-5N1eBUlQ5pOwbgi_wZ8Hg5DGSeB_Ja-GSHK7Hfl9Sfi1Dbgji4q09NBxCoPuxxxXrW0If0DEG7lZ4oNDWDerA3J2xPAW-MYdb2W11nkmlJdORgEgDCtpEAOjMxrUXaoNTtSJvS4E-KjYXP8iMktBUDJjw3R7p4z7IYRlHpsaD1xA0zA_5vBuszE2_aNaueEtwxF_ADwId7Yx7mJWy1kFSNZLdS9XE4CI3ZnTyaKKPZoX7TCGLacV8MoFw5abJbvqkoRTvzj8RXkz7Lce2vX0SadSkFUp4106kqM8SKOC-gkSVrrsxWi7ieegj3GZFzoQcBfJaIwICkKmDMTng3wuuBORgt1YHWB76Z9PWqbhV_9asR-jiBEOIZGCHETNIY9Gjrrix9-G4O3JnzPO4vwIB486RDIzWqe23r0YZ7Kf79mTwEebqVhh4tmMn2rejwWp92N_XPN4mFRfCD_2JJ61Rz-bsD4hCsZ7N6jnmj-s5QY3ODKU8wQR6Tg9gzjn_M89foU3ycr3YNfkwRc7wBmhLWVBUelatAIo28N-W3EzpQeNTBZqOEvZDb95oJzxy9hL3ZxuUPpSjbdgnhs47dA2FH6ogQG5igow738xZ1itx5emf167aqM0jROpOwAhwKJC24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=e9xqvisybW7KaFCxeeCzYKVOGn6wBLfh9xkKigIW-5N1eBUlQ5pOwbgi_wZ8Hg5DGSeB_Ja-GSHK7Hfl9Sfi1Dbgji4q09NBxCoPuxxxXrW0If0DEG7lZ4oNDWDerA3J2xPAW-MYdb2W11nkmlJdORgEgDCtpEAOjMxrUXaoNTtSJvS4E-KjYXP8iMktBUDJjw3R7p4z7IYRlHpsaD1xA0zA_5vBuszE2_aNaueEtwxF_ADwId7Yx7mJWy1kFSNZLdS9XE4CI3ZnTyaKKPZoX7TCGLacV8MoFw5abJbvqkoRTvzj8RXkz7Lce2vX0SadSkFUp4106kqM8SKOC-gkSVrrsxWi7ieegj3GZFzoQcBfJaIwICkKmDMTng3wuuBORgt1YHWB76Z9PWqbhV_9asR-jiBEOIZGCHETNIY9Gjrrix9-G4O3JnzPO4vwIB486RDIzWqe23r0YZ7Kf79mTwEebqVhh4tmMn2rejwWp92N_XPN4mFRfCD_2JJ61Rz-bsD4hCsZ7N6jnmj-s5QY3ODKU8wQR6Tg9gzjn_M89foU3ycr3YNfkwRc7wBmhLWVBUelatAIo28N-W3EzpQeNTBZqOEvZDb95oJzxy9hL3ZxuUPpSjbdgnhs47dA2FH6ogQG5igow738xZ1itx5emf167aqM0jROpOwAhwKJC24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VRpV_TOSjp2Gl5FJ8zgG8jL1whFxnjnt5IgkSBWtpeKeBAUj7Jpz7zE9cJQBGTIMXWZMTyuuZlm8TZDB3GDxwmNwEfR62PrWlr7pXr9XDOFB_7D2uBobWEw6M5Vig661RGtyw9rf_oWuNBvmxY2hLhqCPK4jqlcG-V6a4UVhL4jME2z9uHw7xWGJ0oeeQlAirJRjyDPBCkIOM0bZwI6ic30WUY2zUI0g8_ApKouUgIytvu5f8a0P62xXQGs4aFgK2A4QpoHA1TVL6TfWqp_M_69dfChWGZupSHSIl12yDHyZC6X5rstuAEeRWo6GxKmnCMoS5jhf1094kA7_mKSApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJ6s_A0YKQrv_ZEUHb1-3EC39w8j24eOe-szDU-UquzulcfgcOifChnXJt5L4lZPU7rAWcYRXuHRO-5xvS9ku1RjPPLqzPJ75qA2KsNIjKbSMnncrslHP7c8TQMXDIQ5tMbcWG8Nhq8wxIizsiwhDpfkG0r3V7llF4G4SnAFKeihnFMzkMjv1KUlxT_8ApkcgtedD4-s11RD5wtKzJv1x3oduCqSBqVNzFCewtsgF1FqcDNZ-g2DiiNQiq8HMkhCEOIsceG9AL_iUnAdFfJU09Lmf-UrLa7g-PadaWFkxCIdl4haaoUfpyi8CLNKIZ8XRMNveurev6qNp9NOeOqbaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OC-85T8z2Mte_7I3GoNEo7YuDqdV4F-C7kSrXo8muiKn5z4A0ijD6Uq2AGc4Bkq7dkJKRDqfN1hnl6xdTQ1J4ovtIUWCvkUHV_WKk9Aeuc_AuMQnEQr2dmgE-YBmpspk6XQOjr57VeyZUf501wERviHP3BvXP02EtRXIxY8sWr7iTkH8pFi8v0XOLvjJADpcEUOgSzPcNZuZoSAR5OshRRijuertQgRPquMBU3skPgX2DKIURuMGk4jU1ZkIqisYwZ5Lm9Elsf69ev8LjRsGqtgCAmBsPi48wEkbM3v3BknWaRjJOUT3cF2iajFZPez2s7mFvJfZhQCeF-c5rlk8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpGz4Xl7dBSbvZDOYy-Tz9M8Xcj8iM1NGJJ9kfYeM-7x9kA33EQbIi580DfkyKQdeshzBKQLzfnhtFSOT-av-SZy94Km-jnY0SsalkoH__XxElwWr6WEGcC4c7IF7Z4ckVsxDX78RGj3hv892uAYboMvVTWl6WCJ8sPdO2qz9vVX4SSOVdoisNQr3ubPIz6RfBHPA-G9upi3K2h0nVADsEixd2eghRL6IJnE9D_Zvq8S4HUneoyRjrecS7zMM4k1GXuD-2JJTZIAMv1it07pKpxIy0h51FIiAuSnM5Wfc9hN9wE28dELb5kCfxswj9hVT8XKfUCPDV0Ww0NAOklZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmBwCYIMt-jBTrS4tKUp4rjlUA_oUEF3fvNgqI17iQDqLLo5TphiFtTstrSInoKXe6Uw8KmOV-v_MQHte1wWQ-FaxPbVaJsJO_Khxy8R6AbAcp6BBpoBKwprxBsuudlkMg7kIIaEV-K3zvvU7I68AIZMgbUcoAYJxnmWBlGIFnFTEdrroGxmdLdTwOkpoA_OhdlueICxl2W3i0gsPGulaRWH_APOsz8vgtb9YA3n3BmDoEggZP48-60nM7boakKx_Gz8Fr6evJRJ1cd5mVdhIacJGsge-Zx2Ielhkp6PXLy6zYbU2UYj8c1yYVfx9DqEkGQQHSvoGvisUu9KV5KeFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUZNlNVITI5fLxs8rBYIccuWfx8-S2IKPfUzsqlVVAtPK3_9XItMVb31pZi8FRE7-WnIQDTgb1dH5ujvJH8bI_GOQX2DOHcDZne_9lPs1tsKjwqQFVXnEZXLBDlgK78CHW9meiNaSr6wkb-_h6pH9OMZP98kuGNgXYGb-OPrf3YwSUWtMNsbBgYI109c6wOuCS3NebAsLUN-foX-Xp_pFT06Lzjw2zKV74DCLicxpCXGVC0n0LVWqLwliI2a_tLIy36xNP5RkGJs33BRH7Mbm5Fjfm27pmtEEt4yuBRwomJd07J7SixBY1MpGPzEBd7svg8wsXigi74IK6Y5Wd-jGtDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUZNlNVITI5fLxs8rBYIccuWfx8-S2IKPfUzsqlVVAtPK3_9XItMVb31pZi8FRE7-WnIQDTgb1dH5ujvJH8bI_GOQX2DOHcDZne_9lPs1tsKjwqQFVXnEZXLBDlgK78CHW9meiNaSr6wkb-_h6pH9OMZP98kuGNgXYGb-OPrf3YwSUWtMNsbBgYI109c6wOuCS3NebAsLUN-foX-Xp_pFT06Lzjw2zKV74DCLicxpCXGVC0n0LVWqLwliI2a_tLIy36xNP5RkGJs33BRH7Mbm5Fjfm27pmtEEt4yuBRwomJd07J7SixBY1MpGPzEBd7svg8wsXigi74IK6Y5Wd-jGtDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHf4IrXs4pTvAwT-DEV7Rc2NZp4aRv4JAdRsshRcmcNwQK5VA3MOFiJRUYVACoOiCHeiiVX-Nnx2PriWNdFLq87GzrX2Ftcj4eZZSbFMLZd_h0B-PNFDNQmhkM6DJZyWWZtXCrb10N4O1O0jKLgbUJfb0J01r8yGh3b5_bizhGHHcIRovXs3Ze2evH80f0WGp318ol_afDNQVTrzOivJH5_w8FenjQapT996V9GX1gLB1WH6CpXP7Z5BQ58u7SY3GshDENKFoCmTuGGB-O_iBVcvWuO3s_mQe2vhuHNsnh7Qepk71TLaSnZS7V60Fo2AKytYvahkV40NQE6U7unoag.jpg" alt="photo" loading="lazy"/></div>
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
