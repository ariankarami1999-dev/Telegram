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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6BhsAGpfgAihC3zlGLgi0Hex_h9Sej9D6fk4x0fwNTjH4Y25AHskT4CkW73qc88QUZ3i2ubwIffXSCU1xQNDQ5ZNK0LZterWwdTaE_YigGPIs5Y_3FBL4E4ZxPkv4Z7Bt1xh486sWXGIu2qBrauu1gFunhtBanBbJprB9hbxtd-00kOGG0vx3SstS3BAoj-fHTYyefpsvTaQFuewQQbqh1p36_BB95OtN9hvH-0S2AbiTNLXmNXSWyyzqadnZlkWvMAoGtozTKFj3qNc4nIskaQXKmhIcO7l2qQ8EKj6fARrAHltXZDvAZQ-7lPayzQkhJPQ2nLreegZ5mP_pfI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع و مستقیم به
وینکوبت
📌
دیگه لازم نیست بین لینک‌های مختلف بگردی یا وقتت تلف بشه.
📌
فقط با یک ورود ساده به ربات رسمی، مستقیم وارد سایت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
ورود سریع و بدون معطلی
⚡️
بدون لینک‌های اضافی و گیج‌کننده
⚡️
دسترسی مستقیم از داخل تلگرام
😀
همه چیز برای راحتی کاربران داخل ربات فراهم و قرار داده شده.
🔵
برای تحلیل‌ها و اخبار سایت وارد کانال سایت شوید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 170 · <a href="https://t.me/SorkhTimes/131877" target="_blank">📅 02:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=dUomXgw9H63AA16yKqDZhjAUAOjyoQELGsT-iVpwHyY36oeQpBqj8FG-1tafT1V_zWfmV9PDK0XUkjSjw_z2n182hrj7nGR5bp3ixiMjjXGE6lW1d1gP96DXqz-pms8uyCKyhliEL1u3exhAXneaWYfZv-d9YGJOf8TLWxQhfszWdW7RqjXdLhTisU1Vdr3CXg1lp1YqlZ6iqf7_bpcWYkBzb0PuNNR87rzvOgkerC-WKodP9bQgant7LYxpntO3its9RDgOjzhEqHR1S1M2YH0SOBS7GQ7UCTpIioJjmt2qT6bLNfu5MQXgIIGpGntSkQb6dIO5RqFRlJEHhepXBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=dUomXgw9H63AA16yKqDZhjAUAOjyoQELGsT-iVpwHyY36oeQpBqj8FG-1tafT1V_zWfmV9PDK0XUkjSjw_z2n182hrj7nGR5bp3ixiMjjXGE6lW1d1gP96DXqz-pms8uyCKyhliEL1u3exhAXneaWYfZv-d9YGJOf8TLWxQhfszWdW7RqjXdLhTisU1Vdr3CXg1lp1YqlZ6iqf7_bpcWYkBzb0PuNNR87rzvOgkerC-WKodP9bQgant7LYxpntO3its9RDgOjzhEqHR1S1M2YH0SOBS7GQ7UCTpIioJjmt2qT6bLNfu5MQXgIIGpGntSkQb6dIO5RqFRlJEHhepXBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 400 · <a href="https://t.me/SorkhTimes/131876" target="_blank">📅 01:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 522 · <a href="https://t.me/SorkhTimes/131875" target="_blank">📅 01:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 520 · <a href="https://t.me/SorkhTimes/131874" target="_blank">📅 01:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131873">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=I0vd-y7pTYTox656F-1Z4sVKS0XTjaAQ3Nhu9WUR0dutgAswJ_dvvWK0AGLGsSteiPH9LVw2S3l7KXHudChb6g5kNZfKwzefz83WpC73B77pi5Bnr_0g1wixoY6Q4PqYmHSqlqWJMQlo8CfepSKgzPEjuyJ0WPso6aAQXGy7yZ8EBRXaZJQy1RgXSfT1NR0FVzQ5EIGhDj4rgfvYr7kazDf8q1ie1g0GMHc1EUoRPlCC6xelSchQmJf0M12jE0P8EkAkyOnyi3tVvbuyHFrEygnMQM4ORO6nw01B_IsMnN6kGNUK0kr8wFMM_3uKUuDPJ0U-GQ3erjJ3ZvmZgHCVUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=I0vd-y7pTYTox656F-1Z4sVKS0XTjaAQ3Nhu9WUR0dutgAswJ_dvvWK0AGLGsSteiPH9LVw2S3l7KXHudChb6g5kNZfKwzefz83WpC73B77pi5Bnr_0g1wixoY6Q4PqYmHSqlqWJMQlo8CfepSKgzPEjuyJ0WPso6aAQXGy7yZ8EBRXaZJQy1RgXSfT1NR0FVzQ5EIGhDj4rgfvYr7kazDf8q1ie1g0GMHc1EUoRPlCC6xelSchQmJf0M12jE0P8EkAkyOnyi3tVvbuyHFrEygnMQM4ORO6nw01B_IsMnN6kGNUK0kr8wFMM_3uKUuDPJ0U-GQ3erjJ3ZvmZgHCVUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 503 · <a href="https://t.me/SorkhTimes/131873" target="_blank">📅 01:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131872">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=jsh2B6r4d86D6_j3UZCink14N6SbDWTigUcR0-6wL_hB8XU60CLWM3sDjB1vEBHD--nVXYMJysCgI0AR7tLbgRMgi4E00PIlcDxL3jLlXba2nQZV-TkcdW5_oKMkdJF_fW4wpy7o1dIFotCQOR4ZHhL02uMGl_fBvGKJYcta5cWVmR5AhCdfx0cLLM8oM__Xi0Z7iUAOd_a5SrW8Yusz64K7YL4y-cAUz2Vl_ofx7ty1j4vcRhZMdmxPJblwISHBixpqsyeVN9TPAd5bTHRUZIzLr1imweiz6gdMkbwBlbBCSXOXfEVsHlCPWRwyRo2soLdHF6_GQ7ZFvz98sf4Fbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=jsh2B6r4d86D6_j3UZCink14N6SbDWTigUcR0-6wL_hB8XU60CLWM3sDjB1vEBHD--nVXYMJysCgI0AR7tLbgRMgi4E00PIlcDxL3jLlXba2nQZV-TkcdW5_oKMkdJF_fW4wpy7o1dIFotCQOR4ZHhL02uMGl_fBvGKJYcta5cWVmR5AhCdfx0cLLM8oM__Xi0Z7iUAOd_a5SrW8Yusz64K7YL4y-cAUz2Vl_ofx7ty1j4vcRhZMdmxPJblwISHBixpqsyeVN9TPAd5bTHRUZIzLr1imweiz6gdMkbwBlbBCSXOXfEVsHlCPWRwyRo2soLdHF6_GQ7ZFvz98sf4Fbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمله عجیب سخنگوی فدارسیون خطاب به تیم‌هایی که هفته اول خرداد تمرینات‌شان شروع می‌شود
◻️
علوی: شاید آنها خبری دارند که ما نداریم؛ ورزش کردن اتفاق خوبی است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 469 · <a href="https://t.me/SorkhTimes/131872" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131871">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=dd_LnOs6RM7YYvJGoUbCFmaWH8RI6E7o4sD4ma7gC8yjjKvwf3eYj4uvoBJDaQw6xDzXlbTlvZCgcxCHAgNzMa4AeWXI0H-jBxgGiTM5WzgoX_6uAbpMg8dDiwj3kX-cMxeCEe1whrk4ucajpKyIebhrH2c13E7gjUm0MHI5lf_1rke90CNFbyAvYLvg6pLZCz3MqHtXvY2gPTrkW_0Hto7yDPVMmvHlCbwKFnORCppPlkoc5YgRFVjnPO93VToPkZbq1LzQnBeXJ95hcQoJ2GZSG64LZwG0B6eKIHEktiUIvHZhCWaJQQhOJ5CcIo2RQBHL0qshEw1p9T4tiwm-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=dd_LnOs6RM7YYvJGoUbCFmaWH8RI6E7o4sD4ma7gC8yjjKvwf3eYj4uvoBJDaQw6xDzXlbTlvZCgcxCHAgNzMa4AeWXI0H-jBxgGiTM5WzgoX_6uAbpMg8dDiwj3kX-cMxeCEe1whrk4ucajpKyIebhrH2c13E7gjUm0MHI5lf_1rke90CNFbyAvYLvg6pLZCz3MqHtXvY2gPTrkW_0Hto7yDPVMmvHlCbwKFnORCppPlkoc5YgRFVjnPO93VToPkZbq1LzQnBeXJ95hcQoJ2GZSG64LZwG0B6eKIHEktiUIvHZhCWaJQQhOJ5CcIo2RQBHL0qshEw1p9T4tiwm-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 447 · <a href="https://t.me/SorkhTimes/131871" target="_blank">📅 01:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=NUYIEo84Vpi0kIm90J1260v6pp23edaVFM8aXxyFmGyXjwkXmt6Mtq649pLx7wsq--Pgrg28YfWybPmCPoZqQF9Hl7LyDlwgSDLU2FVG6Z73f5rt93VZCiPoo2If7UW0tbzCkKtHz5FhHzRBDjIetzAGb1x1dwnN7FFxjyolvMOFf4WNMzOdWU7KBriToOSXAF73RWdSbWuPMASz_GQp9LWpdGQDr0lOnDD5yIC3lMPbswWz_f30xZshz2tYVMIOLNNzopWGEVVvKThqLOBqlZ4LOhUbr3LQcLmcGOLQZw7WyySbOt8v8xcDa4yaofL7X5SyurG6UHvKo6GRh0n8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=NUYIEo84Vpi0kIm90J1260v6pp23edaVFM8aXxyFmGyXjwkXmt6Mtq649pLx7wsq--Pgrg28YfWybPmCPoZqQF9Hl7LyDlwgSDLU2FVG6Z73f5rt93VZCiPoo2If7UW0tbzCkKtHz5FhHzRBDjIetzAGb1x1dwnN7FFxjyolvMOFf4WNMzOdWU7KBriToOSXAF73RWdSbWuPMASz_GQp9LWpdGQDr0lOnDD5yIC3lMPbswWz_f30xZshz2tYVMIOLNNzopWGEVVvKThqLOBqlZ4LOhUbr3LQcLmcGOLQZw7WyySbOt8v8xcDa4yaofL7X5SyurG6UHvKo6GRh0n8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
علوی، سخنگوی فدراسیون فوتبال: در حال پیگیری هستیم که باشگاه‌ها از تاریخ 9 اسفند به بعد درپی شرایط اضطراری به خارجی‌هایشان حقوق ندهند؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 456 · <a href="https://t.me/SorkhTimes/131870" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 493 · <a href="https://t.me/SorkhTimes/131869" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131868">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سه ماه تعطیلی؛
🚨
🔴
وظیفه اصلی که هیئت مدیره پرسپولیس فراموش کرده
🔺
هیئت مدیره باشگاه پرسپولیس که طبق قانون موظف است به صورت هفتهگی جلسه برگزار کند (و عادت داشت این جلسات را دوشنبه‌ها برگزار کند)، اما بعد از آتش بس چرا نزدیک به سه ماه است حتی یک جلسه رسمی نداشته؟
🔺
در این مدت، اعضای محترم هیئت مدیره همگی در تهران حضور داشته‌اند. در بازی خیرخواهانه حاضر شدند، مصاحبه کردند، واکنش نشان دادند، ابراز نگرانی و همراهی کردند؛ اما وظیفه اصلی خود را زمین گذاشته‌اند.
🔺
مدیرعامل باشگاه بدون پشت گرمی مصوبات هیئت مدیره، عملاً دست و بال بسته است. هر حرکت اجرایی نیاز به تأیید و چارچوب دارد؛ وقتی جلسه‌ای تشکیل نشود، خبری از مصوبه نیست و مدیریت قادر به گره‌گشایی از کارهای روزمره و بلندمدت نخواهد بود. نتیجه؟ باشگاه لنگ می‌زند. قراردادها روی زمین می‌ماند، برنامه‌ریزی مالی بلاتکلیف است و تیم در آستانه فصل حساس، سردرگم اداره می‌شود.
🔺
هیئت مدیره نباید تنها به حضور نمادین در رویدادهای عمومی و مصاحبه‌های احساسی اکتفا کند.
فریاد هواداران را بشنوید: «هیئت مدیره، به وظیفه قانونی‌ات عمل کن، وگرنه باشگاه را بیشتر از این به زمین نزن.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 550 · <a href="https://t.me/SorkhTimes/131868" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔴
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس‌جمهور امارات متحده عربی، محمد بن زاید آل نهیان، از من خواستند که حمله نظامی برنامه‌ریزی‌شده‌مان علیه ایران را که برای فردا تعیین شده بود، به تعویق بیندازیم
‼️
…</div>
<div class="tg-footer">👁️ 808 · <a href="https://t.me/SorkhTimes/131866" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/SorkhTimes/131865" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=h5gUMriSfNd7dhBOk56K7ITBFi5IAqQL5WF8zru080GZCMj_NiXS0jgY9ajE6pb_mLZQeP2qIuFt7J_r2-I-ILD7uWJ5UNa9ZcI0sXVXnVvwiufZ7rN5VXcUB8jKFMPjGE-g01JlES8aWeVuSsGnIAEP10edPureelRw40LXESyN_nibYDkY440Q75lkYybae03Z37fiYAGCuzULPMRpBcIWvQEl8p85dyGwSXOxHosNN4gzZHifdnaEKW4DB8p6pY_fYIiNtLWwAZ2MdZUs0WVPKYpw5NDTq0nGdrgZP1tc3H41Lzj7coq466j4x67FPVfbIT1IBRj8fy-JxsdDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=h5gUMriSfNd7dhBOk56K7ITBFi5IAqQL5WF8zru080GZCMj_NiXS0jgY9ajE6pb_mLZQeP2qIuFt7J_r2-I-ILD7uWJ5UNa9ZcI0sXVXnVvwiufZ7rN5VXcUB8jKFMPjGE-g01JlES8aWeVuSsGnIAEP10edPureelRw40LXESyN_nibYDkY440Q75lkYybae03Z37fiYAGCuzULPMRpBcIWvQEl8p85dyGwSXOxHosNN4gzZHifdnaEKW4DB8p6pY_fYIiNtLWwAZ2MdZUs0WVPKYpw5NDTq0nGdrgZP1tc3H41Lzj7coq466j4x67FPVfbIT1IBRj8fy-JxsdDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/SorkhTimes/131864" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
ترامپ: ایران می‌داند به زودی چه اتفاقی برایش خواهد افتاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/SorkhTimes/131863" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH0ccrlxLQ7F3-IW3BUyaSMHTO3vHDsuswS4ei7DZacTXKma3-E2NqTJLildmQ4llMtObJQnutbfTrWsP7Fc5LxABkA-5QLs5IAfEyOGGdIbPH60O-YcimeeUIMkB6CVkaSm3rCbY_Vt8VUVuIIk58PhXjl4L_GAp7iDUZB_n5XxV1W1ouOlNX-fgyJL8maqYB8gequo7XtCm3uX9M_y9duqs1X-avCNgpMDeprMw2n-p4Ld7dPYRQjlRy3ZhMpL49XQP4X5HLpk2P-5zyRDvg1otm8uMjHE0D1I95ifRQLc8CFM318_ilsPTjVQWDWtzHQwfoboK6UyAaDvzmYHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یورگن لوکادیا، مهاجم هلندی سابق پرسپولیس، به اردوی تیم ملی کوراسائو برای جام جهانی ۲۰۲۶ دعوت شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/SorkhTimes/131858" target="_blank">📅 21:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
کاخ سفید: آخرین پیشنهاد ایران که امروز ارائه شد نیز به دلیل ناکافی‌ بودن به صورت کامل رد شد، دیگر بمب ها مذاکره خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 775 · <a href="https://t.me/SorkhTimes/131857" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
🚨
ممکن است مجوز حرفه ای چند باشگاه مطرح صادر نشود و از شرکت در رقابت های آسیایی حذف شوند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/SorkhTimes/131856" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
باشگاه تکذیب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/SorkhTimes/131855" target="_blank">📅 21:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-QfoYeJRCwNUH31nlgjVxkYWvAOw1O7ILej77pAsNDEwKJmPMNO0IgOxV8lFkUIdiie7JDKbOAu5iGu5B6RpuQCUJS-LQOmz4q_QzVRxCJ67ygRXkSl_mBGozaKjbWeSKk8ldXaQZIgbzRS1GAIuVkiL6RUVZaYhV7g4x0BCA8vxDQGFIWcND2wCF4Nv9k09AuP4IYq3Ec8-fw_mgHeDaQIYNkftrQqBa2ISqnr82TyrmS6JUk7gIFD32Yi2BF8MpDrJgrCGUResAkuePDtLO-x9D9dR2G4TQkmRN2OiuCY7R9qEoo-biKy8nSdyNHb23Wr-E_NF_6STbwmW_gxBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🏅
⚽️
واکنش باشگاه پرسپولیس به شایعات در مورد معرفی نمایندگان ایران به AFC
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/SorkhTimes/131854" target="_blank">📅 21:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
🔴
اوسمار گفته اگه دوباره جنگ نشه میام و تمرینات رو اغاز میکنیم ولی اگه جنگ بشه فسخ میکنم ولی خب غرامتی نمیگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/131853" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/SorkhTimes/131852" target="_blank">📅 19:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/SorkhTimes/131851" target="_blank">📅 19:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
#فوری |   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی…</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/SorkhTimes/131850" target="_blank">📅 19:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 997 · <a href="https://t.me/SorkhTimes/131848" target="_blank">📅 18:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/SorkhTimes/131847" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcExj_XQieZR08aeByLt558PvBAY6XYAUfHzSECykVMqbpTAKdL8EHn0zIPEzuGVapy87eMGgEUjNS-4LKu0dFnUWDFFXrinzCXYxOwdD5wAYPLSGEzrvjbs_9H1VgBYmFJvPVRJr2q1TW25kaqEcd51acCJOAVH5HsWd1LZpMv_WFtnSa9OGR8ylgNEWVfuAtceM6a-p9Ffw79-UB_ej8FXk6sBxz-XBJznuUaAxrGs9tkrQxfsyvp5RjaVS7eKQWaA534rXNBFEM_MwNpw0_BQClpnpZm3Jg6LQTzK_jqnK-UARZFlFuLJUzvYYupW9f5vRBMjRiHSFyIoZ4kl6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مدیرعامل پرسپولیس عضو هیات رئیسه فدراسیون هاکی شد
🔺
پیمان حدادی مدیرعامل پرسپولیس با بهرام قدیمی رئیس فدراسیون دیدار و گفت‌وگو کرد. بعد از این دیدار قدیمی با اهداء حکمی، حدادی را به عنوان عضو هیئت رئیسه فدراسیون هاکی منصوب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/SorkhTimes/131845" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 952 · <a href="https://t.me/SorkhTimes/131843" target="_blank">📅 17:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 927 · <a href="https://t.me/SorkhTimes/131842" target="_blank">📅 17:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#
منهای‌پرسپولیس
🚨
یاسر آسانی وینگر آلبانیایی استقلال در آستانه انتقال به ختافه اسپانیا قرار دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131841" target="_blank">📅 16:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131840" target="_blank">📅 16:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131839" target="_blank">📅 16:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
لاوروف:پروژه نیروگاه هسته‌ای بوشهر به هیچ‌کس جز روسیه و ایران تعلق ندارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131838" target="_blank">📅 15:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:
پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131835" target="_blank">📅 14:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131834" target="_blank">📅 13:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131833" target="_blank">📅 13:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN6UvuR2b6YHk2osbKlf1eex4Cm2-HwLzdBnTrL3kwkjNDJEKD7DL31Yis1NxFSBw096mCuRTlVIf1w59Us8gp3ZGWdEHTkpVPEeXs_SVJXVuTcakT3VjI3GYiCi7RN7Nab63W-llVmb8c64gKwbEVGd7pgB9qUIvwIxv7Rv8tS14KBP3nqH5cSdDhTAfUfylRFb0bBokPwn3HGN948gR-5wCXLG7M1WGcmMxgD3hKi7f5C8PmYkgoKcY5Ly4fhFXNCraDUoIHhcXcD9r7Uuv0l-yzRMYVH6ls6U7FhQT-4YR8kPkSiQLDp65eMn1Bh-45y3Pd_jrwBNTb3mUthU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار آزمون پس از خط خوردن از لیست نهایی تیم ملی برای جام جهانی ۲۰۲۶، تصویر پروفایل خود را از لباس تیم ملی به پیراهن باشگاهی شباب الاهلی تغییر داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131831" target="_blank">📅 11:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131830">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131830" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=NvMagMykqqdsn-IIiHV3rQ2p9m6d_LcNEQ9dFF9QPfv5pGiXfYHJU8cUprDVTWCj68lJtNvO3kZtE0oTx-KDFj4oiNjl_FblB89JoD04aQI7Brzxr7pm2OWFIyz0vHBOSuyrBhXmkyKJ1_T27fpSRLC0SV8zmsmHmZxJeo0vsf54Qvh35FlqoZe_eKlwYBc3bPTikt4FcQ1hRC7fnLbEGwP6R_MiusZ0dmNljqVnsEBmWYppm4R8MwtOtDQlp6gajiMskk2DKo-0DNGn70A26UNXspwdiZV_-GXnux_P7E1-FMKVynji9f-gfh5lR52wt3RX-7Yk3AmvWJVJO9-mSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=NvMagMykqqdsn-IIiHV3rQ2p9m6d_LcNEQ9dFF9QPfv5pGiXfYHJU8cUprDVTWCj68lJtNvO3kZtE0oTx-KDFj4oiNjl_FblB89JoD04aQI7Brzxr7pm2OWFIyz0vHBOSuyrBhXmkyKJ1_T27fpSRLC0SV8zmsmHmZxJeo0vsf54Qvh35FlqoZe_eKlwYBc3bPTikt4FcQ1hRC7fnLbEGwP6R_MiusZ0dmNljqVnsEBmWYppm4R8MwtOtDQlp6gajiMskk2DKo-0DNGn70A26UNXspwdiZV_-GXnux_P7E1-FMKVynji9f-gfh5lR52wt3RX-7Yk3AmvWJVJO9-mSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/SorkhTimes/131829" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 991 · <a href="https://t.me/SorkhTimes/131828" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFkhRI4kvf16TWa2FQ-6MnNZwFgYe-Awdnxbd7H3ulOJwN6NeHhgwZjaxVD4KW37A-F7jz8aAlBMBWDiif-0BjCqGaxCPgAtsfm9Ou934ZKTl6oELePmtkB-wAb6p7bN4y5P2529h6h2Fpf4Y73_X0PJUCeqMBrNzNYmfk0ZZqQKF5Ux4Y2_ViXrxWZOlaF-4mtg9-4yPblAt8NZDE9F0ihvJObGIGZ3Pm7G2CsoJSg9xzTyqYrAWt7DtsVt9Qg11ffpLNs8TwSfzXRiZDJYHT9wcrmdErK1pLdSZ4NoYhW9WGtFKtkmT269rFW2ofK0ihXJqx0PhZaStaN0zAqZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ لحظه شلیک مجری شبکه افق به پرچم امارات را منتشر کرد و گفت: خواهیم دید چه خواهد شد
!!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131826" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hju0TX71xcdMXAFALq5TjFdYtbJNZuTsYgtpzsGnCE5wBrfEjRsIqorhwjr1rCKullxC6duP6R1KJTXyja8fUHGBJKXnz-kbyVPnaoRVpz8iUKlrDHrRNpPXcRQXXGkgb2L9_QLPo572w5VbbJaPBRlZql2EagLbYko3divNeN9YIVoDAAVX8nKjJBXl8idxy_NAWK84vfgRJjRqD3JgpFqFM2CAcsMUrqkfMGOqCOVytLhqUQ0ZlWyNdR-pykG21avvDO2iw9Cyma8GKexKwrQhTwhkw1sZTNY5U_omFHBNz1oEoyLUlTa_kIS6uJO16PRNH6sMQEEdVDR8TP1PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی مدیرعامل پرسپولیس قول داده که درصورت ماندگار شدن وی در نقل و انتقالات تابستانی یک تیم مدعی و جوان را تحویل دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131825" target="_blank">📅 10:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 997 · <a href="https://t.me/SorkhTimes/131824" target="_blank">📅 10:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚪️
امیر قلعه‌نویی: ما بازیکنایی داریم که همین الان میتونن تو رئال و بارسا بازی کنن. حسین کنعانی چیزی از سالبیا کم نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131822" target="_blank">📅 08:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLWXGALTJy0s6Qqo5g42_S--N6YhAJ7nquP51FaVW4VFYGZc7DWHKvwqMdjqhaw48yEGmE_ReCerzohOmlrBqq7bxA0PhKhf9rxMNxQM8jqLQzCmhK7p0gP2mw8uSPStPDCIRpC6EUucTCECOc7MArW6zCH3C6pbo_8luUkVwb3U3JdAOPa3l-X7ZoLsUPCssRm_fudHfRcl1EVqXMFSLS2AhpZ0W8Xef9O_ZSI89bCVSJXr1wWLBG6cZPtWuk4stdDWgJKeQHcOrNEanRUgTJgR9Q36ZI_0jhiIgqTUHQh5B1qXlWhIcsXxmdxAMekwvapqo5pDv6MXiRaGwcZz5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131821" target="_blank">📅 01:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131820" target="_blank">📅 01:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWZ9S8oM6hyqEW-mf3PeJPhubO3evbUOlNTH_SDiA6dVTJt0GuRK__EgPnvA0MCh8e8TcbK52qNajHEF52UiZU-9yZYX6QcKkUr0CJ1I0BNkYOZpLIGJQImXJjR_y5K4CdNubPXjt7dN5c9Mcf83Nw2IRV1wzzPfxWBrllin3R0NjROMjwl5L9clj1r_WDRwr5S4gk0TupnSLacrkBSPnAUMJjvsDzmhZ1puk7h_f_fDazYL5yvpcyXXVIXtcc1U_FRbb2144cpjz9hCohp2_5rZAavuD1FzgJvnyGHEZ9st7VLIHsPEwcwgU-JvVosNu2-JxZkGYI1iZOqW2bOpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فوری
| پست جدید ترامپ درباره ایران
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131819" target="_blank">📅 01:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131818" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131813">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131813" target="_blank">📅 23:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131812">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDENvz2ClbLWSTPSPcupV0QvZzym0Qj3EoqW2XGtI7gBAMt1dj-f9zK4xgyzexv0VSqeq4w6O8wDRJXADjjYJW5XAekA7YeMiYmf1LJg03ugl47ej-PXNA_uMXVCP0K0T7nsqvdxobjUoDRcgPojA3OL_MaAm1Y6I8Xj4W0iLsTJ137_sbuQGVtlMsTXbKAY2iE4KCtClzhlLuBd98D6horPhSF1jceNuxpgeDIQhhmw1i307HUMXPq4xF7ogBQqUH-VRElOzBHGuVPT8Vmf9qLXxZ8QWNBfZCmCG9n6_5nNxC1U-tfhJdOe2Fi4q2A1FjW6vjC_7KOwbDZMppMo8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131812" target="_blank">📅 23:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131811">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
امیررضا رفیعی گلر دوم سرخپوشان پایتخت پس از چهار سال حضور در پرسپولیس از جمع این تیم جدا خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/SorkhTimes/131811" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131810">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFCCJJ-I4WLhWoQTiDXCAH58fgVw6jv9Ook1eUqEKtudgrj7hz2cB1vLMnDJ_BR57uzNSz9FGNbHEW6_GBuGgDexPNMVh5dLPRYLHC9X0DHlzUPZjaV7OthkBrHnBJLZWkbHhNWHektX7SyKrMa8JnnzdLHCpdlB4RPMKZoaTHUHk8ZliykgO3aE1p2zEZZVjInVjAYay6sq041qCKycGoJ3cfwXVTEHL52PLxvX8yMNNsU8Eq-rbA0NvN-ZxL9TIDXE5KX6wjxw_BFca4PrqUDWUfLmHtu-YwX2GH91fEyD8DQu6_z-LATwZ_rLUIjNLSH4ClF5BLSc02Cv9UYALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیران باشگاه کیسه اول فصل رفتن دنبال جذب این بازیکن و براشم پیش قرارداد فرستادن با مهر و امضا رسمی ولی لحظه آخری از جذبش پشیمون شدن حالا طرف رفته از کیسه شکایت کرده و گفته غرامت 800 هزار دلاری میخوام :)
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131810" target="_blank">📅 23:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚩
🚩
🚩
🚩
#فووووری
✅
فرهیختگان خبرداد؛واسطه پیمان حدادی مدیرعامل باشگاه پرسپولیس در روز های گذشته جلساتی فشرده با مهدی تارتار سرمربی گل گهر داشته تا این مربی را جایگزین اوسمار ویه را در پرسپولیس کند!!!!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131808" target="_blank">📅 22:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
رضا غندی پور پس از استوری علیه قلعه نویی از اردوی تیم ملی امید هم خط خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131807" target="_blank">📅 22:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131806" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131805" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131804" target="_blank">📅 22:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7krrXg1VkpYmVTkF6lFFqlqTn2Uw8rnVMUA8YL2qF0BXoTA5LQlztKwhsK5MiZJjYCUBEI_oV1ytOCygwKkX2AmtKkZ_sxpMIpJkygusaH9DZ-k-1rQlovj4BrhsDvFFqzHVjBKE81zlNU6B1oMAzA6B8oc14fszF_-XJ_EK_KYbiS-LxnugbX4xrTC74-HajvEaD0domaQVWOh_TcHgLFsOeTdXli0ju_TgfCz_UacJoNGUhbcTnox4w2Evh5GnteRYX6GZBu_ZIX5UeouU6rOtHcIXaiin12LcEZg2s7uEofH02TEr35OEgzlAdaSMKZV-kuHoOOikwat31fHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131803" target="_blank">📅 22:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
ترامپ: ایران خواهان توافقه و منتظر پیشنهاد به‌روز شده‌شون هستم؛ پیشنهادی که امیدوارم بهتر از آخرین پیشنهادی باشه که چند روز پیش ارائه شده بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131801" target="_blank">📅 22:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
بر اساس گزارش منتشر شده از
CNN
سپاه به چند شرکت نظیر گوگل ، مایکروسافت و آمازون گفته باید بابت انتقال اینترنت از کف خلیج فارس عوارض پرداخت کنید وگرنه قطعش میکنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131800" target="_blank">📅 22:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فارس: محوز حرفه ای باشگاه پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131799" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMRWA2xD0UyDDYLZAqU8y3NBY93XaQiJtzyCw_NCbv_aLkIRI4ki8zRt82xvFNngbndhtqpx6LbuLi03AHEvTdqtEY3v52EWDBG_MWNT0EffpfZJhk--bevbWXrz1dTWN_1qIFT5Di-zhD0uMMfYBu0ufsVtOK1dhojORedQl0CdN11Go4bSSX_oBkXvKVf-B-pkyWT3uQfipWMCaVj7FkIE3b8oUmXb-E5kGNM_XCz4OrWKxe03uylZo7-3w2UDXcoUsDIZELdzhhbJ2W97yXcp79OsE6gnC-NzTzapV0RKn1uABCrz842oNB0Hvy67nHmz1pgzg_qZi-mzDhms7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ از طریق Truth Social:
🔺
برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
🔺
زمان اهمیت حیاتی دارد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131796" target="_blank">📅 20:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovBqNz8M6kAOvmL2H0cFGsgQun0TDb7zoFyDQ8DKnPRlwUhwE9CvebaWPkzRJtBWoBOSOTlqPPt8TmIX_9BVwKZ1Vtfll-gLiGH37KM98n2f5Iu-uc3dM6Vw_E89IEWwIHr67T8gwI_gcwYDU0JGFPUgDK8Y171sbK68jwAOlU9M8BGdLtXU1wnps02yD18elbYMFL7wdjhvmVTpJuiSHaPVfu18ANCgUYHJqk88a4tu_s7MkLICgZao-cn4dUMlyjalcCYZrqLsEI_vyAWQd86XcMm248CtfvB1DQY_8PZsdBe3LCY62RPPdTpDgPCSNYiADk6xzCJJdStb5Ee4Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 953 · <a href="https://t.me/SorkhTimes/131794" target="_blank">📅 20:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkPJeme5pE02vWl5egVHcIAQ7frdpF0BLQMqTQjxJp5-xeMPPtE3fpP38kxAqbHFcCtLUWPoX5LLMB81lB3bQWQ8e_l_ts8n1zTAbtmK1oNSlGTQBUALJzuoIcP2N7i7m3Cto7qoOyriFq8FmnQMV0RMIRVitV-TDXqtfgPlXXB39yYXDB5aI-v0loavc12yIJNiNzkkCcyXDERtO6SESYTCVxueU4tLwg-WWvmwJPQjGOfCD1KXjJ9cH5rkT7AkyNWrQvfsT5khvcNn5hUHl_RkucII4Zk8an-Z_tFxUI7GG9cznZlrCPigPlOgDDDcT-sXDi8nZ7LUCzrG_yrrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
استوری باشگاه پرسپولیس به مناسبت روز ارتباطات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/SorkhTimes/131793" target="_blank">📅 20:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
ورزش‌سه: علی پروین بخاطر افت فشار ناگهانی در بیمارستان تندیس جردن بستری شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/SorkhTimes/131792" target="_blank">📅 20:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCWKDQLwB82mZ3NXSoLc2suh1nS9hpLA4JnbA2rcyRUte2mPEnDuRKC-RnIAoK0pbQQ4CybITHJNz6_rVfacfW9dc_S0lPqOmMY7mP7buoaTpTdvlFINtwKoRjO3G4vH3kt3NYr8DYkqMI-_oXRqykKLz11TgEw9-eHmaWUCw7mufHs-Idy8CtaDPgcKSDjWJ1FC4ro0mdCxTF2FhvhnrYzYCIQuqJ-bKq1MjIXjKUeHLbCueq5vReC5vcu66lVZxR-C7rCOU0_DBuYlP3ef9OUyIfEJNDC9LYKhHC6Zq7DuLtVXotOfENOiIPZudtEPJag88pajJaQFsN3pqJGp_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 992 · <a href="https://t.me/SorkhTimes/131791" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m17f6k8SUu-7cxD4ha_3l5RdNE2ElC_LjL58_snkLEw4nINarw6hkKplHDyuju6-lwI2Cpcc1LsW-yyi1BoshZD5OvXXM9xpG6LgTMJj1ssm_40V5LFh3xSTKsFFbj0VcQxZOEI4c-4AEOVVNxDnjNIb-yIBzc_IGFnlTgdtymDfkUWwRCRykDhloCCpUfAsocYwRmjIqdFfuDudkUDIYqaGxedvRYFtcq-z5hBMnj_Qb_teC9Fr55JDj5ASBik6Jrmr2zpteCTISCzv7PhiX0NWxxmJC9QD5meT89PiSDWIFSpZcTZyp-GLlpyXXbm509OJh7_xOwEDPBpbG0ImPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
فووووووووووووری
🚨
مجوز حرفه ای باشگاه پرسپولیس تایید و توسط afc صادر شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131788" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
اورونوف: با پرسپولیس قرارداد دارم و فصل آینده در این تیم خواهم ماند، میخواهم با پرسپولیس قهرمان لیگ و آسیا شوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/SorkhTimes/131787" target="_blank">📅 18:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131786">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/SorkhTimes/131786" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔺
زیرنویس شبکه العربیه: از قرارگاه خاتم الانبیا به یگان های موشکی اعلام آماده باش فوق العاده شد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131783" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131782" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131781" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131780">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131780" target="_blank">📅 17:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131779">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
پرسپولیس، رکورددار تیم ملی در جام جهانی!
🔺
در این فهرست رکورددار لیگ برتر ایران باشگاه پرسپولیس خواهد بود که با خط خوردن حسین ابرقویی، حالا 5 نماینده در تیم ملی ایران دارند. این در حالی است که تیم سپاهان و تراکتور هر کدام ۴ نماینده در تیم ملی ایران خواهند داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131779" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131775">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKtYoczJ7IttC62h6bm2Hr7bTV29C19leS84yo1SnDwoxdAMiO3nJ4bvymlDWD_LpAEh3U8TggzwULqx4NZh6T84tH3bbdSMjpVhNkk043rybX66b5QAJygzcFAftthDM0Ycvc0GNTWaZKFS2RCSgb_YM7XT9DLA45UMLHayLW-gOlmAmSkRn03IcdVoxkY5hetazsPlAxgUw_qDk1XLRdHvo6wRkemWtDoN5XNovECLHsG0oT4RJOEIZY93rPPJeS-0d6U8wkMLwMvKyRvPgu1z4hPHGQC03dhClwuUHN19ADpLjc5Z25AZJsqTiwZ_2OIYDzC7ptQcKefhZWud5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اشک‌های رونالدو پس از عدم قهرمانی النصر در فینال لیگ قهرمانان آسیا؛ او در مراسم اهدای مدال هم حاضر نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131775" target="_blank">📅 14:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131774" target="_blank">📅 14:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131773">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
قرارداد علیپور دوساله دیگه تمدید شد
❌
✍️
باشگاه پرسپولیس مبلغ قرارداد علیپور رو افزایش داد و با این بازیکن برای دوفصل دیگه به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131773" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqM-h8c8wiEl5PL2BZQOVvUHjCNCUJOPGMJastyirvJlbWtfitlqecktkS1aKrYDa6OXiiR5B7X44lYduolwfTtJkP0adrDCDidSFu9o62GAduaU_kCSIHiXT0C4bdm8nNaXli9zT5q8eJETvR3lfttVRQ8nro_yxSUenoTFQa4dsk6PBh305VMITIZm6pQrJq-U4AbK7apzofuFT4lLkaK-F7rpQuDrxAlQRo60f2ZjmmTN9B0QhHRUmtIuyqY7-yEZcgkB3GBQGDAp9l6n8WShgwU3S1O3KVinlTbbxc08MTRJdQ4Ai4LDRccrTdnUNpNI-cCg6imaLFfp7Y6n-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131771" target="_blank">📅 13:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nM1VjQgferRofs5zsvMn5iPlg9S7jO2OyoohJT8-8YH1hPqxUSIfLdeMRdLOGl5pTzv-ZsVm9qBhk1DZUKKUPnr2BDp_9vcVGPoZKi2_jgIwUlcN-S4dxCB79fnhy-iqmjSy-MtDCasC751A1orODZOkB3B8Iz4wqfkmddZPq0AU_i5EV8jQO5ZVZrhJr79PbkAaJmUROSlUgci5aOVB6Rx8DKZOeEjWnAiKyEWe1sprzvTDeNmKhxzOeL52SqflZmP5RqBU3FHvyjKPBQ9i8Fv5a8qIiQUKRPxmNpsyyu0cuh3Nx5g6KsTq_ZklZn0fB2zPoMr4Ctwh2A6t9NTMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پپ گواردیولا اعلام کرد ؛ فصل آینده هم در منچسترسیتی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131770" target="_blank">📅 12:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjEu5pKC2nCiIpBOqTIREKx2pjv9HsCq-Sikh_0bXfj1jEHOqATs83keoDBAS1M2XzZ5ZlQjwg1uwMLjtjjnrjS8OXUOIyeH-5FqjKCHWBmeOrX8v_sbP61fcBgTrkaeidMM6nu_qq3Zp1-Bem4F6XpkEQDblI05SYEp12k6vXeZ1U8hOyfg0LMKGL1qo5rQ1TBAiYd7MoHh-M5S-kmFylWdAO63SITeqrllU4WViM-aW0EdxJ8ECwTDSJiqP7DXqnongcc3X9ZV-raIlmUeAQGZEAt1pxAnMv3wQnjc48OsVA6GBXKYsCCEgTkHoAVDQ7i_WQMkehWlRRa0rLKcSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131769" target="_blank">📅 11:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
#رسمی  تلاش‌های محمدرضا زنوزی جواب نداد و در نهایت سردار آزمون از لیست نهایی شاگردان قلعه‌نویی خط خورد تا مهاجم فعلی شباب‌الاهلی، مسابقات جام‌جهانی امریکا رو از تلویزیون تماشا کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131768" target="_blank">📅 11:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131766">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NedTXJyGSmOFCCN9shu5MhFed7khhBLuI4xwGkhqTKQDOGzZd-wKMIkOiwcHf2StqckhWual2B3pNWJTDnP1oq11CcraoPyNf8AoIrU9qAV9lxZX8hT-ad3FI5Grplj70ncloRU4Kf3UoC_79tAQjYwXFAZ5vYXEq7wNY1-NWFj38b0nWHt76Rhmpl5WOPNsWP3b4wjv-4JGWAXdOAp_9Liwwtumqy4fwiV9el29IxtIoF52aWutSjsvNg2YRhGXor2hjRwGvXmsaH7ZXYz8HNTBtMWDkEMRoK3wedAW1jmG2hbLWOUuApUCuu7ZIUIldIIsOLJbL424YO_NTauWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
علیرضا بیرانوند:
▪️
سرود جمهوری‌اسلامی رو داخل جام‌جهانی با تمام وجودم میخونم و مخالفای داخل ورزشگاه هم هیچکاری نمیتونن بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131766" target="_blank">📅 09:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131764">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131764" target="_blank">📅 08:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131763">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEd923lemVdqvnP_bXD0xL2H5GMbxt3XTGpN1sGNMXbCF9HKdEdhWTnB8ex3oH1ISNtr3hKG_0u7lQVSAtznO__nxUTpqa5898QcJvnLavTq6bbn4plooJCzkHX-ITtIcg6WGB7PHq5kyQyHIupJvRiCqJkU716To87tiNN6xeORyctBxgUfZ96N1Zaa_9z8jyKExnSbyVX7IOt2-8lS4HxjxYSr5MDoYzPYO88A_1j2eJtu-S2Amrg2sasfifA4k_g3sptLpu4ZraWl_FZ_d8VMrFzuy8utYsqdhaH_6m8pA9DAjdTYKCKOd72kLXIXBSx-ewqFyc3dskysIpwfoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131763" target="_blank">📅 01:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131762">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131762" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131761">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/131761" target="_blank">📅 00:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131760">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131760" target="_blank">📅 00:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131756" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131753">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
ده دقیقه تا قهرمانی تیم ژاپنی و از دست دادن جام با النصر و رونالدو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/131753" target="_blank">📅 23:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131749" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131748" target="_blank">📅 22:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131747">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131747" target="_blank">📅 22:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131746">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7m9h8wbR4Qi61ghkWzjPklQwp6TnV3p9PpOU9PO8d9TNbJBtdJCGYXEFyleKYMtpuv1LMrh5DcWQa4Xe61_TcQHWpSjHw5etG1C5NfWfLmPOVARhrnQgXR1DKbY___nlTVi92vQIKmDiBxdv0oVKt9S9VAalM6jlrLS-2bF9bDKLeLrwB-B5FR3CQr8eU8FdPnFgXB2lQQe24060U32ANfhQxRQIncufEosHEzprzoveQBUu4PTbtUwrgp_SmWnsbKSZ7ndUcEJxgd-lI4RLQCFG_8K9clTpH_2HhbEXmTmGWdGyKTVXXj85hSlPE4PkP2MMJ5Q9b2vnVNL6jXiyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
رضا شاهرودی: میخوام بازیگر بشم
😑
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131745" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131744">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
خط خورده های تیم ملی
❌
مسعود محبی، دانیال اسماعیلی‌فر، حسین ابرقویی‌نژاد، عارف آقاسی، مهدی هاشم‌نژاد، محمد مهدی محبی، عارف حاجی عیدی و احسان محروقی ۸ بازیکن لیگ برتری بودند که در فهرست ۳۰ نفره تیم ملی برای اردوی ترکیه قرار نگرفتند که خط خوردن دانیال و هاشم‌نژاد…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131744" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131743">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰  گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/SorkhTimes/131743" target="_blank">📅 22:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131742">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
فرهیختگان: امیرحسین محمودی با درخشش در اردوی تیم ملی در آستانه حضور در لیست نهایی تیم ملی در جام جهانی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SorkhTimes/131742" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131741">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏆
فینال لیگ قهرمانان 2
❌
اشتباه در آفسایدگیری؛ گل اول گامبااوزاکا به النصر توسط هامت در دقیقه ۳۰
گامبااوزاکا 1 - 0 النصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131741" target="_blank">📅 22:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131740">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131740" target="_blank">📅 22:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131739">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
قدیم‌ها آب کله پاچه رایگان بود تا اگر کسی هوس کله پاچه کرد و پول نداشت بتونه بخوره.یا سوپ توی رستوران ها رایگان بود تا فقیری اگر پول نداشت حداقل گشنه نمونه.قدیمها نسیه یه امر روتین بود و جایی تابلو نسیه ممنوع نمیدیدی.
برکت وقتی از زندگی هامون رفت که دیگه به همدیگه رحم نکردیم.
‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131739" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ: اگه حکومت ایران به توافق نرسه، دوران بسیار بدی در انتظارشان خواهد بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131735" target="_blank">📅 21:06 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
