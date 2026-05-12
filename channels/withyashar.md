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
<img src="https://cdn4.telesco.pe/file/XoXr2zkQlJae24GRrOmRw3r-hAxIlwrI9gT9d69FnenK30bw38i0ixWLmr4AoxfGPyktP3JrZEypUkvPAHtBaj0_sh7AftRIr7QP54BTk_eIfHFxhkGWTq1ZqYPYpH5OTNwRJEOCJQ3gDl0lHeeLi7axRvf9max080rqaE8evaLyaudR5WF6DC_K9k2CH1Boszh7-XN-i3a0jAGWAnAfo2DGCLQkfQgoLcGlyoZdQat-4kS6ycwCq1eB8K3vVM0Og_va6tFCM_NKFP_BQM7wfUehDcdqej4KhVApaG3b7Q8B7v6uQh_E5UqGeV6lIOhj1Kveh9rdBl9DU9h7ENVIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 259K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 13:52:58</div>
<hr>

<div class="tg-post" id="msg-11049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل هیوم: هزاران اسرائیلی از شامگاه ۲۲ اردیبهشت پیامک‌های تهدیدآمیز به زبان عبری دریافت کردند که در آنها از سوی هکرهای منتسب به تهران خواسته شده با جمهوری اسلامی همکاری کنند
@withyashar</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/withyashar/11049" target="_blank">📅 13:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3ff38bd1.mp4?token=q7Eqjo9hectUprwTcJEclTK1xzFUpysQcxdsVToLkrFEewxDicquaIzChXji82wsMzvejv8KAg8fTIsXlrsmYMwjPY6Pf-_bcnx_zTKPpdTxDPWiUoIaO-QWZyfO2MK1Jj3BoNzCA4E1JWXHXt67DStpLEVj-pYC6k_kYs7Qu5FEEfmenVFxGK7N88A1rB850x6MCStc4iy8xIqcxkD3El-51N1oWm1YIXHZdIqwjulXyBHpBPi_sXLs9Ye5kEKRYlu8F_LE2ZhubI6HAH61RwGzrv--3krvi_9oIs7YINQAxSgAKDHYzNok5IChni-3e97-XAne1jMpL0KxHTa4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3ff38bd1.mp4?token=q7Eqjo9hectUprwTcJEclTK1xzFUpysQcxdsVToLkrFEewxDicquaIzChXji82wsMzvejv8KAg8fTIsXlrsmYMwjPY6Pf-_bcnx_zTKPpdTxDPWiUoIaO-QWZyfO2MK1Jj3BoNzCA4E1JWXHXt67DStpLEVj-pYC6k_kYs7Qu5FEEfmenVFxGK7N88A1rB850x6MCStc4iy8xIqcxkD3El-51N1oWm1YIXHZdIqwjulXyBHpBPi_sXLs9Ye5kEKRYlu8F_LE2ZhubI6HAH61RwGzrv--3krvi_9oIs7YINQAxSgAKDHYzNok5IChni-3e97-XAne1jMpL0KxHTa4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست های دیروز رو ببینید و ویس های تحلیل ‌دیشب رو حتما از اینجا به پایین گوش کنید</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/11048" target="_blank">📅 13:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کرملین: ولادیمیر پوتین، رئیس جمهور روسیه آماده دیدار با ولودیمیر زلنسکی، همتای اوکراینی خود در مسکو یا هر جای دیگر است.
به پایان جنگ با اوکراین نزدیک می‌شویم.
@withyashar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/11047" target="_blank">📅 13:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میاتا فانبوله، وزیر دولت بریتانیا استعفا داد و در نامه‌اش آشکارا از کیر استارمر نیز خواست که از سمت خود کناره‌گیری کند
این نخستین استعفای رسمی از داخل دولت استارمر در بحبوحه بحران سیاسی اخیر محسوب می‌شود. گزارش‌ها می‌گویند ده‌ها نماینده حزب کارگر نیز اکنون خواهان استعفای استارمر شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/withyashar/11046" target="_blank">📅 13:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ :  من نه قراره خسته بشم نه قراره کوتاه بیام جلو ایران ، تا پیروزی کامل ادامه میدم !
@withyashar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/11045" target="_blank">📅 12:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11044">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e519f8398.mp4?token=I4uPzhsNTx-mki_9WtNvLXC0DKrUdrqknqS2XjKkq3iVM2vN2PC5z10b8zZnQIDIjsu8vPD9dz6CXHSPEfjcLftP16jtoldlr791XFq5ryGaOWmlLhbYdfVbWFw9jgUlJ3Ts-yIh8pbm7xmd2JET9PoB_3rV1i-0R9dp-sYE6GBxba83m6lD1WjROwl-c5zaCJh40Q5ioY6JOb93eKXRw7jIYPStWFGarUmufV4jcEOHyg4pfRoMgcnYEPXtQUtS2ckZbRPx5XKpaAzL-9CMf5JuC45aXwkVfPZJEmoGu8PCpG5zceISLZIWezd2BdTCG73aFvPFmeCbBB0XCbH88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e519f8398.mp4?token=I4uPzhsNTx-mki_9WtNvLXC0DKrUdrqknqS2XjKkq3iVM2vN2PC5z10b8zZnQIDIjsu8vPD9dz6CXHSPEfjcLftP16jtoldlr791XFq5ryGaOWmlLhbYdfVbWFw9jgUlJ3Ts-yIh8pbm7xmd2JET9PoB_3rV1i-0R9dp-sYE6GBxba83m6lD1WjROwl-c5zaCJh40Q5ioY6JOb93eKXRw7jIYPStWFGarUmufV4jcEOHyg4pfRoMgcnYEPXtQUtS2ckZbRPx5XKpaAzL-9CMf5JuC45aXwkVfPZJEmoGu8PCpG5zceISLZIWezd2BdTCG73aFvPFmeCbBB0XCbH88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بار نخود از جمهوری اوگاندا رسید
😂
مونافقو
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/11044" target="_blank">📅 12:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11043">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درود بر یاشار عزیز.  اقا یه مقدار بخواب و استراحت کن.  اخرین پیامت یه ربع سه شب بود. اولین پیامتم ۶:۴۰. جات خالی دیروژ از ساعت ۱۶:۳۰ تا ۵ صبح امروز خوابیدم در هرحال خسته نباشی. انرژی میگیریم ازت باور کن</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/11043" target="_blank">📅 12:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm</strong></div>
<div class="tg-text">درود بر یاشار عزیز.
اقا یه مقدار بخواب و استراحت کن.  اخرین پیامت یه ربع سه شب بود. اولین پیامتم ۶:۴۰. جات خالی دیروژ از ساعت ۱۶:۳۰ تا ۵ صبح امروز خوابیدم
در هرحال خسته نباشی. انرژی میگیریم ازت باور کن</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/withyashar/11042" target="_blank">📅 12:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الجزیره : جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.
@withyashar</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/withyashar/11041" target="_blank">📅 11:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شاهزاده رضا پهلوی: جمهوری‌اسلامی امروز از همیشه ضعیف‌تره و مردم ایران آماده‌ن تا سرنگونش کنن، اتخاذ سیاستی درست در این لحظه میتونه قرن آینده رو تغییر بده
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/11040" target="_blank">📅 11:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eeaa36938.mp4?token=CdT0IMk3iH-qWTIQA_DGs5sJUgfPX9VuN5bUJofcZnszeyyGL0FpxyFLNg8SLvvilNp1CTkQo3Y7EtyBuoxoPqoENodXllzk8084f-U8VBpOWg6ltr-EdqhZ6eit-p16oZYG7YXckY137Qu80PhCQlB-89DphGE54Jf2ds5WexCpkCwBsSj6pPVJVYj7Sk91R-U7mZH2zhAP081MhO1UOwQkARU84vADiY7KQucEbAGNvGr6KCyZeO2KIYFXyMTPj6DO2xDxlGFNEAu6xI5eaMDinzj-hszf8hOGRitgr_kCyiQgZZp5zblulAKfsdZ569GgyjAZ-kR9_euitFP1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eeaa36938.mp4?token=CdT0IMk3iH-qWTIQA_DGs5sJUgfPX9VuN5bUJofcZnszeyyGL0FpxyFLNg8SLvvilNp1CTkQo3Y7EtyBuoxoPqoENodXllzk8084f-U8VBpOWg6ltr-EdqhZ6eit-p16oZYG7YXckY137Qu80PhCQlB-89DphGE54Jf2ds5WexCpkCwBsSj6pPVJVYj7Sk91R-U7mZH2zhAP081MhO1UOwQkARU84vADiY7KQucEbAGNvGr6KCyZeO2KIYFXyMTPj6DO2xDxlGFNEAu6xI5eaMDinzj-hszf8hOGRitgr_kCyiQgZZp5zblulAKfsdZ569GgyjAZ-kR9_euitFP1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتظر تایید خنثی سازی هستیم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11039" target="_blank">📅 09:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">منتظر تایید خنثی سازی هستیم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/11038" target="_blank">📅 09:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤭
😂
😂
لعنت به اخوند</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/11037" target="_blank">📅 09:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با شما : بوشهر دو بار زدن دود سیاه کانفینگم حجم نداره
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/11036" target="_blank">📅 09:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPillar</strong></div>
<div class="tg-text">بوشهر رو زدن پایگاه</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/withyashar/11035" target="_blank">📅 09:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش صدای انفجار در بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/11034" target="_blank">📅 09:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE898q-z57EDwL7qXt0qQ09ZMgg3C9wsTrovts89u5o74JgxHFYL4lbbdG5cqahC-hxA4bt2L-yqpeD9ZUjlAREIcEV0uX5SsV-0ftxANfNolW6l9bJHNxzZyGZ1fHqNozIzQcrooKw1BKXnXM-nCtXNEljkR3Jppld3q-J3djqp_TE5zEpS0ncUKSjN3W2QYMVN1DG4KmhyGjzCBce--FhfmcZ2e22ZTYthrsOXVLqOaR22cd3VFpbsR0CJwAz5exPkrMs2dYEa6y888AEvZ1MIQI-aITPvumUDdE8kn0FBPF7nXvA_4KzjTpMkcagevaMir289ZmqhucpOrCeo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی امروز در اجلاس امنیتی POLITICO واشنگتن سخنرانی می‌کنه
، در کنار مقامات ارشد پنتاگون، وزیر سابق امنیت داخلی آمریکا، سناتورهای کمیته نیروهای مسلح، روسای کمیته اطلاعات مجلس و مقامات دفاعی آلمان و مدیران لاکهید مارتین.
@withyashar</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/11033" target="_blank">📅 09:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Raper Ghadimi Remix (IG @yashar)</div>
  <div class="tg-doc-extra">Reza Pishro & Eminem (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11032" target="_blank">📅 08:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11031">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/11031" target="_blank">📅 08:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11030">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJhbNr__tzm-D5E2-IIhoSoeQwSL4FwsQyLhVO5YZvTAano_MEG6XnM0EamqthYAAEaphnNg4mYmeuokx8UrozLVJfqPx7UhongoM_U0JnehNjpVDkV9_1sVlhB5tlycjqnvo2-bbiyZLBQ-kePQ6BIi8l9ZogGbCX_Hi5I3O2Lr1EVyoCk2CM2JbSQW6XatbFXDoGI2PCvlO2JCGd9s8OcdI7mNCcUBzd2qa6jlTEgIbs-auvdvGe622PSw0K-bd4-HAuhbbINTMZ888FQTIDlIgLuy2Wt2UMP9xBdmrlDZnjTgy7tKrSUwVLp3Zpg4rPy066pWQt4CXXWb6nFFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گفتم قبل قطع اینترنت من در لب ۱ میلیارد بازدید بودم ! ویس بعدی رو گوش کنید
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/11030" target="_blank">📅 08:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11029">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">داشتم الان فکر میکردم یاد این خبر افتادم برایم اون زمان عجیب‌ بود و گفتم یعنی چی میخواد بشه ! ولی الان متوجه میشید قدرت تحلیل و ارتباطات بزرگ رو ! صافولا سعودی چقدر نفوذ و تحلیل دقیق داشت و گروه مدلل کرمانشاه چه سوختی داد !!!
هلدینگ سعودی Savola Group در بازار روغن خوراکی ایران بزرگترین بود، یک سال پیش سهامش را در ایران فروخت و خارج شد
صافولا در ایران مالک یا سهامدار عمده مجموعه‌هایی مانند: شرکت صنعتی بهشهر ، صافولا بهشهر ، برندهای روغن لادن ، بهار و نسترن بود.
طبق اعلام رسمی بورس عربستان، صافولا در ۳۱ دسامبر ۲۰۲۴ قرارداد فروش «تمام کسب‌وکارش در ایران» را به ارزش ۷۰۵ میلیون ریال سعودی امضا کرد
رسانه‌های اقتصادی ایران و چند منبع منطقه‌ای گزارش دادند که خریدار نهایی، «گروه مدلل» بوده است؛ یک گروه بزرگ ایرانی فعال در حوزه روغن، خوراک دام، کشاورزی و صنایع غذایی
@withyashar</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/withyashar/11029" target="_blank">📅 08:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خورخه موریرا دا سیلوا مدیر اجرایی دفتر مشاوره‌ای سازمان ملل (UNOPS) هشدار داد اگر به‌زودی عبور کشتی‌های حامل کود از تنگه هرمز از سر گرفته نشود، جهان ممکن است با بحرانی بزرگ روبه‌رو شود که حدود ۴۵ میلیون نفر دیگر را در معرض گرسنگی قرار می‌دهد.
تنها چند هفته برای جلوگیری از این بحران فرصت باقی مانده
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/11028" target="_blank">📅 07:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11027">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شبکه 14 اسرائیل، تو حمله بعدی اهدافمون شامل موارد زیر میشه:  - تاسیسات انرژی و صنعت پتروشیمی - صنعت خودروسازی و پایگاه‌ های موشک بالستیک - صنعت نفت و صنعت فولاد @withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/11027" target="_blank">📅 07:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ائتلاف منطقه ای علیه جمهوری اسلامی
تام کاتن، سناتور جمهوری‌خواه، گفت کشورهای عربی دیگر از آمریکا برای صلح کمک نمی‌خواهند، بلکه به‌دنبال همکاری نظامی علیه جمهوری اسلامی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11026" target="_blank">📅 07:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پلیس تورنتو کانادا : فردی به نام مهران محققی، ۳۹ ساله را در ارتباط با حادثه‌ای در جریان تجمع ایرانیان علیه جمهوری اسلامی بازداشت شد. این شخص به رانندگی خطرناک نزدیک تجمع، حمله با سلاح، تهدید تجمع‌کنندگان و فرار پس از تصادف متهم شده است.این فرد یک‌شنبه ۲۰ اردیبهشت با رانندگی خطرناک به این تجمع نزدیک شد و پرچم جمهوری اسلامی را تکان می‌داد. او پس از برخورد به راننده یک خودروی تحویل غذا سعی داشت متواری شود، اما پس از برخورد با یک خودروی دیگر متوقف شد.
طبق گزارش پلیس یورک، مظنون سپس خودرو را متوقف کرد تا معترضان را تهدید کند و پس از آن بازداشت شد. یک فرد مصدوم در این حادثه با جراحات جزئی به بیمارستان منتقل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/11024" target="_blank">📅 07:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f429f7dbb.mp4?token=cVffRZZxl5xiUmivlq7D7r9AIfqyl2VBu3JjJcwN7BpT0NBjgPTNKlDZET5SuktFX9sN6jwA-p_2w0aGfXYUseCkHu1y_8YYkwOIk2AEE-u5XbqYdJ1mOlfVZnSF4fwvIwbas7wgasFGsqOwx7NTGkIBs7GoEKyGpVbyWFFTmRR6QZLAEnWtmzCrEe6ps0GNpB-rPR-MQlBTXP20yv63aWqHJV97dF18Q_SgFpI7PU8MeAaSz9vd4PcZ4i2mxhjEpCMtEp52FRxZcPmRdJQQUhiVuKkZAh_UbWejM0DNTN-kOY-7qON-d323S_KER1pnmBq2YbLJvrffcc4R9RIxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f429f7dbb.mp4?token=cVffRZZxl5xiUmivlq7D7r9AIfqyl2VBu3JjJcwN7BpT0NBjgPTNKlDZET5SuktFX9sN6jwA-p_2w0aGfXYUseCkHu1y_8YYkwOIk2AEE-u5XbqYdJ1mOlfVZnSF4fwvIwbas7wgasFGsqOwx7NTGkIBs7GoEKyGpVbyWFFTmRR6QZLAEnWtmzCrEe6ps0GNpB-rPR-MQlBTXP20yv63aWqHJV97dF18Q_SgFpI7PU8MeAaSz9vd4PcZ4i2mxhjEpCMtEp52FRxZcPmRdJQQUhiVuKkZAh_UbWejM0DNTN-kOY-7qON-d323S_KER1pnmBq2YbLJvrffcc4R9RIxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : من حاضرم برای کشورم گلوله بخورم. ما باید کشورمان را نجات بدهیم. کشور ما در دردسر است. و من می‌خواهم ایران خیلی خوب عمل کند. می‌خواهم موفق باشد. می‌خواهم کشوری بزرگ باشد. اما آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. و بعضی از آدم‌های آنجا دیوانه‌اند. نمی‌شود گذاشت دیوانه‌ها سلاح هسته‌ای داشته باشند.
@withyashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/11023" target="_blank">📅 06:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamid</strong></div>
<div class="tg-text">درود دوباره ژنرال یاشار
این ویدیویی که گذاشتی در مورد پیدایش دین برای منی که زرتشتی بودم از بچگی و تاریخ دین خودم و چندتا دیگه از ادیان اریایی و میان رودانی رو خوندم تا حد زیادی به نظرم میتونه یه سناریو منطقی باشه
مثلا ما تو مزدیسنا یه فرقه ای داریم به نام زروانیان که اینا معتقدن که زروان درواقع همون مفهوم زمان هست. و زروان بچه یا نطفه ای داشته به نام اهورامزدا که اولین بار پا در سرزمین ایرانی ها (همون فلات اریایی ) میگذاره تا با اهریمن و سپاهش بجنگه (اینم طبق روایات نطفه دیگه یا دوقولوی اهورامزدا بوده)
نقاشی ها و سنگ نگاره هایی در میان رودان و‌حتی ایران هست مبنی بر حضور همین اجسام پرنده ناشناس و همین طور حضور اهورامزدا که تبدیل به خدای جهان بینی ایرانی میشه و بعد نام بابلی  اَئورامازداش میگیره که  در مصر میشه آمون تو کتیبه های مصری
ارتباطی بین این سه هست که نمیتونم دقیقا حدس بزنم ایا هر سه از یک منبع الهام گرفته شده ان یا نه
به هر صورت حالا در مورد این مالکان یا خود ufo ها یا هر چی که هستن دقیقا چون ما میگیم ناشناس ولی بالاخره یه گونه ای از حیات هستن که نامی هم دارند این هم دیدگاهم‌بود گفتم باهات اشتراک‌بگذارم
جاوید شاه</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/11022" target="_blank">📅 06:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شکلگیری یک دین
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11021" target="_blank">📅 02:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">طبق گزارش‌های معتبر (از جمله بلومبرگ و سی بی اس و رویترز): دولت ترامپ تصمیم گرفته
بخش بزرگی از ذخایر استراتژیک نفت آمریکا (SPR)
را برای جلوگیری از افزایش قیمت‌ها به دلیل جنگ آزاد کندو وارد بازار کند.
عدد اعلام‌شده در بسته اصلی تصمیم، حدود
۱۷۲ میلیون بشکه است
، ولی در مرحله های جداگانه ، همکنون حدود
۵۳ تا ۵۳.۳ میلیون بشکه “به صورت وام/عرضه اولیه”
وارد بازار شده.
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/11020" target="_blank">📅 02:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با شما : این داستان انتقال هواپیماهای نظامی و غیر نظامی به پاکستان و افغانستان رو که خوندم عجیب یاد اواخر حکومت صدام حسین افتادم!
اونم وقتی آمریکا بهش حمله تقریبا تمام جنگنده ها و هواپیماهای ترابری نظامیش رو منتقل کرد به ایران
که البته ایران دیگه بهش پس نداد
اونم شیر نفت رو باز کرد تو خلیج فارس!
اونم به طرفداراش میگفت هر شب بیاید تو خیابون و از من حمایت کنید
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/11019" target="_blank">📅 02:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رهبر دموکرات‌های سنای آمریکا: برای هفتمین‌بار، طرح محدود کردن اختیارات جنگی ترامپ و پایان دادن جنگ ایران به رأی گذاشته می‌شود.
چاک شومر: تکرار می‌کنم، ترامپ آمریکا را به یک جنگ غیرقانونی، پرهزینه و بدون هیچ هدف و هیچ پایانی کشاند.
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/11018" target="_blank">📅 02:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/11017" target="_blank">📅 02:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamid</strong></div>
<div class="tg-text">درود بر sir yashar دریاسالار و فرمانده قرارگاه اتاق جنگ
یه چیزی به ذهنم رسید برای این خبر هواپیماهای ایران که رفته پاکستان و افغانستان و نوشتن که برای حفاظت از دارایی ها ایران بوده به نظرت این کار همون شخصیت ال سی سی نمیتونه باشه که داره همون بخش کوچیک نیرو هوایی که بعدا لازم ایران میشه رو فعلا خارج میکنه تا اسیب نبینه تو‌جنگ؟ صرفا به ذهنم رسیده نمیدونم اصلا میتونه ربطی داشته باشه اگر نیست که اصلا جواب نده  وقتت گرفته نشه
مرسی که هستی و بهمون انرژی میدیییی
❤️
جاوید شاه</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/11016" target="_blank">📅 02:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwMZ02iLWSA93kiVZrr_HpCujKuxOv6hTfTlrv6IcJfV_xYTapT9LubrAKw8kScrOHI3rcf9fhqAqXSUEgOB8T8vA-ke3FahD3QlKK_KUVcrC4A4RGSPTnNYcCnD0DUD02ZQbBPvvpSqhrXEKsN7Zp4GJ1imNo_opzjeApYDc_h3sOA9P3nDJNBJcPhy7utS6jQBv7xjQK_jveXt8dM7P3sVx4_96rhgpD_YNbXtwcRszpgrfUWOCVIAQzQSM2vTUXtEsBbctMVlcQaBv_rDOl2V5CVKzpLATejl44sbaaNmsu1eg9d6gBLY8ukSyy_lKaGfVNzmvX6B8LbPwgu43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز اعلام کرد
جزئیات جدیدترین پیشنهاد ایران
که ترامپ آن را رد کرد:
- دریافت غرامت بابت خسارات جنگی
- به رسمیت شناختن حاکمیت ایران بر تنگه هرمز
- پایان دزدی دریایی آمریکا علیه کشتی‌های ایرانی
- آزادسازی دارایی‌های مسدود شده ایران
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/11015" target="_blank">📅 02:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11014">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ادعای سی.بی.اس به نقل از مقامات آمریکایی:  چند روز پس از اعلام آتش‌بس با ایران توسط ترامپ در اوایل آوریل، تهران چندین فروند هواپیما را به پایگاه هوایی «نور خان» نیروی هوایی پاکستان فرستاد. این پایگاه، یک تأسیسات نظامی راهبردی است که درست در حومه شهر راولپندی،…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11014" target="_blank">📅 01:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ :  من خیلی منتظر سفرم به چین هستم، یک کشور فوق‌العاده، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است.
همکاری های بزرگی برای هر دو کشور رخ خواهد داد!
@withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/11013" target="_blank">📅 01:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تایید نشده : ایران به شورای امنیت سازمان ملل اطلاع داده است که در صورت اعزام زیردریایی هسته‌ای آمریکا به خاورمیانه، سطح غنی سازی ۱۰ تن اورانیوم باقی مانده را به ۶۰ درصد خواهد رساند
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/11012" target="_blank">📅 01:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/11011" target="_blank">📅 01:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromROBOCOP</strong></div>
<div class="tg-text">یاشارجان درود
وقتت بخیر
اینکه میگن قراره تو دیدار ترامپ و شی و از طرفی بصورت غیرمستقیم با پوتین در مورد تایوان و ایران و اوکراین معامله صورت بگیره درسته؟؟
لطفا یه تحلیل کوچولو در این مورد برو
ازبس که از اینور اونور این اخبار زرد و بی اساس. شنیدیم واقعا خسته ایم
بعنوان یه ایرانی واژه خسته با ماها معنی میشه
ممنونم ازت بابت کانال خوبت و اخبار کاملی که میذاری
در پناه اهورای پاک
🙏
🙏
🙏
💚
🤍
♥️</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/11010" target="_blank">📅 01:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11009">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA i</strong></div>
<div class="tg-text">من یکی با اینکه قبلا رفتار های اشتباهی در مقابل شما داشتم
ولی الان واقعا قدر زحماتتونو میفهمم
تنها ویسایی که باز میکنم ویسای شماست و ممنونم که واسمون وقت میزاری
🙏
❤️</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/11009" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11008">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/11008" target="_blank">📅 01:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11007">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS</strong></div>
<div class="tg-text">اخجون کلی ویس
اخجون تحلیل
😍</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/11007" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/11003" target="_blank">📅 00:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/11002" target="_blank">📅 00:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11001" target="_blank">📅 00:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11000" target="_blank">📅 00:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/10999" target="_blank">📅 00:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پنتاگون تأیید کرد که زیردریایی هسته‌ای آمریکایی در مسیر خود به خاورمیانه ست @withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/10997" target="_blank">📅 00:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۲ اسرائیل: رئیس‌جمهور ترامپ تمایل دارد دستور ازسرگیری درگیری با ایران را صادر کند
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/10996" target="_blank">📅 23:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10995">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/10995" target="_blank">📅 23:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10994">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKiasha</strong></div>
<div class="tg-text">سلام یاشار امروز من تو اینترنشنال دیدم که داشت می گفت ممکنه که ترامپ سر اینکه جمهوری اسلامی بمونه با چین معامله کنه،این ممکنه که واقعیت داشته باشه؟</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/10994" target="_blank">📅 23:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10993">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/10993" target="_blank">📅 23:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10992">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJ V</strong></div>
<div class="tg-text">درود
خدا قوت
دمت گرم حرف نداری بخدا
یه جوری شده از صبح که میرم سرکار تا شب که برمیگردم خونه کلا تلگرام رو باز نمیکنم که شب بعد چای و سیگار بشینم یه دل سیر  پیام ها و تحلیل هات رو گوش کنم و صدای دلنشینت رو بشنوم روحیه بگیرم برای روز بعد
بعدشم بخدا که تمام تحلیل هات درسته و دقیق
به امید پیروزی</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/10992" target="_blank">📅 23:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10991">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/10991" target="_blank">📅 23:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10990">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/10990" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɨƈɛքɦօɛռɨӼ</strong></div>
<div class="tg-text">درود یاشار جان
چرا ترامپ همراه رئیس این کمپانی ها بره چین؟</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/10989" target="_blank">📅 23:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10988">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اسکای‌نیوز: 60 تا از نماینده حزب کارگر خواستار کناره‌گیری کیر استارمر نخست وزیر بریتانیا شدن.
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/10988" target="_blank">📅 23:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10987">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ادعای سی.بی.اس به نقل از مقامات آمریکایی:
چند روز پس از اعلام آتش‌بس با ایران توسط ترامپ در اوایل آوریل،
تهران چندین فروند هواپیما را به پایگاه هوایی «نور خان» نیروی هوایی پاکستان فرستاد.
این پایگاه، یک تأسیسات نظامی راهبردی است که درست در حومه شهر راولپندی، شهر پادگانی پاکستان قرار دارد.
در میان تجهیزات نظامی ارسالی، یک فروند آر سی-۱۳۰ از نیروی هوایی ایران وجود داشت که نوعی هواپیمای شناسایی و گردآوری اطلاعات از فروند لاکهید سی-۱۳۰ هرکولس (هواپیمای ترابری تاکتیکی) محسوب می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/10987" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10986">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پنتاگون تأیید کرد که زیردریایی هسته‌ای آمریکایی در مسیر خود به خاورمیانه ست
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/10986" target="_blank">📅 22:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10985">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل:
بحث و رایزنی‌هایی با آمریکا درباره ازسرگیری جنگ علیه ایران در حال انجام است.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/10985" target="_blank">📅 22:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10984">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر دفاع بلژیک: به ابتکار فرانسه و انگلیس برای پاکسازی تنگه هرمز از مین‌های دریایی و بازگشت به دریانوردی آزاد خواهیم پیوست
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/10984" target="_blank">📅 22:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10983">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حمله پهپادی جمهوری اسلامی به کردستان عراق
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/10983" target="_blank">📅 22:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10982">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قالیباف:
هرگونه تجاوز به ایران با پاسخی شایسته مواجه خواهد شد،
ما برای همه گزینه‌ها آماده‌ایم؛
آنها شگفت‌زده خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/10982" target="_blank">📅 22:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10981">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ در حال حاضر تیم ارشد خود را در اتاق بیضی کاخ سفید برای بحث درباره از سرگیری جنگ با ایران گرد هم آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/10981" target="_blank">📅 22:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">lرئیس هوانوردی غیرنظامی اسرائیل هشدار داد که فرودگاه بین‌المللی تل‌آویو در ساعات اخیر عملاً به پایگاه نظامی آمریکا تبدیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/10980" target="_blank">📅 22:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10979">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ:
آتش بس با ایران وقت تلف کردن است.
@withyashar</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/10979" target="_blank">📅 22:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10978">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبر ویژه برای اولین بار از اتاق جنگ با شما :
داداش سلام
ی داستان جالبی توی این سایت جان فدا اتفاق افتاده و فک کنم ایرانسل و همراه اول اطلاعات مشترکینشونو دادن به اونا و اونام همه رو دیفتلت ثبت نام کردن
هرکی و امروز دیدم میگفت از جان فدا پیامک اومده که ثبت نام شدی ولی روحمم خبر نداره
رفتم گوشی مادرمو نگاه کردم دیدم برای اونم پیامک اومده
یا بعد از هک شدن و آبروشون رفتن برداشتن همه رو ثبت نام کردن که آمار درست کنن
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/10978" target="_blank">📅 21:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلک‌راک — لری فینک
بلک‌استون — استیون شوارتزمن
سیتی‌گروپ — جین فریزر
گلدمن ساکس — دیوید سولومون
مسترکارت — مایکل میباخ
ویزا — رایان مک‌اینیری
اپل — تیم کوک
سیسکو — چاک رابینز (حضورش قطعی نیست)
تسلا — ایلان ماسک
بوئینگ — کلی اورتبِرگ
متا — دینا پاول مک‌کورمیک(تایید نشده)
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/10977" target="_blank">📅 21:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">همراهان ترامپ در سفرش به چین:
رئیس شرکت بلک راک
رئیس شرکت گلدمن
رئیس شرکت مسترکارت
رئیس شرکت سیسکو
رئیس شرکت متا
رئیس شرکت ویزا
رئیس شرکت اپل
رئیس شرکت تسلا (ایلان ماسک)
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/10976" target="_blank">📅 21:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دریادار شهرام ایرانی:
یک سری دلفین انتحاری کف آب داریم، لباس ارتشی پوشیدن هر کی دوست داره ببینتشون بیاد از تنگه رد شه
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/10975" target="_blank">📅 21:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH.bbk</strong></div>
<div class="tg-text">همیشه تو جیبش مار داشت
😂
😂</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/10974" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84fcb3e18e.mp4?token=B9Ez_vrWZwwB2MquUUoaKPFIQPIICsYQEDK0C1W3AWf1n2svsJTzoo4gSTd1BWv9d_KcjVbw-aZib6vIOGxyNbHPiP4aAl3OmMObBgkQERM_M5XgcziAzwV79vyfPJhpusKbWG767fF4AQMEBm8_Rdyq8sZ_I2TKJ-m9RX0t-O50U7YRhI84MPLXZX2MIETPESFDm5-RaRlijNl9ZL-p4yEeJWbJ6c8UWT0BZi8qItFlKnnhU5_HAu_2FhKHNWO4UPgptjPka6bfTUmmnS4Q_fftki2eh0cVUa-gbxN_riuwwqyfkI_iEt1Zw4iJ0MStlw7RyOe_tOdK7UyS9PCYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84fcb3e18e.mp4?token=B9Ez_vrWZwwB2MquUUoaKPFIQPIICsYQEDK0C1W3AWf1n2svsJTzoo4gSTd1BWv9d_KcjVbw-aZib6vIOGxyNbHPiP4aAl3OmMObBgkQERM_M5XgcziAzwV79vyfPJhpusKbWG767fF4AQMEBm8_Rdyq8sZ_I2TKJ-m9RX0t-O50U7YRhI84MPLXZX2MIETPESFDm5-RaRlijNl9ZL-p4yEeJWbJ6c8UWT0BZi8qItFlKnnhU5_HAu_2FhKHNWO4UPgptjPka6bfTUmmnS4Q_fftki2eh0cVUa-gbxN_riuwwqyfkI_iEt1Zw4iJ0MStlw7RyOe_tOdK7UyS9PCYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرشد
🤣
خودشههههه
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/10973" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/10972" target="_blank">📅 21:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خوش‌چشم بعد از ۶ بس تریاک
😂
:
این دفعه جوری اسرائیل رو میزنیم که هوش مصنوعی اسرائیل میره رو هوا
یه جای دیگه هم تو اسرائیل میزنیم که نمیتونم بگم کجاست ولی بیچارشون میکنه
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/10969" target="_blank">📅 21:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این ناو باکسر ما چیشد نرسید
🥹
؟؟</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/10968" target="_blank">📅 21:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from"Ali"</strong></div>
<div class="tg-text">این ناو باکسر ما چیشد نرسید
🥹
؟؟</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/10967" target="_blank">📅 20:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8416b146e.mp4?token=DyvZw8B8YY7FmLlwUSH2iO9Fb2Rxpow9cgVKWuTsfv6tD8CmfsX4UiYFHkY5St9sHm5DPi59nwj2UMwHGAxC-hjCoLn2Zed4a2KVX9w7Mgb1ZwzM38uRdk5NkDCmZVHtOC5xsYwgNRyblnb_ahHR69pVYz67AASOMaUZ8z1VmvAl1xwgNCJEWOu4PkUNm26Qwqkgvq9IKb-Y5I43GgYcu9ft8uXhs5N31NdpxzEJW7XowWy2wYrBzOdrRnMpfQHfxm6Oqj_z_8p3N9xNFAgM33bZAWe3n8hHHmqg2YnJoOVzOlJI2oi1r7NQhDGMkgJ0A6rpBk2BbbYZ4Nt7trxNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8416b146e.mp4?token=DyvZw8B8YY7FmLlwUSH2iO9Fb2Rxpow9cgVKWuTsfv6tD8CmfsX4UiYFHkY5St9sHm5DPi59nwj2UMwHGAxC-hjCoLn2Zed4a2KVX9w7Mgb1ZwzM38uRdk5NkDCmZVHtOC5xsYwgNRyblnb_ahHR69pVYz67AASOMaUZ8z1VmvAl1xwgNCJEWOu4PkUNm26Qwqkgvq9IKb-Y5I43GgYcu9ft8uXhs5N31NdpxzEJW7XowWy2wYrBzOdrRnMpfQHfxm6Oqj_z_8p3N9xNFAgM33bZAWe3n8hHHmqg2YnJoOVzOlJI2oi1r7NQhDGMkgJ0A6rpBk2BbbYZ4Nt7trxNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دهها تانکر سوخت رسان آمریکا هنوز در بن گوریون اسرائیل مستقر هستند.
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/10966" target="_blank">📅 20:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10965">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آکسیوس : ترامپ در حال بررسی دو گزینه‌ست
یا از سرگیری «پروژه آزادی» که هفته گذشته به حالت تعلیق دراومد
یا از سرگیری بمبارون و حمله به ۲۵٪ از اهدافی که آمریکا شناسایی کرده اما هنوز به اونا حمله نکرده - و امشب با ژنرال‌ها جلسه داره!
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/10965" target="_blank">📅 20:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای آکسیوس:
مقامات آمریکایی می‌گویند انتظار می‌رود ونس، ویتکاف، روبیو، هگست، رئیس ستاد مشترک ارتش، رئیس سیا، و دیگر مقامات ارشد در جلسۀ امروز در مورد ایران برای احتمال از سر گیری جنگ شرکت کنند.
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/10964" target="_blank">📅 20:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری Associated Press به نقل از دیپلمات‌های منطقه‌ای گزارش داد که ترامپ از اصرار ایران بر دریافت غرامت جنگی عصبانی شده است. طبق این گزارش، ایران در پیشنهادهای خود خواستار
«غرامت جنگ»
بوده است.
بر اساس این گزارش‌ها، ترامپ نسبت به استفاده از واژه «غرامت» حساسیت داشته، زیرا در عرف سیاسی و تاریخی، پرداخت غرامت معمولاً با پذیرش شکست یا مسئولیت در جنگ همراه دانسته می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/10963" target="_blank">📅 20:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: هیچ‌کس فکر نمی‌کرد کشورهای منطقه هدف قرار بگیرند.
این یک اشتباه استراتژیک بزرگ بود و آنها آن موشک‌ها را هدر دادند. ما سامانه‌های پاتریوت داریم که هر بار آنها را سرنگون کردند.
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/10962" target="_blank">📅 19:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10961">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره ایران گفت:
رهبرانشان آدم‌های بسیار بی‌شرفی هستند
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/10961" target="_blank">📅 19:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10960">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ : از دست دادن تنگه هرمز«کارِ هوشمندانه‌ای» است، چون کشورها الان نفت خود را از تگزاس می‌خرند. و این تا اتفاق تا حدی شگفت‌انگیز است.
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/10960" target="_blank">📅 19:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ : هیچ کشتی‌ای دیگه وارد نمی‌شه، هیچ کشتی مزخرفی هم نمیاد که آخرش باهاش درگیر بشیم امیدوارم رئیس‌جمهور شی به من احترام بزاره
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/10959" target="_blank">📅 19:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: ما ۴ روز برای سندی از ایران منتظر ماندیم که تنظیم آن بیش از ۱۰ دقیقه زمان نمی‌برد
آن‌ها ۲ روز پیش با خارج‌کردن اورانیوم‌ها موافقت کردند اما بعداً نظرشان تغییر کرد، چون آن را در پیام ارسالی به ما نیاوردند.
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/10958" target="_blank">📅 19:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:
اگر توافقی حاصل نشود، ما ایران را به گونه‌ای هدف قرار خواهیم داد که قبلاً ندیده‌ اند
ایران اگه به سلاح هسته ای دست پیدا کنه یک ساعت بعد از اون استفاده میکنه
@withyashar</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/10957" target="_blank">📅 19:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من با آنها ( حاکمان ایران ) برخورد می‌کنم. به آنها می‌گویم: “شماها دیوانه‌اید. دیوانه‌اید. کاملاً روانی هستید.
@withyashar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/10956" target="_blank">📅 19:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/withyashar/10955" target="_blank">📅 19:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ گفت:
آتش‌بس در وضعیتِ وابسته به دستگاه‌های حیاتی (
تقریباً در حال مرگ
) قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/10954" target="_blank">📅 19:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/10953" target="_blank">📅 19:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به کردها حمله کرد:
کردها فقط می‌گیرند، می‌گیرند و می‌گیرند. آنها در کنگره آمریکا شهرت خوبی دارند. کنگره می‌گوید آنها سخت می‌جنگند. وقتی پول بگیرند، سخت می‌جنگند.
من از کردها بسیار ناامید هستم
@withyashar</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/10952" target="_blank">📅 19:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ:  واسه مردم ایران اسلحه فرستادم ولی کُردها اونارو دزدیدن و منو مأیوس کردن. مردم ایران عالی مبارزه کردن ولی تفنگ نداشتن. @withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/10951" target="_blank">📅 19:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ درباره ایران گفت:
در ایران، افراد میانه‌رو و دیوانه‌ها وجود دارند.
میانه‌روها محترم‌تر هستند. دیوانه‌ها می‌خواهند تا آخر بجنگند.
در کشور ما هم دیوانه‌هایی وجود دارند.
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/10950" target="_blank">📅 19:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:  پیشنهاد ایران احمقانه بود؛ فقط شاید بایدن و اوباما اون رو قبول کنن.
@withyashar</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/10949" target="_blank">📅 19:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:
واسه مردم ایران اسلحه فرستادم ولی کُردها اونارو دزدیدن و منو مأیوس کردن. مردم ایران عالی مبارزه کردن ولی تفنگ نداشتن
.
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/10948" target="_blank">📅 19:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: در این زمان احتمالا مقداری خودشون رو بازسازی کردن که مهم نیست. توی یک روز از بین میبریشمون
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/10947" target="_blank">📅 19:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ گفت: ایران به من گفت: “شما دارید به چیزی به نام گردِ هسته‌ای دست پیدا می‌کنید، اما مجبور خواهید بود آن را به دست بیاورید.”
آنها گفتند: “فقط شما و چین می‌توانید آن را به دست بیاورید، چون سایت‌ها کاملاً نابود شده‌اند.”
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/10946" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ : اون محاصره، اول از همه، یه نبوغ نظامی بود؛  درست مثل ونزوئلا،ما پر از مهمات فوق‌العاده‌ایم
الان خیلی چیزهای بهتری نسبت به دو ماه پیش داریم، وقتی اولین حمله رو انجام دادیم
@withyashar</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/10945" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره ایران گفت:
آنها چقدر احمق هستند؟ آدم‌های احمق. فکر می‌کنند که من خسته می‌شوم، حوصله‌ام سر می‌رود، یا تحت فشار قرار می‌گیرم.
هیچ فشاری وجود ندارد. ما یک پیروزی کامل خواهیم داشت. در واقع، از نظر نظامی، ما از نظر تئوری همین حالا هم یک پیروزی کامل به دست آورده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/10944" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-10943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ درباره ایران:
خیلی‌ها می‌گویند: “آیا او اصلاً برنامه‌ای دارد؟”
البته که من برنامه دارم. من بهترین برنامه را دارم، بهترین برنامه‌ای که تا حالا وجود داشته است.
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/10943" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
