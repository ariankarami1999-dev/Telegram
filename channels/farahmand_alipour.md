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
<img src="https://cdn4.telesco.pe/file/dki_9AGfKzqq05ffQ6hyBlKPwjQnZdnmOaaR6AHJt_Pb7kqUw4IALCfZVpLGbMqpdn1vTMJnDajQ7vnIbGbP9kP01RobGblvHC1jfR_pEk2xGsW0b_jC6btOLTZniT37jljGizM5L1dqRl6jUyinBSorGqTKhM5liv7fYdfpAReNq-6L5Tj81Aizyg-HGv6eVrUqlkxGRtpqpRdmagI2FU2ddA3oeF8gFNbfYcZNrhel8QaqhK0xQisb6D9Jf59G_ZG09Oz6aO1UWC7i-cGKrw0DA-iIOjAkQWCpebMGlJ_o5gjdteVgCHWpWNwWzTcbuI_jn6p2M86mpBWuMZJIaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 17:28:51</div>
<hr>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCvSTOYx0zKLF6l_OFyPakkn2mIljlAQ2ei1ijJNIOnMpO6xaZnv4HyU4NOOPb9DsmNH6A742oDAcg7myl5cYjcUh41dcTXPkl9NQ2ttOaIYpqXYhnwzc0ojH39gBYH0zKrTPD2GMgmwLRLIXNn5lZxeBhwhDrZbu1nW9caz59WbNV8ZpU-MY5tl5E8ajtUmg0QZjFeJ8eYR-LMARvphq0A4xgENyxI33uCge6fS5GDlw5svNmLNklBik2fhNgL2MpIvrBv1OJhoHCxDez6Uv_t6t6Xxurhw7bIrmsSO4uTfKGLbZ4ofTk7ei8NuevxjRE0WCp3yNGMGSXOkXU-xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuBAHLtebmp0i3zJGSC5DvPZLoX0F73DMm9ioklhszLVkTkQTTk7Ib6Y8n0sW50riJ4q-AXm3cOCek1gjlGdlp6GsdkJg4NfLJURDqngcNydiTooRjcG2OvbApBBXj6_rv6BXOT4qv5ZrAG7nzgi-hjSi1Hzef8m-7sFMZElJIU_6_x6ZoIbRBEinOBXPdNi7H1q-4fGeVbLxjPe8-kYr17fX4uxSmgV4lLXgS030geLc4v1hkkxcFTRdn0yBfFJ4p-Mqm1W3Rm6JqMK85quCs-k5rzVomzbggdxg07eI_XnruxRUNW5_u7eDYBpwyMsNKX392qK6JTH2RFBhBsV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaR9NCTrwfD3vNOBPEV_S02tSUAQxGTHYsaGqTZe8cxl3XZbk6-NYz9zE-j6TFbqoxXv4HH2e7VCHv88NCoIaAFhhf6afjvkUnMhtaos6_FaGu0E9qYBfZdAxwBL0Q_ffvrCzzWZmpOokMqfNNk1QArR4ja7PYyqgsghhU14YdlLRay263UIv85n1mSM-JY2k8eUKV1DEH3gpxS6vfrU1ljhrO1c7lHjmoqzCWRnc6AkVi5Vud_EiBR5HYC0_54Y9Go8yRMPJJ2swZ8500mFr45cUI7Zgu-7YnoG9dvg4MW0nscGvycALwwT_929FBdwfUGUPLOs4kHg6VnpQ7rdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZiXrTQ7SbWFTYGt-ISF50z8dQUcWY13qDeYiPD2ddmdAS-WAnfIqxtm_f8K_z0BXWF0jU1K7dQU-_35j37WAlPoIBqn-I7xhBv2A2uFes3oWutiTahuNH7M-ou9bkSb-xbubaCy3faxnVzMsdMnXk7mVB_0AuEeM2C1IP_rvXKqaqSGZo__TIVSBFSH8dj9eUIomA37Xfm8TlS4wnjPzQWqp0Yvvy2jcEyXfIUZal3Qu5vklyVFOnGqDx22Q6V1D4xdtTVNWW4jZSGwqtxunPoP83AlHCSTxp85GpuM_P1VDnRJtXBUYfDMyHfE0HdsaNOFQ8yJSUx1_iwtmJotrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKJ4HzQmGUukaK2SOoS0nZMqIXq1oLpO7eY3wwGSmb-Cxtwukf22u7q0kMUzk5jzt-RAuWt_n8WZAILkqFSdSJMptQIsofkk1VV2t0b__g9shXjxrx502QVekeO2uMrEx62SR15iuXlEW4IiwL0Q7ZWkKc9Jq5Es_fvmTpmJpOzouQUOWfTsp03nImNmMdEjB6O09NSUa8uYYcJLUhtuzu_D8uDEF3XBqZNRHcf70OH7xLM_USA_Rr1KLirlNRSHX8if7bnad9Z3l_T7Gwom45j79DuTfCSTTwq_Iib6lW7kG4oIErYy6nuPgopZ8vWJqTrAyGSAWeRLkNTvmSQ8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Z7H6AxPLkyH08Qs4N309MhQcJ-cfZczl-6AnA7GxAz2qm_AGmdBIHTqAucXON4WqK4aACb3gabC9cmvlX2PnzjO2550JDIkKGrb3OlPNXyRkD2tqBdU5eXp9ON-jv8w3bM7ALNaGiJ3KIUK8X0vodjwcT1JCl7fPkG23hQBA2k0lATISQGAIhXLRQzNQVYnTF99k4uwg7Wt98RiHwGO6GMHydnNfgcKnWnYEuSVBuBQFKL7T1gkWxRWL2lkBaI0Ny9FwFJOynrWsSfiMK1tuWxODNhMK_0ajpYZu02CE32yiVS_Ftg4EVi3SCoUcI0cajLTH8rNRikZU6CJRL4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTKEs0y4J_GsjRjOZY7AbzmvKlAy6uPOMFYRmW1lPTvJlgCJ3Jvtw9pqngLfwOXScTksFiSJPZc6imgv0vrD0BuM1beog2zL3YNHkDB9qpUPddpfqOB_R8fKKZWNb4YyCmWBufZdhWpS6-LmD90ypwcVjm-3X46AIMW8a043GLONKStysH-AnNhshpxb9rWSxafzpE3JhxBQqmvnf0-M4gKETMpweTmdnAi0TSRAROtLoHU7rCQMDKLE3mEZMnOUxoLABN2Qetls8jyBjaCim8G7CuYvJjBOX8HhQLjYkFVJhnWXqKBGpcEZg5MWFPUXBySPpB5dtQER_cz_Jdq7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9LuuOXkJJJ11GtRZ9pNp1zF4kdbQHHlGLDop6TDMS7y97g8_HSOOhVpyy1MsmJKocbNFTnDDXn7f5imiuMb4MoFiCm9Ei2UBSB_mkQLJNhf_f1d6eaA9K54shcZwqCCGjhyzl-4PASTS43QNJ1sUFZWe5GOKi3k1j2pDkJdRzzpgogM6eXbhla0b7rBsovEBbA0qS-FVF3rQw4Hjlb8iB075ez5448hzCZwDLqdYPFL3ubjs4UfA3PhOqxQCK8ImOjwEaraC3a7d-CXgRZU35UWxotshIt3xFvFatUgDx3U9nl8iwFMmkFvMem_3GJGR3Toetms_y7fB_m113PvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY3Q2AHJn5uDtLFColFfCMpe3qaje_eKXc-uoay-xKRgSlvSPnLo3DzewH-Qi0uNscdQCjItqVXI-684BCOb4I-e24tBKcdReWDUq80BHwGZg0aPvccBWw3CeCgxgWNxOzj3mdfQpkiSw3hqc3H6neo8X0ndmmXh-eBpUaDoj_LikZK-K4sX__WYPrAaZn-V5Z4-WE1wnDDuUsM9wZxu_0_ggPxb85S1sdYb9WqrS3n_pzr1MzZvD-ZEgX3QFHXWRXoIIJ82sHmlaVxDvnycXvlsUm2TxuGni_2g80uDbUL5aw0sxX-ZWkhIoM4TooJUdT5yBJXm4koYE7gXp6KlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-fKNRPeTCtuquVXfJDQKeyARlxZMmxbktH_Qh5izyid7wXRfIC5fQG6wmRiZR07BVdFvH9HJOa3IZ3rjz4RyHp1_Mni4v76SJUOr1o82u4oEq0L0qlbXoaZk6ehTdQHAqyx6duw676WBGZ0yjVj7wncIfzA6aRIQs-NIpek1iKb9j_Qu9ju5NfZjm88MIHXs2o11NlvM9I0Xh8z6Z_uV8mNyglCcSb_BKeeeyR6ArbIf5eam_rzDheGgvzh6Y9wOAWwq2V0LuiXJ6nwYKo3XYFDYV7oi8wc-adGqbKVVHt5aejwuZpMFDwrrPQs4uU1GH7CET1Kch8xIkzLe6GlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmHF6i9MvtMumU3JYEPV3rh4akVS-ioXUHiKQhOVn_OfFqhTb-RdgfinHRzhkzfwe068Oc8--RKcCPz-Qs-Jd9WJVe3WvUlqHVD0qee4hl_cG9dk82Mf5zanDJc-KppKBrw0CdAFYXSInPHRyd98lgJ9enPA4ZQ3wSc9klLVhFf-fxpDJNCut8R0LL3jSQME3usw0ZRLkJZRgmt9fdPtAbGWG8IwzkTw1bsNwmm46c_b2WBxYa1npmVchvU1QHq9SnSNh0WhQWpvcLyz3wdM-ziNUXjgP6rrxj8nI3VAuksrR7QUEFYTD2-dKffBPzxSRF8ddHMUoAsWbMBC2NoNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmrQullUvNPFKJ_jAlCT6_IMIuzmFv_MN86i0gh6p4qMj7zgXUPCCyU9y9DHCGju7bwt8BmFwDVCwmH2tSTG_kIAx7sTb8DS8IrjYFSWuNQPtamfwU1uGAwEjSMIP9IOCKvYIq8_Y6l7uk4gPApBsX4fARg8M-bQwn_GF3-BM9lQ48rQjaSXJijLTCZh-dU8L_PaOHN85N8AHRA6e3d0sindLXgFK-e4-WVHWRDQR_YHlxlLNbr0b4Yval6vzKnz5iMhPOHFI8-18tCXQHBLXHlESYkDTv3GhIb2P13_Bv8x9-t_S6c87J3UFL8DsSOlwyK973MdbHLWuauZ_hsBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMBwd9NPsgN0KWsmYkk-alNYbH73ky7Cf1XzAaQbVMmgi-C3wByBWTTVbf4N6MZjgKL_WBT0wx-GpXr0u4hUjl3Q6S02mggocqk7SX_ehhkVFgh_uBEgZa68-OtsAimRyioqG_Wh7TVvJ39A9x2Z8ZIH61mx0pjQIFrpEnUGUEL5WtKZqIFNOSoLNQ7P1CKaLKD6GPQVx1nBos9ljGqmB3rmLdx_uj5vP-snYPP79xoYVXnkNGKIwYTyvTkSe20H1ubE3eNEJ6geeW1HbYu_03EHIoUMBEUqbovbbkWyi0DOGVjqS6-KK6NYLcq2BBo8sPqDHZ_nKvP_i5zMjUDU3EAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMBwd9NPsgN0KWsmYkk-alNYbH73ky7Cf1XzAaQbVMmgi-C3wByBWTTVbf4N6MZjgKL_WBT0wx-GpXr0u4hUjl3Q6S02mggocqk7SX_ehhkVFgh_uBEgZa68-OtsAimRyioqG_Wh7TVvJ39A9x2Z8ZIH61mx0pjQIFrpEnUGUEL5WtKZqIFNOSoLNQ7P1CKaLKD6GPQVx1nBos9ljGqmB3rmLdx_uj5vP-snYPP79xoYVXnkNGKIwYTyvTkSe20H1ubE3eNEJ6geeW1HbYu_03EHIoUMBEUqbovbbkWyi0DOGVjqS6-KK6NYLcq2BBo8sPqDHZ_nKvP_i5zMjUDU3EAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=t8jyVgz-cXl9fwNOqD4FQQV4mzv3vzUbozby93hnVRruAA2F2HWpe8PRgBFJiRmEfpN5RtrS-IyiVB_Wrg_dqePP6_QOkm2p7RI_rh7Y8wQhFdX2NP0EebDQhYdokhuXaARJuU8rzZYRd7fNZogsxfdnL-1Taz5XY_ccy3HfdLHi4P7TNsaCkrGn8fE6-uaVk0SeYEXGf513HYwuQpuls6RB6OIX3IuEpzkPUMNPs7a29jiuMUEM6dc6U8cRp4RcZVHeYg126s3NU2Y49MAMw88VTbqHCZWZ6As4Uhx3ToVXl8SvjcPceGDEJ5MLG1HHYdE28wlguJ1x09dqHFLYN2s1BN0-51s8YzFUvmISDAaL80x4L6kcNEbc4j1upwmqL0iWG9sP660_VD9xu49JMyusxzRs-ycntfieS8uH7MU8_c8GIOEur2KCMmIIFmCVPHfEzx46GshsJJOtsUE58HrdOXtl3pZUweM33GJACFK51tRxJOXzDgZzbs9BhfX35-hfAc3Xdj6GWMoGgkLq_HqEakcWDYcUGUqvfmenL04tmBYEfgpvjh9Ur8g_9iEz6rD0HgLTFKYsDAJtWNJIEvzEW489VAUpGQ6LvPblXBLL2IpqG9Erkuwm7xLjV731dxzpO43srQl-sj2y79rTd24rw1nYXVuosutLNBtgvuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=t8jyVgz-cXl9fwNOqD4FQQV4mzv3vzUbozby93hnVRruAA2F2HWpe8PRgBFJiRmEfpN5RtrS-IyiVB_Wrg_dqePP6_QOkm2p7RI_rh7Y8wQhFdX2NP0EebDQhYdokhuXaARJuU8rzZYRd7fNZogsxfdnL-1Taz5XY_ccy3HfdLHi4P7TNsaCkrGn8fE6-uaVk0SeYEXGf513HYwuQpuls6RB6OIX3IuEpzkPUMNPs7a29jiuMUEM6dc6U8cRp4RcZVHeYg126s3NU2Y49MAMw88VTbqHCZWZ6As4Uhx3ToVXl8SvjcPceGDEJ5MLG1HHYdE28wlguJ1x09dqHFLYN2s1BN0-51s8YzFUvmISDAaL80x4L6kcNEbc4j1upwmqL0iWG9sP660_VD9xu49JMyusxzRs-ycntfieS8uH7MU8_c8GIOEur2KCMmIIFmCVPHfEzx46GshsJJOtsUE58HrdOXtl3pZUweM33GJACFK51tRxJOXzDgZzbs9BhfX35-hfAc3Xdj6GWMoGgkLq_HqEakcWDYcUGUqvfmenL04tmBYEfgpvjh9Ur8g_9iEz6rD0HgLTFKYsDAJtWNJIEvzEW489VAUpGQ6LvPblXBLL2IpqG9Erkuwm7xLjV731dxzpO43srQl-sj2y79rTd24rw1nYXVuosutLNBtgvuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRx-NNyxYm5QIjSQv5C4MR--_QOhgnOGG21bJG2iIwtpAvJYkawbIfLZLfC4rQvdc8bJemfqGuNX-UX4mX7e2HCbJdvHu6lhQajc0szPAQUum5YC7D0tIMvqfs2whygsx0H7dON3p4mfk7gNv_iMKNI2K7cV_KI5zpngeXG_5u5ld0rySEPHnoU8whptT_jFy9ZIVQQknBHNpXPo4ZLrxgTdh6SsCGZMhfnT4JeN8jo_h_CXRBPICieGY4SaRxn045O425gmMm35U2Kvr_stGpJKmtTRZhhCXO0awPjIFlYeruoLfnl645D3QKgsBj8x0f4n-lZOVi9IisP6xdtKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=Qg04ExfR_x_JtUrKqeS004OGlgf9-N1JyahQk5Op1vSGayFS_V2TytPprHXNqSaLLwhN_aQ5IpxYLsD_7p6wlQO_F_tqKxsS0yVlkLKr02MVnDiERdV5Z4yOii07qUuh-Ak9_u_7LvBUBe9FStva6nDNQdaergZXzmqqOF1wCTP5v0EtTk7LlMfs0tjPAOUobLGH6QbLzFreTzF0xrvOX9uIDPVddFgD5Ql33B2VM9KA0lzKfa6Pwz5UJkPafwQHl_tjh-cMHfaZEOhzd7dgIw_1FyVI1buC5dsmnVOwhO80IqNTAMHRlozKqVriRmkThl1bjoGIxjY0sOhErNuy9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=Qg04ExfR_x_JtUrKqeS004OGlgf9-N1JyahQk5Op1vSGayFS_V2TytPprHXNqSaLLwhN_aQ5IpxYLsD_7p6wlQO_F_tqKxsS0yVlkLKr02MVnDiERdV5Z4yOii07qUuh-Ak9_u_7LvBUBe9FStva6nDNQdaergZXzmqqOF1wCTP5v0EtTk7LlMfs0tjPAOUobLGH6QbLzFreTzF0xrvOX9uIDPVddFgD5Ql33B2VM9KA0lzKfa6Pwz5UJkPafwQHl_tjh-cMHfaZEOhzd7dgIw_1FyVI1buC5dsmnVOwhO80IqNTAMHRlozKqVriRmkThl1bjoGIxjY0sOhErNuy9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJvhEqUoIv-cU2A2izuLeP8w4Dkpyckw7PShJRHKc2kGowkg22a1K_SBgLu8UyWHolVDdgVk-M4RtDHlQ0oOu-YcZEtMgc2g9s5uxRIqy-wpeUVLLV1iPzdw30l-w4RfRjGkizDWHeiJ0Kdh0v2ASuk6bZbCcJXjwV18YDzEdt6ETEPr95r-BnVFcFo2Gi2bHDRL38hPs_-chPEVwBfaRRhLEdDlckVL-WGJ8TK_2RfzQJXktPjGFBunOrctioi2rqKACei6ad5Eus3e2tfhuGTmD3VFrFCNCd1vaTNsvYbAQvL2YvCZqOAimA03oWXiyWBY0540JVzh9cUIAZTxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snv3LsVqpySOHc7kE6cchvx8w8r54MJKZfjrExVd_PagMHb1mNdZB94xDWgSi7yDmPrm1AWuGU3VDIxkkrujSlcus4HWPdBd9XHmozRAKCA8U5Rj9B7HAh4FoImSLuREFLOWSIQiHY2J-MmIB33Lnm-bjKL-TnTPvOk4OcyXlmk_lgHSWtYr6A4sQghk0U0dlPqegPDZSGj-RPA19SgN5qdRp9QN_DMyeufDTOFz9Ul94wStc0xCu1IM-fN265GGCsMbMblY-iweHjPOItooB-9qn60bZ7FoPk8h8bhNofZ--5EqgYU2GyM_t4KZRClIsSldwL7toytcoNSKVI28VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=uBrioe_1FWlX8Q1ikP4oaJ-kz31eKf0JoK-_NVXEOd9rmvcxBYuwKNn4DqDxXbE9Us_q_H7ZgDbWjF64PuHBaU62yuSpRd2h65rWMaI5JYvP1Y5Kfz9qTJEBDYFr4kcUoWaD69ydcFfQPGyxvG8BD5p8O7NxZefSN2LTe0tjPSCjgffEuStfag32EI3KlHxoNBSGG6uhhwiUH7Yjlt4uN7NkxXtVZNnjRuI0AMdRE6JKZfpIiDKKvi0WeH_cOUfuafaOMd1cea-XfV8sc0GY3GaAPoweLSebrBGaygJSQQLVgRj3UD7sEMpAhFi1IHTq70bLqn2_blcVDfN_Epr_4nHqJ2BZ8zKfiF_cj911IoO6MJYAY8eV8W60cBjTAemClAJ7hlqWneBOQPy28fh4i2-ForOF5OYrFq_y7UiIctzjrSd3qYPhpcrA2BknqjOXzz9_MzpF4Pxax5TC45R67aR2l0FxKNlBUbUVM86TY14t7yHnq6nMLpJV3fB7ePt4zdpvFhZGkpNSfUIm0bLnca2tJRFAZWpaGd5nhgkzGlh9QJZt5H7pryVFWbkVFXeG-xsUiajT3-LVbdx_zHXPbUR7ZJz16RvHPPfyF-Q50GM5j0pedYlAFG8tOGOj4bxEmbtCWBmM_5oIfTtoxgaxi8ipkMwQN_vR3EPpMMlPej0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=uBrioe_1FWlX8Q1ikP4oaJ-kz31eKf0JoK-_NVXEOd9rmvcxBYuwKNn4DqDxXbE9Us_q_H7ZgDbWjF64PuHBaU62yuSpRd2h65rWMaI5JYvP1Y5Kfz9qTJEBDYFr4kcUoWaD69ydcFfQPGyxvG8BD5p8O7NxZefSN2LTe0tjPSCjgffEuStfag32EI3KlHxoNBSGG6uhhwiUH7Yjlt4uN7NkxXtVZNnjRuI0AMdRE6JKZfpIiDKKvi0WeH_cOUfuafaOMd1cea-XfV8sc0GY3GaAPoweLSebrBGaygJSQQLVgRj3UD7sEMpAhFi1IHTq70bLqn2_blcVDfN_Epr_4nHqJ2BZ8zKfiF_cj911IoO6MJYAY8eV8W60cBjTAemClAJ7hlqWneBOQPy28fh4i2-ForOF5OYrFq_y7UiIctzjrSd3qYPhpcrA2BknqjOXzz9_MzpF4Pxax5TC45R67aR2l0FxKNlBUbUVM86TY14t7yHnq6nMLpJV3fB7ePt4zdpvFhZGkpNSfUIm0bLnca2tJRFAZWpaGd5nhgkzGlh9QJZt5H7pryVFWbkVFXeG-xsUiajT3-LVbdx_zHXPbUR7ZJz16RvHPPfyF-Q50GM5j0pedYlAFG8tOGOj4bxEmbtCWBmM_5oIfTtoxgaxi8ipkMwQN_vR3EPpMMlPej0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=QjsLo-SV8shHIrjUcjPrOgcr1GTwdeC_iEaiPgdXP-RL3uiG1ej02U7IG2-uf3Dixdbgt70gVUCAe_FjHRWTykq6cUBW6h0-0BazSPzcTBkHxDqYF6tM6xstw8RiQ7b4rG6BClWM2lSiC-_L7DxA4hJaom5gYY7DQUpJ8DE4nUfHY06WUn_wQziPlxf6KIgn2t6asalOB0NQf0pAeGM6CSRBAH7lw-mUt1EEUWwGToNQT9e9rR_3RV6e3Pvhqaai3OS84Vt5vVZBcZFLtmR9fWWqJzqRbktQwelJpySEJD3xPBDb4S1eY9qg_ZW65hBRxFVyMuPQVPNN-E6-eLvshEaQyh4S1i64VUijh9wCKdmNzMIjxwTdsI4ccW9cHoE5hmJ4sXBJepFUOtWUhVcR9usJUD-ekLMMRKyz7a2NZz1oKLt5HYHZe0WNx_dPZwz7lbSZNSInRFfvM1ZoTLBkABQpW3vg-FlkxFUIEw_i3I0Cqz8hKXsvkN7HqyUJNBmR67vJM9fVlqIh8Dxpgcr--wZaC0lcKOLehunWPdWe1hKvuM66eZvBzPWkRzEpq60tRclwwQo0Fddx1s9rh_xIGegoWGeykkMLZXanNRbKcUTDox2fPM4XiOO8fUNbVYeUJaKYw5sINgMIxtizzvcxbM2IjQ10onrESUjM_fdfFJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=QjsLo-SV8shHIrjUcjPrOgcr1GTwdeC_iEaiPgdXP-RL3uiG1ej02U7IG2-uf3Dixdbgt70gVUCAe_FjHRWTykq6cUBW6h0-0BazSPzcTBkHxDqYF6tM6xstw8RiQ7b4rG6BClWM2lSiC-_L7DxA4hJaom5gYY7DQUpJ8DE4nUfHY06WUn_wQziPlxf6KIgn2t6asalOB0NQf0pAeGM6CSRBAH7lw-mUt1EEUWwGToNQT9e9rR_3RV6e3Pvhqaai3OS84Vt5vVZBcZFLtmR9fWWqJzqRbktQwelJpySEJD3xPBDb4S1eY9qg_ZW65hBRxFVyMuPQVPNN-E6-eLvshEaQyh4S1i64VUijh9wCKdmNzMIjxwTdsI4ccW9cHoE5hmJ4sXBJepFUOtWUhVcR9usJUD-ekLMMRKyz7a2NZz1oKLt5HYHZe0WNx_dPZwz7lbSZNSInRFfvM1ZoTLBkABQpW3vg-FlkxFUIEw_i3I0Cqz8hKXsvkN7HqyUJNBmR67vJM9fVlqIh8Dxpgcr--wZaC0lcKOLehunWPdWe1hKvuM66eZvBzPWkRzEpq60tRclwwQo0Fddx1s9rh_xIGegoWGeykkMLZXanNRbKcUTDox2fPM4XiOO8fUNbVYeUJaKYw5sINgMIxtizzvcxbM2IjQ10onrESUjM_fdfFJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=lxlMGFVyoSDrGN9DcgdO4fdYLAjdVvyZT58BD56Z8MU69id7DvaIL2TD-CuJUKowKxVoEb92iaVhLjJCIsigd4DlyYfulgfhwQmHM5AwFP1xFn-cCKheC0p3lXTti_sgSGMKG8f_YcfsmxAAwuApe5dmnWOmq_lGQUqEEj6FPOgbhQae18WTRorkIvuTR2M6DS_ZsuNKPezwF6pqekBgfhhNu3852O1WHKKZXKJrZ4IQUduWV59IV6jc1FVdgbbTphKXbNv0UTum7tcF6akVlXDaARVMydZysXmv8fsOhxmQOAdUi0OqGvs3nAkq6WBlf-wOxqLJFKpToJgia0OIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=lxlMGFVyoSDrGN9DcgdO4fdYLAjdVvyZT58BD56Z8MU69id7DvaIL2TD-CuJUKowKxVoEb92iaVhLjJCIsigd4DlyYfulgfhwQmHM5AwFP1xFn-cCKheC0p3lXTti_sgSGMKG8f_YcfsmxAAwuApe5dmnWOmq_lGQUqEEj6FPOgbhQae18WTRorkIvuTR2M6DS_ZsuNKPezwF6pqekBgfhhNu3852O1WHKKZXKJrZ4IQUduWV59IV6jc1FVdgbbTphKXbNv0UTum7tcF6akVlXDaARVMydZysXmv8fsOhxmQOAdUi0OqGvs3nAkq6WBlf-wOxqLJFKpToJgia0OIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQjypZjV5LdrU56Y6l4rnRIeagdczfPNQlI4OWgTsoxi7JfiI4v50VTEisRwwX5dSl1Rbm97GQwGeaYzRdyvimXxR3-LVjPshoGNHiZT-r1QsEZWeASTBJMiTvylCR_a_IbkZKfm-SYnpOMiFhrWLb-c0KxCWrj1NcdfIPfcAYigUeGqgK1AknvUP7fkKtNEwKMO8OOYwbISL5xDfmGmsb6POinBQQ43hsb4YIpFDSAcGhLZ29ucCdZ7CoeCzbl0k_EKBw0ZFnnu7W8JNC7O3LHGafMArB3EW8J_0pVFYdCQTWTERy4828amiI_iaMdX8Ck20V2o5V_7xpXgSafHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=JyN9RkWJOHu9cOF6OJxpTALT8NSgfHGaMDg2qFObfkW5_NY2dRwioblXqHUXwKjyB70E_qp0_3E5vLJsJ3O-yJ7MNOgVqi90ivbMKYlwO-5R9njEJVoKNavoGqkxNIrjYohh3W6UtNKUbYKJ1LZNGdySh_nZ2MPHTM1ZiYaMQlshN65cADstyArW-B3OOuJGm_NB9Re4lPnEBBe5jMvh5TfH8zUH022RMUjqTS42s4b_VGLkRijF8tn-pZQbZBuU-dIc-97tfmvFvVCHEiosNu_Vx6l-6KFvdgy2wDRuaTnNdTvqfkoFAKFWogEp2P1akarSo8CI7dFgLm1mXEEhIW89dP_hr8J4G-z0glKtkhyj_rgZIM5W7Dl5SwvVQEmEqmw4uYrbsujK1xRVrpvFEVVrnU9rzt5FPt4NslSKNUE01Oxf6KW2QVM73HwPQuD9c_2Vfle82xErpYSV1ko4K3ylQp2NKCQKqswERNl3OFxrih-q3n1b_RfbxnzWjXLtz60xOf3Ei20IA9osleotS-wLE2QysdhTn70A777Jn42OJ9k5O_cUcB6duSRJyTGayU0qqt9dQtChXLefLGDakwgmZpy9xNCKsTJXF70R9DgEhWsOp7jcpe7Cr-qqPq3jU5jjYNGIxyyjf535PThic0ZMqjBCdEMbwxbBG8YBeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=JyN9RkWJOHu9cOF6OJxpTALT8NSgfHGaMDg2qFObfkW5_NY2dRwioblXqHUXwKjyB70E_qp0_3E5vLJsJ3O-yJ7MNOgVqi90ivbMKYlwO-5R9njEJVoKNavoGqkxNIrjYohh3W6UtNKUbYKJ1LZNGdySh_nZ2MPHTM1ZiYaMQlshN65cADstyArW-B3OOuJGm_NB9Re4lPnEBBe5jMvh5TfH8zUH022RMUjqTS42s4b_VGLkRijF8tn-pZQbZBuU-dIc-97tfmvFvVCHEiosNu_Vx6l-6KFvdgy2wDRuaTnNdTvqfkoFAKFWogEp2P1akarSo8CI7dFgLm1mXEEhIW89dP_hr8J4G-z0glKtkhyj_rgZIM5W7Dl5SwvVQEmEqmw4uYrbsujK1xRVrpvFEVVrnU9rzt5FPt4NslSKNUE01Oxf6KW2QVM73HwPQuD9c_2Vfle82xErpYSV1ko4K3ylQp2NKCQKqswERNl3OFxrih-q3n1b_RfbxnzWjXLtz60xOf3Ei20IA9osleotS-wLE2QysdhTn70A777Jn42OJ9k5O_cUcB6duSRJyTGayU0qqt9dQtChXLefLGDakwgmZpy9xNCKsTJXF70R9DgEhWsOp7jcpe7Cr-qqPq3jU5jjYNGIxyyjf535PThic0ZMqjBCdEMbwxbBG8YBeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=mQ6lBmve9lsFyyQBrCJqm2LOoDjqYwNQrDlLfyXtNQrWhwBiULLSvMqy1xQt-SjJcxtt4sFDSSW36HJMTqVgSXpsUjp7_pXv45cgOCrqPz8lpA-VjMSvL54MAbCn0MAc1pAjsJ0NYAavkFo5yEb4J_mpDP6BLmeJpOiAtENx9gaipZOOgGV7aDtwM4yPjcwJ5uuoBauyTKoeuD2Zn1wODTazXfPqFloOisTesa5DFfNn9pETYR5IJzPcFlH5VFTNReP40GEblthObX4uft4RM1qHzaGKpn7_G_RuJl7BdIrnxj3ULtAfXIp-KIgax74FU_Cn7pdu8RW71K1f0MLtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=mQ6lBmve9lsFyyQBrCJqm2LOoDjqYwNQrDlLfyXtNQrWhwBiULLSvMqy1xQt-SjJcxtt4sFDSSW36HJMTqVgSXpsUjp7_pXv45cgOCrqPz8lpA-VjMSvL54MAbCn0MAc1pAjsJ0NYAavkFo5yEb4J_mpDP6BLmeJpOiAtENx9gaipZOOgGV7aDtwM4yPjcwJ5uuoBauyTKoeuD2Zn1wODTazXfPqFloOisTesa5DFfNn9pETYR5IJzPcFlH5VFTNReP40GEblthObX4uft4RM1qHzaGKpn7_G_RuJl7BdIrnxj3ULtAfXIp-KIgax74FU_Cn7pdu8RW71K1f0MLtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzS8csY-apdIvMGUPZxKDONyDC1JjhBIKAfehkgD9SmDiKHcOe_JTORjhzNJQ-ksJx2mxA1_RCZI0ymIuA7f9hOwee8YFzazDfReMfYJmZP5G1kQv6leG_hFSBO2UeK2ieuM-JbAvBLYG_mE5y4EVnH_kVp23A0oTAE760qtTVTtVH26L2ZcVIC9QB8gJ65AupBrpniWtdcX29uqT22_DTloIUi-x7M-cp7aI7Xz6kmN0bgupQRfi0psOGxHQHyI47nHsaPTMQYpwQ5YQ17wVdEeC4V5Zes6IsPaKNTmXF_iacInWXeP0ecN29Bw9acMZIYOFbuFVahnpuLmeWkRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTV0HfUKjYd-sFsYsIzffG3bhU6ULbIJDX_S_z09595OQRr7fFHeTG9ca75HaTiFm5y0MysWqqnL8wGA6eqSVvEM-1YtGr19mPl9vGF1hCbtXuF580cUFD6wDz33SEMKyA91sBB0VpuYnNPqz15jWwYfVBB0l81nxrFy6-iGp0VkQSlh0Ljkwn3SnXugL6jcWdIvgV4tOdfoIUEWuXyJy1sXFdwIwJjTxh40Zjb7DgSrczLmYahlMU8d9yQ2PnInAWLBegXcrQLCaZFWO_MfaPE6nXNvy81yGHiiCMfSX5Gr6Zz8cKpSqpirNMnRr-zHYmNkDfihPazIVyiuO5v_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDQ7Jmcah1yDY6NVhF6JqnrpW3t6kdPXJAzNdimHBw_7mjU1MSezSnBXrhMa_VFDzmJ2WgIkWiTIaWasYjg2-CE9LdEVZVSLKubaZTn21Mcd0g0bwFWauVhC-ShVmXTW9wxrWXuJsIcmYEvAKiThuWjUbc7BXawSf42rW730pYPE3WZaGebOQb-15voiqTZo4963p6lH1ytAvcRBeTVm8nlLB5vVs6FcsgORMlpn6qlZAgRKNx50CB7wINBiEdtmT3WMhtURRIzNwQ3qSNSHTXEXna3gfzGupHaT-0NSmk8QrfUkeIz9T-seSHtUP5cyIIbSJqkU17SZhk96vesWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JndwxTOHekxN29ZejUMDbHV4h3djZpKTzsE2olHH9U-8kMA6IOysZIVyBBjDBwRsj6OLBmuDocsE5lxpk38OMEn5-8z3aSsF3F21AhrAQNp969xRgR-Pkgf90_EB8ZA4bB0zmHgFl5DA4r-AAh7eWBET-_XaMR3tPGuJzIl3JfJxk0ujbOh01juuq7UeEt6YjimCb42tFAgi7UB8qTbqxyTrzYmfTim8mEj5Oo9Njk5qDosbCCN_AGrNwxv8UYInrQSPl5a-r-cTj6c4GnNOsBsbEid883QwaTMaCpGvwBpYvwD-XOLIQs5jQuNk7MNXtlBE8pF_urvykJXXP3x-wPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JndwxTOHekxN29ZejUMDbHV4h3djZpKTzsE2olHH9U-8kMA6IOysZIVyBBjDBwRsj6OLBmuDocsE5lxpk38OMEn5-8z3aSsF3F21AhrAQNp969xRgR-Pkgf90_EB8ZA4bB0zmHgFl5DA4r-AAh7eWBET-_XaMR3tPGuJzIl3JfJxk0ujbOh01juuq7UeEt6YjimCb42tFAgi7UB8qTbqxyTrzYmfTim8mEj5Oo9Njk5qDosbCCN_AGrNwxv8UYInrQSPl5a-r-cTj6c4GnNOsBsbEid883QwaTMaCpGvwBpYvwD-XOLIQs5jQuNk7MNXtlBE8pF_urvykJXXP3x-wPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0SixG10xQhW20oi8W0Bi0w-9aejKfGe_la8Xxz1BMSUfFTG9zfNwakOtmhKSYbhdlIgRQPQtUcykcpZAljxRZBqMB98R2hxkL06XKoWxOj02HjEiZHBo_nPXutvPbSbsNYX9NjrDBPiasjpoScOL_FIiwYAM6z0I7OByof0wdrdKJjLnG4Bnp73gVEsOtV-uAWXt9TIwkHzdW0AeHPj1OBBmUqALly6wqN6giq1Vc5ulaK8TExhE__ELw1jS0Mm32Rjvjf5f4D-N4t18bqofejcwx1sGWsAEcNZcQmk1VGcP_Mb3sLdPH3ZEOY2YOB7PbTqaJJfT4BvgrfofN31Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=puy2fGvi6j2KejF44199UKtZiX9lsH6QYjn3jpnRsq0QKyXuyCuhBxrcu-pY0oZzvsvaR6jqelCo2wbYlPD_VWFHakwM1VX8Q7m0DFWNWq5U4OHi1ALZj7knPJssZmouiu0B0KfY4vjiYxgbjSiCN1iA7HJWe4V31NDLjhFoVEm6p_qaRDWSouQ12HO5PhivaWJhrWM3857KfKxuVcfAU9oAEMAgbHD9d5lPBjMh-K-YqBy6vK1FNzxFF1OpumbmwQygbVtrjTFAZY5X3KWoCM0zHUVwhI8bZNTG2jLh3fh5kyp2jjSavN_tAS_VOMbhlbnI4XbnbwZxUMc0yNB-oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=puy2fGvi6j2KejF44199UKtZiX9lsH6QYjn3jpnRsq0QKyXuyCuhBxrcu-pY0oZzvsvaR6jqelCo2wbYlPD_VWFHakwM1VX8Q7m0DFWNWq5U4OHi1ALZj7knPJssZmouiu0B0KfY4vjiYxgbjSiCN1iA7HJWe4V31NDLjhFoVEm6p_qaRDWSouQ12HO5PhivaWJhrWM3857KfKxuVcfAU9oAEMAgbHD9d5lPBjMh-K-YqBy6vK1FNzxFF1OpumbmwQygbVtrjTFAZY5X3KWoCM0zHUVwhI8bZNTG2jLh3fh5kyp2jjSavN_tAS_VOMbhlbnI4XbnbwZxUMc0yNB-oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=O-MUAxBHijEPuUxGa6qZGLOvjmFEbDlSeE2Q8xbmJoZ2Gwhl6Z6eKOR3cSWMyvN3vkabUBh6uHkbNnGtbS-Nd4gp_Mr53smh78yJCQnn0xo0e_c31LEiE6hJ9-qfBhYk63EwxwNo3biah9WadLy6MO-EeI3dFgVrPbQ6xM-Boghq4X1dic9qGuiue8FtFQi0Mxj7Un9Zr_X5JxN4GMTGKAf-c7Gaa65p6fYJiMxyzIRRktgYQTsmfH8Js3Arq6lXr3j5L8tK0o245-9kZPForD4iPMli6tbckz6mXK5hfVHLt4ql8JD4REk8zS1rI2s57rV2tw47gzW7TZ_IRbsrorSqIhgpUNxW0VBwmJkWMugQRjFLWC34VfeG5OjeooDdpqn90bwZRHDflDFT5WWelNTvNJNMB-4yvwXLNChWCTjqy5eklGjNy9j36lbFuf7LRyaNuq8l8SCP30XQsX8xxMlL7z-3msyx2q8zDnIyjaWbys5rfXLwFhqgs4cfb5t_4fsl0b-n4dmL40lGQCmfMr7tWKeJDpIxJlYjnyQ_jhPJzaMII19BhtTw-LTmU-U3Rq99xKpGZuo8jnGSPFHBHzFDskLF5S61EsGxb-NSU7AKIrmvvn0qoIb3gKzacTAsYhxKT67XJjb4mPLqZNXUnu6xvcXSHcHhUxMo2dqTTVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=O-MUAxBHijEPuUxGa6qZGLOvjmFEbDlSeE2Q8xbmJoZ2Gwhl6Z6eKOR3cSWMyvN3vkabUBh6uHkbNnGtbS-Nd4gp_Mr53smh78yJCQnn0xo0e_c31LEiE6hJ9-qfBhYk63EwxwNo3biah9WadLy6MO-EeI3dFgVrPbQ6xM-Boghq4X1dic9qGuiue8FtFQi0Mxj7Un9Zr_X5JxN4GMTGKAf-c7Gaa65p6fYJiMxyzIRRktgYQTsmfH8Js3Arq6lXr3j5L8tK0o245-9kZPForD4iPMli6tbckz6mXK5hfVHLt4ql8JD4REk8zS1rI2s57rV2tw47gzW7TZ_IRbsrorSqIhgpUNxW0VBwmJkWMugQRjFLWC34VfeG5OjeooDdpqn90bwZRHDflDFT5WWelNTvNJNMB-4yvwXLNChWCTjqy5eklGjNy9j36lbFuf7LRyaNuq8l8SCP30XQsX8xxMlL7z-3msyx2q8zDnIyjaWbys5rfXLwFhqgs4cfb5t_4fsl0b-n4dmL40lGQCmfMr7tWKeJDpIxJlYjnyQ_jhPJzaMII19BhtTw-LTmU-U3Rq99xKpGZuo8jnGSPFHBHzFDskLF5S61EsGxb-NSU7AKIrmvvn0qoIb3gKzacTAsYhxKT67XJjb4mPLqZNXUnu6xvcXSHcHhUxMo2dqTTVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=gp813uLm5o8XLcXb6C6-Wl_rYpv348PEqcVOxnJ2T1DCAK6OEdIIt3crk6NYM42eOHu_Ncys2v7uNwfyxsP5KrGx0jQrfW6C3ciRzjgdoI_Apmpbco2-QpcgOXvZ8xH6podv9qgNh6Uo2D7_c2f7sLE9hBOTrzXVfeyUDJM9nf_t6yOLDc0rjK6-xpcmN5uU7Ol0Cnw4Np5binj-ARTFrjZQM5xSpJi7xNv2gkQt8gxulao_KpmWXTAQGRuDpkjXoCPprYOgJUIiF3v8zsHDgG6T2JRjXkGiemHPiwUwg44TnzGsV6HtWhV4ZKgYIa9K2jQwvEoQJN2zWaqKg5YtFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=gp813uLm5o8XLcXb6C6-Wl_rYpv348PEqcVOxnJ2T1DCAK6OEdIIt3crk6NYM42eOHu_Ncys2v7uNwfyxsP5KrGx0jQrfW6C3ciRzjgdoI_Apmpbco2-QpcgOXvZ8xH6podv9qgNh6Uo2D7_c2f7sLE9hBOTrzXVfeyUDJM9nf_t6yOLDc0rjK6-xpcmN5uU7Ol0Cnw4Np5binj-ARTFrjZQM5xSpJi7xNv2gkQt8gxulao_KpmWXTAQGRuDpkjXoCPprYOgJUIiF3v8zsHDgG6T2JRjXkGiemHPiwUwg44TnzGsV6HtWhV4ZKgYIa9K2jQwvEoQJN2zWaqKg5YtFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLhbEwd0q0uiEBfGeTtVV3dC4QpsLfDYbzdLzBn-0NUT1oJpWaz-pbSd0ghJFuRWDj03iMWkcqT5MYGZQiv-QAaeYxcMLNuWQD1AdsrVn9rcb6sCM5lLmEENuQesLB7mMZwNUQmh99V42p37W3BPHCFIKnvWuV2oV1HZDnXmfp0wtuKW3_gy9fwsS4l6zx3no4G2NSG1fiQDfnvPr-rxtDZ_96-M6TQ_B59s3s6c-TOCvCB2Xv47uKgutE6tggdMBVp4fGtECtMBroYoHMksTfueBmugFDfjMi8XwxJlXY7v7RJUuehat8uUa5iUgq8R5vYHeDcRJyhLH32bCLjjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=XKd4KDVYbpD9rH9a9RwVXZ5A1iEenKH9ceRn1dcWz-0V28BMuzUahwaAvP__skjwOGbE_E_kITyughXHlkdrzOTX6eIhhQtu2K995cZWzpaowWlkcuQURFy3pBeldi7757HLPkj3pGFctLU1rWbVrhk5LF9NcPZMJvWuHVUk-FvVXxWhS8GtXppXo2GbREr3IjyKi_INJYNa5v9ng35xYuYYw52Xm9GsgMuf7voFFjBIFLYBMWL7Y_mwlkTrAWKqJaKqxHHi5a5T2BywuCiG-B4cB0t29popEHjvsQtPCprtM05Gcl-R29wdZVGKr9cb0PwzBPCBZenEQO5oL_5T1HyOYmqOseKAAT6ENUPl76A7YPr7J93hjzO8PP13YA62qLs9rqlkH87rjUcax7eNWYx0OUmgWm9P7BUJd0y67PE4bZosdtXjrE0N_sVex07bOGB0et_Ky_gNLDQ2en0_yMivXmtk1npA8V0DHyJDjsDIaohfg5mPqDjozlaqQoZS1Cl-4ocFkAMAAuUOwhp2RNFIZIA5FFhTMUOk_4ZHqPZkPfupOrJ_vOgLG8nayT-F7RwE6GEuC5Lchn7vyOwzuorHPUgM_lGdNsosLdtBGGfKfxS7eZv5rOU3hRSneVKkgtPloMm8xlJ1B-Urx6vW85FP-2PYMKdOSBM5U89US6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=XKd4KDVYbpD9rH9a9RwVXZ5A1iEenKH9ceRn1dcWz-0V28BMuzUahwaAvP__skjwOGbE_E_kITyughXHlkdrzOTX6eIhhQtu2K995cZWzpaowWlkcuQURFy3pBeldi7757HLPkj3pGFctLU1rWbVrhk5LF9NcPZMJvWuHVUk-FvVXxWhS8GtXppXo2GbREr3IjyKi_INJYNa5v9ng35xYuYYw52Xm9GsgMuf7voFFjBIFLYBMWL7Y_mwlkTrAWKqJaKqxHHi5a5T2BywuCiG-B4cB0t29popEHjvsQtPCprtM05Gcl-R29wdZVGKr9cb0PwzBPCBZenEQO5oL_5T1HyOYmqOseKAAT6ENUPl76A7YPr7J93hjzO8PP13YA62qLs9rqlkH87rjUcax7eNWYx0OUmgWm9P7BUJd0y67PE4bZosdtXjrE0N_sVex07bOGB0et_Ky_gNLDQ2en0_yMivXmtk1npA8V0DHyJDjsDIaohfg5mPqDjozlaqQoZS1Cl-4ocFkAMAAuUOwhp2RNFIZIA5FFhTMUOk_4ZHqPZkPfupOrJ_vOgLG8nayT-F7RwE6GEuC5Lchn7vyOwzuorHPUgM_lGdNsosLdtBGGfKfxS7eZv5rOU3hRSneVKkgtPloMm8xlJ1B-Urx6vW85FP-2PYMKdOSBM5U89US6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZX8S4kohqZxYq9jnBm_8AuwS617Hjp68VR4Zk_NwU8W6OYbFhrWoyr0-ZIA3epgGJsJcWXHeuXaBvVejkCZDgWuT9CxLLQ_12xBHRohB1uAgdC_s1v8abBB9iUPRWi0hbmXbE2IU1jvLgk83AD2GjyWsnhLVcenhWFj9dPBwUu3hvr2la-q6Q17CvbL93jR-LgkYRCe-6zzXvO5Ypi890sLrvkU23T410KX6d2Zb_REdYmOhex21YZGVStxdmkfylb93EzCVgPodjTYIwvZ79KKR1Cso4xXuRv-bFFixR8xeRhnEOv1GN_nF57cN9G7I15nc4TD4qPgknMpJ3-JDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZX8S4kohqZxYq9jnBm_8AuwS617Hjp68VR4Zk_NwU8W6OYbFhrWoyr0-ZIA3epgGJsJcWXHeuXaBvVejkCZDgWuT9CxLLQ_12xBHRohB1uAgdC_s1v8abBB9iUPRWi0hbmXbE2IU1jvLgk83AD2GjyWsnhLVcenhWFj9dPBwUu3hvr2la-q6Q17CvbL93jR-LgkYRCe-6zzXvO5Ypi890sLrvkU23T410KX6d2Zb_REdYmOhex21YZGVStxdmkfylb93EzCVgPodjTYIwvZ79KKR1Cso4xXuRv-bFFixR8xeRhnEOv1GN_nF57cN9G7I15nc4TD4qPgknMpJ3-JDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=XRXArjsOMldpzw7KW7Y9gcrkyx0Bxgx6KcFn39VQ0kBgPtyeDQOBnbkMglkcPI88iw3Uj8JCaWWxHbY4jcmHAhcjEFlw96DLSoXFj9HgE5lPW1KVrFPxoCoNWpfNBMJQ2n_5oKeHj41dtyHZpuFC9EMd3BN_9wevgn8iL3dgeb4e18Jat93NztiSJa6Kd0DFizoL6dC3UoX4b7ghid0YZrha8Mn8p2qZt82Z4WJ6z1C21nJ157Ofu3mEj22dY6Aqo5Se5XNhTqRj8xwyhuOnw-py93agm_-ocfJ6BgUEFZX-5_YcfC-uIq8VmynN7RENdCdRefC6K9sGyilrAQwphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=XRXArjsOMldpzw7KW7Y9gcrkyx0Bxgx6KcFn39VQ0kBgPtyeDQOBnbkMglkcPI88iw3Uj8JCaWWxHbY4jcmHAhcjEFlw96DLSoXFj9HgE5lPW1KVrFPxoCoNWpfNBMJQ2n_5oKeHj41dtyHZpuFC9EMd3BN_9wevgn8iL3dgeb4e18Jat93NztiSJa6Kd0DFizoL6dC3UoX4b7ghid0YZrha8Mn8p2qZt82Z4WJ6z1C21nJ157Ofu3mEj22dY6Aqo5Se5XNhTqRj8xwyhuOnw-py93agm_-ocfJ6BgUEFZX-5_YcfC-uIq8VmynN7RENdCdRefC6K9sGyilrAQwphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1o1AkIKNv0MDltdQcgDiOrurGk-_TIEtwDrPHlWQNsUYcoJygoDE7jQRCG5RIeCbRKCtc5Fn0vXc2XDBK78GJhkI78kKADzbqNR5vjXwwX4wXH4jYI9zMwtzS4O1-Qi708fm5hTKwLegEErTMmofl00_NLWUyd-vlb1PZd-ADXmMTcNgavQM9oZHyrTVNbUmcWCZKe0WoG9ev0_tYvUS2cfgc90C578kpM9YssDp0-VByYjfPttwxj0i3bppx6KoTlQq4o0GlpZ_4CNuuWdI-nbA2R78JDSzmg2JeeD5ZJct-Yh6k91NA6QlLZqQOyMB-JpF0Vr4WEkvais3SbJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=fQZIAj2CYxrbr1X_V7dKBl9vBjEk5OsIWP0_mr0pDKy_xiZd0U0QKPhPqbCENquS_NZlI65X3KJ7mEBcVsJeTd9ZSXJNN_MYazJsC92WVPRme_yCRdPK9OvaWExHynfLOJmOJrRx1LQa8Xkop5A2pNMka2pbMdqapkzOe-K90qcD7S7TZFlCN6jActU9dwA9EoHdykwT9By_AmLh2c0A2-y_rYFjTyqKlHnzgcxl-QTWHIkOoS-i84YhBuziUCGYy0nTwFMN7WcjzW_EmyaJT3A4lMySFNAE0bycmZJVd1OD2jTHHAMAdlitBF21l-KfNcF48UXtEju8v11R5brXbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=fQZIAj2CYxrbr1X_V7dKBl9vBjEk5OsIWP0_mr0pDKy_xiZd0U0QKPhPqbCENquS_NZlI65X3KJ7mEBcVsJeTd9ZSXJNN_MYazJsC92WVPRme_yCRdPK9OvaWExHynfLOJmOJrRx1LQa8Xkop5A2pNMka2pbMdqapkzOe-K90qcD7S7TZFlCN6jActU9dwA9EoHdykwT9By_AmLh2c0A2-y_rYFjTyqKlHnzgcxl-QTWHIkOoS-i84YhBuziUCGYy0nTwFMN7WcjzW_EmyaJT3A4lMySFNAE0bycmZJVd1OD2jTHHAMAdlitBF21l-KfNcF48UXtEju8v11R5brXbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdS_5Rz5UQH31r_EHfx0syIEIrDlgPwZxxrP1vla5qKO2GeTe4vNuteyaT1tIy5KDDCRLIDdOewKpUq6Z1y_rilri9SIJZHi71-PU7H7LpHrKfsvXiAFYJBr16Jm4-33iK_xieFtKOtBte3FkFqD8BzfHFyU_RK7HaJ-hBnHcyDviwlZFDbj5y6YyjSLJNKWCjtb_GLaxtNbxPtatedWyakZg0RkAtYkeoWf4wWGFeZtBqsb2v6N2s-v0ByVzSD0gEKzmBqL7biJOApmJN9xYqMTXlb3oJh8UxQUzQBwn0EWyEL7SFHRk-UW5K0uebRQQamgSihX_JiTx-OfWifT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=e1JsMRu4bcP0YoSY8ElwDIz4LsvISN-PO7tVCudfE5Mdj0n4bY7tVlun00BgOOVcrE0Xjoah5QbArRMUv3KtGCIFIXPIrlY83nAxkl6yJepXY7Q4EJTlVKBdZpBlv90_ey_vXwhvq2PzF_gTUpklBPOieokJwFFbApUBMqEoEFmMd2u8Un2A0zMzYlKX0vwfeDeREBRsUbGT2xaw9DXMIv0y5Fsn-AUIclvyCZUR9VE5XXLZKS5KzaSHSN0Q0T9id-PCZZplXHVCXZZZ-xviyKqkEVk8L_F0glQtVZZL-E2yRnxjIA7_Tz4XqwKnry2K8ts5HAeA-L8HI4Nn2AX_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=e1JsMRu4bcP0YoSY8ElwDIz4LsvISN-PO7tVCudfE5Mdj0n4bY7tVlun00BgOOVcrE0Xjoah5QbArRMUv3KtGCIFIXPIrlY83nAxkl6yJepXY7Q4EJTlVKBdZpBlv90_ey_vXwhvq2PzF_gTUpklBPOieokJwFFbApUBMqEoEFmMd2u8Un2A0zMzYlKX0vwfeDeREBRsUbGT2xaw9DXMIv0y5Fsn-AUIclvyCZUR9VE5XXLZKS5KzaSHSN0Q0T9id-PCZZplXHVCXZZZ-xviyKqkEVk8L_F0glQtVZZL-E2yRnxjIA7_Tz4XqwKnry2K8ts5HAeA-L8HI4Nn2AX_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scD1Z8TQxzxC17QtUMosC31zQnjuFDXMyPMnn2_Xx8HeCnH85mD2Oith0WYMQlWhufjR11uszxK5-e2FCk881jTmHm6ATU_MpnwGASxsUDTbs9yndTlwjaZeCQIy2SxdylFUbcRvkir6Bq1iyFMGbBmLvZdsgom7wwOeqTU5ZapPgewsvrwx39Sk9v2ivJfqYs0jtFLA3oMSYQIKFfkzCBSqMVs271Nqqv_FT9LVqTHmg_3W_IEz0XAsDmH3XtKY1vM8kHXONze6Zasg60BaQFQUiSh5EOQRY4gDDTyyLub2sgvIPrMpZGTvDdXoxsqrFRxrlXS4PvHx2o3A6j3xvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=JK5WtsWUMe9ys4WYztEIB4Zf1GYLK8SWJbAWtQIxpglrHjMXKc-NZ4mFpXDVHiChZQDqgy3omij0J4MdWn18oyLBfE4kKlNbdHsuy3PPd0XwIAti2wEsXsOThD27sYSwf-4I1lFBSTXYc9lysQjYDLE7O9BvGo2uoPWbi0F3xZHlRITZBy9jALQEfKKZnc_ZF7lW9O9omect4KKkc9rOuKrwGjZT6cgl_K28251SqtddKU3EgdQiZ1Ya3OhpRp3M2qQY_nSVpxMX5MzDinAODIRYr_N6m_LyqAIlrKy1eZuioR1joMxslFLIFPvbsFKeTyKe-KzXJHcrjpvJyq_gdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=JK5WtsWUMe9ys4WYztEIB4Zf1GYLK8SWJbAWtQIxpglrHjMXKc-NZ4mFpXDVHiChZQDqgy3omij0J4MdWn18oyLBfE4kKlNbdHsuy3PPd0XwIAti2wEsXsOThD27sYSwf-4I1lFBSTXYc9lysQjYDLE7O9BvGo2uoPWbi0F3xZHlRITZBy9jALQEfKKZnc_ZF7lW9O9omect4KKkc9rOuKrwGjZT6cgl_K28251SqtddKU3EgdQiZ1Ya3OhpRp3M2qQY_nSVpxMX5MzDinAODIRYr_N6m_LyqAIlrKy1eZuioR1joMxslFLIFPvbsFKeTyKe-KzXJHcrjpvJyq_gdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=MKN0WVDx_8PwEAmctB-YBHhA0ohBynMMT6RD_nTVsea1E8nlCZtsCOtBPNA2mtaq5D3i4L5RVapTgqIghISr4kj6w941zpqwDvKIjYeYCBsnMLs_zwv3xFLf62Z-GsFhzmpqhvx9oZ1y0GFi_oWp--lnTPgpilktp0FY4EuoIXcgEJTf-6WAI_gQh7SqcX0eUqg4j57FYBgialoS2-8CxP8Vi_g6TJacsvUwLb8OOYn-oWAMw16c2w8Bkj3fKkDMSvyPxz8_0SMy94pwmJbvf3GklP5JJguxu9WWI00CgEZFomvFhKSSm9ie9BmzVjHtHWIHZRkPlBcSO2qeMAh53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=MKN0WVDx_8PwEAmctB-YBHhA0ohBynMMT6RD_nTVsea1E8nlCZtsCOtBPNA2mtaq5D3i4L5RVapTgqIghISr4kj6w941zpqwDvKIjYeYCBsnMLs_zwv3xFLf62Z-GsFhzmpqhvx9oZ1y0GFi_oWp--lnTPgpilktp0FY4EuoIXcgEJTf-6WAI_gQh7SqcX0eUqg4j57FYBgialoS2-8CxP8Vi_g6TJacsvUwLb8OOYn-oWAMw16c2w8Bkj3fKkDMSvyPxz8_0SMy94pwmJbvf3GklP5JJguxu9WWI00CgEZFomvFhKSSm9ie9BmzVjHtHWIHZRkPlBcSO2qeMAh53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPjfR-h5gO4so4hjPyyphQykK_px3bs8g_O1_FiKe3nM_gCixQppxEZ_xDb5ZsL_hiEGZ_-hE1ddghTKN3gQ5aqlER8JBK8qt2rESlhebDFR4nW10W4Htac79on1U-YU8-Nz0xw1SSlJXXWR1Qj7ajP9ANNajPbq4r7zj2sqXqi99xjre898Uka_SY1QXvjgm5LLB0u5eMdCFQ3WGDBRCwfB7GaiAV9UwHqVeMRRN64dYdqr8zniSGwPyn5zktfja0nZ0BIK6I1w_xlOA25x0TGC28tuL4yWXAc8snGXJFe_lqh_VnWkAMrsGVUhb25hNwpH-KSAnL6zSJOD3vGeZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-4hTpS4K1L4Gbq0mnhfhahQRPHHa6IpQVnJUoMPCfOxp_U-lZvvJxXoKXOBR6Dp7GugKsi9sFKqekub_XrAqcW0e6Bv9kGMvFL1EIb7QwAJXxL2aV4OMuBnZyU-H0eeTx3R4RniKaExsfr30G4spwkmyzJrvsw9hhIbWCwT2erioE_n7iVfIS-j9CTy6sux4jnOv5Mi34EhVdHsQgd0KAHBSHLTjvoNA4GizO9vCjx6TfxO6YQbN4HSC3brXjyZZUMZdG262VagVn2OUUFILdc5ZbY5JHAE3ZqYjorss2E3246EqiyzVy2UU-l_eWtgGETFtAT5R3MuR6MbbTH0IoDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-4hTpS4K1L4Gbq0mnhfhahQRPHHa6IpQVnJUoMPCfOxp_U-lZvvJxXoKXOBR6Dp7GugKsi9sFKqekub_XrAqcW0e6Bv9kGMvFL1EIb7QwAJXxL2aV4OMuBnZyU-H0eeTx3R4RniKaExsfr30G4spwkmyzJrvsw9hhIbWCwT2erioE_n7iVfIS-j9CTy6sux4jnOv5Mi34EhVdHsQgd0KAHBSHLTjvoNA4GizO9vCjx6TfxO6YQbN4HSC3brXjyZZUMZdG262VagVn2OUUFILdc5ZbY5JHAE3ZqYjorss2E3246EqiyzVy2UU-l_eWtgGETFtAT5R3MuR6MbbTH0IoDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=uDe8ukoOb67Jvb34dRYQM8uj4jNj-eOPJ9UD9ua-3zZQ2dKZJ6PUp04rMNf7uvAqNrRHjAD3QVi-cz0WBE6szPmiGCHkmM0dBUJJ2LulH6gk_uSGDXaUccCBcNecKq-PrRx-GhqH02LXPvNLE606lbk5xK2jF78fv7Ij5LXRrYRvca3BPPlRUU8qmPfRIKVlJmSgbaVMNiN8KWpRrJBEPcEDievsiR7oTxMOPMEJFcDpiWxEmaVE91iJOkrl-rRyuHmDE2Clixw7ISxJpfxiC0dKf39Nb-FGHWgaVG4b76FOiLHc9ErKJ8g-J_TZ2TvjC-kYb4h4tXGX7i5H3AwehA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=uDe8ukoOb67Jvb34dRYQM8uj4jNj-eOPJ9UD9ua-3zZQ2dKZJ6PUp04rMNf7uvAqNrRHjAD3QVi-cz0WBE6szPmiGCHkmM0dBUJJ2LulH6gk_uSGDXaUccCBcNecKq-PrRx-GhqH02LXPvNLE606lbk5xK2jF78fv7Ij5LXRrYRvca3BPPlRUU8qmPfRIKVlJmSgbaVMNiN8KWpRrJBEPcEDievsiR7oTxMOPMEJFcDpiWxEmaVE91iJOkrl-rRyuHmDE2Clixw7ISxJpfxiC0dKf39Nb-FGHWgaVG4b76FOiLHc9ErKJ8g-J_TZ2TvjC-kYb4h4tXGX7i5H3AwehA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=WDtia1s8TOHYGADEo30h_grQo5PJclSWqhfQA6uGEsLNJ9wbPpD_ESgNSX2Gs64bTA9Bd4hWEgUBJjl7Zi-zL_8Iwrko8alt0hFuxdpkh4cmdDAy09bexR4hmOCtRSOI-JvNO-GCGf-x0rNO4e6qh5CeIu_B4hXhIw2HXW9RelzOnJ26Pn6X3ZnZvSz2aP0KA7YRywzVQRfLResj13V9ElCTdQs6m9BnNkOStC0B6G1oBw8sFp2E399fDYYn6nzHBKlvG1S1XFJuWl9rPPQfTUpA4oXnAb9DQVttEHg7QNeKbxn-iTJ7YhL1E5dyr1DcQNKOBNEtxLEHZ2VaTCDByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=WDtia1s8TOHYGADEo30h_grQo5PJclSWqhfQA6uGEsLNJ9wbPpD_ESgNSX2Gs64bTA9Bd4hWEgUBJjl7Zi-zL_8Iwrko8alt0hFuxdpkh4cmdDAy09bexR4hmOCtRSOI-JvNO-GCGf-x0rNO4e6qh5CeIu_B4hXhIw2HXW9RelzOnJ26Pn6X3ZnZvSz2aP0KA7YRywzVQRfLResj13V9ElCTdQs6m9BnNkOStC0B6G1oBw8sFp2E399fDYYn6nzHBKlvG1S1XFJuWl9rPPQfTUpA4oXnAb9DQVttEHg7QNeKbxn-iTJ7YhL1E5dyr1DcQNKOBNEtxLEHZ2VaTCDByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdq5vu-V0H3CEOtdzXqtBeY1ST3QXILwlejvtcs4Z9U6iIbEpsoNkImSABtxtND-p42qGkTqtyPo631JxVFMy6GcvN0FjuxZqobixHHULufRJGs-vejam1iYw2nsodssqXWRV22vr11LQFt12BNMx3zVtX-0cZGk0P7IVOjmaG4-1EgxHY1EfMNPJCulRabNJpaZav3NHP9qckhXjGzbfZsgqR7qKI-YjjAy02vwNzhGMA0dW4c2THjabFKFZnr9y9y0c85CAOJ0Beff2N9lHGksFPCnZ_4lqZidHEFKYfWI0FM-zeaiWh3y-MMGIljQatuWGzq5sQWJTS06qhttvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B50fwVnHa0uFCO-DQIPqEu5aAOdcXt5t1t5d4GVUcGBpMOxN8K1i6lHzRRGx6nsKVNJ6vWOHEmxWz3UEWH1YCkFMZoki_06go_jwooAZ8V8dHAtp7G6NdAQSvRHSAabDZFLiRYHg5dM69-jw5ZliqLGUxTZwhRvc0GAP66c9k-tZciIR1suGWkIC0UrdB7JhsWnixjbIcRLWiQ0vtuud0pfs9OEp7H4YmrT85jEtE0NpPSkz_7Qwi7ucU7_RhACaSmztG8ht6B697iPVhnNxtVw44o5JDq-f_qbwvPxqXHiU9Ppvi8WRcAYsxhxvucOsSxc1-9wG3t-c5uN1z3sUcXK1Y7cYU1JzxhI0DanStUzyL5lNSmJatw7G4VL0ps7kjaCSStE3pdpDRCvATbqf9Z7Bcz-JIPghIYzSB8ZkLwDpJXvjkZqr5dlVtkwRhyjj2rDy45ZrbhbwsCZx1nMUQHI63wJYK_YffEswNyacY1FnK1s5TJWTeCCe3X8FNgu0K5jCL9Ee337tN6H7A-7YU7NglwDyVpaonNlC0KmE9_sMn42_9lqZ1K-96RtYQK_h5j4vNl4tuKGFYrKQFfm23zXtQx3vKC3bLiW05ruAIQEy8yZE3BGC9t44Y_BNf_glUuNYGJLS2S89ELNcvei12p7drvgG06OBotPhhW-2bUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B50fwVnHa0uFCO-DQIPqEu5aAOdcXt5t1t5d4GVUcGBpMOxN8K1i6lHzRRGx6nsKVNJ6vWOHEmxWz3UEWH1YCkFMZoki_06go_jwooAZ8V8dHAtp7G6NdAQSvRHSAabDZFLiRYHg5dM69-jw5ZliqLGUxTZwhRvc0GAP66c9k-tZciIR1suGWkIC0UrdB7JhsWnixjbIcRLWiQ0vtuud0pfs9OEp7H4YmrT85jEtE0NpPSkz_7Qwi7ucU7_RhACaSmztG8ht6B697iPVhnNxtVw44o5JDq-f_qbwvPxqXHiU9Ppvi8WRcAYsxhxvucOsSxc1-9wG3t-c5uN1z3sUcXK1Y7cYU1JzxhI0DanStUzyL5lNSmJatw7G4VL0ps7kjaCSStE3pdpDRCvATbqf9Z7Bcz-JIPghIYzSB8ZkLwDpJXvjkZqr5dlVtkwRhyjj2rDy45ZrbhbwsCZx1nMUQHI63wJYK_YffEswNyacY1FnK1s5TJWTeCCe3X8FNgu0K5jCL9Ee337tN6H7A-7YU7NglwDyVpaonNlC0KmE9_sMn42_9lqZ1K-96RtYQK_h5j4vNl4tuKGFYrKQFfm23zXtQx3vKC3bLiW05ruAIQEy8yZE3BGC9t44Y_BNf_glUuNYGJLS2S89ELNcvei12p7drvgG06OBotPhhW-2bUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOWzJHOG-idTug_lGwD4COwqfLko6l17blc5RwUe4vWYXbM7MTOeIc1UEuT5WaQ0Bhn_rBRbgAPr4y5HX7YLutV81GkMFMn-F33EsMH5iTypPD56hMM4ZOvs3b9v9ZAdzP_HQdozS33zvXDpZJBjKdM32YPFcuLLwcrWAk5q9UazwvJcXlFST7EDP7By1HRLix8GNCsDTDeeqaIsoE5zz8N2PjQi73Rf6_kgR1U39KkARn9lSE34mN5wXj-b920A7BNKpyKsLmMVkc0QHkpOzqeFrO3XHL2Pn5FsYoO_Q4sFldEeaYFAo_GdkLwBOM0mzReRsyZO6bokpMYvgdSiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=OmxpQ3-Oh3_eNtVnNs6jeFkbc0T8llVO5SI0TtpnGmC9YRbTt9w_bvc2ekS67_Px35UB3YlgpaDTTeIU91NN5NeYbAqhmJVOnnK9p8aM9U9-I9EAzxh6QuRH43O5O0nonqfXSP9Z7lL04bt-DvC0tYIXjr_iWYXVhaa1P3NGDyWGB7P7zXj3kwHQQVLvZhFIzk1GYK5QNnZUEnoHUvrIV-Lryn1ipvUGDNVCnejl_cc9XTALJz1p4HqluKIqlXh3BIVxmxB69R3pEgc1r7_OGNj0RGulJSrI00O9H6LpG-jHSGGXfFBdFlk1czGjD3iIJBtlqPX62t3W6vHVGAahMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=OmxpQ3-Oh3_eNtVnNs6jeFkbc0T8llVO5SI0TtpnGmC9YRbTt9w_bvc2ekS67_Px35UB3YlgpaDTTeIU91NN5NeYbAqhmJVOnnK9p8aM9U9-I9EAzxh6QuRH43O5O0nonqfXSP9Z7lL04bt-DvC0tYIXjr_iWYXVhaa1P3NGDyWGB7P7zXj3kwHQQVLvZhFIzk1GYK5QNnZUEnoHUvrIV-Lryn1ipvUGDNVCnejl_cc9XTALJz1p4HqluKIqlXh3BIVxmxB69R3pEgc1r7_OGNj0RGulJSrI00O9H6LpG-jHSGGXfFBdFlk1czGjD3iIJBtlqPX62t3W6vHVGAahMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXBFg2ILscQIgmX_lSXALtF4yIhys0K9yfOQjcs_9ot8mIhWVga9rGQbDInbwzYbDRZoZ6HXTuNEvQuRSgUqCy002LnH8QwRBcvaVpjgk9T3d9EXPpGwQXYz5ZBHLTwEq1zD4wwG-FyiQisykviCfxqMLMtWW9hqgSdYazFCTWr9K21qq9YdYw4w1noxvn_xui1rLT4xxrYEZ-9QgY9DhzSTp_EmNqwi7TYvKai2X64_OvDOg2GSotYc-EuBL5hNUm56vj3WlxGHgadxD5-_RWVRbydAWt3GeGu-2I7JFfKg_9sTmr46bWdO31uJUqzp1uxqnqQiwOGCqJW6oz-4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
