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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 07:59:57</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 390 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcLHuY22rwk4r1P4vVQH4FvjVZpLB7l0s7QJxe-of_ttkjuFtnExKzR1J3JlRGDbAH99qijJx7F-3O7h374pf0mLkyGrXqux8dMUg2ptkhT9EkQ_1149CMKsjmNlQS3elxrEnjFW6hXKtsFiKNeRmCO8hAn7JDjpd-07mCsBZC3BdYyhiyPL5fcTTOzvwsFK2LSPOx7DLEiMPsRPxRs5i5nuozTE-RLfoEsMqP29dTJaE33z_rcTmOtX8fvWdZZQufUqUJhPiVfVeVx6C6rKQd0SXXGI_EhUAbaYAbhoTL4WAc_aKQxBvMO3krrJd0fqHeMSEvRFab2kiZydHKTBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 745 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 801 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 653 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 734 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD-swgGOjtHA4-BRHP3T3cEuTmJR5rV04dDSjNz2_CBKet3jIjv5Z695mqQ7vCHs7jCu-7xpJ5O48f5op-ciXdqnDIdpS40QFXd8VaO-X9wacGiJdlKfqs0IsMxrJbsZkrk5bXkadFnD7xwJV4GqDr-oIAZf-O_6zlUruJftvaHnAxaEVIsftQulo4zGzY14L5HI8qxlVQTDQ6XuU3gBuDTlXMC64Oug411N5Le220ESYxdW-M0ziVPtxkp6yYTzEe8K0tjK6xDrt-z3KUt7n-Wuf90jHP6-bOhqNk2HhKBUbfniNvL0WTWHgMpPfj-YSD5C_RBypbJwuwQ1Gy6blg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYWol45mkn7GJvvmaxMnIxjojYat8xAOpUuX7h0DUOYzmwRtvXvtsPMPfhHPybF-GEij4M7aDcD8LoM0GJX3YmhEhVxu8m1VmwRuypW7LRLvEuhggbzaL6XB7BtpsppGSToQz-4iVZeBYzVAbm7bAXT8ZM_LncLLCK_sqRzuopl1AQKoUNpBtPVvMvqqBPtb8f2-b4BhDLpfAQ1SN96MPRhOCFWnOkREXDfCva90wSFVyssTyVFFZXhTE30G9AzZ7NtaeQ6NrM_dGnq4-qWRcyLlCOqf88hIVPU1K1YOBrbTlUC1sK2fdH0FwrOZKXue5GeRvJG-LdqBMWjIA8JRKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 954 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 914 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAprEqGnH9aGtZXyJgJOaF0xmcQR35kToWaNxnW37cVLeKABN39M05-6pbGuxZXDZVNM7W9MwCGvHLeAmmuRAhO331fp1xuOEqsbHeSQNOvE_FJEEcuWYARCXqmfAEY6SqDIKSvdIKlNv5WG8QWeyMRgl_cKa_fCXEVr0v2tAotiI1FBs0wdoyh6SXnA1Z0_pCxn12zelYOWDzf0bN0C3ws7dv1lHmQ_n3oujxxinwNQipoI3DGvlvQ1YmONV_qdf6tkdkFI98r8Nf4qsZEBUHBC87mJcNsg4kNOn8T8n8oXC5AFk7hPrk_Ubq9m_MwtiTNTpUjZX6soNyvjVwe21A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTtkSEG_LdR7aB25HE98jPX0H6a9KDYsdzbtGRJOFhgIcHDyXTkSIUxmaVHB6CI1-mDRSLUYmrH1irTw-AWYZDq6tDEo7JyKJm5-7TOv6pIe0cZ_LUtnJJ2Y_LFSCqtDttK4v57JW210LEwwbmcjqpemLtRy2342wm3OpJoMBfDMjJTvf8p7iblRFVXLmUWik0viBdLBbL0hUqgboikj2AsXAYp0ffsE7gqUGIT01TKgcdGt5H8576xtfFZ-CFx3PllinpN15NFq-ZCo4NqQ8cZk12cp0EGJT7vxEQi0JjTZ66JosGS9o_5UmowovcqRwmsYAQBkN26hNsV3sAMoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppGetq9arl9ui4nDeaFeWlMPEgiS5DuHyX93t0LIz5OI7iXn52pViaJpyth_4uHl1fcPhP1Gbo3psKzVx1_kLfT2-UU1pViaU5wzvdRzM0hp9unD8w8A2A0XemFKmMhP42K90FcD_F2hhxsGpaZIIS3sFKwr_GXqTDW1F-jhP9R9HoTO7cs5uUNcUi8sxqZi1_vaeU7v2kSjdUVoPxOkzLrYYgrrUvcsOM4NYLMNsru40k_CB3lfaBA9uvFlaF7oFK5rDx-5Cf9ytgr8ykk3Gp9YHxk5mudYUwH5lxazzAquhz4XiKTqs4J_tcJQE60lQAcT4Lflm9KqTWptamzvNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvnD7mdbf2Thzk7jEfph9XjLtHtiTjjkZ48S7OggeOYUSPp1LbO-vEc0O2wV4IGTtuWDsJD-WsP9kNPpODukjnENV_wzp1_HniSNCsqsu8Nert7S1I9aceJtLaPS_u9gCgvEqriOSOM93kjf6kfHXB2PWdGRkk5wUhe4XK9iQZ0EDbLsnhqqY6JdCCpVu5gBEl1EPiHOuAFtXSujD11mjX3orhLkgvE5wmvQQsxMqD0Au27rYrDIP7PFCuExU5IQ8ihPhI1gWpKUsdCHoKf9YzrrcaCORCHHtMQWgFXDgqedn386fNM0WvAUHC2sMqq0bonnd7EirfzUMxHSozI-rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMOnICi1JlaWXYJp4wKSm-fGGmVYP000l2qF6KyMgpAOOKHJr0pAVTv5b1XcwDYnMaRCZ61x5athSxoTICpnUaWPrDOkD5rHkzqgj94bI32PkBQZmah_icIL0TOdhsB8MOOXfo7SUcLVqjEAhcO51iwEz7t7a_tKNbxfoNeHKw7fuUeBAlr66BshuxL-dtjN1k75O5YFN_PtYDFZO2ukKXidaFXbi5mOFyMTql532sF17iEtpDQzzJuPSjtqBeqXxrG4pqgpbp0jfzYVc_pWD-mYB66E7-Dod8OWO6I7Lr2ikH2ATqanTtKRg-DnZx9exJvDm_yVV1zHqGAt_xcNUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDoMx3pPSoGRViuhGxzjv5dCvEMQ5-fWuqr0GMhi4AyNBK60_6CJwhpwuz3bdQa2scWDxupLJAqHrlNf21P0Ln7ClgLtWWrSOJPHaJ2jP1l22UMbIjTKEDppUF99DbptE07cpGm2FGyaBW-I_k_gOjBAOo0a0jp1HhTs8HQbPok9vfD6bO64FGswkO1Fpww504I49DTdraEnHHvxR_dxzi4AtdUjRPO1zyHL1jhOctgHr_8QtYogA3xAS69CYmW4fIU1CCTXH13El_AGBCHKZPw2nidJ51ZoWgvkfbM0Uu7-4-bzoqfDNrTsDglgFtFusmHYWEGA2mWTj_e2duASdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pia0c-9O6mFlI4SSWBDhyX8-1uwxRw-BPLmlvlH9Q1w07NYzzNDSDS5wepZeqH_NF4muHabMS45gqhiaelgnL1SKZJOwzBaERQuKUacFhAwJMvplUuAZIlKzgh7Zt_jX3uPeHh_lCOj1zHLm7HAs3CoPDuPiCgMoGEgGD1l2TP9ev8moDETM26Qklv03qAY_5_a5QfFzJuF9vxUvXcbwMzf3mGl15Fs8AePPP21ljKWZ7zj42SwlenGmH1F6__gFaLAZt6jiK-GzQS3V5hWJhJGG1Eahcv0-TdvIhuRGps1oLrMIHNdUW9YRA_KY2kB6L2G1865xbTMYmO9sDSsKKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nadJJZmbQS0tvUaROf60JbjG739AJqWjq5Jsm-d8gYHERozOkQfDqAL6fCaY_CS1LypnsUKvSyc-_mKLyz3NZXBA1RS9zfrUjmNVWsCbXqu5dDvqAQRUOqEF58oQWJ-ArqM5oveWzvrSnea8JPxEqZsfPGaNGaaLHlnkuYthkYVakuJq3_u_hFb-X7G1VBZx5T3qW02RobBNW34kUo2NiBG1mkZNcoLuOFGHUNhRx2ho9Iv5ZSlAy7AO1mgdkhYzCgk7Le_LHNEie5axkJv0kFkVlj-xPMJ5E1GGVmm20U9cKrM0vvzjUIMVQpXg_6dRmcyWMbeznAP7eOouyuMPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ndr6kwAR0bFMlL62y9a6b3v0NGkAKYAfwiCO5DEZJkiCpiw86Cdy6KNs_b1InyX_9UClwZ846hmbnbLhSmF99uIJjyUZsqvDPqlOa76hLLsER-AWszhnsyBhetRdzp2qnVqonqnMOx6xvSPgKwRlaCE0DsVvH2AwB_DAMOiBG6Ux67PT0VLyZgeU6glfyLT_pGA_ltI9sfdkU-W2aW7mTPTRlN4ukmc0ZsA2Eab3GN4XVi2BceZppKFy_jRohyGEgKzPXE_OmNQRxbc3_e2kUfPybmBkc5cNBycXBFoy4SVLDgr9EXbnzVSPWZwCfrarMVNcDyu8kLez6WEP8nqAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJBxNGErboM4c5NYb_mbsh3jkQnS4gL4a7trjOSZHKlW8a6k5DVOHOLoGqx2L3fxMM8Zn1H5HzP8y1CFbU97TIfLGFAMTa-remxXgmJRv1VLNPa2b26vmOcg5Qakrz7Hadvua70oRPHobu9_nXlmBFh4ZlJOcB0NdyRqOYN0NLrh9lk6xrLZSm7f7xQwJPt86X7oXWM5C2Wrcs5vKxheaXK2iQBgTmX5nMcvyCuFQNAQwvsj1SuSym_Un171_JZdjP4V37t8ullq4Dfwk7OQgfmR-RI0QacL0nBn8NnmANWC-8vHVcI3eKYlGVrUrUkrY6oM13HbbLsHuizhfYlYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb0IAKEvKCcuScvCKxTMYmeTrv8UBWW8_RnPD61w1bIejODgHZA-egl86vsTG4dRXAlrjaec-IQFIoYRks7tUABKsBudP5KiqnzSgcFbkmei8NuzNCwJHxVL4jl0elPKQBKeADDYR-cW7PNiybln2ayk51FpaNtNkieXtlpUfYeFJDLvPXkn2-0DreEWKl3QiEbYv0X_le_XxeEE6O6w53orFLv8GcX4uGTY7uO_1NScb1wPjGQs0pr-WfEUTFeMgxEqllxnJ0gXe5AgWTrYuJwFKkcEPra8AplBAcCJt3YFUDGIv8thZs4TAU90Q_utFWZlFFHJ0vgb7ZrZSoCktw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zig98lgt8kw46xD9a6mqeH9zmAUecu8FfG2EOwW55rSG9lLCm28Cs9gBrgJ2DFhdRtLZdskVjQddvEpE55ZwfeTw8lpHAcapAEt1lCHWcIVH7cghiG-5JA95YyFWyMSgyuhyoRZaKW6nq5IZnqPgNq6W3qrPHURam7WlyYgt-sJlnfxAZ1M6xJFvwiOzn4faLmpPetdkVSS6PkFUhvnpmt_TPYesDWMJuSjB_7QMx_HHRsUqXRgZ_wqQPFRltBYXa8zu5qzc3a6YFz4fhfe_wd4T9wkwUKe_Ui1rWmmpUT70Cyvz44GH5eAAkoFCKO9UpI14DhTFHV7OgIP4Me1wyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=iKfLlRtetybn18FeJjrO1VV8bi8OoC3Aycnuf6JvQQv1kUvXcYynKGqQfX0_5hHHYzDmu6erTZuACUOFabvNpxgzkxofyZ46-RKLGOH3Y5JvuqOMjnDjESxRWRUjYjWoirkchTU6AwMxeAf3LFGDD4-epeCeCyGqj7HeXx8NtLLPUCbst0_IwLLyT6GfIlFsh0bR7a1svHRE9xO15h9yrJiP1zMnVvDMB8QKod3GYTaCfqgAlSRdUKmRjlHrxkWq8DVvNgehzBYrpVoHoc_UKqLS8-0qwJ-zOymqAPkyxOg1QZPvttfeVD_ZhwFnAiMe6v47r4E6M8OXDGrKJSN6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=iKfLlRtetybn18FeJjrO1VV8bi8OoC3Aycnuf6JvQQv1kUvXcYynKGqQfX0_5hHHYzDmu6erTZuACUOFabvNpxgzkxofyZ46-RKLGOH3Y5JvuqOMjnDjESxRWRUjYjWoirkchTU6AwMxeAf3LFGDD4-epeCeCyGqj7HeXx8NtLLPUCbst0_IwLLyT6GfIlFsh0bR7a1svHRE9xO15h9yrJiP1zMnVvDMB8QKod3GYTaCfqgAlSRdUKmRjlHrxkWq8DVvNgehzBYrpVoHoc_UKqLS8-0qwJ-zOymqAPkyxOg1QZPvttfeVD_ZhwFnAiMe6v47r4E6M8OXDGrKJSN6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhSvj4xHgTcI-KoxB_AVajm2DITTCti28t12CDR_Ouw-5sY8vM_GRQ1Wh8s0oyAGs_lr3MeRTbPq4liHuYAUAMJrq-twcNXvFxbAv2LNbzygOV8D4-ekZcnHGb2KpSaVpnnpy_CAbxjOrU0458qrbI8TaA-xiPfltKx_kH7FtPDcBraTE_vKo4jmIPxWBaBs1ZmoIYzyRVinMNRbA2leNwaUrZMoK37dnME0-4_IYLnBLnzQwqsKKrjf01_b5iRMTH4PfV4JBSH9CG0gyyG-wEGPb88D6qMtO9GTY3mbbut4y9c7dOAofYvjzzFf8tFEs0iqbFuSNJ-5vrgqYkHrBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6MyjWEzB1tKJMs2GlQAxf8_0FbWbQ7VGz8FNAESytyYdsHTB-ZaKDDYf98ZAXFF-wuiDluWTYI0raeg8_k2Hq0v29h4b2dSUXvBfxhUZMUKUOpI-ZuX90NvI2JVax-Xy7LsqwBDNa_800fgxBwzM1Q2bLysDuUZ39DVb7x1fi8ePyyLVVjr0dad0mHhSk_Ohq9gA_xB8umyXu9QZAxUVXX3_CfBhk01WyoKdJkcwB5GpfYgK5RVGNoq0aHXSdm_BhaT-3z9sVGz2AWX9giwmU-20aiBgrWJUwf0bn2N4MOwvTtknfU2JjqzQYFJoF_7AvyCi8OtSycnSyCqvJvFEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4NnQ91oW5J0hM7T8umuDL4VrLAOG88xPHJwuirDlV0bHErnZyVVxiWSxIA9l-oNI6H1jomuRoYwMC40eFcC1dApmtr2HfYUHo-B1mhD76qy4BQ5KGdFxphrp7pR7scN-WrU1LkP41capuLsDWI3i22Y9jeEXfzYiwbu48F22XCHyrzOsUFiXeLqWKkl4iQ5h4EE-HDv6bg24I2IVhdRfL0v4Uq4ESxrjbRLUU8uwT7R9gp1pOpwM_iWJ_CpJ8gFrnwq0FqNoBGCIX5MiaBaxt0mI_zm0BgEbiS_opBAJlCTRw_nJQaaKB9N7mDkm8o9OzcoJCtOys1kTpQ-OPPwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUuce7nYQcWOD2lAn-4ygG2eCRT6jigadP7uAQ09ZHOpbHmAn3Mggr3SVFPIeFF78uHIpw9cKVphP4MB_iSEnKCQG9LM8vAc3OYKAtKtqJHP4EGxEDDqKM6fwB2eeO5eo9wCXJwUCRYNLQFwR_OWfHaIGEHfrN15SmQs7vU-IzQRMHO-VucLfRKWF73IEjzLZUNNPkB1Bq9vZYXK-Ey43751Ltc3KVwmyHut1CcgSTSt8E-t7--46_LztnsEk_VX_G5XOCzAyC72pt9bXoFx0pUwaTPlIFhrmPrPDLHJpidarx3dP-4SE3GGGs0xJM1bergBNOuwxMMOrbwotK-3_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9C0cGpUlGNp54OaqwUi2gyEK1M6P9A6vJ05IRXL1aLZAREAYzAfJ3xlCVX6LvGPIUdsUKv8lEneBlZmxf3wxsYy201QpzkG5YdXOSE5DU8hGbOs0WhNVKSv1JIxSLb4BmjM--Kd3-arbZwd0iOpes9_m-z1qmSE9k_ld9eQVLft8lc_l1CykS9Uf8L9c9wX6TLqyM6abJH0HqqqLbQeeitqZmNTeqrJOuu31RtVHJiuSllcZ3VfDEpcFuFxh773aDaUQIw6JlfH_b0B-V9Z6UK9dehUZTbWyenpmHFKVqziLx9kmKhOXdwm1q8qNdTQMR9GdbVG5oLnkZ7KMNaHCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 927 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSPcRWdIW1S9K40d1wx1gyNgPSJEt2rbqcCJK-DwFF17bM8-53KL9YxDkXO7U0brp7dBDjeVNBLcSXTzQr8MsheWRJfuvuwpB-QqQQSB-DJg4WXhkc-ckoY3rwyjnaqBvYwrp3tPN09Ei5gkrt5ALC6NyIduQwJa4D3uwfxdFDx2QiUEdVZefwLUQfvxlagycUQWjTI8gj1585FyK20m_xIpi_PBcfN3XtEfTdzBp9psuowD4Btxih1w9EvAXDm2i3ggyIBArXBNSnFL8UqW3DRWWtfI8t4wJwfjcqc7x98btLdLhs5M2QWb1CjKjXpLfezx_9QXTcCWizt5Fpquag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 748 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtA7Qi2N0Kxbh8eviNlV273D9wlj0LDZDLKLyGURTYnnMZcM9Ki4EZa71IKAfHwOhossE8rI6rDLZJzqhc2cVAKCyzKpod0rLvX0XXNDbDGHAg1IwQaCdHMAR54bdh9q18j-4pHFs7zGTINzZsnXm-h3BDxcOqsm5akt2HJac3dZy41XETLtRVghyMdsIWJM2xgxfkxikHDEP5Vw1GMUW4ZK9CMAmrsglWVqr-E70iESxxZEBM-xbvUhqr9zmnbUaZ1HxaLBoUHGv3ZgS2q7cYxgaY6dB3X8hw2S3YBqXyaQ6pIfRJ-7m_cKqxDh7_WFyUAA_5XufgMfWbTLdi43Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KO23LC7PTQ0pX1GMiMlsstGdo2aO9CMNwn-MWNSknFNJXbJ5HzSW8GHq_BPzXLDI8rIg7rJkZ1j63hQlJ1GQI-lO05ca67ZQtGArMRMqDKZBL5Iabo4AdVYWFqecnfQhFRqocAYUmQBioy3D4S9MrjboACF9uSIIV51OdHv-hww5o0UpVnZ7_-yenZ4rZGWXGNjuAVBHRYCTQmfr3ygV4xRQdVMpUJPCNB0XZReIIGBilhQPQf8eMslGU_KM53dgAoXlk4KQmU3qoMyHbKaigBWYr5kpScwbsnrO-7Cbjb_9UoDPey71UBeMexxcwuf_jyIa9WUwL_rOL-IySonXLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4uatE7A2U0-O_Vpq4QF6QncsT06PAWx3r3PzsI-LXZUSng5QdExZki_oxQCtMbRyWe5iTREhtmtN6bjQWHFkNsandvVGBXihDl7iTJfwKaJ6_Zb8bAoz-U1b4SlLPOH2yDtRemQVgdRRv4D5gAIyfhxczxL3MmvpAGVKYEOH4zeVKRdJZch2_wioSejZ1X-p9G63WZO5F0PRWM6EiBAvB5tGJIodyf4AH-4I8wK5asxvtLbzZPkO806IyYUbetRdRTnWby8d56yMsYCwcC5gv6x9GvdZp_zUvv3oaO7rRbiWQxETIMggSYObNEVNXjskM27Z5HXtEf7hJlX6buaIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0XzgZWUEQNmBpr_mjenI4dB0qqOhbITuGfR9J1_5jap4gfIftJve23yptan2KvVkRisSc2TGUdhvycaA4lmTN3zL9QOYtcSEyZY2TCQBg8cvLaM3EL6kQhpwxqMm8i6gtgMdY__mzTFTmA4ThxfD1g78ijkJ3CCcZWodNXVZYAjoBoiwBKFQ14MfbKbAeLv6bRMMN-h4HMSc523-oay4bsB4vWCHt1I-TPEIA0O5MWakqMcircqQtfCEmVKEDR4rau2f6SZG17_2V3oS4Vb6m0MiH-ETK15MZtxjy8-SZdr4M-4gfpC2ltpYTqLO5W21uH-5skQgi0bohCG1SvnVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPfghv_yUFgUwgu0TigrRkMkfWFEM1OQ5dasi83yjCoaJ8D0CJ6iXbpEMtRUykDVpxWUQ9DoC0ByzJP6QMWbE10_Qe5GMB2vr8y3OC8CX8nSTjDjc_KVjNT7R_1t5iEQQPp478q9PDGipphLCuOw_4Ac4jYw136M7_WJ3YCB4tp97a-_6TVcJGglfvON_OyRoPGTIlBLlRANRQLJFSSgkVu_t_bd2bsFlzF0_mJ1WerhwF_w65JYjuT7a-Biq9dTDhsSBpc_d0SjrBYDbHPelR3-XHDSTGuADJxVVFzKeYUgTO-84Bu9PrwAOJP5XGu2M_Ts2uX6KsE4DBt-UDPGlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHD29JszmBTOIUEH3nmAh7qouTAIL_gdA4eV1AfsNNgMiYg022ljysm0Pk_vAwyqNNSw2PnNtsBjBxwF9dXJqFw3GwLiziBaiJhxS7gysomdN8QZVTiVNWjE3mWXaKWPajRJQixDCwfeY3Rmw5pRzte1Jf-wDJw2SFvuVTx6iRJHnUFA58emtbD6Vnnpq1KtQQAiEBdMqKCjwxOV9inN9BAIMlEiImVn_v_O_py3Ux2pRMvxaaAdidofX7uzfMrE6RyKKi3xR4l6Y1pTa9KmiRtLQ_TPnF5bJOzB5PNU9o-9aZ-wN32j0KFRJ9p5Ou4o_l9KCrsqcUlEcAbyljKz4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubNhBeBzNsvuX0RXY4-ZaFEIgfJLVAdEkk6JmeDi91aBg95TiVrl4DzjEaSqOzYRHyWzRG68rX6lrWkuCb4rVkzwIGTEVTLaDPdnxrSGfhxIvY8llk42US0_MMI-5SimKB-EWgYabANq-l9dGAkUdEWPcpwZ9E_kf7rRMer9uRISW1ZBkufMOOULxUedMb3NkEwx_Qpn42SmGpttEKjN26R02CrkmU23-ebe70QntYeegLxJRnHAyczRry-nsv9t5-cVtN8s2ES94MyfOOhVWiqSGG0X8KChZwmb9fIAaP1DXGnZk9fzOMZNwNzhcQZkviQAFFXC9onDgVosg9Z66A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_T0XlOtiLhhxsjdedtumlpgAM-Os36pJ8QnwluRrBzbEIItDVEM7RXuLvMuj8Xup0T5cw_eNAsMBZ3cmQbtpgdVnUdA21gA38GgD_zJrlFvJoj090JF5ZGGCRBxKvtmDpoFiLLxz-F5YckkocoVrHcVjQWzDRpC2pliGBFPqeUliz9Crvk31GBmaf6Ey3rbT73EN9m0ifqqCOkKxl-WRyoU7l8X8Jkc1K24LPEhOMh7WDuNhhyqF2cXKXGoxM6CwzSybv7CRK1indfPIhUbAh0Wzwd-GsbNoo6RokK3XUryHuR2WhMp6yERJs1FK864KDjKG8_LkqTlrHN7RVUWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlDjlHZeo8j7rjukx4ARfDCtypmRlT85CTGTe0ZBnNZYPyvTc1ak9TS8HyIroRcF5dTgwv7QCoaSUwDtMyNDIkUXoL8Sb64ErRXP6g7qLAPptPerO0a7iH-DZ6Gr-u4kvPT_Mo44mqi2OBpik_3ronr_3poC-7D81fYc8oi6tSGRRkkFilTT5_QfJYzS6DFA9P-ruCw6HLrYFg9QTXptZSBF8vNYn2WrlhC0hFwWIumis4_YYD5gkJ-JZxT3Cy5V8JSfeX6X594WABr8MU0jV1-B3WvEgsYSRz0kDSFYN9yIb7Yb_Mq9iJMAXKxZ0r6Cgj9NfVCRFm53_RKAU0_0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ko9iqFBjRSuxlV-CyCxuLLonVcidJS2C6l9Mv_9GDmcJANH_6TBFuR_4W_T8QTRucPM3YL0hC8Sky7RWXNUQ-ZLK-JiCk0Cg2OsZ6U_EbsFu3iLk84wXfHre5FYuze6rp1EE8AkNOev85KEAAdoMpYecqwxH7C3UCzjZV-0-0LMKQkM2cp0EhCm7LDl_UqLqEM19GZgiJTIJhANrGGubW20Rx72PoPFo-C52nGWIWsAeWp_laH39K2qrA0LDAr2wICdVXzX7u1V9qBYuyearsx2vEEFiAaKJIWsxUtuSzY7E1skCWRNdG5lUpPwiQCGgDy-YjOz4s1WO0mIGeMfXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cscf23bX7qo4JTWR51pXK5Crx-KjfN3o1oZvuWNyI4ma3l3nSoieLu5Q2PVZ-cihW5zlTuBewCzRzdHuJ9hIZVhAfo4VD76S6fa-VmVLeY0bCgl8bQ9qOU_okAZJMzJEZa7E4cw7oPcnnZne5Bgyo-bngDwFRGD0GlTYUFQL1SCw_DiPBhdqDaEGLlJYtnN9ypjAgbGRp_xCo1Z3w6xPf9to-zgJWh50X-UuAtXgzb9c7RE3vV8d_uAuWVRhK1D8qIMZKqv4BptOei-vIuCrqBzWqsTUpB2_9-F_6WrFSl79jn1TKdq0tTrtcoFj9MRWgW9NVndTxWrtdNII-zCc7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p58QWUGMy46UcViarCBMiiDo8uKCu3aAjA2NJ9Eu8F0vL78zT6qKwynyDARu2pEt2qcdh4sHFTr0K-RJJIxRGb7xqpuid900xOh2pQYO1qidTvrkyLfVoyC1_D_Z_G2LdTDQq1KBc3Y3wZt6us-44JO2G68L831aIcrez_8OnBe6Jlcd_OTipSNCdfshZrTLLMb_wAD_gp4ytVJlMz9TI6pkr7RbARqhp3pwHUOqK_Buitwd0cuixi0VGh8Lx1w8zrnvraCCvUVmWkmLglzhtWZ_gmWVzULExgzJKqnPBqd0qK7xO2V-6YbTMLdngcgIbjyT2xxSvDNmYor9t-I1ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fagN2iF23QN8bU5RXXoEiAcFJuUiC_n8JoFzjvvCFfatVd2CzhrIz8dYd9mxQbD1kYtnYAd6JZQNbEi4qK8mAc-sYWt6OOnTEf61nLvF6Tg7hcHqJpUfMOLGfyxEFid5mlukOxX_sDLQjPPqz8V2TTMQLI6JTKEcX8Kv4jP9l3mjxrpWLtGrKBpcJzLmPmcxszrzmJ_B92foe6zauf9P3jCSPd4AybUYqb59Q_y0fVCHN2sZKgyX-bKvn5QskpwSNg-aadufJ157AiVHBRMIpiGbEj6ax2vS5DRKyUnLB1WubFqgbxL7IBCBHpZm1Ju_sLI_OZBQvjWvpgpDzkWMcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOoHqS8TfbZzq1T14YNlbSvM85v3lqNn4Y00sWGcSSiBJRsBNoUhR92UmrlrzLPj_gXgtW3C6773bQdI7i0BqYnIqGj855Nep54xkI-YBb98PyXGPUpZ1n_i8xAJOGGoomGF4z3BNP--NkP0t_7xyY5xx5W_3Uag0X057ybRERGtBP5MHKoQj59y03kXvKgItZUss91pSWUXwCPaR4AoLvYKp34WoZgGZgzW4AVf3mpTnwdgOruACfw314quQuaoMhNz9Yf_ChaMsS3SJKXKcZh8GWktmim_YfHp3Arp0iTv8nrjJwNFTU5cyMZxpvN-_kkCPU0Vmr6r-d02Vg-X3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBKgzpYqINFeeRFPa7F52jq7RjHCDCzBYKsIjKzw1RyGVhyZL4sT6RBVyIrCpnu9_zanqMIt2kh5bwpj46K7cQ6Nk5Qj95vhNn28fnvva_2AUdCtSiiHhLFcW7IE4MDJ_deaeXKPuMi1Op9D4E7n56HZp1t5ALWF8ioGHa-tEmDx7BZarrB7IS-gwcC9ZfR5YCtE9Tt2J2mnGVV4QkiJ-objI31MvK5SWfl4THgwXj1uqWiZSoujK-qhBQpVr3EnE-A1Nwap93NjmNXy8x3ylo-asqXA9ytVwHcQiuhfBXApULOwLbrtpoD_z41YdQraxerYiq_YIm6WaIiyhWHRmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaPLajFPxixYWYkZWaIfkjmEeFXGjaathwbVTR217EgE9hdpn7EfVMPvW9ZtJS4rxY7c08J3WIw-bNUiJBxqI8RPrkDygkbTazNc8w72ylQBuG0xKJxxogVE2NRRCpt3vLbni1ve3wfvDJjL6ZM9ivaXIABrGfhSH1IixEX0ipGdNH-SYXhlwD6D4fN3LprfWaS5g4gpk8hpFUk9N_wcXk_YBDK3C0q1w6ss0ACjsqB65uYCFx6dPEccEj26QXuoIdLARvpe-3c_douiBmZAl6mb5ECKN5tNhkKv8Ms4gjfCwn1K7xk4t4qXKe9I4y7eIFohMrvALHMifrbcMLmOEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU7Ru2jQ55fBEthSmDHP7VC_isl_poKmi2fBy4sQlTjPrYGd6A0en5YDAtHZFVL0JwUDkrOuvKdhS02BYQtMuX0Yjea7uclHpeyOAziU-lm3zDC7ddhFUOzKaWA7VpQGbzc3ZkT5MezvIiBPaAdg2MsAh_cxJg-pH1FZ5qg6d9ffW5NezM-fU9C70zXMhrUY2c5ogYoHX8uAjawG1V2DIyvhfOCZixEsoxwYlJbDoEe778iyG0Bj6GLtSmINEKIf5S9JXebSzPK8QceN2xd7KOAwsSyPm0O1FwP_tTIoWs8DuEiw3asZTJFIgb7V30ItrX2hXu-QJV9T1NSMvyzcgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdfIe5NpYZ0SjU0on-WNQZwn7WOEuvokmTKMFwzdeg04OdqJk_KIj19J3NXeawfTDPfcCbtoJGPDgjysXCeKKNf5Tbrof2RdzBxU5nNikIuc1hDt19T1fMDKnsIbYBGA4wrNtJXU0WjstTaH-VElCBH1aIWdrfxKfW30ED5Qp1xJNcwLemM1RKXhwPdv51t4jqWtUyY-uinzisdNs_O98Y7AODyj7z6_c_-RRBV7_lvE9V3S2Z8xUvUiZBntL7iG4qI_py715I2V9NOSl0qjX5fqHPXGAnbz3dTZ3T2sHFtCpjwKP-hi_Bh0sp1ZZuPvh6p6M7jaRICvc6Ju6K4-Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Df4KvuunPaFOjB_wo5GoB0BceEyPhLxP_broZTT_Fzh2g_vSRLUMxSxagcevzMllxKeKE0wR6VlII_i5-NWvnGxJJKMfDJLN1ihoHthA-Q2cleLHcw1bCxYUv6-zceahOK3G5XDHTtbzOqUZRyAowXDe5UjbFPTczGYOnFvt_hpTuo1Wy51K9Ct0TdbAq6lRuwzwZNg5BMLR8zo_md0pR4En9tRLCST0kidqEXAqPVYQeT6215-Ax1GIBZCKfvecva0h4OWht1dMyjc6pOoYU_RebZkzgu0CBQBjJMTFmm6E7IAmFa76bhHZWoYoPVmU_qkZ6BG8nvZ-KAQ8wWwiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1f9nJ44Oue-DZQz-etRMhuNPYcdFPAsh12zd9qL6_bybiaS5goIriNWZXfXZW6J6__3zskDAAxTzNO0xP_DrJXE3oRN5nOZbzf3yIytI7jZG6S-4lbcthFvjl1sQbNTbkMmB1AuEBFb0RiapmgTCi15Abw-bnjMS72ZdxzKT1SsQKTpwaL4czGBiKAcrmsOehb9F8Ni6TEJMunbVyXrqJvgivpQo0LGIjAACI4zcNTWYYdpT72og6SpwpFSWI9CtwOIJC46yzalm2xTTDfxvCG4DENvHjVlPPrFW9zL4mDZlhyIThcUgdMR_OuCmt5q2aSIwGiIwAjC1tQ0y91CMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmM2Nv8s-HS5uEZT3NSNXuijqkaOG9EFrmDlKDDdlMIiexqpJJxmoFGw1oFlDGLqzFSzxWnu7B1TsJ1g_1W8hUG2BOI17qiapogzXQwOdBv0k72hRC01aPKN2ejdhdvoUmHe8mqnToXPqdeLAcdvSgh-zrd3uemnX2kqjCywG0-IipGPfVPDvgKPXhfN_X2kOvFUu4-WTOkZZ8XPm1CjUhHO76Uz2G3wwbQRBhSf8-RfgIcaD6eAy7h3ntFs3s7tLvfpEs0fmk430QxvgDIu4XBedo40n6Qol2IPNMIsD0fpT7rkyO1tC52Duf8No1rkXfntGJIJg_lTTyCXW1uz1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE5yqQrLMKrvriEathzPWRFyGTBy-ytQqtzTYP0QA-OpqNad6YnLQ5MtYb3K8rlQvHgD28tBEdoPoE1-aUy83K0fThqlw7MCldTVJ2L6urMjFHY3dzUPN5muB89P0bi8AXXFHqrGmRql_H8soHq-sL_3CGi8dLRJskUHdq2fuuLTyeugd4HSZ4QPmElPc17soSgU_74KusG-S4Os1hS96cCIqxDdBwgpHhM4gNgbn6b_uzlt0qqmc40uAIO4NdWfxCZ-9BkTH1PMHnA9gkUC2hTpCDZbESz4EzjX554-FEAf-dHEbPE3E16r0IBYfO2B83xLWF831isEwe_n9_OhOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-rZr42gAFlK-s-K4JDQIt6KUhEVl7oTr4qOMPxq3KWEoJb1oRVn7uCsk2I1zq8oC-LeU-tj6T0ksf3akv7L3f_to-Qdh8UKZVeNBwNtKLCteoVsfc6F9L3XvqHRNWF4DDa7MBZt4B5mMzGqFO-Zr8kEX6pUBpg9JyBQbsTxaT33EnpEeQdzTwdKF_Zo_NCSfrqtdPuQeXW11ooKnnw9_oI6qQeLDBBDq7oU1mzhZF8juhH3XopX-RY1yJf4QO0HZ0ZhfleWII45B0r4rX-JS1OsJZTIsajfTvxRmva0Eq3wKR5kVLVHtCqCvzpFbAqLk-k-Q_ndV97bKpR-9m12LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvWRovu79RkRkcYYX5IORGtKvXwqFK0bdfrAC7iETCW0TQ5zrSXGEW5wk02n31oh_EWdSt64By3YcIPDKJl1Ejb5vX6USe-gEouEMgl7uHtxrklcKGTZocoOWeVTokRtnRwl-MktCCeyKYT-Dg0qXX48wCxGDrZNYYnYsCyrRPJh_irZb4sMoxcfKZ15pFLkWSW3GTkFUN2PupMIxIedzI0I1wviSy4W5JYn114AU2CGV0ax2C5jLD46A2rPjRPOQWT5jm2R4PoGW1xnXse_Kv1DuXBVKdr1y5WWxFurJd6ZUqgLsNg3Gp1GQCmDsPNYwW9muqC7iWwe7ziAaxKuqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1UdfyDYSASzT9al08JG8wb1k7hX_hSr6uVCL64ZsIMpPc-rROuA0SGYaHE_U5epCoiPpADniYUibz2jeSQOKu2SykQWGF4nBN01ZvGEJc7nEtDgmIyRdgwLdRu0jQRUmlhWbXKBr245ZuuRCImJVdKr2EmWkdB6Blw0XBq3SVaFpBtf_0MCpsRPgWs4CD4QNI9y55deUpm6zpKlMXxOLIrIP4sz91iALBPO9igyT-sUBm6Ywe3l1SKRO5lI9W_yqqYh9FLUsRDT7EK4tTwA4A9sAtfbcIEY4G4yAQV5f9BP5Q6vnn6j5SwmRcT3gBLdP4W18E0y7-vfmGLSzVyLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdm_zhgEb0IHK1pCC_6Sz43ymBHJqlZSImjLvWNil7vvDc3AbSQJlibqeaKLvGXRw4QIZvGx61gjknp7nnWeA12J7RXJgYPoKlRDuKdCJ1sHBrPxf6VPxdawOUFjqHPgNOzr01fAMDWytDlmXUbPJ7mA2Zw0iQcQ99ES6A9s8kRRmhxL_toGEsSCRH0AiKGcI43RRqFP_5Bz1oQnYIk0sntJ4-Ios-J4kuu1t95l3FobzYr7qvCxcQ5Za7ZOX4tn8mi6-UIaE4e1orO9taMgVKEhL1OEuojhGgDzmGZVMGNlD6uKazELNVISduJt85TvIDxRHs3PhoVKqr0yNSR7wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JY5I5dX8GH_hz6x51LiSVprDNlkIxu7aLQITo71grjSK2lBQInjYQ09H_QCs3yNj2VC6uCZxr1CWmR4n4Gbm0J_lX311LUsBw51nGEZkAAAclOjZbBLrircGQiqlhUojArxgHYzqInglbLbhOksflvvEK9GOX3YVLCEVatLrLQcSAG-ks6UynenpchaMzsMPJodFQJyUuomoqSSiwLMLOJbzDqYI2pLCnAgkoOYa4T8wbd3PqRqDBCqPWJQnyTkdqDSm6UJChY2wT9GOSP-8ePlwaRcpQA-Wuu5TtP4Ht0XTO62iEMFf7OE2Yuvf0LMC9bWp6J6FEW9ctZUGVVoloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvNqt2o8NgHLnUJwd5d9UVWk1UDuOkGsy-IGoB-fmDYPh2aHDtVgvQb81BHFKLj4F5m6kYjX1itxD4L_hS_ogHMolQ12TQQ14vHsgOvAAkLBqDq07Wk9U0nC7jjElTbsqpcUwUYwKQ5cljKTOj2dJIL7_Ix7KowBkKFcK7Rwg-KcbtI5-naynId6Yf1GuA_yqySB6U_O5dxPDmBMGZNlv90b8vxNuSSnedibjnKq8LuM64-P8ldjTC4zVJdZ9mkSvc15eeqiVNQsk-PNAaFKWvxFj8RjCxHcmLEozTBQqxA07GE1VJxKXCDi4cNWC4_yove6E5Hd1DBjHsaew6RCIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL3BV4xGL1CPRAvEdvMHuPGPRKXjnNY02up_L-kR0Alb7L79pvP0UD9RplRhNNgdWXasYlfEgNF3VH8wd4OOObHXLZB-vH4-vWu7Hu8mmuuFzR7KFZNIBInrkaqlS8DXXmCa5cvmBkHajJ-UOKHzq-QfO9CnyciLG4gysfaWk1ECBjhUUu-X_4A4Y8GMeE2O1v8K5rhJTmh747uR2IbZB7VVslCS8YAvcnAbfH3N_eY_LgJhr3N-8T01AxX1YmPXP38ftdpEJmo9S6Dk0RMIf9Qjz0BG97YgM1yiiJNwy5TaD464ZU52iQdnBGP8oKnOWZOLP3CWI24d6jvFOOo76w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 587 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
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
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBj-Nlhvd8YCnE3GWwg4c3TC8NfX7xqfGv8oq5cHaS2SPgRyB8iUyvu6b5tLqQig_ZbBdGGg3jZCh7NWWWXczXSWU3eqUP9LtcOkNVZroQi7GtJRzmxfgzFdg-AjFZrhCY7cnkOHRMXl85ma5l9mYQeRdDTRvfVc3_SLx81h19k18RHouRzS2NWQI1snSvpWCkVJM16dp4IHjGXZqB-XmKdUzBlAf0rFxonGZ7GWKclpKjqQd2pCAza4poupxy4PLLPd34ndnqQaZDeoNGkfjiD7FrNKncMMRW4mCKoOMlvtUaOqxXb1Y052905vL15CbLvCIHXsL5OLOvhrxgh1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZrymHyIy5sLSY-gfqTNydOIJXOpnRFYDVs2C1cZjPvkdHk-T0xam9ZCxjKxfE6GIbNjCdj68d8-GDFIyhPxSOxK5636GrqXw777ni4dZxq3xiGULCi4zoDd3fVWyypXgv-IS49hndKBOVF0eYvngF-EnR3i4htBryttdi4YHqEVvLR7SU0mCVa4d9Vu1HA0nBtJigco9yKxxf4NMm4hLI_PlQI1MbgJltrjEYvnHVPysi0iNB8naqbZ6mwmeu09083gIOZEJdEX2f43EuzQeZEdBKqi6AtrTz2vUpOjsOWkNoZIAUBp_NQMC-tSdOD2Mf-QlzmiJTTwbpjR6aFInw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRdsDsylsi-zz2DNMZ1_-aJFEbY3Da_5HKof31RC7Gbt9_8uA4JHhayk5EiFA4nuVXZI4sS-ig1DZ6ctplIU4QeuBwD9VnhwBUXeDnKyQ8GPxhaQLnL9aJ8nL4DD_EhZOYJBNAMW8HsXlFAWCbSJ2m9JPFNylzM5YBtDBAaocngDYYVcBqX66WN1l0ezt6Cd3EuoWnxzYP0YRRXEYVk92hrdDYh6RBOPZdfbkDsl2gV1vxlTxsWmNtyGJY3tFDc9unFQD7_a7xFRdjnio2jv7lZPFX2vGNjuwa9GLE0q6YofvAP2ndoNTze8xgk7n7EepgEGF9DP_zVxX7kdBhEuuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwxhNUa1XkkYApwvC7vExUk19FT0UzEjQSKuw-zKXKkNhvqzY3vSO66fhQnCeGYseStK7yvOW8urkxOBszSfOUjtXRA136VzDX2rqKDkXZuo5dzT3REu0-PP20c0tQwTSXpZZUwZJ6OkInR4aAoCPIxsdlOiC3W2voJqw3FNtqnuEu5ZnlzGxgkA39W2s5cmP_LPUJvaMFVYdxITjk1rbhvKPzFByrt0RQf4P2ZATr_NPOEOj1Au7dGp2z83I8-WsOsNYkXOVjs0DICG1igCEnxJfyQMrM93Jc6jld_7oMJ4Xxfcr0qWUAQeYmVWBy7rNMlCY3A0luxa487VPk8_Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9N9_cowhf_NnHiE6V5KxMtiA0TeQi6oakCaKqGFHnybIm9wl79wX9sGVFHk4LhqQ5nxxPqu9CD9tE9RGY_qXYp_JfJpA83FoROFyQawKfGS-u2HS7oTVkDUN410N6Jo3cx4m4YeKYd0ea5yXLLzIS74j9RBfJeM9jRuyZLE7oDulXsV1eCSBx_AUWL_oDr2yXa76wQqqBfLwTjAyVcqFIyxlE_lFDRszbgXgz8elnetG9N5tp7DVDcReZFVcGvk8BAt_BaXVi4iwxEtQtTxPy9faF9s3vsxfjVoV54K9BHISbaCo62_onlCBwPoq--2tF0FsT_QOibCJmOu4R30BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 771 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTziB7ne0GGkTSOxk4VibC7v5pwCokivUpzL7JffMeVk9m2oY2HmJ9kxungOoVJjhNzxKQNlD1ReYeORFpQ1FEG8IKPqFIHg8PntKzh2UAqvP5br6uTN7dZUPuQWRDPFA0xPW4TrAaLWq5duFak3VOQigpcJ9mHatojPlkwLRwvzEX6sKDQA_D4pG4jaf8rSZMoT20KJDAR3MJKFEIKww7zlGimEc6sLzrVEOXLFev4J4IxKRLWsK_Sy4Q912yk1CgKXohtRZKR0f47lRUuIO8DYrBLlATsKXAN23_Png7uG5nhUtbyJK8Fkzk7VMCkcthYHqbJbN7zpnrCwXqfqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-IQWEyZ9W4LaWguSfMBcSMzBDd6pmGuSN82AqpARi-hLl9LIP108HDWyNFFTCy8zkk_8MmGpwC5xMn9qJciFoRlQ8ntkUuJI1fSX0bG1y_FxSSe5am4imNCi9-tly269GyoHlT_h8KFARh9UuTUD0_Erhb63IVn6IR0zS4aLKd6KpZM8kXJGclEq-yoGMhuk9Ph6-QaEsj1q_Z33gnZdf2Uyb_AvxKGojd4SWOuh1uDyQMDbnHQU_0C5An2vJnDZLJDxgGH-PrrJRi4k5RlGIRN2pRhYT5DwC-ftYpcrlZdbgHvTzq7F7zbh-azxvssWJT_wIv0EPGWkzkYwRrCzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtcQYokgMTM69qd6_ZmVLIrBNDojYrn0LNIBuR9suNA12W4UlfdeU0v_R9PcHyA0agmvJxsEEiNN7tCKFTBVQazSzoaQML_jcFsDEcrEjtGr5Nk4GiMQY5l4QgM6U75vUXvfx0biwN1lhXQxcCBN5wjcEvXzlpGo5lOU7o7oP_geobSkRRQvqopezZ3L_w2o6tuVYI0ASIqZWxHNuO1CzlyQ3zc3tnzwJ0d93XVTG6pC0yvz2mwrqqMjck8P-Q2B9O7zwXU9oUs5oLAiXfB8yxBPClPdw3PfgEx4hgbqKmPfKq1GbYjwFUeQH4VehAM0bJ-QyvTg2mwOGffPE0LfMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhFk73X7zdLtR37_Zw5UlIHzV1xDF1mKfeIADHeMVq_X0uvDP6k0yGfhK01Y4MnjDkRVxNxrjr0FQ80aufwtw2DKawhnlJUT7iWoidC71Kdy_GT7uYXlFNs6m2xRO6uBRIEgN5LcPInikZsHO3TPlRnMbv0Ai__g_LrCPmkTQ6-Oppz2ROg73cGj6ZImxX4tSsLbRGaNKuefuC5CPn3z1hPMbqRw8DhazZOCte9zGdjAM8R8cUZGDWgjksaMi8KGIaq3cRxOCCc3gR3h9AgvUY-vrKL2uAtFpfI4sxb1rEMhLdM8MBAdLyXx2dkzpiu-2GHMUlVV7LzW-dLYkHrvXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foR9NXL2LpxEIYypJ64TPtuePFj6SDeG9XKS-dhrEYLwxpBgZlgKDhdxSXpZ-D6uOpu2EOGv6IBvprZmdK4VCxGn6kRSFM1jhdT1eu9rghgJpsx7VX3xdQZX938VyQUgByB93-iRn1U1B8AHEv4akWEso9y2vOtRexEaHkKxOmEQrhxlcKsSmnS1ZtYyVB1258RCbiIRDQ89jELTOG9VHjW0qxNZneHv0Ra2gnHPXPS7IFpwiGOq0zvwYI_Qmpifort_xkKPhAVpyPxRayEFTTVCnOgEq0HpdfBCj0g_vK1sg2IH26kmkSWkHF0mrWw0kt0QLxKYxNLj4otm43abPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-8yXvg7XvTSz6GmynLmdYHiCVifPb0390Jm0oD2S51H1L6ZgolhOdQC3A_V7yrPI6KFCfn4wHz8defycAaAhc9D3sulZRfJbw2VUUWsBJJJlJ5Bn3zZXZZDfwYB6nGsHsTQaGVCz3z6GOk0kM9231VT4XRqate2TzxWDzL3MuARzyuUaEE-692uZUcrraIQgUGcGxY-m__CM2A2ZZ6MfQ-GAmB4spN2C_ks42IHhqlQ5NhtH3nmQWJvYjGXqLl1wt-lMJ8JmPAhJ1j-9ST6K2VS1Ahg_lfjRu9CBzObWjN5DumzfIUyjzVRfem1UFL0_vXW6rhiuLFUuZxHGOTjBg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=BZd4NtUOV_toSSWTzjTDLWblR1Wmyxh2OMlDPb96jwftzGeEJvonOItz5DktIpvWVvit3cYu_bMXTEPQ8FDC_16licNGJCoRqeeL6sShFJHm7nBLr9sreoehK8O7igQm5j9GIBqAtfYM3aT0phGzhbJrp4JuwiOVz2LpCEMO1qasV-VRaMXwr8MBs9LNUHRr-vw01r-8cXgZhncj-d8HCk5r62EblmqAKLnZG8pG08sQB6pegDQE7S7KxsK5sAjqAHsNFMLFvm6HChH9XgBEXnQ1Al2xUjF7QZ8UB1ugh-SeVj0vGBIkMtLVrmFbp1kJHu9EpwuhdZtTG5W3UdJBIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=BZd4NtUOV_toSSWTzjTDLWblR1Wmyxh2OMlDPb96jwftzGeEJvonOItz5DktIpvWVvit3cYu_bMXTEPQ8FDC_16licNGJCoRqeeL6sShFJHm7nBLr9sreoehK8O7igQm5j9GIBqAtfYM3aT0phGzhbJrp4JuwiOVz2LpCEMO1qasV-VRaMXwr8MBs9LNUHRr-vw01r-8cXgZhncj-d8HCk5r62EblmqAKLnZG8pG08sQB6pegDQE7S7KxsK5sAjqAHsNFMLFvm6HChH9XgBEXnQ1Al2xUjF7QZ8UB1ugh-SeVj0vGBIkMtLVrmFbp1kJHu9EpwuhdZtTG5W3UdJBIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOn9-EGWx8yyI1X4bZHlLNUJkYBMXKK6x2ylKx1-zxG6KwWae90XrD5_Y3fXV56ptxL2FzoaSBatWTUl8vwkf206r-GngJf_w-VXKUfZKFwN2WxUOx3HRHyqn2A3n2nTTNg5FWIU0iTowHvdt2WuVEsW3DfG3-ZVyGKzefi7wb8q7znSilTFLVggM94deFw-PLIXif8SxDVMePT7e6mq5Y-Z4qvF4QBfmGYGNKhTURas1OBIi_76T1f8KN3vMXecgx4AecSdK67UdzQcWaUCoHGsixS7yt-h-rkmKsUymFMHp-lOkG3Aisqr1-TK8TJNj3rpurOlX_gO10_lWA6ZdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smTEtIu5qQkPXiAthLlJdZomEw3ucUt6V5tT-aU4mfaTGWz-Bu5V0LCiomjJNf1QE42vTmt0nLXAq6SqumTecEl652pu421vqUGCX5w2Mh3MhYZ1NGGBVpm3CRg5ysv97Gb2RFZcpiP1w8yr4xJq-07viz60ZjM_E0abXmQ9Fzx8DQfjqHutmRTSi3KSCW2A_H_lyF1aL8dN1FXTKt3H_pebUGUL4Rz4YEdG_ZTxQa3BK5JbUqlsja5lyexMg2j5roLhI-44yID-gfUYxWgpCj_iM8FVTgUyCKyHu083Q3LM_Dawy9V7KharMksM7293WXUX3HA4fGNvCBrdx4RsWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAXmWpIjjVthktEM4HusEddA3ZqmsB-W2kEPMiJWtyyaWO61vXYl8l8Lo76XDanQL98-4mhdDmT9toVf9_-Frv7XSOLzI7IZNLge_zz6kqylriA1XW0miN7PfdPcdEhLexNjBSGcDlsUd3kVZ_iPDsMJGLVj4a6wSHNadGj4Z_apu31K79DhA88QJfqgnRFtQAJ1TYFV8qKRZlBhUyXyhg2OWGL46iqrIvPOdv05vpImDl5rcGN3j5ZVQiPmj8SPPiZDaQ_oqG-mgo_OSNYHi_7OsyNX_wxZYRHqbobWU3RMGyySXKruBhopBX5y7htpmY8XmqWhRr1XR9VXMDCB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enLs2a3OfN-LVydvP-OM5sabE5GPkABFcw5NbrqdnuQRhvzB9ozBjKMSvXwA5DVMgBOvm29HgwunIho4hqjqhCwkFS5hWkavO087qMeNl-MZs6xR0B0PMQ3eee5q_s9Tz--ekLngZmxEXPz3eb_sdbMVprbTtrIbw9JcxGCgdnntQnYzlI5AagKfIRqVNgJ1aZtEU1CKhh3NVIC2TMcabmNlP8JGiOEybVg_ojbF1sOHEYH6Bpe8xCsTPs3ycR1yNrKqZaIDW-YrNODxCPg8n8LvMjDXf7URGkKQ4MSsCFuREptYsn-XDz5E1UBUa0_WWsmWq7jZqqXOPSZVKP1s0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1jKGlSovATrWHVRX_ya9LRPuTEe5j7TORMrv5kkGUb_n9Sc7I4E-79DDGRzw_E7A_fjQ0dmGMez6iBYKtM0ytlgElmFRuxukbEqqshnyusM_MZ0R2piIh8FjNFXttLORKAtVTf9OHOVQ-4LqJ8pFkBr2l-KbHGSkG1OdMqShb3UZxWQEPxp5Rzmn52P11EwqY4WMD5ulWJwJsnPljc56Vy2T5R1_MUpaiWB8Xxrs3ml1Dg7kGd8vjFMbJZUyn_qMasKpRJ99euWPZsKNWsvooYKFiHIAbA_icILSbHyV6BbepypKsBjNFhNDnb1m_w0hYGbdPuRp-l4vrc0M1BG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDNZmwZq4bx61nn7pWm_uK7MLxY586oXt5Dc9zWvKkMJb0Lb0jIWfa3bjj4dz-AWrpIGm8YEO6crrXmscW6-fM0nRYYDoPUeupfkORQqX75U0ZeQkNkQ5wMoifzGdh2wtd8TqRM92dZmH0U4oqDng3nFpr6TzqxNGKd5doSVOA7LEvv4sATYpiHVVW8Jg01NhbOa0e6ovMphATdrdxqsn4BEPAArp3yOmBLNkHN8OWxtOOYCoc34QpWwavLY6ohW4RMSu1oMIW_CRR_FkrplsrmY59meWNRGYYN06u3yabL7KG2mcj6spntA_RnF5Y_EMgpldifJkaXd7gM-DrfT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxK9PT7IbTKhNV2qSQL8-5e6DIKHUIdSlX_HhsHOQIWUJqT9LhC7LiQXKDGW_lUl1prmc378jLQVPW5g4AY2-9z5JMpY34wY0VF4WQCtIbZUsAHJ3SKUcUh6kbh-hx1yCAgJxSTUeW3K2-GD4Rt56ZaTkT0W4fH74aiW5RdLKKaVMZNCqGRcwgkjNDd4SyQToKuDVZ8LipwRCZWr77uC-uAwzQT-keBPtdqipxS1IfV75kBbPlcjfloYeOurFk598bIvWwRp6oatVZdmt7MRRQzPybpT15bXyWxSzDLVgHgovnZloWEiYWMkPXRS7NVsURExYcakrArADkk7W9Sa0g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=SShWh-5mb2Kh7cRzmjL92NVioGTEEJfrL_7a6qLd5ih2qySosPmERQzX8Ig9DAGSQCTWSKHiihVMLu_MTimKhtoInYjQNo0tyIczrHP93cNhHdzABhh9Fag4VB6lJRd8HGpBrtrwflSdSMVAnFHASeVkFJhXBrrbZR6yA_TPXsRyLVumcA87PArYtwXERBZ1CaSf6ehIO5MwJHK8UTfL6qTQiNyw1JO0ZDpJwOsFMX7QaYDa2N2pAG3MonSZIDC-IIFO3GOUdAMNx908WpHIQ0RfnoXMLdqFQgNGwaDrdkjPlt_UJexcgTJxgbEyG2anNqNBCIW0Oc88qB2ehFRjfzTTBofVwYWUzyvT3We7j_3D4MfCcuvcIR1WEK1UgIiorjcFN1ZUzY3parZ79Mxz-EZgdn2urJKn8PkwLYes_2nzBX70nBnIyaZUn5ocSWJHyE_APZ9Ut4s7IjvYtEzTSMr7gw3DYVUGgSLJXYHSUB5GAtNJ0PZumNsm3NpMfP8QfG8gZKvLtvf6DQGUJUN-YT5gajbKonQIpQssb7z2QEXklrpmqTCh8APCenTKY_KrfG8dzI-yiHUh7Jvf97fewI-fVQtzZQShcI7AyQF-OHvadtMNHwgigwK83rVZ4lA88L9LAnBifVVLXBNdUQTtiufuqDzLerVgk2VzhI5IYdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=SShWh-5mb2Kh7cRzmjL92NVioGTEEJfrL_7a6qLd5ih2qySosPmERQzX8Ig9DAGSQCTWSKHiihVMLu_MTimKhtoInYjQNo0tyIczrHP93cNhHdzABhh9Fag4VB6lJRd8HGpBrtrwflSdSMVAnFHASeVkFJhXBrrbZR6yA_TPXsRyLVumcA87PArYtwXERBZ1CaSf6ehIO5MwJHK8UTfL6qTQiNyw1JO0ZDpJwOsFMX7QaYDa2N2pAG3MonSZIDC-IIFO3GOUdAMNx908WpHIQ0RfnoXMLdqFQgNGwaDrdkjPlt_UJexcgTJxgbEyG2anNqNBCIW0Oc88qB2ehFRjfzTTBofVwYWUzyvT3We7j_3D4MfCcuvcIR1WEK1UgIiorjcFN1ZUzY3parZ79Mxz-EZgdn2urJKn8PkwLYes_2nzBX70nBnIyaZUn5ocSWJHyE_APZ9Ut4s7IjvYtEzTSMr7gw3DYVUGgSLJXYHSUB5GAtNJ0PZumNsm3NpMfP8QfG8gZKvLtvf6DQGUJUN-YT5gajbKonQIpQssb7z2QEXklrpmqTCh8APCenTKY_KrfG8dzI-yiHUh7Jvf97fewI-fVQtzZQShcI7AyQF-OHvadtMNHwgigwK83rVZ4lA88L9LAnBifVVLXBNdUQTtiufuqDzLerVgk2VzhI5IYdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxGGnQLmM4qritz0DoDLnFy6tYX9pQbInrKCDgYdDXqKLbEaWRWKBTalvLd-9mTmx5DV2BProR9SvR3XphDjzmTBBZj5xgopDJ1gwKeRgFJLetnE-wyZL3ud9DhPd26XU_H_josU-NhH2uoqaR1Uv7B4KjnkWj8SdOWETZ1EBQ5a4Kj2qvh6xIA8-x8vFI4ERpU7fyu4xTlqJ2Q6iIz69tgu5i8EO0-frZnEib_OtKcTv9GumxYnTFgNEPMEqYI90Eb4rAD6Q0Q2flBcbs0Haja-ZIGp5fIStcf9hmt4gzRcAyy-ngUclKJ9VOdXysEmJMAKhd4UudmlYqmd73aS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prVXE0Q1INAh5p1tVZKi2rvJwYjahSyc4MCloFmZ4HvTjhMDlc6ZT8X0j1SAd8L-JiRjerxliRSxVm4mFpKcW5jYQxTJ-f6_juyiywPS5UTx5qJBX02PPt5d6sy1K0vR7cTwaD-x8MJrQF3rJG4q0pWVDKiqXD86N7Qt5hJdWgKqnOgB20vOQyDGXBtOLreNsDFdKEW1SWBw0X1J6kaNsnOFVvTaqzS59XDhSQY3OQ01IUwWu7-tyyB7__uOy7UVoTuLYcS48DZjDmCumledo2_qrQDY2WijJoEtbgTBS5YniyKOk3NcJXUckXhhcE36WrdrMNFGdjVkjzuz4VqWTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtPYYxK6kbAtp71ODO_j8uqz1B-S4Ia_RqOIzGs6G9WEjgSErC95DEUl0oBkKdp5PCcubyUWmJD49Vy01Z-L5J90Z7T4vo9xWMPaSc4HsfMChx4VP3iAbFD52c119C3Ar6FmN_SJNKFufTrYzRT2dF7GyOFqLZNJOcf7aVcEC1wnQI8Anw2UxwS-eVsnehXrBowl9rvxXWpf4yODBrD2a2G1dkBSpPdkJ0wDu4JcnDoXwlHcgLxtrdUWahzxXPcuw98xpeS04PRWLwadd9sSAz_cQADYp1Q2_Ey03Vx9uPWIVrGXYbNWDsgk0k5Nj2c4se8_jEDMDO_Iki_PxW4r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O03br5ciitIAM26jKom5S8DO74zftLNyY8eX8ztrVOBAuFwK15TDTPOkmrO2eq3rX9QyXWX-gEZhOwPOFwURpnl64Udoms2SgH3oMwYFYb-Lg3E3ZbiwuFwhr9LziRmd6s_4gQKkQOZejHl0YVJIDRJEoLW6kMSX9uLUBnJDjLfejs0qCBqG_FW5Bm5-DO1Tf_2wH6QIisAq8hKiEp_ZFGxMIehKL7TXFP4ZZ9RiY2WWPkYN_HGBjg5K-tiXVuUzuHkdRZ6eNFbP4TkHsAB-5dTMsB2_Gohr-UXl5RxPBmb8hphb6hmsxfL3iwHKLdULRLN_5yjrS5ZF1Ic5e6LAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mn0PFpCx-XqRv09hPDKVkG6oijX29fkPFIbhLLOsoXg2_KtOpD36RCOSKnM7YpwTHbZtTwU7aUQ32PLlcix4CSGFzcybW4WDUz2w0N_VF0xx6L9zqp6gmPFrt3BgggCdjohOyWy4bLhxxuxfTFR7y8UV0FevSb2MhsxyvH1iOR3WcH2tFx7FL06yRyXs4c0BSzrDro2uWkuZHCsOK81f4scixG2EEPqRWeLx-MCDaBW3oAnbeyyjP8OMXAlEUPKt2qQR8zaYF4dWnMTIoXeuQTxmlEN_dsbwxRP05OjJk8oPX0DF8wewkBXX4N9t4caG8iea9F-OTVF47CcsD9ET6A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7mwSTvWq6mqHKj0Nv3XCAy7wzyItCh1wqKwazmNzFOWvpvhpawpYDO85xxess739TTETCcHPiNb3Eh8BsrpPyQOX9qNTmHBQZ49i_m2mKMibskek-OJ4VSnv02_B8B9JmHKcNdyzN42xpZ5dr7YmjPWW1IYH_caG1gGTNFhMXZlLai3RhhgHuz2s05pd2T7XuboEg6iI8YaY4ErpFWng771WNyLVkW33UFJX3-cNDuPvanCrPzHqNrwVUPky9rPqZ7wEpWTV6nJjcXQvRKnWxjf1Em3Gt65xTE8fT_bgLG_g-pGUH5-wsjS6h_I85kD_Qe1_tPthRIK37GVPRoeavfdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7mwSTvWq6mqHKj0Nv3XCAy7wzyItCh1wqKwazmNzFOWvpvhpawpYDO85xxess739TTETCcHPiNb3Eh8BsrpPyQOX9qNTmHBQZ49i_m2mKMibskek-OJ4VSnv02_B8B9JmHKcNdyzN42xpZ5dr7YmjPWW1IYH_caG1gGTNFhMXZlLai3RhhgHuz2s05pd2T7XuboEg6iI8YaY4ErpFWng771WNyLVkW33UFJX3-cNDuPvanCrPzHqNrwVUPky9rPqZ7wEpWTV6nJjcXQvRKnWxjf1Em3Gt65xTE8fT_bgLG_g-pGUH5-wsjS6h_I85kD_Qe1_tPthRIK37GVPRoeavfdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6StKU4gSmryhwMN_qzjxs8ui0n_JIOsyz0C5D90AIZI32IyKvRU78zr5gLdrzSbgprqq4iDMYXBODUryov25rciiwNxOuypeBA3s9rmR7UXLkcV1Y0g3Bpq_B2-gTOfrU-XCFDzU-IfIWaDFbkQLy3KMvQlKXxPD7FscasOzVgsR7CkSNxsW0eu9XMaJmsFSjqxp1iapVIdkXh-G94zopT0j5QkDxGV1xQFoVOJ3zx-a2Qc40Ln85UFCEFrE3i8V6L7BUPMHIvCSDceNnhCb5Q5P7bS3PuWT3KBStmvfeH5CXMIEvdoMqboTHUsOx3n0-J8n75w_KuzUYCVUQQ6iQ.jpg" alt="photo" loading="lazy"/></div>
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
