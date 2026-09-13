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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KGPqOw6uShsFRJrxlojbGPqcLCy-wP0VTy19Y7W-GWbX7vSqAj5DpZmx4vX3DwsBV3i1neHk2FQkhMqRNWyKv1vPEgx4ojJuwS0a2dWU9W07K65nuQaDAIWaJceETzB8o5UXuuGpQ4hCXwlCm8ou1S0ANmT12nKHyvrn1W2Bq7e0QgtFUCabIcy1W3BoS5mEQqGwpan_4sLDafW4OSQIg5W1xcsUvsBUcvr_qIkts_L_DWDdHWG21BUV_ReBel4iAVakgV_0hheRXNNeNOTpK_A2iMCtvG7ggdoJRYBWMsGWJnNThn_0j2qLM0AUoMhV2E2V6hmmgFT9Wj46YQMj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kbd4RVa70-jTIRFepXPcUKcT2FwXXd4X_UEtupNTyzytEg2rFyJZ1SrNVZ0zHdKrn_AGwFvBRjPJYtZOkXsmcr7cXYv7wK3r0UAiXRRPqcykZSEowKXvPQz0BjWkQ9IocaYpfudOa6wW0VxP74uxTRwtMCY2s2an26JFKz3w1gnTURmKWF9OJtc8lCd7W2b51fE2uWu8b_w1lz7OV86BZf2S2ylPWqYH3ZtDzYZ1KEbUhUA8sojccs7TYu2o6-gBzJBtl7XgY42C9KbTIMbvMIqaAz2WtRoOgvMRoDQ8R9_jm0VsfsQx67gnpVGJu7B-wpCapd0EgOdRLIsDcBNVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VuGhCToYb2GnlrYZuZbtnu5TqnOcsSJ-UpW7Md5SnYATIrsnbrhYVkap6Cawehsv-cUirl1_gmBfNx-oP2ge6h0OkZeYTsdX2m-qLHjkh7Bh2GkXIofyJV1Xu5nB9uRHudV8g7x7213HynVGC5Zl7V_eL5lczGfgu3SOczjRJhMASu7WbA6H7qhjMtqv-pHuRjgEhSsYVK6Hoz7f39cFykhC3ShL_Bm5olULEUyUqIrX1XadvZy_cyvjLeF1cxtwSTYWWwHoQbJgOOtfjGp0eCJ_9vJPwS19gfHK8wMazS0Lp6wObwC763iuVCjNsTni27CmjJL4AFAdQlIK4w4OQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prym-nfumx8oBr0NOPxEcl70J9OGYuvT52izPLsNAegTL_AT5a_kFmtOHo2WcPPsbY6Surk9aBZ-1GrwaKPlGCuee96oD6uWpkm7bqz829V5C9hcnMQCkt9KPFlqbzN1wqZEN8iAmAfAocUpt3Ow7StKQIpNnHZlyXD4B9T7e-trpdPMqVT4x0yQ1BsIWwpbxVTUZ-LdmuALPFvfYow-_bxYhFrZv3jCo0_b2kepygSaxfsHsn9Waj2NkuR_GdsrVcP7s4Mo4xQ2H3pM_ma1UqwQeK1pWWsa06xxMnWETDHPo_mPBWcih_qgfEt4482a5_cLCv2qzKf-cDZE085PbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX4UQRnCCqqAie5PLmbK_GUl2C9skBZ_BMQ5JLXlyjzUc9tnuXEAX_G-ioqreDsWgNEXGHUkzQZwNbvXlF4ejl2aRbNWRftHGCddJbu1WkqPibmOOVFWGIKZPvatNhURDDeQYu2LYuMfHC9bZ6F-Q7nog91ho1L1ApOkphS4QR9sxU7ZhK-OIPvBqoBXoNXIwtQxhwDXZ7EMoN-x6h0UY-QeRWg1cOtTH-jZ8bXt8Z4-ihekQ98cUwyFfNt4cgC4JeIdWj2SdoeuJke0XP2RDPuaK-p9aPdSGB2gDRqpv0gILxjoxzHui6JBUQhs-siGv6dk-s6RdVW5VN6KUNkWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BVeUmy1dwwILXwMpuqVs0hWTeWAOTp-hRaUt0L_aY_Vjn-WVp0ADZHngzIC1YNPhhfJ-HScPwCKeJ0BT8u8NLsqufg7mRg8CuGbFRhjLcVIVlbW1FLm9DQ5sQIQZbUK0MjDoiJoQ7CCfXMMB_0ByyWC2g9kXfUB8nL7BXubV30inQpZx30MMs8ATnXLhocZDiRx0ZeZif4WYdqBOw1bVB_BOjadygSYYotBqZbJsmbbunVOwmGbPgptf9EzQ7XR8pbd8A6Daz5-JaPp7AvEXpUZ6Ifj23LYtRhkrWwBCAiCK5zQ-QPufxVl3twuDsXP1mGayvPdTiM9Mi8SsUTMJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C2KNOu4_l1fxs3aDDXYDAtb5tA-1W8kLtN1t4Excp8x9UTgr2v6_fItn4oesJE9FTVjNKyy3kFPzhQlqL6r6_aIYj23ZyjuX82GH2uT8jgmkzh1_bYPIrxMBaul3BKKpiBibvdWxNvoXj1D0BXEQk7WsE8yoi4uncI2u3GqHznWWjSeCxn_ilhzNaVWf5w8U6mWbkGRJHwbSeZoh6ZsscEtaFfletvq6EASBvJwjPdiIpwWJ7pnoL1aaQXL6dSDFiMAM754RZqHbyo3MTbXEEo33RWwlb-6KIgPRkqWXtCl9H79iYuMJx6VemSiCKHd6Aij3hEhcnzcSQbMOPYzAKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkE1kn3ocjB99XrtY6REN37drLLc8dkq_7xf4cy-kMLBF92KbcnYl6flhps20b8r0q9sG-WxsiONQHMa51tOKeXywNhMjwVDkiTKVBXnhH3y_5ZxBuI6FTGJsiSUODgAynfCWrHxbb-aw4gRMeR8WNhbQzH44sBDGZ4LUpqgRzqxkkNrXUrscVQXbIH-UM3lOd2FOEEmPkxsA2p_jb83oUXJXB6KcZr6T1WtGKUwZuuXY3vNwoNTLZbg_xIzN6iv3_OBt7d3Wnl8y7S--nmm5ivhkkf-G_tlZWtjwC0HvWCb86pFFNChWCjoeTOcyW6N_bVXKtCvTKvXx7fvc25OzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTMwkeshLL6e3VNJQUn2ERe2PvyXOMgiHmsZBsyUT6MgHQrvYSajYvtLCKvQE3uQOkFERHtkQfwK8Z6Gf-cFwO4FSlKSPtvrJiiKjum9XzHiE34tUc-9u9MM_yNUKrbkI_MrKLRTSXyd7l50YoVDqMLWx5DEELxxs4suywp6DqlALH55sW_KNhQ97LL6DEeemibq35s64e9z7FLbTC98irDttsU0zvlIfTt2-c5lObvxzoFIpQBs7kPzmzEBYDWOUhZl7XqVycpTIIJgly5LzSRWMhDT4wTpw2yhF_3v_SUs_8jkZ_lP6VjJKYXXI3AyieF6Z5QyDTQuWzn0p1X-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JXa28ufWdDPiV2YORbYJU-ybcsP_yaTEddlbRi7TovOthdtPvlGRnnwZjPEXDqVgZuqGHuOS4UyRZ-THOnX0ZngxwbE0_6tgOWu3Yb2I9wgOXOLD2e_RkWRVcovkCcCjaZwfYOD7kj7FZb5zIq7nX9asw3g74TdpWTkHDI_-SxtyHTzXn-a07KwjUn0-KRFwTWwj3ivZYsamTfPi8ZdH_qWvkPOHcrnyxsnlTQfL4Id9FFr7PBwm1zty35sjipBCSdgaKSfLinQUwaZ71qL8jn0TCdRGLGArJGoPEh1-KIm9_UlX9IpBk0ku8RSt1UJK2qg1QJT0SIeDJMxLKJRSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fXlrJLPZeRUbRigtYqgr3BkVBw7BFleAAoksJgjAvzQm4aViyRk5pDHqfj0dRO3zB942Kx099lYi0EcednRj7I_BUds6LR-wPyZUln0Q5mCDhad88_lCr4J6RLa5Dunp7pOaiFZ6QEVND1uJ6CZycjL0yz5Y0crXn8FZ7akXHKUJznnF0sb0c5SvWHP6TWr3zKbC6hMUOeq9-CjkoOsEqBXjZah0zuwzewWC6YbOYFlVyitt_52q6ughPSuOcqz41EvFZbx6M482pJ1NbAW2-JQ9mTwxzQ7Jg5XTKKVqS-Sk5OZhwHvDmw2YAEV7qGrtqsPq86RhzZTHl8Y5vXdbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QHSzLsILZSXID83e-GqYV3EqLsw3D6ih9_Zs7f4tAqGkpWgBdSKP3zZ4PLIFG-3ugaSnkuj3sjp-bOaz5Qu_Ltd5M2cB1sQ-XTN0qzESs9Gac3gu_JUgC2NTz7RQ0h0NVUL70VYdcOUYgzKwDhb30rh5yYxuIXth4CLEFdEIavOKJ5_5qzdRwSiadXfxV4M5-iMV-cyM7WilySDE_vNyrrCcdO5THddp8eEvttF-nU2ztvYYnd0gEy7Rl-9tL0AvgvOvbhLU9Rd5yNHQiBKV0tkFppPNQcBGs2rASwiV-n7eTMWsMm-EQBKLwZ5Q9onDhpgLnIHvnkVPaYVVBp_Xow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKFOfUsTxyMucNK7CxpAhUCBMBWHpbrXOZg6F6AWMHRXgDN4499p_K9cYKIeabcSfrdmoOWj1-_fq4XUSHsDJb_vufBI6RcImTlqrQpNuJZQxOrGPxzP5PFCCugCi9O5nRaIl7LaMNrHcl1dAIfa9PKTjcNasb6XXT6laGiXielrd-4cT0N0lesFUPt6O9aKkX0_ctuwI60_iKjxMBiGEG9zDQFnN4TEHt6rPz3OIqJjwVuTu_VSdf9PzVQnaIuA1AcN_DbYLWzgoGrPuSQ4a1NGqHiSQvELWykiRzxB_Yf7Ql_U_CHSmSsCWWoWvhAMo7Xa78FP4thubJ-KHeT-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ub-o5q8sDJjD7gP_YNOt9Yo17fPorgqft_3NOOBbq0HJ9vPYuYMLIlUcUF15VYT_0LXgwjrwEW0xS9j5bBUo3zVjZ38qSdmIQS6ZV5G060XOoI2yXUz1ByRZsDikUnlEK2oZCaDAuzDhEy8KC1-niubd4VeP7_02thncbdOcyhYP7EOzPQZdQQGIz7IYqj9KvMuwfFcWNlyqpEX10Tf65eBH0oGq43sK8GKBSnrmEUqD2zYjWdnbuw3RtsJIpyTiTV9DaKSiQ5o1ZjcjirxfEtxCxzR4lpnlHSqe4D5slKsNkhkqYMnjr_IwY_Sh8WvUZWHgno0UhlJKX7kFtM6kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mgpt4d6-Ioq1kxYe7efZk-TuTg13yrxZ10H9LaX84-ZsIT-zSrEouywPo0glYeFJolz_zFd2FoeKfcX0oo7_DhfpYeKV1NytCQYF70pzh-3D9b5XbiNTzb-noNdYEVS7uysikt8bN1-hxvIbHnoh8njWUZpTbsxqufHd2j89IbicYnbf6iMjJw0CGxmSXFByddyDpMoL0eQKbWCE3HQJgeacXpnPhDdT0qClleEnqKNL_-tjUHTQdCyvizRhQcmCzGDOWtfOVW-vQcQrNmmCvX-cgcKN_jdArTnFawEDrCwNhvaHWpAt_ZbOOROV8Dx4Rx0n054nvla2nbnBWsnhiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWaZie1Z_DZJEc2MyxIgculW6_N3jeJZef1AusI4VKh46TAF_vdPHgkpL0WJXiYEMsVynhPq0BnCeKodCTrHyNTrznizIQ-kvjvlQF28OROp9ib9ok5k-lwuP13oL-HUxRbhRZRGK8C3zG2efNtjOawKNXslRGdDv-7zKejRlt_wa3iiDHbq97D4n4FgtQLYhkobCrfjHo66Ed4BP4J0FTxidNB___mZyej0lztJ5JHOMoUmhd6PRDI3yeNef7nyYc1SbeH0-gYhq1RKJET3dZwznq0qxkxVsbyKExNb6qllrG_aZKUB7yDiiHajZXEzVjxD8yzmMvrkS6a0D2yxsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQ1Ymjz6VmXG2oioJlDHDlEpg6nrvQO-HtQoBDLBIVaWpIGgBZcdfdw5h94D7BEX16HxfUM0VXulF_t_YHx8CuWv3wUsxIiX6DJd101e_J91PoftRh0eI33xZ82Ry8yoldFp57U3xnNu5wAQTvvuqQ-HCJlJItlYgpwnicOligl_1a_qfhOGYxPxqdLjfnJCOC2Snfe3t3MdGd-jrjEYO519aMAJyZ9_tFWVAuJKP70mUFh0gIKWQBAlQXYjzJk3sgtZNm8egjya0XoDVg-yEQ5mAZb0dkuRIoFAFK1ZSo_ZnlBMPvjGhZq7PEEx8Y8ANPpYtf2XYdSyIpY_vMHiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q33OorIFSB8yHLbLkMwesMsvHHDG3r75xAwhOLrKpVSYEHa-DCEezIXZMymXBJGSbVR62ZoNlHkbyxkSi2NBUpRZ_rxH2ThfoiotmotX3yxVB-YRrUBIkK20RhOesbdA8aoSXuoz09McRJCcjcU76kKI0iXkFhIeM_c26m1_vThvF_oMzV26OJB0jJGLFLEpHg0WQC9le3wlD3ebkKA1s6V-LAz4CIGd-Sertwa8RfXXknTJTT0CzG2mG-Y1DProNW944_xtpKoSInRyDiYGHTSdUfXgXGyVHvoU21Du19QXEK9nlX2UIDnUmex9sCDX9Tr8Ii2x36DM9XO74MAt6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5376uk1tc8EMrHevrmDL7nfyBEugMzxABWOIibT62rng7SULcfQFlwlnX8FhCW90yxtNhDOc_GPwx3-gAYVHmHw1lp5Yd170SosKkEynL_94qOI-oHWCNadtYt0we-fThY29lsJU5w1A5cP0PER2FoB6_NRTcln4uAVe9anTF9DQYBulAWhIsRXeC62zxhK_DQiBbZdYL6CMZLVzo5FGnDn3h0bFKLuW6pI57DEMUkl4u8ldJ8jc4nKqlNEg52wScc0tM5CFMy8ZDZz-OKyULkReQkKNzuXVJHcDP3Nq1PvowcliEhy2F--8z3zfjOAD-WRzz6NgQ6YLXy8IyhT3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N3fQ4i5IuEcrfHiztk58q3_61JeQueZalCahowiK810nCJr-McB_GX55Nljb8fWs0UEdZwjzTJsocXClbDm4WbRf-Uw64U5KfnoxWsdhafaa3i_LXfRnz7yTRUXwdA9pui0d6quZCXKpN-VOE5huqaZyPQ9fjkupnF2Hd856AD85U3hpXOsfYDkdlO4_UNZFV5i4PMJYda5h4t57PXx1oaY2qtGuod0aAn5-GpeNe4waKrytnB36-gJ91GhgEoqqkmGdjJL_wCFXWhzh9o8ymJxb4GV77VrEu0XJ4b0HKcE4mwBtdp0_Dh96BR3xhXyvuWfn31VB6d4u1QLnAdBxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vJkwB8XSyb-B1g6YAYJUeg4MCRs_OrGSBvzoru25JwyQiQVZ1umUOHALlgDU6643G64IaoCX6fm6VXS8zXLTqZq7isL4yobSEMUKdOCmf7DH_XGrtpzUIMyNMDOYMuhBXSMH66sVvzAuAoFPgNEvF8zO-_EbDFykEz6pfCMDU0jgz84F5y4pmKIwrd6xUSET-EcCVD9mCB5HDKK5GV-9yCJta2JYdUwS8o0f-RaaI1OL_UHyVkiT76KqTD37MpHXsTB0OuwEyxMBln_epel5iXiFXjsRVPvqXkR5fYcN8kApM4Ii4tU-xXFoyQcBjreNqwan5IOG9_o5gFEb81hbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Urok2VDGiCJWNHTteZtnYCZY7gzvob1a_MTZaf9YiE5b3s4tPhsSxgjHRMM5zMMD2EwMa1gbNBf4WUB1lOdU1De7Fa4MeK9cSDP2cJqyKRxdNvZlvNi4rWvE5y7KD61FjZwOrQEKzKkK9KZxZdWA1JDjMpR3-IIILDkiB8RMQHuJKqAVwPEt2j1bGvMDYQZfDx7LuZmOXFRylbq6FJ2vxitCWBHkG8qx-ly-0FG3Ij-SfePJ8LZh4sxdFuauHN7tdcu5HM1urEWTQefVv6B3hWOAkhLB6svRfiwjKtiJuiuD8Og005v05S06xOCIyOigyS9cqPnBKOkGEWCd4e7dLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJfhpQZ4RgVtw-tQleAHP-3jP5Ei6xNgJMGWHCUSkeLKy2-9nIGLg8BS_quGSt2rEXHY7FehBS8-OKbxY07kAlq7QS7m6-D0pf4DJoIth_fU-pQF7dRYejCO69dq-XXoiR3ng_IuhVuzMgreGtkUdbk-e7pIV4tthi-MIqjafoLGHm2q74Hzt1qTSbZ_sjoqxNCBVmNYR-RGwTuB-3ZVaFN3k1ASgIosY3iQb0aj8Tc-6JrkptKUT0708o2SyaFYJPW3EfUPz9g-RZTkOrWfY-Lxzz_SmvvGaSQzVSoLxwJhnwzRM78PBYTmUiyyMt2oUKb9_mR106BomJvmFR8AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=Kshvoyz5AHaRCoWEs2iWc7rbCm5mxHAtRxlkRn8uEtOhykfzsxesG-Qn520da6ymmg-1i0PPGTGpNw9-RsvQ2lH5G86ohveG-Y5vwfxpY4HnxOY69Tw3my53aiysEAGcyA_H0W2dz9OjDq6tJcx3f7QMZS_R0nfWw6jW_ta1P1vAU6WBl_xo20NSau4NeuzGPaSOrQw4t45DSfuV3_W1Ko6vSsgNluCHOsky4ebCTbwY79714ILWI8Q3J3GUb3Km50dG2tUvxvArRpcfn0cNkEgEwk0QNUA5P1jMD7Xw8C8uzGR6MpWTCVsVMT1JaTYKvfLJdW5Zgzgbk2Tw2us3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=Kshvoyz5AHaRCoWEs2iWc7rbCm5mxHAtRxlkRn8uEtOhykfzsxesG-Qn520da6ymmg-1i0PPGTGpNw9-RsvQ2lH5G86ohveG-Y5vwfxpY4HnxOY69Tw3my53aiysEAGcyA_H0W2dz9OjDq6tJcx3f7QMZS_R0nfWw6jW_ta1P1vAU6WBl_xo20NSau4NeuzGPaSOrQw4t45DSfuV3_W1Ko6vSsgNluCHOsky4ebCTbwY79714ILWI8Q3J3GUb3Km50dG2tUvxvArRpcfn0cNkEgEwk0QNUA5P1jMD7Xw8C8uzGR6MpWTCVsVMT1JaTYKvfLJdW5Zgzgbk2Tw2us3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzXOmzFrS3Q9Yn2aVxcLTxTi0pejAkq1auCiXi5os7KE64HUYT0dlC8U_7LH36qzogcRh9zO7WcStlbU2u36jhMNm84optXWkBHzKnY0VuURHXcZdSoZ0zUyGbwydwrW-NSSGbp6hducq_hFfoX5RQOnEsTBZSywZRym8OaZoW_D5Go7xyakiAp6Dlinjwk40q9LxT7tYhRhRmHQ9IBN6vAewiB7iXIISIsJOMxLRfv0yKYa9UnR1OlaTJgRRtGmTPPIDL2sS4XlqXozlUnpDRNdvnSPLF320iH1bpGFlMAZE7b-cGIB46_sqICTdoZrDsAvuSQHqMl20DjWb0PH_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GUpUGT62a3SIZWqn_v7ffCHAZiKUAFkJCQw8iQkgIMzxIedesJtLkpnQOjtad_nmOXf0o7mJFV6ov-2d5OpLrBU2a7CiybVaRTSOrmIaJhj--wYQ3u2UlAWt9-oy54He_dfoXQwnkPCM3v9xoHtEGDu2hr1XWZ2nOYq0QtbIDWsR881zPqon9M-dkyn_z9nISfQoDy8xFQMlmpJ9WwM72Aq7NpnUNlAjATdnOa4ohQSdNVvteEg9mGEfufO5dvbmfbDeLRQ4xcR2BNSefFbGKygxaFmiZZHHWfwHInADvZt8RIctEbnqaRucBBp0GRlu-KmxN_6e4ELbnJIYbQUtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OWgfphS52ncS91yZZuKDhWV4CfBVgUB7j8XdUxkeiqOGUiyJ09mEMYrFVNtVudkdQJrXqycSo5u0MYvKOPKhjwNPYTuRP8ktBEy_NbL61g-z6TeMsQpEADFVWQxCfVrnRFLnlnIZvI4eyrDKWXW7g8Vt9nHmOmck06qGOmvcqONsXtUW55JLGLfkFruMqRmODZEA8cGAba-OD7MnXWcTqrzipFcG9glBvZDmE-fwxBp905ByhNdq58sQ0cY-06_UuVEqUO40yQMtS3t7gTSTsaGaZgwegMEj5vm-IMJhZUSJfHzd9XAwPNnavGRa3O3NUCrgpzjrjrNwSHjFYml2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dy6QSEGwvxjdkGXS-EHpwtzekFq5QTWq-1tMT1q4p_PcXBFazSlFp1IWhkYelQzseOPbKTnaj8icK65Sh6kXA7fFHjyMfUFKRoa4Wz0qmCWHEvre0Oqy_E-aq1lUVYxbQQKTqGZOkJlUL_T2AwoBfVYg9v0dfvmONGt0zen_E_CET1Xa0tLxzgW0UXlJ9_H-7zruBBFsEUVcElLRZstD2rWhjgyJkk_J3psQZZCe8xbkzYAQuZgmh5GV3GzinkJl7JgDqDa8ukzUQkBlOVX6riVwi7dDdmEvjlAmJqZ2aExQqPTiTOP8N6OfTQjRCa4s6_Gp-MV5miHhy0GNYKGK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EV4ekN-xxgGxNgFrOXwv1VOLpt6zeIFuODfceYf-Em9a_nFOWHkRW6TfTNfdfmnw2mvxRvZ6UFJZhvg0HgA68YLvGqTvV5wgJpsZwNP-j44n2l48z6Pz6tUl9r2BeK6NaX1aWlYqAJ-hTDHbL3uVbZP1IVqULGqpsWPRxX2ilvj5V-dI4y310Dc4fOJ1nj6ayLvpTm_NDKbfTCkE-vW7VlcLAJ3XnQbeF3MPBzzoXjhTdxQMtD8IuvkN3RgUoCUZpOI9Pvfp2yb0--JzdtItP0U6n3dchiLMycSNVfPHbV4PHH_w0RN8U4rHN4fBfxFN22TPHA2Hc8i3Q70FnzYHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yjk5c9v8_9J9EoVa-abCBLBvo1OCrTYZKvPd9Lpz8Bi83wecXA3ukIqUdOtgM8MDcC2sVVBnUQTQJfUsGE_2To3YGcOqHWxttfv63fAbpJTJqbLYW64WJUvmUfAVJvj-MmMIQQVeSXQrs_bm4oXxodPyYf66TRhVYxjd4TonDGWZUPuyw_P_9x8sQ6fG8q7goxdYHULilGMeXunLC8kW5DaLDTfXuzr4OL5qZH9v8CsB34cKuwDbEClw-V-97poRlOY7GYRbIbMdkEkTJ5QMtk8mMJBZDltwuDnAt0hH_cRZzlKeyrM4VqsVcR6DO8Ok1gOdj1INqgnwIEMqoiwjPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OMrrMQI61rgwb5HwG98zJYbtICg-CskNkyuYzfnIBz7MoIoZcnHBsvdGOdsTFaiRSPbvH-SKxMSw7DxnFqLLrxlTWGM325ldqscvxO2p-EWO9I3r5m0u1jmFyktVugB3pIoQFB8RFwhimhNFxp_oFcKSRi4k8WmOw8-wH8_oDgftyJjNOq1CNgxb-ClolKsUYI8bIFUiddITZsicK3KDM2BbcoaKGGdggYKahSgL6OrN4AUTQQA-2_lC3EBxRa-zyQWTFhMljx6-FxSDjKzNSJSWFHlOPwe_FCwlsOzjHmcl9bCMjs3BuAjTHn58bRViIjLmuLGjZqm9oVlFFqiE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gN-V-aMfmDEeuNBtxuACH-zgH-RxP8nW3DD-lFJ9PFK9oekTUJM1j-OAhNNmMJE4uwnb_BRsmW16rr31YX6dZc6iPZviGoJNBTe038dWeBEhyjFR0EeK-6nM1JG28qGHLqP2c5z6zpML_nZjR5nc66BCChcP5gx9UuDuRoGzEZvYPYtmVaL1o49Xe0ogMYBOFx1a1jMEUAX1w96eP5O1j9djhUgBE2ABaGBJoKgnmjFWEy0NFCD2C5O8Y6a0MHeZ2e_5XIaQkYM-niLh0fBwAFCl8POytcmPOuftJekJKKbXz5jp671jYk2hY2EZrV2ZHFrwsOEivl47sMOp22A-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vKVrPo77uWuIaANxwyatX9YUmPsnbvb4QH4_LzQw9JVUg-KUMolg77UMNZgHmSB9b9Q1Mr0nplnOkKfgC6k4rTfSmybRrnG4r79arlfWM1p1exy8T2MSJZNgl9Bte1QOyo818psjXCDH6ILeJbpoMuYC0tlSSF5keE6g-tav46wi60PkC4fXSsKF3gmkqNVd9xtLpMwX29d82YQBoBn1i_dgP6qI2H-bf-gpRGYQQhZwxE_pQUD2dtn4Tp3C4Ue9vNNe1QwAh8Xnsqo4jOPsKjvIdLXOMOTA5YCX4FH2MCUDSeRsUHQsQcRXOWlnNnniRztZLY8IoVOuSeEEQBTtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HDd0SsNl6w1bmt8Wl5qsv2BBK2BmPr4-EX26zo_Li0BfE6c7_qiYhwnpy7QTiFDphaSzS1Fh1wCunlkadVNrh9oA-ASlXAVh1awMo7BSzyIzDCrG1DKtDi1g29YbVt3_qNLPxgNfb2Sx4zYK6mvdF6aDIQfC59dKjMFkjzouSSSEDQmo2PLN3VD5e8IWdAY9gAjJWoqo1pQ31jlK4pVC5bNVYj1YozHyyc-9DQPujURdtk4wteiWz4s5m5vBSZmdGToWz9NJLr1XNq6WIp8WvXOAQpbUdVYWJSiBtgxiXrqBxA96USTXPT8_JzneuVN2rgVZBEkLSk3EDJnkl2pkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UT-EFb9dc1DtoU7u1OTr_3k1hqCDswuTWYCrhJiYmnzWKA7KWIGVFbgVEIzxGn0z3rHOiOAeEsS0Seg7y-L9jXVRwrx_YFN5ICK5YkAafbGLPOyPADcSOSjH7z-Tj2Z8FZG7kFvT90OsYSeU8qmbLPcnxE2JeLl4mQX1uQU3Qk4MDs07-CVR6iPZnetPKb89BgfeGKKbO2RqWoPvvlTA4DxpLoshi2VlwhhXGgmlinikwyO5jHIPa9I53xKVRjjvKfsgPsCfP6QCVUhS5PLYeYF9hD7xxWcB6I4UQN5Q3AuJZjdZ2cHUIj7EbImGk69CM11895r2Dvr2DwSIJJpIng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h724LIYb09bC_b_30PRy3TAVZyyxtT19S0bnBS8OsrRpdw4rmPQ2ITgoAQ5QUbQWAvpspjN4JdIJ2by5ReySSFHg9dlmYCvurPD-cSlf_W9uwzqqeVRtqdlJSukrQ1qU3Lnzxii6u1MPReoAY0Jkv5JWiJXiI5RBn37hudUcHWd0S5bfKvRvZIDar3wJfGtqMO3g6OC1HGdxNipAPYwpoF2Qh2ykS6WQtYayeMO6XfT3W9erkQfuybIszJDByMr_iHTQcMBlgB-xbTpqriWsIsIvlGDFMQSJakmB8Stfrp6BmtriJZHyBt8eoxJtvDn5PJdcY3hTGfd9BVaLHc3GOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-XXIdOUMFCRnxoJRoSEr2oiHyWhYiG7veu6mMgQovnUHijaeGdbEdLNB11kk-HbwEjgjOBHkj_0qfV0Wj8Pe8dpwGB4FKLaMscM4f4FVeYS_U0A3fs61v9Mdvg6R4cGvIXCSX1O0zS3wL0BsbIO5sLTatWypTmgHatIX5_i2C6H1ylRsPXUvfpSqJc5FEXPVipC4NL5CUYf2xRVt2PsZ57I7hQ6BclGZfGmkXWYv7OOoH5UzlVAsmt3Ot3eMNpN-nu9qKcCW58_3ew56BdrL9wpU5s7HfhBrikWhaxlAa4j5sHCTGyceb4hCnTCnsk0xv5-N210DNOo0rGolClrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kbZxZBqk7KXHOEq_KRY9QTBlVxhmFSPD5JsjVj0alb5MvgRuS4AQICrX2n9PcBMJhvTr4RSWQdRMsXQASOy_IFnZVufm02tWeusMPvjywzO7TI5P1Kf9puS4fmKW4DPD_P1OUh2jc-kvg8Q9nWA7rsLs3o7B_KJ35OCHjo0IrjOMpDzOTCatXNf85bTZczL9O0pnIBA0juwvKjHI63pFH-C1KPsi97KrlI54Om08_aqsaP1KnEUQABKyNDJTy2lVE_HcuRZbcIc8hAl4orRwimWavhEof0Ge-rZQPeiIEcyUSfk_2u-8f-EL8sR7Qmla58rzSqJsJNaldWJiju2pbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bshy8QWezKoPQAWvg_yKDRkPzADECy98Xr31XbCU_Df4yuZbh0Vn9wqEza0WVFhxBSV1MCTF9uM5cbBaMMb26Yz1Vj6nAioTJXlLfLaD6hXLmMp2OCqu3ch-f7sOBoOGPGlB3o_B-mUicsPXPznVjq9CZ5dFx6WopmTRAq0Oqr9qe2OqpFeT94gPA_E0iF52hX34xWV3G0VvLoCabburHp_HoulNL5gICtyfdLZWzJoXkq2WZGHTlFUxUiBnCdBUJWU0UIgStL3QyNcOsZLokXJxJOR6ukd1z0gltYOUYtdHtUGKFSTXGxFor2vUkTg83C9OWfn3xGDLgExhLR5nnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bXDwsg5B-55nIFrDJ7TkW2yI-lhZry1FV2bxV-Vz-jYPeDuhAQk2e072L50MX3gM0hXx9Ty3XeMzQ3TFqxy8R9eX1YxyK_H0E5A4owqmtPzU1hLbNMRZ-SP02T89YXqvgg9Xwh8moFcmr6w1CTe8CIXJ0WD-Q9fZKdznjP_P2khfOzJzmyW3fkQFoEOZPIXnUSfO2vmM-glVE-WamrKwYMBX0VOftJstTG4iDZNmx99xQnQ-LkUqm8jEduUkwHNbszXLIkATICzj1BIloEAmcpv232VPoxeJBt0odvn79nZnJ-0L8lxo0DlAn4E8flYvJb_d4qD4xbUaO31_TnNUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H7YN_JSNvfTlzgGDUa7K-kqXTj4yU_vBG-SMbh94lJjMWIlUP09iSCZ1Z7oEsvg0o9bBkWFZG2bBvV_iGSXX-UF6W1Rf7HmqHaSyKmQORjMnzZs0fR67qXKUsc-XgVZNyVrMqSu3-KXZtLXZHK1ZEoPxQAUew9F5SLj7lTicux4YXBMv5IOXWqaeXNl0RLRRCl5zthkSPNtA9RzfLrfgBgX3zvh-m-x4pMFL_Q7hKEkkPjK6Yc47JRhQ-38ORdRv8rrx985HDEK_mqilk9APHpkmKgHIAAU1kDXOg5vkL4pWQk1rMOBTR9tw5t91QIAQdIOat-jNREtgC0osDAXQjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f7Ms6jF5WvM8BTZANxM5wjxZilQiZfmtiB0INbZvbjLtjAU6yJ8IJ6f6uqqch2EttU3qGjL5klcA7FIVjdIwXYQelhaevF23tx9NwcCHSNcCnvPfTPQavMqouCxOjVw8UuWyp1qt-gdXtviyGKi9WvOIwq7okvKOYQSLs3KpdbJFERCyQo2R0PC32AEa8Z4W9N1p3YwE1IkJ-z1uFcIQ3zKff_7tpqj5At_S5Buk7hKXColIipqUp-M5xNMY4FHepEqxCFXz0J6A6Ks__u8ua_Dihuz06JcTkgKqTIqM361ujKCizIabQsz6BlF2lP7s3tvQqDAwmAGSZkwfSy8wIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mABVOp2rdqAM6PjjDcBSOUG4A8vFgUwzarye7vnYqRHXj1xEuPDwcx6_TzV6ISDbAbRFesTH-GY89TSFx-mzofhQMTIkJ3AQdTpa-MrJw6Rdgoh_D_moZkiBDcfC8HSbjDiteIIOmjMUYpbYP6CSWOCpOZULVMlN6fE7DxbsXDvjVLHFOIsdgTpzF3riMs-Fw7M7xH_BQy07bF0Zv7pPoGV_tmFjnaYmRtGIj8T2xL7ZLjPEhF4Y7SJyCATekHb8IKG1zEZpn1-8fLLZU-17DmhwxCnA_TTVeHTNF1fhwXnLxNLJNEktl6Wmn39q0pNJ8mI0qKCsi7Pkhqju3Uob_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tvj3zsMwS2adqbHe_R6CZTs243USXzYKULmlSFzlRsYPfBUYlkCm3gO4xXSwwipztMuCRjjOGDyIRy2mrWO8Y37pbvB705kfIbOffcbBDnRAOWlj5LDliF-hlqMQ3Xdm1e5jVyb2VDt17aHxseL-kvGmSiHv5wbdI8j6S24QCklDES1RcJlMrSmdm7yN6KE3wcGEIrEf9usgU_Gdi_qP3QN9IAk3_fRsWMdFLoDTDNpgH3gbrGlFHRHGjUdp2UT1UhAsffUQRH6mXUXU-epvptOHMnSIpE-bsr6ti1idfyES7eCDOMBApXfMANhO5WwBn508ClxXtOfD91UDTh7ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/neYKEHOSy2ccKH2Q-8847_MZ0jTtqoYESlZQsoyu0DamoOtAkJD4lG7gffYBlJC4XZ2845rehx4l_8GX7wKuzqwrT9ekDRQ6Nk90OmEi7Bg5Hui2-s0svljbL37S7aPBJPRZxSCi3qrpYOTY2-v7T0I8BuWRf88wMX0QBZyD1bBAj1Oqfjc7aWpBayVjZcqsUopTLBX2nWZtAxIJ3tCad5dLwZJ-sfbaaFK1GNaICLOFpPqNU17_yFqz3csc4C_3wFKuxZaoUkq_OrQCV9RxtszH2WbRlENAiyvMss6wOhoLhmnL5sT_LFX4ZJEEGN-9F3IE-klL-_tl2XhpC0QuWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HsOOLigQ--Z1XGkS59hTx_oGUA2fNOPs0vD0kymRRlO3IgcF-PdHztYUSJiaKvj_mjFz1BOwq53P7kycK15b2tVue0fMQaKGRZwTIFswOYZvIJPFnModIq8Jz8wjF4b2ReKK-1RDh6FGSxn0hpz_iflnH7TmtPcH2SWnyLWZ9XSIEnR9CSitJC_ckCRSSNOi6e1IEytPmQ5X6n8LK66qtKGpZJIiqyMjdkf0U0aEeHXYDYulEU9fux8ZC1_0Ofd0KwTapN9dm-MRihmbE2-cEt-6__EXK8kEz4yzuzryqDQT37ZjyvyNfcKBLrDPvomhRQAHXAIa-Smht4Xud8zQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pbqDy2G96GSTszggJwP0Mm0q_mEw95dIu9-oqggyL0ftHFIZH7sErop9ZejkEtPn4wEttQK08Kd6MXf0xoY0Lb6aswQ7aQJhf_9ndSB3fFqCYZ1D_l4nOEwKFeANAOyek7vYx1z63K_cxKsY0UC3_k0WYBAKz0A-3ERacfJm8RAKRscQ5GwRQAVVqDGoKv68IsvoNmNX8HyClJ2hT1H2UCly09hrTrdAFERTCQ5d3uXrHMz4k1cwFP9Wzmk8VK0tSOvpe82PwU1gReEOxr1jwDmR6SIpa6LUfTPRCTTNI5bXCAUcObaINPs1JtWAKMTj-P8MyMl7xggP7Nvqi3eAKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VGTU9niVjvO5mBfsbvguwfoiZSnSl7ht0SDpozatGx3bzactRttzn0j-r8MZaqg9nEU1Lg9QxDelRq3ygTkS9b5QU5kkj1hQbhyreDeHJrVZrVVlE6Q_T2VKixhPpyCmDG3FBk8WZWq_K1kICXocmR5piJiz60l2DFyjfa8RVsz2NeOQk16hp3tMsLrvPYjkhnbKpQ-eSqpkP01J8NXgezQwUHAJLtjbmRB1cGF6gMDMpMeNoPwxhnlphrfZl4PsOw_QrrBB0C_CEcJcpQJYQv6d9SOuOm3UgUcJSIOc8cZK48OJ6hNurOkptYgnZKhEeUrjiGIcGnP2L9KHGCuG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G0b4yBDIqS-SibuwdnNy7WfOFKrZJ8gsoYhr46Kv_HG-C9zGgMiFsDQdCJT_KDyVnF8KSzXM_uYXErBgFp0OyrfhTp5F0bdT0zeEAZnvYUuB9b-z6iXtDGMUZwI2-svMu1HhrMcrrPT0X8buik3_ZirPHSPAAvi6g4lSRNYNOy3dC8PWk5d2lCxs_lhpDuS_kntR5nSy4ZcUhqqvA89E5vcgKuxpFxxd9NtjMBzW81nMoKtZkDZyFMZhO4K8mkKq_JTdrQMRGmjmVxSkTS4wtmpjKA2p9MFuw2vk1rPrvhTE5ec1A30VBI3pg5gA0AjIkUAEFTEinyZ3eOPOW65Gvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bPsFcw99cX9N8kQdREMFUL_H5wZ5udbWvGKAzeKsd-QBh2Fltu0V58N9Fc3Q28xbbNroYlOFw-ipxZLesnBlLN2VkQkDZgrzSIW7oJhwqnGuatAONOCwSDbx7mBZUXgXkT0_7lGM3w4rUNLM2au4JiG6o_LHjkl2rkI081J3nMI4qPXdNWmez69NXBHe4mxMjytUEjS5BdvI42lDfv0s2qOf2IRBwWA6_ulIurKIEaQE-3E7s8CD1xjcZh0zfrOJ08NEAM7RqlH5hEHEjXwusneSxtfAU7gx3Zm7wjsc4PYI1-i6cD0_IwouR-hbIMMq1PeItaUAAW4d9lUTYUjWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qM-nTyPeTbuXG_m2Z1veHdUv9cxD06O0ivJ2DOmDiZbF1_NGt8qTBGAHU15IjkITIfSwSRpIjH_zONs7ZUfQQMQjCjr7Xh4uVCo7EVPO169p0gMNZzAdiA1j4I4Ly9vUMtI_dGv9lYfH9zDoV1mICZ0mPplfU_uVzHQgCeC3chD1QK6__mTmHk4DY37eALRro7STCNGyVC5NWD3PJ_aVIHBI5S_WttGBfYsmpp9F5sRNo7D2lhtAa2obGBMloXYMNmZPEaZNsvKSXoUd-T4ROSqD1aPHPs8NqvOQrgqUfMeikmgQXUAxUg8GmZmLMdqWTo7m6HXf5a1CfuxS0bCMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o2uC7XvuzECScGKwOI57aHUXcveRQELyIss-_NcgRcnSG6DkKzKlrtqNkhw2Pflc-fOWWtuz7lMtjX8dEGMH3UZYUdfpiZUM8guzEfEUJKodL8ELn7gfQZgwb_kvEgQ_-rQ-10EhZ0N3L9NQEn1b7NMSrA_ZFIjXVTjrR_TUiCQ84EXV5EK7kiDPOaAq78GVLph9S4dElkV4UA4zGl4xZmex5ewWpMvg0jQ9xfvR58-7q8H-2Gd1aybFhxPJAdZldjsZ6q0mwuaGkLPw4wiiWmi3A0DJbKoM2rlsEfrgf3uZQfpn9xCeq05oHMlRKrIgAOwbaycGNG-zOX6H-dc6dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/frjx-owmHpljeFEhjfmiWTkwbGLMOfLy_jCeW5P6g39rfoqungGavHfN2zhwJZclO707-JjJ99RxBHt557ZFk8Hs6gsUW3lLujJwyYWssx3NLmPG1OfsEsxGk49DY3_ObHk6BNqgH4jNAnI68qekU6XqRkpnxNRLPLnuEvwFXF3Y4lZzC4zijOhHwQvl3GZRWrAkdkmLUAoPLD9lwlVadiNqHBaQ0qPv9HMCSApi-gAS2K35mRzb4KOsTAvbeeGcnckooqDpN5Pjgy7m_slCKMrFyhJrliaO1inrcvum1SBpc329Xt6yXf2mkT_JH1w9iYYTNupvAGAJmpIocc1nTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t04JjTIz-fEVLWmW4T1uz64f6ytsgrtueazULdFSGmkKpK18L7pIZ5bY4cfEVPAsFzlXAKRcvFY3QuMpHAxsYevTqJsNoy_F5qweg1b41T24Pj_9lEC8oIe3tOuKROUqDu1XpmxRYxlGsGazFW0niDkJVwFYPmn-WxpzeVWJu-9wT0v2DYugv4-xTTzDgMnubLsmrG2vni53V8Ku30aFZ3a48QJz8-TPlBAk-EotZOrh9bvmNj68vLXmJJxL571q5_Soez7_G32msR0V8fCUGHoM3cosJxyprOuP0dZT3M7xyK9VGDgibtxUKtkF5edQanEx8l_ChLJta6kd40h6Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YNXLxoTHENQ3sqjQyaBMDsmI4XDN6ARHVE1EevQvpIoROcZ09DoI_lXt84L5UI9FOieZxTKwpuj1cLrF9RLj_kzg4P7xFbJtb37nNa255WLu7wBm12BSq_3o1KEHSnjotb_lkN77Nbdu4gZupRlHtOWypfi1Qu9JO7s8QtSz6BQsYEnraTW7t2DLkmshR5BFXUnkw7_PhY_8JH7---SW4DBc6-SCMV8KyFkR2B5xyoG5NtuSq5-fIbSQtC4UDeTF8L32HyTtBDKG6pYHuOGXfg69rAhdE2QxBrxWral8_zz9kGpULqlzU6We4kfy2s67rp9Oh9Ezmn-0R8ePrF6yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtjQKsFwQYaSpow4a7t1Wu1Qh3711PpZxeWi0vMblbK5kUaRcRKa-no_MF1maO7S0ywUlYZ8PTDMW0ZWxv3vSKc-eIdGP57Nk3tpXJMbnWM7jamkVV6pkaQOWxVZCY6eVW2etziFNUNfkTQXUw2PanqrdmAQhrFXghCM4aALgeur17lkEjhc2fPed34zrVaKJH9WW-ryAzZ0lXXG6TDKwXRMxP8ErBqcXQLqFV48BTHv9sM65pivA7n6vXNS-az49PHoW1p9uE5wq8wVE5T3PpuSZrmx-sHJMRovmcJGfWfCeksUKUUEfLujLSXKE9env5902Nco9amykbqyB1E52g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8ABVORpm4K818qs623Thxv6bOZkBFD0in2yLxJCdholcUsXkPx-V3cqjd9mz-rRCcyVs_8emcSxddTJ3zUZFIw9MxWFUNo9FNk_v0-QkPhXrIk9YrlUijCsvRfEgLiJlnRJCqtWAx0IJPpocu6k6aldQiUZFbWEbkmK-e_LdCtDshb1AoX9-JseG8zEKMUGOAdiuiwiy9FWUKanAlYluaECwZdTJJq-5PiqOJczwYoWT71A5vuoPiSWus3g6iQyB8BF8Y_kQr7JsPefza4LtZLcWjGCioKiUSPuopXn-SF49OlNocq5MX1v8Ah4edkwyM2AxbAODq_mPuzrx1um1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
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
