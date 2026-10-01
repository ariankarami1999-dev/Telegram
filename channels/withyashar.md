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
<img src="https://cdn4.telesco.pe/file/t-R1rgFxngI6clhi97qQqVAv4oMqzQk82QQEvWl6UYj2-x6DNu8s26iSGo9qanbydk-gOmin22RR8CJbr4Tiyk0lYh4V_iIudttnLieynZnf3fw1gH6no7s0zDRpfzt6h8iQ-Uim_qEz-JLbbJgJO5-cEvnnzOfQBMbPmNPlzvpSu--BVtAeDEF3Ul5xfjDMm-Kzv8avdA5YvyLYP_mFmORnAEd27TSJpBgBY2XrtXThJCal-XXu1UtZmy8QiWlDYirgIfTsiY8PF4AdX6p_VsBDntyQCbcesL83AL6fNVagKlkWLXPL8O9pNsbhUrw2MRxz5vPF5cUDt-53XzuASw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 482K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-24716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwSQwc8JacyhNDWMBNQVpvEoT8-riy48LbP6OlT2cT8IQmcE-0r2mmjPHaSDQ_nu9GwNs-OBh5uXmd9scyfDkS2jokXXxNyuTfUtzGo5lY6YrgtWrfrOEWXPdFnW2Gpq-ZhAijgcV0O4drTJejsRW8bB5fcFc5gczz2IqqHmXaosBZujJnHNrCaFa32htJn9Y81j1wKl502O9CiyEkVZJJe4BxRgTGAnT1FtMB71G3LzdevBbB4fNTojyyy4UtbQi1ZcMQQ17338QvYSBwa-2naEyvtbIaQe5pQ14hFulxRQAxgV4_yLvdM9nome3Ml1GuatLoBM1mXzthLpIdyZe_iM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwSQwc8JacyhNDWMBNQVpvEoT8-riy48LbP6OlT2cT8IQmcE-0r2mmjPHaSDQ_nu9GwNs-OBh5uXmd9scyfDkS2jokXXxNyuTfUtzGo5lY6YrgtWrfrOEWXPdFnW2Gpq-ZhAijgcV0O4drTJejsRW8bB5fcFc5gczz2IqqHmXaosBZujJnHNrCaFa32htJn9Y81j1wKl502O9CiyEkVZJJe4BxRgTGAnT1FtMB71G3LzdevBbB4fNTojyyy4UtbQi1ZcMQQ17338QvYSBwa-2naEyvtbIaQe5pQ14hFulxRQAxgV4_yLvdM9nome3Ml1GuatLoBM1mXzthLpIdyZe_iM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولادیمیر پوتین: پیشنهاد انتقال اورانیوم غنی‌شده ایران به روسیه ارائه شده و این پیشنهاد
همچنان کاملاً روی میز است
. اما سپس آمریکا موضع خود را سخت‌تر کرد و گفت انتقال اورانیوم تنها باید به آمریکا انجام شود. از آنجا بود که ایران نیز تصمیم گرفت موضع خود را سخت‌تر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/withyashar/24716" target="_blank">📅 22:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ:
عباس عراقچی، وزیر امور خارجه ایران،بطور غیر علنی پیشنهاد داده است که تهران در ازای
کاهش تحریم‌ها، دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به تمامی تأسیسات هسته‌ای آسیب‌دیده ایران را از سر بگیرد
. این پیشنهاد در چارچوب تلاش‌های دیپلماتیک برای دستیابی به توافق میان ایران و آمریکا مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/24715" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/24714" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/24713" target="_blank">📅 22:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش زیاد از ایست بازرسی های پی در پی در شهر های ایران مخصوصا کرج
@WarRoom</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/24712" target="_blank">📅 21:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">(پدافند) بیژنه غرب ایران کرمانشاه فعال شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/24711" target="_blank">📅 21:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60239b6687.mp4?token=d-4INJOiAgCu3rRX9mfL8Ca792LN28UNSi5r28MyoyQql2YCj4PQbsxUJRp5fEpBo7njUXZe4R-xZYm6HfN2H71dN1cuPVUIzY3pZ6U-lmgxqRRPinTqB2i8UTEBW4QtCwbUBgRiJuPMlzB6s_NU2zUzmHN6TG44YTuiLq4G-F48q28njJl7NIHFHPDvOzOVHffHblojtoNOSjzG9dGVPTK6N11biwKDk3DpVp1Oy-EXC_yvrKqp9n1PVexmjgNI214VlC-M_vbXsxDG6BegvEJVD-V_tQuois1N0h96Sk1WmDpEL6tmmos2zpoPLrzkrEHxnOA4iaYr6me5hkyU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60239b6687.mp4?token=d-4INJOiAgCu3rRX9mfL8Ca792LN28UNSi5r28MyoyQql2YCj4PQbsxUJRp5fEpBo7njUXZe4R-xZYm6HfN2H71dN1cuPVUIzY3pZ6U-lmgxqRRPinTqB2i8UTEBW4QtCwbUBgRiJuPMlzB6s_NU2zUzmHN6TG44YTuiLq4G-F48q28njJl7NIHFHPDvOzOVHffHblojtoNOSjzG9dGVPTK6N11biwKDk3DpVp1Oy-EXC_yvrKqp9n1PVexmjgNI214VlC-M_vbXsxDG6BegvEJVD-V_tQuois1N0h96Sk1WmDpEL6tmmos2zpoPLrzkrEHxnOA4iaYr6me5hkyU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/24710" target="_blank">📅 21:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/24709" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تحریم‌های جدید علیه ایران، بخش‌های خودروسازی و راه‌آهن و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف خشکاندن منابع مالی جمهوری اسلامی اعمال شده است. وزارت خزانه‌داری آمریکا امروز ایران‌خودرو و سایپا و همچنین…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/24708" target="_blank">📅 21:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وال‌استریت ژورنال:
دونالد ترامپ به دستیاران خود گفته است که انتظار دارد
پس از انتخابات میان‌دوره‌ای نوامبر، بمباران ایران از سر گرفته شود.
مقام‌های آمریکایی می‌گویند هنوز مشخص نیست حملات احتمالی در چه ابعادی انجام خواهد شد. در همین حال، آمریکا در حال تقویت نیروهای نظامی خود در منطقه است و یک گروه ناو هواپیمابر دیگر نیز در راه خاورمیانه است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/24707" target="_blank">📅 21:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24706">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">BTC 85000$
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/24706" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مقام اماراتی به کانال ۱۴ : ارزیابی‌ها درباره اینکه ایران این حمله را سازماندهی کرده، در حال تقویت است. کاپیتان هندیِ مجروح نیز برای درمان به امارات منتقل شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/24705" target="_blank">📅 21:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24704">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgcZy2Hv4CPQwn1ECgF1I_E0f_7V8yWnCXjo279OxYGhtOio0jVQTcIswwNm8d93itu6ohQdWOS3Oh2ADGZyr9WE8eMl0xhShVadBaNbLSEtdCSmSP6WXBX7pSKQn1wTKKI6UyR3KNY8YSQFBzg0uQx3bMMTQpHL2Gv2YoO5CZ2tzCj79KxPNfmJbp-C-ZHXvBceN1-rNzK5wbQxOSRbOKhzG43a-1CKNmPrJ-6XhpOF5QGQk4_tyUSEfbbQYw_Dz6y04zGSl2lDZFzdWtpEMCm5nvMjIeCByIX-fYWX7aLQj79ERGKads8BsM5aKLHqxlN_24z4mlp2YTh3xVHxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث سوشال: من بارها اعلام کردم که از بین بردن
تهدید هسته‌ای ایران
۴ تا ۶ هفته زمان می‌برد، اما من این کار را در یک شب انجام دادم! بقیه این مدت فقط برای اطمینان از این است که وضعیت همین‌طور باقی بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/24704" target="_blank">📅 21:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تحریم‌های جدید علیه ایران،
بخش‌های خودروسازی و راه‌آهن
و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف
خشکاندن منابع مالی جمهوری اسلامی
اعمال شده است. وزارت خزانه‌داری آمریکا امروز
ایران‌خودرو و سایپا
و همچنین چندین شرکت خارجی مرتبط با تأمین قطعات، مواد اولیه و خدمات این صنایع را تحریم کرد. واشنگتن می‌گوید این اقدامات بخشی از کارزار
«عملیات طرد اقتصادی»
برای قطع منابع مالی حکومت ایران و افزایش فشار اقتصادی بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24703" target="_blank">📅 21:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=lAaJdkX7WvkPC_MhZdP3VfKL2ILQSPvqM9qTqk4iozgQ5HdW3FpuU-g807Tn-yUkKS6YjJS_WELf0NxnISNW3E0J_Kcn-1hfUblvES3_QiRAIZQlPTBkfh8D7rCC7d6Hqx7Qj6er15VN-XEjIlNj16GKgKNHYhzOIn8Aan5BBGgJCQ1IVh9ks5CMvL3JsA3q7Z-PcQNUYvuI7ppNvb8yStVBYNBhvVssVIZFAvEn7GU5ZYx9a1SFUfmr0LcPP9N6Vmf8dQEmgfESxZ9mVivso1eIMtYfCPDxWAMep8oIpE-ABbvlv_6sMNtI7Y54Qz0yXx3AjZSjiDogr1rs7F-9SU-bSDCwzhRI94SRcRcLN3wQlGjwo1_YvP5yhkwTb8MbB7voSFg__6jMlkPEm2u-9hdmc0jmmmr-iiTPOVm0AzE9GRdxZXZzyMl-Kqyn4uRk1OgYeJcmMl8T0msFL642Ikz1cyc-tCAhxn1Tv1hEUH6qJX52w5RDwomrpPbpYrLpcZme7_qeDJJa6JkndR4iCWVRqJmhdIkEp0_P6H367NU6QjyTxF1d8y0MIwGISvkueQApI8j593njnlRxZdJms_OgC5orNA16909yAUuBz7qcR-Ha9WGwHeMhEHIOJCTrymS8clYhgENH0HRJmxsD_9R-n6RCFIF-0aXev9l9Os0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=lAaJdkX7WvkPC_MhZdP3VfKL2ILQSPvqM9qTqk4iozgQ5HdW3FpuU-g807Tn-yUkKS6YjJS_WELf0NxnISNW3E0J_Kcn-1hfUblvES3_QiRAIZQlPTBkfh8D7rCC7d6Hqx7Qj6er15VN-XEjIlNj16GKgKNHYhzOIn8Aan5BBGgJCQ1IVh9ks5CMvL3JsA3q7Z-PcQNUYvuI7ppNvb8yStVBYNBhvVssVIZFAvEn7GU5ZYx9a1SFUfmr0LcPP9N6Vmf8dQEmgfESxZ9mVivso1eIMtYfCPDxWAMep8oIpE-ABbvlv_6sMNtI7Y54Qz0yXx3AjZSjiDogr1rs7F-9SU-bSDCwzhRI94SRcRcLN3wQlGjwo1_YvP5yhkwTb8MbB7voSFg__6jMlkPEm2u-9hdmc0jmmmr-iiTPOVm0AzE9GRdxZXZzyMl-Kqyn4uRk1OgYeJcmMl8T0msFL642Ikz1cyc-tCAhxn1Tv1hEUH6qJX52w5RDwomrpPbpYrLpcZme7_qeDJJa6JkndR4iCWVRqJmhdIkEp0_P6H367NU6QjyTxF1d8y0MIwGISvkueQApI8j593njnlRxZdJms_OgC5orNA16909yAUuBz7qcR-Ha9WGwHeMhEHIOJCTrymS8clYhgENH0HRJmxsD_9R-n6RCFIF-0aXev9l9Os0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال 14 اسرائیل: «این عملیات برای دستیابی به سه هدف طراحی شده بود: کشتن تعداد زیادی از اسرائیلی‌ها، آسیب رساندن به روابط ما با امارات، و آسیب رساندن به خود امارات.»(زیرنویس فارسی)
@WarRoom</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/24702" target="_blank">📅 21:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=dsE5HEIrdcUMJYfvnEMNGXpnGS57ZVOyEwBj_kY1_XPFqEJLIo-chX1AwdjhXPPuQ3apEdhMNUQvSvilEawUezw74_TwS-DH8osJ1r2FMJA7MSzsZwtcJ0sq-MMByhagWoz4a-vc9xwQKRm-45oe_iwccefZe-RF8l68xDskZKDBuCy91LV3FY9Bv1ErpntZCj_wB7AWqJYjcFrzGHJlnkfDiys-GSP4GsmYZDvnCuTmmjuw3WUEI0-rXkUzJWPD4wZOMJClZs3ZxZZ2szcYwAACRaIEJDfybIyznzeNlHLxyO1sYTeF13gqPX3GirCbTrZMRTgI70SPG2KOgGtpNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=dsE5HEIrdcUMJYfvnEMNGXpnGS57ZVOyEwBj_kY1_XPFqEJLIo-chX1AwdjhXPPuQ3apEdhMNUQvSvilEawUezw74_TwS-DH8osJ1r2FMJA7MSzsZwtcJ0sq-MMByhagWoz4a-vc9xwQKRm-45oe_iwccefZe-RF8l68xDskZKDBuCy91LV3FY9Bv1ErpntZCj_wB7AWqJYjcFrzGHJlnkfDiys-GSP4GsmYZDvnCuTmmjuw3WUEI0-rXkUzJWPD4wZOMJClZs3ZxZZ2szcYwAACRaIEJDfybIyznzeNlHLxyO1sYTeF13gqPX3GirCbTrZMRTgI70SPG2KOgGtpNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوکی از شبکه فاکس: این خلبان فلای دوبی ممکن است توسط سپاه پاسداران منصوب شده باشد، یا به نوعی دیگر افراطی شده باشد و سپس سعی کرده باشد هواپیما را سرنگون کند؟
ترامپ: ممکن است، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/24701" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=h9BlJzgPDp1XH5JAimoqu2Ov7xLlek7Dhaw9HFZW29Uq-KovmXU9GD1bYqgs9DhncFqnXGr-xVVHOhBwdyuAfRypCPQ_pdkzzT4bodd8LdpvdJyTJmFkum4kYxANfzR5CRjlMsGnKzma1h13xgznWD8vH1UyTfBdJdIFvhKINGxq2BtLRB9cvCaRCryKmNnS0mtNzVgAAFrt7YqrB1W8mXGb9DGeYjLF1ofnOtWIWTAzbBKLWUsyGuLx0u7yBOD_GgHJli5ITVpda5kVgr_4p7-cr4dl0xoIWYnddnF1-BL7iDuXmAdsqw5ChVeYpFdnLEmxnAKxdmrh1t2doi-ZBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=h9BlJzgPDp1XH5JAimoqu2Ov7xLlek7Dhaw9HFZW29Uq-KovmXU9GD1bYqgs9DhncFqnXGr-xVVHOhBwdyuAfRypCPQ_pdkzzT4bodd8LdpvdJyTJmFkum4kYxANfzR5CRjlMsGnKzma1h13xgznWD8vH1UyTfBdJdIFvhKINGxq2BtLRB9cvCaRCryKmNnS0mtNzVgAAFrt7YqrB1W8mXGb9DGeYjLF1ofnOtWIWTAzbBKLWUsyGuLx0u7yBOD_GgHJli5ITVpda5kVgr_4p7-cr4dl0xoIWYnddnF1-BL7iDuXmAdsqw5ChVeYpFdnLEmxnAKxdmrh1t2doi-ZBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سوال که آیا ایران در حادثه مربوط به هواپیمای فلاي‌دبي دخیل است یا خیر، گفت: "به نظر من، با توجه به اطلاعاتی که دارم، بله، اما ما در حال حاضر در این زمینه کار می‌کنیم."
@WarRoom</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/24700" target="_blank">📅 20:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=YQ-aDhjQBqmtAHdnyo9aQ2oO4XH75p2bAmFwgTyPGKzJfLwqE6Dd-VPMpHL6QomqG_HDn6STvLbHLSYZYWs9fYOeorlJ1W_G68dfOGHkMYPFMjtAPWpjls5ROyxiqjL4wNeNqqjwG8ORw-36jzx6xT8yp418ayWYV-b4N4LPDRAVaOAflG4uGMMaVa9M6zhTVhtd8D1HsVSD4eNlfLgXknTzaCDAVUbgdIqqKYgH0WrEaYjcLhbUcJ8L2orI-RgeJEVqHic6hLBup6H-do4wIGS299wDHY5FO_KXSNYQajp-UKBCnDzQEU6fZJMJFHjAcl4adhMPxavqIPLgznZUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=YQ-aDhjQBqmtAHdnyo9aQ2oO4XH75p2bAmFwgTyPGKzJfLwqE6Dd-VPMpHL6QomqG_HDn6STvLbHLSYZYWs9fYOeorlJ1W_G68dfOGHkMYPFMjtAPWpjls5ROyxiqjL4wNeNqqjwG8ORw-36jzx6xT8yp418ayWYV-b4N4LPDRAVaOAflG4uGMMaVa9M6zhTVhtd8D1HsVSD4eNlfLgXknTzaCDAVUbgdIqqKYgH0WrEaYjcLhbUcJ8L2orI-RgeJEVqHic6hLBup6H-do4wIGS299wDHY5FO_KXSNYQajp-UKBCnDzQEU6fZJMJFHjAcl4adhMPxavqIPLgznZUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت در گردهمایی انتخاباتی جمهوری‌خواهان عازم اوکلاهوما شد. دونالد ترامپ، رئیس‌جمهور آمریکا، پنجشنبه ۹ مهر برای حضور در یک تجمع انتخاباتی جمهوری‌خواهان در شهر دورانِت، اوکلاهوما، به این ایالت سفر کرد. این مراسم در چارچوب انتخابات میان‌دوره‌ای کنگره آمریکا برگزار می‌شود و ترامپ در حمایت از نامزدهای جمهوری‌خواه سخنرانی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24699" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/24698" target="_blank">📅 20:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=XrBJADpthpI3aRU8zt6taNaNbmcydu-ASdLWEVwx7AGx2FsiUdyfe5BdMAY5d1z7zB-CQQ4xUlEb9IB9QjZWdI5VvUUfuD6bpSgR9YfnDMXq4MsJ9-zg8NEhOfNdfC-7VwEZAEM_poKMZYzZDK8ItFxD6Dq7mj74Ov_TuAPc66ddqMPD9tQgIeYeOLKWcPZYYaWeasoPVopVroiWu0CUxJq_KbW98W1O17dQPRnZ8Nb7M8DvsW_8Dcs2BDNiIJpfj-Hra21NwS4XYlKraX9eZzAbxy0JAsMfxovvtuclfcnhG7s0Ed82ve9eHfSiSwA8LI-cJinTOhSMQIajYh7P-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=XrBJADpthpI3aRU8zt6taNaNbmcydu-ASdLWEVwx7AGx2FsiUdyfe5BdMAY5d1z7zB-CQQ4xUlEb9IB9QjZWdI5VvUUfuD6bpSgR9YfnDMXq4MsJ9-zg8NEhOfNdfC-7VwEZAEM_poKMZYzZDK8ItFxD6Dq7mj74Ov_TuAPc66ddqMPD9tQgIeYeOLKWcPZYYaWeasoPVopVroiWu0CUxJq_KbW98W1O17dQPRnZ8Nb7M8DvsW_8Dcs2BDNiIJpfj-Hra21NwS4XYlKraX9eZzAbxy0JAsMfxovvtuclfcnhG7s0Ed82ve9eHfSiSwA8LI-cJinTOhSMQIajYh7P-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چه نظری دارید؟»
ترامپ: «هر اتفاقی برای ایران بیفتد، برای نیروهای نیابتی آن هم همان اتفاق می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/24697" target="_blank">📅 20:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=lmFLXk2kkWDBewZ0F3dF7pvr6a7tLImE2oQ6OgLGcRoHT_R9SKVQW18Te37ImgsIogBMioE3GbEp1x6PquI2Lb3e_Ba21SljQt-B2I50t4-TVQQqxmUFeNchVTYUEFNkqQH3vbCMlUtXy92au2qkxPUlL_8zC0R7cZCmEAAQoGHX095quOFNPp4Zp4jjOnCEcE1JNanp2cvBdwAqzWebllXaE-SD3foWmZy08KiKalsKl9lkLuJqmA_VTmErZNdhup69Eh5YgVoWDro9rYG0oPOjSmblnKdwlLpHvxAxGiA2eBt1poeV3YR9iehcnmc4AT0liBypwC8mI3LiaCAf6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=lmFLXk2kkWDBewZ0F3dF7pvr6a7tLImE2oQ6OgLGcRoHT_R9SKVQW18Te37ImgsIogBMioE3GbEp1x6PquI2Lb3e_Ba21SljQt-B2I50t4-TVQQqxmUFeNchVTYUEFNkqQH3vbCMlUtXy92au2qkxPUlL_8zC0R7cZCmEAAQoGHX095quOFNPp4Zp4jjOnCEcE1JNanp2cvBdwAqzWebllXaE-SD3foWmZy08KiKalsKl9lkLuJqmA_VTmErZNdhup69Eh5YgVoWDro9rYG0oPOjSmblnKdwlLpHvxAxGiA2eBt1poeV3YR9iehcnmc4AT0liBypwC8mI3LiaCAf6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: به جرئت می‌گویم که صددرصد مردم,  از جمله در سراسر جهان , با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/24696" target="_blank">📅 20:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک مرز اسرائیل بود، اما دو خلبان جایگزین تمرینی به‌جای فرود در مقصد ، مسیر را تغییر داده و بدون فرود حتی در اردن، هواپیما را به عربستان بردند. نتیجه این اقدام، نجات خلبان تروریست عمانی و جلوگیری از مشخص‌شدن اسناد این عملیات بود. یکی از دو خلبان بریتانیایی بوده و هویت خلبان دوم اعلام نشده؛ احتمالاً فرانسوی یا اسپانیایی باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/24695" target="_blank">📅 20:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=uA67SLe_3unyzAISP8yQ7FGnqCuDWv7EonK3NQHRZqewBKg1egctWZA6o8u8J5tB951CKEg7oT7F0-VehHVYDdj49Qx5-BWkXnPhq6pSNAR92IhZ7SPKAtojMlP8yzHMOd8Gm1PfnhkNCfYQo1bD22VhnG230hpIA0fhuNBVA0bGJiXaiXkBh3vH2votoGnOrXEqFeafEGDs7pCDy_izHcc4ZZqipZkoQLnCAx-Yh_KoSAwflbkiQhMHRpDkLDEGpEWQpP15l5N3Jcvhh86B4l-89Gy7chNnc7MBxX9bXBAo8SqM0k5BodBNe3IQHjxzps83pnt8SqnLbEUJ1BftiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=uA67SLe_3unyzAISP8yQ7FGnqCuDWv7EonK3NQHRZqewBKg1egctWZA6o8u8J5tB951CKEg7oT7F0-VehHVYDdj49Qx5-BWkXnPhq6pSNAR92IhZ7SPKAtojMlP8yzHMOd8Gm1PfnhkNCfYQo1bD22VhnG230hpIA0fhuNBVA0bGJiXaiXkBh3vH2votoGnOrXEqFeafEGDs7pCDy_izHcc4ZZqipZkoQLnCAx-Yh_KoSAwflbkiQhMHRpDkLDEGpEWQpP15l5N3Jcvhh86B4l-89Gy7chNnc7MBxX9bXBAo8SqM0k5BodBNe3IQHjxzps83pnt8SqnLbEUJ1BftiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: اگر ایران پشت حمله به هواپیما باشد، آیا شما علیه آن اقدام تلافی‌جویانه خواهید کرد؟ آیا ایالات متحده تلافی خواهد کرد؟
ترامپ: آنها ضربه سختی خواهند خورد، نگران نباش. فقط از آنها بپرس؟ آنها می‌دانند چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/24694" target="_blank">📅 20:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=SYDlXu6gL-nB2mc1lOj7r0j7qisl8KiIdHG4n7RNQWtD5bKJ9_BBZpZAt3JC9ikPXBTw9c-MLHYHDHkFZAAY45Poc-HOkVwvGtTDz14LCWSl1Rimx9_vlOCaeusBRsUVBv1n5EfCLOiNzzyLBIiXIOXNZ0K3K0gpD6w9to_NlySNi09YyQ-CwJvBaEGSlqHDU49E_MX_fOBRDcFPKtMdmZ8oVEfMGXDx0g-2HK3O8oKlV5hOg7T9PqLcWBS4aej4R76GJ3a5JT_eXSdnIleXQnJ8kKXp6Gcs97jHDEiIuBcI1P175pLsgDmlh3MawtMXGSQfpX89CGy_bQKMqvcNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=SYDlXu6gL-nB2mc1lOj7r0j7qisl8KiIdHG4n7RNQWtD5bKJ9_BBZpZAt3JC9ikPXBTw9c-MLHYHDHkFZAAY45Poc-HOkVwvGtTDz14LCWSl1Rimx9_vlOCaeusBRsUVBv1n5EfCLOiNzzyLBIiXIOXNZ0K3K0gpD6w9to_NlySNi09YyQ-CwJvBaEGSlqHDU49E_MX_fOBRDcFPKtMdmZ8oVEfMGXDx0g-2HK3O8oKlV5hOg7T9PqLcWBS4aej4R76GJ3a5JT_eXSdnIleXQnJ8kKXp6Gcs97jHDEiIuBcI1P175pLsgDmlh3MawtMXGSQfpX89CGy_bQKMqvcNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد داشت؛ آن‌ها نیز پذیرفته‌اند که چنین سلاحی نداشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24693" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=MdokYMQrfGN04XG1giiDCzPpMjb6RAcu8rov7iByHSXFlAIY1jlhA3cdnOwd44IpONIfPXLc8XdkYcIRG1IQ3W-VBkVqRoCFhnUfETh2Y0JzBJji3idiElUrwWmDAOOFoKy0Gp9aViQ_1Xb1P2D0v_OvYpW7kV7m6jFWkeBeT3DgKK9ATp7fsozXo5wTdg9tfkeeAz75urVNE5IG79pDw65wj05bA8-YE-5Q7uTX3hnUsuKay_MgdTdzwuqrgGU1cLCYy3CDetgbrhRAxc2MISC5jSrPogwKm9OqSxmSSj8r_kjA2R_6OitNbcpGkcmBLDmMTvSa3Rm2XzlIOrbW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=MdokYMQrfGN04XG1giiDCzPpMjb6RAcu8rov7iByHSXFlAIY1jlhA3cdnOwd44IpONIfPXLc8XdkYcIRG1IQ3W-VBkVqRoCFhnUfETh2Y0JzBJji3idiElUrwWmDAOOFoKy0Gp9aViQ_1Xb1P2D0v_OvYpW7kV7m6jFWkeBeT3DgKK9ATp7fsozXo5wTdg9tfkeeAz75urVNE5IG79pDw65wj05bA8-YE-5Q7uTX3hnUsuKay_MgdTdzwuqrgGU1cLCYy3CDetgbrhRAxc2MISC5jSrPogwKm9OqSxmSSj8r_kjA2R_6OitNbcpGkcmBLDmMTvSa3Rm2XzlIOrbW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نرخ‌های بهره می‌توانند رشد را کند کنند. ما خواهان رشد هستیم؛ و رشد موجب تورم نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/24692" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1487770b48.mp4?token=dVZ6i-zjp-OEdsqwJhhDvrjEdsOa5_aRyMTtXGYexhbtfNFr3v3cidKdlOgorvBZ6tmeSdX0uBZt7T9NOLW_zhl1CP9PaCK1hYvpqPcSu6zIShCAt1R3UOuI4yDl-s3aatEgD2EWkADOSFPUHzS6ag62UX2V7dcPTQZk8OGqseOX8AScQu1T2a807tvLoY0IgHt87kZcNOIW_mUo-pfCRD1y7qPQU-zdvyEZ_2OatU3PcVb5VjjR4xy2DqaiwUrv1Xz7NwRUoavEnbgvXZyJuwo2_DGb6yrZeLxIKmsugKFhgDltnDqeMf1IJZupIj9v_5pAbw6O4Vyzno9zprxDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1487770b48.mp4?token=dVZ6i-zjp-OEdsqwJhhDvrjEdsOa5_aRyMTtXGYexhbtfNFr3v3cidKdlOgorvBZ6tmeSdX0uBZt7T9NOLW_zhl1CP9PaCK1hYvpqPcSu6zIShCAt1R3UOuI4yDl-s3aatEgD2EWkADOSFPUHzS6ag62UX2V7dcPTQZk8OGqseOX8AScQu1T2a807tvLoY0IgHt87kZcNOIW_mUo-pfCRD1y7qPQU-zdvyEZ_2OatU3PcVb5VjjR4xy2DqaiwUrv1Xz7NwRUoavEnbgvXZyJuwo2_DGb6yrZeLxIKmsugKFhgDltnDqeMf1IJZupIj9v_5pAbw6O4Vyzno9zprxDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/24691" target="_blank">📅 20:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله
ایرانی سیتیزن بریتانیا
را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در لندن بازرسی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/24690" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/24689" target="_blank">📅 20:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: موضوع ایران می‌تواند به انتخابات میان‌دوره‌ای آسیب برساند
@WarRoom</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/24688" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24687">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ برای سومین بار اعلام کرد ایران موافقت کرده است سلاح هسته‌ای نداشته باشد
؛ او پیش‌تر در ۳ ژوئن گفته بود «آنها قبلاً موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند» و در ۱۵ ژوئن نیز تأکید کرده بود ایران «کاملاً» با این موضوع موافقت کرده است. ترامپ امروز، اول اکتبر، بار دیگر در اظهارات خود درباره ایران تأکید کرد که تهران نباید به سلاح هسته‌ای دست پیدا کند.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/24687" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/24686" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7423fb5452.mp4?token=XbYXFalxZyTf3KDRhQFARcq0kERFHKE216nyGJA4u1v1x4Og2-xATeM69BqqzRXlHeDqHmnzsIOkKwaLbAx2x67zOb_YquE5qavTD8Ho_d-6fxDyX1s9FRgCclqcMLXB391MznvwnnGgC03app8oX5j-ZoFU2BaYTj3BzcWOsAS5xLdOoX7AH5Dy62_45MdLWniSSwRCku8hJ0npTX_fnPuWlwYZG_ffKKBanNcnEaaj-lGr5tNLWa7bsVD3pZ7_S2-XGNr3bymQfrWyJv-lABX-gCTd_Kz51mnQmfEBBr_xC_VOdUR5fQzrnAeLbOpTcKp_5mAydwYi18B-CRjSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7423fb5452.mp4?token=XbYXFalxZyTf3KDRhQFARcq0kERFHKE216nyGJA4u1v1x4Og2-xATeM69BqqzRXlHeDqHmnzsIOkKwaLbAx2x67zOb_YquE5qavTD8Ho_d-6fxDyX1s9FRgCclqcMLXB391MznvwnnGgC03app8oX5j-ZoFU2BaYTj3BzcWOsAS5xLdOoX7AH5Dy62_45MdLWniSSwRCku8hJ0npTX_fnPuWlwYZG_ffKKBanNcnEaaj-lGr5tNLWa7bsVD3pZ7_S2-XGNr3bymQfrWyJv-lABX-gCTd_Kz51mnQmfEBBr_xC_VOdUR5fQzrnAeLbOpTcKp_5mAydwYi18B-CRjSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین , رئیس‌جمهور روسیه
: اگر صحبتی از حمله مستقیم به فدراسیون روسیه، به کالینینگراد برسد، استفاده از تمام تسلیحات موجود در زرادخانه ما، اجتناب‌ناپذیر و فوری خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/24685" target="_blank">📅 19:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: گروه حوثی با استفاده از یک پهپاد، ایستگاه توزیع برق "طیبه" در شهر مدینه منوره را مورد هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/24684" target="_blank">📅 19:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLnVgIk5urBRxsw-GgQqB32plQqWreSY8m3MLyGwFDvUmNUyI_Jl5X08AR4rUxIMuI52BaxR_CCBXiO7q9UGugvpN94SUPj_vdssRrYj-uWWT8OazCITN5a9x9TogwSIblmpbrqEvq0yexz4rlWdZDlpVG0Q4RgbEJPAAYRh9PgGtie71ITdnU0E3in_bX414fL5C1GjL0j1z8KQpbmZVrCvcm-Q7OS_qSIjxpjCd3coeaeDkvGxIVDzW8lMWdgjxqhv67SYqhX-lJVzOB-kuxy7CO8auTWlE5RFYzhZSmC-zTJpGnc_UecOMgwfJ0BQlvkIxakNRziNFlL-GeP2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یک جنگنده‌ی A10 که از درگیری با ایران برگشته! نشان های پرتاب بمب‌های جیدم و sub به همراه کیل مارک«نشان نابودی» دو قایق تندرو سپاه را هم بر بدنه دارد!
@WarRoom
🔥</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24683" target="_blank">📅 19:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41488cbe9.mp4?token=AwvEJkJRYtOCerjcWQE_hJ9ScIw9DHeW55OSZDABPQTBS-Pd4bkx0Z_UI-JlOkzuk33ih0QqWrRhTo4WrIR2WBtuRCY1Er1pl4bgx5AZNUtUmUbcS8CahBf_ldOTvc2EdvhiOZ5WaegDIKaYJxO02DTTjNyxGhD056mzVkdZ0fcvgvkTf87UEsTzFjECxCPAZ3cSx4BE9R_SSG44USoPFR-uh-jM0r8MZW_gyCBQ9lDgn7ic8FJA5XhtENA2-qkHWCntq5OISSCDAg1MKy__15uziWpxGb0ESw0DpMuVyrHkqfWSZxq11k0Brr3Sgxv5vMpjg9480koHWpVxagO2bEtptG67dOaJFM8VXXSyBPI7Wsw8BNjUDx8_YjKgaUh7xpzGeKyRVfBQV2e5Kg8FjZnixD_-NV23FtZICfcSNjIpMFMURMADUKORY9dfyeoDnjr-O2AoGDGIf1iIzXOWz6d_WntcY3XgNgiHuxZYDNvmmDimUwTxFdnVM8qlwYIQ2zl-s-wsE5u_67gdgJCqQzCrmhjjwtz-Z1V0jFcdlM7A_lq48oUcT0STFhrvKWzTNnGRzfRaq38oCZj8_Jg6dg-_jaXM1IO63lt1GRXnlzeUS8mH9iTa4kIvZ-LzE7LOZvXBKK5Nh73nxDXi_rKzvHNG8PzEfh3hS-8bcYKyi-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41488cbe9.mp4?token=AwvEJkJRYtOCerjcWQE_hJ9ScIw9DHeW55OSZDABPQTBS-Pd4bkx0Z_UI-JlOkzuk33ih0QqWrRhTo4WrIR2WBtuRCY1Er1pl4bgx5AZNUtUmUbcS8CahBf_ldOTvc2EdvhiOZ5WaegDIKaYJxO02DTTjNyxGhD056mzVkdZ0fcvgvkTf87UEsTzFjECxCPAZ3cSx4BE9R_SSG44USoPFR-uh-jM0r8MZW_gyCBQ9lDgn7ic8FJA5XhtENA2-qkHWCntq5OISSCDAg1MKy__15uziWpxGb0ESw0DpMuVyrHkqfWSZxq11k0Brr3Sgxv5vMpjg9480koHWpVxagO2bEtptG67dOaJFM8VXXSyBPI7Wsw8BNjUDx8_YjKgaUh7xpzGeKyRVfBQV2e5Kg8FjZnixD_-NV23FtZICfcSNjIpMFMURMADUKORY9dfyeoDnjr-O2AoGDGIf1iIzXOWz6d_WntcY3XgNgiHuxZYDNvmmDimUwTxFdnVM8qlwYIQ2zl-s-wsE5u_67gdgJCqQzCrmhjjwtz-Z1V0jFcdlM7A_lq48oUcT0STFhrvKWzTNnGRzfRaq38oCZj8_Jg6dg-_jaXM1IO63lt1GRXnlzeUS8mH9iTa4kIvZ-LzE7LOZvXBKK5Nh73nxDXi_rKzvHNG8PzEfh3hS-8bcYKyi-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏امیر قاسمی و رو‌کردن نام کسانی که با سپاه در ارتباط کامل قرار دارند ، آیا نفر بعدی که در ایران خواهید دید معین است؟ گزارشهایی هم هست که در کنسرت اخیر معین اجازه ورود پرچم شیر و خورشید داده نشد و فقط آهنگی برای ایران خوانده شد و در نمایشگر هم پرچمی نمایش داده نشد و اشاره‌ای هم به انقلاب شیر و خورشید نشده
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24682" target="_blank">📅 19:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مرد خردمند ، مارک لوین : مردم ایران را مسلح کنید!!!
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/24681" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏آیا سنتکام در حال آخرین تمرینات آماده‌سازی برای هلی برد در داخل ایران
ه
..!!؟
‏تصاویری از فرود دو فروند هواپیمای ترابری C-17 گلوب‌مستر III نیروی هوایی آمریکا روی یک باند خاکی غیرمتعارف در محدوده تمرینی نِلیس
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/24680" target="_blank">📅 18:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الجزیره: ناو هواپیمابر روزولت به همراه گروه ضربت خود بعد از ترک اسکله سن دیگو همچنان به سمت خاورمیانه (غرب آسیا) در حرکت است
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/24679" target="_blank">📅 18:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امشب مهلت ۴۵ روزه شورای عالی امنیت ملی برای برداشتن محاصره دریایی تموم میشه!
محسن رضایی اعلام کرده بود اگر در پایان این ۴۵ روز محاصره برداشته نشه، بصورت نظامی و با زور محاصره رو میشکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24678" target="_blank">📅 18:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70be8bbfa.mp4?token=BRCVujn4IfQwsSHtE48y2xLCzA8U6QTkBWYT_AgmAfD0eg3zPlSEQwXac6f9lJF17vjfg8aqzE4WWTECZ0z8nbkraYCExBPArcjLX_vqzjTSXtl16bwnwbXqXZhee-UsLmLdnasllcRvOMpDrI3uMHH5CrKX86vSZplLZFe7f5YWCW2fjN-Vi-op8IwF6hyq-VLvfyV0sKIvWEOl5AcrLsS1YhSG7gPeZg_ZBc8uwReoPSeqddo5RcuAzCf3SPegBSpaq8xGA7HHL-dCloLom7slLT_E5295CvJqkbsFfnVq49QVrsj7Xi2kqhaMnzYt0XrCYA8O8oGA6TYujR7cxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70be8bbfa.mp4?token=BRCVujn4IfQwsSHtE48y2xLCzA8U6QTkBWYT_AgmAfD0eg3zPlSEQwXac6f9lJF17vjfg8aqzE4WWTECZ0z8nbkraYCExBPArcjLX_vqzjTSXtl16bwnwbXqXZhee-UsLmLdnasllcRvOMpDrI3uMHH5CrKX86vSZplLZFe7f5YWCW2fjN-Vi-op8IwF6hyq-VLvfyV0sKIvWEOl5AcrLsS1YhSG7gPeZg_ZBc8uwReoPSeqddo5RcuAzCf3SPegBSpaq8xGA7HHL-dCloLom7slLT_E5295CvJqkbsFfnVq49QVrsj7Xi2kqhaMnzYt0XrCYA8O8oGA6TYujR7cxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه فارسی وزارت امورخارجه اسرائیل با انتشار ویدیویی درباره ماجرای هواپیمای کیش‌ایر نوشت: حالا که بحث هواپیما داغه، بد نیست یادی کنیم از هواپیمای کیش‌ایر که ۳۱ سال پیش در مسیر تهران به کیش با ۱۷۴ سرنشین ربوده شد. وقتی سوخت هواپیما رو به اتمام بود و خطر سقوط وجود داشت، اسرائیل تنها کشوری بود که اجازه فرود به این هواپیما داد و جان سرنشینان رو نجات داد.جمهوری اسلامی هرگز نتونست پیوند میان دو ملت ایران و اسرائیل رو از بین ببره.
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/24677" target="_blank">📅 18:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رویترز: آمریکا مصر را نقره داغ کرد
و به‌دلیل همکاری مصر در جنگ با ایران، شروط حقوق بشری (فراهم کردن شرایط نقض حقوق بشر) کمک نظامی به این کشور را کنار گذاشت. وزارت خارجه آمریکا تصمیم گرفته است شروط مربوط به رعایت حقوق بشر در مصر را برای تحویل تجهیزات نظامی به ارزش حدود ۳۰۰ میلیون دلار اعمال نکند. این تصمیم در پی نقشی اتخاذ شده که واشنگتن آن را «کمک‌کننده» توصیف کرده است؛ با این حال، جزئیات دقیق همکاری مصر مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/24676" target="_blank">📅 18:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عراقچی : سفیر بریتانیا در تهران به دلیل اتهاماتی که به ما در مورد حادثه در نزدیکی پایگاه ویرفورد وارد شده است، احضار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24674" target="_blank">📅 17:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار تایم:
پس از حملات حوثی‌ها گزارش‌هایی منتشر شد که عربستان از اینکه آمریکا از این کشور دفاع نکرده ناراضی بوده است. رابطه شما با سعودی‌ها چگونه است؟
ترامپ:
خوب است. رابطه‌ام با آنها بسیار خوب است و رابطه خوبی با ولیعهد دارم( پاسخ نمیدهد)
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/24673" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ به تایم : خیلی‌ها می‌گویند جنگ با ایران بیش از حد طولانی شده، اما ما در جنگ‌های زیادی سال‌ها جنگیده‌ایم؛ در ویتنام سال‌ها حضور داشتیم، در افغانستان سال‌ها جنگیدیم و در کره هم سال‌ها آنجا بودیم. جنگ ایران حدود شش ماه است ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/24672" target="_blank">📅 17:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ درباره ادامه دار بود حمله به ایران به مجله تایم :
من آنها را از بین بردم و می‌توانستم همان‌جا متوقف شوم، اما تصمیم گرفتم ادامه بدهم. وقتی سایت‌های هسته‌ای آنها را با بمب‌افکن‌های B-2 زدیم، آن تأسیسات زیر هزاران تن آوار قرار گرفتند. می‌توانستم همان‌جا متوقف شوم ، اما احساس کردم این کار درست نیست، چون آنها می‌توانستند به شکل دیگری دوباره فعالیت کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24671" target="_blank">📅 16:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرنگار تایم :
شما در اسرائیل بسیار محبوب هستید. آیا اگر گادی آیزنکوت رهبرحزب یاشار در انتخابات اسرائیل پیروز شود، آمریکا می‌تواند با او بهتر از نتانیاهو کار کند؟
ترامپ:
نمی‌دانم. درباره او چیز بدی نشنیده‌ام. اما نباید نتانیاهو را دست‌کم گرفت. بارها او را کنار گذاشته‌شده تصور کرده‌اند، همان‌طور که بارها من را کنار گذاشته‌شده تصور کرده‌اند. من او را دست‌کم نمی‌گیرم
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24670" target="_blank">📅 16:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره اسرائیل و ایران‌به مجله تایم :
هدف اصلی من کمک به دفاع از اسرائیل است. ایران نمی‌تواند قدرت هسته‌ای داشته باشد، چون آنها دیوانه هستند و نمی‌توان اجازه داد افراد دیوانه سلاح هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/24669" target="_blank">📅 16:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز:
چین صادرات سوخت به خارج از هنگ‌کنگ و ماکائو را برای ماه اکتبر متوقف کرده است؛ این تصمیم در شرایط اختلال عرضه ناشی از جنگ ایران و حملات به پالایشگاه‌های روسیه، می‌تواند فشار بیشتری بر بازار جهانی سوخت وارد کند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24668" target="_blank">📅 16:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng64JLq9WIvh0WVNKSdy4xnSfqhF9-FpudpTQgDjnHSNYgILWohdYmVNqiT0rNhaDEEfROD0XhOczffuE5viOY_RqekT9lhWghteRbFL1yBHAFZggtZmZTNqRof-j4nfflDBkvz6pexHowxxlvVNbpi5fxhooiLbSYMY1-DF5OeEki4Wwq3KnHCmZ-Hk0iCqavknnGWeYV2s1P1wR8l023GCG04Wr_N3iD2VCJKKJHw9Km5as4kq5eH9vBvjNzbXiueKnq6sP3xjWzfpijnsibIvXeaDlci8a0jyCotSZRt9qctYci-vv76lKu95AsoIa2-3aMOy_xsE8asq-iASIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ارتش اسرائیل دو تروریست را که در حمله ۷ اکتبر به اسرائیل شرکت داشتند، از پای درآورد. یکی از آنها در حمله به کیبوتص بئری و ربودن ۶ نفر (شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یاهل شوهم و شوشان هاران) نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24667" target="_blank">📅 16:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ در مصاحبه‌ با مجله تایم:
هزینه‌های مربوط به جنگ ایران برای ما کمتر از درآمدی است که از نفت ونزوئلا در یک ماه به دست می‌آوریم
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/24666" target="_blank">📅 16:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به مجله تایم : ممکن است ایران نابود شود ، این یک احتمال است چون احتمالا دارد پس از انتخابات میان‌دوره‌ای، حملات به ایران را بیشتر کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24665" target="_blank">📅 16:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو: ما همچنان در حال بررسی دلایل حادثه هواپیمای شرکت "فلای دبی" هستیم و می‌دانیم که کمک خلبان،
تحت یک فرآیند آموزش ایدئولوژیک افراطی
قرار داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24664" target="_blank">📅 16:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به مجله تایم: فکر نمی‌کنم ما هرگز با ایران به صلح دست پیدا کنیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24663" target="_blank">📅 16:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: «ظرف چند روز آینده متوجه میشم که آیا کمک‌خلبان ارتباطی با ایران داشته است یا خیر.»
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24662" target="_blank">📅 15:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تتر ۲۵۸،۱۰۰
بیتکوین ۸۳،۹۹۰
نفت برنت : ۹۹،۸۰
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24661" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دونالد ترامپ با روزنامه تایم: خبرنگار: آیا در نظر دارید که قبل از پایان دوره ریاست‌جمهوری خود، اعضای دولت خود را مورد عفو قرار دهید
دونالد ترامپ: بله، قطعا این کار را خواهم کرد؛ جو بایدن که به خواب علاقه زیادی دارد، برای همه عفو صادر کرد؛ من بالاترین ضریب هوشی را دارم. من بالاترین را بین همگی دارم و بسیار خوب هستم
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/24660" target="_blank">📅 15:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترابری نظامی خیره‌کننده و عجیب آمریکا از ۲۴ ساعت گذشته تا همین لحظه…
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24659" target="_blank">📅 15:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ به مجله تایم : اگر من رئیس‌جمهور نبودم، امروز عربستان و اسرائیلی وجود نداشت
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/24658" target="_blank">📅 15:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db5c82ed3.mp4?token=lHcwJP4VvhNG9s1rV7O7eVrRTLe1Xhes243i5YtTRzZtzf0CDtV1GcpthVOzQxHaPKeps88zcbfdLbXZZy72tuvoYy7TE1slKwrcCcB4g_RaLDZUzDidD-aE-Z74HW0yoEiXPWZSxBa2bkxf7d_Xj5xDrtLUwH6lfhn1I-BDs9puGMqEu4C3Zp6iWGSMtZlJD-yRc8kWu4A_CGHzSUnZ0WbyEzKeNetzt1t5oJKNdLf1XFV6t6gy6HSQINjt1spoCVhnpzT8oOa1ncQKFVjpfBgoauQiygK_SPFGbgyoqYqrT12XAe13vXv-BYJv-lXUnmZlDfeB0BPD91iTUjc6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db5c82ed3.mp4?token=lHcwJP4VvhNG9s1rV7O7eVrRTLe1Xhes243i5YtTRzZtzf0CDtV1GcpthVOzQxHaPKeps88zcbfdLbXZZy72tuvoYy7TE1slKwrcCcB4g_RaLDZUzDidD-aE-Z74HW0yoEiXPWZSxBa2bkxf7d_Xj5xDrtLUwH6lfhn1I-BDs9puGMqEu4C3Zp6iWGSMtZlJD-yRc8kWu4A_CGHzSUnZ0WbyEzKeNetzt1t5oJKNdLf1XFV6t6gy6HSQINjt1spoCVhnpzT8oOa1ncQKFVjpfBgoauQiygK_SPFGbgyoqYqrT12XAe13vXv-BYJv-lXUnmZlDfeB0BPD91iTUjc6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، درباره ایران: ببینید، ما فقط سر راه آنها هستیم. ما مانع آنها برای فتح سراسر خاورمیانه هستیم، اما هدف اصلی، شما، آمریکا، هستید. به همین دلیل است که آنها شعار می‌دهند آنها ما را
«شیطان کوچک»
می‌نامند و
شما را «شیطان بزرگ»
، و آنها به دنبال از بین بردن «شیطان بزرگ» هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/24657" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ درباره طولانی شدن جنگ با ایران: خودم خواستم جنگ را ادامه دهم
خبرنگار تایم از ترامپ پرسید: «ابتدا گفته بودید جنگ ایران حدود شش تا هشت هفته طول می‌کشد؛ اکنون وارد ماه هفتم شده‌ایم. چرا جنگ این‌قدر طولانی شده است؟»
ترامپ پاسخ داد: «فقط به این دلیل که می‌خواستم جلوتر بروم. آن‌ها را از میدان خارج کردم و همان زمان می‌توانستم جنگ را متوقف کنم، اما می‌خواستم ادامه دهم.»
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24656" target="_blank">📅 15:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: ما سلاح‌های زیادی داریم و وضعیت ما عالی است. در حال حاضر، حجم زیادی از سلاح‌ها را ذخیره کرده‌ایم و آن‌ها را نگه داشته‌ایم و به متحدان خود توزیع خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24655" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رئیس جمهور ایران: آمریکا باید از این خیال پوچ که می‌تواند ما را از طریق ترور و آدم‌کشی وادار به تسلیم کند، دست بردارد. @WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24654" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دونالد ترامپ در مصاحبه با مجله تایم: وضعیت ایران بسیار وخیم است و اقتصاد آن‌ها در حال فروپاشی است. آن‌ها می‌خواهند یک توافق انجام دهند، اما من می‌خواهم یک توافق واقعی داشته باشم.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24652" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رئیس جمهور ایران: آمریکا باید از این خیال پوچ که می‌تواند ما را از طریق ترور و آدم‌کشی وادار به تسلیم کند، دست بردارد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24651" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران : ایرانی‌ها پیشنهادی برای باز کردن تنگه هرمز ارائه کردند. من برخی از جنبه های آن را بررسی کردم، اما نه همه آن، اما به سادگی کافی نیست.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/24650" target="_blank">📅 15:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مجله تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرده است @WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24649" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مجله تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24648" target="_blank">📅 14:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد @WarRoom دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/24647" target="_blank">📅 14:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت خارجه امارات: دادستان کل دستور تشکیل تیم ویژه‌ای از دادستانی عمومی را برای تحقیق درباره حادثه پرواز فلای دبی و نقش احتمالی ایران صادر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24646" target="_blank">📅 13:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COABT9j8FQUSRTuGRLb4Wk4LigFWe2iWXXBI5NYMiipRwhMJuVBHDoe2VnYk92FpL5TZbGR94QfyeQxvw0ZaaOc0-wCIhzZJTssOsSyJriFisghFkY_O-uoZ0VAlNU2Lwf83pfBAVfFv8lhu9ObHUW9SXgfaMMKl5zfyjldIsugElo8GuS3VnwlrWLsEfXmWtBzdwAYHqlxfB_3O1Fad1EGUDNIXBvImbFD7Re64aiXd4yHK6GjtmxQ3PegrklNsEUXxKPBybJevyAH9xCM2rb1JlmEpmy7oBk4_2CnqgGn171y4KRl-PZ6O0yegiIb1_xBHZDvIFg5go70nu4g4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: احتمالا ظرف دو هفته چیزی از اقتصاد ایران باقی نمی ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24645" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ویدئوی جدید شرکت اسرائیلی XTEND؛ نمایش سناریوی عملیات نیروهای آمریکایی با پهپادهای تهاجمی در ایران:
شرکت XTEND که در سال
۲۰۱۸ در تل‌آویو
تأسیس شده و دفتر مرکزی آن اکنون در
تامپای فلوریدا
قرار دارد، ویدئویی تبلیغاتی از عملیات زمینی نیروهای آمریکایی در کویر ایران منتشر کرده است که با پهپاد شکارچی حمله ایرانی ها را دفع و با مدل انتهاری به ایرانی ها حمله و آنها را نابود میکنند. این شرکت می‌گوید سامانه‌هایش در
عملیات واقعی هم علیه ایران
استفاده شده و سابقه همکاری با وزارت دفاع و ارتش اسرائیل را دارد؛ همچنین در سال ۲۰۲۵ قراردادی برای تأمین
هزاران پهپاد FPV
برای نیروهای زمینی اسرائیل را تکمیل کرده. اهمیت این ویدئو در این است که XTEND هفته پیش اعلام کرد وارد فاز سوم برنامه پهپادهای تهاجمی
نیروهای عملیات ویژه آمریکا (USSOCOM)
شده است؛ پروژه‌ای شامل
STRIKER، Scorpio 500 و Scorpio 1000
برای شناسایی، عملیات در محیط‌های شهری و بسته که حملات دقیق با پهپادهای قابل‌بازیابی و گروه‌های پهپادی را شامل میشود
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24644" target="_blank">📅 13:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb859cb846.mp4?token=mKbWLTPHHs5VD-bq77U2l11VcgrLObsHerOepm757iGVClypmM4fbZ4pI85S00DDjrWwfopvL2hfZd67NNKVdM1wQ0UYoR9Ujp0FWtqXq8cKsyLKlQ8jfUBEXvk7FEql4X6sEthsZD-Pr46VbSxAXvKjRpIDvIf-yvcPcMCS4n7MKFG5xy_kAM9TKgMLg2VH2MhbsEHnTBBLJtfvw1HB9lYbK3lEv1O5lGml-gnZYM4-__xJUdx3KNgG1eUhEbx2OMf7a3yPVr8uPNvgsH8Q-UhmniyXXTZPVDxiJ2s5GZpK9FNowB-kbahhGul_zbWSuzs1NU2uPVXqBLrn3xIMTWbCbdUXWV79kdZwar8zOHYPqQNPXqtdWz5TlRSEXm2QUGM6cD0CK2e-kbCE5xHvPj20cUQm_xfQCym_BsBICIt-EfymiSNoIwDOSwsSviBX4E5gd4vVX7EnH7MaTEqkpR6y0waSdC-dSnXzzowhFWK20gEtdBrmzDLGOKJUWTyzhQmGXenQFCYhjioUp8Z77Gof1ClfIypETUAxN3ePzbHKTXwdFYsPs08i_9P39nH2YW0zB1O-4wN9NqqY21TjmyoY01UHba_ZF8lqzaTGTS4e4w7_i8tm-NuKV4cRnkp57MAzZmMJUoIp2jcJbDs2yLz451OmL6o3AlbOydUdO-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb859cb846.mp4?token=mKbWLTPHHs5VD-bq77U2l11VcgrLObsHerOepm757iGVClypmM4fbZ4pI85S00DDjrWwfopvL2hfZd67NNKVdM1wQ0UYoR9Ujp0FWtqXq8cKsyLKlQ8jfUBEXvk7FEql4X6sEthsZD-Pr46VbSxAXvKjRpIDvIf-yvcPcMCS4n7MKFG5xy_kAM9TKgMLg2VH2MhbsEHnTBBLJtfvw1HB9lYbK3lEv1O5lGml-gnZYM4-__xJUdx3KNgG1eUhEbx2OMf7a3yPVr8uPNvgsH8Q-UhmniyXXTZPVDxiJ2s5GZpK9FNowB-kbahhGul_zbWSuzs1NU2uPVXqBLrn3xIMTWbCbdUXWV79kdZwar8zOHYPqQNPXqtdWz5TlRSEXm2QUGM6cD0CK2e-kbCE5xHvPj20cUQm_xfQCym_BsBICIt-EfymiSNoIwDOSwsSviBX4E5gd4vVX7EnH7MaTEqkpR6y0waSdC-dSnXzzowhFWK20gEtdBrmzDLGOKJUWTyzhQmGXenQFCYhjioUp8Z77Gof1ClfIypETUAxN3ePzbHKTXwdFYsPs08i_9P39nH2YW0zB1O-4wN9NqqY21TjmyoY01UHba_ZF8lqzaTGTS4e4w7_i8tm-NuKV4cRnkp57MAzZmMJUoIp2jcJbDs2yLz451OmL6o3AlbOydUdO-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس پایانی تایتانیک…
سکانس پایانی رژیم هم یه نوازنده ویلون نداشت که اومد…
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24643" target="_blank">📅 12:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52888268eb.mp4?token=V-XewfpY6Uk3mkYq7_sB_6uDio5Vkd_pKiOWbUGg9LlARgowpB-E5DvuRoLdXC-ryVJht-YED4VKufAZ_OYrjvxIfOiumOSAr3q7yXxSb0DBJQXJlbq9ksWLgcnGalxeZm4A0YY61-gxaaRMh56SBunJHoyAwOxIfGHJoLufWALGHUlrBry1FI41AZuSE-bG5lRaLjiLG1S5Rst5vGXWPmGmNmgpskVml46geJYBLFzao_JErbYzwTX6EQN2dOQKrbKFKRlVJtw-aajQiSCjBfm-5AzvhmrUKti5G_oSMf4Qck6OOhFrDcR5Rh3reMW3AmtWPD4cv6-fxHpjtoyDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52888268eb.mp4?token=V-XewfpY6Uk3mkYq7_sB_6uDio5Vkd_pKiOWbUGg9LlARgowpB-E5DvuRoLdXC-ryVJht-YED4VKufAZ_OYrjvxIfOiumOSAr3q7yXxSb0DBJQXJlbq9ksWLgcnGalxeZm4A0YY61-gxaaRMh56SBunJHoyAwOxIfGHJoLufWALGHUlrBry1FI41AZuSE-bG5lRaLjiLG1S5Rst5vGXWPmGmNmgpskVml46geJYBLFzao_JErbYzwTX6EQN2dOQKrbKFKRlVJtw-aajQiSCjBfm-5AzvhmrUKti5G_oSMf4Qck6OOhFrDcR5Rh3reMW3AmtWPD4cv6-fxHpjtoyDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیلی مک‌انانی
،
فاکس نیوز:
«واقعاً چقدر ساده‌لوحانه است که فکر کنیم شعار «مرگ بر آمریکا» معنای دیگری دارد؟ سپاه پاسداران می‌گوید این شعار هیچ خصومتی با مردم آمریکا ندارد، اما هم‌زمان از آمریکایی‌ها می‌خواهد علیه دولت ترامپ موضع بگیرند. انتخابات آمریکا پیامد دارد؛
ایران این را می‌داند، کارتل‌ها می‌دانند و چین هم می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24642" target="_blank">📅 12:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60c71917d.mp4?token=N9kU4WTOvgcwPYA3GnCFlqPdq8Srd_BM8ZDzmzRCZnmNxYfWafHlrqV47amwdOwIeWq4yNDc4FgdI3e0kmBhHEg_sehbbPuhjlHQc0gR7BnWWFs9zDDyEQmQcMe4s-WfqvJFWf8moBVwk3kUkn5iT2SkLKnnPm0E1j-Vx8R9mrrU4GmqIXAjzz8Ia3nUl3cGz3_w4IOz-gjCs_TOgt9DP8X8SqSRhd0DFwviuwDaojYLkSSEwsJ42-PdKVEi7MFy6i_dbxLsfy1wLwKLGeK-gN-5zQgSDOuj3KoGhBIJ3n9qvD9SiqUJiIK4AxmLeO8kHRxenlrRN9pqzJ7O0AA7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60c71917d.mp4?token=N9kU4WTOvgcwPYA3GnCFlqPdq8Srd_BM8ZDzmzRCZnmNxYfWafHlrqV47amwdOwIeWq4yNDc4FgdI3e0kmBhHEg_sehbbPuhjlHQc0gR7BnWWFs9zDDyEQmQcMe4s-WfqvJFWf8moBVwk3kUkn5iT2SkLKnnPm0E1j-Vx8R9mrrU4GmqIXAjzz8Ia3nUl3cGz3_w4IOz-gjCs_TOgt9DP8X8SqSRhd0DFwviuwDaojYLkSSEwsJ42-PdKVEi7MFy6i_dbxLsfy1wLwKLGeK-gN-5zQgSDOuj3KoGhBIJ3n9qvD9SiqUJiIK4AxmLeO8kHRxenlrRN9pqzJ7O0AA7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏درگیری مسلحانه شدید در زاهدان ادامه دارد ؛ صدای تیراندازی و شلیک آرپی‌جی
‏از حدود ساعت ۶ صبح درگیری مسلحانه میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح بومی در منطقه منزل‌آب زاهدان آغاز شده و همچنان ادامه دارد. صدای تیراندازی سنگین و شلیک آرپی‌جی از منطقه شنیده می‌شود و تاکنون گزارشی از شمار کشته‌ها یا مجروحان منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24641" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آسوشیتدپرس:
ایران تأیید کرد پاسخ رسمی آمریکا به پیشنهاد تهران برای پایان جنگ را دریافت کرده است؛ جزئیات پاسخ هنوز منتشر نشده و موضع ترامپ درباره این طرح همچنان منفی است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24640" target="_blank">📅 11:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد @WarRoom دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24639" target="_blank">📅 11:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد
@WarRoom
دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24638" target="_blank">📅 10:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آژانس ایمنی هوانوردی اتحادیه اروپا (EASA):
توصیه‌های محدودیت پروازی بر فراز
ایران، عراق، لبنان و آب‌های سرزمینی خلیج فارس و دریای عمان در محدوده بحرین، کویت، قطر، امارات و عمان
تا
۱۶ نوامبر
تمدید شد. EASA همچنین از امروز محدودیت جداگانه‌ای برای بخش‌هایی از حریم هوایی
عربستان سعودی
صادر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24637" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec6681269.mp4?token=quJuWVwh-L1xwBmL10LCILWN8mFMpAG-knZc154T6suu5ETtcCyMmYnmAqzljqW8q3TOxuvacZNWvuD_f7k6dgMNzCm9Bejsuhr1DOwb5L5HPXMlWjUwAbAqkpdsD0Jo2lrRY3rcIXC5eZyyBNQ6Fu3B23xJFEJlrVt3RwtJ3A76vSuPnKslKYKb3OvHe1YPKGX8kSws1lG6UWyBwuFGQVEl0tW5k694OJVuqFKGE4LHsgABSrGIsM9NBriiMxvG8kZLxUUf4VhwFHFeCoVTSt2M4wHCtYkDC3PWck3tWUhAHdTxow3NyUot1CWfLzThbi-_b1wHd7n7eDS9XvZTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec6681269.mp4?token=quJuWVwh-L1xwBmL10LCILWN8mFMpAG-knZc154T6suu5ETtcCyMmYnmAqzljqW8q3TOxuvacZNWvuD_f7k6dgMNzCm9Bejsuhr1DOwb5L5HPXMlWjUwAbAqkpdsD0Jo2lrRY3rcIXC5eZyyBNQ6Fu3B23xJFEJlrVt3RwtJ3A76vSuPnKslKYKb3OvHe1YPKGX8kSws1lG6UWyBwuFGQVEl0tW5k694OJVuqFKGE4LHsgABSrGIsM9NBriiMxvG8kZLxUUf4VhwFHFeCoVTSt2M4wHCtYkDC3PWck3tWUhAHdTxow3NyUot1CWfLzThbi-_b1wHd7n7eDS9XvZTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در
مورد
اسلامگرایان تندرو
:
ما در حال مبارزه با
بربرها
هستیم؛ این افراد
بربر
هستند.
(منظور او از «بربرها» افراد بی تمدن و وحشی است
)
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24636" target="_blank">📅 10:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85883a33b.mp4?token=i_zUH_pyi3q-d5YUSQhCFLMtI_KgGmt6Z_GG5cr2l7R5PWw11BolX_ZYT0O5G296wS9sqhoeh-nfOXkCkv7ArnEZPxLFzwo5llipffifToipiIwGtSehWGzr2EfEUXr5dL0lgUdYsn7SsO4f-npQhrgewin8xCD4lkjFtTcIiFAGij0SCd58FoWO1fzlnpwo_zid5nVmImFJio5T3uYPQNKmTI5R7hiFmN4E4CLHYtTIPfco0CZp_kxF6zhRB3097p85fdKnqZAM4SU72yYrX2GwxS3Nz7Kop8ZSXFhrcOFCxYhzoXtH-9nS4__KXELvoh3wHdow3ihLyAT0fSBJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85883a33b.mp4?token=i_zUH_pyi3q-d5YUSQhCFLMtI_KgGmt6Z_GG5cr2l7R5PWw11BolX_ZYT0O5G296wS9sqhoeh-nfOXkCkv7ArnEZPxLFzwo5llipffifToipiIwGtSehWGzr2EfEUXr5dL0lgUdYsn7SsO4f-npQhrgewin8xCD4lkjFtTcIiFAGij0SCd58FoWO1fzlnpwo_zid5nVmImFJio5T3uYPQNKmTI5R7hiFmN4E4CLHYtTIPfco0CZp_kxF6zhRB3097p85fdKnqZAM4SU72yYrX2GwxS3Nz7Kop8ZSXFhrcOFCxYhzoXtH-9nS4__KXELvoh3wHdow3ihLyAT0fSBJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
به CNN
:
این یک
رژیم افراطی و بی‌پروا
است و نباید سلاح هسته‌ای داشته باشد؛ این موضوع کاملاً روشن است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24635" target="_blank">📅 09:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4854e3d13b.mp4?token=nsRz6sjftTLsoQTLYYVESQtXCll_6yjh2Qi6c_Bt5bYjEQSys7Sci1PH4I6jYA4O48ze8up4XnZR1-Fg3ZSLFOtRKLhf7bSDSlUGTGGUA-AD5ySoMtjG2niu9b3R7qSohnw2hM-96y8f_H2mWYxUyHuY-CL-BnGTK0DhCjj0Z9iW-0s1c0Xr1wV1Q4Wn18ksdRHlkKmVsHjjkA0sdLhKHdk9GzlwpDWyHxusSLFjsPcp3lWzi5pao7Ai77gtqi7ABw__shWQU_UBipjwAlxEEQUbY4f3MQB6mlnleJoKBfQmGwYWDHr-C_LcLb8MTD1Oqdf3OBnYydBrViWmpmeUEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4854e3d13b.mp4?token=nsRz6sjftTLsoQTLYYVESQtXCll_6yjh2Qi6c_Bt5bYjEQSys7Sci1PH4I6jYA4O48ze8up4XnZR1-Fg3ZSLFOtRKLhf7bSDSlUGTGGUA-AD5ySoMtjG2niu9b3R7qSohnw2hM-96y8f_H2mWYxUyHuY-CL-BnGTK0DhCjj0Z9iW-0s1c0Xr1wV1Q4Wn18ksdRHlkKmVsHjjkA0sdLhKHdk9GzlwpDWyHxusSLFjsPcp3lWzi5pao7Ai77gtqi7ABw__shWQU_UBipjwAlxEEQUbY4f3MQB6mlnleJoKBfQmGwYWDHr-C_LcLb8MTD1Oqdf3OBnYydBrViWmpmeUEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره بریتانیا
و
ایران:
ما اطلاعاتی در اختیار بریتانیایی‌ها قرار دادیم که نشان می‌داد قرار است یک
حمله با حمایت ایران
انجام شود، اما تقریباً روز بعد، آنها علیه ما تحریم وضع کردند. واقعاً عجیب است؛
عقب‌نشینی و فروپاشی در برابر ائتلاف اسلام‌گرایان و مارکسیست‌ها
برای آینده غرب بسیار خطرناک است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24634" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e94c9fbb.mp4?token=UrNHLnJH3v5jU9wAtCT7neA3eMH07s2iyF8YtaS-n2zFZsy2cr36PujgbfXBMDoVcfBBY5jPqKF5BPtXSzLEHI2wyt3neEPTBqsqwl93PkoA6hO4GRSbbcLEWQ3ki7XzWW3YJ5t_rEvL0Ft7f1UnackGlk0zSaNEusRIFvWCfFNUNxTzfk-m1b5fpKibtBUoEQc5ME76E9o3a9dRqLyxCgVvCvd5DinIklqyq8y-kgtpGP1jG9EcAAinL-cIhfeQD6dUQ0K8Aa7Ve8CfFWPHHpbV8n9Kvs50138QM9juTV8iyZcsbmi94Neee-yB4HxpW2ty_7bqbVPJk5NsOpNtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e94c9fbb.mp4?token=UrNHLnJH3v5jU9wAtCT7neA3eMH07s2iyF8YtaS-n2zFZsy2cr36PujgbfXBMDoVcfBBY5jPqKF5BPtXSzLEHI2wyt3neEPTBqsqwl93PkoA6hO4GRSbbcLEWQ3ki7XzWW3YJ5t_rEvL0Ft7f1UnackGlk0zSaNEusRIFvWCfFNUNxTzfk-m1b5fpKibtBUoEQc5ME76E9o3a9dRqLyxCgVvCvd5DinIklqyq8y-kgtpGP1jG9EcAAinL-cIhfeQD6dUQ0K8Aa7Ve8CfFWPHHpbV8n9Kvs50138QM9juTV8iyZcsbmi94Neee-yB4HxpW2ty_7bqbVPJk5NsOpNtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
به CBS
:
آنها در تلاش‌اند
سلاح‌های هسته‌ای و ابزارهای لازم برای رساندن آن به هر شهر آمریکا
را توسعه دهند. این کار مدتی زمان خواهد برد، اما آنها در حال کار روی آن هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24633" target="_blank">📅 09:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919a200a36.mp4?token=cvxwDMUB1f82O2JzmeyA4s5PR8qSrZRNinOQPHM0_YQYR4LLDCuKdSw1VcgjhXXQU70N4XHmIxD61z-EBCx2wXCFQKfryiJciToG5Sl37b24uJjHLusdHbO9hZq6VxaR7ucOH7fLZO1qD3VnSvK0vI1OqGd5yOVugTAdnSTiboypscrQp2x5S1k62Bmmy3UPmoIpPQUf834IccQdsO154OIKvsZt1hrfqMvHRw4B0DwuBLkcuBUN8RbRcbO-5quKJmbZhHvMrMRMIUGg57WYWmu63BLThXXbgXy0Cr6AvhvDIkn7kgz4H8ScDEeC-ciJ48x3MiaQZadqyydpmCFY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919a200a36.mp4?token=cvxwDMUB1f82O2JzmeyA4s5PR8qSrZRNinOQPHM0_YQYR4LLDCuKdSw1VcgjhXXQU70N4XHmIxD61z-EBCx2wXCFQKfryiJciToG5Sl37b24uJjHLusdHbO9hZq6VxaR7ucOH7fLZO1qD3VnSvK0vI1OqGd5yOVugTAdnSTiboypscrQp2x5S1k62Bmmy3UPmoIpPQUf834IccQdsO154OIKvsZt1hrfqMvHRw4B0DwuBLkcuBUN8RbRcbO-5quKJmbZhHvMrMRMIUGg57WYWmu63BLThXXbgXy0Cr6AvhvDIkn7kgz4H8ScDEeC-ciJ48x3MiaQZadqyydpmCFY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
بر کسی پوشیده نیست که ایران می‌خواهد اسرائیلی‌ها را در خارج از کشور هدف قرار دهد و در داخل اسرائیل نیز به دنبال حمله است؛ ما این را می‌دانیم. در واقع، ما نشانه‌هایی می‌بینیم که نه‌تنها ایران، بلکه نیروهای نیابتی آن، از جمله
حماس و حزب‌الله
، به دنبال انجام حملاتی پیش از انتخابات هستند و ما شواهد روشنی در این زمینه داریم. اما اینکه
حادثه فلای‌دبی نیز بخشی از این طرح بوده یا نه، هنوز نمی‌دانیم.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24632" target="_blank">📅 09:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0159708785.mp4?token=GX1mR9OhK8bqiiXvyO7egNv0xyrad3PEciFX8yr8knWLXhoTCvQQK2YgGHi89Ful6_lppyusE4Bytsz1vU6g8tU-cGrCZIH_OSqRG_RM0Mz0z2jB-cM-sZGng5DKGQPS9oSpr_heb5WDB2kHMhCLAxMx5LVBkbPRwETlQ1B-TNnWqOGCF_X0-YWmszdwhaNKBHMxtyaPIq1y83MRBG6WpXYbkg78ctFULW3mMpMNqvQ9B6hfvihhrhaILhARXepzZr-kx-98roBTJzAtcqWvbVS6nOry_7ypr3ZuGNH_oiDxmisnE3vvWwjHO3ybN2y6VOietoichvHX7eLhXuER_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0159708785.mp4?token=GX1mR9OhK8bqiiXvyO7egNv0xyrad3PEciFX8yr8knWLXhoTCvQQK2YgGHi89Ful6_lppyusE4Bytsz1vU6g8tU-cGrCZIH_OSqRG_RM0Mz0z2jB-cM-sZGng5DKGQPS9oSpr_heb5WDB2kHMhCLAxMx5LVBkbPRwETlQ1B-TNnWqOGCF_X0-YWmszdwhaNKBHMxtyaPIq1y83MRBG6WpXYbkg78ctFULW3mMpMNqvQ9B6hfvihhrhaILhARXepzZr-kx-98roBTJzAtcqWvbVS6nOry_7ypr3ZuGNH_oiDxmisnE3vvWwjHO3ybN2y6VOietoichvHX7eLhXuER_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در گفت‌وگو با فاکس‌نیوز:
به ریشه این حمله‌کننده خواهیم رسید؛ اینکه آیا همدستانی داشته و آیا ایران پشت این ماجرا بوده است. فکر می‌کنم خیلی زود مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24631" target="_blank">📅 09:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واشنگتن‌پست:
به گفته یک مقام ارشد دفتر نخست‌وزیری عراق،
سپاه پاسداران تاکتیک خود در عراق را تغییر داده
و به‌جای گروه‌های بزرگ، از
هسته‌های کوچک‌تر
و خارج از ساختارهای اصلی شبه‌نظامیان حمایت می‌کند. همچنین
عصائب اهل‌الحق
حدود نیمی از سلاح‌های خود را به دولت عراق تحویل داده، اما اعضای جداشده با تشکیل
یک گروه جدید
، بخشی از سلاح‌های باقی‌مانده را در اختیار گرفته‌اند. به گفته این مقام، این گروه جدید با
سپاه و انصارالله یمن
همکاری دارد و در حملات به
زیرساخت‌های انرژی عربستان
نیز نقش داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24630" target="_blank">📅 08:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز: آمریکا برای شناسایی بهتر انفجارهای هسته‌ای، آزمایش انفجاری زیرزمینی انجام داد.
سازمان ملی امنیت هسته‌ای آمریکا در سایت امنیت ملی نوادا یک
انفجار شیمیایی پرقدرت، بدون استفاده از مواد هسته‌ای
انجام داد. هدف آزمایش، تقویت توانایی آمریکا برای شناسایی انفجارهای هسته‌ای کم‌توان و به‌ویژه آزمایش‌هایی با «اتصال کاهش‌یافته» به زمین بود؛ روشی که می‌تواند
آثار لرزه‌ای انفجار
را کاهش دهد. واشنگتن مدعی است چین در ژوئن ۲۰۲۰ از این روش برای کاهش قابلیت شناسایی یک آزمایش هسته‌ای در سایت لوپ‌نور‌ برای ‌مخفی کردن آزمایشات هسته‌ای استفاده کرده است؛
چین این اتهام را رد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/24629" target="_blank">📅 08:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe0100bea.mp4?token=PTthmjGzBIkYQ5jZ1HyZAnQ5M8chNnsfJnWq9UcgyEQGXEiAb3eu9D_BdI7IYTSKcUJ8832_P65X2y4eaaWnHKXmc-y6CGP6sAdw43MvU6WdOi_g2-0hz3ocXfaACYd87pQBKZXn917qSGt73PwWyOI2EB2SRqrR2cw5uUk3BPJIINAfKnElCClhkf_1ZLMHU_E2VlzpOfZ2JDtSuzGK3VMkK44aKVe42D_q60WdgHaAceUTlhzEYR5xZB5PovCk2SrfKsELOe7jcSqR2yt_kzTUcBsTPot1x5C3xvd7Bho-9snUbH5CnGla3gqHGTgGdeSN6LT5VZAIkmSVzyLnHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe0100bea.mp4?token=PTthmjGzBIkYQ5jZ1HyZAnQ5M8chNnsfJnWq9UcgyEQGXEiAb3eu9D_BdI7IYTSKcUJ8832_P65X2y4eaaWnHKXmc-y6CGP6sAdw43MvU6WdOi_g2-0hz3ocXfaACYd87pQBKZXn917qSGt73PwWyOI2EB2SRqrR2cw5uUk3BPJIINAfKnElCClhkf_1ZLMHU_E2VlzpOfZ2JDtSuzGK3VMkK44aKVe42D_q60WdgHaAceUTlhzEYR5xZB5PovCk2SrfKsELOe7jcSqR2yt_kzTUcBsTPot1x5C3xvd7Bho-9snUbH5CnGla3gqHGTgGdeSN6LT5VZAIkmSVzyLnHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری سی‌بی اس: چه چیزی شما را مطمئن می‌کند که حادثه فلای دوبی یک اقدام تروریستی بوده است و نه یک مشکل روانی؟
نخست‌وزیر اسرائیل، نتانیاهو: خب، ممکن است اینطور باشد. من نمی‌دانم. به زودی متوجه خواهیم شد.ما نشانه‌هایی داشتیم که ایران، و به ویژه از طریق عوامل خود، قصد داشت حملات تروریستی علیه اسرائیل و شهروندان اسرائیلی در خارج از کشور را افزایش دهد.اما فکر می‌کنم که هنوز خیلی زود است که بگوییم آیا در این ماجرا همدستی ایرانی وجود داشته است یا خیر. فکر می‌کنم به زودی متوجه خواهیم شد
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24628" target="_blank">📅 08:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae8a735a2.mp4?token=K6yCyX_h1RbvhVVF-SYamT7EM1T2dveVHqrkurXeBLgwqb4rec2weN_atAGPV-W7d_1yYtll6mrJ7qtcOIvsChId8GH8BBxfsudbpLumcqaWiBV2XLjc17RVExRnMYslPEMm8aB6sWmQ0FxD3UiO_TFBmZWwZoY8Ao0RnDP_MKOP-crCeLggOAB5ZRm-7TI8tUu2_2EkRNti6RZYPVQ_IkD-MumFfEpSLp0D5PHUCFI-gefViglBB4auGlC3Y-c3RUGPqVILrSIAs5_Qa1hwlE4WKwQjEda5zMg1tNeh_-uqi9MjjfiFU1gaaz-L42sKyw4GE9hc5Pfj0NriNusYtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae8a735a2.mp4?token=K6yCyX_h1RbvhVVF-SYamT7EM1T2dveVHqrkurXeBLgwqb4rec2weN_atAGPV-W7d_1yYtll6mrJ7qtcOIvsChId8GH8BBxfsudbpLumcqaWiBV2XLjc17RVExRnMYslPEMm8aB6sWmQ0FxD3UiO_TFBmZWwZoY8Ao0RnDP_MKOP-crCeLggOAB5ZRm-7TI8tUu2_2EkRNti6RZYPVQ_IkD-MumFfEpSLp0D5PHUCFI-gefViglBB4auGlC3Y-c3RUGPqVILrSIAs5_Qa1hwlE4WKwQjEda5zMg1tNeh_-uqi9MjjfiFU1gaaz-L42sKyw4GE9hc5Pfj0NriNusYtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری سی بی اس : آیا در حال حاضر نگران پروازهای دیگری هستید که مقصدشان اسرائیل است؟
نخست‌وزیر ، نتانیاهو: بله، ما نگران هستیم
من با رئیس‌جمهور امارات متحده عربی، شیخ محمد بن زاید، صحبت کردم و ما توافق کردیم که پروازهای شرکت هواپیمایی فلای دوبی را به مدت چند روز متوقف کنیم، تمام شرایط را بررسی کنیم و تعدیلات امنیتی لازم را انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24627" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اکسیوس به نقل از یک مقام آمریکایی:
مارکو روبیو، وزیر خارجه آمریکا، روز دوشنبه پس از به بن‌بست رسیدن مذاکرات ایران و آمریکا، از هیئت ایرانی به ریاست
عباس عراقچی
خواست
فوراً نیویورک را ترک کنند
. به گفته این مقام، مذاکرات که صبح همان روز امیدوارکننده به نظر می‌رسید، تا بعدازظهر به بن‌بست رسید. هیئت ایرانی چند ساعت بعد نیویورک را به مقصد دوحه ترک کرد. ایران می‌گوید خروج هیئت از نیویورک از قبل برنامه‌ریزی شده بود و موضوع به وزارت خارجه آمریکا نیز اطلاع داده شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24626" target="_blank">📅 08:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffd865ee13.mp4?token=vO9iDuFGJAqohQh5rakb77GtNj-0RwTsy5T9g1Ibhwj6xhwH_INHB-DDws-Y5jajmJDbE9Ebv4yZElqNbQCrsF2JRqoAzbErEj08cCTXXxjWwYyl6UpCzzwtMd7sLcKOccrjb23LhyqXJj4FoGYW2Ib54ZaFwhJpcvUmJpzG3ku35tz4IqJXS5QMc1S-In3tUYyE0ETLMo-6iBCYzi7fvps_Smbe-snlSRpD3tioAMjxphC4Krs4dpWCyld4FwZm2zfHKMl3jTzTuhFi3DGlIsGuozFAKZLr9xHXKO4NwBi70nF29zwrKGS_6AP5Md06smMba1lJ6sgL7gD2MnmCyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffd865ee13.mp4?token=vO9iDuFGJAqohQh5rakb77GtNj-0RwTsy5T9g1Ibhwj6xhwH_INHB-DDws-Y5jajmJDbE9Ebv4yZElqNbQCrsF2JRqoAzbErEj08cCTXXxjWwYyl6UpCzzwtMd7sLcKOccrjb23LhyqXJj4FoGYW2Ib54ZaFwhJpcvUmJpzG3ku35tz4IqJXS5QMc1S-In3tUYyE0ETLMo-6iBCYzi7fvps_Smbe-snlSRpD3tioAMjxphC4Krs4dpWCyld4FwZm2zfHKMl3jTzTuhFi3DGlIsGuozFAKZLr9xHXKO4NwBi70nF29zwrKGS_6AP5Md06smMba1lJ6sgL7gD2MnmCyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الان تنگه هرمز تو دستمونه، عملاً اونو اداره می‌کنیم و کنترل کامل در دست ماست؛ البته می‌دانم که این وضعیت همیشه می‌تواند تغییر کند. کافی است یک مین بندازند؛بنابراین اگر واقعاً مین باشه، شرکتها حاضر نیستند کشتی‌های یک میلیارد دلاری خودشونو از تنگه هرمز عبور بدن. اما دوباره تأکید می‌کنم ، الان نفت بیشتری از تنگه در حال خروج است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24625" target="_blank">📅 01:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: من با بی‌بی نتانیاهو درباره این حادثه صحبت کردم. طبق روایتی که از او و چند نفر دیگر شنیدم، کمک‌خلبان احتمالاً تروریست یا فردی دیوانه بوده که به خلبان چاقو زده است. خلبان با وجود جراحات شدید توانست درِ کابین را باز کند و فریاد بزند. هواپیما با زاویه‌ای بسیار شدید رو به پایین می‌رفت و سکان عقب آن نیز آسیب دید. یک لوله‌کش اسرائیلی که هرگز هواپیما نرانده بود، متوجه ماجرا شد، وارد کابین شد و کمک‌خلبان را با وجود فشار جی از صندلی بیرون پرت کرد و با کمک مسافران او را مهار کرد. سپس این مرد قوی با وجود نداشتن تجربه پرواز، اهرم کنترل را بالا کشید و توانست هواپیما را پیش از سقوط دوباره متعادل کند.وقتی از او پرسیدند چطور این کار را انجام داده، گفت برنامه «سوانح هوایی» (Air Disasters) را تماشا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24624" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ea45ed0.mp4?token=ifpJEFqd-d8gEWqsn5wXzSApzL7bscw-LuXvRMb9UikaKZnsDWabBeMtmmJM_EbANSTav0ZFWEAiLM7TDOKzIK_mgSeCxe2n0oR0IT0pmApKWAXgKjihylhD7vIMbmkTXxI-F4tfaq-kzcL7BV9mkYOd3l-pw1Yqqkuxj2YtWKXesKBa3GAA6OXXhV-KlqnetK1MSdNHmkKoLoxWsJDREPOG5--xdQl95MZGob4X4G59R0k0aotqm4PNvE5tbfQviYqkEb6AyiXsWmHDGpG8ZBJ7CVnMD33550UakOafzK5n7YTXRRpEpIUL6w24RMMQPozSUGfMNa8LhvmOI8bN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ea45ed0.mp4?token=ifpJEFqd-d8gEWqsn5wXzSApzL7bscw-LuXvRMb9UikaKZnsDWabBeMtmmJM_EbANSTav0ZFWEAiLM7TDOKzIK_mgSeCxe2n0oR0IT0pmApKWAXgKjihylhD7vIMbmkTXxI-F4tfaq-kzcL7BV9mkYOd3l-pw1Yqqkuxj2YtWKXesKBa3GAA6OXXhV-KlqnetK1MSdNHmkKoLoxWsJDREPOG5--xdQl95MZGob4X4G59R0k0aotqm4PNvE5tbfQviYqkEb6AyiXsWmHDGpG8ZBJ7CVnMD33550UakOafzK5n7YTXRRpEpIUL6w24RMMQPozSUGfMNa8LhvmOI8bN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
شما حاکمان ایران را دیوانه توصیف می‌کنید. چطور می‌توان با افراد «دیوانه» به توافق رسید؟
ترامپ:
«شاید آنها را
بمباران کنیم
. باید درباره این موضوع تصمیم بگیریم؛
یا آنها را بمباران می‌کنیم یا به توافق می‌رسیم.
زمان تصمیم‌گیری نزدیک است.
این ماجرا خیلی زود به پایان خواهد رسید.
»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24623" target="_blank">📅 00:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a58f7f7c.mp4?token=d6xqcVNgQb0WrdHAPk-IJMpoVvwZ4rkVI5QXreZYOASLqS7ocoKTRHvLBiM6ikB5IovACfXU5tWjANGM6eV6-jbLVaUbI8RjOIFbb8QhD-tfebdmObZFSMeyPPKjmK4BOx9uZ96j3sFFdeQgLl7xw4qx8ySzOPYwcl5fq7m20xp5EErpeWWBY5u5VNH8PwbIBA_xx7ozthGQ_8_UrEwfEK2iMC7_FHNajmKmYkSvbdON9nY6x_Z8nM6UqaURto0ngeoEkC81Q0awuNlqksdkSikj-c4nAEhXjgscIhR5RiRQi-Fkz-KevateMsR5BduLeDDJWuH0XAkB0VvVMNA6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a58f7f7c.mp4?token=d6xqcVNgQb0WrdHAPk-IJMpoVvwZ4rkVI5QXreZYOASLqS7ocoKTRHvLBiM6ikB5IovACfXU5tWjANGM6eV6-jbLVaUbI8RjOIFbb8QhD-tfebdmObZFSMeyPPKjmK4BOx9uZ96j3sFFdeQgLl7xw4qx8ySzOPYwcl5fq7m20xp5EErpeWWBY5u5VNH8PwbIBA_xx7ozthGQ_8_UrEwfEK2iMC7_FHNajmKmYkSvbdON9nY6x_Z8nM6UqaURto0ngeoEkC81Q0awuNlqksdkSikj-c4nAEhXjgscIhR5RiRQi-Fkz-KevateMsR5BduLeDDJWuH0XAkB0VvVMNA6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«
رهبران ایران به‌شدت برای حفظ کنترل در حال مبارزه هستند، اما کنترلِ چه چیزی؟
»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24622" target="_blank">📅 00:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76e3f894e7.mp4?token=Z83Obsix7iYk99sLIsePv68UVESlSJ-FZ_rqHKqvtW3KEPYhqGmedGUSrPwxIUscGzJ81QrrdZiE_PZx1fdry6tI8Ks_SkbE1l7MaTdbfWeT_YxMuPu0Hro9d54h4x7Lwl44ls9X5nzYnpI-QwH4iuGu_TxvuiXQXgvXXbZlzGZkAbiOUbh46OkaFem4cZwfOfirIUpYqvJ_jtde3jSnMYJj1oet8GS_3iIpU_-HQMRUcQqHMhSN3x8KzLrH76YkuoAeFwabqwNmUMIP14ZnZ-7bxWXiuSkj7AAi_RPT9-kLzuLftZcpCI2TcThNAhulNGmg76UsgQiKNXi5Hhe_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76e3f894e7.mp4?token=Z83Obsix7iYk99sLIsePv68UVESlSJ-FZ_rqHKqvtW3KEPYhqGmedGUSrPwxIUscGzJ81QrrdZiE_PZx1fdry6tI8Ks_SkbE1l7MaTdbfWeT_YxMuPu0Hro9d54h4x7Lwl44ls9X5nzYnpI-QwH4iuGu_TxvuiXQXgvXXbZlzGZkAbiOUbh46OkaFem4cZwfOfirIUpYqvJ_jtde3jSnMYJj1oet8GS_3iIpU_-HQMRUcQqHMhSN3x8KzLrH76YkuoAeFwabqwNmUMIP14ZnZ-7bxWXiuSkj7AAi_RPT9-kLzuLftZcpCI2TcThNAhulNGmg76UsgQiKNXi5Hhe_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
اندی برنهام گفته است که
ایران در حادثه پایگاه هوایی RAF فرفورد
نقش داشته است.
ترامپ:
«ما در حال حاضر در حال بررسی این موضوع هستیم.
خیلی جدی در حال بررسی آن هستیم.
ایران در حال حاضر
مشکلات زیادی دارد.
»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24621" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93e19363c.mp4?token=s4y2NUTKhVkSB89_sPt9FEk8kAAOI7pfNy3Q4VxoeHyZD40o2YeVsOo-2RYaEanP1G7kBHXdSJ9C4EsLQMczp6RxKMaBWYCVSUvvXOUav9-t528JmmRKUKeLgvvA_00dDE2xrohkVbyuzXnNTRG5bU4DIgtjTelBBxZooe9hkCOaOY85shiniGLIk1kF6dUQiK3Iyq8_9tEOwddYTFSvhNBGrE6D4xnfnyM84aPszLaMh7QZXTotaX6zs_D44gBI21lH832fgeLcU3cdiUEwJAFO6VDpb2JK0-s5J_cPVjKuu3caZXaqfnIupp3ISdkyAyAQO3Dwjpanv8C1FGSDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93e19363c.mp4?token=s4y2NUTKhVkSB89_sPt9FEk8kAAOI7pfNy3Q4VxoeHyZD40o2YeVsOo-2RYaEanP1G7kBHXdSJ9C4EsLQMczp6RxKMaBWYCVSUvvXOUav9-t528JmmRKUKeLgvvA_00dDE2xrohkVbyuzXnNTRG5bU4DIgtjTelBBxZooe9hkCOaOY85shiniGLIk1kF6dUQiK3Iyq8_9tEOwddYTFSvhNBGrE6D4xnfnyM84aPszLaMh7QZXTotaX6zs_D44gBI21lH832fgeLcU3cdiUEwJAFO6VDpb2JK0-s5J_cPVjKuu3caZXaqfnIupp3ISdkyAyAQO3Dwjpanv8C1FGSDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۸ نفر از نیروهای بسیار خوبمان را در درگیری با ایران از دست دادیم؛ از دست دادن حتی یک نفر هم زیاد است. اگر به عراق نگاه کنید، ۴۵۰۰ نفر را از دست دادیم، اما نتیجه آن حتی نزدیک به چیزی نیست که اینجا به دست آورده‌ایم. ما در عراق برای نابودی داعش وارد شدیم و من در دوره اول ریاست‌جمهوری‌ام این کار را انجام دادم؛ به همین دلیل آنها باید مدت‌ها پیش از آنجا خارج می‌شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24620" target="_blank">📅 00:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c295dc969.mp4?token=kz2FQQegjMZ2mf_l6n3J_Xr41fCU7hDgeKklxmjhNFxTdPQive9zzxkd2cchgwE3g5AYMLaWckQA1RGI0RNKH-mvVFKMCrRytvFPw7u8EZ19VWsrWbRRhc3EdDIofkZfLGVGzhPxeNRKbZtbzQwzLsr7LayhsOVo8NL06ZVIkgyez1m99gdbo654S2AtAAmlE0N6p0rOnL8l8PNXLOa-gydn2D4KPTL2U3DceLXcj7iutcV9ELL-B06ijeyDBO2snYO_H3gJJHmEqtgT9QIJ7m2tl_uzA28WPVCAs4EkdnkktJXtIsjLqbSDrRAI05BmjvmhLzY5_LxrHt-emAJlzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c295dc969.mp4?token=kz2FQQegjMZ2mf_l6n3J_Xr41fCU7hDgeKklxmjhNFxTdPQive9zzxkd2cchgwE3g5AYMLaWckQA1RGI0RNKH-mvVFKMCrRytvFPw7u8EZ19VWsrWbRRhc3EdDIofkZfLGVGzhPxeNRKbZtbzQwzLsr7LayhsOVo8NL06ZVIkgyez1m99gdbo654S2AtAAmlE0N6p0rOnL8l8PNXLOa-gydn2D4KPTL2U3DceLXcj7iutcV9ELL-B06ijeyDBO2snYO_H3gJJHmEqtgT9QIJ7m2tl_uzA28WPVCAs4EkdnkktJXtIsjLqbSDrRAI05BmjvmhLzY5_LxrHt-emAJlzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: رسانه‌های ما باعث می‌شوند رسانه دولتی ایران منطقی به نظر برسد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24619" target="_blank">📅 23:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری i24NEWS: در پی هشدارهای منتشر شده , رئیس ستاد مشترک ارتش اسرائیل ، سفر خود به ایالات متحده را لغو کرد
@WarRpom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24618" target="_blank">📅 23:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وحیدی: اشتراک چت جی‌پی‌تی مقوا رو از پلاس به پرو ارتقا دادیم ، علی ای حال فردا یک پیام خیلی مهم منتشر میکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24617" target="_blank">📅 22:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El7KAKB9_ovErnAnU8KfTnVwgAb2tw8JSAr0GpEU8P0kKYv53r8IQNXGM4ZIuXRnClGhMsMXEcFsz6f4RQuZEDfVrvY9bvEf9CT0sF12igcgmhx1VYfOnJVuSjfbeF1YWovsLpcGe2gNbKe_u9ahVucrMy6asNa1feBtDgy55SOMD7voqGTSociYnybhD7MpOvitrJYpCLnbNc8-9aLbld2kWQ-BOW0YIBHMO5MM7ag5sGekEx7hK6GgQsLOmF7V74IeJObQOcaajsRj7QgEfasUs0HPFXBAAlYyLCsaa11pzUvCw8rnhF2kDNtiIlX29YUVY1wlH8Xziwa5xPantA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : خلبان هندی ، ناجی جان ۱۷۴ اسرائیلی مسافر در پرواز فلای دبی شد!(پیشتر به اشتباه خلبان اماراتی معرفی شده بود) @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24616" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">روایت قهرمان ماجرا به نتانیاهو از لحظه درگیری در کابین: «فشار شدید هواپیما من را به سمت پایین می‌کشید. وقتی به درِ کابین رسیدیم، یک نفر با پیراهن سفید هم آنجا بود که فکر می‌کنم یکی از خلبان‌ها بود. خلبانی که مورد حمله قرار گرفته بود، بسیار نزدیک در افتاده…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24615" target="_blank">📅 22:25 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
