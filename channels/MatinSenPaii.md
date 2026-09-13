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
<img src="https://cdn1.telesco.pe/file/v8LX2QMm5Fi7Oj--OGhQEGuqiwwVy93VF0_CJqCZRWmr2hz87wCnRT6J-KFwXhndnrjY278LmAxMMbOpvYbz4YWs-gUsxjQK98t3lf6rc7eEG6_eFPivkjfbCP7rvrFZ1yrhT-L22oVhPp08nGrR34Z9d09ipJs48GRlmnJuxM3Tzw_KystcxQw-0HHOjyixrsMU3flVtu7F-L4VnkMJKwJENEl5zkocenKhdFxUSgKJZcCm_XLetGPomyUdTy3HKzqXenJnd_UfiZ45ZlqVilhGg3_46XfPRoxAxSB4AHJkZ0mV0TVZONpntK9dLvZ3XCbnnbgOVI12sDMzTChR1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KGPqOw6uShsFRJrxlojbGPqcLCy-wP0VTy19Y7W-GWbX7vSqAj5DpZmx4vX3DwsBV3i1neHk2FQkhMqRNWyKv1vPEgx4ojJuwS0a2dWU9W07K65nuQaDAIWaJceETzB8o5UXuuGpQ4hCXwlCm8ou1S0ANmT12nKHyvrn1W2Bq7e0QgtFUCabIcy1W3BoS5mEQqGwpan_4sLDafW4OSQIg5W1xcsUvsBUcvr_qIkts_L_DWDdHWG21BUV_ReBel4iAVakgV_0hheRXNNeNOTpK_A2iMCtvG7ggdoJRYBWMsGWJnNThn_0j2qLM0AUoMhV2E2V6hmmgFT9Wj46YQMj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=eAaBqnYiBQVTGVhEt0nrNATl-E75_7vyMMbxbb9Sxyg2z49GA20aocu_A8-HGOg2r0tDL9e7R_VWh4V2sLm-gahazZp8NEiVsBe3t3bgahLr2B99J7ElIOjX8KbY26XTNZcUKeV5kZVY66ow9i7EOi-SaMxthOV-mDytIRKR1KOkSBnIFy2kWUbG5xtLiw5LpfI0MkBsY7q9ZsGXoBeFKf81vGZ74V2jDZTNXzOVdmecAaZ6JQfarL3U1nSfA-JVouiOvNmJrFafhOf5627-7ebKYj0OfB6L9HAxSVjDxaH-kz3D8LUbIpGDsiNVdXCuTLO781ZkHx3oyhwsxTYzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=eAaBqnYiBQVTGVhEt0nrNATl-E75_7vyMMbxbb9Sxyg2z49GA20aocu_A8-HGOg2r0tDL9e7R_VWh4V2sLm-gahazZp8NEiVsBe3t3bgahLr2B99J7ElIOjX8KbY26XTNZcUKeV5kZVY66ow9i7EOi-SaMxthOV-mDytIRKR1KOkSBnIFy2kWUbG5xtLiw5LpfI0MkBsY7q9ZsGXoBeFKf81vGZ74V2jDZTNXzOVdmecAaZ6JQfarL3U1nSfA-JVouiOvNmJrFafhOf5627-7ebKYj0OfB6L9HAxSVjDxaH-kz3D8LUbIpGDsiNVdXCuTLO781ZkHx3oyhwsxTYzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kbd4RVa70-jTIRFepXPcUKcT2FwXXd4X_UEtupNTyzytEg2rFyJZ1SrNVZ0zHdKrn_AGwFvBRjPJYtZOkXsmcr7cXYv7wK3r0UAiXRRPqcykZSEowKXvPQz0BjWkQ9IocaYpfudOa6wW0VxP74uxTRwtMCY2s2an26JFKz3w1gnTURmKWF9OJtc8lCd7W2b51fE2uWu8b_w1lz7OV86BZf2S2ylPWqYH3ZtDzYZ1KEbUhUA8sojccs7TYu2o6-gBzJBtl7XgY42C9KbTIMbvMIqaAz2WtRoOgvMRoDQ8R9_jm0VsfsQx67gnpVGJu7B-wpCapd0EgOdRLIsDcBNVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VuGhCToYb2GnlrYZuZbtnu5TqnOcsSJ-UpW7Md5SnYATIrsnbrhYVkap6Cawehsv-cUirl1_gmBfNx-oP2ge6h0OkZeYTsdX2m-qLHjkh7Bh2GkXIofyJV1Xu5nB9uRHudV8g7x7213HynVGC5Zl7V_eL5lczGfgu3SOczjRJhMASu7WbA6H7qhjMtqv-pHuRjgEhSsYVK6Hoz7f39cFykhC3ShL_Bm5olULEUyUqIrX1XadvZy_cyvjLeF1cxtwSTYWWwHoQbJgOOtfjGp0eCJ_9vJPwS19gfHK8wMazS0Lp6wObwC763iuVCjNsTni27CmjJL4AFAdQlIK4w4OQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv1cejMg0iBtJQT6es9GeG17Y7BOsflKGYaEZYHvr3o_cxTJHYLE2TWpt-qzR2w8XyuazgHULHPWtchA8XrnvTTVaBhq_QtY3bGuYJbqvUAPS5VK_u6WAabzfYzbQy4o1BOI8c8w_ykqlKtwvOzuoatq_Xm66QnFCZt3Osxemuycwag0PbQT9VykKAgFZQbbBW6Ref4tZm7RF4PFV8zCicuDVWtjosH29blY9BpEMumNXgfYUZAZw0h0-2R8OmZH9GL3hT5ZkAFoFc7o_tkhHA3npmE-pnftPLHWtnCO9KtVLMd2eVvct5XaaXfuohdHDvdjM3-WtA3pDatABp9aOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=RA32PGnSuxtogpi0JU2x-mG7ID6vv66nTihIwCt0JUMjE0XQxFNc1LBh-QpPnwfUAX5iJY-mP2IHlC5SOLc-NrruMU1T2LOu-593USWlj6P5vl6RDKrtT-uKviJpvgs5rYcyaWT9nHqmNSy5kWIWOp8Qr2jx9HGYWuzkfhvGpUZnJXT1avQdBGZ2F7X3cwDgEUpxaOJ3h4PLFz0p75ZC0O955DktPq7i_8134FQ0tk4rF_RErgXmJw_pnQcOHB0ArDcQZCphdaGinZzYZDZ7ssJTj6JV1qo0VYFX_Swi8qoYS3R2EV0bRsUb5xawIEW1uEkXoIvJcB8RotfWLxfhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=RA32PGnSuxtogpi0JU2x-mG7ID6vv66nTihIwCt0JUMjE0XQxFNc1LBh-QpPnwfUAX5iJY-mP2IHlC5SOLc-NrruMU1T2LOu-593USWlj6P5vl6RDKrtT-uKviJpvgs5rYcyaWT9nHqmNSy5kWIWOp8Qr2jx9HGYWuzkfhvGpUZnJXT1avQdBGZ2F7X3cwDgEUpxaOJ3h4PLFz0p75ZC0O955DktPq7i_8134FQ0tk4rF_RErgXmJw_pnQcOHB0ArDcQZCphdaGinZzYZDZ7ssJTj6JV1qo0VYFX_Swi8qoYS3R2EV0bRsUb5xawIEW1uEkXoIvJcB8RotfWLxfhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA82HIawR3InAMCe4z0r2QopSiaSu5UAxJW0WSOTgAyowCUYc8g9EommiHcFQvG7YXdznjuv1pRIsTOSoRzRkGpEThPSgGbsXXoU_hy4r5Zs7DlYZw-RT0tP9Rxcq3ABVsrzV-6EGGRpteLBnHo7au9D6pMBMuQYVYQj5cmz9n2vY4NaroYM48lCrsnpnMv8l37Kg7GBP4xnNPfmZHpo0x0JpS-q5dQAjTPT57kNvdU-jvFyZ0n58HWadfeZGjMHwyib81u3ZFTJUUGSeEmJzyIKP5F9YETNmCVoGyR5j8vFnMLzH6AepElPFo2no7a8BBo-3pd6v9iHXlt8_7FPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DbtIdlNahHbQxmCU8JBWqi_DGvjhIqym8pqfvKJeirZ-ByYLH9_6o0EMPVfaJzwNWM-FfFBx5ZDBSdQeQfvgd2GrIK7C5rvyeHWLfKD6u1E-g9SltvDEYM2UmWQxs3NgFOuBcnbTw2hBVFzMzObx_P0lFbgH1XzbqridB0-6megO6rr0CEV21rgDfi8p-OHtrMEt2Yex2AIQh3SQFWmnOKBgXU7L6erZY_1W-i39Vbm1iHOQiSZyKd15tLsHxMe-72wZg7SyUewtIwV-JwmQNS9I_P58WYiLFqGNdksEOvWf1ZEBHL2znELXYXA15u_lPQwGwUzABbHf64TjADxSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O8GBFYFMYERD6OmcbdiY5tmhJgoy17GGfwIMh7PVinLxOUZuaqu6g9kjoN-6tgUGjwmI_IU17fbN8kdSdVc1MMXYhhhdJdJkeQcY3mlFDSCLX-I6bptL2d93LDf0Uta4yEq2WQXn3DFtF-BZ8KIhYFLocvLtv6yLs4m6W-jfWxj4KozY6CFYVgntiR2Rs-QX8VBoG5rtH4Ry1VXJTpqTBvQDKWnRgYVrIT9R2J-tnnNFS7YQVTsob0sSNNyZjvwtWI51GJeQ8qQA51jzre-ih1weXK2mrfzC1yamFGgb6INRYNmG4eLdRG9imPAnW_zKJDGRF5c8a43AvUFX4nVk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RfS2qxP_vTl84iFbRR4MJ9OHrw7pTKuQPZ39YxOIwIpJ8hsKe3LN_-Kd7_Vn4iEmCNLrwk1iK-_BxhVWlrq0gVN2Ux81w9Bxkkw05gOaOkHSw1eMuw6pB8CJQ3nQrwiZtqcqAnUF9WHQ7W29hy__YNZjAxHl165BQAHN4GAg_z_1EQXCBNhv7TLLeG3L589r2n7LYc81GHMZRWnNbNyEaiDZi-Lo2CeU3MqcUryXnTcJlRDbbm-abeT8XG3Sj5pjYvt6bF5peeNIKCmATjrrAVNPf-7iEWcIhw1HAw7imVvWPdqIEFkMA89_LGI18NujFaZVfmBpnQcxfYM-zGOWiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixAyyr44QuPaPySzs4FXe2tE9ZIkl42S8DFj4xIpJpINqFGoOWLRg9AigLNYA_7DV_6n_-piMbUIPcr2gG8XcOA_wO-VZeKfTxeUSn40_tsrf9MZnSjPg9Do-Tu_jsClbASOJmXlTxps_siDHh7DES17FaKwgt5juv8dlj6BaEo3eiRzqQcT9Yk4SG0D6dguKKrGYwEbHPVvKnpDz3JEQXMkX7xeHf5D7lZmOLHbPEHyRjD58YDul339ghFGb_y6egd-Y_8xvf9nIUda-qcerHQF9fdASLwxmAAv9IVBe2X4q8clOprS-qhjqi1cRd-Cv3Xz4ydwUu2sSrqE5-sFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTMwkeshLL6e3VNJQUn2ERe2PvyXOMgiHmsZBsyUT6MgHQrvYSajYvtLCKvQE3uQOkFERHtkQfwK8Z6Gf-cFwO4FSlKSPtvrJiiKjum9XzHiE34tUc-9u9MM_yNUKrbkI_MrKLRTSXyd7l50YoVDqMLWx5DEELxxs4suywp6DqlALH55sW_KNhQ97LL6DEeemibq35s64e9z7FLbTC98irDttsU0zvlIfTt2-c5lObvxzoFIpQBs7kPzmzEBYDWOUhZl7XqVycpTIIJgly5LzSRWMhDT4wTpw2yhF_3v_SUs_8jkZ_lP6VjJKYXXI3AyieF6Z5QyDTQuWzn0p1X-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=tZ9QvniJJTsKSvn0JQV3keav9odHcJDYFj2AVig8wKPrfvLx-gSBxzn2A0AbY0CDGbYH4xT-Qt5oreuF42mNzwJYGnD0dcBadwYSY1aGWtSz3poGwUqE6GAV_yyc3DnRaZL_Txwq849bU2tCnWSpYZ_WSh2DYxT93HfTl1xnYtIPbTU4YFtECPEd3SdPB3q-48NDY4g6bQOxx8lecL4kHlhVpcNSyc_uvahzfPJiE-q2gMzgiBAC0PlndJgguknsQVpSkebAGX-MUM9AOj9n2ki6qJJBeu5g7OiCKtELxfHPVjs18kf2Jh7tgP9h5dBQU-X80vsZtHIGO2rA3KZxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=tZ9QvniJJTsKSvn0JQV3keav9odHcJDYFj2AVig8wKPrfvLx-gSBxzn2A0AbY0CDGbYH4xT-Qt5oreuF42mNzwJYGnD0dcBadwYSY1aGWtSz3poGwUqE6GAV_yyc3DnRaZL_Txwq849bU2tCnWSpYZ_WSh2DYxT93HfTl1xnYtIPbTU4YFtECPEd3SdPB3q-48NDY4g6bQOxx8lecL4kHlhVpcNSyc_uvahzfPJiE-q2gMzgiBAC0PlndJgguknsQVpSkebAGX-MUM9AOj9n2ki6qJJBeu5g7OiCKtELxfHPVjs18kf2Jh7tgP9h5dBQU-X80vsZtHIGO2rA3KZxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JXa28ufWdDPiV2YORbYJU-ybcsP_yaTEddlbRi7TovOthdtPvlGRnnwZjPEXDqVgZuqGHuOS4UyRZ-THOnX0ZngxwbE0_6tgOWu3Yb2I9wgOXOLD2e_RkWRVcovkCcCjaZwfYOD7kj7FZb5zIq7nX9asw3g74TdpWTkHDI_-SxtyHTzXn-a07KwjUn0-KRFwTWwj3ivZYsamTfPi8ZdH_qWvkPOHcrnyxsnlTQfL4Id9FFr7PBwm1zty35sjipBCSdgaKSfLinQUwaZ71qL8jn0TCdRGLGArJGoPEh1-KIm9_UlX9IpBk0ku8RSt1UJK2qg1QJT0SIeDJMxLKJRSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fXlrJLPZeRUbRigtYqgr3BkVBw7BFleAAoksJgjAvzQm4aViyRk5pDHqfj0dRO3zB942Kx099lYi0EcednRj7I_BUds6LR-wPyZUln0Q5mCDhad88_lCr4J6RLa5Dunp7pOaiFZ6QEVND1uJ6CZycjL0yz5Y0crXn8FZ7akXHKUJznnF0sb0c5SvWHP6TWr3zKbC6hMUOeq9-CjkoOsEqBXjZah0zuwzewWC6YbOYFlVyitt_52q6ughPSuOcqz41EvFZbx6M482pJ1NbAW2-JQ9mTwxzQ7Jg5XTKKVqS-Sk5OZhwHvDmw2YAEV7qGrtqsPq86RhzZTHl8Y5vXdbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QHSzLsILZSXID83e-GqYV3EqLsw3D6ih9_Zs7f4tAqGkpWgBdSKP3zZ4PLIFG-3ugaSnkuj3sjp-bOaz5Qu_Ltd5M2cB1sQ-XTN0qzESs9Gac3gu_JUgC2NTz7RQ0h0NVUL70VYdcOUYgzKwDhb30rh5yYxuIXth4CLEFdEIavOKJ5_5qzdRwSiadXfxV4M5-iMV-cyM7WilySDE_vNyrrCcdO5THddp8eEvttF-nU2ztvYYnd0gEy7Rl-9tL0AvgvOvbhLU9Rd5yNHQiBKV0tkFppPNQcBGs2rASwiV-n7eTMWsMm-EQBKLwZ5Q9onDhpgLnIHvnkVPaYVVBp_Xow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljx95lZjjeZvB_fGh5cXHLQBsL4_Hkm01atvJwy5-amJI8QCnnGK935SHKb3LJ_ppJcZaCjnevu6BTpzkfohSlo8_8KmtsHjs-9hFLUJuflBq87kEd0WJacHjOCnKujn-BUwhcgtJUpdSkUlStD9uMfoSiolhEItK_28qao0hoSBuvIR6zsIPzfAziaSiP2JrvaRYa5yFIARCxacyQbfrdg2OjaL5i26pyi9jgYNTUhZDRzC_eOdwQr-zre5BM3bBfpWujCdiMMJp64_Q_Avn6MxkeM6NS43n49uDfGYO9Ma4nZN19lis90_rvtJmJ-xlEjddcqVLThDaP8PcM7iCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltlOc1Bb1fXdob2QfJy3CgBo3Tj9rb0T2RgstqNR9txRNOAtZZXbPNtQgMzOxrjxHs1ImkMbqG2leXNcqw7eHv6DRFKukOFmmZMof1OOd7R0VHeBTysBUu4ULtWEMVRB9ptjOkXEaoSbGV4JJ37tYomkBtS5oKlGZTCV6zyWrJQaBV7SxYkOOHzmEZxjLUB3MNWQidvaJ7H8_4kpIiqtw1_yyahv6_wBsvMw1M-e2fjb_FNlqsq0pGFN56hhENJxqGeW0NTiyk1B60hcRh9MebP8r07426S_RFHUmvfDlmfWa1c920gut8LQg-1gNxMTtZFr728B2SVOvFbsrY73rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKFOfUsTxyMucNK7CxpAhUCBMBWHpbrXOZg6F6AWMHRXgDN4499p_K9cYKIeabcSfrdmoOWj1-_fq4XUSHsDJb_vufBI6RcImTlqrQpNuJZQxOrGPxzP5PFCCugCi9O5nRaIl7LaMNrHcl1dAIfa9PKTjcNasb6XXT6laGiXielrd-4cT0N0lesFUPt6O9aKkX0_ctuwI60_iKjxMBiGEG9zDQFnN4TEHt6rPz3OIqJjwVuTu_VSdf9PzVQnaIuA1AcN_DbYLWzgoGrPuSQ4a1NGqHiSQvELWykiRzxB_Yf7Ql_U_CHSmSsCWWoWvhAMo7Xa78FP4thubJ-KHeT-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O0u6PyJf7EGdjylEFaSGdVpXEo300SprcEKKGdrAwV4pVh6ITs55cIRSwJTVZyq8qtD03qylo7mqw2pAmbOGzp4IZ17TtczSNC-D6F27-tcueRDNQu2UnqrnH5HKXMXBFUAEKA4vFfOFp_bm1x-tTU24lOB2EQGzUF65w8FjDbtAtxH2C8cd1PzRxfjsA6CKX9rsGiw6w9Ls4hVZzHzbh46KbfeUGMKbPZ-F5kg_7CzJGdETTRq3RsaIPeSGjOEMm2RZLct5P3IiytfzxBB8burPjCovjCB18gEhSff2YzDJzOTM7dvfNSyt7mDcJsYML3f4dlcbCHBCVsQLh3ogOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ub-o5q8sDJjD7gP_YNOt9Yo17fPorgqft_3NOOBbq0HJ9vPYuYMLIlUcUF15VYT_0LXgwjrwEW0xS9j5bBUo3zVjZ38qSdmIQS6ZV5G060XOoI2yXUz1ByRZsDikUnlEK2oZCaDAuzDhEy8KC1-niubd4VeP7_02thncbdOcyhYP7EOzPQZdQQGIz7IYqj9KvMuwfFcWNlyqpEX10Tf65eBH0oGq43sK8GKBSnrmEUqD2zYjWdnbuw3RtsJIpyTiTV9DaKSiQ5o1ZjcjirxfEtxCxzR4lpnlHSqe4D5slKsNkhkqYMnjr_IwY_Sh8WvUZWHgno0UhlJKX7kFtM6kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=MPH9nFahM4YSbd7yFi4Vdo0p6jogESyryYSF5XblOkUgYmZUeHi9k8iSZP7X-hvhMqfFCbxiD6Atk2SlYdZ7wdSsyfZ3WdVn4GFlP2Vh7JFTSI8DNVTuEWNzPYaBsYpBmf_ePb_thX5VE9ODb8rLu8-WcpEkSai-mK_fPm0jGV6IRwJoLSUAMGbjYWZqQy48iMFaHzY3bKcYvK5mOzpjk_zf7S5XxplKHmAJkk7As4LEZJhDt-nMIeO6ZuQsYWwHYHBzsj4iaTfBpujHcWjZr48X68QBWp6iQV0LfYH4fkFRKNqq6V84NUDD3CbIJ_WlJQ3SP0xen6-PEoDgOsyWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=MPH9nFahM4YSbd7yFi4Vdo0p6jogESyryYSF5XblOkUgYmZUeHi9k8iSZP7X-hvhMqfFCbxiD6Atk2SlYdZ7wdSsyfZ3WdVn4GFlP2Vh7JFTSI8DNVTuEWNzPYaBsYpBmf_ePb_thX5VE9ODb8rLu8-WcpEkSai-mK_fPm0jGV6IRwJoLSUAMGbjYWZqQy48iMFaHzY3bKcYvK5mOzpjk_zf7S5XxplKHmAJkk7As4LEZJhDt-nMIeO6ZuQsYWwHYHBzsj4iaTfBpujHcWjZr48X68QBWp6iQV0LfYH4fkFRKNqq6V84NUDD3CbIJ_WlJQ3SP0xen6-PEoDgOsyWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EIaTN5Kx3fqaA6Qtmp4W8rAsw-wZMaXOJPPX3_dmo8k-OfYlpM66BK1EQOQuvK2sNDgSfPIoRfDqq7-hBOz92pS8NvkOhMXdlpydX5uwy9wirIrOoxGvSu2I0CI5MMpaew99B9xm1dMzHktTBggW5hMqeiVIurdw9Rpp5OFYjwvV994zH3-kHtLvlWBzzt6IwsVd8jbuAocW-p0jZETV_Cb4mQcI-uN2di3oQnEdOiPVCW6PotqBcvfBVWKe9jA_5RoMjVdyfiEo-LKHIlFkI8FrXDU1M2KXKfpjJMQJpZiKUwzY_7xMv8UEXxR0W6291F79ea5Ae9AcSazEf_ci0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eF2Mh7xPDkiaK5rwsRjX70iabeFX6wZ_Aarebdp1xtv3Pi2WM_JU7fTXxAYSI5ZugtKwQLE9My6ov7HmzvonfuMzh6arQS7JZZX_w2tMdEozKNlLKmeHtDtpg6DjDR16OPktPzE3tlDZr-3U8wgKfX1T6j9NWXvRPCZrh4ACmOqUYRCes1ImgKSQtVE4RcgnWgCjZJHMhyykcwsNHUmS13fpwcAOhwgNwgdWs9oXK8zBa615HNICrPZKaMqENgWePDC_YT02q_0K8uQcan5wdinUxn0F-9jJtyUeJRYKsNI-7K0OIbGjCdADXZNUTnE4Rdd0Gzbyb4BYT8_JJEpkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5sK32xZjBjRSy3r5OszgQ1iudiSt7pLMPipsSGGz1inW6kGF9p_8LqGlg039YWRGt6INIhbucGvGazji729PeOazi2qqW0gnoAWImUId-3JV8Nm4Cogh-VrLjj1kAtbE1gh9D4usZfzRPCjC2frYNKn13MWY9fF7p94PcxwUwTneuUWwZtshRaBCvBDGVThnYXbEupPOW_JGTrwCQ0zUMG0bzcT-E9oYizieVsrcrVBcW4NQjSQPHgHXoYXLoWZxiKgVOaif83PaIMXAEGcBsf1SEa1m5v1qlCkzvEoPzPUHT1Eu5Ukxum1qcyTCbbIE4wP4e1G1JBrNf0KczNRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCPAAbljK1VAHJs31tvv5r_x75HPPpqEhU2WUzPjSOU7EJmnt9Vh9Ki_yDFDmVnjJdbwU8tpriH0ifrnmGMbBeOB8ynQk1HTTN6Da_816dxrDGBd4TIFK7sRQm0NQy5abHDM8_DIgxa9MJiPG104J0v_2S4Sgn7tBkUMbgGhBl_TX6iTn1J1tBDYzgveNPwhCkTY1dx9tgpSVi6CvuomjFP-8VaUhLgeHotlAEcqamWAi2vxUsHqVl4nHKwNA-0euJS_r_xYE8P7J8AjtqOLVwBIZUnlhlkFVv2v7TGZXiyYFttnQpdCSCm73TpTx6j_86v0aNjYeDho_v28p8__Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6CjtwtMr5h9dn0H0iUkng040G1vv42L9xMURudkGMN9h0p4b88Q218bPGPCbQd0tyjWTXpn7wpMP9TnlmqqRTb0XsHM1HCGa99I9HjpNSxmRZQbOPtH1Hge4lRsiY_hMEAlX9tJgYQe5QuNbnuYIG9x-WUmXj-C7fOkHMhK2PybM4VzzJ6QFyTCVBBAhee1j72zIVSD5akTveo-zJDkZBXpJt1J27nQjv26y7K6fX9IgktpnRSQYqn8RA4gw5ldCNlH0yMPehDbpIX3FpuZ7c4Aomc2gSfdUZO_lZM6n6mt2z1w5ezlZv8k94aGnu04Z1zbxmeSWEnW5QuUpfbA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s_iNvFrW6PmWClGFg0g1nGsZGjpVpqtc9aisjqljfbB8--xjwAIUEqgznN91cP1F_1zf8JS5iyHpi_67RNTeCeeiGb6p00JLTqMEq1QrJoX9Zkn28dk4wXid4r7G1kypIBVc03sNWcym97UfbzvnYtT8sDEcmHIW9xwgyolas9Pn7KHJV96TXe5ln3HqLgbSJsiBnqxSBjRtF6kG3X6v2VxPB3EDnZHm4vHFC9b8IfFpQvD3RxVCRz2LWD98J2A8tpbwfCsqdg-5H6lr9c7ssGvHTUDdQxF2WIFWx6W6JHNnGJatbBg2u1IdLjJxnMyJfpktvPOWmPPggFc3Tfm_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ceQqcFkbwcLbJc320u2MVO7BE6lu7cL4GaQakB3v8B_4kvMyGLWp-dlfKoDHZyhA6GNTomp0j2X5RjSlv2VOup9Pm4uk0weAOXZdKgJRg_7MBVSC1-jX4bvPSBKOpmmwCMeQWLnIbj0ZSs5ESu7-vp6QcWhyfvhyovODk1SKCd2pApo0mSfLy5PEwDY30hPiZPp3nEQ2-KhtJ045PcdiBz4Ix9JxFV-YD-ptWzrAP6g_Mm-YSAwUGR5xtf-wp0qTX8Vc4QfCIjgQa6Sa-hKz5HU1cIQleKRf0q_lBUD-v1Se76Kig2IctZcv4_QtRejTmKVA-pYQbB0Twv9EvdmE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TiNimQsaPU4zxQvs7LDBPApI18VTES03f_Lq2u2usI-z62e8LIoq0JrNRcSOoJvXPsC6wH_rh4mvvvMCoEiPMCO6sc1GdhGloe_onlhf2cW62BSM6PqMpwQMnr_qAVDnNohX7bc4Q66p3RiVJMusuEQ7QDzkFj8rC2zulqF1qwaxbIc0W_baFPFkhcP6Cc3xTWcl_ZOwGcb8PlCwC4drPWc1KZ87C5Aq3G6XH3FzL51mmPl78pvIwekQ0LhmWD9i_wVaokoUD7v0uLzalEybjSlU1bo4Z6cuP_wrcavGYysk80k0EJoz4ru0q6tl85OqGhJ4bVjVyj1T_OnZFNHKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bjn6dLOj3qotFq6m2Y1aKsuBGwMmtBzjGbDPmksh6jayAf-94hH1_ZLrNS0si4i7bsEMiYY4Ry70WQMwSFG8tp7_qT-CAzm-WR6ysvanQKBDVFNXqOHp_WJe4B_YDB5UVslCAZ9pQBFU5D2T7qyPDhM8EhPhI4NayjtZXV_dxkPncCPyzaGI0GFynXRqlSwiO3IgCZrptyeaca-1sqt8FeE7ghIRgw5SWeUZVy97A-3U5kqexOfoTniCCFxeaM7_usf23r_lItJjqBRHpMZMcL84fqEoVrK7eWswOuAAV17ODhzXlWqh6OFTZHzSa43LIqj8FRcLxjIksmOrJ5bjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eKbuuZml0uaHbHpTgBloLznv0-RVlxOh7pqoWezwSyNTQYGE-oBjURD5X81QNJ22ZkQ2bZVIiaGLPGl6Qt2dmyMo9z_XMPhfVmi69ebBOcqUKEvfGtTQNhBRdNkRZHMf9ww2OnGDy9-uGsztYpna_qoHCwjQZKYjrL5Rwtw1fkwyXQjbEH4b8VcCK38C1VkSIyDLVV-HYHMlqZ7sn1uqCyySB7zfpmFeC8sBsFgZWQiv4LZ9JWNQJ8aijScLkjheI7Bn2ah2r8UZq2_u-MK2DLiWltFrplk2ecZtY3e_8fpAqHBkM3_QbgU4RRcDjq-qwf9SPq7xp6NFwC2J7ZAS-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWU9bMnWw5-Nu0V2C8A2hBN1WTrxyrEkB6Z2qDCGoRb1LKMi57d7-bn_CzyRcmtQXEh8JnpPFV1XnNj2zqoCAPDCg_3QAYPx5NWlJr1Rg-X8cPdv8WIPHo-0ISxN8Z7VbWtHcgjX6Upw_cif-oV0PDqwHKavP1Ee3sMRPHcROE5agiljvIEBeV4TDINAl2I1HXO0QBcxYKIlmF2hCodAv5QMFM1xAtURmI-4SLSjJK8LYsew3dI_ekgErMvL07vMKwjmHBEr5pN7hAKTIDS_CcrM4_0CmR_Kz2vU_Nlac_5NbYtu6HEgJXqhu9Vf3TtR3gHp7zyn1cWstjUnIn-nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=AAtETv3rz0Kh30bH_hNiLjY3o786NVynPKMFHeB2gfp9Q0IEMIy86Cnhp2BkdrXrYMK6bmzBQFNvp25lG8odV7j-xx1akAXpF75iRu0gxwVj4I7iBsypKhpV4EdGGRyTyDSNwx3GNSOuVDf8bqHOFsGqUtt2A7NMc6JUy5tEbJqjk3_JCKFgS7GaNNB-iZ--M4E0hobaiu021-pKGvu0NZMcMVfslgUTv8Xb_rRKa_yzHQCBI0feYz97WJPhfaFzcdytKUM1IHX1w0u6raYrCe95IIpzZJeFZ0HGk7Du3DRlY6uSkRDGamFOUGCnRFYYQTY6l2CY5ww2CbSIA8KXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=AAtETv3rz0Kh30bH_hNiLjY3o786NVynPKMFHeB2gfp9Q0IEMIy86Cnhp2BkdrXrYMK6bmzBQFNvp25lG8odV7j-xx1akAXpF75iRu0gxwVj4I7iBsypKhpV4EdGGRyTyDSNwx3GNSOuVDf8bqHOFsGqUtt2A7NMc6JUy5tEbJqjk3_JCKFgS7GaNNB-iZ--M4E0hobaiu021-pKGvu0NZMcMVfslgUTv8Xb_rRKa_yzHQCBI0feYz97WJPhfaFzcdytKUM1IHX1w0u6raYrCe95IIpzZJeFZ0HGk7Du3DRlY6uSkRDGamFOUGCnRFYYQTY6l2CY5ww2CbSIA8KXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jSr5vAfzFpKo5_jDRZbIccjOfv18RcVKajE6f1z2jo8Muw-KChgbHTmlPiR_HRoXeLx3nMbPwDGoMmf-3I95ODKcy7BoB-E_qCecKfkCENm_CZdBIXbQWirfTSs-2esZU0dt668uwsXvQ7CqOvEahCQvBwwZdFhG7vBQ_g6AbuHifRk-9Ka9OcY-QiyzgODCaSAYnO6XpxAl1WpgmOzrXH1khC9hB8v5UzKcdpARde4f0OHPKcnljc6SGEfCKbQlxW9pRWiYxLWD26gCTPYRvA-IdXLayD6E_4i2J-RTylh-cNpN8oqIL7DWLs8YDrBKmf8hi-j2d8tyeEvnarGJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TuW1vAH5OshfbGp2gZYydDOAjGzlg6MFuf6_tW206YCDIPDjQTSXRLPbQsyaA5FSnd0nDw67BE5JJszCU-Tz2LceeI_LiiPPuPbPZbyhYkFiMxNnWvwPNNASWDtPxFa2IfWGGwrBAPO6EuuXUXv66crleEtUwZ30u3basKA-ZtvT1wQOBZQQDb865NwH7KuyVYfKIqe9FO3c6v4EoIHlBtuB2awpDYrZbAdzGUAIkTMs4ptJujEIu_ArdFqnqAxjTSmuloTGnvVECc2nRk7tB4ZXPwmH1XLXA3_B6_OpGrfNGmNggFlOWgzhICAP-t5VV2ef5SxayVJPTgh5wQK_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uO6yJq9WMyU3PEFy0ZDOxO20MNCC2uNgJwjG-cMuWr-uvv-zFHUWa-zbCGQFWtvmcR2BThK9-Wy3XsRC7p1nHS30TKf2VuVtj3Nn1723jE6UenDm1sW5q6phjR4RO9l571G6y9tZNc6fBsEEiRshfeSe6P-DsK0ZsvC63tZnPnF804JzKNVSI1SsDwXwDSKytCQ9rZAiUYTf2psk0aWhRlD0rJvb0D-wnSjMYFmglbWoHwK7HtPxmRfikhrqTlxx_XAV6IeIjw5oYHjYKMlychSUaCxrt6-hz-nH2ZNwkDV5qAY8sDBk45k_ZPCkfzFOo8Nx7lDR4Yk9EZxgeuFrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ju6GHSpbOBgsS0ndKC3n41UhNCLk4ZDTKFaLiyFgFbkov6RHD-RuvifvKd0bssxTH27Yj0xkh_rXutq_F_CfP5FWjbR4v9JXTtlq-k7rQlOWePrqYvS_F_py_mSTbc-ng5Br-SnaZbqiBTKDq4oDE9i-rPWoqJ0b8A5077TmUdU3x07Ce-9xOXli6OJsxGmLSejz8abIcCzhZYkAsLvuXAqaBwtxlWrfyx6nLYZRizXs4OTW4lzRQojcwmGgmQi-MfA6Q0Ah9Ydwj6AtotyXvYSZo5_Zo_MtZIbq360pux2Q6qhG-ymQKBGimqxyaGU7-y1mak3DSislQ303hWDkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQla4DEvYKGAv3MK4ZUTFf8fv9Dn6qdxL5npmUvp66Y-eXZQOKs5jgPCpH2xx3e3oJaS6tQjB_QrkCQQkgB1UB6wUXQGe4PLasPX0QF9AtNCcEN5eJ39QtFbCMIq7kDZme9v5OCHEArFuEAwbVq0lRe4aNW-ZeK6dE65ucDThdZFvW1SjkfDs1iDek8eY84r0-1MQJlWyKGMBEXNUxnSN-JWXNcj0g6EJD5Ka-xS6u4-FmYP48gSI0wELmKb_x_u_a-FE_OKAnIPFd8f2YwDNUqa5lGvB5k9XmGi7_AHG6kTT9A4iHZa4WFeC6-kVRv6P5m7To2I9A2-ybABHOSm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-JtwhYfO0ZRNAkWV9qutt1r5cpY0uf4kho6htPQib-0eZ2b2T2uyZ_3vBZ4Q0Yrwj5WifJL06LnfBHVs721w1WeaFmD_MClEI-UDCe6rdo7EQh-CKMyJ7yJYAvt6EsSMVGSE5iGWRdaboxcNCuC8cJS2J8NgOW6CH9SCORpJUVRCzDp_n-eMkFk6JkaBTQP3vhTf95grEJojCzCpFzEW5Bk6n7GL382YkMKmjfVg3J7kngH7UAVYYZICwST3qBOosvhlYjjW7xlYPvrafrwSPTrqMIUYz7BjQQHke6zsJPcqOAZr-4WplC7ia7r8PL72dHOYvfGosuKrB7tGKJ4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPe_fEP72Izn4JRge9TPzcGsaEfIxmEa5I0gDUIbvNzU37Tmv503x4busrY-S2VzgRX8xUF-QJa4EIbwAXJORw4SD8KFeD4cgnX83wBpbB5AqEiLJKMFexh5jHcOnNG2VSXC0scW2LkqtcQh3Y1DsAN_xvOptlW3UCTjWFdIlKTMUPmyEPjuGLKhzrY5kriyPnS8XQy5eJDGNmvKAHAdTPGrEc06TbZKfhtyd8Ln0JHTV8OA6FTjzH7SJcIj5WkCYAgUvH7p3hrydEK-tU9mPdoryM-UT2DJXgkvEfyZVXtCcz1nun46wTJNfTQ3Wb_RuwZJceC0pX0Ckxthgayykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OcIHLvxJRg8WDLfxsUzRY4ZwoER7YU4_mQOj2maWld6d6Z9PNM9PQ4dxE3mFwGPAJZCHCDrJtSC8vUOJnQdmDCG8Ni-TJ0Po27DIpl9qzBFJXqDGk2FzF17LoqEXLdEiFd5pSawVdC1fpT7MPS4yc0osTWZg9R6yljM0Eddstn27cWoS_XNT2FwIfeNhd1qdYkS-BiD01_ggyeB6eTAnjXF5bcQ62gD-FfEhs6OnhZ5sfjUkQusT2Xr8fzXw-xOgTIyiSgOR_vSr3KtDDO0AoZB8DEo2l01_HNn89soaYNZhtsGat7ITjz19WSrpNoOvdo_Aj0ePre2XX1Yx6ofwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LkhTrWDWyF0pM1VEIw3LjQGNwxxY3bASZcx4DwX9O7X0aFG5TcLZ0w-t6fjZ1pXsY9WkV1XyngwdcEtj7G5Mc0oCLcpvyIyv5Ex21ZNDAVOAojRrVBoedW8cGEDc3edV2Ch-lvhdxpkhoR2E6Y6oeMnWIcqSHzuH4DvSM6xUt8_njpj4q77CRjJ-II5QyU7zA36ea-F6XdkGqGtMr682S1zInz2wEEKx6pEv680pVdIfQ69jjyau4yDVM87wy7u8dPAPh9ZhQQc_X8YMH3sD2Dh7VinmEzbDZBffAzyJFDIeKHrfxmUZrdEpF13s4Seb2jDweAwxGSvfdHrV43qQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YlK2UajiaL9vum1HbkSWxTVqkZXWvRZEL4k4zhkPEM4dg2FA0QRWj0DqSrX8BTX18xDANrnABRsvyQUbYUOTF7OVbvBUT-QyZ-S2vpR5jx7_nIpJlpgNLzvRThGxc07BwH_lx0aF5zHI8atGuRSIFRUcsf2Pt7oAMp62Mt1z1J-1iQ6xemZR0Cn20qznuOO3g1M6BEexqCgksFv-OasosyvOUy48EvE8QFgqNdMmcLBzF8e6blkLH415xjQt2jYReMRzmkj3IO3ZAPMnHmhl3s79jpTg4YugYY1tc4QlZMakNDNy-8XzUTo6nl2f_67lOZ3bfoXDnxPZYDbTTpbhAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W7ohCFyeJq0cpZJER5pqllcGCY-0W2vg5UDLcXCEjygjssd0lXNXpYDeLVBzxYlc1vTCYFUcwvWwCrMFgdNgrKPx_jc5g2xkOghXH6d32LjeR6ZI40XlFxBs-MMkZewdcHolkLTCx_FJ5K8DxDIgZZ8al3ncJk34hpeYIb2C2kPFAHK5LvnpDn54gOfSGLYbDqpSw93qiY7uYjSjoqOwvI2fbrKObTyLXV9ZpSPWGQqV3bpLan9ItLMbVNTuWKkcE4MtB7dfKFUhcl6LSmfv7Pj-W6oDPBqUuDdyTqP3azbWpuIx4IQEEaLOgi-PAlyidE-ocQUHHg58i3uIORHKyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Libl6c3f4lCiDnrRKwC9odLOl12kN5g0zMkc4dU0Z37FfdkXQT_n8X5tR7C8hj-HDI82WKuoJRIzw2jAZXs98ox6lQNt7VxFPVIlCjD08viigeG1fp5cUgJJqc_Z46KN7JWuACFPR-LeuZ5sRYvOaWuDP4OW5R_bVeWKIsCqv86PpL_XIGEta2B2bV1tzbl6COEoU4pF7yStmx4UE-Tv3DctwkdzDmHvCU0X26lOvkarx-CEnubWJWXTfihQS91nS2gyX9B2TXD6wVKaWQdXtFH4UxWNDbqUrRFoFNFj9cc3WWIjoS8wxQWfA15-ckxy5-g5e448Wfx0LwobsNtjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_RNp3SgacONkDtLpxI1wEmYaFB-1ZUxBw5_ewzIGXFqBLqmaIGxFx_FEIIOn6mEK5tpJ_-_wP64YWjYtOD2EoBBCHmfrfM3iuuKZd9FVf9baVL42zYRPnOLhsQW_jJxF1CT2kvtO9K8vKw8XBl8CTZSYyyfnIUBCg-2yPomZwB5tm9DNBE7i2RgJ32eLKziuxOTH2Co6xJ7DMfGcZsfEkl8Znt23skgrDyYYQpW5mMU0FPIMzNmY9YnZs03v8VeyLXSaW_WzWXxzRo_zky982hTfvIzA6P2VeRVwtRYw-7kaAOSDhj5qRQhCH8AWp1lkfRFo2r4F02K0qUIsyWbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPjVqWr_UR9TUOUmxBzWIbHBUTWDwKxYddG_j7ePvdINJNML4Ezqf9kqLDPupfgqui_MudPIQubAqAtDqEvuvhDMZd8lBpozXzQSO0dZ1VsnOz88p2MjvzgWUkb8EJRgZ_UTJBAt6a36eSjfNQvwkhIVrMscueZbpn2B6EaSvpmNAWo44TE5MCoVihSjtKcK3RMNukY5oqPqTl5qeVDAiIERrB8c4d3dUNdb6eHS4qW6CsAWYs3hR5MpHHz12ckvS5jvYuMq98P3dGHgNV8xFv2Cb0mC3z788KJFXaZv0VrlvWt_WepMHeoi3cVYDRP3da7_yf2GDb5GUAIJQfWjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O3q9T7hGceNxHDk51DbVDNtMOfwz8OJzI3UjpfJ-4n1U2BXioMoKsZsYMgZbTQhW20RfvB1AImV7dudDBuXflTz5bljYxMwpsn2TIIa3aHFId5yKhYwET8RzjHiStkgMQOV7VM0alqA1vGTE1LhtJCWRCaN1vS-3wwl0xvI9yIP49gOTaOU4F852G-04vmyR1EKjhcaD-EJanwxQrIwo-wRzxw4RYHrd-r3WkdIr7QK6ndkJc_0JMrW7W48soFNYiy-dQpRyFk7dozxAhwG9DsI4YBroAue8ecXDQ73t9X6m5dZt85OXmVhNgpV2MaHDmBhzhnWbweUW0PQwEQcGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aKLZZzDlURWhxHSfBPE7srjsM4AILEjdoLRvyL1xkOWBDzg3fGb2K085rXoTv9QwAxjtwizGC_BS7azApD-6NlBDcwmvLUw6XJr15lSHkkbcLl8xxWumhr_WoOSHWcsRbRozUM0IrELFMJBeJ_5BdiA1DmnzjgNQQoU-9LgqTjF1Y5fZ3IUXv3AA2rgzYFZ7HLPsCg-I0HIxEB2s9XUQBBSrniSXx8d4uoS8YTs9UJ7acAepnEtVZ1qgXMe9V_RV26_ORzpz1ACWneiVBBhsO23GkrEbynnJ1SOme3jQ-nUpcZWaQzKrobztB5uVlz0AeuKfTGb6jjmctbZ1ivfX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eX5vQqLOWGMe0bvlZhylQGE21a5ooux0xupRPjcOT4VFlkeaaVRAa6zI2Hw85E2SZ5xIbqFCIAgrxxUnt1WPbNdbVpf8QS73-Tm5IoZmDSAo7ZeXfvRGX3MrwwFdhIOfj37wlf5XuLnyAQl5psMsatksUOU8HLLw9or-SSGr_tUZ3yMPlWrf5ydJp8wnYfwvLqNiCqLdlU5lA-b1UDBN_kh98bTkdWwkQ5xZaZh3znynCh2pJ2eiMoNR7MLxIL0FEEH33fxi4WHuliu9TuBSABM5j9ChZSkKqneONl3WMS1yfCVCofg_Acf1hy08scoQ7JFcVaaxCEJN-HZWuP1e0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iMzoCZiJCjw44JLIdL5UhGIgOcyKdiXDcsgSdwKi_ARz3CzuM480UcB2lXiZDCGw7J_x57XlsY5RsfIqGHVKgQ8-ppAmpet7AhxyzNmhY2L5DJFFy4rl-uj4ESaTJWkgazFkK29KP6UxETHcZxRxmcWSKmBIu22svJ0mjVpfCHfcfWSP991swKJFEHMFwYAe7_0_mzQU1puEmSfdlVHYQHMmDOhSKtv47ycAmzUmMqTRyTamaxj3a6ZS65to1tmtHEpmCN1ro4d5Ol9ilfKfKWtxSb0TH8P0j86tBr5ykdMCaz2nxVWJwG4gAgi3bOZSoK1N6MnXKmfQ04BeSFQFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c1tNucD587lJsXW9Xm8tvvZAwDDFi5pBmz-javrEKO9h6rOTr07XXbpDr8QJlCAJJvqhekkv2XmKQKbtlb6olPf2_aj_BKwSqTnx9AjmFweOj24w78Xgp381i99K7WgP_dIU_4lTAe1_t8FWGnD0dPtfJUMMq3dlL3T6MspZ2EYsvcNkEOfZGTp9j-LpYPCjJdv3zeNIDuYGNYTBCMY7DdxHnwGCNdfkfGYEYUiTtyqG88TvH-gebLqzyN52-LZZEtKAMaNriEtgWk6-egGOBiJ8xA-XcNB0uHTC7s77AkDE8zbQOvYIr7uMbjuaYOaix71437apzoeCCYrIk7Npcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EveKBh1BbRqTWNB8Mu880RzeTlo7jU7ZC1iYNWmWqZ2q1Xg3w697SvelL3pWb_L7DPSzA80xxjzi8bF9F_dLgy1QmEck1Ju-sFgCZJIHDUzJnKVCPf0BEHzidckF1j3lCAtdB8zEUHAQNqTScygoBdfiQk7uN8gxRKbpxjdb4RuzIlAS3kW1HdAc-Z_uMgaStkCS3wByJmIu2S1jmQcIUt22jFGxWGT4ELWVaNc0nHmLBKuHkgQBRtEDT9bIw0Tn_WX6Q_dDeuNFkxpmsnD67GaHz0tB8x1ZM4CjlanwsK_06w-zj2sIr-Sqt_eGh_bBDlTJL4XVAdL5zorDtfHmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slLz3MD0TF-eIQhrDUw6PPp-Y1Oy2KIobAiV664q2wCPoSp8LxKlo8Z_ZXxgM0wI12ir2DVnI_3dmYCzMaLZbPR7OhrIyrmVyabJowPwRGxruTYWYYMEHAqXuvLZzhNROXB8kPzlrWexejkKy6UPDvkUCyzL4_MNmIM8xikG9-IUFo9LQCA_hvIFMI2WGD1ixlWt0zhdR3RQ0QSkMUI8_4oSo87F6rFhfWIhcFMs5rnPjnc-9XqsZfnE5MbkB1ftMSUO8yw7bvScpTHdMorCeVzTiwKO5YIhr0FaMjZk_kluy20LeLvdXShNAxjTyQspWPF1zfBKdTVSSQlJkSTisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibJ6UY84fkMACSPIoAnxVRXQTzAhX_W3AuH6KpnUxewxqBXE8weiFBY0te-_sraclf-60zacBR838TZcqQXeiG_-yUiwnnNRmcVW-ABiV5sKHhaDQupavYoAfAs5e06eMSeUahTzgFkNyMgiiBvREnX1x0w5t0JXtzE4R7G35emOAYqbJTJ2SLuekFp577TmflCOMx0G9LtmTiYBDcvbqnYg_pTH76g6Mxs63347z7CEDmeukuZNN7XUcF5Ng_DZATQvak8n2MdVnZuGBwoA_XIAVe-7gOs_MG_2F54RTqglERoDy7RQUd5kA74tIjhWVg1LqvSgIZAqQQBLeYSeZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j2V1Hu0-WTw2GICnwQKA_tPpf_kOvqWMyy_1RvYecTw96rUP5Q0epLxdZi973dhOEYiKDTcZrQ-k3Otg-wjMKxjZfIU5OA7F0-Ickl8HWVgbISfUQoK43a6zFvST9uSGnxxKD9UbeE6Noz5huanmNFT0an2p6r2MdXVQictuwm6_ZZbCp9e0Xqttvgs0ZHL57VO3llnmmdtaUUEBACrUwBeCrqz6J-jYFlVU0RO6wU5xbNLZCaVBkXMlxA-Krk85z1RS1FNnaEmgGkjaPzv2jZoR08qjxvxt5ahd6kuqvo5UlJKshTjAGViDVGBCSUcddd8AhnWie3rJXeD9njm98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3BxeIqjnITjDqJuAxIW0fU18P9rhpRdEyQ3sxJjRMVuLt4YnZcpVI9VPc7444jTIvom43cPIGAzeION1mJxE1-RXV_pXCizwOVWiW1-zOGJ2y28lkMP050phPRYp2Z1ICCKbG7tM50_ff5M_gRAtWjS9O7jk6CqQyDG-SjVP7GoohxVu2MJ6giclj6AScWTbbCFKgULm34-M6m4dM21nEKCbXWMrXBdpqxLOwIq6YIYg4ioT7s_sBjGjR0CWlVG99oj_nFxsj57NBqfdTfuKn0QifuOISk9EdZ8ydjALIyxPUHGQap7eorz48xZBXrk5jDCHRb12WRxRkgOmovf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0Wmo385-Qln2hTqi2otFfhdE_6_q-9rpEUuCbX9Fsjzo0irwcHO8LBimGkFUz1V90astuVukGDq1PFacfoMS6sc3BovFaxRHu1-ZInZ-DUFPMaNqB8PEqJnCVog2p3wCi6wd_aHEOu_MhLTMdtAq4-J1T6m2HByvSkwpEuGuXyBH3eGazAP9icqZJcEkBWdoljiF6vuKlKrZJ1anKhJL6D8ahgEfp9mf4OXtmLM-IadScLy5r6sXW1pSVSF2c9DacozOigJHgMghHZYO9zM57Kk-_QDvNW18F_lsUXNkIbMFgMAc7clSKFQCHNtRUSFeNhCXIYyiosO8-DKFoFhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AiwPhwp336zTTI78z2grb7MdNoiAvLuq0Dn244WbQd7Uk48ErSQCp7xlMInlHcy8tiiAUkwoAXIkTSCiGGb1gwG4K6x18DAW3X-v2UwoGmiKBJNAyr5I2Jn7Oj34ilVUpH78KsTjrpwJ-3vXWDVXFcoASLGneIBvDXA2IhJ-0epo9gPBtJujbSElOSiCWhf-gOWJDKXoenH4ytGBuOGxCRhsNn-XgUPUzxc7Svw9uY2bZigJIFj7oGZKENbUjkxLYw8TDvcmeBmacyclwBJ7WmBz0o6_lwzMjARo-92avVYJI2jGEOHNRDPQ_MXOaQmzwPDIv3Lsbdhk24vtRV173A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ta0Z-5PkmCNTjaci18RXKymJWLMSZMN4IqwcqPJJDeOc-hUttUIR24N-J_7nS_XJMc3hVd-oxB3N2OnVfWWgsMawwo7ld_wAwaA7biiTZetZeRDts9reSUtmE2DSLZhVjVuxV3o85254DuX2r2DgVkk9h9gt63GRdzWmeYeSGfNNt48Wk4ZUADpaQyqgE9iHaQIbJK6CTS7tPs1GPDnU0B7S6IQ9ureRbv4v51iqTWM0cU0Oe8c0Bt49QtMNYZMfIfKmZyjhnYONc01WcdF5nbsyfYomD1GBBoXuXqWOpaBRA48odMULjuqKno9IhAB_LNUGWl4wVm0RC9m6UaqdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MATzErPpciLh4spDy-H17qE4TeeTaHC3jIRkcbnwIpZ79HcZiiGulCa0_isxlmE2gmvO4SBljO6kJXTboOuGMcJU931yug6Et2SvuOormyhi4SBrLq9Tg3D6-3BnNroA5ikiABTUnubgqXJNpArO8-AOZWF5HukQGI3r7lYd9ZlVl4xL1SJdJNZeD4z9liXnzX12GmnsN3bgnncDjC2csy2jNB0bt4mu-dAhsLh2oAcddG57MdiqelY308J9B-GX2IJj3CsgJuk3exXyG9p8Lm07GnvKXwMyFyAkr9OALTrwjmf4qlbgP7AbT7GmaWGNp6_bD-wowOwjWCIuyQklsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vbNdQ1vdjoaa3Ol8AJZoe9hFpjZ5pxRtZVFBBTLPR9bE7Ya1R_5Gwk8zy-XeJ8y-ADPjsxg7Zm0juxoTsaH8GOz4b6OaYCKiWNeYlBSEvqmOr1UZx4hLbywJ80TrZHTIivBRnZ0H4eDwnymXlmydQ36JBVJdBhpi_N_IFakvCXxm2OP8S20RZClhlyAr6fbXCs0-kRMtOz9NfgdjO1Um6ZouOotV78pobvOMqF5q_pt_utTVAQYa5ndITP4UOETRh6R1AjafuparLHbjCJo8E9p1KIoGSHYP54Yo1nsD1dyDsnUM3AUTRuOmpguU2oRtMIi4f2I91ImcqQmiKwIA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kBkP6l9a5otP0oSOMGhq5gTDcAsmf7hGfWlHD-rKEMIHhk8t6HRdKLjRxQFk2o0eTVNDwuLb3ys7KUejTSnZrMBZGslMJHfdr9hQxsBWEF1ZC2NcUJeD9peKlHzPLfzvt-xNvCAE5bSMkpbWAOJQWdpJkx-t7gShhVCxkGDMCYbWn2MB-OmD4nel05JDtfq8pkBzS0_gdDSlmBBVVB0iUU_cN8llo2XxVi5aWPPmHK7Hxu6RVW_gTvwhF5JeU2KQkDTKGWQp6kDWibCZr7Yroa78LFVS6QjEm2_J4aeKNUIWW9B9ylhzB5pMwxwXMfVIXmOzQuenBPbjLEmZtykPOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/az1dq0DdZonkDgPMuKhejZQRKWPJaq0D_bUx7uCF7l6gBg6_8L1hFb44_xP8pGZ4QKyV2HljMrerai2jRzBWUTaknQRTWaGYiML0krrQS0cJJJb8Qj4bf7U0xpPaUwltrO98zJNtT_icX5Zxwuz3m8u0WxA3Pim9ndyrnQEQZwNGcP4wUhMcOaSYTren-DHOECAk9w-LkGTiaRu5qCuvpuVj5SAkr9z9urrJ8dv7PUEXEcWp-ocanf0MgQwhI3aV-974xqwq93Xp_D0rP8JOFC15xDoMYYOEcRG6bwkv2MnyCBgzUhLT2un_h_EAMgIQoL3fG4I65gVM7wBLU2XqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXH4v3i50YLoYAecC9l0cYuB16P2BU0D_ReV8m2KrgvkwH7QVseZlHQiI2w-wq9e0OD3jGi31hQI_rkzfNtPsWoqu5B9JmGtdMueGGs4fuqMwYDgOKrtu5mdV5QN-bsXLV3m_vhPhxiJPLwgFhHkO7ucqxfpTrWKesdmiCfAtBWCbeRBf-UDa-xzcWulLw3mi8IbWT0Jteaf5V2FSeKjgoZXafNQnnF8wCxh3aHt5FOAq-dat8V0B1kPirgWM99-o_pRZ5QxJfDGYhIyuN5PO64sw2Qk6hnCuvZJB5XG9icaCYk5FxPKDqFcj3qPoImLF6BDoxax44-t1OrDw4AFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUBNTl50bQQT8kyNekT14Yntd9BeUdsdgnJalCukzGJuZtqimq4k786yECcr8xC85Jhljt4emydNu6wGClk7Azs_3xvL41ymNAwB8dswg7iChTujOktot7tWdbVRKBWNcI4q8LTnxNhpIajU-uwoOUB33JS4mqbNEELtpYrWW7ykC5LkS2xL6BcAoVll8afzMGutMOYcC3IPsvVo6ghMa5bDBKje9PRh3kHUvNnXcchEOpNwRWldKhqtYDrZtP8haa5lNiSqNrtpW-EPHo92WKeG9NeBUJm2Ngm530Hi1J_REQ_1mfbAD0O7cyxyLwl9iwpFmbBg1kMelahoVssC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
