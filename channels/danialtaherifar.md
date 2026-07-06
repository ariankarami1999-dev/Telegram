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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhSlJhE0fMJaQZeo6otQEvBIBwD_qIiU6MvbQGsRq9kHHqzI4gjzhfME7R6uM9o0igk9a3Ab8_XHtgDUzEAFi1uErjW41SC8ALmEO52Z8ok2ngMaZB-LLG_yiPCNggb4lO_MxFZKWTY2PzY9OOlA2QDudY1OY1-g1nftOyvaKVvevsaDrfXepiKY_huDvVTPBx1T9isJt7n77lnor2spXhm6zf6f5ghu5BQUfHe_UaPCv2r2M4XQ_XWEgeFzrdd2QyyuKaM1tlN1S_LDYrOlsV_GCgAX9FeV4CD3RVry5JvPqVUWE6lHnrlXpP5caasxbfpNnwjuSUwcAzAvjIlKIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YV_nYa98uaWT0AWAeN0Y_9gk5wALDIQagUyzdhJkZaUK3S_AQchwEuwyDYbSLNOccBJSO6zPiaFHkAakDLV4H6C_UZ3jr-IP0FbWgOhp62CfHcplMGrrjYn0HM_LCa9WYIKFr6pZwzvvex6NzAYU34YZ8mIeVXJGjbFRMUJ26jvO6v8sswl8YGUkt-OPWWp9Sckglh5rcgVtbOjCv7i8gA0ZTYCaR8soz5mZNr9FY2Iwzi-_-JFLo-60cAbl_wUGTPLg-RXzkkJAISoCtzgxAPsuwOV-UN6SIH8PeiP8ALTvw0RDYS1AXKYE6QKws3K2kcMwk0d_veOu1X6uJlOZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYbGzt1yRCBfxVCXFIYal_0Xu2qmVRxHrWxipExMLq0jJSphct_VYstiJ-PaVSbu9UxzUwdlYuvm4-aCZ1sLYL3xXbs5CnrZKk0b7CBON_lLpWwO3Qg7INXe_0gYwcWL40Svjj35D0K3Htx36wnlUrl-wZGuHaQgub-_MZzo9UUhL4skBQ6GCZErZcOX1HVFUOojTcnOjgk4KsaJnRhnOWCl8DeAOwI_FQeG-R34GrPzomTbRtXOhNhMu32ZpCPNRaHlAPWoScCj6fHGfgneQm7KsoiiwYtjIy7zptWDGXB6-Ru1B9vlUH0jFpTOdv_LEAMKPIBVou21PQjxKZqKLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7RpeHZuAjsWIVn7S6EBfUYs64ImXb_vv6BhIIC9S89HxglVyxpLtJevsnYPBnR9zuhRy1CmiPBfOXi-iKvEip2er5XKzAKvKi6iwiawgbuN0AQu7M1r0ckuzVfL82NX7_KSl-CgEHz3dOd-0bK3P5iRhqI9LN8EPtpskUlDwoIir4WCPjOqEzwji1giSjnw7-NZeUribbuWxJEG7LSIraQTt8mgpBfQKC6C1ykH1XIQFY2xG28zz42CjsbuSmUFmKttdrV4YN-3UL_m3xZbt4b5X-dY1RgjJhd4GPUCzarqxkzZB7m7dMrQBrL9Xbp3ElYi46e9XZX8SCcxClmQlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv68d7SV1mjJbHWlqQd3iJwenc1y8Cy3tede8d8c8gjJo3GYxh2S68gJb_XzuYRtq2dUlBhc-qdFmMiHOBzDQt9rdEKfynteR_gaEkd6_lMNg8zIdFN3adGxdY9yJVvnoJLBv5vMpNbGBHlAsl4DL1ezpBWFivXelafXEi7_X_3MCuX6WzMa3Z0s_8jTIRIL0UfCzzg_psIkxYZUbmxSRR8C8nMc1etAQD1OoTUMrnKrG_0p9zgphDesuEs9NNO_OnKvV9t1HO2Ub4Dp8Cj1A8PSJg0TOLDv2i5-Szws82YVgN0rd87BD97D345fiEoY8i4ptFx_xYpx3eUVaeF1yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHVX5q4SP-wN9ic5OGbyjDl_U7NKsLESbGvYna8QOzlFssT41SvWbAl31MjeKQAthKyiACTj26Eig3wdhT3exMrtAFSS5Pmh9QETTsLvGSAXHIhqJdCNM2GGno3KCM8xCkypFTBgQvi4aaeoIRmmwcOnT3HFvO3K58bR92xNKNtK1ur1HEldoZt6P-L_zzvvo66GYP6FDcudEVURmaRnJ_DIE_9igXRinlJ1Y4EwLECTvorar3Bdb5SI76bWz09UvdEHagY4Xre4iXumiI4yzAR14P6hzX9aE9465_aVOOeJwqKfG6W1BPXQx_pp84MhrmjhxcGfNAtm2CV5lB8sSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGbFmeFXYs0DBs5uvm5d1dY3aLgvgOoiAzg0Es9qPxesV6ogsCXqC_2A24xiAcaquuuAZQavZ7awPYGPFwMg7UnldkCSXD2-F2fF4oXFCalsqqhK2UM8Ro-k6FW_3HfY3cOt0nhXVeHgPDFD3LQopgoIvmFhrmUmqkQ9z0eda4VA2iSvUi5V_JhGf-iCxQC6BYocKJIq6RJ71qp2BHXnR4g-DJw3mNDB-HkN6YBeq-sayElKBs1qEYg-54voF-QJksXDPfliFVDfEZBpCsmv1oYex5Z7ry1MHslkiUjAj1Grp3TbqUxN_C0nyQifIvHqqiKpUyVPITXJD5BNBctzqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muI6143syL1DHXsX_AmbFIVQlOQgAD-_mXXdjCy8Yh7Oq4-aTnPFqX7JUtwfJE4Cs_wWhurzvYu_NrTeNMy0ViJdlgd9F8uHAcc_9uU6XyqzxAQEc7BT2O3ys7Q4YwAGt0IBHc0FQwu2JSjdnoPzDuSDBIfEp186NY0HgGrhMK5tpg2O3GFqwL49IwLl4exukMPvz_udqRxSXiIGc_PNq4xzBG1ctWwjHL86p_GwnpU7RDgVGN7bMFGi4fU7xZG4i-RxV4262JqP_gFba1yClDF35NRbyTFsQ_QxWV9tB1RqZVjcrrHyoWIc99czaY_Ilv17Uq3c1Cjz-KqFOAEUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwIbRCKpSYrEe5j-ccgJl-cc7Wq28ASNXkXM3jeOM3RbALKzrXyon4frXb18EL1EHeoXqipC4xiIHRJsn08EwLozulT_XDi8Meu1M8SBA1B2G6T39hSmA2sfYG45zBcMsz-JyfX6eT9zM39Rrl5-EnJqi3Yx2G2QmvHvEdh03HotnMgLXgboYSiV4huvMlAPINqKYYZ-RLhcq4DGa1_wXQl6NspXucZEeafe2EZmqGKOYmc8LUCgA6VDKGrfttJiLj5iNKEAmJzIi-CLPcmhfKQNVlslDeplbL4XQDfva3BIltjTi2m0f_5H8KBTW0niPAHy29pvzF-Kcw-zUdkXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYtzaPqRJyrUELa9_qPslCFQCzcR7LrjAHnxaMMmODvsmgGrwVwqRH4QIf6-XXGMgNccew2_KEcZAtC0DLDnRmh4CLdlhFN0mDrR1mAcargecKPLya9VPylwpDFFUeRKIVhSW64MCrDezVgU-gImWIn6d7kqN1Nex0AFR1X4eN39QraTMN5H2odJxp4LCBXMmgZnEhT1sFoFYcjMnuRqYBhQQi4KpdymBIv5vkfHAPdePTybOE7sXB0n4qk9s_2SjCg5UueMccJDjH-CcZCD_4zbHKSUS5QXhJUgj7yTT3pYLtueOlz8_QSgXVKSHkQSrsddGZs-vrPrJw0mxzdk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhIRZrgcEmLo3Kp0zWJ9lZdhkfc8yBW_mAYtbi0gBT73hkl6XGDFQKDmmKd3i1ndoHhw3jXVOFUa7yGTbdwRhCDBEopYKNA9N6Rh06etulj0TTIQ7a-pBJMOIrd2LA8FNWrRw9WYAgO1HN_xaB0ZJZI2DhVMHh_4U1pFGbqklfhvZ1EZvK6xi8t59vkK0yWJi5TI0deMHRrNsHqf4pEA-b7gE43WXiMPNk5EMH6MkO1jUT7Fa3mVnMg0OWa6S2la3JXpHxXAyxyr3xUQ8iAhI8yCtCRLd7CwrJ3ubfxgTRjnHmkTQyCd7Adj8jrZrUSW3A62_LKZn9qydvL7TZe9vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqQO9_C4bBcqneUVq0qIkVW-kspClo8qc_z4gQKWNlPrVhX_85dxyJlyAE7KR3JS_HSfGv26tQAeksB00PyrBop6Geu1SOuTlVVcXdzjfBRC5frUIPQm-wSnHJB7RSxVglb8q9dsvu4Bdg7uo2DrfEd98W_LkJ76eL4BslnrZLoxnBVRN5azM5LATfV7BmYlB7axHD6H-5XtBkFFD6wkT5mp2nWM1oH-yX2rgyjQi-lVXtF2jQNXHQknAqCKIeghFHqPADsUxBYftbyASMgJUDO0QzSjDfr3ZQ-2XiQ0vx_JiQWSZp9Ik71ZgeYJOKA7Ku4W28hqzkf4lNAOpzlF3A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=gIFHEpJyiFu8IJBy4X5Yr9Wj5zRNRBZ22WLfZ0Po3ApUJk0Cpwrsb9IDf_olL_kj79SlBLR5K0KrPZDl8ilKHLUQaSWEVlLKEEtxNRBiK0l1xBEjAOMk66NVgysLQSi1DdaixYCTUBSPcRsw8NKVu61Om3Sb9f2GBuvVbRO_2g5VL_eqIHCNiGWPuBkXAOGR1fgNiZzbaaFy9OePdQR3u2Go2Arz9J01dLL_OV0uUNmOzFJPCnP1g9Zu4_OO0EzjyLZhG0WaflPfLDfwXjvx88hwSaT_i7cml-ZGcGig73B2_daKTM8qpwJDrzRv7Vf81JUqPYJBDAps3nDvmpsQdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=gIFHEpJyiFu8IJBy4X5Yr9Wj5zRNRBZ22WLfZ0Po3ApUJk0Cpwrsb9IDf_olL_kj79SlBLR5K0KrPZDl8ilKHLUQaSWEVlLKEEtxNRBiK0l1xBEjAOMk66NVgysLQSi1DdaixYCTUBSPcRsw8NKVu61Om3Sb9f2GBuvVbRO_2g5VL_eqIHCNiGWPuBkXAOGR1fgNiZzbaaFy9OePdQR3u2Go2Arz9J01dLL_OV0uUNmOzFJPCnP1g9Zu4_OO0EzjyLZhG0WaflPfLDfwXjvx88hwSaT_i7cml-ZGcGig73B2_daKTM8qpwJDrzRv7Vf81JUqPYJBDAps3nDvmpsQdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrgrGjWqasOHthqicTbPt6SWlIYm5jex3Tm6zu9dNS_j8MITI9aCCDow6czCEUR7iN6lmV_TqOQyGnuZmipwnr39wd3m_yRJT6KR9Zf9mgFwDFjzfrh3zEFC93STpIAxUaPBCb9dVAAiS1abc0nWuhhNFfyHWzxeOZCApq1FpRqfjFHUDs_PjQ9yMswgkJE6JFYlnHpLAUXRYqOWSeL7S4oNuF_PflG7rE3SngIjqwK2G0CFOqrsCnRicnWmmKX88pFzaqfnFRLwe68xdN7aNJDMb0jVC6MYgfe5edKjXULTE87uagMIlVTptyt8ys5Uj-Sli1HPmfIBOBSAsBWgyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWrjpoCTljzF9Iy_oC40VOnM9Vr2eU2mqnbQ2ob9a3CihK-_mCQJ3ID7ltLC_Su1X_ak3IqoyQBUc1hY5rEoFSMiI8YQDIJ46_6ikPQ33EWvIfWy4ay8csMgkHm9DPhhIbmONtJK_RKMSth9d7RygupoT-6gK1oRsa1UjgJXTLatJoVyyYQSXqpjmPTv6QgkxjwrDx_ULF79VdHj4Z530c_oP2dXzOGU7TMIJ2htGHAvk6Vyg4OcgB0-NXnmoeZkIX3FFFYWPDkllnFKe5ezL6rXOFUytEQjawbg-DX4ZpC19QvF28T_qEzqbtd5WNiAjLetMIq6qsSuAASUdzBJOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtxxTo1TuHGiXruylBYDu8d7TXRkd1lrwhcWIbmwEc-Qp7fAt4ImmUCbJdGruHL_oaG0WOlv4ZUcCtNZUytMvJM36ilQFFut2XjAm3NfSQ3mjoTuhqLR0c86Yy4PNEkcN7xLi4ZMqZf2XqQ6Nl_N5U3AR11ju-COhsuc79qo_IkZcVqB6mEfmsxtfPH8VSJm2LRDw3bUSHqRQG3_XzJhxEZmK9nifsQArD3c9mQi88K_hwGamApu7a0DlSTuTUmyOFjCQAtMymnfpBRppHblM27NXSm5LcsbAtLYwud1x9stMJiDdeXxMEhH3YJQhpn7sh14dOsnwdPQHOgKEkgPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJrYCKfJCSNt9wVnj-U7tUkoOxoHaDKWaR7ya7wtuIPI6kJ9fVsU69vLVIQB-63T1ceBLLIL6lMqxrm2K9xp-yVSEQ0eYcHlS87GWvySOcfi0Sz5MBwhnTh0sYh1LW-psw0DsIUUM9TC51vTyxBKVN_taramMVyC9Jd7AYq13czJQpI8Vuk-MLHT3_3vc6JfJJAPmi8c3mCWPGr-KwXTdecJaSTM-KggOWTWX6hNKkOqcjK2QMRK96MOS77b0sv28_2FURPK7Gn2eUxmNlE2WoIXb-SCxILjjm-n4MwF6Ndjpk4DsYV9fy-D1oaidFuQqyFOSqQuwO41JIU69rG_lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXhHNQKBnBpJYLuiX7iFkhVHHsKktV8xj6z4IpJXGzmUqBF1Hf9XcAIM8y2ZvTxywunje-6JuMEF2869LJBx0zSKcsThNc6OHIL3pl1yELOIjbIS8EAsbKAxwf78WGbLOcVyabjIgw74BQ40vbxuOG7LHX0o4A9xUnzWuKaX8ZaIl2Kx2yM4SrRVCqhS4dAjYTnM04P6G1TIguXB8gSd3fx_1AyECPYkedhUvgGB-0lOwOl6rIZfkndlib0i6HPqLzjdPGIxUWhpdabObOz3s172NJt0brG6EfIJOkl8TiPGJPw9MnXwPbJ0JhliJNXR55vBssuOm_TMgBwSQYgWgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq_kGoeMAha3ypUhVc2ibZEGXdjBbMEdZ32OYF2hm1I0rIJgTky9iAzgJ1JrpjZQRo34u2BKJtDEr32-aKXV56b0hrGYxFSQzJGTUkaSL_yunBnikTB7vOYbpI_WKVnUctzOeQDjH3clzVS5AO2HSZVKTDGT-HjEI47JG7ZCfnWlIBlTkFVATJcTGDrwrXls1x79Z3YsI5udRq4MTzWp-mg4ImP2HPeG9mEOWs3mR_I8I1XQ9ifQQ_lKJg9cCUQpbdGMjN2HOrjOJdLe9XhTbL3V1VUro0luBhuEfWFC_UEwobblJkx0AQkJMuDdgRWfVimIvG83kEPYm8i0AKYiEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOhZSjzl7d6rDfvgqGhHhtTgcrY8kC8nqTaGfXUjWx-OH1iPN94Rk7W7xMOV9k5G8SSdGCv2DYvZZAsFD7raHwHxDNQz2iHaQse1rMJwoeE42cY_uY3iD99J7bdx5QZk7ac0Lo4B-WgZ-lM_7mv6nq0vy2XRBdq3GU6SxfnCDaR2C4h-UOGYW6qH_d46QesKWCwxk2aHrnQYxPLdi29nYIpkvlJ4vRVemHQlEpiRDzl9wlnTPEPIR4FrEjQJGo_SuNfvgG4AdyM3FW25kIBWyo0OD7LCta4yijQsan3DV-TXpXcMrMi4ZIhaRRZQ8eWSwj3ya5ZYgosIt4ExIk81kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2FigmITB6p2rMKNCQX8dsOm-LufsEVg-zDeDrtPr67MQij6QPwFP_SsDJcSWw_pBlpqiPQhu-fuJkhv_oUIZl0a5AQDWhhFiR2s3rHOH9y2cyYqMVIfgha9dhL7kENfTToGG-om7IvL-Sz1aOnjz8GW-ecIeUi-TOGj2YObyQpnlTKD4C2XeAmr0JTkzmrv7-ZsQfOto4KnSlmKDlUCxOdZNB9BnvBC3JT4JLTzgnwZKmPN2jB3kHUgcpvTXVJqLWMwiwhF03k3-WZZ7LeGx_5tp0nsl9e60LMt1gnTvdwxsL1p3suvGDhjEcMWs7ADum7kaW0HN6sxom4_nXhqPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAJq7YNF8gXKiUZjxUuoPCLwFs9cHW37On0vQ0ChXNBlSQeFF7QntFqzKjKNJ09DVaWzso0ISMZgqoCfaWejbDdw5ZXSQZiI31RIkgs-mxeRXEpwvkDIvPwRNnqnezKTK30Fipt5hvGEUN5mZHB5S2_WFJu3C1ev8FHcYczPlXLe4l70vI0e7KKWGeHw-Lxep6st1SNx5c6QVGid_Jc-1FC4tR6cjNoXTJr5RF8QyBBYPZ8NX4u9Wurkn5Rc1wlySwsEGk6s7v3_aDFi8TDus6Qupdrpp-hFibvWK2ZU080o9bp3qPH6tW2-XcjGHJIiWHCtUMWtcTXNI3VKwZEaHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXdmot58okT73nHa6vuusL13ermtXLyM0tbohhdmrNxUeenhQb4CJCWLkN4m_ufuiSKEs8llGPE3NofwGvIQva3hPbQBuh5eKMlXFAOjE9R29rrEx3L8VmmsGE_LTzXYe-HI-vJjpoMk1SHuKPYKF5F0-rUQHy9TZjGEKDMypuiK7xL9e9wkF0s4j-q-ictlUFUQyX6Z__82wU3KpOOVJOYeXv5eP6Mg0H2SMBg1uWvwnrWbKXHiGf-ZfHsGIm8IUPNWbmxDWdsSnfhY0SjTR6owcxt2EZQybRdnlnjPZkNgjBNcEuWZdfssi83waJMCBh6vpaRf-YVvgl7sLpIFSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoY5KxN1vb74HxSgt8WzmAcM1M6Xn-SAoszgUSe7QfAusMK--X8gCPkqD2cCBoxrkpglED5zn1qXDCrMJDr7pu9qzuy0SQ66q5mDFvNHnC5TGCKV15emUiJsDUgTgAvRG7NXZGBPy4TFTa2zAiUOT_EKtyPAYdZcNikTsGfCywwVzuhBmwQMEmrbnYKGHhXSJCt7nUMmxh3y6A_929uyraFi25-HJe1FKqS_UpIdi_Mi70s-1V_r8aKzcTZEoAAuMcb6_0dJvyR3pyQixOZW9CB719QBWAQAtHP9q8mjqAxrbLZFpMvHjLXNxUkLloTZNzUFbTGi6_ws5euxV782gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOO16nkv33I5z4pam3_aVlkITbelXrTYPNtsQzhxcp3b4LsEhXzdP4ivJWQVEcVTva44iJ2IA8oBZGpXTbpc1kQZIEIIaCSKC5FnQb9iJa6CGIWR32JiBDhp8F_49p8Q4k-hj_VhLBnY-VSIrc243PXO_E7VsJ2lpzxO0YdoLE4r7QlcZT1ejQeOscLvOoAamcsrbsW4lgS4FObtQXpiFJsrhld7dQBDywTHqO7D8NS2VGmh4mPFtS_G-z7nGviriFtC8ixqQ44tKSU5wUo_giE_E5HdlGGFYoCaAkB95gJ71fVdWdLJNUmd_5xqYjBw5qN5P7I8pnWDR4ISmShSKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEWBNU-DOND8uA5KF83LB632t_PIm_MyQgR86M_TIRFgQwGKWGzZYnadSpq2YVZH3roRsNH-YqzJJt7lAX0Z3Y3vjEV6S2mAO2upNFUL5IFuKZDQEbecMNTQY7lQ4DzygDpLciRMfN0dcG2eMXl_CFwHJo3QJZJqtwtr3pF1jQ8Uaeu5MvI0UDVwu7tPncsZQiKxe6bDCiU_ymmSEcqKjk2YcIwqAyzArAbqpfy_-WKFKZAp5qmzvDgIYEmJdkpyYSZvc50gBjhpCMBRoDGM10YQjMxbVJnr1f3NW01GXcEYQJRpWsl00IWtJhyO3x9AaxypLEagJahFbxF2s30S5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNJU9EdBrfzkRnMGMBhef1z8qgLEpH-VtdzcsqrwYgryU1isoTSS8C5Q63-G2IBewkyV5u78nvmH8oRVXYstvea70XPing8LbOLiIMshJV3QHMyJwf-_c8s8VXvf9CFBcNcqguztZHBgv5ZHrRZds_vAwBf_zR5NvG9AbJlqp7Rju4op_IbNMjafXuJwFxoqgl-jNLvgTiEYdEJBZcwnpWvfFfvndjYqv_XrxTzPAQiiD35RcGvqSLkWMKdJrHDXmlCISOQYd_m3QtpSMA5vacyl7mgjW9IPZw993Zx2f-dt6kq27NpZEqO46O3C9bxSPDp1tTSNt_LPnHkKYRjTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNEfnXIKfAyX3pdjzmgcAjYHg4iyFURZF0j0yUan-qRgqxBn21p7TxRR7Tr0F5AojynHuwpI49NM6rqzqaboqoKrvWaucf5ns4aN2UDQgeOwn0B02jSpJa2UxuaP1UNrNVcKzkIMwfUf6AMX4XEo5i1ZzXUAizc7jq6uFiwE0D8PxxhGU9frxSQDb_Xp14skWfgh7XaVGPgCL7RULQZPwZJlNxXx5m1lwswaYUCdB47CjPuYVz4AB5OJoI-mK5FdJ1vuAZz4j6w2o39na4vgEhMwUtWF5223etcK2BoU6g0mIYPqanE6eNF7Rsq-cg1OId_M4Xkh8vvd-VkVu2WGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9wtbZj0O71mDjsLxUGmYrht_L6qbxu3-vTeZQ_tABrB_r5TqPHnOzA3QFftMPvHFBr5aHDpzpvtHDoHlC7rtOezvu09dgrB28onHliwzUaI_J0Q8lZT64FNJMMFKtEKuAZbovgQfcjZlMtaVZin68tYtaEKG68UOtZENPc4T6i_M6QRPIveHKOsr0a_mEihuZSPzV1FWGsao6Px1gB6s0FH4Wa2TObbwO4-aZlfAJTR2twOxLXKsTs0kdNP0ntMyeUSW8SE60Uow_Q07nINlwiaychvEiqIB6cfhJ-O-P15jYgfe18jfyEb3n-JYJjDsmZ5C80Y_l-ZuF85Jt7wag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T60bi2LQ4fRSFS-hqoG2Fuk88DGCrSnG-i3TEBgxXq9IUMT-E-msr4VmIeH8xLsrbK6x9yXxc0E8Uarmp50Wh_Uby9U_d2Wy1Y7W9iWFNCjxxHuckEXTGJyJt-aHdIMCLjGVMk0hMv3v6X2S-aJaWNGlQ1a-W9cTaaGB3Aoh4ZwqnvOzI8JC-zFdn97meg1z5Aalvy6CcuyiLzqQVLV3vbEwt7HGU6Ss3N_f7KNJbrUWgYTeSbi-CsEDBO3ZDAALLAqtpDJMXFKRkUINbCCC4sFmWSBQ6SOHACLoDSw-L5tqM39hxj0rxRARsBURq1kns7J1H9Dvy25v0i6JCQKc4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYPNK3YfphU5hp5Yorcj5VDMU-l3m47fiLwx4iobiPTf_QFxAnXoIRphV2qaWQ9YEbfDuxmX2z-pIn2brniab8ezfP0mW3reuXbDS4th27FJraX1Je3CIvYJlfcwPq4ebMq8hBYQMDCHu-5VkZpzPjeuukjB5S1RdU12iaMwLnjF9_U71UxBpj5E67bbg6xOU9gfNCbcSGRsna2AVrCLBjP3ISRDJbxzcU9AIOXW_1fzQcR19PBCPx7HD0NeNEk1nsiND9zRxCxnE5xScxYJi0BonxwELuC57YzmRrONWLppWlCselvHJFGFFoK6NK7MpomCxpCiiqxIX6Sq65XYBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npkXWfIZgx7KF9HFctWhkkq06n_R0GfIp-d9xJrj7S1xugkGDucZWfJCN5x6QEdwmtpAm71eWRYpMpgpezCRDeEK46XnerYfV0gNIaVd3X-R7KYaQk7S617pL8RUhalinp8e4IobAlP2gIAgB5DPg1uTDSSjw0RxAx2WpCdyIsSS7EHHzVH8_Ynwcdf4XaUBDK5BPWfL9LUOhDwnaMV2np_rIvYAH6qyteQoaG10ICnpcNmdP8zLHhktxQZTloEhNp2E7sC7OqLLe0CGFB_CWqRpD1_wSzv75952CJ2Nl_f9nuzG1apG0_OCaYDi7dDhvbFebeL6A2JuAI_k_432Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUS0uN-THz8fS2xp6STn36z4C0AsqQ1RWR_YfHMk4IFwBH8z3GGzf59LNuLsBcnjKHzT6Fv7Vf8mV4dfQ0ucvEI7t8Ui2unrM0Y0Lk-Kc5DXDe2yBEW-K6_n1H268a5dZmGs77HDOsGk26-Gi1wofOwl4LXKypl3IJDP3WS87LA4zf4_FtwXMhlr6f4FaZs1oC_wzRuulTKibavg9UmSGW8D6RI3zd7z-6E8233r-gSJnb8ErYoB_Znqlo1RmyV_oCMl1Yo3IGBxQbPVzRMrbU1cEHUfnMDAbKI425ExyrqP6zbi2s9W7VazsKfY2E8oX6m1dqW0tivhhdqXaaK4OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j21AwXuT3r2T-fBVFb0kp-0RvRTlwOcf0mPr8diUBQ3VIxgoQHjPsrA_hZ-Q9gGXMKcj3og1kJdyz-17IxbqcSN9RyGROBNkzSeMFtoJIvcJnnz2yxyEthq_yTN-5SStAEfN9DEagYPLv4sVc9554_wdWyaRQmRJ7gTVbl4efTIdGOpMJ075tOfVWvCrEYyO8Oni0BBDWXrxvs5JlC4l5F8jSxCLIQbQuNszF5q4tTz0D0Ku7mcsLhTPD2afEv2RP1LBzw9-b6keeGFoDtsClr7QLH2QQAPErFKmRe_Xv7pyj8xJ21LJv7AIfm4Z92fr-6IX455vbfT0VLCF4dun9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-C2LXHSPO4gFJ6LvKMrlulOleQqeR55tyQLaJRRmfLMKhJkO5pyERbRTrdzSWJ8UKMZcW3FzUDx7jI9Ntz6Aa0g6JMq759Gg8Qr7cYxC80Rn3O3tP-1SZlj5Y3e0USQBfWiPR0VoJJ1JZacQ4Mi3QzPvTYtI6bGx8fIAm1l93ZYbz_p0TWuhoy-mJXQ8Sk6249Yg8SKoaSKbhSaMGYi5AR9txZqo9LubJUgB9iA6hoK27mSSfcHOE-RfwAKKOfbwUQpKAtaQYkgFwwu8jI9vdz-wBqknpyS7KWcpZtCslUz74I00EDIbs_75KU1cAaJ26Bl73PSnFnw3oIE9HcMeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDQc-23WkpKs9rK6EqPoLMgSHSjRnS-Avqygu4Sxrk4hdLdb9pFrJANvdbKPLTmzRDSOVlM0m6Jy74AP1-VbBoaqnC4EkTNq_hduSA1wQU9u51G2G3N7Wv1F0a-6HlbgGHxmgBaCzHLLuCMPm4gXF7UHsr1YmTlks1YKWDtBbLU-yl7OpGMg2OMnfkUhc2GBzSG1PTHk3BnvM-Uod7OhplaXkOrIbUmS3ZO6GmwU-qKZa4beM25A00SfKOHL7KgWcS6w8vfbGvBkViJIcmTb5SruTzNzKgs4AyjXzx6qGv711UntGnF66PfSvBXDOrkrWJdchQfn5dYYF2qETWPBww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTt6bcS-gB3XjfyD5A_wYIdK7G1vY8bduCkdJFXTqCUmS3GLYrAsdtkAdr-8RVbbOIJSez4u2rDiZOod8NkRmSbpK-U6GGBJG3bcUaTztIhniedGYA8moxd4kyEW05nyXXJ72ro4cEBiZ7_GqfFaM4sy-9Ui1OFeQEGMQ5DA1ZPjAy3oBdiPBgXMcUTWD7-Ofu3Zce0Tb9_1XFUxXed38aBNC-KUIGI_b2nW0FhQPYQlVJuHcVoasNewMRCvJ1w3KOzFypBWzJ67X8L8rtjzXirBmqoOWeJCb8wQvDzkehEXQMr72Vna1fkXocfrfCMWMA6nlonyBKxqKwYqw2NyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QupXnaspw1XXkYv0ZObpZccTQrlHAUT1SCc1Qeip6KIPFLNy5n5iKRUkOqLhX0re7zvpH73DEfWqoQiVFm51PR7PwyiNDwOwvLh0wHHRl963uVW4mlSSbZDRNqHPKLk-Pb4Xo952QqBQhi8c9vletnaXEn3dwfvx-Q-ZCmSWXqo7OxB8JdOjUIHucixxF1BbuSmoq-EGQevuwA-fhsAh4ckxDJopatksAa8uIAXcZNAZpedz4f2NYTXH4FrhZMYiLU3YNjGjzX9G-0pdX2T_IAgtaf_zCDiActe0Y1iPpfd_rAy-PmuuY-W4jF6x47iDTsFLm_8aDaziHVxRprH-Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0FdGfBbVXxNyZnavgL66wkswKwjdIn5JXU-7j8WlzFVidE6hy2GF1pk37z5YIy-wEZyz_NCUuOtr-DgWHHgXJ7sgRL3d2jwyrQcqGZQCWWyM57gQ_IO8keoK4FPRJA46uindL1U_WAn9cmSXeOecJBl36lsum3gQF_-oPMMKM_ajTZw68LmBrbPgxu71bNEBu3h8-P5Cihj6jnG7KhZVkTuGbIUSksmGd11mShtjVL8NnU-eGhlNdih1MnkJwwxFbJbmUaYzymEBI9xenKrWZDnp8hrYoxE2g7JR4dyIwjFai3cJqwj22ui01scii4ShOgEIkTy8D_bKtNH87PIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dji8UCNJDQ46t0OdbdUM5S_1lPqv86DbPp3mZzsSkRZYZYAGXiAVvgrxeCFQUV2-_ioTnS9RS5aB6zrwsxRbU38IFSqHUVBD9AS0PIqHvzU0UJAo4E4n7UIt1myirdkyHnzTlrvEL6TvW2pip41Bz2U5a6mAP_5TqHnre42XYpb5uSduk0GkdL2RHuUve1qOj5VI-pPEBZ7T3nafnEmv7oJrk_9sd0YA4qC2qhA2l2hqOce60eao0dw1tbWY1U3hxA-_UpGIAdRtgnwxYRUnT6EuHc29iuS71wCAK_2aGXVQz-wuLkgiFJ0vyug4E-HVnFLFHL5h8znsttmut0alqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNj6bEafWD-iaetQ2TC6oWiE8W1zC8JAP--leosGbupPk9A3ljPV0foReT3IkWToe4TB4laz77df3Ad7ZE0aoMZZUdoN8jEkQzQXn4eirGn2Q4q8puOgJfqi0WHgKjMqi6PJY-pJ4IKK7-RENeNDbGk4s0Wu-k_2FI5XQtb-hg8aZO0NqdsXRDWJvzMo_ecC7GPcQ_pE0Wm1I25zpyrNczOnq8qX6sKoOl0Ym4eSTNODF78ZhgIXOvpD40l6fZfmbcd5smrkpPEyCTE7UAPqXJ0tE21PdRhLO6fnj1hSmW0CY-UV3bNTW-dMkZmiucfhDeSNPeTEQwiQFwyPcS3COg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siCEbzMbK-PJUg4h3DxtThbjgTkNHLdyODbETxBmng9CbhGlfwG-sdKPiPnEmevMYa8YkP0xoZiThzXFJ5AXrqbwr8I06YkKu33nVHIF33GHZXo772lqG_qcb620sag8O7M-na_xxjdJSwNflprlhNrmF1hpZ0AyLDkotpaHlMG2kNEDmlsaa-2wFhi75XL6sGF2YeNjv2VhBpCIcwy2olTWJ-obuDyTRqLZ1aUIZA4f4vGwLmtlbT7BBEVAxmb_4RTnQ-Al_4JvEf4P1-4aKL8L3wx2nj5IdiG2UU-MrN3rpO_YrHEnlKaKI8cl6DGFx6lDwmDXQqGhh8vsKws7jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p831PsZpurix_svq98SF-lTU1g0xw5BYsTiHr1zWWAWAX-O0l2zxQxUor4mVHYTFgOq1U33CYgZ9tvrVBPAdXbP6in70MUr9e4Jfue-IO8g37h9LiPwiXkye2J7xtA2Jjq8EOTbTujoJNm67EbdDKQKjthG6D4RHlyGiPsYk6cmoc901y-48Jb8t0aPh8em_oIVqXQdjJ7SgiTjs-5gCNlMRZI9WV2w1uDpcDcdgXHLlhyiXJ2tf8_EwbrlXPzpGDEgHlRnbVagbTlhhTYPEbtw6tJIlSqzRgIVcskr_VsGTOT5ezfpP7f_zJWB5XsLzgJ8NLe8PvDkQQvtPg-jfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDs63tX1q-lv2Sdz8t8Q2_j3Z5lEWO62r__0AzoUrbrMTSeSoLXYhBaL20qMhEG68u5Ye-vzKE9FxSHqxE5GffuK1c1ILxdYarG0kz9cPWPIDAlKEdM_mlsYfn6UKKhxqDcHvi1ibt3MUT0V6U_4Eiyp3wxXib-nCVMn6O6swvx7Ex8JhLv144R_m7W_VAZHe2R_kuH4d1WL2YGFSJwsFwa3sD5cZ95SLCTErGfNTWgkNAIxLATY9G_OFlbnpbzclgIelWWLdywqdQymJN1MoP_vziwSI7kwYGd8Ue2IPtOeNnmf9dSbMG3-UURDJwETpepIRn-JKgXpAmlimTCybQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cq-cXx2twKHbBCb6S3Qit5KaZzsd6xRAT0euH23099zj5B_20_JwZTQ1m4aSR61vzewLSqRBU7ApbqHxWM97Ut5bpgSLjwW5gHEzeB6IJ4OPPTNuqCRqLr3_d8TvSKtc9PuBNW_MjhvrfE-jpd-mHVpHFihZrAyDFoUby5VDji95hvrXYzLpMUfiT_7xJ9ju0lrMzYc-FtptojTMZi5DPfda-oedinApCdiunRvdnCuUokeS2hG-tUSDVjQj86CFEtXYa1u2rA4rA8qDikXtg3KI6-GNMspcU10k4xqu4iLePXg4WcKV120XlSV-vVvQ13oFMN8XOC3Pp3G__wqk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4BS9WNwqQ-g4Tgi6ltlnsUz1j1IKBK3BoTrwuHl7_qM07LxSvlVdxVff3NROMqJLgCNvJ9Lql9RA4XmDraMSccmttDy5yo0Y9d2y9M82BcuHADz7tz9FzIM7G8JRj38gwm3N4Edc2UxrNgHFplHhMCzMkws71cyUCaK_91aRlI7JsKL-kd-NtOFJ6As2Z_QjDPr__Mx5YOMbJVZ1mAwnE34lQTJMYa2XNAxeUkvFoI_CvCo-_Na1jHKr8Uqo92EbPGzCbSRBze1R8-88psujbx-s_RoRtCc-jG-A3Y2w5QDY2SOSxLnxsI2i1lrjbTZ8O4-DXIsOoWadQAElDuW5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvljhaFBDRej5Wz2-qTpIZ37xfK_ylFch0u7jMYEBSrDjrEGj6sYlj2mDLp_OEYp_4R3GhY7J3MC85XC9XnANW7It2y9FKwXT-JfaJvOytL47hQNcOrhWEZ1DaPYttGZ8fkHkqGkoceQdXLE2mYCDts32AIFwxmt0-5iYbh3YLBnuWkjnrUWa8ufB8kzMgVezgIvQt5-ON89DFzB62-G-rGR9qobzjDyCJF34PHw3AWPSMtxPOAtT8u3nsCTiyYTc6Ay6cjm-vs1ndNZWQnDF7wzNexKavOd3Krn8Psq0H9AN9UXu9u5JPwidFV58KwA1RKgmQb09MfCqzjfeFk6LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHKRq7S58ZwpHI9Lu72KtFZe_cz9Ka31q2Yd9Kn6W22T0Bx1ehrGyf-OzEynM0pwWcinUHwA0D87SqQoGMUDkCG7Yrw4jPrR8csYRnFoGxAagMISqWKwaWPgdYVc6VlPlz4Y_54xgOwzpJ97WhYjWcPrJa33-e0lnha6kXkHCOR5jcmP4Epg93-uUlxHc4yKquWwF8s6LgZpz-svRWPWUCRn2mU5WeSc77yWoLk_dfOjoKv-r33EwsLgmKYAKlS-ofQgRXovLgX0_A1h63wWtYxx9nKVYYA7Uu3pfd9jYc735EE-7QSQJ-uarT5kJmqSKPE855LfHN2kWRSdX1b8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIg4LqDUJ4rUy8-lzy7XFipx-SM2YBeEIT7htSSEnnDS-pk9KCyiqS0ytbx-eCbyN7SHJUuEWB9QeXrEB2ncjq__FKwgjBKcndjJImEZ6RcuTJDKfgIYN5Go7EB0Swg0c8C9if-ZMndfbGwb1dVh38jmSEgRvArmxEPfGjN-XbeP19fYqOuyidemjqjFUMLYjHUoK49nnIPBOoxmMn5tq9-nvp7SbxWMfrUQPCIOSk8yJLY7_ZK1Grc7SREy_DcXDAl_3lagcAi7YI3i0cwKiNwqxpOrpRc-lHqNdGuSFBB62IhEx4C2G6fTtpjQovMgs2meLfT6pJJINZQ2e71uKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_gMVWLIIwXZ_jNCpiZ4guiGJLK1HN2FaPyW_73gVRCgqIp9slVmEhNWgGqnHAlSLz9bMq6aurAbO5Uy7QhjqtLEUOyfBBNJEEGgOnKo6-QOsi5WHZzAtKPykJX-i7xKPW3mhqkARwN2oNNaelJotPeqg2HU7KYXSDyFy1ls9DuVOjbFVxDuOF47Uw-cttiyR6MLo6ivbP-txbirkMSV7OZWwV2EDQ-vW6q1qydYVXntwaU3MylDNfMBYptWHTOl71cFScpzTnrrN_XzhI66n20iLdBv1RJ42aQgS7eBXczP9cgjDTEK48Jvm94HU55aj4KpLaJL_mdDR2fYWRPlow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUUn4G606PiglLKAJbRs7NfjXTVOWF5VsoUSgJEiD8AURVq5iQG_8WD0OXMCru5chPJwbpTh3ZsvKb-xfALqV7PItVdPfrqms69UYyM1UFK5CYlDhERf8k_hfyyg8_jEUWZq7FF4kcxddyyrY11NmItRjefrwsOvs5yX01qIqv5oSSb3X_YJY5N-qgJzbF9hiXJbturzDBkmum5SC8KCCmbyhnp21-zhyp1HY2p2G3aS4-0Uo_8viVvtJ3y5ggSKBv89HmOdEZrIGo-eFX0JpgSrHBcV4dE_nJK6WgXoykSoKpZDsOgQCXCpCKCTdlxfDAuk3KcVX3Gch7T5d1EF7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbTXuU1yD6cz1R-rAT63dFpfQnsOGkze0AasEH4f954_1A6wnAml40vVnuJCr4-RtAR2uxhU3kT9t9Ji5iwlcMTUVUkMXcEG92PFqzpPKGacly8GeFCxYaGnr6prWjG_sSIO_rHLdjeBFm1K1UaLQb-y7U1U1U28KtlxEVbgd5_rMz4c3t8TQnYIN2Xmnyo1mdjU_pdN5qnBZSZJyAO5dQXwaUWaDB5KJe_x4xSxwYNlxxV_yBZv6yQSROlHxgFQ9g_FjZRL8Xy_l3FVDwrc5JZWUW2LQKla6-fGhep6xLp-ynofh_BrFM7vehEPXdUYGG-gPUZcML1oySdqjNBypw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJlmEM1b6KkjNOFMtya4oBxo3Hua3ws592aV0rMJY_kZKl2c-lnZ5WetRX4xWW_xfNsmsxpzbsmBXm-Fsye39tssDdbdzGML24oV-EAapK49VFKYJ1xuf2bzMMc9XbfuHxcoiUCmCZMYN-71wOvZHRnwV1UUQc-_fX-u5nwGNW4_Pb0rxhnvch7q-Yj0f9T7WLX2JjP8NOM_E6ddyj6LO8AzkMXoftz7xPs_bGlG6Ps5ZtENGO_AtLZ8JmHDuD2HsWZHZR6POXxEamcGf2TiCm67NxOA4IiU2H98irccWTGhjHW7OE2Zn-yB3qIpdXp0EvFus3JoWr3TdeMrUvSvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnhOs_b2MtLuMKVEmpdV6gYwfIvMQbgMgXJMVfTEr8zV10VuWsXYGt_q-JCxEyUwp34Tj6Vfelt8yW5LKHt4hddiR9G1SD4pMFlnWUoP3IQaAHCMMCjSvjMWViC8V7bQquO3Nhbl7qCbyWwyoDapCm0PujhFNR7EQHGScXYSSBRKZEv0YLvTrY07D4foeL6ULim5lzXU8Cu3_JfMxczTHfbVaYHewDjtaZkYHNhAU4A09qdETb94upmTaJUEFSxe2Fw_qmyDDLKLYrhwASWav5grpmW8h6905Oz65HutGTKVxrulFRky9k2l2hxPvA6-sB0YDTjcMOSTB2lB1orp3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_9dvIPHL57CYjRIGItstDKx4d_zdY0UeEGTOp7875VIQWS8D5Rk3UfXmyTzUAwh2wVeF10tNZ9QTuinSulSSDCiPFrl2QiaCWGy5rxYcS7Lq7FhXBT0YazeJQtFtV-yTHZoiXLbDifnQ3SWBDaXRmUP_daM6MiawmzTi6Lrxe_H4EcqmoQ2iawdMZk4KmMHBUsTD37Cb7SX4Q5ZiNUYg3ugH3sUJw9OIXktq5-gOT_tYhU6uA9SfYHhX6s4ewuWgrxrIBvlU5qrPoW__XdEyufAwqVoIL84KJlB8G9pj17BHOW0iaAwRDusemMXEAMkHRH7A0TWuBmJuxXfQX5q7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtlonoWJ5mrc-WAFlc3NOs8Uy-CboXtCBXc1TmLQ18HeFRTvYMMhUAn3ydL4DLUNw02Rr49Z5v2hk8I1I43ZlHF_Z-QGLtq0OiOZWZK7Fjfu0-WVuhXYZB1D29OWJ020GcW7IKfxC0FyMEZ06uBYbfm8y7CmfkkDz9G6ONiPFdcJwtKwGtB7qUxDmwqr8takkpWB83bFz5ow9etwq8G5hIYzxs016PENOXP1qZuj-S4k2SzJCM9upiRNPRT4oVkag6qRhbyAdQfcYliYVD4xalStbK1_0YRKvlXO23O-zzoiz1qGjH5ncSt9N50c8NsNqgHcQX077e0xEreSyYrZCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNjGItpFOpeN_5w1uqSSMHaixXmo2Wpktpp--X4z6_hp9aea4vn_u7UsvrjGfrcCUjl9DZSXrXBNQo-uS2Z9gRmRmC9XZnfDW_aVgsnJQctnyw3txWI25YMPjglyXEmqtaXZFUrg3ckj7FXi7Zk93FE0hSEjC1_ZlvqWBJDwpKQbq-U1YuFgJyHgc3lGHFh4e72CtPfhVVslxGHKogEfCLiGf8xnHtZC3qASbyOkzj0UCK5sIQs53rCMCQ_2Y6-IJYH1qYNs2AbFr_1sZCKXaQWjrNWdd7jj8b2VnpWaOGj1iUWDPuvErfpqlQdI5rS-GmgOgfj5M3VM9HvlWs85lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgeph-hIHXgQsZgcw86LNAnMM2WoOuod5tmuy-G2Ws6danrcDiF0lnqDSJdgePjrCwQyiY9qeSh-sEObGmG_nQgCah4OS3y3MdDFHyTr5z33k8vVo9nJ0DYXQ7EhYGzNAPMPSDW3TbZsNKWBXUQGCWV9oFy5Mzv-M3uX4TADCy6QrKCZ65avJfmFkBHyey4mkPOh81gfMwsVkLImBj09n2F_wkui9jLdM22PDDXdyuHjBnUwDQsJlLDpDJXroAZmshP3YiFKDeFigkWKcMZSZBv0-tGj4SdJu2jZLLuLX2HxYsQF_dqtth10DS2ENr2ljqYW3SDrT2N6ilDarTDjzg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=jMfZEUwkYTzDTBm4ghVi_LG93KKJn-9uehEV1d6xE6istt5bTVYMYttuqiGk4EheR0eEbA4HgYU3XJyAOLI0v4Lw-jSO0BUsGsqonqEdzxxVXQS2NiLoAyGdx8ktsw1Wypt1OTSsQln81Uf7YsVkMce04mNw-3e7zSd3O3rB6tHaLK9n0F7VOZqM014JG_EiUuFWLg0fc_67GcvF_mLdZ5a7a_MwFd5E7DVgaEZQWXq65Z_ZES8o7v9YQx0WQ39ksvIXbNnlgaCuptz4lCuCmGOLiXDA6QnWHtEG1pLlMADdtr4eX7mwYpF9ZMiCYMgNQMDkmy6h1w1htDn9FrYjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=jMfZEUwkYTzDTBm4ghVi_LG93KKJn-9uehEV1d6xE6istt5bTVYMYttuqiGk4EheR0eEbA4HgYU3XJyAOLI0v4Lw-jSO0BUsGsqonqEdzxxVXQS2NiLoAyGdx8ktsw1Wypt1OTSsQln81Uf7YsVkMce04mNw-3e7zSd3O3rB6tHaLK9n0F7VOZqM014JG_EiUuFWLg0fc_67GcvF_mLdZ5a7a_MwFd5E7DVgaEZQWXq65Z_ZES8o7v9YQx0WQ39ksvIXbNnlgaCuptz4lCuCmGOLiXDA6QnWHtEG1pLlMADdtr4eX7mwYpF9ZMiCYMgNQMDkmy6h1w1htDn9FrYjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if6PTFzPPxN6LDTkUwX27vpn8w1v2Ghl4mXK_DnDakJabbMAOJDGrBV48M0Ku1Fvz8zgoMiIqkVBB-_k8iTfCkThlkd-L69ufiGM8cGmFcwtl7qXRE6FO4Vug0GH14XdEvmBdXK6_EZ3Ynm1qZaa9qH4XVKfskkMsdxlkuNfvCx8bI5QZSUrTrr71cSUT7qei6KIkdBnYk1nos8Nzm98t49xiLR9E3OeUbralytnr12lGP9vY1Khr7hLz9AElbxQN-Bb2ZkRElKlDfBQe1omo1MBpJByqYLDEvbvA-PBA0kwEcd2wkF1-qVPMvYZyVrnkbwJ8POkwYv_pAsY0g9Z2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEAF12-twOEn-nBhdqOp_RyPWsOdY2RJcWdOS1totaJshzcI4zttYcb40aCdv5wl2ONk0oSqNvG_PmvEACFb7XohKh8ZlqGatDlF0S0aoDC1KGw0uJcoaaySkPk6MwR0e7o_2XtmjsSEBPlPikejlDb62IYqSWVaOgm4c9kvSI6O8pJaz18LVdJ-DMzc-3xOy7J8tMdazua3HHQQYj-s1yv8pCoAwbbHa2I78UWg3CDVk5btpRiImgiCOtGzbjchnrMghj8r3QFAd5iMzQQajy-yq-RxJ_3WC7B01coQy2Cjk969dz_pnnXieAoSncLdwzWdv7Hs95yjBCTSvMQjvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTpb1ORmEFY730r3Y4Y95gY1XH8RhFqchm_xLKAV-vv0dtRS3a9dfAorjT-7ckTvOJa0HnY8e2XmMIi5BOVF8DHiPJVciwcsR3j2AP8u5HilGxniGwqxKD7u2tjKOcTljBBVRdKsGyS4nk6qs7LaAp5ABOuMMvTUxoCTY3v3Ali02TqpUw6bLE_0Aljwk4inOngX4I9G8aw3KSaDlGVW3rvTBTF5jdP5k2FeBiHzrijokfK1vTnx-r46LOSTsTpw_mu-iPfS7TdF--kAQGTyGVJXZ7L54bOm9iUCYLsS2XV1WK4BX4WDCwog4xNMnjCoYjfDqw3cghGKRIkUM3g00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpUZ9ke2D-mqzYRVSTX4Y09jslGGtZFMUyTPRd-ziHWOGWUDMRFWkwdyBUT6WOJlMXE8Rck3M1Dr4Gxrb5jeKWLVIxG77doqeqldKCEewjTBZpi0Y-hdP2VBW6gSp_IDdHnF1jJmqdqIhc6y04Vls9v3Z-QPl-ZU3v2yKpUCkF0C5YUNNPk1GzQXpttis4pCc1Lf4h6Slopn00oGGQt4XVAlkbr6utnh_CLUm6mgKAcbB6W6kVKsUjrixo_O8s6N9i3dFC3qtFfiCrMhmYrexGcmSl9bXSkrMZU97-bHYK6friDHS4yS7Z7Ij25zUviSse5b73kqtz7JD8snaiu4WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtqZPQHGN7qoR0MXB0qNvLBf8txAXZDf9o12N7N8kWyEIySHEygG66VZdPZyN_oUjpvgYdVSMQwFgMzOfhspMxLibIhgjOOeVp3PCcbWAT73o0F0LByw6bplLD3WGKEvmWb4_qyYk1nPI_R-nQXU-vDaycKFCcfwZe-TDQqM5Eg6IrJhP2F-KCF3mCx61Gqp9rJKIsH_8-tLb4pS9shT7xpkiXAdbJHjkudHkHZh91riTZ_Zhg72qElxIowaF3FniFdnyAEJBvaZQGvfLh30wnhT0xSQmQwxnkIpc7lUAcFT75aAp51Wyxx5ZAoQKymsk4D2ECGk6XD5_TcIeHGkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6e827bqSHLv24ccxch9lBNBfzjJxbHbsH4LP6-tUbL9saGiuHaV0BQTwvEkBTjRxKoXf96I9ED5dZkj4adLC-hWr6NbEzuVJIO8ste1VwLGt0m_NFSiyfK5ZTmYpa04oul03LjG2ljwpXdhgUB1R28zYcAX1p8H07-q1e3XrrRoWvlQJKjFfNzlG2uvwA11u4_RV_YTpzmBdrDS40qgDM5hwvHljF4-PPWyE5fuJBvcdbTbE_3mbbJh4ZZ5fTIDymBF-02D0IR_Ycf5Ia-8FDwyl7M6Bl9x05KzpUnw5ID9SiCxiiwtL1Q0gD_EJERYNuRq1k8LJ27q3251LZ7ygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oc3aEKusdP84uyRecK0vi4sEDGN4gDxmAwo7Iqs-om7vxR3UkH_Ow1VI-dYWTq2hx73fPDMrimDetYQmBHDbLS86m_vrN4_2YojfKsIGC_ozEohLzPVl2PHk8ToLv0G6-Mm67n8zaW6EEoddnT_HhF0BUD32sOErh8s-_yDsSZeLDy0PitlDjWp16E_-uIfM3_DpoZY2XcaGNfXGRW1R9M0fIP4OgHPKNRss6lzwhf_7Nugaj0ET-RiuEXX3Zg8_fLVs5yN2Hy_XMQGU_CctHNqYJ4L8kel9k6ysdBfbLNPW2kxJOaZw6pRXUbfhs18mCO8E3SCZQxv0Tizwoajvwg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NVvrbvc5-yDiWx0yetlFxB3-wylO-xgOak2akmIBEvQV2UYroT4GuZVhihXAB9TbeEEJnz9ZN46H4XtmIhGswnOdCsipSB1-a1BxOxbU1c71yP_eaumq4T4WbFHpTDZvb8lorNBzkx5nBnloVDW5cWlNEXtqlMqroGSmPpUVQJ2FBF7kqjKAIH4KDMQmXFSBn7KUH2MkodjCs2D7pMcpGBk3fef72PIRG0yOuae9HJz1IhFGWqeuBzifNv0L8-YvJBrTP84JquxB6CB2-0CttSZ_eq4lwZ2FlI4QriL1_Wbw7MooR5uqDZl9G1npzef_iGbpCbGhN_m_ce7QoSaW2Carhz4MtQbydIhDkj55hcAF_WHLU9eTC_SZ9iRRaGs32wUYVHddUrX4JdTNCusL95p3JQY9UOG0xxXuUA3Oqb_b3FJB5eOkOf4uRoH5vFQajrbYu7atc4PTRICGOD0reYVG2lvPHWxFGLlHiIqNDpsHJxjVUzr_n3kfmyDltbe1hhAwAA-fPLKy6PLFjtJ1WVIqGhWCuq2A_svllVJDsl4mUOrDJXb6ROrzPadKzJN4HDEphqmoGAlf3l6GdH3NpvYjYPk9tBDdMguUjOyGV6rM_oanNkvS9gmklVELpClrdJWK0q2uw3KbMBwvqontPDpohSG9KmWnZicW9Avf_zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NVvrbvc5-yDiWx0yetlFxB3-wylO-xgOak2akmIBEvQV2UYroT4GuZVhihXAB9TbeEEJnz9ZN46H4XtmIhGswnOdCsipSB1-a1BxOxbU1c71yP_eaumq4T4WbFHpTDZvb8lorNBzkx5nBnloVDW5cWlNEXtqlMqroGSmPpUVQJ2FBF7kqjKAIH4KDMQmXFSBn7KUH2MkodjCs2D7pMcpGBk3fef72PIRG0yOuae9HJz1IhFGWqeuBzifNv0L8-YvJBrTP84JquxB6CB2-0CttSZ_eq4lwZ2FlI4QriL1_Wbw7MooR5uqDZl9G1npzef_iGbpCbGhN_m_ce7QoSaW2Carhz4MtQbydIhDkj55hcAF_WHLU9eTC_SZ9iRRaGs32wUYVHddUrX4JdTNCusL95p3JQY9UOG0xxXuUA3Oqb_b3FJB5eOkOf4uRoH5vFQajrbYu7atc4PTRICGOD0reYVG2lvPHWxFGLlHiIqNDpsHJxjVUzr_n3kfmyDltbe1hhAwAA-fPLKy6PLFjtJ1WVIqGhWCuq2A_svllVJDsl4mUOrDJXb6ROrzPadKzJN4HDEphqmoGAlf3l6GdH3NpvYjYPk9tBDdMguUjOyGV6rM_oanNkvS9gmklVELpClrdJWK0q2uw3KbMBwvqontPDpohSG9KmWnZicW9Avf_zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9cVyzsIb2aVM8jdBCDu1d5-1reHMlQqA_L4gYi-EN0V7kx1XDFdAMFgTOqOR4cMkBQN6z5OpFhxTApdQhT1C7w2I81H8FRGtAc-xD5Cblhm-fFt8SEw6clqswT7zJAG_TJ4LThANw3j8vnuLdpFoNOnugPDNdkPsEDUGf0L_BjnhDx-ywD7KAYACaj1x5EI8tj9_II_AG7h-IzBGkBp6EgBJIEf5x87mhuxepvJhFAlHJga_v3PbJbJnw_LQYf_ZM9jMrd6mt71zZiwGOLBLM77tpO9z-5srUvUVzGtWGGlYOKHTuhAWiKPuFvAoWkuxY9PVoQdW2wCyIv6UmxlrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuuW2dsPJMCSmdYzDz3-pztDnUpYGskS8n8UxerYpHwBdukSRHKfF90UWmAA8XiK90PetKd6jlv2OX8qvX2g0WZIr1OZ-rNod2ZISRURoy4Nr76mw_-RQ5GuY0uzceBmoQzvUcUMUcrd__YbsNvMpweXauK0wcTDi8niszA4BfLyufr1KhNrJ2tfdaOwofeFSIo3BR8_jL51p1RCuf37HCsSs_I0uezcR0ztaulvyrl_XOiIskcPD10u01EDmyO2i2E-ZMYAsPubJdaupYjBoMLDhIDqeV7cyOtNQk0Kvk-WEXI8AFrshwHk3TOKy2TUyzFTS6C9Gkr6KPHU5uaI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjggK3geZxRPQmR8LgYgYYjyydWuIPtbt4nTvL9PXjQX4iDWI2GDaMAdAt3Ne14br6tOeE9RTjo3F3xkk7qc-RKdR3ak1ZoOC2_WiIE8D85uSL_fOyNkikaIDdvuYc6o2xqpyBfyoV34bcG9cv63bLDaBc_OzEfATdlhoWjHQ5vEneW46WvIcHA8kHrs89oRJY4aq95C3fdFCQ78J7jXtxjNH1Yls7pnYYpvOzitkB1O36WFx43GC79ZzWujwtXnXMvzhF6uxTcSGkFlL1u2D9IuNRs1EMkn26yIyHImo0Sl23xYdeSchT76-D7QcEtiRzQpS6objIrwUcAap6ki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGo7V9WKpNdDJ9p6O-TAgAHxzyckgPwnqd_KXvVcDt9fOaUJpIDStDu5BxFeDeZilCoabDcHZVxAGgB71I-VzjUrbSW-1f2_Kr4d1GTUAwrPTvoj75KUr9EMCVmjzeihUC_CsgycBwAQZEiDiMrf816eWXYdIUPtEIouGoskDL5tWeM7y-K3RxGjf7-rvrX7wQLrytM8MTsutkVvnkn9U6a__RJxiBTg4pTipn5w5WnQsftORW4KMhv-JxPGfCfDGKui3OAi51B07GDZ43iWN8-7HwroIgGGjR8N4WxW_GxjuyiJBB_aYuvf42lPGA4PkWLnblA0VKeGDrEuq7M2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHalHEuFsrBK-mJgR5X5dN5K7mFksSYgnNrmPEND60K6dHH4r5S34pqF1J_6Ci4lEP2PG2JS1ITYzYRDV9PiEsovAhZAjN3OLhPXijm2HOCrIVVuI8RZTcT__57feAZDluUveY8mvBKdLhitWiVVcGWoHAE2hJE9q2CV5irwo0jbNhhoewl8StrtsWd7ORZjjQddruXgpJ-swedyRqCyO0ZMhOUSpLRIbc7jeS1RczUlGx-lGgQCUOqL59RIberIPHdPVOu_pH1iCjEsCGBc-HJiL9wWPp8qMI_609s0bQTjvPy4OkN0FObT5c1d3bOaOjlXkfGe4I-Y6ks3OXjySQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TP0BX3Ad_7SxPc509BdOKBOzjvG3B93Y2Y_hiu9iD886WC9niOe0Tzic3QQc3HPOS0j1zWzp9Mx5szQlDDpAMW0OVwI19e-Ue6aZIlyTb6LAeVoJIygOo0YqoMyr7mQ8z5oYaCWVneDwKlqbyVOjWbRVCuG_7w67Wy_hzQSG1CqkMCKlciQiLXtkAB4hoXOk6XEYGhPzg6mugFfgbXOs1Vn9AaFM4e2l4bpafewvXBWBUHbbExchJeYa2dv7hQ8GlwzB19CVGGZhFH89Nnl1Y-uDiZB5Q4ES4Ehfat02TiusAxL1vEbijxWLWgnfml1dJJX1gDj0NXxTg2na-EHVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TP0BX3Ad_7SxPc509BdOKBOzjvG3B93Y2Y_hiu9iD886WC9niOe0Tzic3QQc3HPOS0j1zWzp9Mx5szQlDDpAMW0OVwI19e-Ue6aZIlyTb6LAeVoJIygOo0YqoMyr7mQ8z5oYaCWVneDwKlqbyVOjWbRVCuG_7w67Wy_hzQSG1CqkMCKlciQiLXtkAB4hoXOk6XEYGhPzg6mugFfgbXOs1Vn9AaFM4e2l4bpafewvXBWBUHbbExchJeYa2dv7hQ8GlwzB19CVGGZhFH89Nnl1Y-uDiZB5Q4ES4Ehfat02TiusAxL1vEbijxWLWgnfml1dJJX1gDj0NXxTg2na-EHVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP_y5GqBlEaYM-iM7y-JnPdau0GeiNHua5GvB39f_2pvmLm2ny1g1Rlw4ZzjDLprbxCEcCukBBggbRxWOOEVgSQvzKuCmRqr6XsoN_PZyHtTekvcUhYrD4dWpNZH41lqB2K8fkxk1eQy2v2ICYBevYqtUu2Uzku4NMr9Z3Zvg5qYfMs2gIe33jZS8ffrq5oonPglC6hVaczOehDbP-rE9r3kpqpvoS7LbKL5inXlDhWLGqJZxxViQ9_U9IKPysHrs9fBek_iQlyE0Sv3bpztzdD1YnyrfiT1uKmmNqzVO--vDD9T4O0cOyHf7-pOH2XWOpDc9ZGMnZQCQy26-nYhZw.jpg" alt="photo" loading="lazy"/></div>
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
