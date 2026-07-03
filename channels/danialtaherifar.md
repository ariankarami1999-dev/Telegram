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
<img src="https://cdn4.telesco.pe/file/CbzMCmJjDOCNaSePphkJ6U9S-cUs3MFBNxJzuLzYKmnlL5X-c5DgfvzJy9KBYQnH8gqsyu6mKSd0QdOSQ-zfm27lf9ZosICPQ9SEManGfst1ft_D7yOKzTCbVt3fqCBynC8LQiYJEQ5DbAWGbfPw9Yxcq8GwgZ_zhYABpWhDpjAAzipbPy8-cmxYJIHT5mwYjqAb2gCdhx0LXMquFwh5ZUSCCCZIQLmiyE9w08ppRGQrqYfWfaRweyI5CPS8Hj4Z0lgLYtLUUMq5eQcDTafGFgZenuRb2YrEieWl3OFDr6kYvY1braPpUoQIdNJ_8RxXxfRCAPQ2pvviRsbqXzro4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 265 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP9aOn1physZNsINVAVigTg86GlFnPguKG-sgcH317VRxuqlbPUaXks6xXmyAwxB4z649ylwm6ftkSqD0zXGBvqGsKCnCDpGEruWcu81e9khGwPOAqZHUq3Yv7Lke9fthYW_ncaxyXnEU5LgspTmqiULMP8by8BEvqKNL_HKhhh--j53gv9T0bd6W_T1GCH6pFME3isSY2Q2omraW24LZPTQ4J1-vhXK87BoHWuNYTKuD1PL-5ZqJmFpWU6jizUoWwCC3l_qVeYRtyqPLod9QetJ-GV9lbfnn8CNkER_jMQD8G4XDJIj53cx9Tdcnzy3A5voj1-gWjQxDtnwwhoc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 497 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 745 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dl1ol_AS6PftJbc0s1oqPAS7YH50b4f9wNdF-KqptblylKfdRZx1muz3MZZyvDscJYBe1Te-Rd1ZTk3XrwJCVmLS7ymAUohKVrrmkX1IEqWrYCS9qc_xHUI9QFZTGJdeA8apilR_WySrGIp1Lmq_yaN8RffOtCSmUmC-UDmv04JJFqVODgGbfXDlxiiRQXRGShxoQ6lpWf6L7IWaqtJlS_ulmfXKUyX0c5ibfem4ERvwhXrL0vjGsQ_YB-sMzsCEJUYr8TsDn81Sbef4xo-tK5Q-ulgacLPxiPYq2LYtwVjRL0IX8uwry3h3YTVrhfkjNh3TKREjNigqQTla0dbUDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dl1ol_AS6PftJbc0s1oqPAS7YH50b4f9wNdF-KqptblylKfdRZx1muz3MZZyvDscJYBe1Te-Rd1ZTk3XrwJCVmLS7ymAUohKVrrmkX1IEqWrYCS9qc_xHUI9QFZTGJdeA8apilR_WySrGIp1Lmq_yaN8RffOtCSmUmC-UDmv04JJFqVODgGbfXDlxiiRQXRGShxoQ6lpWf6L7IWaqtJlS_ulmfXKUyX0c5ibfem4ERvwhXrL0vjGsQ_YB-sMzsCEJUYr8TsDn81Sbef4xo-tK5Q-ulgacLPxiPYq2LYtwVjRL0IX8uwry3h3YTVrhfkjNh3TKREjNigqQTla0dbUDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 760 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0qLMtsPs9KnnFjNUNVr2gKyT2eufvBPD8VzbgvC4vVg6HvNpxfRhniASggqqVJdBdHAMm7KpZF_w7vy3yPK7ghnisPsp-zFglo_etzLpLKSyjMlEBSxlII0FsCWBAE1QG23eCWr3Gvgx7Dt5CiqhoZNowSF6tti_SGaZw3Z7EvwNJBQV15hXkWYUdsKm8MtGRLkp2Z6BdgAgWm25klrpOHENz3HYPjuzlv5nmUM1bHta2rZ6RufhSleMULoPwuzlZQRKqGEMrZYQXXL-G2v1YjbC2teLhpdp88BC-f2-febeAZNWjyOPiMIbPTpzFOdICvgXm8AL7ELU1fKfSqXlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 627 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPMGE-UQLm4ARk9P2-AArSmvC-izFJOz2Ikq9DyV0o28o76RSewu4O9Xf3rWwEq-tfNN6TIYx_v6XFr4GBOH1WhRRCenhUatrJWy1a3SfHaTmSRsQDj1h0U-KpThVqr46NaNJGdaEgtzwJhWTiMGk307MSG1So20eFNVSPrx-8fEncJxl45lyIDBCs0pZpnUFFTRhS5SGDu9fcA2vmS2VfdpwBp7u_tUFeEM7XnobvBbsVsUOE7B_AcKT70tCyfqAYwfqpq7uD6JjSEfTMVIEnI9IpCgHoBFTVXK6Jz9hD4B5dNPYkEWdrGAWn4ZfwQOMip6u-eBUAyM6I_6Q7F1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgk_AYLAWUf7zWtywOl28VcVbpht5J4EwK7RmW8iESM_C8sS4bDW5z2I1lE5YSinS-v9gY3Ns7M-vcPXrvRsH3ThqRFHFhnXQ2Z0UIZO8bsPbS6_3EFjTMmvOjt22pBEBHaFnrM4uXRqczmfeWgXy_j3Z3hdbhguI7sWOH6NYd4IRFsjQ4kC_vSUw-opYQ40lpSm7SvwhBde90oR9Tzi5MBAHbn2Ax-4qseCyrMTAEqC0l-2lLRt4QhOu-niPKACF_wC8ZCHxC4kIKQCjYF_co2IZP-CbiUwdtGfvc-YImD_pS-ddwdI-UnN3P0d2XO_IiI0r8-o8f3TsQXrw_k0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjVIb4yBFs_ilFfD_WOI-ABC1HtL3puWr652GU2qbqkSIPUF-F0KH3W0q62K3eoLwB8S9DYr3RoSvu8102g3vUytX2sLVFHyy1vXjjtk7S-F0k_K-8O8HiNHIKgbgii07hPOt8a8R7ifm2WSAp31537jtaGhLf-2X50tP5-EJVYjUh6ylxB2aulBQ3cZ7hxjRp0KbC8gSYmBl9ocLhLA67_CCMiR1PHFa83pl1-ETKdhqlIJtZw-QuHtSiIwA4LifvcLTKUPpB2d7IEwj0-By8aoVNHerwjDexXbOoCwA8VJKOGe8smG4NmVdwLVLs21zqM8I4-Rj58-fRs414xHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqzdzV52WOcJN51VtGO-qEe_y3_EptiZJkqM_1XV-nlw93evg3Ufyzcx8LRGat24Qp_agS6orRb_JCHoFsVj9y5F19P9WFLwvumzq8rEYNtMTObgS9yBJgzzKX2aOH_jrYpzRjtF6yy0alTvIylZe6JNfkY7nDFZLih5FAiAmDI54MBRK9-P-3LaU0hw0tlHMQlhsQYihzB0JsfXibZFGtbUIyWR4-z6raBoHPqArOBQ4AnQMTomIwKJsWvwoPRYGQb2kjkwpOSotXvsRpWhoT7Rfj0rS3dYlMzNge_INA2wjIvHzf07cusos6f74nFk0HbEUTByjAez7ijS7jM2HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPA4QRMCyTi_VIZYkJMH1fSqf7oW1C7Q0SvJcT16LmucSKsR0_4cr4lQXz9caARzHGcAw81mzYzY_v_VRASxP4GTUoTl-HUix-WX21HLyf8_xEubfc9BIMk-ZeEJd7jXIm9TQvZRFXXdmhq4okmlLvN2tXZG5d6CsqUUZ6vnEIwtXRNBJyk-IS87o1UqV_05jdZzO4U3KiIBjtn3Q9Bx_plLJh8XnXiKw3rIQjl9qYys_PSDTwInzjiuON8w4cBRDTl9PMYKCZW8yI5fLuJukdInR58iv_vJ16NR2yeg_gCG_Dclp5Y5CdWxm13G5kj8NeP-mR1pIybLInvO4p1oXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 909 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKvt2K0CK9-pdSMNNArfeQBKz-TSck2VKjI3NLZlM6tQc93sTiVgVWHeW-mo6lfiIanswOgG4OuAj_rjGh20tcBYtmCdp-KrXjEObOMSNKtiaIslTtcHYE4lBq5Ur74NXSv1lqrGohTEf7NJzBVOMJMdK5GgU3fkIXVDgGuclKcAeiAwAmlA10A5MCeun41b_Yq9vvITa5pFaPn2hDlq0Sak4l35bIl1ISr65QK7mr2Pudq1sin5eukJ_pR1LiBXyMmZrtL2qp8SfjOjAc_oig9MuXmbn1Owdbp03IfpAvS-MyLHG1H22MlA8X4SI-RZ9M618g1BxYUVgwmgM4VsAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khswD5k0wCvVAmSNTVhYTdl7cowDIjGs7V9ass5ZWmFK2oMJYW1MBajDKVlETXFpecjqcFc-XZvdkkfriNX3IkLO0aFjyhCjdKaP10ho-efYpbGErHSQMQ0AdxGQ37cOSo6sE3lsCKq0l69GMTdBsuaP60OqfwCDmzSZsSUO1qKyLdMStDaguXmzqX9gRXCUSfKS1rS3LzsS1C10vTIhKpVvc6x9M_KFW8W90dCSuZxrNASaDhvNHjN7KndXlxQqjTTJnSOCpxbk4VmVfG7KUPBUa3u_ZoCpr_k03GgjigP9H3OlSQBAJfdc4nAXdq9omEIr83TqTIycsHWHiHMggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMaRBpjxjqziXbhrXfdYaCHA_jprmjbWvBonS2yQzSKsbdsYojRPeTKZpYsyeQc8StrFpsyed1hXB_1Og9FIhTK4sRYkLIAwssmQQwvENHswuhunfoKLlHAjk378jy9AGJznrtLvvEgOURiEXgAc7COtW3ETt7dt-bEsC354ZFyCR2XXhncg8ocWY__qTj1wjgV--6FWz9QziTRsUc4MCPpvcTKD0JNlYS2Kn4pWywQqYfSnd_kmCGnovHGYKjCEirxSkspaxmrkbrnyxGX-bKG3RnTf6oshCXzGpTJ9eWeZr70hiBNpek6ASC4nTNuayeid79n2fLVo2ZMn9bXovw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWumXoNwuhvNU9yh69bGqqjj_Mujgj71XN7iPTLERMGq1AWEsONXzCRSTsK8o2AMj_1cRtx26BabvlPJnUTto-mYBHJS83O0b8WtqZwME1YQdez6Dq1Qd6463kVsDbk20SCY0VAGWErcWJS1v6agtVNeguLXpu3IcROsSvfABp-7zAIv5p9i_C7iwGRtjgur974KvfuT9XZcJlIKG9QztKTL3aeD61h5BAdyXzflHMA9MXckCk4OIFwU2FKHL_kETtWE1AFkF6QseEGed6IWekRiwONz3qlI9T03FyjZJACKON_VaV3zoktrH_aAFWFh9sKnXjNKwQar9DK1LZoXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 961 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZjCYOAfHk7vQn26dBAfhGz7IO-4WAwOnDuqGuoInjikvF9U4LSNVACiuKzM544bRTrxQ9hShuAElUuJ5wOvbHSKcH0D1CoMhLdkCOhWrFvkyWfZE-05l3A4txYYynB07GzABZV6k055k3W_1Dbuo2QU6I3bt_NLwJ4kH9CSqEAwD_Ozb5Fh4Do9_JVsq-3RIn2Gco7jiYvxMzqBHre5u0Du1vBFtxnrizl7HLzBVhAgT75Rkw_E5yBza6hdOPUYAYTyczpGdqYwUyraNeqqP4wCKzUhxOSY0xoQxDpCh6c2doYYP2E-CpgdW9DNuDhVrmOzlVdRZULj0kyhJ5hd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdoroiMD3aB44hs9LAA6_XZs4K5SruNgvTVl1e0E9nHQa2QAshwtsWucD0aAa5VW27HoyRDH4bj-MnrYOqaGS8SFkIYLTFOnQPNBGb6xSQSbS_VrNcRTFW7aw_9coKZKk6s-2WIQ8PORw7rMJr4QBmrPlfgax-Ep-46bsE63zUdRRZcLXFP-LBpeOlKkjHo3KrTOEgNz2KM_zxGNdHHTv1IQGp3Nw4Fxdb1TTRAy9BvlubdP3DDN6ypCxOKTrcmjpyJHRjsTJetrALN-BOMGbiOic5cpfy50lIvaR6qcBbNv5hFLcSjUKuw5dlpovVzr5p46jLQuZJyG1BIAtKWBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 689 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id7TRwR7Q2KQ78hoGWVEIpfgS5VovDQpfvPu5tG7t5E-Jnr3QCtCk1P_WSEsEED50r7DNrMufg6g991_U7gZRFI3Y4o5oDdz2Lt8grpAb5PwwbpeQrr2sLBLRsZ65zAmt_JuoZTe95wIN5TGH8Ru9ip0YV8u3NwKPzLC_VeHDX0dNlDtyOSbUpJFGS0bi5OZNU_tgfu5RNfMsqGm0H9ZrvvJLe5PnTKFKXDU1oGLTeqtAXJ_chZ0JPPjz9NdA65SG0NvarH3_UOXLCzAkt2LWQf7CiKoqj1hR8Snx9QrisLx5FGNaV5ghZTP_F2oKPOVDYlq2txNA3RUidGpWJ9wgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmYpHGxM7TtJNebJGqp-fkfJaBqGBxantNOteXMP5zuMlPZdVr6K2a8OgtduqB9g9iYE9uyPGaIN_9Q27auJ3b_VcaqCtGTTVo-iikBGFuwV_yF1uhFOyVsiz5kGJT_Va4FT2E3c4-9masBGiwivjKBWxACGBaHFEmQCD0TSfyFRlU1B5Pnm0qH42WojmihaegsnkEQSVJilvMQbhjPsyPnaO-Dck_tZuUT10rccnFn5W6eMunaM_3gEYzws44tsX3XRdTervnt5ecU4vyzjCrO1W6SooDfPVxPf7KicBnfJuopPSdKfJwLpeWdlhCSx_MXFeI5vPBMXrkOyWQ1wjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/By2CPECgjX5AdyJniLGvxtg8ryrPBBcqPT7NNISsGTa3O-U8IQrKgn46fCoxj6jGvTDa-MmN655B8yynEwFYcWzFJNyay_hkknX_LkHSckV6wGNZNVti-kyrW_OW_E-9hiYa5qS4XPOjBa3IQqnpYPmY0QrSyhoXzrMyBKvdU_RcQe2yocn0JzaqZ12sU-J88IeGGNWM4WMvM-wRiJjZvMdXbvjvmgKuYFeya91uvWywgmVtpQwxuHCdBkJAFPw3BW3lqH-L96K9fo5H3D-GzLSCXsBKUHEXQqx1nxsgYcb4VA0EP7kRjB5UwKzCTF9w2TG75WpMKZASnV-H_Uvs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKcjyA3IxMC4SQ3MipkEpmLzkx-ffsTJ7esLg6PlWXwH9U-XnsuR2MzJw02JIHy9sInjLN6Rv-ZEcqNLGjUfHKlllowEYJdDBMGlg1_XGrAGaLwPWShB7fFEWpJf_hMVQChtbY2DTyT2WGXHXK0ZeHkWnPUN0DHuAszjZx11jsHnLRftcaBKH5xQUgaWG_hPWvl7Ax6owjCyI0P5Slo4IiRRmqHFssa1_aAM72UnYhqyrNjNZy57r6p8wGzkvwVRsJ3U5L3guM5ssn2Gxw39RbmX35AQQRBvFdXc0Cq7msrIDsHIeynHAeG0klg3ycxELTsVySeUF0dhSxb5nYitog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXjoQHMmOJQ11byoXKNGqWViShXPEQvDpl1Oy5A25RZHBgyrMkG-S-M7M2nHtI7-Ol7zPyqCv-eqKA0HvWHrzJlHkxdrd832iaR9wRSjh9Bq2qtu20OJ5O_0i-9xHPregCgWL4RD9jrBTMgnX8KGiP-UuEFyxQbLS2m_OsH5Cx2xcjd1990aNDtpch8hQ2aegKzNGOU9oEw3M6ez5l3pH41LfoLiiqOjymrqRQsJ_6n2SN7uQlWATFD2Knd1M1M_QIO7aw8mVY4dfmW9w2jCBX-mKAkTKOLyeujhiGzTM1HZKI80PnKXnWTopF-5FQfaEw2l_BWPI6t0ZRL9-eXrBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STLJQFDHH4P2WW16sxHKxYRl_HMFxAi7mx84zpVD5jH4BAT_N2Qz6G9r2KzLpsAyPT4UOY_mlGLCVYAfH7weJoYIIgNQzAC1PHV20D8JbI6fU2FhAcsJNY-xxii9vBdPYLB0G6CGdqLzXXAZ_1cKypZTs0PqCoE3X_gdNU06wAs27VAjU8nTnZcdxDfAI_Uv0SH6OYY908B_veJBEr6MZgs-JgaMUxDvNXCrmPrmP0zgIKs6HiNcb79fRDid1jYocrYmottv3-9LWBIoU42YoTbskQCv-SYLdID7gLnK8-YgI9foXzEmNxYiXIHp6_fg9DQds9kkj8CIXQAjpi32Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=DMmp-JajDgULFrSvxu0pWXsg7mSaxu2tPEqn1mLY5SjmhY7flgC3ThKdRaYkOmYp_dU5YtFzd5NvL1REMyj29hN9m5wAQxO_EGGI9S7RfJlDlrQCT0ahMo3dK_AXqWuNtPfxK2GqRJ_OGmdiu_G6uqC0hPMFMhipOxG8IXGJq_Jc-01JbS0gmjyWPJaBd7b36Bumi1-teOB2ddZ1OkCjF_ZHSE5AE2nl3O7itULQQYOQfw8syDlB5_Ekcz-QAv4DdUrEHpskb___IZLY0dZDwlZSJ85oQbeOpFd_V1sAO0FWppAo4EkJGiK6yyUCGC3LvkM8yu-St1-xBZ3JLErmRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=DMmp-JajDgULFrSvxu0pWXsg7mSaxu2tPEqn1mLY5SjmhY7flgC3ThKdRaYkOmYp_dU5YtFzd5NvL1REMyj29hN9m5wAQxO_EGGI9S7RfJlDlrQCT0ahMo3dK_AXqWuNtPfxK2GqRJ_OGmdiu_G6uqC0hPMFMhipOxG8IXGJq_Jc-01JbS0gmjyWPJaBd7b36Bumi1-teOB2ddZ1OkCjF_ZHSE5AE2nl3O7itULQQYOQfw8syDlB5_Ekcz-QAv4DdUrEHpskb___IZLY0dZDwlZSJ85oQbeOpFd_V1sAO0FWppAo4EkJGiK6yyUCGC3LvkM8yu-St1-xBZ3JLErmRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6ko8you_Ijtrenzpui5olOUkCNRwL9p_WRqYr3by2VIRJTt06ltN-kGMzGhYSjkdCDwStWl2tGNujlOENsZgHzuUjo7CCU9aeaGO-_xclZOQp29niom7FUcYRmHLmiQK7r9hBUHliYsoZOZk7AIvHEKDWI9AqNH6sQD8esv6axli2wKXhIs4qNi-R1kC4g_Pbf8Jy01vuJBYfYlN6M5oi1TuecA55m-9JBceDispbD0G6Is2bA7HsrErDlCTxsoJ0FLU8Tnee3MgzGsDW8vLkjlIBUrR52_Tur4tUCPQ7ktJPrgjCQ7UK5rv5qCkQUQfmW9zir4-HHscbs1WAykEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_xIsRyXW0wjY-cX_8Qh6QpYWWRiA0Dsf-uFqdBlCjgdaU0QODK4UZ8z9kYpcnU_WDIUtZ_-GbQdkseBKZEnUH8Z59wfichOi0Fz6s2zWO_qRhvJ-AXbqCF8cYU6yMM6pMNAJwDYnJ2cYCCQcEqtVoCTwGSz91DfY8hX3wxQSG-O6hfkFHH6jZEyaTfZpRK2ZjIUOd2aTBrlRIgh42JqUZIEXLlOfEJQzzzupEMoayN5srxinBosueUOmIp106TwiO0AlBXDXktp0iUbxLX8bMrZZA6jdSB5R2jsn28HqXo9XhHxATLaKIdthJIh-UUEAu8yTr0-68DT38jz0eO1Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vP3gd62zjQ7Rur42LU5hWHmI64ZlCWl1JZvrc9aUMUe8b4lp2xJAsiS00y-fK7_n8c7AYIokM8CX5LizfNQglBQ_97C5Rb2eAu9VnSsBSaUHTK7OGcH_vT_bcNTyoaj1NGL8KTFx5d6Mcb96B2140g9NpPAIgxlJq92E_7Xoo6rIIXfHNTZcQu3X6m3Spcy2WLGpOruoPcJeFBQnFapE1KxiyZKADu0iLve1n32bayinBGbelSboi5noMc0E7aFUfUyGGH2JiW6-KH5nbssH60v8MocZqprMBiSWrGLVqiSwaeTEV_M0FKq2jV7Rh8xDPIeOJNKCCOdOqbL6dO9ZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwdXXnXaRHiAayHmvb6trcUhWpJHlCV77OhJIlo0nZu1Af_aup4k7gySfMKEHvIhyAXnIvDzSj5nL9I6A2YAkom1irdJnJ0fbUAZd6ZYei5jicjVVMyNo9KZt3mIvsGI69FKmz1PDrSWrz_qQr5WWMOj_W7MvSRI02fMb66UcJBj4_OXJanxsqKMHsC1mJR1KZTYqVUvPlgNFovuYMC6FbA5cC5BTRne9uN6sL_QSpIVKIF4Rqi5qhj9JaKFeUQD84fd4NZ0PLyh880k86QZTPIk4JNyZBB5ShQ-Ec6C5zfFtaR_Uu0dX1MjOTh1qHGpeakSb1ZIltzUyL9JIjD2GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
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
<div class="tg-footer">👁️ 991 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKTLwQmG9B5wifyRHLG7ZjHbu8D7F1Sxk75Cw29SIP78PsPqNuRp7wvD3yKvagwqqfm9vEfWj2VeK95abjeMS1e87Z4QmpErl4GlJCc7dobX98DT4DLex4WVK-eBIftaKmFJySEqxa_mU4qHN9T_QvG_YCm-f59URTOi0p6cF_eDZmZIYYJzoZDp6AlCX2BtiSfcJYDMhVF7ZW0NSKHjHSN4h0jzaxt8RooPTqaqRF6Q94jKVUQcS7q7D6KC1a5H59RPhSc1rzSI0-2o1jjUjWGorRtaDJUBZ9WoskOysqxZI4AidQJjd_-7G2OcrF0fhq39h2ZhH0AXk4KK9_WgfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7k18ZKtd7qXYdhiG0zTHATc8yEDyPd9YLEaqAOOvB0F6T0mZhuPodZW5zXVtVOgArNZsynuINgjW50kykKv7sV4SHxLQOI7spUQzcnN7U_kgXOxoGp9n7sDfpCU0ykk5Al91N17LsHAot_nMzvyxkOUF8Ixjg2bSkiOOf97a0OvX8Fa7P7xzeHbzvZ9CnuQQUZZYQXswCY9jukCoQEyFahXR2cj74STUUMbCboz8ZyB9G1hQi57pg5JvkjQKFbGLSmhd0M8qxCyIfLg4gm_L3e7XNPOEFiy94hBHHQfuWlMsJsVuESDBXQA9TNsngHF7QRWlAAtwJ7dghUysvei3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkZ9kZ2VJ7cMcbccDpsNwnWqv-SnyjL-Di2aXqZ8Gv6KbAy1NtfvUqatOPr7epcQwQsY5r__NVUloLALJFJq2cC6-e_TQmGhQUoNQCAvYkwVHV18x_tGh1fin2MvtiYq0DvKiBAB2mqsGgZ77tjYW_nMooLRNRV1yOX62Vov2Op1_Pia9vKCacWFWfQmfbRqASo-JkIUXddRI5YP3XPm96pOJ3sOjy9oXhpcyqGTCIFks58qEM2ujXA44Y8mnjOesW2KlQnwMGIVdZ72DNoAXh3JOxPShV0nGidl701X_3DeZJwRuHWIYJQ-w-8CXFrEdukGVjr5HUlZZeXooJo8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbHjtPgd_5ym-wqJHARAaYbaj0s0IsX7-IeOVcq-BnLv6yjoprwyL08orKPIhRIU0yBfBFaUrOJdsY9XS45AsV566zrBG-RoLj5uY_Y3qJ1adbWiRUEyB02yQciq-rZcmQCqGCIW8_gg6keOsvfVjBn5FiE9P-dFjltZ4-Cs312oFM6ofv57DM4ZeEaGpuOCLlafc8SWM1OVXLHG8h979AyEOr0ZRQ14sv20wNnPpOfEuH3BVF-oIyqqihHbf4K1sHrjBXOUd1GhFZNihqbjnDp-CmUi1tK1jQlSYEuw_9IR3_OarjUvqRciGQcN9MDbDNAFWxkbBwwLLjwCctB_uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMUEsCtooUKJYrCBB5oKIy3mLXo8-Ci7TKpD3fYzl7d6M6UAghbBGb1fOk79TmTxNFF4a4MuxzuXVL9aLzm6erFIEns1n0IB5Vi3XU0_lpaI9RkhMH62jDd4u3jT9GyQYenL75tbf7rllyyLuBZjoYKSHOI2gaN3glH5yKAGehyEx6E8Xvq2Zi0XvcbVEGAU5JBKR509lwaIjxhHk62hcwUHakB3iEkDNILBUlOHVDKmA5YA2CkOtejm7vxwRBEGeP_AjFJoYm4ixsybKAAzriwC_qXG6fzxFXwxWMEBZtGQjJ2uqfL8EvUd2kmVx2VxjemAudI5htw9q47GXkKqZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6FjSc1ouopSu6p2ZrOIPnqzL6l34GeMcqkF_Qq1KbI_yjvyzh0VKpnZ6sp6wVomy2LGstqUuISVWLnsBhbrdFdEyL41GuReJ9hZdwl7sGlHnEp5KOKGMDKJnrBtaZlQFf6rBPS95f9DMBc58Y9WvnrTsg4Ol2Py3SjJ4PH_Zr6IRb8IgF2wR3MZeixd5Kjn8V-9YtKp2GI0_1uAPB0JJlpqWBteFPY-Dn5M11z0b1yYr_WkIlPKk_zsVyG1XfwjAsM6OSqNkpVUOzbaiwp5sSQEoVyvM_1gF1RyjaH-ibsMntZ_0LlQplbcR-3hfX-HBsow4gsFIwKz4-d1Cnxv4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLWTs7G4wE7das5Ok5ovjSyEmhJD_6aNrd_ksR6-VqgvgAKpZ6au8CVXTsFoUA4iFHmPLqWIQqufjnwfA1O4V24pW-xt06I9D7xRrTdWZPFYWOYOmT9TY3wvjn1Ja_INvJJPLkZazV-Y07UxPQK4BepCPxVd3jjlBrIRcaeD6a3pqaQcnVpL4uHUnd6BWCDsRKecBlmiD1CB5VrkUjs4Q8qp8bQdpX5rAeFUfPrVzdhAGdwPnTITb7Xu_kNxG4PxV64W9efONHkNns3P7-zIrhjoaMghk6cnNakpDbB73zQLCVYsUEptnZPG-FkaOaHFkMiUnYr__410IFdVth19ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBhdpyvITiUq-eBYnUpawMFbHA8y9R-MBl99-6QJ_vqrNU8mgjh7H_esHccsxtRhMcuwyHazbjfK_BPYKqPkzBh17j0XfQTGS82di85Lk84nn3YlYtKd9oLGB7Yz2h82GMidQ17ZaWjS6uJEiwlOqouHec9HVVFQny_4KzlM--CDYNKv12rBxQm8AzwzEZ4YjLQkyqpiUOEbEOf3aMtke5omSFN-jRVrnTkm_q2n-vtAVzCSu6XcpAjD8L4NoS7vTUaw_rMsmJNdT30IATew7zyzl5xk69f_ZuRC-62O2G9BxaaoPZBd1Ud4d3cRalZ5skLCHXNzfegjBCxtgzhk0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGzXkni-ojqK5rkfFPPCxtGn97WEKJedgJa3F16lUSjkP-nbma29MYa7KUHtAW8M_SXboAm_VutDYdrX2L2FrMr5NrA1KSAZMUH3EtRf-MMIWceDIuvk3_nEyaP6rf4K6OCSAd9s4RcHPx-O9Ue3r9bIY2L9LCB0V3H-_vO3Mk3nNpyjf0o0j8RvH8d6bTYeEHccIbYCBN5CWKEZS-4ajF8AR_loNqRLFwRGvILKP6nKP83FliUmswB9kQgxmFAw6AxgCJGSaToYECAUCJSDqanaFplv5dMKEpVKF8XZ3T3WHCUyH_P52iqaxLxIgHWjmft-YHuPK14jAbbIWWpaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPWKpZ8xslemacfRVmpH8H6KhFuNG00egJTIZn1GvWtLzuD5SKseZHsw0UGk7shDsCnfNdN_ZLyCL3mN07jaqN1hCuzEA3Ok8Npll7eJj-qZZBgx9Vn2bXoxqAz1d1NqtEIq2af6FvOimGDXrwzyy9InB9YlFJUVNpF7VRf11ZGPoiQEHmT8t8ax-tijxhkSCGKaXZD7l9zMnvihOXelT4v7PzAzgg1ACK9lV-62-b1u-HVRHPPoTKe2I1bfLfpfx8pZIQXe55zKIYT6mY-PJdqIbGwnPpueT4e-e7PbjTcNPMyp1cFiQwAX15bNzsk81PrVdExbUnldxD-t5h4DXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWUX5pIi6cYpeHR9TAa0fRaIOA50AxUl03_GKIlHko6g5-b8H7l8gsUru1aRUO_bO_YepznyWq-2OkeWLwFpR2gUVhqgH0fTzcjpTONgnwVHQaFYjoMcp3b0PlP_lxwA0Zk1qfiUCCqGhSuAlk380hz3rxl-BT9VTJuqOG95gBzdPwVxcsogiSv3cBL1IugEZ6Ns0TMfkmOEgx3LpWruoF1w2uEy6HJ-DIJBi6NORrc48mKTkqAJB5CQm25MzMk0IVDCtxm4N1tvEvGt_3BPA5e_spZrHQ0pJ5Sr_y-If5pntMEA9Qcs-hi_prO-PBR0E2ttYFAPlgBCzuelSXoHQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akNq88VOtP0kYY82flLbwOJKAmDze4Sklk0tBWJNDWCOZ1lmzwwA_oeQ-Lv7Nd4F8U4D3W36tMutWElZSQLCfaSzOp-vE9LF4R2JThV06ydkBAvwTsRwd0EJR4G8Xx0wEwgC23gEAhk3TSjdfYwMz4FrQB-i9hYhA6kZMtLaem59ZzfVxV8Z1QK7t9drJfJxD5l0Gr2ng2Ac0KsMWu7DxaHPamiZxZJtuHYPwFjLLlXjKZAcwOHPFOHlOuwfLlMIGb62u5iQmtKoGnRhSS4ub3lA4MtNDoS_crX9bD2tl9xrDRQ0awJUZECA-tObdbM0aw4qMFl9akzwJcOuITtGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ1hwCBp0bQ_GK_T9kR2T1FpPHN2ihgHwUmyd1WPvdDIoUg7oiu75aiT71FhtFt04gUvgFTyifeLiq3B6lFD2oMIxxrTpLwGS_8CqTtEGklkkD8RnT_ffr_PbsrEIOzHCeuTPGVwShNiUmP8_ldwud9rT4LFarC2pHVKbE3X3Bbjl5_a77A_fEu9uRRfSv4vXTljGfWIfjapMu-dXJgB9h3r9PEZlLVx_xEiQsaM5irAtc36tWxryhmO9mVbDNoR4k3jwFpaUSN42SCvqeJ7-5G5-KIBjLwXtu9TSY3AX6QkLSnqmX6kINEbWwoB2gyecvcIPZq0_fVJogFPIUHJfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ4_dnvcB96OTFF7-m2nntO4Qm9OLDMaZVWyi4_WfqUwtrMKf847S6K7Mtim4ix3dUf3UknbWI5rodOKzexSyzoWpAt3536waf6jKIGUWs-A5P3x96tGDXv8LJoSDN1jxV05xCnRAeK1rm4qYBe66RXfRgPWDC7aN91iPS9W_2jCpSbHrOHuF8YaDeNEU9JO1LgmoR6B1lMCMvXi1-YNs_R5g-OPZdbVnFfFsnGkstwNItULqXWgHAY2Q5iMDya4OIw20pa0dnlYYVix7KFCGR8GxmOBBC-2dD1oNoYrR_mn_u20844nHUyfKq85HzsgI4xEBwSjwFlYdMPktzmEOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7uQmFHM2OPJDZF-7VaWnENV1Lq2ouIz1Pewij5fhUhC4agrGb6X4vbKTtYOC5_Vsp6r1HonBOYOPaD6NaNsQvxDlCNIh1d1nmTHfur76Q7WDIcByLq_llKDj8q3BOP9BjSOoxpCVPfOPcLuWKzm_syHNxzzm9Utj5bpcdqkDRNjU3814ukreW9bWHWR6zIL7l0h7HejRcmuB-2oMLyHZzvmfMzdO5c45fKuJeHRFjEGKiEHO1QfOTUkhpDCJBEcBP4SQZ4Iw-b50tTjKcgspDV3J5pZuZNnHI-BzuggIbhxd9hxQBKy8L3_XDdMYfRClzJAQMfhOj9FXTljJVmBOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPky8JUp5vx8t8JQK__Epyw8bc10XvWnFGAabdMGy8MnBePImWdsi46C86Vgn72ItRTJTCwVXrFa5gY3am_9IM6yE3p7dLOOIiNVvG2PDVuwUu24LvNcMFo6A9TcYgdqIV2TKjNOCz_ALxW7Wn6sGo8Zss603aizBCX9Vr2A0BpSB8awS23tQquNfsIwt4oaT7gOxZR-X0NK4CHSSKjM5OP7hf4EPS1WK_H9pOPR9wfEd-TwE6xFKWdzxeFzfqlIGW70YLIqUlcTAkgl274s14hJuOp13Sk-zhJmUSyG69B5NWlnbWrlSUGS639RneKWwfZ04-ZvXagMt-Z6liMnig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghLxpyCthOae8hc9bPPAQsdDuH4QgzY1u1xD6t2cAbROwuWv_03wUL9ETYQqriX5S9RbBaagTVawe96ZhaUwWyVd3OUuSif0BUCM6mDyg8-roOeWWE_hfbjxffBX4IoHRgUWTBR8pgs5lHTk7wIgGJti8MwsazCSjAGZpLiFH_Aor3Er9KZIJqC-WrQ75UwP_HUY8pInqsdApLHYosWPLBCVdur4wXr-ACdVL3dfhZH7Hw24DaniBJAR3qOe0slLOValmhjM5VZnJ5s9cY9-Y4A3zfv_rO625Y2urRvHmVVx938vBImLtMSgd-iDek2Dj20d_B-CplQB3d2XC8sw5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evKuOPdeIdJZGk9soJApMwY2cM8kJCtOGmwUSLFwXf5HSgJl8prIpPgobwqQeA5tAbS1tQBaIIq6A6TA4QNbpwkrnBP3RYTnxJ-Hdiqrx7yrEfJyP-SVgOmSYy-1bp8E2-z61LW2ZsXkkuRRy-fSqCJQoSjCSyrNH_gEV5-owdlLbousD0deSxvLgZXGvCeSAcxytpe7eJRRT8bHExYf_bFPkmN5jS2l8LP35Qun9o-SCMjPe7yDkH1YvF8wkkY0CwVc7ZZND9xdZT7LUxyE_V0wwn5rkwgoylaavpZBLHuZLukE90vL8Xvkzpnm7Lnqe1rub91gf57AAEd7Hlpa5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc_Y7u8j20wytE9P5vuGuoxk17CpY3M4UFBbCNkAgMC8lXj0fPx8Tz60Ktlsy8qCzt4AT-zhsxJuWlPPLuakIO1IgNqy0IPqKRfEUtqJf4hOcG5t8jy9Z4v9yqVS8xB7LCWQuj-1qIu78k1rQeKsM9k283YeABd7JIV9ygpRuNuXPDqZV0bXxY-12SqS5XBL2P6rpFoa1akhtI9VWEs6AXxuPOK1112Mj9KdcvIwXcNcCkDTKtJBzLdVqJEtHIqQk45RnqrxkWom4OtMCV6trhxS4TgWqF-9sS34k2Los7yUZpytQz3TyI2a4pXcWrWXjCx1lZ8AQLyBujL8_v1E-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udm39BrN7l1QdzS3SdFWad_M-bC4wJVbgoWvYLw_dIunpoQ9bFpYBK-IMRxwm2SI1AVq2UsG4diTBiJbPEMsPl-s0EOTYhfEXkOzZ3lvpWLN5XNoqzBZ7hEZkMLMcQJp-TrbgM4mGUVu_mq_Rhavuq_9QE6w3thX-2Xb4q-xQcM5P48j5GPcHrM0DDZFmisvTveD-p-q1yTtHqUDKo_CsDhjbZOTVE1FfrcD98Lh7MTPDGbp4hyup3GjqwqT3-MOCR-zJV8D_fJu6UEZQXfhIxAFQT8G5DbX2Npqknjd2OQMs3nOOvsX2WcTd0C78pipTrlJvKOC8LgjtFv7kr6SyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsnA1BwJUc2pTqOzwsrBL4TFO-W9Mc4aAZWh4u68DhrISekuD_z9P1hcSYG0fLpJEKcSgPcolkVs7FoDK50Eul48JnkKVtl2WwNBkalhVexxIm9z_z7DDKwLB7OgCOQywvsKRoxffE4dCop0K24XafFcvqaRj-GF-MzuU8WvIcLBW8EdZAaZEno9-Bh3w8JMdVamLOuXNZRfwGSpEhmhdiKXybHxH3c71LB7Ny_M3yLDXhFJNDmaVhB7csFswIgfeIERrhS34XIcOC9MGKuV_P8cqFHZY65_ANK_GUmErFRpUZpjBnoH95CIqBf9eSrziZu7ux6NbNu9zidxHIZjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHb9uoAAHF7KfYN_GDNEB_4TaTqOazsYb0R8xiz-VvUuPyma_qCC_Hm7BGi_gfLgffA4groSoj-jyLeH-t2fk0GK10IBtAH9pvKLWx-yvAF12Rn6Ac0rLN-nF67whdffn6S_IKhIw0rEvHHqLYNiIF9vI2B0ZmQ9kT9k3LVD-Cn2OXzkUVYubRDVXz0Nba_dHHM9RToYASrhFAHyk3PYtCLJBPGuD_GI3whonpfYCxCBduq_8U0EHp5KpfoJ3LJNOYwgjBxKiI9V0TebopW2cmZPAAcMPsR_KbBKGIGvUyB6Rx0NrwPLrXA2pvwRkFydJ2xtLT9pNwCYOIzz22Su1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSWV14DuYgmeBPdzzclcfistdyVfEVrNJhguj1A5I5ebI4UX73ZqlOlUzVmCP3ZANNgeZD7YM4he8eMNL3KwqWYXv1_H2h2ADatbYueK25_EDxEr7oCkPYF0F21S0BrBnWxYsUwPHejPZHEbHgoo45ZS_LjOimjxUWWfnVqCl8EEE289y_rjaHI68evju5D2lXXfSAq7l5Yw93-vS5e9ibcCeLdDWWnKAU6hk9EXMP64VQLG9HB2XJpApEIHh79ifn5updfN41v0YB9ZbkNZTPXdqT8A9NR71e_TwIdTRg5hcTJrh9cU7vOK0adTTXZ_uhSJGhW2u6nyaobylZdw5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mby4agda1wGnSOc02eWMoqtERoWUx42Qjf21xH1KAwB8dCQDU7kIovHDXuVg-w0VUi3gId1DX8QgKijiqj_e8bl_RV1LKUTEGPDV7xqJsFcu1jND9aYl-pwL31O2mzJ8Py6c9Bfz0KDGhqmJ_0c1fC8Fr8KfFtdYIE4Uj4exwIiAcDVEt6j3M5DjQ8hIZTDVBJaLqB0Vq6cRrD8cPZFPzQJdpNzJizr7dbnYC20HyU1VJEzRFPQe0nELF-X3ZS3K2jVwlCm3og8hw7cr9ARQvKqQcTt2gB1eQjT1ud__rtifHzqQvVaBNnlTjBb-xcsDYasB95b8CRX-lZDg8zPJmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kspZFrD29dildVmWmOf3FFxdBbJTBDUtcPnpyO6rrjUDKGTlZcUxAF4XgwMD-JXuJU0WjKpxwjdZlBFAniQvP3xi1ok4WHuqD38NCdYMpyB3vvd5kpEmov1zTKOxACQtgps0LvRkAzpemOmkiv3BBtMOnO75XOgkjrdZeYq_bNzOuR7oWWAK_rL4Se8lFMaMUy-CMAsArkEyASdGZlPQuDGZWlaNxy9rjbOU7HKk2U8R9SxIhzXMv2FHX_BK0fCymzDBZw2FRDrm0WIbVnKo9Ywqykss2MAjQszvK40-E8OqjAzsTamcR8AlbiHzVhI9aPgAymTyaalacxI86tqdcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQdVHnyS6BdyHIaedQ-kZCAZ6kfIfxus9o0gV7tVQpcAiSHhTTkM9gOUX4fAOexujYdPquhM5ks94pgya0s_ioLok7aVYkcYoqxJuHxS7W7JGT6JC17X6H5URTMbjzZgdVisuCOA5tvQgEQbrPYgKFxep7MS8r1r3oKJ7kiWLvKb_jskau_NstcHdphd4LW4j3-KvfmNXAYVIEYLoRVKV-1-TVDqcZmeDqSaqMiz0RWQSZNfHzaacFuu3crkPbO9-EKWkpa9E6og8MRdZ-SSsZrzkVAp2L19E80092smXYcMJbXrnkZDpB9n5pyz3kK1ovilfsgqrpbhcP3GxYQVCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_YgQFp6Qi2qoJJT6GhUfPuplCEY1C8yCEYO62LQBuvYxEHTY7va9HETyteRtXiD3rqWTcDHQCGaRt4jVxAL_oujOLlKEJETU6RYqSp9HE3YEroM3ssNHgE0fAT94lt_F-0MgCHnzzAcGREbktPW6k4IjB6QTOJS2TYDQoBlrh9m6flMWkAiM5t5UTD3wTW1BlpAnM7cmhixKvEvpbBCv5WeEMLRE7f_WrCljI5UyBdx_Pu5jCQuGQ4C-XeWAC7pDesMC7e-4Dzs2TA9sVceZeIM5q93OqMxmdRqkukC3hERCyS_47cbwwpOR248i2PYdYYX0VtZ5p5T7XnJnlYj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Esk38IyW5hjTHJVHs3BYTHpkit-2b-XskkuTzTxWQAKfl33afZlqISSWLMrNVgiNIRZZFtptHJnvFUDOq6Trq6O8uG-m1tzGs8Z4T2zaMsstOu7UnVDkacece0bKjwYoFTUFsz2T8rWrCIkxLCiYrpV8LchjGoGNsF3DtqumbEvVyEUO015GggcUKxFkFxvlspztnqX6k_RmshW1Z-1KqtawYOevy3l6qyagEAUQzbPPU8fxUI60B-v8dV_Ff-n5T8ODQBxZn1ELK9d6vvZ6ad0KiLFHIO-H4yDslXz2csI_kzU7p7ZxCil5WSY6MtZJWWrTpUg8MDY65169PVi-Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctuyJy9JZFwgmM0AkxCoSgmP_E61y2AOc2moqCfmdUcgu8Bq2ZJ86i_-9rUhHit9G8tX_hp2UoE67wMB8BKr7sca2OPdZGNVlJQ8-8kNKDHKrB0PJNu82LcY_TKu5DXCTo8uKjNdKLuHuoB74EM6Tyyb8i4BZjAcPVbt26UOpVm23EeXgsaX4ePSgnF3nPJXSr7flchQf3nbB-oTEzRPotAFaO_1sfnoTVpqTPHlEjplNsyX5yNJX3XcM_Y2N1yksYY7QXAAchSasUVUZIh8ha5C1hYWkg0C4zZjhB9NRGAgaXryZw1XDQZ7RD_gPopGlQDkKzFf5n1CQJWkNnD5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRifuYNQM6gkRFHa1yEb5e2QUmbOSNUDvjbjgAa4loMgL8dj0sLcDEsuspDMAsARwjbM2kIJVZ1cmsGpQofXSs5aSYbSOPT9IxVjnjKfP2NayU6JEr4xUkS_U9UhhguofECB4YCnbqUUl3g5yVBb4FNw2XuRdrjfEVuwwkoH19MNhE6721Kaq-QkhG7zQongiprQpgsHkoU0DiXLD2t-08idaCu4XwafH6ioQsR3P0iOPCNQ7PhHtDxffBOa0-6rFxMYAnor0ZKEf7bpXjrvAFBT777_WSqWwtzI6ERWBvH00cUUqN724NcYLS6HtXPX71MXgfLhHCfXqu-zdqKOng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOUflFK-2F9-CRON-Iz_-_npg0zttousb2BqMMyvHr5Ke1faErmSQS9kndYomUS_CM5zV47yFE898buMHXBuijiuGf0-nkwQ1Wv-YeptD1Bw9f0KTwC9wzlhEkNqggtD1BtRsENMy3o89vS8qU7GdxlLK0UCobjjcpfN19544hZqZMeoxx3oXSpl0rLuuneEI8KLB-o97RHgj8D6Mkn2jK-sFlRMRUB1ReZL1eKXqntXQaGAzdc80SySUfk9gbMYgLl1geHeYtrx6gJI98Ftp05iFy_Z6w9kV5WwQiIpj2AqRQwo23fns87QokA63w-6AfjZVAPd9cXi4mMCmwgIsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVkHKJ8avSO1k3GvvFK52xuFx-pJuYw4iGJWaVhMl9lTTglRpAyaE3uy9r5Ltiqv51aEK9DH89D5_llnU_Q3D_wpkCPRUxjrnoPZKWNi0QF-PjKvd84AAERCH-w2U4NWwh7hbswdXBhCLsZp7K753VrHgwVuOQR8J5bX_htHb47Jgo1St8kC3kDUmMXl3oTis7RLnIQo5GJ9bO0qJwXIebbI-mjFjZ2JAQZ-s6pu-Z3Q9YzWrPychTBeB22l7IlJEkY2OcaP7Dd47AQu_RCaWdyf_PpO2MEVsdD8gvE5jubt9_b0KfIedgxvkKwxh6rWOxb5iPsVjS78SwDe64ke0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZo7BPpGD-spo3Qyw5_INEqeZJWZgL6W8K8s20fxqrBceaKGQfy2ezwB4BOte8FuctmD8cqtb956KGNFKvVHKCWX42uVVCUOwir2AJCaybnlFaq4WJmpmDWHeYLtSi43cKzHQk9nYWrOJ3T6Fnoj0hGScAedxDW50A2z67w25qgENgwhbdWecA-BjFrPflwF7l00V6s7bLmdm9XW15pakpxtW6LxL7o_vx01Jyjk6EJoONOpXn5yyZcw8LW41KlWxuUOjj-V4c_kRuspnXKO5RtuEHTUzW4R61P9Xd3CRKRlGn_Ova1wxub7I2NEX35fGkR3yZlZbJDwQsGH5f2iLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-fvUiSf94Ww--FOK91qt9IbMcTLV4a7_D7_Q1L9V4E0IuOs-qo4Rniuzu0sMHeK5WjIFGO-E3JHKsmpdX2SUecIdN5VT5m7i8hXZh6SEIHYr4DnUvv2jubxlMaaVinv3frQ6dLZB5lkcTDdVJjHYxxh5ywQQ8hPSJw6YmOJ5-IUdfIqbqMN-dEH6mWMYyZ5bs0nFyXY8JTQU6XPyowJK_aDwIfOnVVb-BGQWSE1q-gCVQ_cn43k5uQURmQRPCPsCk96-QV_8ZqAVDiy-h34X59D9QrCtW8fzWfEzd4rn_cjTElSdhQT5hWNAymS7k0fleTR77ca4xkph0WHgr5B3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2uKuamg8_N7fI3DgSytQF-N-DSvRigyBPVVt0Nl7xEU2XxuFWv0QyPavMDEfQ9rQzKtr_8Q2LMcVOLZujYuJFSw9s8x-KTZ62bsNy0gZkfkMQKpDFqtkqXlKIYcEz5IaJlHzNMKXe7FGAnH0K1V4VihuH-SbE2h-9tcPO7tde8Ke8IN5eea4ZPP5nOk7yFcycgyHa2TBGNW4aRziXJ20nD2uLxAkf6xDe6H8z6KxH6vArY81K4VNQ9TuSaRkXPFlnaFcuQ2yOXnVIEOM7Q6gHLqi00hYjDG5xEG3XcIYxusGtXsyyDVBXXSRTMQaxF0oFRy_wvWWGU_PoJ94y3IRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaSTtgyh2PZ6JqVWKSIXnkixSUQhcTXRzg8_x_f147sprEFToUA3vSYJybpckg3zAUFiKt7UEvyIaq1QjoRCW6j0q8LUH8zZTTGf7lAG35anXyZxcgN8aBjyaL4bBS3DI6QGy4NHEFOKU3XvUqT2xfa1avDuJozsExAKzFJRuPXYOM76k6VJkUqOt-l6mGBeQf5N2De8McyIiGhgzwU6pTt-hWmsz3B8Drt6L8V9L537TAqKgjXw-eE26oxAUMFsrwBfm78S9j2yKb-KkGw0HWFlcpoxqKZpIXsgHkJeqVj3--x-r8UVaKK43CsHsg_Bb67osQqJ6ZtNavV_jaIz3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEQ2L4OH985jJYWAICXd79UHTuw7Q4l2xH68S1DJcp_qEKdAjrHuiF33Ox5ekWA_zsg06P1jJjpeZmIuhalsxSk3qp-sP8rNn0HiWuLIPeZMx3xHfLiSKtzB0ODBz0KFZdHyYl_J5hKpqrNgOT4OvavgEJQtFymRAVEs8FGmsZ6Ty03SwPtxc1cx03kWSKlagSsAknNfaOxF-oC77_mGKuE84rcRWCnnR8ombrKP8cy0eWO-WHZKQn_vFkO98M3hlD0EoIRkt0WbsvE8CrVy5UPSskUm1NuERTZBTrF7nCd5bd3KERVPflkuzHmrMbyqRMA64zqjQUNt9g0WQQPyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opBH3mlwigKISxPMS2rchzcM8YvZjo5t9QaF8dyqrbJHkSJlO7T4hRqW-JRd5K5_w4wVLdxRBsyrxm5mIxLcgzk4SuXYhV3XteoSn4qtYBb0RKQAKjmzd60GBMjZw_OMij1CuvhUoTns4UNe45-Nldkjn65Tcvh0ycmubvFmeszEbh-vbHdhLow_wFEUHNra-8V-l2ZsVuKpXUQ1bvw9aw9wmCw7kvP8f0SnrdWpsR1yQ8whqFYto1goewhzGzFBAv4diLk1k5_bX5OKuecCvjwLS4uT11JcPi6Bx4RO2RR20NxagrDAZ4RIZnOoBPxmyK6zs8P1RGir_jYS59OsiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R45hCigiGWCNXaYLpVG67jiYKd5pDHgD5FysrqgaUEEpmI-LGBRD7WBJJsyp9WV5HVmfRU7Bi8x4BzzO4Zs_UJXKdgph8DjHRIq37Yn8AMWioagQzeYbRAQ_7iMHTqmml8R8nHLPP8tG9s30UR8I-GuyKe3bx5rgFVDuJo31XIm_VMqNF54sE8epgErIRC2FOHjFG_0HI8aJXCfcOIrnlBRYoJoU1y6I-GyvcubbMrWYuTcgaCk6Z3a9aJvRauXCHAmmIcAaVkkWbILbioar675cCK3CV2bCwpTXr_-8SeDh7njHMzyife3Hoq4kl8qMX_GTvFmbe8lxTb8wB0oBYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKpZrKpkEtL_XbPArr8AWVIT0KzVv3ggeZZORa70biqn7R5IJfp4Hq1aNSFk7EJYMkl88Vs0ZZhnrDWAwo3JHX_FKUi2q6wnVarbpMx7J9xaSeCfQBWa_qjC_ewMGeCYPVbX-o1Q2AgYVkeX8lzFPA1460pvF-k8OzfSUWu7QXGQYbHK3mwbodvULtV7_9JhPpQIyZwOTzi3m8nCfAsu-ur1Rjq48bXTLvnFA69-_9HvHjFfLrvHy_sijb7S5UxaZM-QLqCCQ6TKL4yfOEatlvkk-BM0ado9uPqQ8v6qhULKNFpdFUpqzUB2tN5ty8WpDGj31DAJqGU3FpHWyZG4kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avytMzOY9CvjNg3cthkU9Mrewt_Pk6NuatoGEXCDNnmHaQhNtF96n-zzx9XCrrY0hXQYhaklws-8-uhXwmx0xHZgWAZAvFNO0p2kpyJ6FS-2K3TaGqm0hi2p7YaLqP9r1f0wobGopDjGCm6Cs9Ny8ggZ2yZDp47CaemS8amdhqV0cstRxpc4LDk1iyOt_8SxKeUjKrW1NToB9DFr7jgH7UakI19kr9DX3v9Nd1_NaPGGxblVdN7_RLJ0XVr8hDJ1GJIPKLdV_n-Hvjio44_xqCm9FZaF_UpsTVp2sgxFmNGx0oyPAsLJHWE8FKPeuBWDcPv8Kovba9SlVpvk2JqRrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOZ_eyam2R0eKNb5ZOv-maHzyDvNHQZ7E2FkIKgdiGzNek--jITJL4RoSIpXhVJd1riV2B8dDVl_9ik5-3LSqpAv8wnoVstn-aAG6LjW8vfWsxQC0aJcLSSwvIm0ECPBSZ6eAH18CE4MpjP_-gjOX2rbnDwOmIh-m_-nGFrtPjNpyG8c8gwnnHE6xIs7aQzwE1ojTH6hXdtjl7Q7jm2XOm-RQeREqUMFVzaLqiWoMuMxESY-TdcmoeVQos6HVzIq9GiBusWF-2AUfDdaQPTivDLvvOheRbHNH-CZE901GwhotiE1mPMna-N4Mmv2hQTgYuhgWysxoJjhOLFGtHVBDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sbB-27NV6yvNR7o3Msp8YYvjZvo-Uxo7z36J5OI7EhFkBIvsFQbSl1naLJm4jqS_4YDYuTiAsosjdh12dHSzD0PihliCvLX4cG2RIubvku45S8HOkSItyCL0wAevBcytVVeXCilLoNd1yNl-slCfqrKLE1pbvG5N-7-ujLbN9loA4Evw_5L6p72nXNCYrrRqnLW7T42qD4jYKaCbYlGEDW9gIS-i6mpqEbCE7E-sURdmn3w2FsJynqAPZFxRAXVY38X5OpHJgUU48Q3EGcAWDNqdIqe-ms_mmyofe7Q-AhSFBxCh_Od7N8qweGstQ7b2qoTuXlRWtLT82Jr65neUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sbB-27NV6yvNR7o3Msp8YYvjZvo-Uxo7z36J5OI7EhFkBIvsFQbSl1naLJm4jqS_4YDYuTiAsosjdh12dHSzD0PihliCvLX4cG2RIubvku45S8HOkSItyCL0wAevBcytVVeXCilLoNd1yNl-slCfqrKLE1pbvG5N-7-ujLbN9loA4Evw_5L6p72nXNCYrrRqnLW7T42qD4jYKaCbYlGEDW9gIS-i6mpqEbCE7E-sURdmn3w2FsJynqAPZFxRAXVY38X5OpHJgUU48Q3EGcAWDNqdIqe-ms_mmyofe7Q-AhSFBxCh_Od7N8qweGstQ7b2qoTuXlRWtLT82Jr65neUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmsvWp313S9MxlyJ0_9gRTcT2UylZTtnmFTMt-t1Qpzd0LN43oI17giCN4SPb4Q5V41kfnzv18LmXTppLOQ2VRydOZDhXWY25-socHnrG_wFkdf27a0wdIBp20jhrmJgGic4SAqpy0wHzhbmY0bajTRKKGoji3knbryO0eYPOpnln6AV6p07lSFZmG_Hmdu1-C5lC108n061Ks0PlpSnSa511EyvyYjRnufSxMP6-DB9xGkAYFcJtHCH2HgExb14LnlB3UnziP3PRwC-FnbNDhM8CYas_5GAonYpKcvu2YLNPaBwH8MHkSOioiR4MC_G95ubDPNvtKnGo7CNENGChQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VehKjdd0kZWnKomNKF2L3-pwFOgrcPJ2LdvT4xnbEgcuY8He7CEjlBuNQAxVstQ2AoUHgDHtjsmXiXiiJpVeV84nb5wJHW-ld7ztV7Ie8TwuGM2J-TLzj55fOWx32zcALAwCEoXdMLmPmBEPkbR2FTm9fCzX6M8wzRcL4MCjUd6sHfGBdZJdrZ_SNcmOk05-rqMSFLelLfZjlYXmPGJjTtpJsUZd3urR9BjyjCqEjyVlv4TUCrfThEYUsIiwhwVnHGcEtYuoZk45EHdvF3T2-ojfLi7IZjFtUKhF3n5vCTQaH695CGgnufe0mS3BhUQ_1kxZUHjR8pQmBn5REfMVnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFJ4985V4tyQmimFuWPAiHSxF9EwZiAeZNVSNWm4GNCHlM-phUbreHCCAvEsHA4xiBxnS1xltIV5hyDaUgj4f1AAaJ8J-XZBJjLstXlcEDYSvLMX5-AB5vZc5t6UXAMeQ5Cw2iGOAEKlyg8ekGTh8NkeMitSuP6RzYgHFnVu54d62pbhOomXk79hxhTSFnLentvIatScgFAqQKuZt6_S8MHzV-4HdcjS_3pjB5VKwBwz70pcTFShZzZACSKkdDimM9gMSfhegJC0w6zzo9wgJMeZlBZLuK8lwpIOVFvyqj--dFXF4xAqtW0mJP767I3u1oQdauB4jGchvBRozRK_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yo6ezrRlfwcyPaIsl1zfT013LhCH33g5F3hD94q_srBsUL5TLWsO6sPqNb-fHjBiRkNEh6xBtsodJAhFvc1iVEo8t_Q6ZJRcYd59L18aX9QWuplA1ZdAM7L2ODm1Bx56wtBZVMf0a1R-uFJife1WYpzi2XnSaHo9OK4tcIGngxPwu_BSE5yikYmNDdfY773mfFC55CysaQuFtv1cMCTVffLWX0f1ebu8O3Z4NA8StnGrnvizzqQBKeB7wljbPXkkTHp9mjFYNFslvOW14EmFS9HyI1Jx51K6stb-r14EklmdFXizl3ppEYRErVcxbO8J5GfPQ-LGdDPJFZQ9bnHEpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZylHCNfFtQT6sI5lzChDfvY7cBTvnqjbKsb-2txIwmX_yMBRW1gb3o3bMI1cEF-dmmNqeCet0KAmnxhit5_9SuB7w7imptnyeFxmIGYDq1jM2XDk0ej57OXxSBdvXC8Xk6PsUPS3yU_C-NOF8yWhIKctP3WbwFM60x1heVfBsyFqbLFBQw5-DrVDIEt995L3fcS0HJvZj9kIGQKJRsbZ0zvr7ECXjLdVGpr2f791BYpfEq4bDLrr6ygGpPp-wIYQ3mXG-vqiGNat2a42_2tzQ7WIl-atOhHab62dljGxKjo9swp9Ur0ix2tffJVhyA4kIN0nu4WVmDU7HwCi3w1Xsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPw0nYZsRwoxH5he8sWFdXshVFses6qDV-Q3eGeHakYERx3dZsxdOqpC7BRgFsNbCARYWpoIdoQyWDd5rTEnd7ycsR9bZi7VlRP35P3rT4KbsKAc97HBPv-3fogmT5yCN5O0kOnyR--IKqvGokvz9ouCNhmljxE-AfvFG7M1kqcgRsq4wUQDPYULIg3sJj1RvQhTJA_I5S2OL8WaE6-tKxvQ-S2X2KlvsZj5mNYftmlEJ1PEzMnvbckb2oJbDWCYXwpJz1WJW3Rq_oz200-npWC7ueLi1CQneWk74KjxLl-onv5mFHGwEA5g5t_1ZK6OOkCxJEh2knBU_yY4V63bnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3IFyv2g1PaK7Vp57E7dlb4ms5LpWYvcQM-RsCxDiqmmoOnlreXxNZO45yd0DMK1lQ1bpxl7JlBjWsaMxV6DWPr5cRUSBJANmIMBWl8vFIaHq-QiyiWacDZC1WXZwd5LIR5EWYWNQX5QbSkyfwmKCdJVPfLiVUOyWf3ZJ8LDSUyQuWG1f5wPOS-6cimJm5yaglt_EehoRMvjxOKf_NcXI8Vt12xM2TR53y8qEKKUF4IGHsRmcPBaJC07HNH7BlQiphImMDDh56ot6GSNEPREqpM7WnB7fIWJ8iyUo7cn4fligFtP0wDzC_q54u9c3R3HjYVGoPzBSNGXgB0EameUsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=qdCMnEQX0rz5IofS9HoBLlzs0kuCW7k4-sHp-Dc3RIn6D52th0V39RXy0I_bbW-b5FLeLw5EPrTXsnjRxkXOXn5TfCQg4IbKnJAoWsFfPMOceQ7_MWbdj2puOQaQJ_-7JRNIHuva_vW29kZSvy0wba9K1uaBb9PuE4w3OCwIq3F5tWSkpGsEZErY4jetSSSCcMQTgKdLfD2J6xIRjJLntLE2Nv5zH2MWzIOI0GUcNBds3AYxSVbvjOr7hHMOo5-Z2QyA9t6ISjVq29WRSDDx4YXvZ39OPHCBNoLRusUlkEg5FgfsaCQHmJPAD5FNv6ccC6VXnzNTc5oeEBJHd7I8xHIdJMa-zALN5qICZM4YbyXlSwOYOALf2-Zfzm_rQK2u0pIWPjgB-uxddSnT_sMl_LGPyRG7shKIfA1ecoj_1ud701ZRm_FeIQtlB9KibGne2R8av546sIG1c6gKkEfJYuSK6ywVs19RYuIT-0SypgeNcn4BmNRyyVH5YxDPn8llBgM8STmM-n8L3I7qGpbkQrECu2S7z367bbrBWJ2GVkFKWh9YlmF1zx559HSFHCvVouXbYtogOexzhOyUsWOf0VuUVdyWw_tQ7s6xw5wW8IxkynV9lsU7djxCM5C1_1gVtzyogS6yVvHQ7SnFojL7wng3_b23WLNGzmYNzZhyXwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=qdCMnEQX0rz5IofS9HoBLlzs0kuCW7k4-sHp-Dc3RIn6D52th0V39RXy0I_bbW-b5FLeLw5EPrTXsnjRxkXOXn5TfCQg4IbKnJAoWsFfPMOceQ7_MWbdj2puOQaQJ_-7JRNIHuva_vW29kZSvy0wba9K1uaBb9PuE4w3OCwIq3F5tWSkpGsEZErY4jetSSSCcMQTgKdLfD2J6xIRjJLntLE2Nv5zH2MWzIOI0GUcNBds3AYxSVbvjOr7hHMOo5-Z2QyA9t6ISjVq29WRSDDx4YXvZ39OPHCBNoLRusUlkEg5FgfsaCQHmJPAD5FNv6ccC6VXnzNTc5oeEBJHd7I8xHIdJMa-zALN5qICZM4YbyXlSwOYOALf2-Zfzm_rQK2u0pIWPjgB-uxddSnT_sMl_LGPyRG7shKIfA1ecoj_1ud701ZRm_FeIQtlB9KibGne2R8av546sIG1c6gKkEfJYuSK6ywVs19RYuIT-0SypgeNcn4BmNRyyVH5YxDPn8llBgM8STmM-n8L3I7qGpbkQrECu2S7z367bbrBWJ2GVkFKWh9YlmF1zx559HSFHCvVouXbYtogOexzhOyUsWOf0VuUVdyWw_tQ7s6xw5wW8IxkynV9lsU7djxCM5C1_1gVtzyogS6yVvHQ7SnFojL7wng3_b23WLNGzmYNzZhyXwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MN09KSNwW3Iin_QRAY3PtksFtaU6iTSbzS-UNMTN09qnVXLkdMbIfKUS3bLQZla1IFeKYK-g9XrRVpiW5Nc2hQ2o2XJjrMsIkq77fWvcOmCL4dK3VjEIUDk8q2Yg-6HpuXoZ2-x9uJYNVGBy49E7fEBmHySgzWg5cqTvZVMJBWbd-cvhrrS_VFwB-dPNPyv_gJRgU1nqAAAJu_ee0GQivY4hGK5JoyWn2s2iVd-HEFPXXtBVtZRKqrrbdHruGhfy1qqxDrzxo1AHVDeGciVUMa1IaHupijyb9MfzCr8gJ8-WMK6pWTpHNPLovmA3thaMybrizncxnIjimNx3q8xZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-NY22_Xngb67P1NbKg8J_vp31StTRMu1_f9deh8gKM2A1JTSIqBohgFIdensOcY3A3hd2bmuY4SXRC8Xc36P_FyTol1-eetYPQH6kDjcSQjVCsSvzEocPq8-BHM4Q9dwzHLJB80r5u8adJT6JMJN-EVD7kHHTzkGPWAq-QLzbE7Z9OIUz6xSuB1n14kLpIxLulEVldbhZdIhCeriXSDb7912uSnLzTusq4I-ysTB9J5O7r5dKXD39Snbxby5XrA7sW3XtF1HFnwgrDnMogzwFO6nR6x8BbuoiT8tsXxwRk0Pkpoa-LUO1cdmx6o1VFKqLhy5cgZYyJDVWjhdHX0Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEqvIbPnCuUw_M4uHW_m5fJYw3ebJLVEeJCf4CK2u1_NDotXCbNHaQ-COXp-Il5irdUOUwbdeIkc3lSFLbXjpTMm3iAnsF4OvsUk7tfHfuft9ZLwjoV_rcPERSMRXIObQrY60bOLe-f6Hm04bD-SqH1yEw9aJkrKJBrD-VUt37TZlxE2qZ5roaejD4qzAHgjLxvFR8ltOHy-Dn9uqYHDzyqpxkV1jukJ0ydOMlZyVHc2qIbfasw1sPUdCUwHTLqD25afsySQgoQEI21QI405XNuWC8EAf7b8O1J2r66zaw8vlrMN_esM1ccC1n-aiZdECdH0mI57NdNzViJforeOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1WwgxI-_7HI3b2dXvVYs7Cbi68MlG5_X8FbLtPnS1nd2ntTVOFNIH0zi1zQD834qDCQy4HW_F07og9RwAwZSiBNxKTlKP295j7kHfHabVRzDqVHgLGu8nIBrdsmwn_b0z8M3HRAy_uAW4m4Nsw4LDDbI7gfUmk8WeRKozRzUw0v6g-10GqqvKj8TjbEQ5CtF8KaKYZ4mmyoNKRafDA4FSQU4ZytF6RE2Hw5X2MIN6WkPNAUULTNH12vtgIOqMzfoRUOrMGTBZqYlSgdDmH_Ba7yXRvqpckdy-BHU6Uw8CG3RSXmI0IpZLRrehx6xf3aCX6Ba9cNQeaTJ4Eie-11DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8Ytwtg-i5bhrVuklIvc5Mvh7ONxamOufZN3_sqFlDJSavbO1Ek-76nmLppQ5ydl-z2x-8Z5pLu78WuNM4XxF5CNmqwH3MqQoN4dWWBONFtCvhDPftv1coXaNDhE41wfOyE-ErkKFGTy4S2wTjljGcqp05q65IkcqVgyqPpuKvZkFec5Q3QAhS_hWkD_sLzLLr6Erp2a-2jeMKjRuziUGKkXx2gemsjatqjbp1WNHAbRSj_tk1FZUR2cO9ba0pq_MVytZqVVsPnJK3BODByALV5DkqP71xqjPxRZQe9es7ke5rvoTumCpdY-zD5j2slTadj5WeiGwi8wodi0FjmoJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YqdY8_9MKSGYSNlMhAJx6mZOKVMODNLwa7nCEVmkas4rNj0cJFZF304RHKf6He5I9odei0FYG8irwXibWIbs8cBb6D4EPGXtc-lwq-IljV3tuH0nowvtodn7i4VvchZj_vjSCAVF_XVOUdijWUnzIPHRHvnwGq3uRYwxs5Md-saxOQOZNbphBLXQgAEt3y9TpMstnAKk7TkU76scHr8OaQnffR8mnio9S3ghuv5d4LOJHirfDBlPk4SAXk9MUDPjzLyoQIUbeiHbIyLn-QGAxdxFjPFm1DarrBJxFidA_cpZa8bRM25eR7M60JlF-uW7xOwcqzLP8jbJcC_z7LIPb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YqdY8_9MKSGYSNlMhAJx6mZOKVMODNLwa7nCEVmkas4rNj0cJFZF304RHKf6He5I9odei0FYG8irwXibWIbs8cBb6D4EPGXtc-lwq-IljV3tuH0nowvtodn7i4VvchZj_vjSCAVF_XVOUdijWUnzIPHRHvnwGq3uRYwxs5Md-saxOQOZNbphBLXQgAEt3y9TpMstnAKk7TkU76scHr8OaQnffR8mnio9S3ghuv5d4LOJHirfDBlPk4SAXk9MUDPjzLyoQIUbeiHbIyLn-QGAxdxFjPFm1DarrBJxFidA_cpZa8bRM25eR7M60JlF-uW7xOwcqzLP8jbJcC_z7LIPb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo4wNX7ww0dtXyQdnLdv6gsACdPAphCR9T74vVIWsRSaECqiJp4qsLK-JHtpVHl9_M1qr5kOE1k4MHcofL7DEtoTM5CmuPyoFTWKiTHmWxzfHbIKmN_jLbHzv3irXnj_kNlTwAdbZVIiK3Uq81smbUSX5po6WF6BkmNtVJscT96KDv1FaV7VG0NUuQQtRNBuFWnjyLnx8WBuaLAxhzIf4uTMiVd6x1Dlr02phw1InTtYKg6h67gSD_iomuWMvvBn0h5w6UYW4mVtKdxEDFPdMdrAOs7VmfpcTN2UfsGymQVZ3AYz22QplW_SxIAvromS5qijx9IA5ip8woM7VhN1nw.jpg" alt="photo" loading="lazy"/></div>
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
