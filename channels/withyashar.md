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
<img src="https://cdn4.telesco.pe/file/akb16bUfntsjDmVPmgcI30b_Jm8uoGLOy1YlPID2IxoTtv3O1tTm0CP1fn6vf2kPpTPoFPbfVckWWubb_LAY89Ehf-2aAGE4gGbKkytFI9oWqAHO6ZEQTlC-qPMfuHV5CsgtyV7tRbaaTqdkvLeeyhYceWLfCxnfnAdX4kFHMvXWQt7f3jfeK6yNN2ldqWpwjXrGRbTPRjJaO9l483BH7Oa5eYSCyRbxUFXb0cqfVPUgdVeB2Fn_0tuP0C5bDZM7GuevWadoILMg-s-xsqASlYyTtZQQewqNhA1vBupQBFcshKNhIZoGIiOOJhr40UUIM124ECE8E1-YfDYHEMlwpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 276K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 11:07:02</div>
<hr>

<div class="tg-post" id="msg-12517">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03565b856.mp4?token=HmOOUhQ8MiesTveIweb2GyEidXIWB8oLRGwz9FKj1oeH5yPdGuPs2QLTuPRBeq00MhDpPQpF8L1BX4K5EY2y-o5scDERE8ULGodh8olAFD1cQ1Zi-AaqCfkvvV5Nj9j_6uyjNnGGoJ7GBJvINy0Y4u-SkWSfufcoYGA63ZG6wQ0lWI9MkytPzHJl8WdvxlLpWkiqNRxC0kFCewIV150FPAepmzQzC3rsWIcusxHXrN38c_ZsQSIPAkaWWirywGHkDcDWnEogsVSLGwZOre1qaz9XvV6rsPKsLCkGC-Ba91U0KPA1AtAlBLP414qNZz7rhXX03kXkCvR6YzTgAQeAAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03565b856.mp4?token=HmOOUhQ8MiesTveIweb2GyEidXIWB8oLRGwz9FKj1oeH5yPdGuPs2QLTuPRBeq00MhDpPQpF8L1BX4K5EY2y-o5scDERE8ULGodh8olAFD1cQ1Zi-AaqCfkvvV5Nj9j_6uyjNnGGoJ7GBJvINy0Y4u-SkWSfufcoYGA63ZG6wQ0lWI9MkytPzHJl8WdvxlLpWkiqNRxC0kFCewIV150FPAepmzQzC3rsWIcusxHXrN38c_ZsQSIPAkaWWirywGHkDcDWnEogsVSLGwZOre1qaz9XvV6rsPKsLCkGC-Ba91U0KPA1AtAlBLP414qNZz7rhXX03kXkCvR6YzTgAQeAAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تجمعات بابل» اخطار ! دیدن این ویدیو ممکن است باعث بی اختیاری‌ادرار شود
⚠️
😂
@withyashar</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/12517" target="_blank">📅 10:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12516">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فاکس نیوز گزارش می‌دهد  بعید است حادثه دیشب تاثیر بالای  بر روی روند مذاکرات داشته باشد و در صورت نزدیک بودن توافقی هر دو طرف بر سر یک برخورد معامله را بر هم نمی‌زنند
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/12516" target="_blank">📅 10:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12515">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شبکه «سی‌ان‌ان»: برای نخستین باز از زمان آغاز جنگ ایران و آمریکا، یک نفت‌کش ژاپنی از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/12515" target="_blank">📅 10:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال 12 اسراییل: مجتبی خامنه‌ای هنوز توافقات شکل‌گرفته را تایید نکرده
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/12514" target="_blank">📅 10:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12513">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZcKQ9jMwTafMx_JoU4ZNCszJuuBR0F9q-LUD7yMwIWR7mrySK32y-8zUKEUhQXXWoyY0KdwLm_Y88SBnUmVXVxu1VQ3inyq19R06c7hi1hPdGG_TxoaKEu66dRYTts_p2kWtdVgcHMYVd495_-xKjbDfeRjFej-GxAdk2_-4ycdi31idYnuuhTzGzmIE72D2Qyavt3zWAwLp_UUkrce-iUP8GUBtv5GxBnmVfIKasIOH69uPe0pvMq-3gkohT1R0FCQaObmEiBcBP2tV5nztsP4M_eT5QPdJiI-SX-8UeYsQinYyLu-5rdkHLe89BH4kr35FpClDbArgNFib2nwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه اینترنت پرو از سایت همراه اول حذف کردن
گویا این پروژه شکست خورده
@withyashar</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/withyashar/12513" target="_blank">📅 09:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12512">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taBG1olcgUyipfhRdfYuvmtEEEbvq4dwH5gWxC8vhszj_qxg89heRewIiRHvfa4CG0JY-h_fzYmEcxrs72OszWbcZO-HLUzvMfsmq1FBW9pTVDgLJbkVvQ2ykL2-Vo3Wp1n5cLZOd6FGpHFJNSn5iTakVpgvccAb_JmRSx3-G22t6lgS8JaP5plzF_aFZQ8FuNdPjl3RF27h6NOG6TmXolqodIjx2QVkNPEB7QnVSJNK5UBtjE2NcZfARvMnY1dbiylRmBxKYxaLW0vwHXN9fS09WnHkdvTiEGk82raAWHIm9VSV1SSkKarUazrLFwpjTndju_T0CTLDOQLPLChvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز، یک هواپیما دولت حامل مقامات عالی‌رتبه به مسکو رفت!
@withyashar</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/12512" target="_blank">📅 09:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12511">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک منبع آگاه اسرائیلی روز سه‌شنبه اعلام کرد که ارتش اسرائیل در روزهای آینده خود را برای گسترش عملیات‌ها و حملات هوایی در لبنان آماده می‌کند.
سی‌ان‌ان : این منبع تأکید کرد تحرکات نظامی اسرائیلی قریب‌الوقوع «با هماهنگی ایالات متحده» انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/12511" target="_blank">📅 09:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12510">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q55ejvpshOonJ9yoOM4rs3NT6Uz6lcvcMIpZz8qbgYXIUL0pbcdOCnyS31mYwdKO6lCzxaa53vJ4_SBB6__cscwqwJUHcg8PqzgD-zRASsvUNzvYLXGeWFCGkhEgvUZQ-5dBOJNT71eSqZysT1NvNe4enVuhsEah7dJlcRT6ZpiTwhz0B19wIEyKRJclSpg_YqbTpWRnpWYvwVbo_HEGSsWY9JiwbmXWDJ0skNUJjy9__WZkdQFF97cw2a5PairvGbcSxDt8d4nqxIfrZMv6LNClsLCbBXBAudCOrjYkXWifpJ72h-nGO3QDDzxA7OEz4DbeVRwlWAPRX1PdBN3CMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ در تروث سوشال:
سیاست اوباما: بسته های پول میده
سیاست ترامپ : موشک میزنه
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/12510" target="_blank">📅 09:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز
:
پاکستان بلافاصله پیشنهاد ترامپ مبنی بر اینکه توافق با ایران باید به عادی‌سازی روابط با اسرائیل گره بخورد را رد کرد و گفت که این دو موضوع «به هم مرتبط نیستند و نمی‌توان آن‌ها را به هم گره زد».
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/12509" target="_blank">📅 09:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
اینکه گفتن قطر 12 میلیارد دلار از پول‌های بلوکه شده ایران رو قراره پرداخت کنه کاملا کذبه و از این خبرا نیست!
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/12508" target="_blank">📅 02:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12507">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی سنتکام به فاکس نیوز   :  نیرو های آمریکایی در جنوب ایران حملات دفاعی انجام دادند تا از نیرو های خود در برابر تهدیدات نیرو های ایرانی محافظت کنند. اهداف شامل سایت‌ های پرتاب موشک و قایق‌ های ایرانی بودند که در تلاش برای کاشت مین بودند فرماندهی مرکزی…</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/12507" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12506">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی سنتکام به فاکس نیوز   :
نیرو های آمریکایی در جنوب ایران حملات دفاعی انجام دادند تا از نیرو های خود در برابر تهدیدات نیرو های ایرانی محافظت کنند. اهداف شامل سایت‌ های پرتاب موشک و قایق‌ های ایرانی بودند که در تلاش برای کاشت مین بودند
فرماندهی مرکزی آمریکا همچنان از نیرو های خود دفاع میکند و در عین حال در طول آتش‌ بس جاری ، خویشتن‌ داری به خرج میدهد
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12506" target="_blank">📅 02:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12505">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نفت ۹۷$
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/12505" target="_blank">📅 02:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12504">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری اتاق جنگ : کار کانفیگ فروشا بود نت وصل نشه
🤣
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/12504" target="_blank">📅 02:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12503">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتباط زنده صدا و سیما همین الان</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12503" target="_blank">📅 02:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12502">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2931acd1c0.mp4?token=vpybcXGMzEqOOIZZlyq0obPzo12-yqIl9X7zLoBXHvJezJEEzQjXZnuo-BaqiE4mOp3Yqe_9cBj_wb5y7KxYkN6kiDhmFudk7l91QPDwGqBlTWDFFqwbWLczgfOTXOaVBA_yMtxeYOKYORbvOjlnaki7zR8Rt5xkysLKK5ZFuW_ArqNWoa3Vr63Mz7PEMyQ6MluhYK0eSS1seeFqnUlp4Pk7cb_GoE4On9aCUAirT16WgAot89JWHmtYYYDDBtJ0vaGah4R2elIxTko-cFd-Q_rhZejD8rWGErDgIj51hlWqPh4rl--JN6kpT7K6eH-k-5ItBoTXyVCun5Hr13DGcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2931acd1c0.mp4?token=vpybcXGMzEqOOIZZlyq0obPzo12-yqIl9X7zLoBXHvJezJEEzQjXZnuo-BaqiE4mOp3Yqe_9cBj_wb5y7KxYkN6kiDhmFudk7l91QPDwGqBlTWDFFqwbWLczgfOTXOaVBA_yMtxeYOKYORbvOjlnaki7zR8Rt5xkysLKK5ZFuW_ArqNWoa3Vr63Mz7PEMyQ6MluhYK0eSS1seeFqnUlp4Pk7cb_GoE4On9aCUAirT16WgAot89JWHmtYYYDDBtJ0vaGah4R2elIxTko-cFd-Q_rhZejD8rWGErDgIj51hlWqPh4rl--JN6kpT7K6eH-k-5ItBoTXyVCun5Hr13DGcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/12502" target="_blank">📅 02:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12501">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال 14 اسرائیل: "سلام خامنه‌ای کوچیکه"
@withyashar
😈</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/12501" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12500">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سناتور لیندزی گراهام: چه مسیحی انجیلی باشید و چه نباشید، اسرائیل برای آمریکا یک معامله بزرگ است.
اگر ارتش اسرائیل، موساد و شین بت فردا ناپدید شوند، ما کنترل منطقه را از دست خواهیم داد.
پولی که به اسرائیل می‌دهیم، چندین برابر آن را از نظر امنیتی پس می‌گیریم.
اگر اسرائیل می‌خواست همه فلسطینی‌ها را بکشد، می‌توانست. از سوی دیگر، حماس می‌خواهد همه اسرائیلی‌ها را بکشد، اما نمی‌تواند.
حزب‌الله اگر می‌توانست، همه اسرائیلی‌ها را می‌کشت. و هیچ‌کس در اسرائیل نمی‌خواهد همه مردم لبنان را بکشد
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/12500" target="_blank">📅 02:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12499">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاهزاده رضا پهلوی:
«یکی از نماینده‌های پارلمان حتی بهم گفت فکر نمی‌کنه ایرانی‌ها آماده دموکراسی باشن.
ایرانی‌ها فقط آماده دموکراسی نیستن؛ ۴۰ هزار نفر جونشون رو برای رسیدن بهش دادن و من نمی‌ذارم این فداکاری بی‌نتیجه بمونه.
چه اروپا کنار ما بایسته چه نه، چه خبرنگارها کارشون رو درست انجام بدن چه نه، چه سیاستمدارها شجاعت اقدام داشته باشن چه نه، من برای مردمم و کشورم می‌جنگم.
حتی اگر مجبور باشیم تنهایی این مسیر رو بریم، می‌جنگیم تا ایران آزاد بشه.»
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/12499" target="_blank">📅 01:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12498">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارشها میگن که اپ های ، روبیکا و بله، سروس و بلو بانک از دسترس خارج شدند
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/12498" target="_blank">📅 01:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باراک راوید
خبرنگار آکسیوس : چرا مهمه؟ آمریکا داره موضعش رو کمی نرم‌تر می‌کنه
- احتمالاً نسبت به قبل انعطاف بیشتری درباره اورانیوم غنی‌شده ایران نشون میده و حتی تا حدی به خواسته ایران نزدیک‌تر شده
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/12497" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12496">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پست جدید ترامپ که به اسپانیایی واژه خداحافظ را نوشته که بسیار طعنه آمیز است و معنیه «بری دیگه برنگردی» را میدهد. @withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/12496" target="_blank">📅 01:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12495">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsNSEmmv4yXZODvANJZE1RmVRQU6HSwlULgPMqrMSMciD8EI8FESMuTm6Hh2z78IUabLTp6leqRxUxmh-tv9SyEmsQPpcfcNyTcB1bKrjBDKjpMo3blPcIZu96N0TIWJqhjyJycTW0G3Bc8gASY4aoVLphohRGPoWO439Ai89gqsXirLcRn_rJq7BioWzCGahZNNYlywH8bqNcuKAUtofxzi-XAcyTxXwNMce7CRv1QVI7HpNohyNn8VcYC5otKAu1sRXDFfkj6rXyTZvvdOQrShIRK1QD2g-8QPJ_2emK5US1YDQo_btAQlT72dcSnOzpaxUiskWJxZ6fWlFDPRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می رسد 2 آتش سوزی در جزیره خارک ایران رخ داده است.
جزیره خارک بندری برای صادرات 90 درصد فرآورده های نفتی ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/12495" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12494">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12494" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/12493" target="_blank">📅 01:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12492" target="_blank">📅 01:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12491">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدا و سیما : حمله شب گذشته دشمن آمریکایی-اسرائیلی به شناورها در جنوب جزیره لارک  بر اساس اعلام منابع محلی شب گذشته جنگنده‌های آمریکایی-اسرائیلی چند شناور ایرانی را در جنوب جزیره لارک مورد هدف قرار دادند.   طبق اعلام منابع محلی چند تن از هموطنانمان در این حملات…</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/12491" target="_blank">📅 01:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12490">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivnIaqbKFM2KrBc93tiLErVq11OeKx6bMaTmz2Pf6wOZSeBIvsD3NarKmtfFMxmfpQJXGrYi7uWY37c6x90LmGbIiMk8ozRXvSLWGQNSU6zZ5knhaEXIP0m5RRsoxK8gWMhyTJQYYpR9Sq5GmBnpaJjd4I2Fcfg_kodJoY-wgfL-RBHKvL2RxeNms-ZNyyXwn1ybdng4v8T7D2slhmZxrM4aylxTG7qve_-5NNVo_MAhXhyGn9sLPu8nxErk6_OV4FwhFLJeUAPpaz__l5pSPlpvpsgfCdcbavG159zxC1cxeykr5py65Bdj9O-UJLWg2dmp5--GK42FoQCBIRtU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : اورانیوم غنی‌شده (غبار هسته‌ای!) یا باید فوراً به ایالات متحده تحویل داده شود تا به آمریکا منتقل و نابود گردد، یا ترجیحاً با همکاری و هماهنگی جمهوری اسلامی ایران، در همان محل ــ یا در مکان مورد توافق دیگری ــ از بین برده شود؛ آن هم در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، بر این روند و این اقدام نظارت و شهادت داشته باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/12490" target="_blank">📅 01:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12489">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هر‌ چیزی لیاقت میخواد…</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12489" target="_blank">📅 01:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12488">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12488" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12487">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پدافند تهران گویا فعال شد !
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/12487" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12486">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۴ نفر فوتی بردن بیمارستان شهید محمدی @withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/12486" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12485">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صابرین نیوز : اسامی شهدای حمله سحرگاه شب گذشته ۴ خرداد در جنوب جزیره لارک
بر اساس اعلام منابع محلی نام سه تن از شهدای حمله دشمن متخاصم آمریکایی-اسرائیلی که تا این لحظه شناسایی شدند به شرح زیر است:
شهید عباس اسلامی
شهید قدرت زرنگاری
گشهید عبدالرضا گلزاری
گفتنی است تعداد شهدا هنوز مشخص نشده.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/12485" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12484">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صدا و سیما : حمله شب گذشته دشمن آمریکایی-اسرائیلی به شناورها در جنوب جزیره لارک  بر اساس اعلام منابع محلی شب گذشته جنگنده‌های آمریکایی-اسرائیلی چند شناور ایرانی را در جنوب جزیره لارک مورد هدف قرار دادند.   طبق اعلام منابع محلی چند تن از هموطنانمان در این حملات…</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/12484" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12483">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صدا و سیما : حمله شب گذشته دشمن آمریکایی-اسرائیلی به شناورها در جنوب جزیره لارک
بر اساس اعلام منابع محلی شب گذشته جنگنده‌های آمریکایی-اسرائیلی چند شناور ایرانی را در جنوب جزیره لارک مورد هدف قرار دادند.
طبق اعلام منابع محلی چند تن از هموطنانمان در این حملات به شهادت رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/12483" target="_blank">📅 01:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12482">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هاآرتص: جرقه زده شد
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/12482" target="_blank">📅 01:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12481">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش مشاهده  چند موشک ۳ پا در آسمان یزد
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12481" target="_blank">📅 00:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12480">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">برابر گزارش‌ها، پرتاب  موشک از قم.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12480" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12479">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اتاق جنگ با شما : فکر کنم ترور بابل درست باشه بخشی از خیابونو دو طرفشو بسته بودن کلا نه اجازه ی ورود میدادن نه خروج
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/12479" target="_blank">📅 00:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12478">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">میدل ایست :  دو قایق تندرو نیروی دریایی سپاه در خلیج فارس هدف جنگنده‌های آمریکایی قرار گرفتن و چهار سرباز کشته شدن @withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/12478" target="_blank">📅 00:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12477">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">میدل ایست :  دو قایق تندرو نیروی دریایی سپاه در خلیج فارس هدف جنگنده‌های آمریکایی قرار گرفتن و چهار سرباز کشته شدن
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/12477" target="_blank">📅 00:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12476">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انقدر مسیج بی‌مورد ندید مگه به بچه آدم چند بار باید بگن !؟! دایرکت جای جوک و نظر شما نیست ! الان  زمانه  گزارش ها است فقط !</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/12476" target="_blank">📅 00:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12475">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترور هدفمند بابل (تایید نشده)
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/12475" target="_blank">📅 00:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12474">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تابناک :
باند پروازی فرودگاه بندرعباس مورد اصابت موشک قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/12474" target="_blank">📅 00:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12473">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12473" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12472">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پدافند اصفهان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/12472" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12471">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبر ها حاکی از شنیده شدن صدای جنگنده در دزفول و بهبهان.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12471" target="_blank">📅 00:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12470">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گویا اشتباه تایپی بوده مقتصات حمله رو بجا جنوب لبنان ، جنوب ایران نوشتن
😅
🤣
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/12470" target="_blank">📅 00:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puwziYZlLzyHfdO39Or7dwAPXfSGBNkGpm7cVFtXgmESl-bckVMf2uN4HkiPFiYmSBkWfbyMShZBtZvg8eIqoru7NDzmMxZFEUhYff1IgDxjGCYzVQgy_3sDPTKy4jwXTS0EMV3DbrH4i5V38bh5R42ksGPzb_EA4qSImexMTwPfCjhyvgrGRPEekusqrACsmnOtLyhFW3L7kf--UumX-4_ygYyKt5Uw5oJQKpM3FNv6I8vaeH3HKnNqWNtGdzVRZ3DhBA9cAvHm4_2ajnK9XO-in2-2SWKmwDsuSyXZ4YW7yUZbCjelf7V96-cKbTIhZzN6kO0wCIvIQBDklKSjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین عکس‌ از بندرعباس ، سمت پایگاه هوایی
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12469" target="_blank">📅 00:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌶️
🫑</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12468" target="_blank">📅 00:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/12467" target="_blank">📅 00:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فارس: صداهای مشابهی در جزایر سیریک و جاسک شنیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/12466" target="_blank">📅 00:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مهر: دلیل انفجارها در بندرعباس مشخص نیست.
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/12465" target="_blank">📅 00:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نوتیف واریز پولای بلوکه شده بود
🤣
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/12464" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تست توافقه چیزی نیست
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/12463" target="_blank">📅 00:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی: بعید میدونم آمریکا با ایران توافق کنه و 5 بند ایران رو بپذیره؛ توافق ایران و آمریکا خیلی دور است.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/12462" target="_blank">📅 23:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12461">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ممکنه مثل همیشه پدافند یا شلیک موشک هم باشه ! صبر میکنیم فیلمی عکسی خبری رسمی ‌بیاد</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/12461" target="_blank">📅 23:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش سه انفجار بندر عباس (تایید نشده )
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/12460" target="_blank">📅 23:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش زیاد دارمم انفجار بندرررر
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/12459" target="_blank">📅 23:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12458">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئیس دفتر موشعلی : تمام وسایل زندگی شخصی آقا به اندازه یک بار وانت بیشتر نمی‌شد.
@withyashar
🛻</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/12458" target="_blank">📅 23:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12457">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جنگ تمام عیار ۳
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/12457" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">@withyashar
جنگ تمام عیار ۲</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/12456" target="_blank">📅 22:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">@withyashar
جنگ تمام عیار</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/12455" target="_blank">📅 22:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/12454" target="_blank">📅 22:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو:جنگ تمام عیار در لبنان از امشب آغاز خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/12453" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ایسنا: با توجه به تایید مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴ از سوی رئیس‌جمهور و ابلاغ آن به وزارت ارتباطات، انتظار می‌رود این دستور فردا اجرایی شود
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/12452" target="_blank">📅 22:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پزشکیان: در جنگ ۱۲ روزه خدمت رهبر شهید رفتم و ایشان گفتند چگونه مذاکره انجام بشود
ایشان قبول کردند ما باید برویم پای میز مذاکره، اما ما اکنون تبلیغ می‌کنیم که نباید مذاکره کنیم
@withyashar
رفسنجانی هم با همین فن از قول خمینی ، خامنه ای رو رهبر کرد !
😂</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/12451" target="_blank">📅 21:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: دولت ترامپ از تشدید اقدام نظامی اسرائیل در لبنان حمایت خواهد کرد. @withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/12450" target="_blank">📅 21:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">61 سال پیش در چنین روزی الی کوهن جاسوس افسانه‌ای و عجیب و غریب موساد توسط دولت سوریه اعدام شد الی کوهن توانسته بود تا سطوح ارشد وزارت دفاع سوریه نفوذ کند و عملاً با اطلاعات طلایی اش توانست پیروزی های اسرائیل در بلندی های جولان در جنگ شش روزه را تسهیل کند
@withyashar
قبلا به شما در اتاق جنگ مینی سریال بسیار زیبای داستان زندگیشو به نام The Spy معرفی کردم</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/12449" target="_blank">📅 21:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: دولت ترامپ از تشدید اقدام نظامی اسرائیل در لبنان حمایت خواهد کرد
.
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/12448" target="_blank">📅 21:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">طبق خبرهای رسیده به خبرنگار هم‌میهن رئیس‌جمهور زرشکیان دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد. @withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/12447" target="_blank">📅 21:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e9a943ca.mp4?token=N_xqephuGGGf8HHUdq5woZhYCXD68VWqPMapf9NhUMEC72icpmrCbX6MaUW6NLfHkKEir6CWeaPIZr2R4QK0zoQTz9HyAiOgyN4t34yBdkewtxppBTNIf40uCVUN0EwXBL539R_8p8ILPJni2pQTpY4DGlgdshONteDl1P-efw9vz2XL39IVWBYPAhMRS6N39FNn7DQJzoRWlw_xANNpgBgEue3Z-N5w57tNPrIonMSqQc48bMb5vIemXtTs5EqdZI6fd01wZHAWSAZZgL1YT9rOKfz4W-OltTS758pCHPWKEQ-VJyJzJADdesBnxKWXfBQEhExWz9ehxbwGXJ43Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e9a943ca.mp4?token=N_xqephuGGGf8HHUdq5woZhYCXD68VWqPMapf9NhUMEC72icpmrCbX6MaUW6NLfHkKEir6CWeaPIZr2R4QK0zoQTz9HyAiOgyN4t34yBdkewtxppBTNIf40uCVUN0EwXBL539R_8p8ILPJni2pQTpY4DGlgdshONteDl1P-efw9vz2XL39IVWBYPAhMRS6N39FNn7DQJzoRWlw_xANNpgBgEue3Z-N5w57tNPrIonMSqQc48bMb5vIemXtTs5EqdZI6fd01wZHAWSAZZgL1YT9rOKfz4W-OltTS758pCHPWKEQ-VJyJzJADdesBnxKWXfBQEhExWz9ehxbwGXJ43Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ:
"در دو جنگ اخیر، مجموعاً ۱۳ تن از نیروهای نظامی خود را از دست داده‌ایم... در عملیات «خشم حماسی»، ۱۳ جان فوق‌العاده را از دست دادیم."
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12446" target="_blank">📅 20:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شبکه ۱۲ تلویزیون اسرائیل به نقل از منابع آگاه گزارش داد که «استیو ویتکاف» و «جرد کوشنر» به منظور بحث و تبادل نظر درباره توافق احتمالی میان واشنگتن و تهران به اسرائیل سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12445" target="_blank">📅 20:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">طبق خبرهای رسیده به خبرنگار هم‌میهن رئیس‌جمهور زرشکیان دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد.
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/12444" target="_blank">📅 20:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ برای بار دو میلیون و چهارصدو شصت و هشتم : ایران هیچوقت سلاح هسته ای نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/12443" target="_blank">📅 20:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">منابع العربیه: نسخه نهایی پیش‌نویس یادداشت تفاهم آمریکا و ایران شامل تجدید قابل‌تمدید آتش‌بس 60 روزه، باز کردن تنگه هرمز بدون اخذ عوارض و پاکسازی مین‌ها و برداشتن موانع دریایی از این آبراه بین‌المللی مقابل تجارت جهانی، برداشتن برخی محدودیت‌ها از بنادر ایران و دادن معافیت‌‌هایی از تحریم‌ها و فراهم کردن امکان ازسرگیری فروش و صادرات نفت ایران و همچنین ادامه مذاکرات درباره برنامه هسته‌ای ایران در دوره تنش‌زدایی میان دو طرف، می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/12442" target="_blank">📅 20:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای الحدث به نقل از منابع: ایران آماده‌ست تا اورانیوم با غنای بالا رو به چین  انتقال بده ! @withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/12441" target="_blank">📅 20:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طبق گزارش تایید نشده از شاهدان عینی که به دستمان رسیده است از وقوع یک درگیری نامشخص در محدوده میدان انقلاب تهران در ساعتی قبل خبر می‌دهند.
بر اساس این ادعاها، گفته می‌شود منطقه  تحت کنترل نیروهای امنیتی قرار گرفته و رفت‌وآمد در برخی مسیرها محدود شده است.
همچنین طبق گفته شاهدان عینی تعداد زیادی جنازه که از ظواهر آنها مشخص بود نیروهای حشد الشعبی بوده اند روی زمین ریخته بود
به محض وصول هر گونه اخبار تکمیلی به اطلاع شما عزیزان خواهد رسید ‌
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/12440" target="_blank">📅 20:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نورالدین الدغیر، خبرنگار الجزیره در تهران:
به نظر می‌رسد گره مذاکرات ایران و آمریکا در حال باز شدن است و ابتکار قطر نقش اساسی در حل اختلافات داشته است.
به گفته او، دوحه یک میانجی واقعی بوده، نه فقط کمکی در میانجی‌گری.
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/12439" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">العربیه: پیش‌نویس توافق میان آمریکا و ایران، برقراری آتش‌بس جامع در تمامی جبهه‌ها، از جمله لبنان را تضمین می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12438" target="_blank">📅 20:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای الحدث به نقل از منابع:
ایران آماده‌ست تا اورانیوم با غنای بالا رو به چین  انتقال بده !
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/12437" target="_blank">📅 20:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12436" target="_blank">📅 19:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca508f5252.mp4?token=QibxweggHVqikDzKo5FKp-w_xZSBX5LFs56YE8idmTFCJ6NWeDCZjwk_jMMicYI-fjMcRgXelsM2vwfVPPjXcGYhkLb_T27nSzP8SIqQdH1ooJxoFRo7KDBSb6IVgyRbLqsfrysURgNNePHsIAe8_81UQqcLQ1CMYUY04ZjIIP7jecQrHFjkyKdnx7Mat6WK4t6RAHAo7KEaaeHJ0gG2GGhe1xUe0MuZnfKvpIOJQ_AvmEE2ce2QomuMuMrFmkJO1nbfl5txnZ1K-rsnqJxBsL3m3vGNMqM1HwyRCCRF7ItTe0NGu0C3Ylf-k-Gbt5_4KorsYmlqsb5RHloMAcJP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca508f5252.mp4?token=QibxweggHVqikDzKo5FKp-w_xZSBX5LFs56YE8idmTFCJ6NWeDCZjwk_jMMicYI-fjMcRgXelsM2vwfVPPjXcGYhkLb_T27nSzP8SIqQdH1ooJxoFRo7KDBSb6IVgyRbLqsfrysURgNNePHsIAe8_81UQqcLQ1CMYUY04ZjIIP7jecQrHFjkyKdnx7Mat6WK4t6RAHAo7KEaaeHJ0gG2GGhe1xUe0MuZnfKvpIOJQ_AvmEE2ce2QomuMuMrFmkJO1nbfl5txnZ1K-rsnqJxBsL3m3vGNMqM1HwyRCCRF7ItTe0NGu0C3Ylf-k-Gbt5_4KorsYmlqsb5RHloMAcJP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/12435" target="_blank">📅 19:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADiuE5U1zIIHaf7dfVMbpzjxyNVfw1wl_poVGfvW18scSw7cc5jCDUsrjDfbzdDDmmH4ZfE08Ve1YXCZ8jZE00HlR5d1dWwZsj31IU-xBU4ACRP3NT6dCjPayyGqkgR-tps6BzfPZwnVEfqemxFMojktzG2giJlcxzRYyr6DniaAYiSE3dp-Cmdse0JJTolLxiXvlE_z9cJHYEdS7WTOWzSd3NzPw9LPPyxTGiiIAQI-d3PcQQAWqL7t6UiH-wj0DHNDF_ClxRWZJbmcS0kyJP_LFpE1qR9JzaL6nrLxh-dUQsdS5ZnajGg_yroaoDfmD3VCLH5NzsTY-bEsiCKZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vC4z2bkfbeAytwEL8u1jAq2oZjN_t-MrIsz5KZOuD1Ci6Mh9-5EytPVLpvemANw7Ul0k09DI8ZFhL6LuYbhlaz2BFu21909HQfBIN_ppQmPKT372SXqtTeCM8O5YjV4S5KrPIGuEoaDleCg72dNbogzcghLTyYQzEoeP69jMoEoS5BIaQ8HniShvqc2Xd2GGv961SKGz8ERcYc-Fhsd11tLXe3shAD_4VE3YZ0U8Hr1oYMIeIqClBumss58mPpQLTPNjNAxo7bXYHPYGE7IKecU9heG2MpqfkOIrl1YM0YQR8BiV8t8bjN85DYwCJ2os1hnJb0mXVTi7CoSMHK3-eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ با مسخره کردن اوباما و بایدن عکسهایی منتشر کرد که آنها به ایران پول میدهند و مذاکره میکنند، ولی او آنها را منهدم میکند.
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/12433" target="_blank">📅 19:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12428">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/12428" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12427">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئیس جمهور مکزیک رسما از میزبانی تیم ملی فوتبال ایران در جام جهانی خبر داد
«کلودیا شین‌بام» رئیس‌جمهور مکزیک، رسماً اعلام کرد که تیم ملی فوتبال ایران به دلیل محدودیت‌های حضور در خاک آمریکا، در ایالت «باخا کالیفرنیا» مستقر خواهد شد.
با تایید دولت مکزیک، تیم ملی ایران شهر «تیخوانا» را به عنوان مقر اصلی و محل تمرینات خود در طول مسابقات جام جهانی ۲۰۲۶ انتخاب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/12427" target="_blank">📅 18:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/12426" target="_blank">📅 18:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۴ اسرائیل: اختلاف نتانیاهو با ترامپ عملیات فریب است
طبق گفته یک تحلیلگر ارشد امنیتی اسرائیل، گزارش‌های درز کرده درباره تماس‌های تلفنی پرتنش میان ترامپ و نتانیاهو بر سر ایران واقعی نبودند، بلکه بخشی از یک راهبرد حساب‌شده برای گمراه‌کردن تهران بودند.
بر اساس گزارش کانال ۱۴ اسرائیل، این جنجال با گزارشی از پایگاه خبری آکسیوس آغاز شد که مدعی بود یک تماس تلفنی به‌ ویژه دشوار میان ترامپ و نتانیاهو درباره یک پیشنهاد جدید آمریکایی که از طریق پاکستان برای ایران ارسال شده، صورت گرفته است.
کوبی مایکل، پژوهشگر ارشد در مؤسسه مطالعات امنیت داخلی (INSS) و مؤسسه میسگاو، توضیح می‌دهد که این یک فریب تاکتیکی درخشان بوده است: «نه رئیس‌جمهور ترامپ و نه نخست‌وزیر نتانیاهو هیچ علاقه‌ای به یک بحران واقعی ندارند. با درز داستان درباره یک بحران جدی ادعایی میان آن‌ها، ایرانی‌ها ممکن است از زمان‌بندی حمله نظامی بعدی کاملاً غافلگیر شوند.»
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/12425" target="_blank">📅 18:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12424">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وال استریت ژورنال ادعا کرده روند توافق بین ایران و آمریکا به خاطر اختلاف نظر شدید تو موضوع هسته‌ای و آزادسازی پول‌های بلوکه شده ایران خیلی کند شده (به بن‌بست نزدیک شده)
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/12424" target="_blank">📅 18:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71963b16ac.mp4?token=LW4BgQazy6fC5jzJsFvpB_kYuCK3Kri3lXWTV6QEqkMg4MXkmqcJdZsexkJkE7nMrZ6DpN-W9Tw8XkpRVj-XzKsqujGW-S13GUEf1v_PFTTjD_vwopByAgj8rCEfjedvbJAT0_FJjnLBwmDZlGK8698T1X_kVN8WztF76m15NOgyIFbCR_fWgOq-n8yUQFoluDcgRWmPG-_oHP9UU0_0eO3uJ-VvR6kj7cWGxxcreRu2Q7Hk2ebSkakqIoPdeGYcEz_6H3thAvKh-nb2amT4yD9CVQKFoAjtndsV-yIQa9RYZ6mu9oo5Q71C38nLgQu7WF0HTDPB2roTPuzRgimzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71963b16ac.mp4?token=LW4BgQazy6fC5jzJsFvpB_kYuCK3Kri3lXWTV6QEqkMg4MXkmqcJdZsexkJkE7nMrZ6DpN-W9Tw8XkpRVj-XzKsqujGW-S13GUEf1v_PFTTjD_vwopByAgj8rCEfjedvbJAT0_FJjnLBwmDZlGK8698T1X_kVN8WztF76m15NOgyIFbCR_fWgOq-n8yUQFoluDcgRWmPG-_oHP9UU0_0eO3uJ-VvR6kj7cWGxxcreRu2Q7Hk2ebSkakqIoPdeGYcEz_6H3thAvKh-nb2amT4yD9CVQKFoAjtndsV-yIQa9RYZ6mu9oo5Q71C38nLgQu7WF0HTDPB2roTPuzRgimzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خلبان کلمبیایی که در ارتفاع ۱۲۵۰۰ پایی پرواز می‌کرد، تصویری را ثبت کرد که به عنوان بهترین فیلم ثبت شده از بشقاب پرنده‌ها تا به حال توصیف شده است و بنا به گزارش‌ها، اصالت آن تأیید شده است.
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/12423" target="_blank">📅 18:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12422">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150a08d32b.mp4?token=bGU92hRMp4Swlu9JKPXojP3QczpOLTEtOqLIoUOEp6ZKDpZDY0ovanI-SntWKyS3n8E3niFQ-tJkCceQ0--91h1bwBiBVYgwHR40suG_saxKkrD1Ps207dQk8piV72d8Md0b3z4pflcHYSpHqvO46fQJX6CRGmJ8-bCAjI0GtaE5KAb8-MHFJzhTl5qIKzUWSoMjGiw6k-i33sZ_L9InjXGFjhnszxsnAoO7qsongpbQ-byvRh3zk29Up-prMzDGY9IGYNsI0iFsZbKpRVQWM9s8mtKsnn9QXuOfb7sXs-MIewoxF-YFNpDOzcgCcp4dNlV3MZxvjxydjVnorxfZNx4xP2Q1RbObueMF9jXhYG-5EuPipiYj4n8yBfNPbMMOwLtp8W_tlUERXw004djCaMzvEjxj5B354XnKumbRBeHduUyogiNqB1vq4oc8s8KHREYtXCS1z5Q4drNOh9awyPJB9SxbC_wBJReVUPlj6X2ugj5UmUTAnyfe_CHxIyLuQjnL0DPYXHjXEKWz2J2lDT7S4Gxl4X5w7_2aqfV3_TnjFWeWAVe6gWpJ4J9nk2v-R8hyt3TpTCFxZWvcTgIyRlL-9RQ13vpSGDaSajoNa4DJsRKppMfIwdnXBcO7WQcOI33bcNT0dTNgiaNfVlfOYJr_7bFFp0DsWOBZIHn-ilc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150a08d32b.mp4?token=bGU92hRMp4Swlu9JKPXojP3QczpOLTEtOqLIoUOEp6ZKDpZDY0ovanI-SntWKyS3n8E3niFQ-tJkCceQ0--91h1bwBiBVYgwHR40suG_saxKkrD1Ps207dQk8piV72d8Md0b3z4pflcHYSpHqvO46fQJX6CRGmJ8-bCAjI0GtaE5KAb8-MHFJzhTl5qIKzUWSoMjGiw6k-i33sZ_L9InjXGFjhnszxsnAoO7qsongpbQ-byvRh3zk29Up-prMzDGY9IGYNsI0iFsZbKpRVQWM9s8mtKsnn9QXuOfb7sXs-MIewoxF-YFNpDOzcgCcp4dNlV3MZxvjxydjVnorxfZNx4xP2Q1RbObueMF9jXhYG-5EuPipiYj4n8yBfNPbMMOwLtp8W_tlUERXw004djCaMzvEjxj5B354XnKumbRBeHduUyogiNqB1vq4oc8s8KHREYtXCS1z5Q4drNOh9awyPJB9SxbC_wBJReVUPlj6X2ugj5UmUTAnyfe_CHxIyLuQjnL0DPYXHjXEKWz2J2lDT7S4Gxl4X5w7_2aqfV3_TnjFWeWAVe6gWpJ4J9nk2v-R8hyt3TpTCFxZWvcTgIyRlL-9RQ13vpSGDaSajoNa4DJsRKppMfIwdnXBcO7WQcOI33bcNT0dTNgiaNfVlfOYJr_7bFFp0DsWOBZIHn-ilc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بار جدید نخود رسید
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/12422" target="_blank">📅 17:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMariam</strong></div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/12421" target="_blank">📅 17:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9a649e54.mp4?token=syv1X9ZiZ0FTOFbBE_apX3k39ZiP0nLHI03Uvc8CEbgSNOT-k9UPI6eyFUP-FphjwtfMo-m9BhabGievADXfHRbznvaTmbs992EIedUT2hqEQOzS1IgsVYhIqB3cdjzC-IBJwLWCiaaSdsbjnvTG9xo-Osw8t45JNPXpXBr1ECqwa7RlIwok1npQQUHIdvGZqvE_4Xr854IHtE6VOXMeHuApFw10_2WS_3WhCEVwpME9S73fB3KxHBOyjyhd2x_tBoYO5IEpsOILFdtM3aSO947qr_oCuCkdqnL6wK6NeHKtTpI5sYm0DG_bmS-7x3NGwWlbBFmpoIGYyZDLeOdx9jVmOl_gJeZhLvpt0ZVfKB4xqfUjW16m0AYKobST6VXIVAxZ2PkINrcLw10DmkGxz78NkTqocmEpmhueb0osaJZNmSH-MVDmsLxetxAMBOxFcQwoQazI00T3rpCaO2da366MknGBiEjqeDItkMNREP9HOXuiIrKvwK2RjbiiVL2FGhIyjnnAylfcrORqwwrOIHN2kWpq-AUdEKaohNgVdV9VX0aRZsj-YsYWPQjqHJ_4yt7Fy3XkFlPaaokAcABNpCSpa1zdcgznxon-EWWZi6d2tNMd75USOpzddzM7XcJhrw8jm38Dcgkv2oBzJu6P-1odQRJoZdDI98cK0pPJznU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9a649e54.mp4?token=syv1X9ZiZ0FTOFbBE_apX3k39ZiP0nLHI03Uvc8CEbgSNOT-k9UPI6eyFUP-FphjwtfMo-m9BhabGievADXfHRbznvaTmbs992EIedUT2hqEQOzS1IgsVYhIqB3cdjzC-IBJwLWCiaaSdsbjnvTG9xo-Osw8t45JNPXpXBr1ECqwa7RlIwok1npQQUHIdvGZqvE_4Xr854IHtE6VOXMeHuApFw10_2WS_3WhCEVwpME9S73fB3KxHBOyjyhd2x_tBoYO5IEpsOILFdtM3aSO947qr_oCuCkdqnL6wK6NeHKtTpI5sYm0DG_bmS-7x3NGwWlbBFmpoIGYyZDLeOdx9jVmOl_gJeZhLvpt0ZVfKB4xqfUjW16m0AYKobST6VXIVAxZ2PkINrcLw10DmkGxz78NkTqocmEpmhueb0osaJZNmSH-MVDmsLxetxAMBOxFcQwoQazI00T3rpCaO2da366MknGBiEjqeDItkMNREP9HOXuiIrKvwK2RjbiiVL2FGhIyjnnAylfcrORqwwrOIHN2kWpq-AUdEKaohNgVdV9VX0aRZsj-YsYWPQjqHJ_4yt7Fy3XkFlPaaokAcABNpCSpa1zdcgznxon-EWWZi6d2tNMd75USOpzddzM7XcJhrw8jm38Dcgkv2oBzJu6P-1odQRJoZdDI98cK0pPJznU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹۵٪ از توافق ایران تکمیل شده؛ ایران اگر بخواهد به توافق صلح ابراهیم می‌تواند بپیوندد/ خبرنگار فاکس‌نیوز در تل‌آویو:
"ترامپ به طور خاص از عربستان سعودی و قطر خواست که بپیوندند و اضافه کرد که دیگران نیز باید از آنها پیروی کنند. او حتی در صورتی که ایران این توافق را امضا کند، درِ ورود ایران به پیمان ابراهیم را باز گذاشت.
در حال حاضر، دولت ترامپ می‌گوید توافق با ایران ۹۵ درصد کامل شده است، اما جزئیات نهایی همچنان در حال بررسی است. دیروز در تماسی با خبرنگاران، یکی از مقامات ارشد دولت توضیح داد که ممکن است چندین روز طول بکشد تا به تفاهم‌نامه برسیم، زیرا سیستم ایران به سادگی نمی‌تواند به سرعتی که ایالات متحده می‌خواهد حرکت کند...
در حال حاضر، ایران میلیاردها دلار از دارایی‌های بلوکه‌شده خود را به همراه معافیت‌های تحریم نفتی دریافت خواهد کرد، اما به گفته مقامات آمریکایی، تنها در صورتی که به تعهدات خود پایبند باشند."
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/12420" target="_blank">📅 17:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مهر: ایران با سامانه دفاعی جدید خودش به نام «کمان ارش» یه پهپاد جاسوسی دشمن رو رهگیری کرد
@withyashar
گویا همین پدافند قشم است</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12419" target="_blank">📅 16:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12418">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق جنگ با یاشار : نقشه عالی پیش میره
😃
💪🏾
مثل بنز داره کار میکنه … از این جدیدایه فابریک صفر کارخونه برند نیو</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/12418" target="_blank">📅 16:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12417">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دو مقام اسرائیلی به رویترز: نتانیاهو به نزدیکان خود می‌گوید که هیچ تأثیری بر تصمیمات ترامپ ندارد
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/12417" target="_blank">📅 16:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9xcQbTRoW4NRALXqny9FYJQmHSKrir6K7bUUS_52nfTkMiXECzgUTqvIMheBqRX4d6prqM2cc9YetVlxMIuLfliZVWBXvccQKC7UoWAI_WVGEtPDW0KlBAjoyGZ3lC0gEhjXNsBAFrR8M5-pfBH2dy-etIDm13F9qdw5LSrcIS4E7hSB6xYR-91QZcvGjpy1GXiiveq6uGC3FpdfsGIIDx1FcwtZukCosBgu2BwbFX24XBZPcLkFvLw2lelqbeC1vXIR3RacMCj4EybS1eSv0Xcz_MWwpoMGNNN9CCyRNKh9ga1-qzcQGzM8WtJ7hpkyIGYI-DtZvSQCX13EFRk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «مذاکرات با جمهوری اسلامی ایران به‌خوبی در حال پیشرفت است! یا این توافق، توافقی بزرگ برای همه خواهد بود، یا اصلاً توافقی در کار نخواهد بود — وگرنه بازگشت به میدان نبرد و تیراندازی آغاز می‌شود، آن هم بزرگ‌تر و قدرتمندتر از همیشه — و هیچ‌کس چنین چیزی را نمی‌خواهد!
در جریان گفت‌وگوهایم در روز شنبه با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی، محمد بن زاید آل نهیان، رئیس کشور امارات متحده عربی، شیخ تمیم بن حمد آل ثانی، امیر قطر، محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی، نخست‌وزیر قطر، علی الثوادی، وزیر قطری، سید عاصم منیر احمد شاه، فرمانده ارتش پاکستان، رجب طیب اردوغان، رئیس‌جمهور ترکیه، عبدالفتاح السیسی، رئیس‌جمهور مصر، ملک عبدالله دوم، پادشاه اردن، و حمد بن عیسی آل خلیفه، پادشاه بحرین، اعلام کردم که پس از تمام تلاش‌هایی که ایالات متحده برای کنار هم قرار دادن این پازل بسیار پیچیده انجام داده، لازم است که همه این کشورها، حداقل به‌صورت هم‌زمان، به پیمان ابراهیم بپیوندند.
@withyashar
کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از: عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یک یا دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند تا این توافق با ایران را به رویدادی تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.
پیمان‌های ابراهیم برای کشورهای عضو آن — یعنی امارات متحده عربی، بحرین، مراکش، سودان و قزاقستان — یک جهش عظیم مالی، اقتصادی و اجتماعی به همراه داشته‌اند، حتی در این دوران جنگ و درگیری؛ تا جایی که هیچ‌یک از اعضای فعلی حتی صحبت از خروج یا توقف موقت هم نکرده‌اند.
دلیلش این است که پیمان‌های ابراهیم برای آن‌ها فوق‌العاده بوده و برای همه نیز حتی بهتر خواهد بود، و برای نخستین بار در پنج هزار سال گذشته، قدرت، توان و صلح واقعی را به خاورمیانه خواهد آورد.
این سند، همانند هیچ توافق دیگری که تاکنون در جهان امضا شده، مورد احترام قرار خواهد گرفت. سطح اهمیت و اعتبار آن بی‌همتا خواهد بود!
@withyashar
این روند باید با امضای فوری عربستان سعودی و قطر آغاز شود و دیگران نیز باید به‌دنبال آن حرکت کنند. اگر این کار را نکنند، نباید بخشی از این توافق باشند، زیرا این نشان‌دهنده نیت بد است.
در گفت‌وگو با بسیاری از رهبران بزرگی که نام برده شد، آن‌ها اعلام کردند که به‌محض امضای سند ما، از حضور جمهوری اسلامی ایران در پیمان‌های ابراهیم استقبال خواهند کرد. واو، این واقعاً چیزی ویژه خواهد بود!
این مهم‌ترین توافقی خواهد بود که هر یک از این کشورهای بزرگ اما همواره درگیرِ منازعه تاکنون امضا کرده‌اند. هیچ‌چیز در گذشته یا آینده از آن فراتر نخواهد رفت.
@withyashar
بنابراین، من به‌طور الزامی درخواست می‌کنم که همه کشورها فوراً پیمان‌های ابراهیم را امضا کنند، و اگر ایران توافق خود را با من، به‌عنوان رئیس‌جمهور ایالات متحده آمریکا، امضا کند، حضور ایران نیز در این ائتلاف بی‌نظیر جهانی مایه افتخار خواهد بود.
خاورمیانه متحد، قدرتمند و از نظر اقتصادی نیرومند خواهد شد؛ شاید بیش از هر منطقه دیگری در جهان!
با انتشار این پیام در تروث سوشال، از نمایندگان خود می‌خواهم روند پیوستن این کشورها به پیمان‌های ابراهیمِ تاریخی را آغاز کرده و با موفقیت به پایان برسانند.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12416" target="_blank">📅 15:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12415">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2fb5139f3.mp4?token=jnHWoBMvEghnSm8GWYs3LaulZhk6yhrCu-20cgO9BKs2axKcQ3iV_xkQKeoLV4VlK21JFZ-2V8PzvP-9lTA3Nzccix5vjz3xt4rT0z4Y9W-K1khbdb4jhPRE6RCXFwpzysNKoi-_eTLKf2rnv2zdEE3LWd4WcTWiyX2FHQHW33xF2v7xMvIzV1sYD04c_ZHnhPDVtp8AocmhRgsT0m5a0jDMgdeyeOlTylMp_RTXsc7AzW7oSNzIGJPPLAyp7MmscAOJjN4DbP4LBqLfclze55INOpLtS8ImR32SfQXWgxwd5l9utecQg9ejyKngGLf4HvdL5v5smDL6DltW66kuJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2fb5139f3.mp4?token=jnHWoBMvEghnSm8GWYs3LaulZhk6yhrCu-20cgO9BKs2axKcQ3iV_xkQKeoLV4VlK21JFZ-2V8PzvP-9lTA3Nzccix5vjz3xt4rT0z4Y9W-K1khbdb4jhPRE6RCXFwpzysNKoi-_eTLKf2rnv2zdEE3LWd4WcTWiyX2FHQHW33xF2v7xMvIzV1sYD04c_ZHnhPDVtp8AocmhRgsT0m5a0jDMgdeyeOlTylMp_RTXsc7AzW7oSNzIGJPPLAyp7MmscAOJjN4DbP4LBqLfclze55INOpLtS8ImR32SfQXWgxwd5l9utecQg9ejyKngGLf4HvdL5v5smDL6DltW66kuJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز: رئیس‌جمهور ترامپ با قاطعیت شایعات دربارهٔ یک توافق هسته‌ای ضعیف را رد کرد و اعلام کرد که هرگز به تهران «پول نقد تحویل نخواهد داد.»
رئیس‌جمهور ترامپ به لارِنس بیلی جونز؛ (مجری تلویزیونی، مفسر سیاسی و خبرنگار آمریکایی شبکه فاکس‌نیوز) گفت منتقدانی که ادعا می‌کنند او در برابر ایران رویکردی نرم دارد، کاملاً در اشتباه‌اند.
«واقعاً فکر می‌کنید بعد از تمام حرف‌هایی که دربارهٔ این‌که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند زده‌ام، من به‌عنوان رئیس‌جمهور فقط بیایم و پول نقد به آن‌ها تحویل بدهم؟»
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/12415" target="_blank">📅 15:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe86e64833.mp4?token=FGwRzg5KHWdwWtaSEs0y7ZeTrVD0Pg4E8A65QHei91LaKGzIPqhVPRyxcxlyWEXulx_kS8IdmGl2QKzu89sDLipLl0a3N-2TVRCQzkXMuILHk9Ke8YGdjC6PfPkxg8hT8pYCgse-EfSOm2gdoqYWrXPisl2fBHuM5tbPx4VnFmeyaB4Os9S9NGtfUk_JRel_Kahi4yU1jdmXoNux0sVqDe6v6pZCJICy_l6dM-xs4s8r-Ux1dH38cmRQYZbL4RiYt9J4K_u3PeQiOWjgOPl0YX0Yi9Z-jI8P2SDQIxYmD6Azn0dRW3KaQXX6eEppnP97QrYqK0L6aW6Kc0Caqj83ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe86e64833.mp4?token=FGwRzg5KHWdwWtaSEs0y7ZeTrVD0Pg4E8A65QHei91LaKGzIPqhVPRyxcxlyWEXulx_kS8IdmGl2QKzu89sDLipLl0a3N-2TVRCQzkXMuILHk9Ke8YGdjC6PfPkxg8hT8pYCgse-EfSOm2gdoqYWrXPisl2fBHuM5tbPx4VnFmeyaB4Os9S9NGtfUk_JRel_Kahi4yU1jdmXoNux0sVqDe6v6pZCJICy_l6dM-xs4s8r-Ux1dH38cmRQYZbL4RiYt9J4K_u3PeQiOWjgOPl0YX0Yi9Z-jI8P2SDQIxYmD6Azn0dRW3KaQXX6eEppnP97QrYqK0L6aW6Kc0Caqj83ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مذاکرات ایران: رئیس‌جمهور ترامپ با قاطعیت شایعات دربارهٔ یک توافق هسته‌ای ضعیف را رد کرد و اعلام کرد که هرگز به تهران «پول نقد تحویل نخواهد داد.»
رئیس‌جمهور ترامپ به لارِنس بیلی جونز؛ (مجری تلویزیونی، مفسر سیاسی و خبرنگار آمریکایی شبکه فاکس‌نیوز) گفت منتقدانی که ادعا می‌کنند او در برابر ایران رویکردی نرم دارد، کاملاً در اشتباه‌اند.
«واقعاً فکر می‌کنید بعد از تمام حرف‌هایی که دربارهٔ این‌که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند زده‌ام، من به‌عنوان رئیس‌جمهور فقط بیایم و پول نقد به آن‌ها تحویل بدهم؟»
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12414" target="_blank">📅 15:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همتی رئیس بانک مرکزی هم در تیمه و برای پیگیری آزادسازی منابع ارزی ایران   راهی قطر شده
قرار شده است که قطر بخشی از پول‌های بلوکه شده ایران را پرداخت کند و بعد آمریکا به آن بپردازد!
سید محمد مرندی، عضو سابق تیم مذاکره‌کننده هسته‌ای: ظاهرا قرار بر این است قطری ها بخشی از پول را برای ما تامین و بعداز آمریکا دریافت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/12413" target="_blank">📅 15:30 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
