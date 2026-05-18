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
<img src="https://cdn4.telesco.pe/file/c84qBlkoJUqS5xevRdg4pJjUS8hi3-HTWIkztt7V8nlnc6MkiQ5w-NMbnTbAwFdmr69uFMCMvAfasESqapOREkXcLG2JaaeOCe0z18Kh9MbixYzKJ4GfcRfgZGPbHBOHt6vVMofsh5q19R_RiMW2tDwleF-qJtFuXFDv4z8YMhi3-4U1qfJfRVLgZScEEog34x4PUhswM1RTcUHn2uyWWANnR0_mCN5QSxCJiDTDwIogWcLogKpo9wKaLv0OvUE1f_Pr7CfBQcggOYccZahzUzG1ybQBZwQ85yT32D74o6_OPtC0MFYRb5uMC83Kat3N0lu3mIcofupI97w1yaE9aA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
🔴
اوسمار گفته اگه دوباره جنگ نشه میام و تمرینات رو اغاز میکنیم ولی اگه جنگ بشه فسخ میکنم ولی خب غرامتی نمیگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 201 · <a href="https://t.me/SorkhTimes/131853" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 321 · <a href="https://t.me/SorkhTimes/131852" target="_blank">📅 19:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 325 · <a href="https://t.me/SorkhTimes/131851" target="_blank">📅 19:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
#فوری |   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی…</div>
<div class="tg-footer">👁️ 337 · <a href="https://t.me/SorkhTimes/131850" target="_blank">📅 19:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131849">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 375 · <a href="https://t.me/SorkhTimes/131849" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=X9Pxqf62JC2wEn-fvNi9jHZlXC6Hr4Z0-tElyqxaeNCCGvkyLG5ZgDZV1BElNOMJCOb61_7W7JIyJ4mxFQxSBUyJ7y1rPpWqJsYqPdWqCpnAB9EHbI_igKvLYIC6x45XWvNI20bpaQ5PWzeBJPeXNpOF2A6mRNuSOkbeZ9UXsqoV-VmlyA2qWIbEaX9_VwO2PFKMKuCD2qYKyRByRsAcHs55U5tChrirVFe1tpUek1qwiBbj5kHSxSda11VN5J1zvVviwcF4jCT2TnOICbrHuZr3RhbiFyohl2x-hj9DkVQH4Y5d_ElKvCoNX6xDAqdrk0Xg9_nFHabkVlE9ypWKug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=X9Pxqf62JC2wEn-fvNi9jHZlXC6Hr4Z0-tElyqxaeNCCGvkyLG5ZgDZV1BElNOMJCOb61_7W7JIyJ4mxFQxSBUyJ7y1rPpWqJsYqPdWqCpnAB9EHbI_igKvLYIC6x45XWvNI20bpaQ5PWzeBJPeXNpOF2A6mRNuSOkbeZ9UXsqoV-VmlyA2qWIbEaX9_VwO2PFKMKuCD2qYKyRByRsAcHs55U5tChrirVFe1tpUek1qwiBbj5kHSxSda11VN5J1zvVviwcF4jCT2TnOICbrHuZr3RhbiFyohl2x-hj9DkVQH4Y5d_ElKvCoNX6xDAqdrk0Xg9_nFHabkVlE9ypWKug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
|   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی غرامت با تسهیلات اقتصادی بحث شده است.
🔻
این پیشنهاد بر ضرورت تضمین‌های بین‌المللی، تفکیک مسیر دریایی از پرونده هسته‌ای و نقش‌آفرینی پاکستان و عمان در مدیریت تنش‌های تنگه هرمز نیز تأکید دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 596 · <a href="https://t.me/SorkhTimes/131848" target="_blank">📅 18:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 555 · <a href="https://t.me/SorkhTimes/131847" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcExj_XQieZR08aeByLt558PvBAY6XYAUfHzSECykVMqbpTAKdL8EHn0zIPEzuGVapy87eMGgEUjNS-4LKu0dFnUWDFFXrinzCXYxOwdD5wAYPLSGEzrvjbs_9H1VgBYmFJvPVRJr2q1TW25kaqEcd51acCJOAVH5HsWd1LZpMv_WFtnSa9OGR8ylgNEWVfuAtceM6a-p9Ffw79-UB_ej8FXk6sBxz-XBJznuUaAxrGs9tkrQxfsyvp5RjaVS7eKQWaA534rXNBFEM_MwNpw0_BQClpnpZm3Jg6LQTzK_jqnK-UARZFlFuLJUzvYYupW9f5vRBMjRiHSFyIoZ4kl6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مدیرعامل پرسپولیس عضو هیات رئیسه فدراسیون هاکی شد
🔺
پیمان حدادی مدیرعامل پرسپولیس با بهرام قدیمی رئیس فدراسیون دیدار و گفت‌وگو کرد. بعد از این دیدار قدیمی با اهداء حکمی، حدادی را به عنوان عضو هیئت رئیسه فدراسیون هاکی منصوب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/SorkhTimes/131845" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89becc508b.mp4?token=ol2_AEiF_9czbqA9SG-4sR7sauun_ogYw0faA2hFDha2a1Jspg896sMae0PWQyn0qv33RyYcz7Z2-yoO1hhb5YYOxKgqnmhJ8iDC8s4003HCoqOiCbqSLMiY0U49lIfUS1MUk6Gsd_0SFZRjz8UQknnF7TEPjFwkmscaWv-kkpdiZOVNc1_BvGHqDz9gTUmGsPrhkWq46E6Ixxv1PXjkYYSdVaqO8xw8CS91rwi40QptNR3NJBj1VOJ17pwiys28JAyzd1qv3vvXTiOWXu0ePYPNIrNJLrgpkD-qVJBa5Wq2ENUb5haHQJrju3mkblrLDUJ2qLSSCPTxV5IJdHTPk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89becc508b.mp4?token=ol2_AEiF_9czbqA9SG-4sR7sauun_ogYw0faA2hFDha2a1Jspg896sMae0PWQyn0qv33RyYcz7Z2-yoO1hhb5YYOxKgqnmhJ8iDC8s4003HCoqOiCbqSLMiY0U49lIfUS1MUk6Gsd_0SFZRjz8UQknnF7TEPjFwkmscaWv-kkpdiZOVNc1_BvGHqDz9gTUmGsPrhkWq46E6Ixxv1PXjkYYSdVaqO8xw8CS91rwi40QptNR3NJBj1VOJ17pwiys28JAyzd1qv3vvXTiOWXu0ePYPNIrNJLrgpkD-qVJBa5Wq2ENUb5haHQJrju3mkblrLDUJ2qLSSCPTxV5IJdHTPk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
قلعه‌نویی: امیدواریم ویزای ۲۸ بازیکن را بدهند/ ۴۰ درصد عقب‌ماندگی بدنی و فنی داشتیم که ۲۵ درصد آن را جبران کردیم/ شرایط سخت است ولی نباید بهانه بیاوریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/SorkhTimes/131843" target="_blank">📅 17:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=OwzzY-UEy-2nzqILeoPRXFX_Q1gc0EmqB3e7KbKheUwYKBAvTiHsndgJTP8WHCp1p2BbOGUmek8sWPUmw61OZYkyRcNjIHReGq1mtY3ifeWpohJ9nh7X1R_3eX76g7q9PzzppzVWKBVEfozrudpGfExvb6YAMWxY0rolzhYsRS6QqDl7dDv_0i0r38EGpywYgP-WvpLva-5JaRa52A3dXbeTsxqQr9L84qfS_jKDK9pfbTTi_ktJPG1b7sFHko6QWEk4BGAA0DK0TS1BQMd37JLmLPJtkXs-QEnK7MVMhf2_AIZAoK3owtuGKM8cqEp3lipXGdy11p5wrc1sw2cOVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=OwzzY-UEy-2nzqILeoPRXFX_Q1gc0EmqB3e7KbKheUwYKBAvTiHsndgJTP8WHCp1p2BbOGUmek8sWPUmw61OZYkyRcNjIHReGq1mtY3ifeWpohJ9nh7X1R_3eX76g7q9PzzppzVWKBVEfozrudpGfExvb6YAMWxY0rolzhYsRS6QqDl7dDv_0i0r38EGpywYgP-WvpLva-5JaRa52A3dXbeTsxqQr9L84qfS_jKDK9pfbTTi_ktJPG1b7sFHko6QWEk4BGAA0DK0TS1BQMd37JLmLPJtkXs-QEnK7MVMhf2_AIZAoK3owtuGKM8cqEp3lipXGdy11p5wrc1sw2cOVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورود کاروان تیم ملی به آنتالیا برای برگزاری اردوی آماده‌سازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 628 · <a href="https://t.me/SorkhTimes/131842" target="_blank">📅 17:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#
منهای‌پرسپولیس
🚨
یاسر آسانی وینگر آلبانیایی استقلال در آستانه انتقال به ختافه اسپانیا قرار دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/SorkhTimes/131841" target="_blank">📅 16:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/SorkhTimes/131840" target="_blank">📅 16:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b213799d6a.mp4?token=J5gZYom_BdFANQW2RU_5V6CZeCaDXafT0R9yo9rqvLwpv6r_1dLzpo4VQOitDVzUILXuPCaR0pQvsGKvpJ1Drw2K1SR8sOmG7QaaPjFfakEfGYg74Hjf22LitnsatZNlcGCS_z5z3hDwlOmA5zo7JWuEKWaHIH79-6-p26HjdvrkkBsWyrlKNgNU_YpYWxV_lzhZPTU1B9EC-sZswfk5NC6UPOlCpQg3Zm-KEGsDXFE4KAFH6VYJJaL40NEFzP9YvtKxC0waNStjBfaEq1JCWYRxh7SOs6Kkh8PT5Uh6P_a6tzabnDHuYIRO5pYKqbq3_5JO1Rn3G0fW3Q2Nf-bOkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b213799d6a.mp4?token=J5gZYom_BdFANQW2RU_5V6CZeCaDXafT0R9yo9rqvLwpv6r_1dLzpo4VQOitDVzUILXuPCaR0pQvsGKvpJ1Drw2K1SR8sOmG7QaaPjFfakEfGYg74Hjf22LitnsatZNlcGCS_z5z3hDwlOmA5zo7JWuEKWaHIH79-6-p26HjdvrkkBsWyrlKNgNU_YpYWxV_lzhZPTU1B9EC-sZswfk5NC6UPOlCpQg3Zm-KEGsDXFE4KAFH6VYJJaL40NEFzP9YvtKxC0waNStjBfaEq1JCWYRxh7SOs6Kkh8PT5Uh6P_a6tzabnDHuYIRO5pYKqbq3_5JO1Rn3G0fW3Q2Nf-bOkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
| نیویورک تایمز مدعی شد:
🔻
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری جنگ با ایران در همین هفته هستند و این گسترده‌ترین سطح آمادگی از زمان آتش‌بس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/SorkhTimes/131839" target="_blank">📅 16:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
لاوروف:پروژه نیروگاه هسته‌ای بوشهر به هیچ‌کس جز روسیه و ایران تعلق ندارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/SorkhTimes/131838" target="_blank">📅 15:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🛜
سرور نامحدود 1 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 4.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/SorkhTimes/131836" target="_blank">📅 14:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:
پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/SorkhTimes/131835" target="_blank">📅 14:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/SorkhTimes/131834" target="_blank">📅 13:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/SorkhTimes/131833" target="_blank">📅 13:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN6UvuR2b6YHk2osbKlf1eex4Cm2-HwLzdBnTrL3kwkjNDJEKD7DL31Yis1NxFSBw096mCuRTlVIf1w59Us8gp3ZGWdEHTkpVPEeXs_SVJXVuTcakT3VjI3GYiCi7RN7Nab63W-llVmb8c64gKwbEVGd7pgB9qUIvwIxv7Rv8tS14KBP3nqH5cSdDhTAfUfylRFb0bBokPwn3HGN948gR-5wCXLG7M1WGcmMxgD3hKi7f5C8PmYkgoKcY5Ly4fhFXNCraDUoIHhcXcD9r7Uuv0l-yzRMYVH6ls6U7FhQT-4YR8kPkSiQLDp65eMn1Bh-45y3Pd_jrwBNTb3mUthU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار آزمون پس از خط خوردن از لیست نهایی تیم ملی برای جام جهانی ۲۰۲۶، تصویر پروفایل خود را از لباس تیم ملی به پیراهن باشگاهی شباب الاهلی تغییر داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/SorkhTimes/131831" target="_blank">📅 11:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131830">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/SorkhTimes/131830" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=miCc25-kyFnU-d7_ZLIk9U2SGYg0MxiynI5wUeNtWYIs2YakRo2-QyZ5c2pfgqJOY45YKytJekG7xv_7-QtXQTGpzrSj-Ou47zUH6YUlF6vrapT75WFUDTiAeK2yS5NIlXxxQVq-1vufQlkvGTYr_GUN827uk714N-BsV2GmIstGtK36-24POYKDQRGMx8GfbCwQe34tqewvR74dWhlRet3Sh6xxaVQlPg4Y8_YeGa6WYr9LJWl6TkaDK_qja5LREMTDhM_PyNkqwshor62KhEPQWc_RpnAeQsUGb26I_K7U8HXah1k_c_57yUXVLfoAjFdfXl5EOavq9eXM008floi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=miCc25-kyFnU-d7_ZLIk9U2SGYg0MxiynI5wUeNtWYIs2YakRo2-QyZ5c2pfgqJOY45YKytJekG7xv_7-QtXQTGpzrSj-Ou47zUH6YUlF6vrapT75WFUDTiAeK2yS5NIlXxxQVq-1vufQlkvGTYr_GUN827uk714N-BsV2GmIstGtK36-24POYKDQRGMx8GfbCwQe34tqewvR74dWhlRet3Sh6xxaVQlPg4Y8_YeGa6WYr9LJWl6TkaDK_qja5LREMTDhM_PyNkqwshor62KhEPQWc_RpnAeQsUGb26I_K7U8HXah1k_c_57yUXVLfoAjFdfXl5EOavq9eXM008floi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/SorkhTimes/131829" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0f3d0278.mp4?token=RD4d7iFMSjST25beZcM9mt8Uc57H0WXYCbdNohypmqIjHrxZh8IeeZ9zxRhuhRJ12VE62OLIVeJjJOBiqWKiUGETBNq6Ac6s7CFNM812gnOb9cSJG3Da2FXIcxhcM80D4l0_2rPw0DqhkSCexV-n8fEwdL97Ir1DKxDznyOrtQO3y60X-8C5n1_gzlnl4t0V_uUH-xu-7TzZ3WOuyf97B_LsdJX5uw1z81XgONfRdDF3TOGzfyW9WbKO_NOdY9UC9ST6YCNKajLCWotuzdh6JgPfFY2gHPrRB7Kpw70UvRO1nwov95BG18cjxMLT5ZXBUUBkKluQQH9AVqgA626oCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0f3d0278.mp4?token=RD4d7iFMSjST25beZcM9mt8Uc57H0WXYCbdNohypmqIjHrxZh8IeeZ9zxRhuhRJ12VE62OLIVeJjJOBiqWKiUGETBNq6Ac6s7CFNM812gnOb9cSJG3Da2FXIcxhcM80D4l0_2rPw0DqhkSCexV-n8fEwdL97Ir1DKxDznyOrtQO3y60X-8C5n1_gzlnl4t0V_uUH-xu-7TzZ3WOuyf97B_LsdJX5uw1z81XgONfRdDF3TOGzfyW9WbKO_NOdY9UC9ST6YCNKajLCWotuzdh6JgPfFY2gHPrRB7Kpw70UvRO1nwov95BG18cjxMLT5ZXBUUBkKluQQH9AVqgA626oCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی و امضای پیراهن تیم ملی با جمله تقدیم به ابر ملت جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/SorkhTimes/131828" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFkhRI4kvf16TWa2FQ-6MnNZwFgYe-Awdnxbd7H3ulOJwN6NeHhgwZjaxVD4KW37A-F7jz8aAlBMBWDiif-0BjCqGaxCPgAtsfm9Ou934ZKTl6oELePmtkB-wAb6p7bN4y5P2529h6h2Fpf4Y73_X0PJUCeqMBrNzNYmfk0ZZqQKF5Ux4Y2_ViXrxWZOlaF-4mtg9-4yPblAt8NZDE9F0ihvJObGIGZ3Pm7G2CsoJSg9xzTyqYrAWt7DtsVt9Qg11ffpLNs8TwSfzXRiZDJYHT9wcrmdErK1pLdSZ4NoYhW9WGtFKtkmT269rFW2ofK0ihXJqx0PhZaStaN0zAqZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ لحظه شلیک مجری شبکه افق به پرچم امارات را منتشر کرد و گفت: خواهیم دید چه خواهد شد
!!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/SorkhTimes/131826" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hju0TX71xcdMXAFALq5TjFdYtbJNZuTsYgtpzsGnCE5wBrfEjRsIqorhwjr1rCKullxC6duP6R1KJTXyja8fUHGBJKXnz-kbyVPnaoRVpz8iUKlrDHrRNpPXcRQXXGkgb2L9_QLPo572w5VbbJaPBRlZql2EagLbYko3divNeN9YIVoDAAVX8nKjJBXl8idxy_NAWK84vfgRJjRqD3JgpFqFM2CAcsMUrqkfMGOqCOVytLhqUQ0ZlWyNdR-pykG21avvDO2iw9Cyma8GKexKwrQhTwhkw1sZTNY5U_omFHBNz1oEoyLUlTa_kIS6uJO16PRNH6sMQEEdVDR8TP1PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی مدیرعامل پرسپولیس قول داده که درصورت ماندگار شدن وی در نقل و انتقالات تابستانی یک تیم مدعی و جوان را تحویل دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/SorkhTimes/131825" target="_blank">📅 10:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/SorkhTimes/131824" target="_blank">📅 10:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚪️
امیر قلعه‌نویی: ما بازیکنایی داریم که همین الان میتونن تو رئال و بارسا بازی کنن. حسین کنعانی چیزی از سالبیا کم نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SorkhTimes/131822" target="_blank">📅 08:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6uUS19z_PIDOa4GdcQVrhH514w_2_TvPURV_zk02HxE0cALsPIARjfxulQpgtb7C3O2Zp0Kk1t4BuxobSr9AZHoySSD_L1yzU5UElF6abNHgQdh1yF2mdkE7LU5OrsetvDWdHPL8bOwTMMFzyV7cW1X_akVeJdnW-Pv_NtnfLGEjIEq0X7UDMXrV0CGGv2fud6aqJpAcRrTnwdKQHzmEog7YIRwe4I3XxThMZQfkr5eyGSJVRUIDa7RJD6rbp7duFNsVR7Eq39LxFwpT7hOEG6YsRIb6y0SPIpa5SiUGJlK1InSP9bHzHTZvekhtbhGNWH5s2ttuwHqB8RAG4ldtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131821" target="_blank">📅 01:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/SorkhTimes/131820" target="_blank">📅 01:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjJMLGEXSq2g098keHz8h5KnGes_DAFCLJnnKNZMhYdBvtEqwSBVdJ2JwiFtb0-R18vg5Jeq4pEnDC0okyvsVvPWig5c3K0sutCXX0RNpTsjP8pgE7R-_ogTTMZ4Ex6bsMw38eGsWCiB-TtAmjFhSypbScFrQhLYINpR-SnmMk6aRc381lDIjnkPloQuYW0x1vPKsymlwDp-_o_aMlTIQHjHV3JMQie49FZmNCf992_uuwJKMk2nLmVWLPBoTlmP9JA0x9orUMaG1Jve4L-srZLPmFPv_22WeJxfA2wH0brztI47YS37hCAl96WIIutcOCXXVjvWuhsi71bhsNRM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فوری
| پست جدید ترامپ درباره ایران
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/SorkhTimes/131819" target="_blank">📅 01:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131818" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131813" target="_blank">📅 23:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3k8p_pQsBGLnWjJ26yVhoifISbTGfuGyz42BuvT48kDOimmz7jad4uqRO9yJKq9SrSxJsEOOUL7ZoKF4fjy1uVThP-HTuUIfgBWMpk45w8IKJ-d5AwUJ6eqhmh5fL-nGQjKLara9nanRKLnQgbMo5rZTFQtBDViLDU6s5VNMEQ7-4DaIjjVtAWZcIKott9urbh0qTWKUjKqqGuQMOhgUw9ouuybEQcDdvLsKu1IsaT4pCMNyoXgSK7UClNfgGXlG1HxQsKzT5-SzANiWa71Rfz4waLuQYXHYWJcCWIlnputBO7OC_ZUOwLxXbZKIHTzjO_lbMFd3Od_awlXIrncNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/SorkhTimes/131812" target="_blank">📅 23:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
امیررضا رفیعی گلر دوم سرخپوشان پایتخت پس از چهار سال حضور در پرسپولیس از جمع این تیم جدا خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/SorkhTimes/131811" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be_VpQTq8w4q62kK_cfUS2dagkC0fsbTOeeJgqcvogt09tS6MXZ0TiGYgv8avFT0J5Tz79KcLlRzDA1uL18JNt7J117UTP9CAIrWf7IEN9FBOD8B6RjorOOdO8UADMHrrLT3mOA9azOmRxi0q2kKwm6b_yG-2w7C071aSW1iUJR5DwmC1M7fctX5O0O9EwCHtue9tTaqdkdIFkTnnWd0AF4sNM0A9_dpjZSOaxe-7MS4-EEUaCYT6gnewIaSOUHBek4BKgBB-JRisDGlJTWEZpa7IJhYteTHfup3yP7v3TExdxJ2swdzBiTlVeLhBx9VZ5FzbWBdespaCaOsgxlaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیران باشگاه کیسه اول فصل رفتن دنبال جذب این بازیکن و براشم پیش قرارداد فرستادن با مهر و امضا رسمی ولی لحظه آخری از جذبش پشیمون شدن حالا طرف رفته از کیسه شکایت کرده و گفته غرامت 800 هزار دلاری میخوام :)
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131810" target="_blank">📅 23:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚩
🚩
🚩
🚩
#فووووری
✅
فرهیختگان خبرداد؛واسطه پیمان حدادی مدیرعامل باشگاه پرسپولیس در روز های گذشته جلساتی فشرده با مهدی تارتار سرمربی گل گهر داشته تا این مربی را جایگزین اوسمار ویه را در پرسپولیس کند!!!!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/SorkhTimes/131808" target="_blank">📅 22:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
رضا غندی پور پس از استوری علیه قلعه نویی از اردوی تیم ملی امید هم خط خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131807" target="_blank">📅 22:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131806">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131806" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131805" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131804" target="_blank">📅 22:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHs49cIhNuCLUDFrJdC17810z4TL_Inx-m7Oe4b6DXljSz0Gj_jL7xc1V_EVJirFKfr02ljvv9-Ulmao2VZNvW1raiRdoRDdQmDdaV3fQlb5Wetn22FLEbFNLTw8e5F8PZ85FqWCNQ0m9u8tgLzCJtE53n9hJX2rwjhQTAmMMqIXXniIWkaGZ41yf7pYNs6-FS2fMkUXgUXfl-NCiJlPRyIMoeY6k5NHKki-XMtMUpBBf0z8fryhwrgau3c7FPMq3BPf_qSval1LTwgGzsKrG8Ol33CxRs2l75ZZ95HMGfkkorlSjT6DoT_LqYCTMC7cyxYX_MXgq7hl8VzA1CK-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131803" target="_blank">📅 22:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
ترامپ: ایران خواهان توافقه و منتظر پیشنهاد به‌روز شده‌شون هستم؛ پیشنهادی که امیدوارم بهتر از آخرین پیشنهادی باشه که چند روز پیش ارائه شده بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131801" target="_blank">📅 22:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
بر اساس گزارش منتشر شده از
CNN
سپاه به چند شرکت نظیر گوگل ، مایکروسافت و آمازون گفته باید بابت انتقال اینترنت از کف خلیج فارس عوارض پرداخت کنید وگرنه قطعش میکنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131800" target="_blank">📅 22:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فارس: محوز حرفه ای باشگاه پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131799" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2FK0D3CMe1vOTt4cIADd6iOoV4PeqQpL3NQTIKXidF2Ot4N_KfSzRSBnZAvu7AWg-Dld9F7JC4dV87syr2w7pVV8JVmE9mXeiGGNnZRr1jShOvKupmEZONV-XlS2AqS8d0uoh9KxZL5OLkeSp4HquNoHWTno3yr_b7EDYvkUGdbJJJtyebxOCS_w8mxhF2GWc2rQ-geQvTz2LrQvSsmYQMirJWPM4233CSAiQ4MH9L2t_yXZ6BwwIAfw5NcpPbAnP4r3p6oMI59q8cfwKZjWwIovJUJeePkg64z7iE61vkhTcJbSAU8BdKv0NwaV_J18hwa3D9-l2aoYIu9Cx1qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ از طریق Truth Social:
🔺
برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
🔺
زمان اهمیت حیاتی دارد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131796" target="_blank">📅 20:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آف ویژه
🛜
25 گیگ 4T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/SorkhTimes/131795" target="_blank">📅 20:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut9E6Otsofmt8GCEyxHbC3xTgIIxkulCyEmUFqlrBBD-0kCa41eyye5YDl6hcDl3gmgQOXh27EwjjWmEPbiujmFHdY2jhKDg4Ry2aJWYDAa5KCD5M3L8lcpaRXohb8FWE-liyBwjNalFsRiCeyt296ux4gUGa_YBy5GZKgzELpClPotM40ZJDqK7z0HBuMJSUTtXlmFaJvLpbWp83myQ08XZ7-y9bxNT8TSCmejYfZOb026XFkVH0oDHqmpLv3tfB-6P7s1ER09y5eMY6uWur5SVoWohV8jT4SymOauNgrrTQMnConHeNMR4-Q7NzBRWgbkQ-_JpYFahBkfQpTeyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سه سهمیه مستقیم لیگ نخبگان برای ایران
🔺
با شکست شب گذشته النصر در فینال لیگ قهرمانان آسیا 2، حالا فوتبال ایران برای دو فصل آینده به‌صورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود.
🔺
در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات دوم شد و ایران بالاتر از قطر، رتبه سوم غرب آسیا را حفظ کرد. بر اساس سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131794" target="_blank">📅 20:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkPJeme5pE02vWl5egVHcIAQ7frdpF0BLQMqTQjxJp5-xeMPPtE3fpP38kxAqbHFcCtLUWPoX5LLMB81lB3bQWQ8e_l_ts8n1zTAbtmK1oNSlGTQBUALJzuoIcP2N7i7m3Cto7qoOyriFq8FmnQMV0RMIRVitV-TDXqtfgPlXXB39yYXDB5aI-v0loavc12yIJNiNzkkCcyXDERtO6SESYTCVxueU4tLwg-WWvmwJPQjGOfCD1KXjJ9cH5rkT7AkyNWrQvfsT5khvcNn5hUHl_RkucII4Zk8an-Z_tFxUI7GG9cznZlrCPigPlOgDDDcT-sXDi8nZ7LUCzrG_yrrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
استوری باشگاه پرسپولیس به مناسبت روز ارتباطات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/SorkhTimes/131793" target="_blank">📅 20:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
ورزش‌سه: علی پروین بخاطر افت فشار ناگهانی در بیمارستان تندیس جردن بستری شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/SorkhTimes/131792" target="_blank">📅 20:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6BzW1zBiclQxXCzVkTxxOFlG7R1Qa_EhZY9oE4C1Mv_MeMw_l-LIKHcFSGk3S29AEFFuhSsZeSGz1OmO75WOERo3KSlpEK12_MyaLGn0pR0dKQT4Sf75IF1SKV-WXeKjUbyV1Rc9q4vrdPzdWI6fW3ks1o9v8B8nYneiIaRpcXGc0SoNLUAqKWabQLXvpI-WJAFJUtrp0Zphv3cTo9Tmr8MuIKLDsRCJ7qkWjbxKLQHq-CtVBZ9049H3jrYLLZsy0mdddyDK65-7wGgA36Q9WfyB1eOLtcVJL8rfpqWa1DGWrdh-XCVVvuR0RD8WvU5bYYqFbaQl1Ml0GOWlf2Ljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابل توجه کاربران محترم وینکوبت، تمام قابلیت‌های سایت یکجا در
ربات وینکوبت
در دسترس کاربران
قرار دارد.
📌
کافیست با استارت کردن ربات و زدن دکمه‌ی وبسایت، وارد سایت بشید و به‌راحتی ثبت‌نام و پیش‌بینی مسابقات ورزشی رو انجام بدید:
👇
🤖
-
@Wincobet_bot
🎰
از پیش‌بینی مسابقات ورزشی تا کازینو آنلاین، بدون نیاز به خروج از تلگرام با مینی‌اپ هوشمند وینکوبت بازی کن!
📌
در
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131791" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl-r3kMlECLEgpjWLandVjOzEJoGJFYnzea45GQzcqhjSWvqsg1Js4zVGKNOw0DsMr0ZViElrpK_-9oRIHd2dk6c-wzeaF-a_K3Mzb-4wFrC0H9JpvMm6vxBustvHQF4k46AijDtxouZDIFU7u-Q1tBigVSns_DK0XxhRzSNnrVAR5hoZg-OaKUco-ELB8RCGbbJHt7UYK0imZ2qqpqDm3w1r5XBFmNJNvpojhNb0i_KL_sxDRC21Rd0MsYJHtrCQ4dV8k2VcNNV9pdgXC__lJFkrLfA3XjQUj0ifqYaFvTO_c69uGhJvCR1Tcwc9e8DBV95e3tL_O-bnlsFx3tsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
فووووووووووووری
🚨
مجوز حرفه ای باشگاه پرسپولیس تایید و توسط afc صادر شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131788" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
اورونوف: با پرسپولیس قرارداد دارم و فصل آینده در این تیم خواهم ماند، میخواهم با پرسپولیس قهرمان لیگ و آسیا شوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/SorkhTimes/131787" target="_blank">📅 18:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/131786" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔺
زیرنویس شبکه العربیه: از قرارگاه خاتم الانبیا به یگان های موشکی اعلام آماده باش فوق العاده شد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131783" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131782" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131781" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131780" target="_blank">📅 17:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
پرسپولیس، رکورددار تیم ملی در جام جهانی!
🔺
در این فهرست رکورددار لیگ برتر ایران باشگاه پرسپولیس خواهد بود که با خط خوردن حسین ابرقویی، حالا 5 نماینده در تیم ملی ایران دارند. این در حالی است که تیم سپاهان و تراکتور هر کدام ۴ نماینده در تیم ملی ایران خواهند داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131779" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHgs_8JGX1e7aWLHqViqhYX0NnhPnPQiTwQ3EV0GpkjHMx7_5TzRwaoTW26VWnnW0DSKlHu3MunlltLnoipBaU7nSFfyCYVoxIuYmeMeCXjggvhjAT7JQnrWzd4W9VcwZmZhyfd2rQX3HpjbNAG24tmUILrfvbeBgtjE5Oco3kM6gNt3gOscTCigmGHuVLA7sPlRwGhg-jV_5sh1BWncVNRNjOVw2mTyQpuESScdBc3oDyaijsfz6oxNurk-XT0Y9xjL1KNo_5K9r-xP-Q1_g0Hrw2w1qvudkcgKZP_zo5jgJnoGJ_zEGDwGuvmprhbgTxnmd2VZ0Hz7hw_sCNYfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اشک‌های رونالدو پس از عدم قهرمانی النصر در فینال لیگ قهرمانان آسیا؛ او در مراسم اهدای مدال هم حاضر نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131775" target="_blank">📅 14:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131774" target="_blank">📅 14:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
قرارداد علیپور دوساله دیگه تمدید شد
❌
✍️
باشگاه پرسپولیس مبلغ قرارداد علیپور رو افزایش داد و با این بازیکن برای دوفصل دیگه به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131773" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLHiZv4hSau8g9cojQF5_cvc8HaXoy7aMTOsFt5jVwEGHuRVomE3MU0qh3A0-JwsM8jYcR8SAsOM24ER-8yrvcqyXtb0t5LRjRrAsC63F4qI0E9OzJabHKnS1t_dcw8xXMuggvH1UW0OVkyUyraQPhr4q33d6vGaHk8gHZc24Du5qTbyxRxliMmn3fmV9gIloerykmmEcQwGLRyu8OmGky4dZkqQSWz4zyZx0lFGw6axaan9BQbr3XjUAJr3AgZ9GfEM1-m_CfZEx6o9s_l6HXVsbILUF3SUsFnCSAGJHeaKqRKxt2wM05t0Hh7FnQOa91T48k39cjKPlLhUsT6kMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
داداشتون رفته از استقلال شکایت کرده
😂
🔹
گویا براش پیش قرارداد فرساده بودن که جذبش کنن ولی پشیمون شدن اینم رفته شکایت کرده که پولمو میخوام
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131771" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4vER0XmnvZcj6l81OsGPXm7yqZflo4QDKusYzwupfn7-84KhbSuJ71rw7690r9BARIX6o5Ujm0sBK9ybKkmJgsYRFEk3kvvs0A8-qgzrnua_F03-_tY6qmOE3juVRiudjNMUy5evbyVSBUQYT6ULzRGAFp1mFbt4dGSvtuok4ubrZgRPGUDTg1arV02RY-diVhmWbp0x7HpxhenVtfShwRdy__TlJ60xFxPpDJKn968-enFyFKPlGjr9JK7rdS56Ocg_e16FE2m3YFJDyKwGmpIkMX3CTa0_WCVoLjRh4ZjQelUqjAxQYE4ZFRHOE_hjXFzTDqrzAK6Pi_crzym4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پپ گواردیولا اعلام کرد ؛ فصل آینده هم در منچسترسیتی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131770" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_qxBNk1lIdPQc4DoL0a3w0lcvYp4HUda34pXSCgepazpSahK5aErvVT3pts5RmmT3S7wHWO1Li8GAI2x-A6zHz0WmfyXFvaSvMrAad3hXI5QWt8EKGNjZtRPITKR4DNbL4IL62DVTnGuSnGXjnfvjTDk5cvDqMwYdrhnfdFS84zexehAO1vsg6UFzwDojZL8D13dT5b3BnGVDbKsdOKbhDmYKRTlUwkyHmiDfecqPd6DV_Phnt6RC277V7KN26h9cV941yg9Xt0GfUQ-qI2bPi_LnCr9zp_jbzf8G-4HmAORkRUU2efJRH56GmaFKDceBhHYseKBmkvy9wCBVnbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولیانوف: کارشناسان غربی معتقدند که آمریکا و اسرائیل می‌توانند حملات نظامی علیه
#ایران
را در روزهای آینده، اگر نگوییم ساعات آینده، از سر بگیرند.
💢
اگر این درست باشد، به این معنی است که آمریکا و اسرائیل از اشتباهات استراتژیک گذشته خود درس عبرت نمی‌گیرند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131769" target="_blank">📅 11:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131768" target="_blank">📅 11:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHFdpPFVL-_Nno4R3sMZLEsoMLjkED-zsSulfh8Ejd41y_jDpUDGnSYbRqNjA-99W38WPluSJ_MLb4ZtdH5BS3BMPNbjJRigiYqg5gDuQ_rcxDTB_vGrgcWI-YhnXy1FmCCBkwEn1EqTl8rJS4vsLh8kH7WR0dFFCqfm-mfcqYOlmuTawwCEwyOp-T2Xf4si0_zXXIuicpOnT0nj8BErC_r__ZqUWUY_feJDiFZdflAKznOHvhenDOmJ29Vm1WWIdTPynyDu-4BnXP3iklTI42RZRF7RjGbi5f7mdZufmVoEm4d61OuUH57iZRTbejhcS9H4c8gJQWOEb451UALIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
علیرضا بیرانوند:
▪️
سرود جمهوری‌اسلامی رو داخل جام‌جهانی با تمام وجودم میخونم و مخالفای داخل ورزشگاه هم هیچکاری نمیتونن بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131766" target="_blank">📅 09:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🟢
محمد شهباز شریف، نخست‌وزیر پاکستان، به روزنامه تایمز بریتانیا گفت: نسبت به برگزاری دور دوم مذاکرات مستقیم بین واشنگتن و تهران که منجر به صلح پایدار شود، خوش‌بین هستم.
🔺
پاکستان مورد اعتماد همه طرف‌ها از جمله ایران، دولت آمریکا و همچنین کشورهای خلیج فارس است.
🔺
تلاش‌های میانجی‌گرانه ما علیرغم تبادل تهدیدها بین دو طرف، ادامه دارد.
🔺
صلح به آسانی به دست نمی‌آید، بلکه نیازمند صبر، خرد و توانایی حرکت دادن امور در سخت‌ترین چالش‌هاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131764" target="_blank">📅 08:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtoDMJHqZQWyt_itzNdnfxPxCsn1ATpizwJYSty06HjqskjQvGIlHrk9iMDb1Pc0Ue9FiAKZgT7-aVSFdc7ToJkIlnxexXjsoFT-rkaHvNr3E7C2pXHirxdn0MN8lRlPT0vceY-Yc2Yt7XTQBFGacCUbLyKZdMXAZWZM4BTKQep9Gy1jcikNxq0NMFNxOVZWHRPjeVuyuHwigTTqhCohb_O1HNaQyqT7BpdcScS8xpZGmcB7uX6SPsdRWQ4-qaHcji96I9cUaSXkw6ggOy7ZpVK2Zpem6uEjGe4iglnI7K-AWZMAayfBF3QFStdhFnx6FYtxkREcdpBfG_I8fcIc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز داری دنبال لینک می‌گردی؟
✅
حرفه‌ای‌ها مستقیم وارد میشن!
با ربات وینکوبت، ورود به سایت فقط چند ثانیه زمان می‌بره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡
بدون فیلتر و دردسر
⚡
بدون لینک‌های الکی
⚡
فقط یه کلیک تا ورود
🎁
اگه سریع و راحت میخوای وارد شی، این همون چیزیه که دنبالش بودی!
🤖
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال وینکوبت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/131763" target="_blank">📅 01:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131762" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131761" target="_blank">📅 00:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131760" target="_blank">📅 00:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131756" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
ده دقیقه تا قهرمانی تیم ژاپنی و از دست دادن جام با النصر و رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131753" target="_blank">📅 23:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131749">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131749" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131748">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131748" target="_blank">📅 22:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131747" target="_blank">📅 22:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaeI_G8nfHzKVwr804i7aDYSyaRSRJQ-WRRGqixr8yqZ2P3-ndkUi4q9VXsJlCKNl9habpJhCGKwRYbb0fHQmqYjr4gL0xOFhFuOfGBgaQPIEcse9gXF_0wQUaO0N6qwwRpcRh-SVK6v7ZwB7ughVUf8HfrwEyBz4LJ5mMqAsVivjj0Vsk5i8tu5EisVxg2Dw1HRCEQlYwy__0dq_31E4Il_2f32G_sHRPJbXNaHPA2j6AWGSWasWcxvX_qgULsfhvltgCQVmOT_7FOKUyG2dsSXYheCs7IhBxn13U8QXafQxxKmR5UZmI_wPEFzBJYjD1G8SxPLFGTgqFylWcMD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#رسمی
تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131746" target="_blank">📅 22:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131745">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
رضا شاهرودی: میخوام بازیگر بشم
😑
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/SorkhTimes/131745" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SorkhTimes/131744" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/131743" target="_blank">📅 22:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
فرهیختگان: امیرحسین محمودی با درخشش در اردوی تیم ملی در آستانه حضور در لیست نهایی تیم ملی در جام جهانی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/SorkhTimes/131742" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131741">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰
گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SorkhTimes/131741" target="_blank">📅 22:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر از سایرین گرفته تا بتواند به برخی از مشکلات خود در کشورش رسیدگی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131740" target="_blank">📅 22:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131739">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
قدیم‌ها آب کله پاچه رایگان بود تا اگر کسی هوس کله پاچه کرد و پول نداشت بتونه بخوره.یا سوپ توی رستوران ها رایگان بود تا فقیری اگر پول نداشت حداقل گشنه نمونه.قدیمها نسیه یه امر روتین بود و جایی تابلو نسیه ممنوع نمیدیدی.
برکت وقتی از زندگی هامون رفت که دیگه به همدیگه رحم نکردیم.
‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131739" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ: اگه حکومت ایران به توافق نرسه، دوران بسیار بدی در انتظارشان خواهد بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131735" target="_blank">📅 21:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abJNy8tYHJIEGeU8ru3FSQ-GgKG0mJl6Ldo8ug66xSIeQ1tfUSlm6IGCJ8d1IpLRcDCq6sLZ3vSpBCObpQxMWyRMnKtr0Sw1RC_tCqgBCWcNIVpG92gPKdEs66QqF3Huk4WAoSrkhJZ5yS0cTcsGBLP2MM8ALl3SaT1dBJfrHLBK_YpXWGG1AtoFnMmakmrYwg_Btq6bGAflQdVTPmpHriSArAiKQW7EVdpvP78YfLIRIQdnTxG3C9gCpcppp8CTGgGdM96k53mj3yBhgrIktR5nsiEeVJwv00zTRRU7YqPw6bvQ1fe32yzxbngswsdPYUfseLWmnVGeCejjNXS5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Nassr -
🔵
Gambaosaka
🔵
فینال لیگ‌قهرمانان آسیا
⏰
شنبه ساعت ۲۱:۱۵
🏟
استادیوم
الاول پارک
⚽️
النصر حالا با رهبری رونالدو؛ در دو بازی باقی مانده از فصل مقابل اوزاکا و داماک، فرصت دبل در قهرمانی را دارد تا سی‌آرسون، اولین قهرمانی‌های‌ خودش در تیم عربی را تجربه کند.  تیم خسوس، آمار کاملاً بهتری دارد. النصر در ۱۰ بازی، ۳۳ گل به‌ثمر رسانده و سرجمع ۳ گل خورده. این آمار برای اوزاکا در ۱۲ بازی (با احتساب پلی‌آف)، ۲۵ گل زده و هفت گل هم خورده. تیم ژاپنی با فرم ضعیف‌تری به‌میدان می‌آید. اوزاکا در پنج بازی اخیرش، متحمل سه شکست شده و این آمار برای النصر، در پنج بازی اخیرش، یک شکست و یک تساوی بوده.
📌
در
ربات
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131732" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
فرهیختگان: سپاهان مشکل مالی داره و به بازیکناش گفته سقف قرارداد ۳۰ میلیارده و پرسپولیس میخواد از این فرصت استفاده کنه و حزباوی، لیموچی و یوسفی رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131731" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
وزیر کشور پاکستان یهویی و فوری وارد تهران شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131729" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
باشگاه سپاهان به مشکل مالی خورده و احتمال داره از آسیا کناره‌گیری کنه که در این صورت پرسپولیس شانس اول برای معرفی به لیگ قهرمانان آسیا هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131728" target="_blank">📅 17:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHhzS08bjQ_O4GKCHCu1Lzv2Bt_t8zwg0nPf25DqHEV5KLhGU3m-gKvcdmZcWI_jnZSAh3dVm75tVgszWvUFPjTCNEPbyIdvSX_5NmbegJZmiALIOw3q9PJghUqPwlVz1ydkWC6TvyiM8bqyp7GzQFptoi7mXCpcVs6sQkrt23R3iEYRAzkWRRJgsMD9rFyDRAcPyhx4hVnVxgBJ7jh2x5kPfO0M_dUwRvdbSidc3c7QyeqKWQ2VUcTYL6YQet7EJWWJ4UY5kx7YGsb0gTX3eC7Wy5RDgf8QowMnF-DdMJsK-USizJknAQmteTSDkxl64hHUCQkLUFzuFur9-ZNmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب میتونه یه شب رویایی برای النصر و کریس باشه. اگه الهلال نتونه امشب بازیشو ببره، النصر قهرمان لیگ میشه درحالی ک خودش داره تو فینال اسیا بازی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131727" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131726" target="_blank">📅 15:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ldHbrZnKp09Zn0ySThKNHnokyB6Vjt-7zhlLe8549PFeaEQ8VV5pQlpx_4V-388pIdww7lIf-7qcMPGUo_al4JcChtfhx0Fxlzleb92hO1GJJfvd2TQNAXdIsd0wAH2lHsMzqWQT98bXxU3o6bq6G5wGqjLQr7XmOEL1e4UUqFtzrWWJjVttVQfbFBxT8ENroKCf2XYH9paPUOjpwiwQWbNKXXbAWXQqT3Vf653Tpm0yfcPnCusR0v7JRpsfuV9OjhD5aSsYRrm-sq8c53dRArCPVl-ueOusJZHYe3OB0RxsxSnKyiPed7i6U1rcCktdCPf6684ij6S6qvSauCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مراقب پیامک‌های کلاهبرداری «اینترنت پرو» باشید.
🚫
🔴
اخیراً پیامک‌هایی با ادعای «آزادسازی ثبت‌نام اینترنت پرو و هدیه بین‌المللی» ارسال می‌شود که با کلیک روی لینک، گوشی را آلوده به بدافزار می‌کند.
📱
💣
✅
راهکار: لینک را باز نکنید، چیزی دانلود نکنید و این هشدار را به اطرافیان منتقل کنید تا کسی قربانی نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131725" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131724" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksr2LzxFLTDF4t-SNj4Lwj7fsXmSmWAcqZ-U0emHYWAmTC0QQWzSUR5rovZfbmCXzeoJhAn68kYDtijxTG4v9B4e09afzR0TN99715zlnCB_dKMyfxcVnlCBzYHrV4jrugOkYkJuDa6pofsR6wxuWLYA3JARP_XfSE6mY6dYfwDmYLwWZyf523OAV3_c3Wt1WAlA55job142QejuF5ginoBAGxFaDhcz1sYMQt6mp2buRYobBL-Numm1GqpCP-W7W7xMGEEkVmrQT7oOvdfW9SBDoTK8GnQAOepi2cxVjsZgyg9W8tWufS5UwhEULiBuO_d3M0gbnEuC37BqRyMP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131723" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131720">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
پرسپولیس حداقل ۸ بازیکن تو  جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131720" target="_blank">📅 11:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131719">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131719" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد  پ.ن پس اگه مجدد جنگی باشه میفته بعد از جام جهانی ..  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131718" target="_blank">📅 11:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRgjOftNvVCKwxgLUwh2Yy8PXIvDawbQl9TgwC379V2vSOzjAsrdcdKD00fk7UV6wywKNTB36FhCzX_MGHAkTgwfvR8N2NLB0jSHkXJk7pzC4AxrwjLE8s4RdXsE2m_1wztvEK4O6fheT0sN_4gFazviRmboQi9GQpP6g90SAUFkoHu0ivAD1hP72SVmec7lGkqRZw0gyUgHLiwzp3JJH_1ORtZLl2INaByGHBVn4gDlgi_QgzvaoiRl2zbzcI1jlk9jrLk-5JO2kb3RBWGehmEpPQ6PosUjiPp2nsqay6O1WBzhhmggK7hqS4_YJrqNY14pFEOGZBiiPDU-VJ8SMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس
؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/131717" target="_blank">📅 11:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poKVkUwfXwDCObwa88rtE81FYieE6X1Zn6b-9UD9RqsLhoVzQellfMi9ix1CpWEHtieC1MLQrtMqb7IByXbqdmYGJZb7JTwsJUTeo5swOtuXyBAtt--Snt0GyTc6XKlZXghBpvQHGEvOr2c7_V9bZSWK2hzKn7FWlSkfRWr4XaTlqQxZi6fs3COTSNPlp9d04QZKTr4V8mtSu27BM79M2XefWn2aVdVs1ILukesnQkIujqrev3WiP0K9S2-Gi-l96_JSq8pUUQQxlr0DjebcCG9fMpRFzKhwDy9FCdXkdBiW4XUHauX3H5YH64ocVFAmfuFgwWWAE_JC3K8B3scFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز امیدواری کرده که باشگاه بتواند غرامتی را از اوریه دریافت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/131716" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osU1NUmJUMmNlKhZT3kXww63uSBYZl75BLidZ7cJIuRnTVaotVSwys1-TczRZtAMjg-VsXtG5e-SuDfUx-9T65fAyyce4AcULkfWVcQRd8Ux4ho8LRYXKD5AuhACmnPdDgckzIShqs1NFy2n3m5fK3x7cFHqhVPNguWLvjVwxXFx6ruMnVeZojXfBjVBvYZR2TrHD5i42J6Ow8T_2lVzwwOdzy7akvm-xgtPpFbPtol4grwLf_YYC6WqRWXExzsFMzbAJcIRI4_28jeivRjc6p6m668dPd2g025QpcFy595GII2f2krN5aluaUn_4Kvmc5pmA6k55A5G_wg0s-itaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه بازی‌های مهم فردا فوتبال
⚽️
فردا دیدارهای جذاب و هیجان‌انگیزی در فوتبال اروپا برگزار می‌شود که در مهمترین بازی‌ها، سیتیزن‌ها در فینال جام‌حذفی باید با آبی‌های لندن تقابل کنند. بایرن در زمین خود از کلن میزبانی ‌می‌کند و دورتموند هم میهمان وردربرمن می‌باشد. همچنین در دیداری حساس و در فینال لیگ‌قهرمانان آسیا سطح دو، رونالدو و یارانش باید به مصاف نماینده ژاپن گامبااوزاکا بروند.
⚽️
بازی‌های فردا رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید.
📌
وینکوبت
انتخابی حرفه‌ای‌ برای شما، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SorkhTimes/131715" target="_blank">📅 01:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=DFCt7COv-nNYMKpkuKLvUZ4addWUzETGapXxITNr3lCCBSCWigZf_xXYFC-IoF5V6TqcEZzAw7g_z52I02nq-Wh7-5VpL7-nAtfPVYOgI1NmEteWueB4YzewUzvL02N61AqzledVOcGtdQNb0ZJZhBllcdVfc-DY5Vj0lql2SUWKSFsMlU11R-WJRxL2caWxIIepLtarADbWO-f6Yq75P32bZXaLha2IPwFuGqeqCcwy-lSt8T6DzhR7WneZLJ3ri3IXqcPF0IxRI9GC0Li-P8RxWgq--xLqsI9uHUI8awr-leMdjol6Qe78ETt1cR2sdGL7aZoqndCDyDHXx8EQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=DFCt7COv-nNYMKpkuKLvUZ4addWUzETGapXxITNr3lCCBSCWigZf_xXYFC-IoF5V6TqcEZzAw7g_z52I02nq-Wh7-5VpL7-nAtfPVYOgI1NmEteWueB4YzewUzvL02N61AqzledVOcGtdQNb0ZJZhBllcdVfc-DY5Vj0lql2SUWKSFsMlU11R-WJRxL2caWxIIepLtarADbWO-f6Yq75P32bZXaLha2IPwFuGqeqCcwy-lSt8T6DzhR7WneZLJ3ri3IXqcPF0IxRI9GC0Li-P8RxWgq--xLqsI9uHUI8awr-leMdjol6Qe78ETt1cR2sdGL7aZoqndCDyDHXx8EQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: از اوریه غرامت می‌گیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/SorkhTimes/131714" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
