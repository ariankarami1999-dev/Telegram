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
<img src="https://cdn4.telesco.pe/file/ruQz66cNyZAQfFMlewHMgl1m3B0dTLs8wEP4mTYC4_IK2ggdPrihuAqD8lCW5WHV24fPFg5VvLjdbJZB0yNNorzr80PeXelWRgu9na4ILKLOPC6Tu_WphVJKKH_4u2xGWi68ATefeBp_JwKOsVb1rGuukDz8NEihUchHV7m4SzQfa3vBJ6YrYDYJFZThYIidjUnR4HwZl6hmut2VSfFb2dNniRG3CGwctGXT5NG9s-FtaBGSp-1JpF_VD5jREbsEr_lgJBITnyKlKyveaOKAIVjZ-gF545otO4bZKx7NWUlmDNr9u1VdvOV3j5xSgsYElsscegTG3ehP95BgieNjfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.09M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 00:15:59</div>
<hr>

<div class="tg-post" id="msg-682402">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbEpJsRd5abXxHnn5oJkeeBZkAhgtBz1a65Q2-KPGn4qH-CWMhnzQ4x6QsJtwxzV19zXg-HZT7GofVl9sy9BhQE9JcasmGooTBM4dfkNe2t3o-NuxkrS5CmqaWPFlmHZzOi6FNSmuNRCJ5nOqcydVYYT4srxuedDSi2Kx0oIAtene739O5t6O73TMG0VGrN8tU_2mMNRg0M7FZWSmbbOru6upW_YaEScriX5tF46ma1rPq1fv2aULPDidMYV6uw9-UwYRkVwZ6MBzXB81lMXSGEHa_gvJhLdrYaux8DlPIsrJKpFmw3_Z12Pk0cyZPIjG5Fw8oZOOA9120FlRqH99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی در نیزارهای پشت فرودگاه شهرستان امیدیه در حال مهار است
🔹
علت دقیق وقوع آتش‌سوزی در حال بررسی است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/682402" target="_blank">📅 00:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682401">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc736f68b.mp4?token=Zbc7L-5e3qVpPggdfAmtRWBv5u3ClCU-JHnYcU07a_Mto1rtkVIUL899ZiHdQ7VVD5igLEynTbcBp47kj2xlnzZPS7txDJCr0O64beJvkI9Z_t8IsRPtzEV3fDrqtvYJmJ-ihJq0dbwpYxwaTja_1eCgeALZU6-CsB7AUkY8rFj_5Ud3anG7x2jHMtrUsIBZvNbhS7Tg397nPPKPnHKPELJbVTLYcqxQ60VMN6cTWKkMatojnuctFS_97WAgCmXq-Pu3FKh0VkNtZXkyPZA4ytXxWEntumEKGUBjkD4LRcqt9VQwCGNORJ2q9c6RWg82h-1Amuo3NYBnSVmeAlEZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc736f68b.mp4?token=Zbc7L-5e3qVpPggdfAmtRWBv5u3ClCU-JHnYcU07a_Mto1rtkVIUL899ZiHdQ7VVD5igLEynTbcBp47kj2xlnzZPS7txDJCr0O64beJvkI9Z_t8IsRPtzEV3fDrqtvYJmJ-ihJq0dbwpYxwaTja_1eCgeALZU6-CsB7AUkY8rFj_5Ud3anG7x2jHMtrUsIBZvNbhS7Tg397nPPKPnHKPELJbVTLYcqxQ60VMN6cTWKkMatojnuctFS_97WAgCmXq-Pu3FKh0VkNtZXkyPZA4ytXxWEntumEKGUBjkD4LRcqt9VQwCGNORJ2q9c6RWg82h-1Amuo3NYBnSVmeAlEZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدمحمد خاتمی: فرصتی که در تفاهم‌نامه ایجاد شده اگر از دست بدهیم دچار مشکلات عجیب می‌شویم
🔹
تفاهم‌نامه نظیر ندارد، بعد از جنگ‌جهانی دوم هیچ سندی که به امضای رئیس جمهور آمریکا رسیده باشد اینقدر امتیاز به طرف مقابل نداده، ما در موضع عزت به این‌ تفاهم‌نامه رسیدیم
🔹
دو عامل باعث شد در جنگ شکست نخوریم؛ یک عامل سپاه، رزمندگان و مقاومت بود که کارستان کردند، عامل دوم، مردم بودند؛ همین ۶۰ درصدی که ناراضی هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/682401" target="_blank">📅 00:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682400">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ای‌بی‌سی‌نیوز: کاخ سفید بر سر اولویت جنگ ایران اختلاف دارد
ای‌بی‌سی‌نیوز:
🔹
ترامپ در تضاد با ونس می‌گوید اولویت اول در ایران، سلاح‌های هسته‌ای است، نه قیمت نفت.
🔹
اظهارات ونس در مورد اولویت دادن به قیمت بنزین با ماموریت اعلام‌شده رئیس‌جمهور مبنی بر حذف برنامه‌های هسته‌ای و موشک‌های بالستیک ایران متفاوت است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/682400" target="_blank">📅 00:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682399">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMqogib0X7ocoVje3yQ4T8XjtRafxanFaor2OmBEJDAqCAWxDSUIPKVUnC73u_dFcLL3jIA57yyA4qw4sNMB04VnTDuB8SrLzDKskJwLK_sk38ISHTwi6t6oVVyDxB8EPMUEi-qWmWlyf6bjeuVetAAww8Z_NVTItQjRc0X2gmgfYcO1JzeT1yDfc9MVAFtprQNsosAW8yK1KHTdcTFSqGIuIKof9zF3UcRL6xOsQiOuZPKqRbpms91x8vMVBrSZjPX0Gynv_cnjq0NYRPhjkO5sXkiDjW3FJlsJ79FSvA0lPoIog-a9IE5JI8noqrR-euAggkVIIuw4CN4hpSGncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی بزرگ ارکیده شاپ شروع شد!
🎉
این بار خرید از ارکیده شاپ می‌تونه براتون فقط به معنی خرید نباشه؛
شانس برنده شدن ۳ جایزه جذاب
رو هم دارید!
😍
🎁
🏆
جوایز قرعه‌کشی:
😍
👇
🥇
کرلی شیگلم | ۹,۵۰۰,۰۰۰ تومان
🥈
شیور صورت و بدن شیگلم | ۸,۳۰۰,۰۰۰ تومان
🥉
سشوار روونتا | ۷,۰۰۰,۰۰۰ تومان
🛍️
خرید کنید و شانس خودتون رو امتحان کنید؛ شاید برنده این ماه شما باشید!
💜
📌
ارکیده شاپ | انتخاب مطمئن برای خانه و آشپزخانه
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/682399" target="_blank">📅 00:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682398">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlPLUmlCFb5yITVDbS6OKFs8VowSDbQZuO2GU-138LpEGG7JLjbY5AkSufg4MhldwD8qIDpZyoo1urKzy3Buc6P0hu1X28hQ-zWjS5shaVnB0MqbVQH_Y6XrV0nwYcB1UGmLmTTu0rbxOGUPkUmbabMkPiv_9ehb6lrBAuSXtx2DDJEVZiPdW3RNLFkjKKgYBePkMtHQNqjBmRtPPC8tPPw70WlMM3HMCkKlyLQRJxHiJeaexAHIesN24FaY062Wm3QSAnDq4FAqkw-gscqxFp4XFTDNikmNx5nNMYmDHZbQbI9mc9AduQeHVj2DVoEgxyMtYXJlx88F5CxaGvoYrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/682398" target="_blank">📅 00:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682397">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbceb5ec7.mp4?token=kL-DrorHekY0xq1Zzf28_MMeGKGgWIfbYNgjkVuoEOwmTsuLIoQhjD5WcEwTp_pAf3FcZOPgVWJ3JDqG-OvxFtyzC7AjIZrbfuA9ONDrKicr6RX0BbGkVlnaSiPYjFFcVpNYCCCFkYSLMrjCxtioi7MMRYvJUUyMcsjsiUAV2v-eU7NcaCLtkUNFpB26RoUZaj_xqwOGIKpMO94Rtw0ozANQV5GBpbzm49rfGk8F4SKlXV3EKP8eIRiGlu_65EKFRa_t--4AvxwOxm-e8Fv5lKJOLT7k40mHIxz0BSUNVdaBzzQQMLA6dyt0if8ZctCyHNw2NngbgCRIdQYva5ygMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbceb5ec7.mp4?token=kL-DrorHekY0xq1Zzf28_MMeGKGgWIfbYNgjkVuoEOwmTsuLIoQhjD5WcEwTp_pAf3FcZOPgVWJ3JDqG-OvxFtyzC7AjIZrbfuA9ONDrKicr6RX0BbGkVlnaSiPYjFFcVpNYCCCFkYSLMrjCxtioi7MMRYvJUUyMcsjsiUAV2v-eU7NcaCLtkUNFpB26RoUZaj_xqwOGIKpMO94Rtw0ozANQV5GBpbzm49rfGk8F4SKlXV3EKP8eIRiGlu_65EKFRa_t--4AvxwOxm-e8Fv5lKJOLT7k40mHIxz0BSUNVdaBzzQQMLA6dyt0if8ZctCyHNw2NngbgCRIdQYva5ygMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر حالت خوابیدن روی کدام بخش از ستون فقرات فشار وارد می‌کند؟
🔹
روی شکم خوابیدن هم به مهره‌های گردن و هم به مهره‌های کمر فشار وارد میکند و به مرور باعث آسیب به آنها می‌شود.
🔹
بهترین حالت برای خوابیدن به پهلو با قراردادن یک بالشت کوچک بین پاها برای حذف فشار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/682397" target="_blank">📅 23:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682396">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ملاقات سفیر ایران با ۴ ایرانی بازداشت شده در کویت
🔹
سفیر ایران در کویت امروز در ملاقات با چهار نفر از اتباع ایرانی بازداشت شده در کویت در جريان سلامتی و آخرين وضعيت آنها قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/682396" target="_blank">📅 23:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682395">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHMhO9FRKsKgLEqz9v8ZgEg5wI0d01tq0BfTSKAQvNQ49BWgOpe7xjRCJZcjOm9N8AMjLD3xZJBVrForoGDhITbOrwI9B023ald9fCw2I9muuwxcvLCpCJlbzF4flb3613Lht3YKPxhU7fWsH43-FYSnGo_slsyzElYeXislIMFZk7ELAYoJESouyRxvhIdULz8vZdwlEB35y6Q22DH2XYdwfYx91HF0kaYA2Lk7pF-_WTxht1x-5Nmc43O-HXpchGPk2089oBJ9Ef7pOmQ9mEGqcy3lvc0DBeboKvTwrF0huq8--ftOmwgqgnk64zW7qURjgzltmiBx50fguy1LKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی گازوییل در آمریکا در پی تشدید کمبود جهانی سوخت
🔹
بلومبرگ گزارش داد، سود تولید گازوییل از نفت خام در آمریکا به بیش از ۱۰۰ دلار در هر بشکه رسیده و رکورد تاریخی جدیدی ثبت کرده است. این شاخص روز دوشنبه برای نخستین بار در سطح سه‌رقمی بسته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/682395" target="_blank">📅 23:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682394">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در رنج مردم صرفه‌جویی کنید!
🔹
این روزها بیش از همیشه باید صرفه‌جو باشیم... اما نه فقط در آب و برق و سوخت.
🔹
باید در آزار دادن مردم صرفه‌جویی کنیم. در تصمیم‌هایی که بی‌دلیل زندگی را سخت‌تر می‌کنند، در بخشنامه‌هایی که جز اضطراب و سردرگمی چیزی به جا نمی‌گذارند.
🔹
در آزمون‌وخطاهایی که هزینه‌شان را مردمی می‌پردازند که خودشان مدت‌هاست با حساب و کتاب زندگی می‌کنند.
🔹
باید در ساختن دوگانه‌های دروغین صرفه‌جویی کنیم. در اینکه مردم را مقابل هم قرار دهیم، برای هر مسئله‌ای دشمنی بتراشیم و جامعه را میان «این» و «آن» تقسیم کنیم.
🔹
این سرزمین بیش از آنکه به شکاف تازه نیاز داشته باشد، به اندکی آرامش و همدلی محتاج است.
🔹
باید در حرف‌های اضافه هم صرفه‌جویی کنیم، در وعده‌هایی که عملی نمی‌شوند، در شعارهایی که سفره‌ای را رنگین نمی‌کنند و در تصمیم‌هایی که هزینه‌شان را مردم می‌پردازند.
🔹
این روزها کشور به تصمیم‌های بزرگ نیاز دارد، اما پیش از آن به عقلانیت، مسئولیت‌پذیری و ملاحظه حال مردم نیاز دارد.
🔹
صرفه‌جویی فقط کم کردن هزینه‌ها نیست؛ گاهی یعنی کمتر رنجاندن، کمتر تفرقه انداختن، کمتر تحمیل کردن و کمتر خرج تراشیدن.
🔹
در روزگار سخت، هنر مدیریت این نیست که بار بیشتری بر دوش مردم بگذاریم، هنر آن است که خودمان بارهای اضافی را از دوششان برداریم.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/682394" target="_blank">📅 23:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرسونه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUAcIIMabwG6TrMH-lPZitXW0X8yLhg6KX7_5P5XGRhnKWJw-sdznUiB6dMSQn849v5pCzFsG3xH83p1Brhqm6tHZOGA5kH5ZEs4z63qt4BDTe9PCeHkmhghYww7JK0Jn7nu9BAPVh8cfZErnIaVfe1YhWe8m_L0j5fIHqwcTfz_dAqw_I9x5L50Vi88PQzPgndQja3PYx9mU7_fWKb7Z7oCtXDgbsTaJm4pCYTitV3Iw-G6cElzdH8P-Pfrf00tDJ-NR9kod9z6FqpMl3X_dbFi19Y9sRxoCIHne1YmPCpCBuygNGazZhXKHd5xG1FA8XMyDvnDwnY8o3kQDCkhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکار بیک؛ حامی آموزش و یادگیری دانش‌آموزان ایران
🔹
آموزش تخصصی و رایگان پایه اول تا نهم
لینک کانال های درسونه
👇🏽
اول دبستان
👈🏼
@darsoone1
دوم دبستان
👈🏼
@darsoone2
سوم دبستان
👈🏼
@darsoone3
چهارم دبستان
👈🏼
@darsoone4
پنجم دبستان
👈🏼
@darsoone5
ششم دبستان
👈🏼
@darsoone6
پایه هفتم
👈🏼
@darsoone7
پایه هشتم
👈🏼
@darsoone8
پایه نهم
👈🏼
@darsoone9
آموزش زبان
👈🏼
@en_darsoone</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/682393" target="_blank">📅 23:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
باکو: خبر سی‌ان‌ان درباره استفاده اسرائیل از خاک آذربایجان برای حمله ایران صحت ندارد
ادعای آذرنیوز:
🔹
آژانس توسعه رسانه‌ای آذربایجان (مدیا)، سی‌ان‌ان را به انتشار اطلاعات نادرست در مورد ادعاهایی مبنی بر استفاده اسرائیل از خاک آذربایجان در طول جنگ با ایران متهم کرد و این گزارش را یک تحریک سیاسی علیه آذربایجان و امنیت منطقه‌ای توصیف کرد.
🔹
مدیا در بیانیه‌ای اعلام کرد که سی‌ان‌ان در ۵ ژوئن ادعاهایی را با استناد به آنچه «منابع» خود توصیف کرد، منتشر کرده و نوشته که اسرائیل در طول این درگیری از خاک آذربایجان استفاده کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682392" target="_blank">📅 23:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682391">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53e129d07.mp4?token=oB1-l0sOHw5benCcVGeXfTQXUgdZJsO0PTDmSlRCpRtLLzbLXa7o_MbPjD0z8Rc-9SCVxyIdSPRXDQ1E4VDS1W8awKwbTKzInvDMxh4EnNHV92ob-EV6m1ku8cesmpsVuKbioRy0lX6Csn0J2JecqUAABJb6gAEEohXiqN08NSWcxBs1LXsaecbBw3vlfWvoSDFekVm8582qj2-8JWdMf4bRG-LFlhk4oyQoFo1hQKvrIMm5ouV46H3wHSfRDxEAuM3i0zDF7NurLyK7wSr70EbH5sxX9_gETqQmzqce8rMdpFp4cKQeooQJvDf6gabf4ZUp_NTmGzuB5bP8u56TYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53e129d07.mp4?token=oB1-l0sOHw5benCcVGeXfTQXUgdZJsO0PTDmSlRCpRtLLzbLXa7o_MbPjD0z8Rc-9SCVxyIdSPRXDQ1E4VDS1W8awKwbTKzInvDMxh4EnNHV92ob-EV6m1ku8cesmpsVuKbioRy0lX6Csn0J2JecqUAABJb6gAEEohXiqN08NSWcxBs1LXsaecbBw3vlfWvoSDFekVm8582qj2-8JWdMf4bRG-LFlhk4oyQoFo1hQKvrIMm5ouV46H3wHSfRDxEAuM3i0zDF7NurLyK7wSr70EbH5sxX9_gETqQmzqce8rMdpFp4cKQeooQJvDf6gabf4ZUp_NTmGzuB5bP8u56TYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک گروه در آمریکا به‌جای توپ با ماکت شبیه سر نتانیاهو فوتبال بازی می‌کنن
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682391" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d5136558b.mp4?token=a_UhoJKn3uV5wWXf4rNC-REGnmplCPk8YFDwJHtIns1CbgVx3U6HCd07VHXm4D8QsCPDbWDSuVu_T-1s8Hlh2OkyauMmefQD-Ac088ugd2AEN2g5ziQO0ysjBHnWbCTVENR6EMn5sG2CY3oncTqbXEWhKoTPqpd_5-OpIlnlEnYTKOYz1yZk3w4EWX_lDzVMea7lq6-4lJ_7QUJ8DitdnqedMXPUO4aiPZ3ioIPGxb1Gx253njQBVmHHFJ5BR07ju0iRwT_nqSSlxV8rFYd3rTK0SCvFk2fvUPtHs0y_ZdhfX-IUxNIgrr50Pd3jiRmDwfj5mljRIC8iGYJHcfPzXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d5136558b.mp4?token=a_UhoJKn3uV5wWXf4rNC-REGnmplCPk8YFDwJHtIns1CbgVx3U6HCd07VHXm4D8QsCPDbWDSuVu_T-1s8Hlh2OkyauMmefQD-Ac088ugd2AEN2g5ziQO0ysjBHnWbCTVENR6EMn5sG2CY3oncTqbXEWhKoTPqpd_5-OpIlnlEnYTKOYz1yZk3w4EWX_lDzVMea7lq6-4lJ_7QUJ8DitdnqedMXPUO4aiPZ3ioIPGxb1Gx253njQBVmHHFJ5BR07ju0iRwT_nqSSlxV8rFYd3rTK0SCvFk2fvUPtHs0y_ZdhfX-IUxNIgrr50Pd3jiRmDwfj5mljRIC8iGYJHcfPzXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده محیط‌زیست ایران در بریکس از خجالت اماراتی‌ها درآمد
🔹
خورسند، نماینده سازمان محیط‌زیست در اجلاس بریکس به سخنان وزیر امارات درباره حملات ایران به مواضع آمریکایی در امارات واکنش نشان داد.
🔹
هر کشوری با میزبانی از متجاوز و زمینه‌سازی برای حمله به ایران، بدون تردید با عواقب عمل خود روبه‌رو خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682390" target="_blank">📅 23:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یارانه ۷۶ میلیون نفری وبال گردن دولت شده است/ هر کس یارانه می‌خواهد، برود تحت پوشش کمیته امداد
مهدی پازوکی، اقتصاددان در
#گفتگو
با خبرفوری:
🔹
پیشنهاد من این است که دولت اعلام کند هر کس می‌خواهد یارانه بگیرد، تا سه ماه دیگر برای قرارگرفتن تحت پوشش کمیته امداد اقدام کند. آن‌وقت خیلی‌ها، از حاجی‌بازاری و استاد جراح تا استاد دانشگاه و نماینده مجلس، دیگر مراجعه نمی‌کنند.
🔹
یارانه حدود ۲۰ میلیون نفر تحت پوشش کمیته امداد و بهزیستی باید حفظ و حتی افزایش یابد. اما چه دلیلی دارد به فردی با دو خانه، ویلای شمال یا سفر خارجی یارانه پرداخت شود؟
🔹
بودجه مجلس از ۱۶۰۰ میلیارد تومان در سال ۱۴۰۱ به نزدیک ۱۲ هزار میلیارد تومان رسیده است، اما در سیستان‌وبلوچستان هنوز دانش‌آموزان تخته‌سیاه و نیمکت ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/682389" target="_blank">📅 23:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682388">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سیگنال خطر به بازار بدهی؛ صندوق‌ها از اوراق دولتی عقب نشستند
🔹
پرتفوی هشت صندوق بزرگ درآمد ثابت نشان می‌دهد تقاضا برای اوراق بدهی بلندمدت دولت به‌شدت افت کرده است.
🔹
فروش ضعیف اوراق سه‌ساله در حراج‌های دولت، در کنار انتظار برای افزایش نرخ بهره، باعث شده صندوق‌ها اوراق با نرخ حدود ۳۹ درصد را در بلندمدت پرریسک بدانند و سرمایه خود را به سمت سپرده‌های بانکی با نقدشوندگی و نرخ‌های جذاب‌تر منتقل کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682388" target="_blank">📅 23:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682387">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617832e930.mp4?token=nvALOG4CaiTNWaBrZir38PgXkmOtGQYCxvCi7hf4AXh-PulsGldfgBN8J6RrJfZBUCO4GXc8kOWGj97gS6aZy0wp6N_YoJOT-xkfXfHsop63rdx33gbxsHkOdqvP2hx_Zduoce2T-ApdW9_aJGfx6a555pt1HpHTk9T83VBz1ordjNaMVenoDxsweoVUHDmJ80yxVr7ctlpu6H7zG89RSriL_PI7g58jsLvR9PlfJ0YVICA8gg7A3X0S4afQDwencC-a69B-h2uAWyo9MZlJS9V0MgxyUnmfI4Ie3qDfyhdoQRT45-OiYUJ2Edjp4BsFVA4IP6wOx3ZFbSmB_iDmYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617832e930.mp4?token=nvALOG4CaiTNWaBrZir38PgXkmOtGQYCxvCi7hf4AXh-PulsGldfgBN8J6RrJfZBUCO4GXc8kOWGj97gS6aZy0wp6N_YoJOT-xkfXfHsop63rdx33gbxsHkOdqvP2hx_Zduoce2T-ApdW9_aJGfx6a555pt1HpHTk9T83VBz1ordjNaMVenoDxsweoVUHDmJ80yxVr7ctlpu6H7zG89RSriL_PI7g58jsLvR9PlfJ0YVICA8gg7A3X0S4afQDwencC-a69B-h2uAWyo9MZlJS9V0MgxyUnmfI4Ie3qDfyhdoQRT45-OiYUJ2Edjp4BsFVA4IP6wOx3ZFbSmB_iDmYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای بیلبورد جنجالی در اسرائیل که در فضای مجازی سروصدا به‌ پا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682387" target="_blank">📅 23:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای وزارت دفاع امارات: دو موشک بالستیک از ایران شلیک شده را شناسایی کردیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/682386" target="_blank">📅 23:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682385">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
‏
وزارت دفاع امارات: دو موشک ایرانی که مسیرهای دریانوردی بین‌المللی را هدف قرار داده بودند، در دریا سقوط کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682385" target="_blank">📅 23:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682384">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تلگرام در حال تبدیل حساب‌های کاربری به وب‌سایت است
🔹
مدیرعامل تلگرام در حساب شخصی خود نوشت که تلگرام برای گرفتن دامنهٔ سطح بالای «.gram» درخواست داده است.
🔹
اگر این درخواست از سوی سازمان آیکان (ICANN) تأیید شود، حدود یک میلیارد کاربر تلگرام می‌توانند دامنهٔ شخصی خودشان را داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682384" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYYLIuigPxaHRH4a-S4wyNjGaADh-0zFotd9nmfDh0xk1w3rtN6WKyl4KPIMTAG-rt33muAvoImQvXRs1F04LoSdIGig6B7K1TUwK0FpnCFNg9SvRRvdJhIo2CjmBLmL2yzO3GZDjKcxCCNi25hIA740n76Jm2HwWJ6zm_N2zNiGjOEzff2psTLI8tdKvuVrxszOMuFSmXJ9H9YrvRXSTKFIxfXNp9P8MQ9RF1qyEbWOBaSkenWehrEp-pIN5lkhNZBNJSRqG8GFtCoJjspYH89mjZxcSoJWrWuYV-gmJLcHomg_3crRb1hp2yA4eoCvIQDJ2D2HFcDCSDeWPB1Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام کامل کشتی حادثه دیده در نزدیکی یمن
سازمان تجارت دریایی انگلیس:
🔹
کشتی باری حادثه دیده در نزدیکی بندر المخای یمن، مورد اصابت چندین موشک قرار گرفته و به‌طور کامل منهدم شده‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/682383" target="_blank">📅 23:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682382">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یارانه ۷۶ میلیون نفری وبال گردن دولت شده است/ هر کس یارانه می‌خواهد، برود تحت پوشش کمیته امداد
مهدی پازوکی، اقتصاددان در
#گفتگو
با خبرفوری:
🔹
پیشنهاد من این است که دولت اعلام کند هر کس می‌خواهد یارانه بگیرد، تا سه ماه دیگر برای قرارگرفتن تحت پوشش کمیته امداد اقدام کند. آن‌وقت خیلی‌ها، از حاجی‌بازاری و استاد جراح تا استاد دانشگاه و نماینده مجلس، دیگر مراجعه نمی‌کنند.
🔹
یارانه حدود ۲۰ میلیون نفر تحت پوشش کمیته امداد و بهزیستی باید حفظ و حتی افزایش یابد. اما چه دلیلی دارد به فردی با دو خانه، ویلای شمال یا سفر خارجی یارانه پرداخت شود؟
🔹
بودجه مجلس از ۱۶۰۰ میلیارد تومان در سال ۱۴۰۱ به نزدیک ۱۲ هزار میلیارد تومان رسیده است، اما در سیستان‌وبلوچستان هنوز دانش‌آموزان تخته‌سیاه و نیمکت ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/682382" target="_blank">📅 23:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dadb004324.mp4?token=t5bxXhe_KiXm7e4S2dunMBHgOPPdgprCqibXHbUs5UMg7YZO0Sv-vAF_Xw-d32MIGifN_FlLGmaYoetlQFYE17YN55a7qdUWe1BBW6bHOcmEuobh227I9Uc5x_MDy91HX2wAdHIYuC5yTcHQZXFsyp8j1xv4AboaHLamBQmKIRJaPvVt15PB6YkTVdQfp84PkjJ3bwVniz6nFke02XcOD-RCxYDEaj1YIZoUb-es5e2fj-acb15CBRORoe-8q8lSoklpA8CzVNWzjx3vQXfk2Hbm38yXGvzFGEM8wK0pN3HUHdLNmmcPnoZK4M0Qf_YlJBYyB_b_I6lM1_XGcMZ-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dadb004324.mp4?token=t5bxXhe_KiXm7e4S2dunMBHgOPPdgprCqibXHbUs5UMg7YZO0Sv-vAF_Xw-d32MIGifN_FlLGmaYoetlQFYE17YN55a7qdUWe1BBW6bHOcmEuobh227I9Uc5x_MDy91HX2wAdHIYuC5yTcHQZXFsyp8j1xv4AboaHLamBQmKIRJaPvVt15PB6YkTVdQfp84PkjJ3bwVniz6nFke02XcOD-RCxYDEaj1YIZoUb-es5e2fj-acb15CBRORoe-8q8lSoklpA8CzVNWzjx3vQXfk2Hbm38yXGvzFGEM8wK0pN3HUHdLNmmcPnoZK4M0Qf_YlJBYyB_b_I6lM1_XGcMZ-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش میدانی حسین پاک، خبرنگار حوزۀ مقاومت از تشدید حملات رژیم صهیونیستی در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/682381" target="_blank">📅 23:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
احتمال حبس افسر آمریکایی که به جنگ ایران اعتراض کرده بود
نیویورک‌تایمز:
🔹
سرگرد جیسون واتسون، خلبان نیروی هوایی آمریکا که پس از فراخواندن مردم به برکناری رئیس‌جمهور ترامپ به دلیل جنگ با ایران بازداشت شده بود، گفت که آماده است به خاطر مخالفت و اعتراض خود مجازات شود.
🔹
این افسر در حال خدمت می‌تواند به دلیل «اظهارات غیر‌وفادارانه» یا «سخنان توهین‌آمیز» علیه فرمانده کل قوا و مقام‌های بلندپایه دولت مجازات شود.
🔹
جرمی که می‌تواند به اخراج از ارتش با وضعیت نامطلوب، از دست دادن حقوق و مزایا و محکومیت به چندین ماه زندان منجر شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/682380" target="_blank">📅 23:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682379">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLyIT1piYsePXtugDWWIFfzTDixW2Q9BNz6DTm2YkQjl27tmpPdnd-C_xoJ7_lTHkEd24vB8NyAhOIdWmfV80Hyl56nmjrFPyh8CYS81GPCI3da4TMpa6cQrU24X0N5HhfQyELo8NixoT_qKTpWg-M_vUCuYy0XuBQLgE4t8njGNLr1-OYj6VT4nwh_soQu3zcAWTCk7rY8Gf1LxGy0thhFpZYsjjgGk3ipJyWZrie2B5p_NBuGXSc-ETmsV-KVve0xHhnfdQZ8MLM9v4mRNytAqxCr8y1O6EQ5jL1wTaigdEOrwxI2HEe9uggqF8i6NWbNslQ_JnUY6RUF7aOi_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین مجتمع‌های پتروشیمی ایران بر اساس ظرفیت اسمی
🔸
پتروشیمی بندر امام با ظرفیت اسمی ۶.۶ میلیون تن در سال، در صدر بزرگ‌ترین مجتمع‌های پتروشیمی کشور قرار دارد.
🔸
پس از آن، پتروشیمی اروند با ۲.۸ میلیون تن و مارون با ۲.۳ میلیون تن در رتبه‌های بعدی جای گرفته‌اند.
🔸
در بخش محصولات تخصصی نیز پتروشیمی زاگرس با ظرفیت ۳.۳ میلیون تن، بزرگ‌ترین تولیدکننده متانول ایران و از غول‌های این حوزه در جهان است.
@amarfact</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/682379" target="_blank">📅 23:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682378">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963f08ec7b.mp4?token=QPwYiNj7Y4jjWjUE9_W-y5BaQVKyYtX-uP_duliP3mapFTQ8h3DCBWRv8C6rzRXQGqGaQdDhPS4NlF5S52Ayxk79cVS44xJOesPf97Kv11vm4G_4_0QBUUpwJRzgaMRV48XaYGwPo-SAR6obhBaOpqR8BoHjZkA7f_kwAVTQpWJLj3SaMdUE-qmjtDIW8IP8RF1ESmGAQryxDmD6BeEZ41YT6HRcAyFG7lSbLx_mbyk32aIExS_PYs4mqo5rgMugYme6z_lOaOu0t1O6bwa_QyydFFB9EEGXw6yduC6XHbUoDIdDWfo8M-Dzs0ScPs_fRHKNQj9x4i5bKYr3qA-DKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963f08ec7b.mp4?token=QPwYiNj7Y4jjWjUE9_W-y5BaQVKyYtX-uP_duliP3mapFTQ8h3DCBWRv8C6rzRXQGqGaQdDhPS4NlF5S52Ayxk79cVS44xJOesPf97Kv11vm4G_4_0QBUUpwJRzgaMRV48XaYGwPo-SAR6obhBaOpqR8BoHjZkA7f_kwAVTQpWJLj3SaMdUE-qmjtDIW8IP8RF1ESmGAQryxDmD6BeEZ41YT6HRcAyFG7lSbLx_mbyk32aIExS_PYs4mqo5rgMugYme6z_lOaOu0t1O6bwa_QyydFFB9EEGXw6yduC6XHbUoDIdDWfo8M-Dzs0ScPs_fRHKNQj9x4i5bKYr3qA-DKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قانون جالب پاسکال
🤯
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682378" target="_blank">📅 22:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682376">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsCIq5Ax4IdyJYfGP1rhcELP-8tMk9uNEcygZ5-nCpnbLJBVHNVDm7BGqd7lZutq14aomCD1PUz00nPcx-Ok2ZJPx_n9KpDUx-FbzZVlo8jIrpVpY-TI_WTJKX4IGRHtY71a0UHrbwQfKuiURYJHRYfcqb9TUZ4W29r4BvFL8eaYVQ0o07poLPPdYzd1FchpuEt_GvXPG6_E57fx_5MC3qkMM7bBPqDmwMMcz3XowcMJL0Pxy-A_5uvMix1mM-W0A7UUhjFHPUAz54DFRlktjb8kNBGWpcXU2kI8r-acH250vKNQT-0aMCc31g0JcOIsqQKUp6hOK8oaQkO1N6d9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر رئیس جمهور تغییرات هلدینگ خلیج‌فارس را متوقف کرد
🔹
محمد شریعتمداری مدیرعامل گروه صنایع پتروشیمی خلیج فارس با ارسال نامه‌ای به رئیس سازمان بورس از توقف تغییرات مدیریتی این هلدینگ با دستور دفتر رئیس‌جمهور خبر داد.
🔹
صبح امروز، نامه‌ای از سوی سازمان بورس و اوراق بهادار به مدیران هلدینگ خلیج فارس ارسال شده بود که در آن از مدیرعاملی حسن عباس‌زاده در این هلدینگ، سخن به میان آمده بود.
🔹
بر اساسِ نامه ارسالی جدید، محمد شریعتمداری با اشاره به ابلاغیه شماره ۱۱۳۲۱/۰۴/۰۶ دفتر رئیس‌جمهور خطاب به وزیر نفت، تأکید کرده که تا اطلاع ثانوی، تمامی اقدامات، تصمیمات و ابلاغ‌های مرتبط با تغییر مدیریت این شرکت متوقف و وضعیت به پیش از تغییرات بازگردانده شود.
🔹
او خطاب به رئیس سازمان بورس تصریح کرده تا پیش از هرگونه اقدام، مراتب را از دفتر رئیس‌جمهور استعلام کند./منبع: فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/682376" target="_blank">📅 22:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
زلزله ۴.۷ ریشتری در نزدیکی کاریز خراسان رضوی
🔹
محل وقوع: افغانستان
🔹
نزدیک‌ترین شهرها:
۸۲ کیلومتری كاريز (خراسان رضوی)
۸۴ کیلومتری تايباد (خراسان رضوی)
۹۴ کیلومتری سميع آباد (خراسان رضوی)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/682375" target="_blank">📅 22:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291dd19206.mp4?token=KNbQYEmZQKPMSHpNPSTo6CZn7IU-exTmcZt2HEvueem_CkhphiqIpNvEzLsQFVybrB6-mkTU7tD3Z1jc4R8WZeIse5aMMbKYW4A3-2O2hPG-YNqF1d23IkMMbJnG2a7a_-Qp0bemzOFoPOuAXaVd3Kbt-36x6ht_xJtHtzq05Pzc-Jeb2Mmi1ILyl7NxB6rRlWkHobgzKWHYSddqtGsIZwRZJLfNn0Fnhh2LdrjOf3bCEe4J4dOj5EpFcpi_r6J5w3YO2w6sSJ-fJiGhUzpd8WIJvfDyTH2yswH_N73gyMJZ4sXGDqXxeXwIef7XX42gOzGTboxoDnRgD9bxM_DsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291dd19206.mp4?token=KNbQYEmZQKPMSHpNPSTo6CZn7IU-exTmcZt2HEvueem_CkhphiqIpNvEzLsQFVybrB6-mkTU7tD3Z1jc4R8WZeIse5aMMbKYW4A3-2O2hPG-YNqF1d23IkMMbJnG2a7a_-Qp0bemzOFoPOuAXaVd3Kbt-36x6ht_xJtHtzq05Pzc-Jeb2Mmi1ILyl7NxB6rRlWkHobgzKWHYSddqtGsIZwRZJLfNn0Fnhh2LdrjOf3bCEe4J4dOj5EpFcpi_r6J5w3YO2w6sSJ-fJiGhUzpd8WIJvfDyTH2yswH_N73gyMJZ4sXGDqXxeXwIef7XX42gOzGTboxoDnRgD9bxM_DsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاثیر بارفیکس بر بدن شما
💪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/682374" target="_blank">📅 22:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh-WyfXYjrLwXeTk3XN0Kyc-rMO4JnNzKUDuw75UaZZIYRzO9o-41jP8XrqGDMPnUC1VQokom3wPEzWBf69YRJ8d_djCrU7N1p8ItCaZzSdpvLjMMZK386vCM1pkB7cp5RXpM5PJBwAyaWy5RpBiG6WjNwHgifNxeXBmw7YetgkLjUJCOiqbFaeVm9adWXoMWwALVTgmC7G2AkczQvUJwryRWz9WPhQb4dZetNC5R4i-eU0mYUNy-xfrqBvTnzZx8LS340rz8_qPXLOwSMFQwIgJZAXTiP2pe65RVS_3KyMVfg2rlLsHBAYV_NDN_Ph5-P6c23dB1KWoePRZ7TF6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرکت‌های بزرگ دنیا آینده‌ی مالی‌ات رو بساز!
🚀
فقط توی یکسال گذشته سهام گوگل 75 درصد و اپل نزدیک 38 درصد رشد کرده در حالیکه طلا فقط 25 درصد رشد داشته
!
هوش مصنوعی با سرعت زیادی در حال رشده و شرکت‌هایی مثل
انویدیا، گوگل و اپل
در مرکز این مسیر قرار دارن. حالا کاربران ایرانی میتونن خیلی راحت
سهام
شرکت‌هایی مثل انویدیا، گوگل، اپل و تسلا رو در بیت۲۴ بررسی و معامله کنن.
👉
توکن‌های سهام جهانی را در بیت۲۴ ببین.
https://l.b24.ca/o
https://l.b24.ca/o</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/682373" target="_blank">📅 22:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hao6yYbvzh5gsrgjpznQlPBJqJFhnEtJnsiiggZmQCxJp9lUfzWAg7ONzWtV4H-8uUOMX5--rEqrj7fOPwA43ka8KSL2dmBoHS4xdPuCuYJAeVsNWmrJzipWqY63NDl_9WiondFUWc2kQhOgS41hHEcAQAq7iIOMEvsZGscxHTMb10Nw3N2qMxd6cqiY5nsrk8csBP7ANIuNDRXIqDS6bhGpBonm_zJ4oH_uoAGk8gGqk1LFrIwap_-nXC12JL3MjBGE0hMqz8QSTOHd-rEzxAOalJFg32_Oxmx7oEo4d4YYL16CUgOAyGwnkDmI1J6nwhlYdkbSuGd44iwDPYiAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری مهر گزارش میدهد: هشدار مجلس درباره افشای اطلاعات فروش نفت
🔹
فرهاد شهرکی، نایب‌رئیس کمیسیون انرژی مجلس، با اشاره به نقش «تراستی‌ها» در فروش نفت در شرایط تحریم گفت: اختلافات و تعارض منافع میان واسطه‌ها نباید به افشای اطلاعات محرمانه‌ای منجر شود که ظرفیت صادرات نفت و منافع ملی را به خطر می‌اندازد.
🔹
او تأکید کرد استفاده از تراستی‌ها ممکن است در شرایط تحریم ضروری باشد، اما این موضوع نباید به معنای نبود نظارت و ضابطه باشد. واسطه‌ها باید احراز صلاحیت شوند و دسترسی آنها به اطلاعات حساس نیز صرفاً در حد نیاز عملیاتی باشد.
🔹
شهرکی همچنین خواستار بررسی دقیق هرگونه ادعای افشای اطلاعات شد و گفت صرف هم‌زمانی اختلافات داخلی با اعمال تحریم‌های خارجی برای متهم کردن افراد کافی نیست و باید موضوع بر اساس اسناد، سوابق دسترسی و شواهد فنی و حقوقی بررسی شود.
🔹
حفاظت از اطلاعات زنجیره فروش نفت، در شرایط تحریم بخشی از امنیت اقتصادی و منافع ملی کشور است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/682372" target="_blank">📅 22:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fc7d6d1e.mp4?token=fgpCxZp-Ph-mkqNfZzzylVrp-Hg21qFqPi2M33JbVQt-QYp87sdJOa4HOD6PSKSTzOqd-cpSbnTpm17QoVpYoTXp19Jsve4hgT7A3ZrxnrIOfXCeDrFlEKDZDYEiy2-ijOr9Mkh1sIHT5JCfEWW10gxsrHuo5aoA-YYzjRLr8s0L21VmGmC_6gSPWWDK4MEOdcaTa9gleJikRUFX7ZkEIvkX_d2249rN4VFKqZDe4t5oWth8EkkoyO1pqI2qN7wjTEYooxK4nH5ys9UlDWUndN7Q5GbQDzykf6f883jwiySnPmARGsGk9nrxqmtjzP4Rtt1wujS3kNvA6tiNdMDfKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fc7d6d1e.mp4?token=fgpCxZp-Ph-mkqNfZzzylVrp-Hg21qFqPi2M33JbVQt-QYp87sdJOa4HOD6PSKSTzOqd-cpSbnTpm17QoVpYoTXp19Jsve4hgT7A3ZrxnrIOfXCeDrFlEKDZDYEiy2-ijOr9Mkh1sIHT5JCfEWW10gxsrHuo5aoA-YYzjRLr8s0L21VmGmC_6gSPWWDK4MEOdcaTa9gleJikRUFX7ZkEIvkX_d2249rN4VFKqZDe4t5oWth8EkkoyO1pqI2qN7wjTEYooxK4nH5ys9UlDWUndN7Q5GbQDzykf6f883jwiySnPmARGsGk9nrxqmtjzP4Rtt1wujS3kNvA6tiNdMDfKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن تولد، لباس عروس و حتی آواز تولد برای سگ؛ تصاویری که نشون می‌ده سبک نگهداری از حیوانات خانگی برای بعضی‌ها دیگه فقط نگهداری از یک حیوان نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682371" target="_blank">📅 22:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
واشنگتن‌پست: آمریکا بعد از جنگ ایران حضور در خاورمیانه را کم می‌کند
ادعای واشنگتن‌پست:
🔹
پنتاگون در حال بررسی کاهش حضور نظامی ایالات متحده در خلیج فارس پس از پایان جنگ با ایران است پنتاگون در حال ارزیابی کم کردن ردپای نظامی خود در خاورمیانه است که نشانه‌ای اولیه از پتانسیل جنگ ایران برای تغییر حضور ایالات متحده در این منطقه محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682370" target="_blank">📅 22:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPJyS6y2Ce2hAAgufeBnF3JJJR9ADkUEfRbdP7xEFcgFTJUeAEIeZ4IPkQDIY9hIQg82a20xhiYDqDXmp7kZO3CKqFwSSqKNBHO1WkL1km81th_H8VZ1CoBE7ODcz2cgJwcvT9vtUhRrFEvZZ8iUXfy96lk0HNh7XsoCuAsp2_X7gvJP7m9mWmryM9FzcxleEk_M0exeUJtz7Py9B83vMOA8mS3w_3j9Z0VvykbuQFvHnZbaJQdKyAvWHVBrbw1bQ0os2609Q40lJ9LJuiS8PlYoMQW4DaDkbSkOWTIXqtuTTWE_6aQXGqgBsLIW_H3DND81qjKgmOrRvYh9eQZ_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در حال بررسی کاهش حضور نظامی خود در خلیج فارس است، پس از آنکه حملات ایران ضعف‌های عمده‌ای را در پایگاه‌های آمریکایی در طول جنگ آشکار کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682369" target="_blank">📅 22:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">🎉
۶۶ سال همراه مردم، از گذشته تا همیشه
🏦
شصت ‌و ششمین سالگرد تأسیس بانک رفاه کارگران را گرامی می‌داریم.
#بانک_رفاه_کارگران
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/682368" target="_blank">📅 22:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682367">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
علنی شدن شکاف میان ترامپ و ونس درباره ایران
🔹
ونس هفتهٔ گذشته در گفت‌وگو با فاکس‌نیوز گفت که اولویت نخست دولت در قبال ایران، پایین نگه‌ داشتن قیمت بنزین است و پس از آن، جلوگیری از دستیابی این کشور به سلاح هسته‌ای.
🔹
ترامپ روز دوشنبه در این باره نوشت: «هدف شمارهٔ یک این است و همیشه خواهد بود، اینکه ایران به هیچ‌وجه و به هیچ شکلی نتواند سلاح هسته‌ای داشته باشد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/682367" target="_blank">📅 22:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682366">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شهرهایی که قهرمان رمان‌ها شدند
🔹
برخی رمان‌های ماندگار ادبیات ایران خواستگاه‌هایی دارند که بسیاری از جذابیت‌های آن به خاطر همان شهرها و فرهنگ‌‌هاست.
🔹
در این ویدئو ببینید که این رمان‌های مشهور مربوط به کدام شهرهاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/682366" target="_blank">📅 22:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682365">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۹۱.۰۲ دلار در هر بشکه رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/682365" target="_blank">📅 22:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682364">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNUcWDH2XMUWDr-Vd96VAz2mZFaheOXQx4qqThiUYlN7NdENIsWvLQBNgynCm1cmsEq92zKhZ_UolK_7cy2Q8lth6mG6qSXEh3m07BA5RToolKcpBk-waaEDQ5tAoW4FGv3cFZPB-5Faq6HCBHGrsIG4jlg2HY0AxwneQ0qYM5KSbqoTK8Yo3JDIowm1-Z7vk5HUb90-PAUEQjKudH5g3DPXIIeE0ZHH9-t3HUSlmd2Nz_DqnPABX4tSfQxB3rAX-52CY0aCbWmKD4QGlrX0Y046db19w-i5rn7kjBHDhBXkDInP2rHkzWNPPMsl2UFmJm94n6yhcvNOiZfcF1YxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین افرز: خاورمیانه آمریکایی با جنگ علیه ایران به پایان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/682364" target="_blank">📅 22:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682363">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rydGLhCA4TARVG3Heq0Z3vBr6ek35SXFTG5G2PPCAh-DZjpmpqFpVFwf9dqE8QFGudSys_uU2dHZXrowp56yImiZRReTmVeGWj4UxZbopAMFhyGOhQ0zGHCjM84WMKmtJFAdContN2I0pLsFDMu50UPZ3VsU-M4znYRRC-V-oH4BC9MB_2w_ParBm63vm1y45FGv2fIaiGBdGd55pntnKl-SCvCjzMVQ-0WK7RMPS4GxurwNk_V3qBryNLtM_L7am1kxfStFi28bLU_lwk5ioc76GUUaNGqJDwCAXPlyMRlbhMoDXIhPuJCgNrBoHbeQevc-JUF0KSKvxALW9UkVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا داریوش اقبالی فُحش می‌خورد؟ | دعوا بر سر یک ما | چرا «توهم توطئه» داریوش جنجالی شد؟
🔹
انتشار ترانه تازه‌ای از داریوش اقبالی با نام «توهم توطئه» در فضای مجازی، فقط یک اتفاق موسیقایی نبود؛ خیلی زود به جدالی تمام عیار در میان کاربران فضای مجازی بدل شد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3238706</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682363" target="_blank">📅 22:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682362">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17101087ed.mp4?token=o1JF7satjBgWFyzhwL0dA3b0XJS6-ijYboy_K4HPQ1cM8IbGO8drgw4zs3GdFRmGD3aM9fZV3aEgyWDqufl9iMCmi4wXMRaEMCh79_LxDOlvgf5XL809WQRsJKY6-0F77yrsneHRSt_6WVsTva8D-uXeqVm_-jtNdjzFdauLuDhzsHlSWtah6DNFQuCto6rmxTiUfOL0udMXHA3_PhkeYbb2RmyunylqMdVMrNZkfXpenqaFdRNg0oyuh7oUohrxyzT676BdxrS6uGBxKjJUnvU2CiyVPRe0r47In4cDPmzHbejXGRpXIUcjX7qpHpAEH2immFUnfsGi3Hjy3MSf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17101087ed.mp4?token=o1JF7satjBgWFyzhwL0dA3b0XJS6-ijYboy_K4HPQ1cM8IbGO8drgw4zs3GdFRmGD3aM9fZV3aEgyWDqufl9iMCmi4wXMRaEMCh79_LxDOlvgf5XL809WQRsJKY6-0F77yrsneHRSt_6WVsTva8D-uXeqVm_-jtNdjzFdauLuDhzsHlSWtah6DNFQuCto6rmxTiUfOL0udMXHA3_PhkeYbb2RmyunylqMdVMrNZkfXpenqaFdRNg0oyuh7oUohrxyzT676BdxrS6uGBxKjJUnvU2CiyVPRe0r47In4cDPmzHbejXGRpXIUcjX7qpHpAEH2immFUnfsGi3Hjy3MSf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تولد ۵۴ سالگی عمو پورنگ در کنار مزار مادرش
🖤
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/682362" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682361">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وزارت دادگستری آمریکا: تعدادی عملیات هک از طرف سپاه پاسداران، سازمان‌های دولتی ایران و دانشگاه‌های ایران انجام شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/682361" target="_blank">📅 22:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682357">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjbO0nEGnVtkIpaq4XX5jC293uPY6ELqjuiXUMjP-Q2Rtqn8eBnasUzsBJ79od2fMMw0G0begrURI4c3bzi2yuy9s7vmc5ysXXfFKw740SuFygHUr8uavg_tOV9yfL7vNb4jfaNy1bp00WfuFtAnCq0c1l2qjKHboYFvWInSX25_j1eE_MjxevaoK7X7HluhSV8Z-tOAcNivC_c0v4vTjr3XOwBPwBXYhvk5ZVxAKjgLU5Ved3o6wt5n8JCChRquiRP3eUndSjmkn5iVccbJr7s9TTPlZXI_F-0WLdwmIja-yrMK4wlhb-e4ZQBLCz_1dxO9YeONE3i0sRw2Mxs1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxKC0A3fKzRrH7FMim0DJn5Wp7WfJEYGKQCOnnn9MIvCVSD_MPznLSa9Ia4q9M9NtLS6BpDc6J3kHbLsU_B97KUPHYrZAvrbfsE9wueIMZFT9Uf4oDQGXuwCI_iAjo1d3H6NN09ufdpA1j32aRITj84NudeocVPb3B7wVCJwhxGaobKcwYP5_HVvLq_TbeBV_4wcr63LCpaa-XuiAs7PChOp0J--sKkfHF25WD9AvkZ5F65MiDqlhyR5cQx1osdEqvOtdAIzXitK-BrP6WQTX2AjpWRQ3J77RI-hSNlQyPfRtK3hoTSfEcFIB63bf8YMWcwH80W45h5qWL5Ml4B7gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba97f33e3.mp4?token=jdWStIy0zA5EaHxGZdR03v5AQFzjZuBFdaTQBgjcohwkR4TiqyAS9cb_yjMs1eNYJpOtUE7Zx4tpRyU9lfX94z0sNYvkV4CvYSHl729WohUhXOMSTd52NeEhncMz3pcUuLWJwk0kT21D0fH56jNW_ZjSGcQ-ubZ8TwgbPWMyj2XWsk2RKzBEdXvr1JlpL06a804AubQ3kjjD8SKdIHDUsdjYMSQuIVsd-Ks12goUVcwD64gv_gWsWeADxT7NUc9ipV8lRNXpzNcjuovEffEwEfOIqMi9oH2Kv_H5wPSR2go5Km8lxkgJBo1yfx-zvJtSNQBUQcYIJccchbUU7iWoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba97f33e3.mp4?token=jdWStIy0zA5EaHxGZdR03v5AQFzjZuBFdaTQBgjcohwkR4TiqyAS9cb_yjMs1eNYJpOtUE7Zx4tpRyU9lfX94z0sNYvkV4CvYSHl729WohUhXOMSTd52NeEhncMz3pcUuLWJwk0kT21D0fH56jNW_ZjSGcQ-ubZ8TwgbPWMyj2XWsk2RKzBEdXvr1JlpL06a804AubQ3kjjD8SKdIHDUsdjYMSQuIVsd-Ks12goUVcwD64gv_gWsWeADxT7NUc9ipV8lRNXpzNcjuovEffEwEfOIqMi9oH2Kv_H5wPSR2go5Km8lxkgJBo1yfx-zvJtSNQBUQcYIJccchbUU7iWoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این قانون مدیریت پول رو یکبار برای همیشه یاد بگیر #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682357" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682356">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b4ed298.mp4?token=lsvb-_r1MKxMQNKWcDbnva24Hjwyz1DOdXHPhLTtSw85LxXmiThsxKDDlPeJav8S9dCUvv_nWRySrJErZNWIR5W8iPbnqI6yc8IFeqHRfHXy95c5oamtOrUH09tTmBU0YFulzCMpMObjwVaRyI1rsCTbLCDtHPw-7iJbBxBullmaL73rjig43vMP2HW4jevjIRJezuJwjllDfwpwqT8z-7FTaG6gboQzZ81TMyifwUelSvicY_Rv_vX-lfrWQw9FiQhZkcWWkstuDUScpKP7afqdiKqHDriVlDqKhgFetEIKH88_ud-nTnbBu54IkMRfZ1ox_6T0Gt0se4wrApIW7XU9AFYY9OcY_e-qgUB5CXTfTJ92D9Ud8vSLohS7ZSLcluGgMxDXtE7iyOc8pWJQDjnH6rFHsfMSJ-1oRsiJHNkYJ4loMetvFUPfFQp6BMFajGpUkeC_-I50Mjl2e_HNjpnyTMuc0RnbQgbq2UBNOdI3K3htiBEZuXrvFczLK5kplZxCTjZ0HmDMOZeEsPodV64E26pL7sBeRHk-sUTN86AXWNaXrRt_Nmb6HbirZJOfQ_e4ca4Gfjcd0h8ZFcfrLSBP23_FlMW6mSKQIq0AXVqh1DgwVrUDDImp3RDF2Zdqe-hlsv1hpSU_v_rAsUaXipbeuSgJs44g9i6CPmVr9PI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b4ed298.mp4?token=lsvb-_r1MKxMQNKWcDbnva24Hjwyz1DOdXHPhLTtSw85LxXmiThsxKDDlPeJav8S9dCUvv_nWRySrJErZNWIR5W8iPbnqI6yc8IFeqHRfHXy95c5oamtOrUH09tTmBU0YFulzCMpMObjwVaRyI1rsCTbLCDtHPw-7iJbBxBullmaL73rjig43vMP2HW4jevjIRJezuJwjllDfwpwqT8z-7FTaG6gboQzZ81TMyifwUelSvicY_Rv_vX-lfrWQw9FiQhZkcWWkstuDUScpKP7afqdiKqHDriVlDqKhgFetEIKH88_ud-nTnbBu54IkMRfZ1ox_6T0Gt0se4wrApIW7XU9AFYY9OcY_e-qgUB5CXTfTJ92D9Ud8vSLohS7ZSLcluGgMxDXtE7iyOc8pWJQDjnH6rFHsfMSJ-1oRsiJHNkYJ4loMetvFUPfFQp6BMFajGpUkeC_-I50Mjl2e_HNjpnyTMuc0RnbQgbq2UBNOdI3K3htiBEZuXrvFczLK5kplZxCTjZ0HmDMOZeEsPodV64E26pL7sBeRHk-sUTN86AXWNaXrRt_Nmb6HbirZJOfQ_e4ca4Gfjcd0h8ZFcfrLSBP23_FlMW6mSKQIq0AXVqh1DgwVrUDDImp3RDF2Zdqe-hlsv1hpSU_v_rAsUaXipbeuSgJs44g9i6CPmVr9PI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گوییم دیگر هیچ‌جا برایت امن نیست یعنی این
🔹
با این قسمت از انیمیشن «انگری بردز» همراه باشید؛ جایی که پرندگان ایرانی زندگی آرام ترامپ را از او گرفته‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682356" target="_blank">📅 22:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682355">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26f35d727.mp4?token=SrSr8FoZxZ-ZfE6SZZZt9AGPe-fbw2VL1xbG7yZYGLBHYw5XHO3Z7ZZ18_coIZs1r1gC854s7sTwMurk_IkC6xI0nOzRaQtcpagTwajfjWIPaZ1b6FCfaF--4oZOqxdAcCI1T1_-dBaEJ-5BxkCJxEk-s1eMRb74ue1Fvmtl04OrNSXHOPPO2pM8l4g97GFOyuHcjdqckeAiinx2LkTsu2S6Lt40fWpa5_6pnQjVkzyOE_LPZdxNHmJrzcoIWyc-3QigItGfhNRtWAlJQ00qR8KREI-p4IrWYb2u0q8Iecozu4LdpeG66-Q7pV3-ETfwjKwa1a7IaIsMfwWQyiyX5wNHjR3iZx-Q99indneptasA4jMAPBOFQwY-T7Q18LJz9qArJ1OlWi9S9xVEkMjWMUSgnQ8WK-A4QV7kXD1Ww2bqQpo3ALQ8vGUUaeD8DP2Ga2YeCXyITXENt2zs1GUNzJRBK0mAye6SJeVLvZDxFYgKJ-HuCF2CnxAXVYxGP9yYSz4qwRx7rJul0RBSmA_ivKIRblWlGP76aIHyt2l9rdD_j9COPesusY7La3RIAQPzVNQKdB15Ox-CMEzLz5OX_AcNp4ZrzhAkGmN4Cl9dVGMZyCmXiHrF1szdXsxMl4-09apIgvF-OfvfsHRnY-W3KiH_20bPEYckzg1ozkKqBts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26f35d727.mp4?token=SrSr8FoZxZ-ZfE6SZZZt9AGPe-fbw2VL1xbG7yZYGLBHYw5XHO3Z7ZZ18_coIZs1r1gC854s7sTwMurk_IkC6xI0nOzRaQtcpagTwajfjWIPaZ1b6FCfaF--4oZOqxdAcCI1T1_-dBaEJ-5BxkCJxEk-s1eMRb74ue1Fvmtl04OrNSXHOPPO2pM8l4g97GFOyuHcjdqckeAiinx2LkTsu2S6Lt40fWpa5_6pnQjVkzyOE_LPZdxNHmJrzcoIWyc-3QigItGfhNRtWAlJQ00qR8KREI-p4IrWYb2u0q8Iecozu4LdpeG66-Q7pV3-ETfwjKwa1a7IaIsMfwWQyiyX5wNHjR3iZx-Q99indneptasA4jMAPBOFQwY-T7Q18LJz9qArJ1OlWi9S9xVEkMjWMUSgnQ8WK-A4QV7kXD1Ww2bqQpo3ALQ8vGUUaeD8DP2Ga2YeCXyITXENt2zs1GUNzJRBK0mAye6SJeVLvZDxFYgKJ-HuCF2CnxAXVYxGP9yYSz4qwRx7rJul0RBSmA_ivKIRblWlGP76aIHyt2l9rdD_j9COPesusY7La3RIAQPzVNQKdB15Ox-CMEzLz5OX_AcNp4ZrzhAkGmN4Cl9dVGMZyCmXiHrF1szdXsxMl4-09apIgvF-OfvfsHRnY-W3KiH_20bPEYckzg1ozkKqBts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: آمریکا ابزار جدیدی برای تهدید ایران ندارد؛ ابتکار عمل دست تهران است
استاد علوم سیاسی دانشگاه شیکاگو:
🔹
ایالات متحده به هیچ‌کدام از اهداف خود دست نیافته است. هیچ‌یک محقق نشده‌اند و هیچ شانسی هم وجود ندارد که هیچ‌کدام از این چهار هدف محقق شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682355" target="_blank">📅 22:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
انفجار زیر میز ترامپ؛ سکانسی که پایانش همه را غافلگیر کرد
🔹
یک امضا، یک خودکار و یک انفجار مرگبار؛ همه‌چیز تمام شده به نظر می‌رسد. اما چند ثانیه بعد، مشخص می‌شود که ....
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682352" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0UbDHZB-_n9w9PjZxu_3pIER853Z5R0jLetaLlJ5KIXyJe_DWXjwBgkdlKB_H3btuqAC8pFOStGbsleWerJ7hO1HgCE9v_n1H53M0uEExFcixTOYEIA3Sv3LJC6SDFOOxvlrn4Lf3R-S8ufRxI_IIaVwpVIUnb2V3wESPV-_WoqFrHd2o6aL5zZ7L68mCkpdUJzXi7-S3GQPOS1onr86XEa10RPthVfsmRSiAYAX32uRqlwWk971H-tWKGcXRH_umwzJX6j94eAUQKgaFlG8EslWhyt-8Qp-y0TSYag6iqUXjxog2LolZB749lofYQwCiLs6SUdojwC0JKqG3_5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏡
ساخت یا بازسازی دارید؟ قبل از اجرا، درست طراحی کنید.
استودیو طراحی مهندس وفایی نژاد
متخصص طراحی داخلی، نما و ویلا
از طراحی اولیه تا تصویری که دقیقاً به شما نشان می‌دهد فضای نهایی چه شکلی خواهد شد.
📍
تهران | پذیرش پروژه در سراسر ایران
برای دیدن نمونه‌کارها و مشاره رایگان
👇
👇
@vafaei3d_studio
@vafaei3d_studio</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682351" target="_blank">📅 22:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
وزارت امورخارجه:
🔹
با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/682349" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqVrO8WN4s1QjoKMQkhcU8EAxmOJLTt6_MxklxH92XU_ZtjUC6RGOpIYs-HUgzi8vJIZrGemLAoi-qeNPTPbcCkBVSmNuh5W6YOlMBG2UjQ3z9UgQHl5NRuXQb_Ol6Dg97JfD0mEML9ob2iNjYgCxUeQA5OxqRHf-XAbs42e8v9JGdOfpgl6NQOht4h1U9juHJlA0kW23vLI0fuOGgKXswoJXbGhGdltIbamMWHCkFjZ7T512dek3tyVs0togiZ5bwsOa2m03-DuzTHs-KT_fbIShmkUK2eVY7rGRoZpX9VGPr7gaseYfhwuEZ-uHipH9_s4__3BtQq2mlYRVNTgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرانسه: دو دیپلمات ایران طی روزهای آینده اخراج می‌شوند
🔹
وزیر امور خارجه فرانسه در پیامی در شبکه ایکس ضمن حمایت از اغتشاشات دی‌ماه نوشت که قصد اخراج دو دیپلمات ایرانی را دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/682348" target="_blank">📅 21:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورشکستگی صندوق‌های بازنشستگی یکی از عوامل کسری بودجه دولت است/ برخی از قوانین مجلس آمار طلاق را بالا برده است
مهدی پازوکی، اقتصاددان در
#گفتگو
با خبرفوری:
🔹
یکی از عوامل کسری بودجه، ورشکستگی صندوق‌های بازنشستگی کشوری و لشکری است. تمام حقوق بازنشستگان نظامی را دولت می‌دهد و در صندوق کشوری هم حدود ۸۰ درصد پرداخت‌ها بر عهده دولت است.
🔹
وقتی مخارج دولت بالا می‌رود اما درآمد پایین است، کسری بودجه ایجاد می‌شود. برخی از قوانین مصوب‌شده توسط مجلس آمار طلاق را بالا برده‌ است. برخی پس از فوت پدر برای دریافت حقوق او از همسرشان جدا می‌شوند که خیلی از این طلاق‌ها صوری است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682347" target="_blank">📅 21:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682346">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4282992554.mp4?token=Ypwgp_AFFI2Ifdo0StnQqMZR5Bgw7GCz4mO6UWwSPluy8e5mtYJK7wRCN9qM9GJv1TuJZFkDAwNcm9gPL4UIBN4OP5RR9-yckl2fa9CC3kYDIf1n8ggRssLHkhZktyf8O6KcK7BoB4TkkjXkG0O-UxUPTe_KOLkH2aMj4Ta7wvmTyHS-nfo9bYfZpvHxkFJxlM5JmnbEVXy4gMmRcB85FGb8S8bobsmTSqoGfkEZXKu_6VRDZstS1oLu1f_wH0wDEp89cfXqIHbk8IgLgERgOG5aCelPmaDr-vCRi5edfesy5EAc5DLARQPCWu-vdhi_usP_eOKEDPY3t5vSxq7PFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4282992554.mp4?token=Ypwgp_AFFI2Ifdo0StnQqMZR5Bgw7GCz4mO6UWwSPluy8e5mtYJK7wRCN9qM9GJv1TuJZFkDAwNcm9gPL4UIBN4OP5RR9-yckl2fa9CC3kYDIf1n8ggRssLHkhZktyf8O6KcK7BoB4TkkjXkG0O-UxUPTe_KOLkH2aMj4Ta7wvmTyHS-nfo9bYfZpvHxkFJxlM5JmnbEVXy4gMmRcB85FGb8S8bobsmTSqoGfkEZXKu_6VRDZstS1oLu1f_wH0wDEp89cfXqIHbk8IgLgERgOG5aCelPmaDr-vCRi5edfesy5EAc5DLARQPCWu-vdhi_usP_eOKEDPY3t5vSxq7PFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدرضا صدرالحسینی، کارشناس مسائل غرب آسیا: خروج نیروهای آمریکایی از عراق همچنان یکی از مطالبات اصلی بغداد است و نخست‌وزیر عراق هم بر آن تأکید دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682346" target="_blank">📅 21:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682345">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee31e797fc.mp4?token=j8S0Qfu_8R1WiJ9QJ3eab3q5ueTPgw_rrbehi6yLtSSP34i2H8u2_npFNCaf1_Q32o1lZjTsaeLi8wOX7-bgk10JEKQAIdvTC3xGs_Tr6vrDlUf95mD3dMpXfz33-Tm6bWNuJ7G5irnYL1nPiXS_tx0_RjuQU2nqua2lPt9MIY7ypAFEWaU4G34vcOkcw6cvYV6S7GAwg9GOKPUS4GsNuK3A4UsHRv2E5FaSSNwhDuSaDogS6SAFW-NdfE-4vO35uAHbsJNAMxjH9Fw1-BXuXmQAzexHOFfrf1F0-oHecbEJQsBAZyFElvgQlaV6DgX4AgJhsBTUpH3TH-bdgstcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee31e797fc.mp4?token=j8S0Qfu_8R1WiJ9QJ3eab3q5ueTPgw_rrbehi6yLtSSP34i2H8u2_npFNCaf1_Q32o1lZjTsaeLi8wOX7-bgk10JEKQAIdvTC3xGs_Tr6vrDlUf95mD3dMpXfz33-Tm6bWNuJ7G5irnYL1nPiXS_tx0_RjuQU2nqua2lPt9MIY7ypAFEWaU4G34vcOkcw6cvYV6S7GAwg9GOKPUS4GsNuK3A4UsHRv2E5FaSSNwhDuSaDogS6SAFW-NdfE-4vO35uAHbsJNAMxjH9Fw1-BXuXmQAzexHOFfrf1F0-oHecbEJQsBAZyFElvgQlaV6DgX4AgJhsBTUpH3TH-bdgstcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: رژیم صهیونیستی از فعالیت‌های اخیر شهید لاریجانی در زمینهٔ حل مسائل دیپلماتیک عصبانی شده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/682345" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682344">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
با ۴ قلم به راحتی در خونه بستنی مگنوم درست کن
🍦
🔹
موز ۳ عدد
🔹
خامه صبحانه ۱ بسته
🔹
پتی بور ۱ بسته
🔹
شکلات خرد شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/682344" target="_blank">📅 21:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682342">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b046f6e2eb.mp4?token=gg8HZDuSOLk7-jZiHr1PQUO8Uq-b0pkMORiMS43KJPPq073AcNtuLNPt06YO_yS3tisMnYPmZ6sfrGdGjSOQiisSTPL6V_xGeVw8Si-ZW7eKtbmEuTtN67VLjpNc-uiJZ4dHI4zBiRbr_zOQ6YhtxFRb9thkU1HXeg0N8-FOtRNfy2_y_ScD7whcqLSNyFzAi6e4oebKLCVI_H_wECzQJHnRmCQkEY8LlBy482MCf08rXhNKS8Grm8iE-r_3j_snJ3ut3qRQWNDkrYow4Ird32aDERDHi02ZYh_T1PFKNCgkByekewgYMEmGKV2ECuEMnkIweySZlJ0vIUWtQQa9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b046f6e2eb.mp4?token=gg8HZDuSOLk7-jZiHr1PQUO8Uq-b0pkMORiMS43KJPPq073AcNtuLNPt06YO_yS3tisMnYPmZ6sfrGdGjSOQiisSTPL6V_xGeVw8Si-ZW7eKtbmEuTtN67VLjpNc-uiJZ4dHI4zBiRbr_zOQ6YhtxFRb9thkU1HXeg0N8-FOtRNfy2_y_ScD7whcqLSNyFzAi6e4oebKLCVI_H_wECzQJHnRmCQkEY8LlBy482MCf08rXhNKS8Grm8iE-r_3j_snJ3ut3qRQWNDkrYow4Ird32aDERDHi02ZYh_T1PFKNCgkByekewgYMEmGKV2ECuEMnkIweySZlJ0vIUWtQQa9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ظهر روز اول جنگ رمضان به همه کشورهای منطقه هشدار دادم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/682342" target="_blank">📅 21:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682341">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJYIR-ZD9OT3DqdGrDvw9WUUCqYM_gFh6B6p7ETytranr52RFc2q0F5xZs3CjnoaJGzd1zmYnOOGxnRgbovSvNRrskUMVl7W7NgIfWnbDMk7v10e4iNRc7HP_QHJIpyJXKe4tha9JjytHRMYzNpMLb-1iPkiDO3aY2_SC1ZztPiGxdY2PH0WUf83EMB2PtLiXqQpoplf2_EP-xFpoWhaiVDBRhb03AtTwMJmFb6g3P_2mwrxcbuUvHrhPUHrsZWNGaP36u5ymY05wDDaTEKWnM38_vvu-urgCCdQW62C4_HwrpozwPgvIGMW_tCDKbBjIfnfmc5n60IOprJ9Ufhe0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۱
🔹
ثبت نرخ ۹۰ درصدی برای وصول مطالبات بانک کشاورزی در سه سال اخیر
🔻
بانک کشاورزی در سه سال اخیر توانسته است نرخ وصول مطالبات را به بالاترین سطوح سال‌های اخیر رسانده و تثبیت کند؛ موفقیتی که در کنار رشد مستمر پرداخت تسهیلات و کاهش ریسک اعتباری، بیانگر ارتقای انضباط مالی و اعتباری، بهبود فرآیندهای وصول و افزایش کارایی مدیریت منابع این بانک است.
🔻
این بانک طی سه سال اخیر موفق شده نرخ وصول مطالبات سالانه را با روندی صعودی به کانال ۹۰ درصد رسانده و حفظ کند؛ به طوری که این شاخص از ۷۶.۵ درصد در سال ۱۴۰۱ با جهشی چشمگیر به ۹۰ درصد در پایان سال ۱۴۰۲، ۹۲.۳ درصد در اسفند ۱۴۰۳ و ۹۰.۵ درصد در پایان سال ۱۴۰۴ رسیده است؛ دستاوردی که از اثربخشی سیاست‌های اعتباری، بهبود فرآیندهای نظارتی و مدیریت دقیق چرخه بازپرداخت تسهیلات حکایت دارد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/682341" target="_blank">📅 21:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e57f1913.mp4?token=nup96tc1YVA0GN6ImJb0P2aT47Q2JrNMbicbHRMRGr7JQ67zulmGwibWD8-fwlIVpyvF66fu_clWrK0HVyUfs2iIe6OHb7SVN66WugjwUWYmzpxENanYZ37xjhDFp-2qQAIeOKf8_MMx2W6VSbFX1SiFDkH5_3I4nyPZx41pNszFCq_xsdc6cSeg6VBTleJ2PCsXpPAPDO91-ulfVCIJSEa47Y5yQs3lH6GTieyYZkbz5zI8HPLbz4RwNBdYVNsi3BJpIfzVJ8nNeLww6ubPlN2Mv4Ljn1B2mxJYyp4AJNiUTV2623Q2Sq-KGF9Vo7klh0FtImxJ-KdABg0StSyQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e57f1913.mp4?token=nup96tc1YVA0GN6ImJb0P2aT47Q2JrNMbicbHRMRGr7JQ67zulmGwibWD8-fwlIVpyvF66fu_clWrK0HVyUfs2iIe6OHb7SVN66WugjwUWYmzpxENanYZ37xjhDFp-2qQAIeOKf8_MMx2W6VSbFX1SiFDkH5_3I4nyPZx41pNszFCq_xsdc6cSeg6VBTleJ2PCsXpPAPDO91-ulfVCIJSEa47Y5yQs3lH6GTieyYZkbz5zI8HPLbz4RwNBdYVNsi3BJpIfzVJ8nNeLww6ubPlN2Mv4Ljn1B2mxJYyp4AJNiUTV2623Q2Sq-KGF9Vo7klh0FtImxJ-KdABg0StSyQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بایدها و نبایدهای قبل و بعد از کنکور!/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/682340" target="_blank">📅 21:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682339">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMhssN2ygzEcFoFuLU0iQNlhTvib5gEVP21YP9j1Xhro03wFbLWiwgVpvHvbpR9pN7JIZvZpCmIJvB5iKfszJyB4JBgUqkUdK3WAInpHaBs3Yr2r9pZfIj0f4iSprTgPjuXrAGvkjN07KORhCTksUf1us5YzT7fVndqQVqrNT2Zfno1v_o9f42byFYfsR_Wk1VM4Il6FsPkdK7mdZ8kfrevEVghgorgjRiA-6-AuCa8FnEv1oE9BYRWc7ycN_x4ORBeLGXy_ENO_bgW60eLmS0M17lVhB_0FeOAOF5bfooo1HmOAhx3MyKlno2V28eQU08xem2XvSHVe1PSB1sXDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه کسی واقعاً آمریکا را اداره می‌کند؟
استاد جیانگ:
🔹
ایلومیناتی‌ها امریکا را اداره می‌کنند و از سه گروه اصلی تشکیل شده‌اند
🔹
یسوعیان‌ها، واتیکان را کنترل می‌کنند.
🔹
فرانکیست‌ها که امروز دولت مدرن اسرائیل را کنترل می‌کنند و فراماسون‌ها که دستگاه امنیت ملی امریکا را کنترل می‌کنند.
🔹
آن‌ها باور دارند که اسرائیل، این جنگ در خاورمیانه، کلید دوران آخرالزمان در ایجاد بهشت روی زمین است.
🔹
پس تقریباً مثل یک فیلمنامه‌ای است که آن‌ها دنبال می‌کنند، حتی اگر از نظر ژئوپلیتیکی، معنایی نداشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/682339" target="_blank">📅 21:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682338">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad568cddf7.mp4?token=ZCIMg7mslB8AtWf-M0dCT9q48xu7mAkpmH7vzShOKuRVrUMbJqzr4Gneaw14OrP6urXIOUy3C8JhaKK6kUBdA9M6Ch-DQhTStNN6Phj486r7iv3rr5SVPSZg_d7UiR07b1Ys1J933B0YxeNzB_8pFsXhJH2kdiZhuNbXXBi5GqmhoDiw-qPxL0lrFRHveu2fO2y9nL7fLOy6zfZL0heHoiKf3N4s6xpzVD0sL87BjeityoG5FupsChIPgRDo4dTcGzCKpSf03A6BgA8VrGJERw6aAUDsinSw9Gkh__s3Cl2uc3Ix6EG7_9N0ahlGa7nxny2Rdkkt2I4Jnh3SKVwYgkXBOj7S-o_o_2VFBnQ6m1bnW8qJ3HqkjmXxxMUcVnCxjucarbJy_uWh1Kk5v03UCFjKHa8nvJWUKmRwR-yglHrHuKH9pfeaYDtXcd1N2YghymBnn1JA3n0AEoDTOU-OiM7HPn-mvm5Ew_Nx1K-hSKMNOMr9t4VO9BSMOuJyvai5tZ7afSAfdALslZOIb816-xV9gMoWrtKJAoG0Su3UEDMgGTLgdSfI2Xmk7sFGp6psAO2yWoerxb250YlqTTR1jgN3TKnwyXoRUvCLX8deM_dyEeC1lJW9TyM-YiGUzV3wN4L8zD8gcratJWgTLZkPgyaDRASzPqIYNdIcv6n1jDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad568cddf7.mp4?token=ZCIMg7mslB8AtWf-M0dCT9q48xu7mAkpmH7vzShOKuRVrUMbJqzr4Gneaw14OrP6urXIOUy3C8JhaKK6kUBdA9M6Ch-DQhTStNN6Phj486r7iv3rr5SVPSZg_d7UiR07b1Ys1J933B0YxeNzB_8pFsXhJH2kdiZhuNbXXBi5GqmhoDiw-qPxL0lrFRHveu2fO2y9nL7fLOy6zfZL0heHoiKf3N4s6xpzVD0sL87BjeityoG5FupsChIPgRDo4dTcGzCKpSf03A6BgA8VrGJERw6aAUDsinSw9Gkh__s3Cl2uc3Ix6EG7_9N0ahlGa7nxny2Rdkkt2I4Jnh3SKVwYgkXBOj7S-o_o_2VFBnQ6m1bnW8qJ3HqkjmXxxMUcVnCxjucarbJy_uWh1Kk5v03UCFjKHa8nvJWUKmRwR-yglHrHuKH9pfeaYDtXcd1N2YghymBnn1JA3n0AEoDTOU-OiM7HPn-mvm5Ew_Nx1K-hSKMNOMr9t4VO9BSMOuJyvai5tZ7afSAfdALslZOIb816-xV9gMoWrtKJAoG0Su3UEDMgGTLgdSfI2Xmk7sFGp6psAO2yWoerxb250YlqTTR1jgN3TKnwyXoRUvCLX8deM_dyEeC1lJW9TyM-YiGUzV3wN4L8zD8gcratJWgTLZkPgyaDRASzPqIYNdIcv6n1jDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌و‌هوای مراسم چهلم رهبر شهید انقلاب از لنز خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/682338" target="_blank">📅 21:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682337">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-Axg7FaU_Udu8YiK95RIt-0DOsZiWRqFpiafdAlVFYMn-TTZyfxwYPTD4s_XC-NittRdpTlKykq9Ow75V2BZ7dXdGXvwIElIRwEb3PNWCjU6JhXMA47VYvf5Ffku30RMeaW7Z87ok0-300sI4AAFy1XAMFE9R3_OCVPHsyl2BLYnOp3kMP0jIPbOnDnOBrXPXJRaQtdEdxENqFIpLcIkyykqUvjdhT_J7YuMlnGKqWiAJ6bc4RMqxfHWYNpxl1dL99uwQ_lAR3dBVDpZU818pxm58LtaSnxN94FS3a1LAOCP1dPvVw9axiEQtiBJOtW7bsIJXM9qoAazZF8dbgF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: بیگانگانی که از هزاران کیلومتر دورتر، طمع‌کارانه در خلیج فارس شرارت می‌کنند، جایی در آن ندارند مگر در قعرِ آب‌هایش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682337" target="_blank">📅 21:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682336">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c91454bf7.mp4?token=vpME581UUQ86Xgd_ZICNwvwp8Mcqs_mS0Aoj91qa9QCMFo05GA9-Mk5WVnZL5C-bAZlW4zKVoa3ksI7zxqh9rkFb2v4D228s79HZHcXe7Qu7JXfyjoli1waPgPgJDKfzE_Mq4x-IkQMN1LTbsxZENWNWM1hoBMb4K6JVzTGtkPdeyU7SyXT7nubUqBkpQXLjKL2spy-IBlQCOtsumeFnMcaXxxHFBnkVfeUeR8UbtTGhYBJF58ulg9g8lJ__ba3u_0lF7nh_mh0a6QxyZ9BQCuGFHd-pJrfLdBVC9VWi1HC7UY7dq7hSwGE5QvLqXPjJQpcfD_pzMBnZxt382Wu6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c91454bf7.mp4?token=vpME581UUQ86Xgd_ZICNwvwp8Mcqs_mS0Aoj91qa9QCMFo05GA9-Mk5WVnZL5C-bAZlW4zKVoa3ksI7zxqh9rkFb2v4D228s79HZHcXe7Qu7JXfyjoli1waPgPgJDKfzE_Mq4x-IkQMN1LTbsxZENWNWM1hoBMb4K6JVzTGtkPdeyU7SyXT7nubUqBkpQXLjKL2spy-IBlQCOtsumeFnMcaXxxHFBnkVfeUeR8UbtTGhYBJF58ulg9g8lJ__ba3u_0lF7nh_mh0a6QxyZ9BQCuGFHd-pJrfLdBVC9VWi1HC7UY7dq7hSwGE5QvLqXPjJQpcfD_pzMBnZxt382Wu6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده مجلس:‌ با وجود این که ۲۵ سال است از مونتاژکاران خودرو حمایت می‌شود تنها ۲۰ درصد موفق به داخلی‌سازی شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/682336" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682335">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وقوع حادثه برای کشتی در نزدیکی آب‌های یمن
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای کشتی در فاصله ۴۰ مایلی بندر المخا در استان تعز یمن خبر داد.
🔹
این نهاد انگلیسی تصریح کرد که کشتی مذکور پس از حمله در مقابل بندر المخا دچار آسیب شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/682335" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682334">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlMYWMw7lq5QAJ5ew7vygi441VVkXyXjG0tmX6ceeyggdTiBdcWm-Br-uepualfor9QwXRCl-JY02gcfSkN07dvZvGI59B2ayAjc8B3Po0YkjinOfu4lwaey8e9N308DjFaXe-VEcv8mty09-Q0DNmMy4PsMeEj2dWmSx_T7grcgA9SOVsDZsqP2S8Xo8vjvqMkvWFiJObasvzZNd7QQoDPicaMHi9Bou8cZYpqv8S9y5BICtDQJRN1-IXLWImwZ_jwjv_faHD9lIy3m8OUt9_oHsNEmsOYRCFfFymYXGzy7WZ7a4itjIb0nxgmyL3eyYYqCVWqNs-juzG49VAkklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: به نظم پساآمریکایی در خلیج فارس خوش آمدید
سرلشکر پاسدار محسن رضایی:
🔹
شکاف بین ناتوانی آمریکا در بازگشایی تنگه هرمز و ادعای مالکیت آن، از فاصله ۷۰۰۰ مایلی بین واشنگتن و خود تنگه نیز بیشتر است.
🔹
به نظم پساآمریکایی در خلیج فارس خوش آمدید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/682334" target="_blank">📅 21:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682333">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2a62fbe1.mp4?token=e5hAPdnsYyj9oS-K0CkQHsYMI2nTRjGtxtCVN-tcextsztxFvnJ4UkEj3XIFaDDLgF2Nze78pzxGZo1xsbT7DiDlwQJQCNv1Tq5cLxkZrIQr4cAADU1CNHI1kdb0Ws2BWQ5z6iMTuixxYcl22rdXF5lJ4LZydDui2a9FmxCmMwJaLQEnEphp0Y1guxSznVWG-f0TOpxfIIwHkSC2whdPqNjHtybTQZq2VRbqKCQO-kjwAyM-0-ydq8pj_i_9LEkUSi82paeTb5C9c8f1mceMejrl7OnT0Trgnejp2IZ0WxgJWLmC7aNb1WpcdPHxVWaE4SaW-ayyghK9eWAitnICsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2a62fbe1.mp4?token=e5hAPdnsYyj9oS-K0CkQHsYMI2nTRjGtxtCVN-tcextsztxFvnJ4UkEj3XIFaDDLgF2Nze78pzxGZo1xsbT7DiDlwQJQCNv1Tq5cLxkZrIQr4cAADU1CNHI1kdb0Ws2BWQ5z6iMTuixxYcl22rdXF5lJ4LZydDui2a9FmxCmMwJaLQEnEphp0Y1guxSznVWG-f0TOpxfIIwHkSC2whdPqNjHtybTQZq2VRbqKCQO-kjwAyM-0-ydq8pj_i_9LEkUSi82paeTb5C9c8f1mceMejrl7OnT0Trgnejp2IZ0WxgJWLmC7aNb1WpcdPHxVWaE4SaW-ayyghK9eWAitnICsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: جنگ اخیر ثابت کرد آمریکا حتی از پایگاه‌های خودش هم نمی‌تواند دفاع کند  وزیر امور خارجه:
🔹
جنگ‌های اخیر نشان داد کشورهایی که فاقد پایگاه‌های نظامی آمریکا بودند، آسیب کمتری دیدند؛ در حالی که پایگاه‌های خارجی نتوانستند حتی از منافع خود در برابر ضربات…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/682333" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682332">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2cDs4rPY7x2F8UpV1tuW2mzeFYanpQJUPtgRXwPLCxgV5e-fdFeVpJgqwwEuKz2js455JSsxi_mvUtI0mBRBM2WerdT04mV0bSEVXYGShkmzV8Y-R5jq4inU-cv_6um0Yt4VMsFvnipu3jtqHR_osMvx02TYVqcPJ55e1l_NmCdVW-laiUGmEP1TH4EdXYw03gh1-MVJt_4O7idIELCLRTPmsUw6pWjTTs2JJzOmKpiOKmEKvwfbuNNw3BdLi4COZDuLUyCLbbNJHhrnJFY13Gdi3DESgsRuiD0f1sqFbmC4xbl5QgNrMX9x_nzCJ1eYgpehsUQfakJWVDiC-0pLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا استفاده از آمپول‌های لاغری برای شما مناسب است؟!
⚠️
این روزها اسم آمپول‌های لاغری (مثل مونجارو) زیاد به گوش می‌رسد؛ اما این روش درمانی برای همه مناسب نیست و مصرف خودسرانه آن می‌تواند عوارض خطرناکی به همراه داشته باشد!
پرسشنامه زیر توسط جمعی از پزشکان متخصص غدد و تغذیه تهیه شده تا شما با پاسخ به چند سؤال کوتاه در کمتر از یک دقیقه متوجه شوید آیا شرایط استفاده از آمپول‌های لاغری را دارید یا خیر.
🟢
شروع ارزیابی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/682332" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682331">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q84Hagg0444bazWYebO5DYNJuAGX9Va1JYB_Q0U_kxtrpBy61GORkATknyFb9kMvrENoLcB_0LEckwY5sWJfe2l7l8ufD_hmzCsF0aHTEZ1Yk3aRExeX1k9fpfa_DE9vqKCnTF6ViX0AahMBsJVLir9wsXE8d5dE-SNATVADotzjCfEtBb3VYuW6jpl8tDs_Uz-mDrrB5l7W5Yeymw36z4aEx7vBij2Cy0O8qZn7hp4XzY-CII3_qczAQ2hwcDJ3sMamaUseTp_umDts04AJHYgQlnhC7zpoW6Zfcwy7cYZ_RlqJY_1Xb-MVahfHJF5fRk3lGG89cJPdESLrbzOP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۲۶ درصدی تراکنش‌های «تاپ» در نیلسون ریپورت ۲۰۲۵
🔹
به گزارش روابط عمومی تجارت الکترونیک پارسیان(تاپ)، جدیدترین گزارش نشریه تخصصی و بین‌المللی نیلسون ریپورت (Nilson Report) شماره ۱۳۱۲،  مربوط به عملکرد سال ۲۰۲۵ میلادی منتشر شد.
🔹
آخرین گزارش نشریه معتبر نیلسون ریپورت حکایت از آن دارد که تعداد تراکنش‌های پردازش‌شده توسط تاپ در سال 2025 به ۸.۰۲۷ میلیارد تراکنش رسیده که نسبت به سال 2024، رشد ۲۶ درصدی داشته است.
🔹
بر اساس این گزارش، شرکت تجارت الکترونیک پارسیان با ثبت برجسته‌ترین عملکرد عملیاتی، موفق به صعود به رتبه ۳۸ منطقه خاورمیانه و آفریقا و کسب رتبه سوم در میان شرکت‌های پرداخت الکترونیک (PSP) ایران شده است.
@AkhbareFori
|
Link
:
👈
لینک خبر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/682331" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682330">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
عراقچی: زمانی‌که آمریکایی‌ها در جنگ درخواست مذاکره کردند، آقای پزشکیان معتقد بود باید به این درخواست‌ها توجه و راهی برای خاتمۀ جنگ از این راه پیدا کنیم
🔹
آقای قالیباف به پیشنهاد رئیس‌جمهور به ریاست تیم مذاکره‌کننده انتخاب شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/682330" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682329">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6a90c8b3.mp4?token=sJSmRbSHt9KEdKlcAGU1jUZ_givxoZLHucAgIFoZdz7rOJrpj09J1Y6fdSDGDXDtsPCOhchFKWwwexk-DfjuSgFqQLVKIvUkyBQxl4IyY4LLLJClYfC9BVqbgrwnKbDI09otjr_rHlTRhH_1n60x8aKnp4rWzWLyugea6dm4JxReIP9cs14rlZSWxgZvOFb3d0h-FaG4Ex5JW5JXNcbfGvlziMF-bQ8-eDRG5deu6Q74O9Yr7zsHvTw3Jwmz6uJ_aqrKAfiQ94zzSpNsapc5ALkrztwHwJ8HYiDdsgr4gYDTg-hRxhASOtiDnJ1D4wgUUu2x5mPXoq50DQrqF-Ppvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6a90c8b3.mp4?token=sJSmRbSHt9KEdKlcAGU1jUZ_givxoZLHucAgIFoZdz7rOJrpj09J1Y6fdSDGDXDtsPCOhchFKWwwexk-DfjuSgFqQLVKIvUkyBQxl4IyY4LLLJClYfC9BVqbgrwnKbDI09otjr_rHlTRhH_1n60x8aKnp4rWzWLyugea6dm4JxReIP9cs14rlZSWxgZvOFb3d0h-FaG4Ex5JW5JXNcbfGvlziMF-bQ8-eDRG5deu6Q74O9Yr7zsHvTw3Jwmz6uJ_aqrKAfiQ94zzSpNsapc5ALkrztwHwJ8HYiDdsgr4gYDTg-hRxhASOtiDnJ1D4wgUUu2x5mPXoq50DQrqF-Ppvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به نساجی توسط آزادی
🔹
استقلال ۱ _ ۰ نساجی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/682329" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682328">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084c864e2a.mp4?token=XZEdYedPUIGYU-OUsVoSzP4HY8fxTZIH2CdJuzN324z00wWnUs3Q4PxnqNrre6Xnxeyqgby-bfF4liBcwue2birV5YyNnV3yLRZg-fo5BBgGPVQ2Lyavh3Qd9r74l4OCldBIM1EQNGiI-KmlY_XjelN_MWYr1NKljVOmNe4wTprb67nE4Myrmzw7Qvfi1RM42Po_JPKGKXTobD9YdI4asmuBl4MyuyhBq47YrRCTyzQNvBKi4Ta06EKkaYRog6VOjgSnykb2CygBD1tlAoQOrA1xcMImhoNKeW00Qazmft-3i6JOCVmqKLIcEgi6KxsASpWwAZpaI26MAS67rPhIwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084c864e2a.mp4?token=XZEdYedPUIGYU-OUsVoSzP4HY8fxTZIH2CdJuzN324z00wWnUs3Q4PxnqNrre6Xnxeyqgby-bfF4liBcwue2birV5YyNnV3yLRZg-fo5BBgGPVQ2Lyavh3Qd9r74l4OCldBIM1EQNGiI-KmlY_XjelN_MWYr1NKljVOmNe4wTprb67nE4Myrmzw7Qvfi1RM42Po_JPKGKXTobD9YdI4asmuBl4MyuyhBq47YrRCTyzQNvBKi4Ta06EKkaYRog6VOjgSnykb2CygBD1tlAoQOrA1xcMImhoNKeW00Qazmft-3i6JOCVmqKLIcEgi6KxsASpWwAZpaI26MAS67rPhIwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی، وزیر امور خارجه: رئیس‌جمهور به همه مردم توجه می‌کند نه بخشی از مردم
🔹
دوست و دشمن به اخلاص رئیس‌جمهور اعتراف می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/682328" target="_blank">📅 20:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682327">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2238f7d033.mp4?token=MqLW9Hye2SxDx-bweGuT0kdkjILJlp4x_Hh4GFPVkToZDTQvHa3qBSkvcwo3IJtIAwnxdfr-Esl0AK27IwNbBwNYzkpP42cNUleb0QA8QUyvGVYP8JhNubGqdKhlATCrPbbbPg_ZxyBEWuTsh8YOVqtKEW1l2kjRflwLrK73b7UJoWj5rTPUrk7CxpOTSMpzq5FnFezPs-gTaL-Xp_ApXDUCFRERd4wPvYiU2PHpwvSpZfQ6jFLEfuXzj3p_0-B0octSDhFHhE6yTSrEYPYTeMr5LlGqX77AeHnaS2d5qpr0XU8gLE5Gjjb7sciAl8Lanz1pA78UjKg9jGJhLCEnXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2238f7d033.mp4?token=MqLW9Hye2SxDx-bweGuT0kdkjILJlp4x_Hh4GFPVkToZDTQvHa3qBSkvcwo3IJtIAwnxdfr-Esl0AK27IwNbBwNYzkpP42cNUleb0QA8QUyvGVYP8JhNubGqdKhlATCrPbbbPg_ZxyBEWuTsh8YOVqtKEW1l2kjRflwLrK73b7UJoWj5rTPUrk7CxpOTSMpzq5FnFezPs-gTaL-Xp_ApXDUCFRERd4wPvYiU2PHpwvSpZfQ6jFLEfuXzj3p_0-B0octSDhFHhE6yTSrEYPYTeMr5LlGqX77AeHnaS2d5qpr0XU8gLE5Gjjb7sciAl8Lanz1pA78UjKg9jGJhLCEnXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: کُردی صحبت‌کردن رئیس‌جمهور روابط ما با کردستان عراق را تکان اساسی داد
🔹
ارتباط کلامی آقای پزشکیان با رئیس‌جمهور آذربایجان روابط ایران با جمهوری آذربایجان را از این رو به آن رو کرد.
🔹
در جنگ ۴۰ روزه مشکلی پیش آمد که رابطۀ ۲ کشور را تلخ کرد اما یک تماس…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682327" target="_blank">📅 20:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682326">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6284525301.mp4?token=f3ek6MIfv1zR7rhkK6IxgFrFHYMqVWixtY0d-U3DJcPai1l6jTgiIZK5GCzH33gYuJlacnDVSWMDqrjjJa_tQx9Kx1pav_zv10wxE_cegGxN5gLJjsY5o6czbJCGo8lZMQTrsXGqjz28RMk8MJ-Kj6BVRzLccdvPZabmQbopS6DSqN_YZsshvYafVmu_cpSCf-aKnVxwgSQ1YCFEI833GxGgKTiyYfPshHI7RMlqT70Iqofe-4PdAVsxJy264cMLN3HvgcgRyaM96-JgwUooa3PllnAk1wKQMYUOMCkWS_Y_3HZ4oN_vblyOd3CMa1hMCR6K96jHDKVzlYhMRT3uhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6284525301.mp4?token=f3ek6MIfv1zR7rhkK6IxgFrFHYMqVWixtY0d-U3DJcPai1l6jTgiIZK5GCzH33gYuJlacnDVSWMDqrjjJa_tQx9Kx1pav_zv10wxE_cegGxN5gLJjsY5o6czbJCGo8lZMQTrsXGqjz28RMk8MJ-Kj6BVRzLccdvPZabmQbopS6DSqN_YZsshvYafVmu_cpSCf-aKnVxwgSQ1YCFEI833GxGgKTiyYfPshHI7RMlqT70Iqofe-4PdAVsxJy264cMLN3HvgcgRyaM96-JgwUooa3PllnAk1wKQMYUOMCkWS_Y_3HZ4oN_vblyOd3CMa1hMCR6K96jHDKVzlYhMRT3uhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه: نگاه کشورهای غرب آسیا به ساختار امنیتی منطقه بعد از جنگ رمضان تغییر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/682326" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682325">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8QQb3h0XAWy647eeYrnqIB9WulT3HLfGQw6dZR7eLXlz5E6mRPxgSeSqqF4TkocGgfBVD5HOoxG14GwnMkMz3vQJ_kfKjJBLKL7J9eBwf6uYt-8GQGpejQYOIWump9f5m-A3G_ZHF2qR9ZKpPSSTOu6APnC31fDf8PTKy60FGEaBmy17DyJInwMD1s4RFFRPHsIFW_eqyaNdQovjCmwvSyEm2F4eWm-pqmUB5Q9d0W8xCrkSwZ6zxKlRaYFWIQWz2iVRWM6-nmXxN5cIXKRXWG9IdrbHcuOrNaCobrvAKiDl0_q1GdJRaERKa9YY21TjfVSCVKDIuVZXm4ep-GqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکایی‌ها خیال می‌کنند با فشار بیشتر بر ایران می‌توانند امتیازاتی بگیرند که اصلاً بخشی از توافق نبوده است
🔹
وزیر خزانه‌داری و وزیر جنگ آمریکا در حد و اندازهٔ این کارها نیستند.
🔹
منتظر نباشید که این تیم دلقک‌ها خرگوشی از کلاهشان بیرون بکشند و گندی که زده‌اید را پاک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/682325" target="_blank">📅 20:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682324">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e9d06f8f.mp4?token=Eaaqoc9H5jDqcDM-jW8iyPZWvXV-rfI30IuDMBbp0zb0I3di_OcKOSbDw6M7tIsGfSgzJUcrPXRYUl1vzWQoKBbz8Ry-QtAeyULiFnfdDZPG4pwnb-R8xFXhCtBBF0Se71DPE735BZyV6pxnS9LFUInQmFpaSY6zSv7pm8tv7QXGxPKAl-C3Sz1DSE1VJfKHBY8X5UwRYu0cTqFSvRSFWczfm58QiKPINyVRNsezH0IRvTMNowGGvcOMIC2yApbS_lbMkalnsss8p3rtAIanr0PFuXcHbuzCjR89Bl-wujloqvBCQCMYly-SMif-COwT83aiJ2MPEz_EWeHiGF4YIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e9d06f8f.mp4?token=Eaaqoc9H5jDqcDM-jW8iyPZWvXV-rfI30IuDMBbp0zb0I3di_OcKOSbDw6M7tIsGfSgzJUcrPXRYUl1vzWQoKBbz8Ry-QtAeyULiFnfdDZPG4pwnb-R8xFXhCtBBF0Se71DPE735BZyV6pxnS9LFUInQmFpaSY6zSv7pm8tv7QXGxPKAl-C3Sz1DSE1VJfKHBY8X5UwRYu0cTqFSvRSFWczfm58QiKPINyVRNsezH0IRvTMNowGGvcOMIC2yApbS_lbMkalnsss8p3rtAIanr0PFuXcHbuzCjR89Bl-wujloqvBCQCMYly-SMif-COwT83aiJ2MPEz_EWeHiGF4YIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به میانجی‌ها گفتیم آتش‌بس را قبول نمی‌کنیم، باید جنگ خاتمه یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682324" target="_blank">📅 20:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682323">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c79df0400.mp4?token=Mj2kPQtAYKLsB0xXyi1EVlTR9FpH2JV5wUt9YFKlisC9FfaIPJWYotmxm6ZcYfNA6-YCqhbON8dQ811RV1OLyrPtL4Dreh1HYUob8IeCGXQc-Mjx-QJEarV8pRBJ8G0uqdaEcQ5XnbeBmdd7B5tQ7PnPamkWYmg1A06jP5mF2jTKF_VLpPIEazZb2kBUrihzbxNKMCcgbPZPKmWOg2q6kS-mY4BIgpcMDPM-fehPHaAx6T7DxJkoM3xR0caDVXP-FpNMr9wozYU45q1ZlEV-kNFQUBvTQI3_Bu9ef24rN1Ar7kmYRjNPLU5az3vnGa0CniXvrvB5m2vcKojcqc4hzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c79df0400.mp4?token=Mj2kPQtAYKLsB0xXyi1EVlTR9FpH2JV5wUt9YFKlisC9FfaIPJWYotmxm6ZcYfNA6-YCqhbON8dQ811RV1OLyrPtL4Dreh1HYUob8IeCGXQc-Mjx-QJEarV8pRBJ8G0uqdaEcQ5XnbeBmdd7B5tQ7PnPamkWYmg1A06jP5mF2jTKF_VLpPIEazZb2kBUrihzbxNKMCcgbPZPKmWOg2q6kS-mY4BIgpcMDPM-fehPHaAx6T7DxJkoM3xR0caDVXP-FpNMr9wozYU45q1ZlEV-kNFQUBvTQI3_Bu9ef24rN1Ar7kmYRjNPLU5az3vnGa0CniXvrvB5m2vcKojcqc4hzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه درباره عملکرد دو ساله: رئیس‌جمهور با یک تماس تلفنی با الهام علی‌اف، فصل جدیدی در روابط ایران و آذربایجان رقم زد‌
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682323" target="_blank">📅 20:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682322">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d25c1842.mp4?token=nytIha7Iga4_NkyFaMd-b3lUOJ9LoIGG-nKwSPakEQbO0l3GSqB9lACpHamVB3G8L1ftQrtURcTf8bqesYQT0kctcJa_uhfZhmCY5vJc64MksvZJMBMy-83L_aMB-AnHTuO2gnHUGi8L7mr6ZQiklbwvzts7C9xEUsG7FFJW7Jnrcz0JgNw6e8lAGiKQzrAKIiLsJTBmwoJif-PS5PCz1J9usfkR2VqqzbqV-LQL5o1GLt3Ayt0bR0PrKKodXk8DPDdc3bPT1avNIYomURBY37aTwCV6mwdR3U0D2s-5ewKodedEMumKsqi0f2HsEZxjtqO3F7V6vxq7CPMpSGTdJpLYtjwUfGAydOqmUPYMJZuREErnG1APvOUww_JCxFTxxAkSjPK6k-IGkSJLtYVKggN4m__ZacHQDP-RY522YpAECCq3a54C3KR9HisR3k3mioV40l_Tu_WeiginlYYvAulSxlOhFpVp5sRYKUPH2ymgJeJiWv6X6p86ZPN9x4pc9h1kkjtiSovxxsjExzpDXODl6VrLGtPCNfwbgoNr828wA6gGVBCJCkQK5ct3lbyjxAGfek8V-wW3LxzHA-c9He4zsOal5AUPnyyzdCvLx9tKXxaj_BkAOuhMKgKGlryniXPZCeWqsSBFze9QcjPBdZQfGUcg8xtsPHkshtVdkH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d25c1842.mp4?token=nytIha7Iga4_NkyFaMd-b3lUOJ9LoIGG-nKwSPakEQbO0l3GSqB9lACpHamVB3G8L1ftQrtURcTf8bqesYQT0kctcJa_uhfZhmCY5vJc64MksvZJMBMy-83L_aMB-AnHTuO2gnHUGi8L7mr6ZQiklbwvzts7C9xEUsG7FFJW7Jnrcz0JgNw6e8lAGiKQzrAKIiLsJTBmwoJif-PS5PCz1J9usfkR2VqqzbqV-LQL5o1GLt3Ayt0bR0PrKKodXk8DPDdc3bPT1avNIYomURBY37aTwCV6mwdR3U0D2s-5ewKodedEMumKsqi0f2HsEZxjtqO3F7V6vxq7CPMpSGTdJpLYtjwUfGAydOqmUPYMJZuREErnG1APvOUww_JCxFTxxAkSjPK6k-IGkSJLtYVKggN4m__ZacHQDP-RY522YpAECCq3a54C3KR9HisR3k3mioV40l_Tu_WeiginlYYvAulSxlOhFpVp5sRYKUPH2ymgJeJiWv6X6p86ZPN9x4pc9h1kkjtiSovxxsjExzpDXODl6VrLGtPCNfwbgoNr828wA6gGVBCJCkQK5ct3lbyjxAGfek8V-wW3LxzHA-c9He4zsOal5AUPnyyzdCvLx9tKXxaj_BkAOuhMKgKGlryniXPZCeWqsSBFze9QcjPBdZQfGUcg8xtsPHkshtVdkH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاد، ما را از انقلاب و رهبرمون جدا نمی‌کنه؛ خداروشکر زندگی‌مون می‌چرخه و امیدواریم مشکلات اقتصادی هم برطرف بشه/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/682322" target="_blank">📅 20:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682321">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حقوق ۲۵ میلیونی با هزینه ۹۰ میلیونی | نبرد در ریاضتِ بقا | چند درصد مردم درآمد ۹۰ میلیونی دارند؟
🔹
محاسبات تازه درباره هزینه‌های زندگی خانوارهای کارگری نشان می‌دهد که سبد معیشت یک خانواده متوسط ۳.۳ نفره در پایان تیرماه به حدود ۹۰ میلیون تومان رسیده است؛ رقمی که فاصله آن با دستمزد رسمی کارگران، تصویری روشن از تشدید بحران معیشت در ایران ارائه می‌دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3238688</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/682321" target="_blank">📅 20:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682320">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e6cfe160.mp4?token=umbocC-fSAR9SHhPc02rmqrouxB_5kDwiMvlOXQ1kXMIPOkHAux3xoR_TV5fH9_VS1SWD_EGVxCAcAaD86oVIw7eZ7Ud2QXrN44OCRdxkh1ZGyEKMUWfcZgF4aWd8HFVUiCW_cxeNT98O811Tm2hwEQtnfMliMpYlF9q2QC1o7Y4c_dnFJfq04U3SHd22TTv0rTfmvWXs971ZE1mHWhdLqwzXTX4Qx0MvHP35jcNt79o6F8UhCmrGhPuKb5sZZq-9W3FBFGLly46i3kJzYtXp2BlrV6UINnTyJ91lnBdTCXhnjLOgMS9nJsA6s4qIWvT0zCCESQ-WJJthIll8piMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e6cfe160.mp4?token=umbocC-fSAR9SHhPc02rmqrouxB_5kDwiMvlOXQ1kXMIPOkHAux3xoR_TV5fH9_VS1SWD_EGVxCAcAaD86oVIw7eZ7Ud2QXrN44OCRdxkh1ZGyEKMUWfcZgF4aWd8HFVUiCW_cxeNT98O811Tm2hwEQtnfMliMpYlF9q2QC1o7Y4c_dnFJfq04U3SHd22TTv0rTfmvWXs971ZE1mHWhdLqwzXTX4Qx0MvHP35jcNt79o6F8UhCmrGhPuKb5sZZq-9W3FBFGLly46i3kJzYtXp2BlrV6UINnTyJ91lnBdTCXhnjLOgMS9nJsA6s4qIWvT0zCCESQ-WJJthIll8piMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه درباره عملکرد دو ساله: دیپلماسی استانی مکمل دیپلماسی همسایگی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/682320" target="_blank">📅 20:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682318">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a321fc3a.mp4?token=syeYUqFgvev3Ip9KhRWNVqxcemYO3XZHqrrsD6gXeoDslgVuEyr21CL8LidfcrSNjYX9GgeowVaZ5A1pi1-otuR4mMCWx2fMJMrd5C1-1XvvM0kIJ-gmO0cDMgd90b437VbKjHyEv3D33hHyhJq3HhLzZ-HqAPlk1vdLjP2Kd_OiLxSJfUNvw3EKrSYePRraPxASMRW4z1X57UkAaDFNjhfs5tFjg_p9m29ag9RtseJlrc9eUgoldBp2LnKkQWzT6qnaQcA0SG0sHegMLCaiYOl-v0h7bMSk8EJpRa54C0LQ9dlITKVDsX0Nj3CY3ootxr3Gzx-pec_adhd1plweYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a321fc3a.mp4?token=syeYUqFgvev3Ip9KhRWNVqxcemYO3XZHqrrsD6gXeoDslgVuEyr21CL8LidfcrSNjYX9GgeowVaZ5A1pi1-otuR4mMCWx2fMJMrd5C1-1XvvM0kIJ-gmO0cDMgd90b437VbKjHyEv3D33hHyhJq3HhLzZ-HqAPlk1vdLjP2Kd_OiLxSJfUNvw3EKrSYePRraPxASMRW4z1X57UkAaDFNjhfs5tFjg_p9m29ag9RtseJlrc9eUgoldBp2LnKkQWzT6qnaQcA0SG0sHegMLCaiYOl-v0h7bMSk8EJpRa54C0LQ9dlITKVDsX0Nj3CY3ootxr3Gzx-pec_adhd1plweYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتحاد و همبستگی رمز ایستادگیه، ما نسل قدیم شاید دیگه توان گذشته رو نداشته باشیم، اما جوانان امروز دارن پای کار می‌ایستن/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682318" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682317">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حمله مزدوران سعودی به مناطقی از استان تعز یمن
🔹
گزارش‌ها از استان تعز حاکی از آن است که عصر امروز، مزدوران وابسته به عربستان سعودی بخش‌هایی از این استان را هدف حملات موشکی قرار داده‌اند.
🔹
منطقه «الاکمه» در بخش «مقبنه» استان تعز، هدف چندین فروند موشک کاتیوشا قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682317" target="_blank">📅 20:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682314">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
یک جانباز ۵۰ درصد در گفتگو با خبرنگار خبرفوری از آرزویش برای شفاعت در آخرت گفت و در ادامه، از مسئولان خواست بیشتر صدای مردم را بشنوند/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/682314" target="_blank">📅 20:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682313">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اخبار تائید نشده از شلیک چند فروند موشک از سوی نیروهای مسلح یمن خبر می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682313" target="_blank">📅 20:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682312">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
گلف‌نیوز: ایران دو ملوان مصری را آزاد کرد
ادعای گلف‌نیوز:
🔹
دو ملوان مصری که از ماه ژانویه در بندرعباس و در داخل کشتی «ریم البحار» بازداشت شده بودند، آزاد و مجوز بازگشت به کشورشان را دریافت کرده‌اند.
🔹
رئیس دفتر حفاظت منافع مصر در تهران، پیش از عزیمت ملوانان از ایران به قاهره، شخصاً با آنها ملاقات کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682312" target="_blank">📅 20:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1d447e4a.mp4?token=l6gyeA3nlATVMeoHyx8F_D_t7kEAtbZF4bXOmEm5GLal4Sq_LhghFzdTN2dYMAd1Gi0jkwWiY4lg4LjQzdOVq0D2FvQM7lwPfVCzC4W00utqTT9BF1BiLxY1A5tnCGZSBzmm24ihRAOtK2dG2kdAJDZJWANQAOKT8zK2DUtkhYk4K2HUOLUZTGg7WJQGvSimt_E7zKzwbKURnDL_46z-V-Bj2ni0IODVxlbr-OabPDGIIM68Ic0Jfkz9kilkRAwhhJRyXitxTeiQfmaD6UCDTujQSlYIcu1IUvPE_qiVGgKVgvMuIFIgL5QgNCbjOZBQ3qSJVOUwhu2uYXTX3ysXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1d447e4a.mp4?token=l6gyeA3nlATVMeoHyx8F_D_t7kEAtbZF4bXOmEm5GLal4Sq_LhghFzdTN2dYMAd1Gi0jkwWiY4lg4LjQzdOVq0D2FvQM7lwPfVCzC4W00utqTT9BF1BiLxY1A5tnCGZSBzmm24ihRAOtK2dG2kdAJDZJWANQAOKT8zK2DUtkhYk4K2HUOLUZTGg7WJQGvSimt_E7zKzwbKURnDL_46z-V-Bj2ni0IODVxlbr-OabPDGIIM68Ic0Jfkz9kilkRAwhhJRyXitxTeiQfmaD6UCDTujQSlYIcu1IUvPE_qiVGgKVgvMuIFIgL5QgNCbjOZBQ3qSJVOUwhu2uYXTX3ysXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه درباره عملکرد دو ساله: دیپلماسی استانی مکمل دیپلماسی همسایگی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682311" target="_blank">📅 20:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازنشسته‌ها و حق‌التدریس‌ها کمبود معلم امسال را جبران می‌کنند
مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در
#گفتگو
با خبرفوری:
🔹
امسال کسری نیروی انسانی آموزش‌وپرورش با استفاده از ظرفیت فارغ‌التحصیلان دانشگاه فرهنگیان و شهید رجایی، حق‌التدریس شاغلان، بازنشستگان و پیشکسوتان و همچنین سربازمعلمان جبران شده است.
🔹
برنامه‌ریزی برای سال تحصیلی جدید به‌ گونه‌ای انجام شده که مهر امسال، کلاس‌ها با حضور معلم در تمام پایه‌ها آغاز شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682310" target="_blank">📅 20:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029e3f4ae2.mp4?token=lWbahzFeob--xH5bCdYxOJZ_KdVeEghgEkzy8rDRcyXYNACsdzHTxeCSm6yKo9Tt5WITaXdSQc8pgPlBQRGUSOZGW8OSW5ilPYpYhaN-UXd2v7v3JjFc6zW2wyDzkxrdSraL1s6t2tR4t-Q1fhIzZ8ZJR7yQojuNtq8nOg122etu3A-zonO5kj5eCJHQeZAHgAnEXSLxV5KBJPQANYfmsEa4s2t2p-Wu80wKqr5s-iZJYA5A7xRAWj0kdKNfPaafrGZfQMWjwVAgOVGdpiakgQd927ThTqwUHwaxvucd_4U7wGK-VwMWJq_ycRdFTKCg6n1oncgyBL1TslJqcDylQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029e3f4ae2.mp4?token=lWbahzFeob--xH5bCdYxOJZ_KdVeEghgEkzy8rDRcyXYNACsdzHTxeCSm6yKo9Tt5WITaXdSQc8pgPlBQRGUSOZGW8OSW5ilPYpYhaN-UXd2v7v3JjFc6zW2wyDzkxrdSraL1s6t2tR4t-Q1fhIzZ8ZJR7yQojuNtq8nOg122etu3A-zonO5kj5eCJHQeZAHgAnEXSLxV5KBJPQANYfmsEa4s2t2p-Wu80wKqr5s-iZJYA5A7xRAWj0kdKNfPaafrGZfQMWjwVAgOVGdpiakgQd927ThTqwUHwaxvucd_4U7wGK-VwMWJq_ycRdFTKCg6n1oncgyBL1TslJqcDylQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلامت موهایت را با یک لیوان آب بسنج! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/682309" target="_blank">📅 20:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682308">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای وزارت دفاع امارات: دو موشک بالستیک از ایران شلیک شده را شناسایی کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682308" target="_blank">📅 20:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc0f1428f.mp4?token=KIAUQ767CYQoqacvWKGXWSZghxyYRcwWFZ7Cg9DgahuBBZyqeW-ye61RNOGxKUvOPFHWv23U2WGq_wPwFIOT4HtW0zbNp9zsmXYNFOoFmpKhov1QFxXCKwLX4skd1YSppgqMOotcry8eGteMlW6zVWSc8LukZisL-w8wxigMzB-kbhsCqs128PElghqN7ZynwRmPIA8BTYRXnWOBLVOmZFiq8oYEDcqn6i_vOGg_47Uqr8JhxpccV8FDrgKR9fpr-foDT8RBg3qgOhyCa1-ar_riNY1RpnZVKTfyDhUKKVD8Gi2pMtLyGH3kw0W6_ONb2LBTDmhnTmDb0OGllp6B0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc0f1428f.mp4?token=KIAUQ767CYQoqacvWKGXWSZghxyYRcwWFZ7Cg9DgahuBBZyqeW-ye61RNOGxKUvOPFHWv23U2WGq_wPwFIOT4HtW0zbNp9zsmXYNFOoFmpKhov1QFxXCKwLX4skd1YSppgqMOotcry8eGteMlW6zVWSc8LukZisL-w8wxigMzB-kbhsCqs128PElghqN7ZynwRmPIA8BTYRXnWOBLVOmZFiq8oYEDcqn6i_vOGg_47Uqr8JhxpccV8FDrgKR9fpr-foDT8RBg3qgOhyCa1-ar_riNY1RpnZVKTfyDhUKKVD8Gi2pMtLyGH3kw0W6_ONb2LBTDmhnTmDb0OGllp6B0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: بودجه داریم اما در اولویت‌بندی دقت نمی‌کنیم  رئیس مجلس در جلسه علنی امروز مجلس:
🔹
دو موضوع کالابرگ و بحث نیروهای مسلح، موضوعات مهم و فوری ماست و باید به نحوی پیگیری کنیم که خدشه به آن وارد نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/682307" target="_blank">📅 20:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeTvtu-kHSBzGEveBcIMQaJtTLk8We5S-eS12bLHrGRuCDMEGZOs04ssLlo8opf9zl4huHFHrv72Hb7uDMh4WPMZCC9MwpAbA260ja6HZzDK6qo_vISsqbGL_uV3K7YxHOPNxFhRTuz93Au8HlJ9CPzf01p4MYeWujZ5hEOcBHWZ-9pqDWGfpVOULkwIfzoW-2Hd0WSxT7fmQi-WixMxnNdgF_KamMBz0bjM0Y41RG9n_uhRi3u-Z0XOd2vnWvXjMYkKFq3yrmcpMTuBAJn5BvE3peFbOknk3ho15Uy0DTrnZWoY5J5c8Lk112W5ZuwquCh-2GckqkfAQ-8_LoBn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولوریتا(
®️
Velorita) چه تاثیری روی کبد چرب و قند خون داره؟
داروی
سماگلوتاید (Semaglutide)
تولید
کشور کانادا
با نام تجاری ولوریتا تولید شد.
ولوریتا می‌تونه علاوه بر کمک به
کنترل قند خون
، در روند
بهبود کبد چرب
هم نقش داشته باشه. این دارو با اثر روی اشتها و کاهش دریافت غذا، می‌تونه به کاهش وزن کمک کنه.
🟡
مصرف این دارو باید زیر نظر پزشک انجام شود. از مصرف خودسرانه پرهیز کنید.
@allaboutobesity</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/682305" target="_blank">📅 20:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d1b7f113.mp4?token=WsMtQ69LanFDaO7xYlVNpsrSYumI45Z6WSTC_aOPjCmuoaq-pscSgRP1ntvaa-Zn5lN9VitZ8piSfcjoUk_Wjycf1RGz5lcRIIa6aAlprZAUct8eIremp9K_zSUjCbZ3Lu7BKQbj8807zohjeYeB1IAotXXe0ruLl4IuKSUpm1XRm1P6gybxegssxT8uIVzdQM-D1oKXwF0YB5-AMr9iHMRZ2fgCtzTpDtCtodnD-uiXs_lyZHtObGj7lRJm4OKOZIvl_ppzsY2K4cY-o5J4iW6UFmomv5Ox7mnGOuHW6WvgF8yBCx91nzPcUK0uZVhgA_ppptF6QrUH_rL-fy_XPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d1b7f113.mp4?token=WsMtQ69LanFDaO7xYlVNpsrSYumI45Z6WSTC_aOPjCmuoaq-pscSgRP1ntvaa-Zn5lN9VitZ8piSfcjoUk_Wjycf1RGz5lcRIIa6aAlprZAUct8eIremp9K_zSUjCbZ3Lu7BKQbj8807zohjeYeB1IAotXXe0ruLl4IuKSUpm1XRm1P6gybxegssxT8uIVzdQM-D1oKXwF0YB5-AMr9iHMRZ2fgCtzTpDtCtodnD-uiXs_lyZHtObGj7lRJm4OKOZIvl_ppzsY2K4cY-o5J4iW6UFmomv5Ox7mnGOuHW6WvgF8yBCx91nzPcUK0uZVhgA_ppptF6QrUH_rL-fy_XPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اطلاعات خوب و دقیقی نسبت به تراستی‌ها داریم و باید در این موضوع نظم حاکم کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682304" target="_blank">📅 20:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d6cc303f.mp4?token=toiFjGEGVhWehcpDQRKyU1DD-Pu7ev5h1LIsL6OzdSHIn59hDZ_Q_muqa-kTo54-Y4IxGaXTAWG9RCr4V8yIlalRgZOMmMA8e_OM2FEyRmZynxNFFRWgEtTN_wJCf_-R2mTzWnyqtmGN447JBYB21VkRAFO1K6BEfvXUxhbJrm1SQXQFW35f2y1yXaUGycANEfddu9F3Dud0HBsQ7FkQYqa678uG07zl9_bdBQzMPfMr2pOIgDM9mExqy4mBDsJArPn05nKs5M1AwVwv09GYCcwxP9N2VD6reV_Knc0DjIhX2ebt6Xje_V4m0Dn9iNQHln834sbQzINhyp9Y4hbLaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d6cc303f.mp4?token=toiFjGEGVhWehcpDQRKyU1DD-Pu7ev5h1LIsL6OzdSHIn59hDZ_Q_muqa-kTo54-Y4IxGaXTAWG9RCr4V8yIlalRgZOMmMA8e_OM2FEyRmZynxNFFRWgEtTN_wJCf_-R2mTzWnyqtmGN447JBYB21VkRAFO1K6BEfvXUxhbJrm1SQXQFW35f2y1yXaUGycANEfddu9F3Dud0HBsQ7FkQYqa678uG07zl9_bdBQzMPfMr2pOIgDM9mExqy4mBDsJArPn05nKs5M1AwVwv09GYCcwxP9N2VD6reV_Knc0DjIhX2ebt6Xje_V4m0Dn9iNQHln834sbQzINhyp9Y4hbLaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ۲ موضوع کالابرگ و بحث نیروهای مسلح، موضوعات مهم و فوری ماست و باید به نحوی پیگیری کنیم که خدشه به آن‌ها وارد نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/682303" target="_blank">📅 19:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024c1f2502.mp4?token=rtSojlAiGipo_STx-H86RcdU1fbWVq3FusdBWasKA7NbhotwTQW_s7veQheVuk-WNFqrdVJ6Nqb-VkETlfpmQcW4eBnbPW6FeYnVJNTA8Tali4SsCZs2hjy2rHjN45j8nMK5CmDxt0Afb4TtepLVqr-DLCfwrTYQmO53NZsT44Kpt4qZnf4pgxcgRyPIQXflZPcHglPCCxNAeYOfYqwn6BMityVDg-hEjc9c7bBv-S_tWG-u1QTW2f1DFKkM9gtsDuhGnfPtSUGvI6KF-V11jQOZlsCgTFnR7hQxNVYv5rSCLy4TEDHphLWRhKe0vFJopmr6jvb_2ouXDCutMWfJ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024c1f2502.mp4?token=rtSojlAiGipo_STx-H86RcdU1fbWVq3FusdBWasKA7NbhotwTQW_s7veQheVuk-WNFqrdVJ6Nqb-VkETlfpmQcW4eBnbPW6FeYnVJNTA8Tali4SsCZs2hjy2rHjN45j8nMK5CmDxt0Afb4TtepLVqr-DLCfwrTYQmO53NZsT44Kpt4qZnf4pgxcgRyPIQXflZPcHglPCCxNAeYOfYqwn6BMityVDg-hEjc9c7bBv-S_tWG-u1QTW2f1DFKkM9gtsDuhGnfPtSUGvI6KF-V11jQOZlsCgTFnR7hQxNVYv5rSCLy4TEDHphLWRhKe0vFJopmr6jvb_2ouXDCutMWfJ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: قول می‌دهیم به اجرای کالابرگ خدشه وارد نشود
🔹
در نیمۀ دوم سال هم باید به افرادی که بیشتر نیاز دارند، با اولویت‌بندی پلکانی بيشتر کمک کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/682302" target="_blank">📅 19:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c30e01754.mp4?token=u-dIhcYrx5t3v8cJwLNtLrOQXxhEr9frcXwHyK5kh9qqLoqEyoB7iTS3fOn1-ETghBCzs1VJ6rcfP_cW_8rAR5VRPEI34jbuhC3o4G0qK6doL4JgWce_Q7WpbaR-pcq96kdTNgAyoxsvNISlKzswHSjSgpBGjVLWXnyzCsP7dDuKnqxYWwDQuhgTE2_CxIc-I44XMHtc9mpXu9YqlAvhKXvIppPXLhUSeRCw3d6ueqWfqYtesel9NFmPjLaF5JH_lZ8z0qfaRS1tXH0CIukG1FQ8M0-Nglwi6dmbDG2fgIKpa2RMIUBmLs2LZbdCyECLdF0y9SINVef0kptJdl4IeYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c30e01754.mp4?token=u-dIhcYrx5t3v8cJwLNtLrOQXxhEr9frcXwHyK5kh9qqLoqEyoB7iTS3fOn1-ETghBCzs1VJ6rcfP_cW_8rAR5VRPEI34jbuhC3o4G0qK6doL4JgWce_Q7WpbaR-pcq96kdTNgAyoxsvNISlKzswHSjSgpBGjVLWXnyzCsP7dDuKnqxYWwDQuhgTE2_CxIc-I44XMHtc9mpXu9YqlAvhKXvIppPXLhUSeRCw3d6ueqWfqYtesel9NFmPjLaF5JH_lZ8z0qfaRS1tXH0CIukG1FQ8M0-Nglwi6dmbDG2fgIKpa2RMIUBmLs2LZbdCyECLdF0y9SINVef0kptJdl4IeYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما اینجا هستیم که بگیم تنهاش نمی‌ذاریم؛ در رکاب رهبری هستیم و تا آخر ایستاده‌ایم. این ملت و مردم ایران همیشه سرافراز و سربلند می‌مونن
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682301" target="_blank">📅 19:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc70156c4f.mp4?token=BLLajwNbOVWRut1CPXEpVPiH-SCwIpWbvdUIke-VZyR7pygMKHn1pN1e08ULskyeEeD1hF75mnYiXCNqDiWJxDlh4QJfWXWvD5m8oOVYh8zHR4Cy5GxbTZewp62vh0xvJ2fnHtV1coXUM0IA3XkI3AN4j2PL-5dwaT64ORi49ruzPbywQhs3pFcp0zB6IfZ0rA-YlJxu5G9iZn3e2tpBB6odpAc0et3wAprCkRthTRBk4speP347X_cK8qqA_q4hoYUYkYM43_u2VRIsiqIC5Xb75OmRNjwtG7KAL8UCppLqT5PdvkxKghTcd32r7zcYj8_4iQHPnENz4KZGEe7Byw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc70156c4f.mp4?token=BLLajwNbOVWRut1CPXEpVPiH-SCwIpWbvdUIke-VZyR7pygMKHn1pN1e08ULskyeEeD1hF75mnYiXCNqDiWJxDlh4QJfWXWvD5m8oOVYh8zHR4Cy5GxbTZewp62vh0xvJ2fnHtV1coXUM0IA3XkI3AN4j2PL-5dwaT64ORi49ruzPbywQhs3pFcp0zB6IfZ0rA-YlJxu5G9iZn3e2tpBB6odpAc0et3wAprCkRthTRBk4speP347X_cK8qqA_q4hoYUYkYM43_u2VRIsiqIC5Xb75OmRNjwtG7KAL8UCppLqT5PdvkxKghTcd32r7zcYj8_4iQHPnENz4KZGEe7Byw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: قول می‌دهیم به اجرای کالابرگ خدشه وارد نشود
🔹
در نیمۀ دوم سال هم باید به افرادی که بیشتر نیاز دارند، با اولویت‌بندی پلکانی بيشتر کمک کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682300" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
جنگ ایران چرا به نفع کشورهای خلیج فارس نیست؟
🔹
جنگ ایران اگرچه می‌تواند قیمت نفت را بالا ببرد، اما همزمان هزینه تأمین مالی کشورهای عربی خلیج فارس را افزایش داده است.
🔹
پس از آغاز جنگ، صرف ریسک اوراق بدهی این کشورها از حدود ۲.۶ درصد به بیش از ۴ درصد رسیده؛ یعنی دولت‌هایی مانند عربستان برای استقراض باید سود بیشتری به سرمایه‌گذاران بپردازند.
🔹
برای اقتصادهایی که میلیاردها دلار پروژه توسعه‌ای را با انتشار اوراق تأمین مالی می‌کنند، این افزایش هزینه سنگین است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682297" target="_blank">📅 19:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d4fae581.mp4?token=hsqSdObiqeqSJH4H-749TbEqYcUbIvbGwvhfukjiIF3jxprf7JjyFJcrgEXzJvzxdP5qF_j4XF44npBNywwXB7OKCvSqanjrYKriVuRLjVK0mamjKsYiBt6nyoQbRCGEnke8IegLKevkWvFekfK7gjvtuxk_9zLPJKyHaEfH1LJ3f9x7BI4MlymMPNvMF-rLKxCPnRVzk-gIaXDjyA1NAAza5LBnsEEncjGsH1mbUAxxiKzgqjudh7Mj5mAATX7t-KnECEqWGR4DKTkmjWAN6I7lmg3_TToIzLRHwvW9sMr9AEea1ZOhQkqi3cAPiEPPkjrInO8h8n2BueszGDwIVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d4fae581.mp4?token=hsqSdObiqeqSJH4H-749TbEqYcUbIvbGwvhfukjiIF3jxprf7JjyFJcrgEXzJvzxdP5qF_j4XF44npBNywwXB7OKCvSqanjrYKriVuRLjVK0mamjKsYiBt6nyoQbRCGEnke8IegLKevkWvFekfK7gjvtuxk_9zLPJKyHaEfH1LJ3f9x7BI4MlymMPNvMF-rLKxCPnRVzk-gIaXDjyA1NAAza5LBnsEEncjGsH1mbUAxxiKzgqjudh7Mj5mAATX7t-KnECEqWGR4DKTkmjWAN6I7lmg3_TToIzLRHwvW9sMr9AEea1ZOhQkqi3cAPiEPPkjrInO8h8n2BueszGDwIVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری در بین هواداران تیم استقلال و نساجی
/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682293" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a54317960a.mp4?token=WsVDkhOmcq0Dk6ooJhOjA9NIuB0Ghjdg2DNZ9Ic_TLL8I0rZSS_lwgl3D2i3Hu3dCunsp2av7mE5dw1rZ0rbGEOkbWkZsQ2SrsXknFnx9MIeicCL-Kq9OimUekluFuFDmi0VRPIZ4SZT84QTuxPImcd9z42i0_D3EhQW5ivO1LVSQlSjzuWHQIQPUxYlsh_KasEQ936rvAGRW7z5YMlF4l4k9ZJtC6DhggbnPeqfAeFPPjjdl1tqzBtx_TsAvpZ-8P-LrzXh3ZjDWVEUqiQLfvQjwE-YOHIIrY1zsAFUeX-BJB-2zeYxqgJDE6Za0oPaC9PN_9_sNz7jUo5wdYUMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a54317960a.mp4?token=WsVDkhOmcq0Dk6ooJhOjA9NIuB0Ghjdg2DNZ9Ic_TLL8I0rZSS_lwgl3D2i3Hu3dCunsp2av7mE5dw1rZ0rbGEOkbWkZsQ2SrsXknFnx9MIeicCL-Kq9OimUekluFuFDmi0VRPIZ4SZT84QTuxPImcd9z42i0_D3EhQW5ivO1LVSQlSjzuWHQIQPUxYlsh_KasEQ936rvAGRW7z5YMlF4l4k9ZJtC6DhggbnPeqfAeFPPjjdl1tqzBtx_TsAvpZ-8P-LrzXh3ZjDWVEUqiQLfvQjwE-YOHIIrY1zsAFUeX-BJB-2zeYxqgJDE6Za0oPaC9PN_9_sNz7jUo5wdYUMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف مردم بعد از ۱۹۵ روز دوری رهبر شهید: اگر الان بخوام باهاش حرف بزنم، می‌گم خیالت راحت دست پسرتون بالای سرمونه. ما هنوز اینجاییم، هنوز پای کاریم و راهی که گفتید رو فراموش نکردیم/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682292" target="_blank">📅 19:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU_nt3L8i7vl5-NyLp0bvpsp-88_BLut3DN8UNmLnqOfKhxpTlOSfyploauloGNIflp_4x0fGoov0uSJpFkWETShKfGgYr-c2Sd-tiW6iCvwUSaOzQANjQCqvh3LuS7E8Oz59uW6suAdNUgtno2u6RjwT4UmHWtRiS1KjtM9iU6dL1WZoh6-Y_M2uyw5qNSBg6hAK54gWcHp4FbxeWA6wi58QB3NzxGVdk3b4CunXG8mPx7Fo6A16MWG_xNVl7EvtEfLoXQGcepf2U69EU1pAth2hJtFPZ5EmsFYuMUistbwM0ru070kvK6ajDXtLUGAHGEb5iGR2szJqF9il8SRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقات نشان داد:
آمپول لاغری علاوه بر کاهش وزن، چربی پنهان اطراف اندام‌های داخلی را هم کم می‌کند
چربی احشایی
چربی‌ای است که در عمق شکم و اطراف اندام‌های داخلی مثل کبد و روده جمع می‌شود و خطر ابتلا به دیابت نوع۲ و بیماری‌های قلبی‌عروقی را بالا می‌برد.
در یک مطالعه ۵۲ هفته‌ای،
آمپول لاغری حاوی تیرزپاتاید(مثل مونجارو در آمریکا-اروپا و زیکورپا در ایران)
توانست در افراد دارای اضافه وزن و مبتلا به دیابت نوع۲، حجم چربی احشایی شکم را
تا ۱.۶۵ لیتر
کاهش دهد. چربی زیرپوستی شکم و چربی کبد هم کاهش پیدا کرد.
نمونه تغییرات یک نفر که در این مطالعه حضور داشت در تصویر آمده
👆
منبع:
SURPASS-3 MRI,
The Lancet Diabetes&Endocrinology
, 2022</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682291" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWme5YGsZK0HHjD3KdV-m_n-JK1Gq3-6dj6uRsS1NqwoGYXe29sOf7vat3un5w2CWlKtQQSG0nWmzNn169CEKF7gJnBCr1AzVh62kh1Us-jUbBqgulnJ7LFXrepTlUA2g1-7fS9lV1CxdQJRv8aba15KZk3x6nhHrrz4wMcwIbH6E39Rpos8mlecLd_auqtmuac-daGT6w6o8Us35iySMy8QlZ93gGVtUiDeV0LS2KrmlYHopcRDwVsb3WEEHXiymTOu1ireXVnaLZRmp0c4c4P_i3eKL7_BtG3BTGhO3MxSSFqEWrtAEt-H-9SQVwoeYBMQGbIxdInPlqGYlb2GKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار جنگ بر ذخایر پدافندی آمریکا
🔹
آمریکا از آغاز جنگ با ایران تا کنون ۲۰۰ فروند از رهگیرهای THAAD خود را مصرف کرده، درحالی‌که کل مصرف آن در سال ۲۰۲۵، ۱۵۰ فروند بوده است.
🔹
رهگیرهای دریایی نیز با سرعت بیشتری مصرف شدند؛ شلیک ۱۳۰ فروند SM-3 در جنگ، در برابر ۸۰ فروندی که در سال ۲۰۲۵ و ۳۹ فروندی که در سال ۲۰۲۴ مصرف شده، نشان‌دهنده افزایش قابل‌توجه مصرف است.
🔹
این افزایش، ذخایر موشکی آمریکا را تحت فشار گذاشته و بازسازی آن را به یک چالش بلندمدت تبدیل کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/682290" target="_blank">📅 19:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFUHysvfZacm7Hw3Fp7GkAnvqloarJcl8UvuthPhf3HeEleJEYx5XWok_M1p-LZ8xp613cMwki9-WmK778laKxpB3rByh1xi6j_hFwqe1vYU05eTJBhqzzZNwAyE5toxCeCBBZg6nfE70_m2RlQ5cx1JuBwWfrFOmaq5ZvG0DOtypBAzmdzywPyyARibl7amK66trC6K3DT9egWdHJ6NuRfWFVDsaWFnTm4r_Qx7mqp2co-blNeEiCNkNXdZUi3wLRC_iKxXDgyNxWKwZUkk85QgOkLALW3Lz9I6KwnlD05mlXrKZQl2BaWr6emOk_oXKvptdNyu9YsD0f6VeQG_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تصویری از آرزویی که گراهام با خود به گور برد را منتشر کرد
ترامپ:
🔹
لیندسی همین چند هفته پیش داشت خوش می‌گذراند! کلاه را ببینید!
🔹
اشاره ترامپ به کلاه گراهام است که بر روی آن نوشته «ایران را دوباره با عظمت کنیم»، شعاری که گروه‌های برانداز و تجزیه‌طلب در آغاز تجاوز آمریکا و رژیم صهیونیستی به ایران زیاد به کار می‌بردند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/682289" target="_blank">📅 19:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای رسانه اوکراینی:‌‌‌ روسیه برای بازسازی زرادخانه نظامی، مواد منفجره به ایران می‌فرستد
رسانهNV اوکراین:
🔹
با استناد به سندی از یک دولت اروپایی، روسیه تامین مواد منفجره و مهمات برای ایران را آغاز کرده است تا به تهران در بازسازی زرادخانه موشکی و پهپادی خود پس از حملات آمریکا و اسرائیل کمک کند.
🔹
بر اساس این سند ادعایی، مسکو به طور مشخص مواد منفجره، مهمات و قطعات پهپاد را از طریق دریای خزر برای تهران ارسال می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/682288" target="_blank">📅 19:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682284">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887752b933.mp4?token=V091Loba9Vq4UPZ2Mq_mKbzpe5y2hmwrA1EKhRsZOHvDXh5VtnVxnJdLeyMeOniOk7tDISoTpPVR533XmgHXtB5JtsxoXaRrepNGNvRKw6yOtPa_cuYXOawdb44nD79UNRSpOyfrkmjaK3H0-Z5l7tIuK7autBrPE5AaOfqcGkm1x5jkqx79TyQy7oQ9EcIk7B48A8ZPIYIBX-orUnwr3ncrlr48oJtkPHWzO2cLXnf0DyUplr4-C9gU6GTKFvzGXeaov7kttQRLWXXeZNxt_e3s8rkFtqtVwfNAxkFq9izpn8_c17e8cW3rZGYjPjujr_F9Byqbd31WLkNAJDtxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887752b933.mp4?token=V091Loba9Vq4UPZ2Mq_mKbzpe5y2hmwrA1EKhRsZOHvDXh5VtnVxnJdLeyMeOniOk7tDISoTpPVR533XmgHXtB5JtsxoXaRrepNGNvRKw6yOtPa_cuYXOawdb44nD79UNRSpOyfrkmjaK3H0-Z5l7tIuK7autBrPE5AaOfqcGkm1x5jkqx79TyQy7oQ9EcIk7B48A8ZPIYIBX-orUnwr3ncrlr48oJtkPHWzO2cLXnf0DyUplr4-C9gU6GTKFvzGXeaov7kttQRLWXXeZNxt_e3s8rkFtqtVwfNAxkFq9izpn8_c17e8cW3rZGYjPjujr_F9Byqbd31WLkNAJDtxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید و ضررهای انواع مواد قندی از زبون خودشون
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682284" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITEQbkBNvpcU4Q_Cd78q2tlAPOR4YoNGrARaLbgLCHMtJc4Qj5PXMdca9UHBFzccnYiZGmj8wVGvLmVt9aMVZY4hB4D5CMGy_HSDN6hNHolJeOq7HZ80Lrt6muIikZ0pSVp3ta9Z_TgrwO8tJdYnjstGF-m5Rc7iEovu7xAHevSCvK9gw3T6pisfVKoY6BMczMGuTgw84waPPVs-zWDlVNwut2VvpCEuRSFoYe7QQ-RA5_6GaPh4-lT3XZC7lratJYPAIt0MG34EYhG7gpvuIObwBp1YMFDDFuSmydTCG635qKhzCb4oMW6hRnmkjA8vbyYgg-Sz2leREk643vavnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682283" target="_blank">📅 19:05 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
