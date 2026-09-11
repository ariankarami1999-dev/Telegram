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
<img src="https://cdn4.telesco.pe/file/Ct3vlM5ZkRlciPe6X46QAEjK6Yif7oItDdqsjlBRqr2L-_ViRb4XD77L_OHh_-b-J4pLMb8uF8TKKm8ktQIwvQDPPXgYM9ILTWLXzIucH-a8pjqnKfVK_9HaBcpVghPqTP8OLmzbGhOAlelXofyutbjgJJWylribDuBbHvb_XqUh_iq-tt1jFbTgZR8jzb2MWUe2zI4o9A7tnEbtMstPkjFZvnUEmpECOLm0NivQixJLZv8ymoYQFUI76q3gK6KLah-znfSOr2znsohrOTs9FYHusODzE3XF5wr3sdYq2dufqOHMAyZUvshSfW_QNGVag509WBDfHCvMFuumg5PNTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/139906" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUTR3T3cCUqBipph6nIsspCa2BUQaOc6ia6iOQvWvfLHaPsQPQmxwwKQtkIABStPr3fFWE77Wb_R9fVM6258k_0q8cchHI0vxojzfIQiYiRbthfnOCCG3IJOlgoRC-ZOGpECmaQPlXqiTgz_uA6lRiwL4F9eLNTPyEzHmvuWASOwH6w-IFo3DLlZkovqUS5JYDMoA3MvJIvrmG0sLWGJ61_kbxTBi6SHGwdwHTcP8SJQyR5JdAvCOAb-bo8BngfF9A-uv6CCxcrGFe8wyud1Q7e6v64Wkt2ZpEUo-MZSZ8CGVOLSdHDhB9WIGNpDC7PCQ25KpfBxADz3qz3Rm2lPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/139905" target="_blank">📅 18:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/139904" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
مهدی تارتار بزودی و بعد از بازگشت دنیل گرا به تمرینات درباره‌ی ادامه‌ی همکاری با او نظر میده/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/139903" target="_blank">📅 17:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/139902" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATQaLdt8XcnymJwJl4XAE903qiffVXUP3JCIdk717kPtAPHKsbFuiO5K0zgS8j2dkAsWPSG7ynfo6or6TCkX7rn6OrzLyOVa3LqW7FkPCaHQxPiv3DvrD5R65a7YwKo1N9647TRFVerFAcaIaYgEGNiCYfTYdYO1jNyWX0h7xw3sFyg2_XLK4aiqWJrdAjN_gF4yt5sMG-nPagj57sF3Fhxb5JNY6bmjWbCEC45aRfKg6pInzsmNyt_BEMGRP2xvxSS3IlbT9hh7Z0iH35t1JoY-UlTg6NuXj3HW8aU8Zwb3_49aBCy7i_nrd_9gGXwCIgNDgaPfNBoBkgzMpc3WlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
پوریا شهرآبادی ۱۵۵ دقیقه ۲ گل
✔️
شهریار مغانلو ۶ بازی فیکس ۴۶۰ دقیقه ؛ ۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/139901" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/139900" target="_blank">📅 16:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/139899" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
🧤
علیرضا بیرانوند نتوانست کلین شیت های خود را ادامه دهد تا رکورد هشت کلین‌شیت متوالی پیام نیازمند در لیگ نوزدهم، دست‌نخورده باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/139898" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
فووووووووووووری
✔️
اسماعیل کارتال سرمربی فنرباغچه پس از مساوی مقابل رم در هفته لیگ قهرمانان اروپا از سمت خود استعفا داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/139897" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/139896" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/139895" target="_blank">📅 15:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJJ1VhEc365UPSOyYZ-C8xSg89HSYgw9VGupjtIdO8F9yD0ZLvQQVJiX_DY80GUlNF_xD0u93pG6OfUZtNKD7-DPSgLOnED5lDLJGnqS9kOroYJcEy9ssfibSRV5VDb4_g5QuDNeanvdluOgDQMwaY2r2uMQoQEi9_xDeJfNWLgsfEWLvvPsiwTJRMKW8DXRRkac0WUbkq9rCuL0YCWe4THH0huOD--rOkIvUwTf3zG9vB4BXRncfGvSF18sE6qSFCj5pZ4dFeO7LNdfjeZqChOMWyjjfs7_9HeuJbiWEWV67wc9rUEbQEQ-QeUUaxPVemIhHM-3K9D6ktS1gvMWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/139894" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoRhJ_HJYPUfE_gVKdbPswyR4oPzCg8lXKtkHT3JlBYfm4QVl0TY04lCeMSU2wUBkirGYpkD7ay_02mmOxJQ8FwsQZgK8t9zqsdrAlS1yBkhbEe1so4HdS9hU-CmPHDxEHhA5y_1zKeFh5AYZ-QE3mhbDV5kTWOUvIpRAqvSpflaaUoaVXF25yZ1uUOEXzIokjeYPmrIlTujUP7sIeHzgsguns5I-qoRfbS_O3dq4GI5j8vhc5yKR9j7LI9VV7I-7ustBis1SUUz9jh-K5Jt1g7ws_0cwMzKV3G6U__L28vZR5nvV83KAM6q51_lkIwSg_knPHtDnUyChDvaIdq4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان نیز پیشنهاداتی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139893" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139892" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⬇
علوی سخنگوی فدراسیون فوتبال: پرسپولیس دوست داشت بازی‌اش لغو نشود؟ باید بگویم از آن طرف خیبر درخواست داشت که بازی‌‌اش لغو شود
✔️
✔️
خیبر فقط یک ملی‌پوش داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139891" target="_blank">📅 11:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDR4bucjfNCH6969Xqj8DrJbQGJwMFlF8JCX7diQa03VJzKhFt7hoEad0XDAQJPNEmybYM17bMtn2HQJPb-zIvfugvAowDKhDK-z_6OD1k3jlHCYG7Rm7goLS4l7meByX4KP5LaPwy4PAOZ9g8sbjMV1CjvZUxXC_x2ztNJ2dsgwmaMluBd5shmqqRK6PKm0zFRuLf738Vo30jWOvN3cFcdNwaPy7snZ-9z_kQgydctSF64MKpjnjuEfu1feVHicIlDpbDdi-lEULxo60IjrbPmtyZ2Q4uC-qesjZp-gYJdKllAPO-w4ijJkF3uzVcmJ4xnK2sT8JkGj8i-tp9cfCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
از دیروز و با آغاز دور جدید تمرینات پویا اسمی مدافع وسط 17 ساله که همراه تیم ملی جوانان در ویتنام حضور داشت در تمرینات پرسپولیس حاضر شد و اکنون پرسپولیس سه مدافع آماده برای جانشینی محمدمهدی زارع در بازی با خیبر ( در صورت برگزاری ) در اختیار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139890" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139889" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
آسانی مصدوم شده یا از ترس شکایت جلوی السد نمی‌خوایید بازی کنه؟ ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139888" target="_blank">📅 11:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/139887" target="_blank">📅 11:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
۵۷۲ دقیقه مقاومت بیرانوند برابر رقبا
✔️
✔️
علیرضا بیرانوند از آغاز فصل در ۵ بازی، ۵ کلین‌شیت پیاپی را توانسته است به‌ثبت برساند؛ اتفاق ویژه آن‌که بیرو در آخرین بازی فصل گذشته تراکتور در لیگ‌برتر مقابل گل‌گهر هم توانست دروازه‌اش را بسته نگه دارد تا ۶ کلین‌شیت…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/139886" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
رضا جباری مربی پرسپولیس :
✔️
من با علیپور صحبت کردم و قول گرفتم که بتواند امسال آقای گلی لیگ برتر را به دست بیاورد و این مقام را تقدیم به خانواده‌اش و هواداران پرسپولیس کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139885" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139884" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=ioAVIaiOOsAFYI8fsW2yViIQ20dbrhbjtBFfD4AnB-Wq7Gg5eMFcvV5VgNg8xxy1W5ffHcSSlriohlsCT7SrMWzsrhDbej2YTOi95fj97MURANu06upgGeFyHvC4CXYl7KAbP0Fr8p-s91zaNGACEMWWPDyJBw0-PlODfsPh1ghv-LeVth1QouosTNCmN_6X4jr3Ilb2e10Dk-iDDODFp-hPvwY78E7DU98UsQhICLCXKJPxMb3-H5glomDLuDGfuX3xlM9IHhj_trLddPiCF016_u2BrKnA2NxRgZJ-gdjQ-GF2Uw2ZzuwBPy6cPRbpLInf0it62_IbOU0QZQG0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=ioAVIaiOOsAFYI8fsW2yViIQ20dbrhbjtBFfD4AnB-Wq7Gg5eMFcvV5VgNg8xxy1W5ffHcSSlriohlsCT7SrMWzsrhDbej2YTOi95fj97MURANu06upgGeFyHvC4CXYl7KAbP0Fr8p-s91zaNGACEMWWPDyJBw0-PlODfsPh1ghv-LeVth1QouosTNCmN_6X4jr3Ilb2e10Dk-iDDODFp-hPvwY78E7DU98UsQhICLCXKJPxMb3-H5glomDLuDGfuX3xlM9IHhj_trLddPiCF016_u2BrKnA2NxRgZJ-gdjQ-GF2Uw2ZzuwBPy6cPRbpLInf0it62_IbOU0QZQG0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حردانی: آقا سهراب جواب تماس هامو نمی‌ده
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139883" target="_blank">📅 10:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/139882" target="_blank">📅 10:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139881" target="_blank">📅 09:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R13O5ZoJOM85FxC9WjztdsLmP5ei5TVdd8vGd4PWxoApfdpgb-fbjI0_Kkc_sx0cfWeEmR5kPQW1L4UVgvnZujwWRiE5qWvz212WKAmPYBOsL9T1KJg4BEBYw8gCAKl2V8CvCclqr8Fo_xwHe7WVE2NLGD48baStvyWmInC3lNUT0KQgQK-DCIf2wMjsRTHo9xKXvJyl39ahJC4Ilk9DFUFPTESZfqp-YlwbvM1BAKoBXm9_W8MDoFZMAhuuQ9_QAVikW9KHbZZnExOt8RghZ8c3rRbs02zFnQk3I9bRp81jqbsVHwFT0nVHc8gmc0kzRC5cCbdemEijljLKBdQoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سابالانکا مقابل پگولا؛ قدرت سابالانکا برابر بازی حساب‌شده پگولا. ریباکینا در تقابل با گاف؛ نبرد سرویس‌های سنگین با سرعت و دفاع. دوئل‌هایی نزدیک که تمرکز در امتیازهای حساس تعیین‌کننده است.
🎾
Sabalenka -
🎾
Pegula
🎾
Coco Gauff -
🎾
Rybakina
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139880" target="_blank">📅 01:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139879" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=rI8mUW2K9HWJ8LElr3WkExH9eL1yEP5JOetzCWe3FyV_tCiBn3CO2agOAK492f39Ri7JIGbNvsCmHeKhXNUpMedXuzR06KEZ-mAKjAZOR6GbpgdwY8hoUiMYIiaV3gycYy8Ebi3Wh3Ua82RwZDJsTEQHyEJQnRUdTabJRxDP7MjHHihfdPBoIJ5DlvejYn3AC7yulijA5hoT6ze3EnmXNKbErvl4kAP0u1Z4TZi6ZnSQPtiP3LJF-RDPMfqWcOs3vlMVKhjwyOyuO1ZBQCpO36vlwEqZQkuGwkuH475SbEsGOWfGUZ0IsBJiR7r1Z663rp6Pn0wbau4h-HepCBYsczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=rI8mUW2K9HWJ8LElr3WkExH9eL1yEP5JOetzCWe3FyV_tCiBn3CO2agOAK492f39Ri7JIGbNvsCmHeKhXNUpMedXuzR06KEZ-mAKjAZOR6GbpgdwY8hoUiMYIiaV3gycYy8Ebi3Wh3Ua82RwZDJsTEQHyEJQnRUdTabJRxDP7MjHHihfdPBoIJ5DlvejYn3AC7yulijA5hoT6ze3EnmXNKbErvl4kAP0u1Z4TZi6ZnSQPtiP3LJF-RDPMfqWcOs3vlMVKhjwyOyuO1ZBQCpO36vlwEqZQkuGwkuH475SbEsGOWfGUZ0IsBJiR7r1Z663rp6Pn0wbau4h-HepCBYsczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
دقیقه 95 بازی استقلال و پیکان، یاسر آسانی به یکباره بعد از سوت پایان بازی مصدوم شد تا شایعاتی مبنی بر مصدومیت تعمدی برای عدم بازی در لیگ نخبگان به اوج خود برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139878" target="_blank">📅 00:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139877" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC8b-X_o6rWaUnKm3CKpHOKey3gvs61343OY6qBNA42vveyXTo2V4Ivy1e75zZd_6F2ZHaZ7SJjCprRXLZVE5cCQVaIqZYNOL_IAIkcU4EzmLXRk_FQEILoP4evwLbZfEPH227TQb_Z3VO7VVdq8F5rkitOUYO9-FK4BjSytQyV0_VQ2USK6dycODDKzzYx7LH99aDIpA35BkT4FZb9Iz_51xOomy1MPaUNIgObs17gDZ0tnR49aiAAqixChNoRyJi1kJ-baQBu__B4YdEleU_aIq88XUb5bsr5R4HNP77mPq6g9R10RjitiRQqc7rbLyLow1PLx3kHHoUQnn-Dpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
جدول لیگ بعد از بازیهای امروز
پرسپولیس با برد خیبر می‌تونست به صدر بره ولی آقایان رنگی تصمیم گرفتن خودسر بازیها رو به تعویق بندازن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139876" target="_blank">📅 00:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🗣
🗣
ورزش سه: یاسر آسانی به علت مصدومیت دیدار برابر السد قطر رو از دست داد
‼️
السد قبلا اعلام کرده بود آسانی بازی کنه می‌ره شکایت می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139875" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139874" target="_blank">📅 23:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
#منهای_پرسپولیس
✔️
✔️
استقلال ۴ روز دیگه با السد بازی داره و السد تو پنج بازی اخیرش دو بار حریفش رو شیش تایی کرده به بار چهارتایی و یه بار سه تایی فقط خدا به دادت برسه استقلال :)
✔️
✔️
شما فقط مراقب باش دوباره خاطرات العین و الوصل رو تکرار نکنی قهرمانی…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139873" target="_blank">📅 23:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139872" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxtW0NJTLiUvL9x3lvcqsksRcN27yPv50vE67ZYoPV7TCBoQYHKdbVr2XR7BGOkXmuG1EdG9jpplWz5PThtlzbu4O-T5R3BxyW8L1fZUj_B41_-rvei3ptybDx2kGl4oannYk6TkLL-ng8pyHn-I09uA7Rz70vbW7AGb_EoLZpkEC066vj_w2aZvXH3_ircSy9SRVUIfK3Me1vCjcsq0uQV3aW0geA4Fm9FQhHv9qC9JIqU5VVyhJQ3u9w7YrfZALlCf0ctPtR-KrfI1-zb9zMH2SpSEldNmlj7oCTVGFmTA9ufy0Yicdt6im4rXUbF2KeA5jlI28GzlqXr8BZtNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پس میگفتید که استقلال خوزستان ضعیف بود که ما چهارتا زدیم؟
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139871" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139870" target="_blank">📅 23:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
خداداد طلبکار هم شد
❌
❌
بعد از فحاشی ناموسی و اظهارات بی شرمانه به امید عالیشاه، سرپرست تراکتور:
❌
❌
دارم میرم مشهد به یک زمین چمن سر بزنم؛ فردا از باشگاه گل‌گهر کسی ویس منو ضبط کرد در جریان باشید/ پسر بده فوتبال ایران هستم؛ شما خوبید  «سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139869" target="_blank">📅 23:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
بازگشا :
❌
سازمان لیگ بهمون گفت بازی بخاطر یک ملی پوش خیبر لغو شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139868" target="_blank">📅 23:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139867" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ww5EFLOaWuPJB2QHt8uvx8PrHQcps7Zh_SJPwuCpxAy6RQzi_OVSKE0bHWrqKN1FUmQMaKkqvRcT6qMWOyNd95G75qjrsF5FGbD0KO8K27MALRyhL5WGp55QiU8mjZXHTruB5IU8xlMPD07WaM-5r08TtaK3KEHMmOhrmdcFVGTCPg-jYDwipvSqmaNR_IKiQ1EZ3M7MQxHt38laiXGKp7MfMPr-vvF1ziVGLirjlsYH3FmDuVwULlH8OW5tyd_StcsHj0kwItKRaRCeMGDfiYWvuGEhxJqTejs5GIJId-2y7s-7yEMUQBHbh-4wLXuuIrL94FMMlESS9AWkQfbflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139866" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: تصمیم لغو بازی از طرف خود سازمان لیگ گرفته شد و برای ما عجیب است که چرا دیدار تیمی که فقط یک بازیکن در اردوی امید دارد، لغو شده است.
✔️
✔️
تمرینات و برنامه‌ریزی پرسپولیس همچنان بر اساس برگزاری بازی با خیبر ادامه دارد.  «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139865" target="_blank">📅 23:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
⚪️
⚪️
⚪️
⚪️
❌
⚪️
⚪️
⚪️
⚪️
⚪️
⚪️
لعنت به بی برقی ...برق نداشتیم شرمنده نبودم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139864" target="_blank">📅 23:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tflixpyCW-Hz3sS6xGZP7Oz4eZRT7PcIH0NEgnVRNRKUpYansf3jwDvMtW0TmIQh-q29BdNRziLv_xg43jcov5eOM_klOjf6v1e3I-t7mGCagWCDNKFqSfd1SvP3VU1tdsJNKcVjS3Y-r0Wva-AnKtrr2CzukZzJJXzM9hPICQmbxahZgjkwMsyzTmmAiHealNFpxsx1xC9Cg8UR-Ij1nWus-0XqAvYha6lmyv7mNXQ0_PdhXeP0olg076s6Oo6K76EDarY6d3VmNiYPnuxErHLN3sPo_16QP2-vzjET85kWb9TfSZ-zo1ERDGlNwYmgaJlMeDEqAKdVe1EnD3CRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Bayern -
🟡
Bodo Glimt
⏰
Tonight 22:30
🏟
Allianz Arena
🔵
بایرن در برابر بودوگلیمت؛ بایرن برای جبران لغزش‌های اخیر به دنبال یک نمایش مقتدرانه است، بودوگلیمت اما با فوتبال جسورانه می‌تواند دقایقی دردسرساز شود. با این حال، اگر بایرن از همان ابتدا ریتم همیشگی‌اش را تحمیل کند، مقاومت نروژی‌ها خیلی سخت دوام می‌آورد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139863" target="_blank">📅 21:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139862" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139861" target="_blank">📅 20:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
تارتار:سازمان لیگ بیجا کرده بازی مارو لغو کرده...ما هیچ درخواستی برای تعویق بازی نداریم و میخوایم بازی کنیم...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139860" target="_blank">📅 18:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139859" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139858" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139857" target="_blank">📅 17:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139856" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139855" target="_blank">📅 16:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139854" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139853" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139852" target="_blank">📅 15:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139851" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139850" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
با اعلام سازمان لیگ، ۴ دیدار از هفته هفتم لیگ لغو و زمان جدید برگزاری آنها متعاقباً اعلام خواهد شد.
✔️
ذوب‌آهن - سپاهان
✔️
خیبر - پرسپولیس
✔️
ملوان - فولاد
✔️
فجر سپاسی - آلومینیوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139849" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔔
🔔
فووووووووری
🚨
مهدی تارتار با لغو بازی با خیبر مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139848" target="_blank">📅 14:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn8JJttsewsaudJBGMO3kEeXWlAZcerUoTbtJT-xsvN66_jc8LqEvrvJDmi_S5IsMOoTQy-DUyj8PPXyQe0iovHNdTLTW-h4O0700ju6ojZeu7zH-UzVV2c-iWZTa6z2HOgE3pRLKjq6MAiIr3GyT-ZPtM_MkkLmavchJWQbPq_ZSvudrxchCFvUJCZbSUi0Xo4u65z4R7AspU3OuJ8nqxrcwsmCcvPn1a5aqmWX0U_lnBIHiYicYs1ZisMcdDBul5Fw_2vOP392hoo3VypKpNC6IjYB0oxf6DQ7ZjMnQEpTk0THl8IO3wGGoASmBYtt3hkC-7yMbY2mGFhtjGoz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مونیخ؛ بایرن آماده‌ی شکار بودوگلیمیت!
⚽️
بایرن با مالکیت و فشار هجومی بالا، شانس اول این دیدار است؛ اما بودوگلیمیت نشان داده مقابل تیم‌های بزرگ با جسارت بازی می‌کند.
انتظار می‌رود بایرن از همان ابتدا برای گل زودهنگام فشار بیاورد و برتری کیفی‌اش را به نتیجه تبدیل کند.
[
بایرن‌مونیخ
⚽️
🆚
🇳🇴
بودوگلمیت
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139847" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
پرسپولیس-خیبر فعلاً طبق برنامه
🔺
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر ارائه نکرده، با توجه به شرایط موجود، این دیدار طبق برنامه قرار است یکشنبه برگزار شود، مگر اینکه در ادامه تصمیم جدیدی در این خصوص اتخاذ شود  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139846" target="_blank">📅 12:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
یحیی گل‌محمدی: فکر نمی‌کردم لوکادیا روزی در جام جهانی مقابل آلمان بازی کند/ او یک بازیکن حرفه‌ای بود/ از روزی که در تمرینات حاضر شد مربیان از نوع تمرینات‌ش راضی بودند/انگیزه زیادی از خودش نشان داد/ لوکادیا یک مهاجم شش‌دانگ در محوطه جریمه بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139845" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139844" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139843" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❤️
علی علیپور:
🇮🇷
🇮🇷
واقعاً افتخار بزرگیه که اسمم کنار علی آقا پروین، اسطوره بزرگ پرسپولیس قرار بگیره. خوشحالم که با کمک همه هم‌تیمی‌هام تو این سال‌ها تونستم تعداد گل‌هام رو به 96 برسونم  ﻿
🔴
ولی حتماً از قول من بنویسید که میراث، رکوردها و افتخارات علی آقا…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139842" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139841" target="_blank">📅 11:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
عبدالله ویسی بعد از باخت مقابل پرسپولیس، از سرمربیگری ذوب‌آهن استعفا داد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139840" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
سازمان لیگ به باشگاه اطلاع داده اگه میخواین میتونید طبق قانون بازی تون مقابل خیبر لغو کنید و بازی نکنید حالا قراره تارتار امروز تصمیم نهایشو بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139839" target="_blank">📅 09:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139838">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139838" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139837" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE24NE6dPNYYw3XwP4K8S36d9GQsm_fPRdeD2Xbd7WuyFKG1-3QDX87_9ztPwzwB0h8Z9K3cL7Wm1KeeeQvgK54Q01rif402koWQH9gG4IKfgiSTmq2id-iEwChyTFMn97p6xBU3ujWMQqS5Lbgb1oz3TIfZh9r1iQaSnIPM5YKNdKec2_m36duoIYLnXnovnOeqVEpPuPFM_iNCiHqVcVyzkaIeCmZqsfOCXrntTusuWF8SHCF0LCYMSc9kJN7U-ZiFoFjClFtA3YswWP1BvFM2rN60dqX_oKu3zumCIygBJ2P0KdhbT-GM_P8AZx1IiC5YdeJRjKBlh2YB2Rc7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139836" target="_blank">📅 09:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1EgQK9RPfLy6qp1ZoNzRrqjyqmI4tRg6nLrhBKFZClhqI6N7bgA6NLUd_By-AgEC_jqBIenJ2oPTS_33zLrUwpThb688dqcZvEEnEkTwIphiU_w4Z0L4tIMjMKporCg5_MSkVG_X_kbx7Ru2CDwBV1hkmmgqAdEWT4XTdO2OOjL1sx-6L7WpZY_pmzJx-3PUFIAZHW0nNBwq75RcJE2S7xeoBHf9kD7jzMET-fMwp0WJ2mZENVGuLcX5uZk4MnJG0zEOIBuRVoDLlEFCgDuNYj_aUM64Yoh8Y0F2ZYk4n7zOHtmKomdKl3QQZy4FtgLRIn7DzxSEpmm5vvAJ9MKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال قدرت با جاه‌طلبی در یواس اوپن
[
الکساندر زورف
🆚
بوتیک فان دِ زاندشولپ
]
⏰
بامداد پنجشنبه ساعت
۰۳:۰۰
🎾
زورف با اتکا به سرویس قدرتمند و عمق ضربات از انتهای زمین، دست بالاتر را دارد؛ مخصوصاً اگر بتواند رالی‌ها را کنترل کند.
زندشولپ اما با سرویس و بازی مستقیم می‌تواند ست‌های نزدیک و تای‌بریک بسازد و زورف را تحت فشار بگذارد. با توجه به فرم اخیر زورف در US Open، کفه ترازو به سمت زورف است.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139835" target="_blank">📅 01:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139834" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
احتمال لغو چند دیدار از هفته هفتم لیگ برتر
✔️
برخی باشگاه‌ها از جمله سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند و به‌این‌ترتیب احتمال دارد برخی از مسابقات هفته هفتم در روزهای شنبه و یکشنبه لغو شود.
✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139833" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139832" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=pf-m39JDYypaJe9GxEKgShYFr-CHghWyZqrugSz28KsOmkhjIxSfKwIKVLsKyZEOTM_L6no9gL8-hlbR_WtTMPHFWyQSQL-hyx8GVKRvhbe5HUtYUyPb3c78V2i8dSeC6irl38e48IhuyCy3jV3AdCP5rh-6Z2hBhoWQLvfp5ECHJBC4muBTF2s87HgXKC9R6IUpJH8TgaMJhk9yDl7wSbnlJeicXnrtcsHHUjziiPS65106CJS-11OEruRaWDdpDQNfsvxY6R6WhdCuGfBNDbW6ZGWj1EGcrKHyIWUzR0XIIulHN-YLYAe80StpULDTlAS-TsNDAt4n8B280-QYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=pf-m39JDYypaJe9GxEKgShYFr-CHghWyZqrugSz28KsOmkhjIxSfKwIKVLsKyZEOTM_L6no9gL8-hlbR_WtTMPHFWyQSQL-hyx8GVKRvhbe5HUtYUyPb3c78V2i8dSeC6irl38e48IhuyCy3jV3AdCP5rh-6Z2hBhoWQLvfp5ECHJBC4muBTF2s87HgXKC9R6IUpJH8TgaMJhk9yDl7wSbnlJeicXnrtcsHHUjziiPS65106CJS-11OEruRaWDdpDQNfsvxY6R6WhdCuGfBNDbW6ZGWj1EGcrKHyIWUzR0XIIulHN-YLYAe80StpULDTlAS-TsNDAt4n8B280-QYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.»
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139831" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=iY1G_Rsp5pkTEsBpghu-A1dbTXMkCiPejmWd-l4PYii_KKsbtl4shRa_kCHIuuT8krXW-BlDA_3nBB_tXIX_9n8jVJdLc9hNGLDMDFtd4KWt1LDp-DjVdkPvz4yUSqfcfUWXfFQz5cPLZpLYXusFRh9k93aRgfV_kcDpm9OU0nqE6OEIH7cSrRbjiRaFrglLCFRHlEDE9EyW7mWfCY-DrxgC4ZKQhE_yq6dZsg5RhrDYTZl2dWbsCmrGWCFuF6dqg3KW99rcZmU6_fM0PbKfBu-vgfR02FdXbFwfrvplKoQDq_6cWo9YDqPyxekbe4XB1ze_LTDseLC5e-wYVF7vCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=iY1G_Rsp5pkTEsBpghu-A1dbTXMkCiPejmWd-l4PYii_KKsbtl4shRa_kCHIuuT8krXW-BlDA_3nBB_tXIX_9n8jVJdLc9hNGLDMDFtd4KWt1LDp-DjVdkPvz4yUSqfcfUWXfFQz5cPLZpLYXusFRh9k93aRgfV_kcDpm9OU0nqE6OEIH7cSrRbjiRaFrglLCFRHlEDE9EyW7mWfCY-DrxgC4ZKQhE_yq6dZsg5RhrDYTZl2dWbsCmrGWCFuF6dqg3KW99rcZmU6_fM0PbKfBu-vgfR02FdXbFwfrvplKoQDq_6cWo9YDqPyxekbe4XB1ze_LTDseLC5e-wYVF7vCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139830" target="_blank">📅 00:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139829">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
پزشکیان پیگیر حل مشکل آزمون برای همراهی تیم ملی
🚨
مسعود پزشکیان، شخصا پی‌گیر رفع موانع بازگشت سردار آزمون به تیم‌ ملی شده و به احتمال فراوان مشکل آزمون برای همراهی تیم‌ملی در جام‌ملت‌های آسیا حل خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139829" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139828" target="_blank">📅 23:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139827" target="_blank">📅 22:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
برانکو: هر روز به بازیکنان می‌گفتم پرسپولیس بزرگ است و نباید معمولی باشید
❌
❌
به شاگردانم که مربیان بزرگی شده‌اند افتخار می‌کنم
❌
بدترین روز زندگی‌ام، روز از دست دادن جام مقابل استقلال خوزستان بود
❌
❌
اگر به عقب برگردم باز هم پرسپولیس را انتخاب می‌کنم
❌
می…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139826" target="_blank">📅 22:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
❌
با اعلام کفاشیان، جام فصل قبل به کیسه‌کشا داده نمیشه و باید برگردون تو غار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139825" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139824" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
✔️
هفت ورزشی: فدراسیون با اعلام استقلال به عنوان قهرمان فصل گذشته موافقت کرد
🙁
🙁
🙁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139823" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdivZe3Hh8G_kPJpaGhOVzR8x-AVRLOacmFf2Ky1dn236JQYK4A2zVzysZ43cKFn2WiTxyeKUcksxMw2TgdxvYfMhbi-XclZ1UIeVudAKcI68DrlgXRuWw72uX8qaz6Br_0g-RfVOnEEQ3MpIC8nDAOwvFu5ZuBouSq5OrIaMx8hBCNHIrnXzcusRDw2TEMC8c6cL5eotDZcMksl7OJ6oMkGLJbRuev7Eozg9iJ8h-quDPmaWuD2ZDePKAp-r0YerZ15CHz3FnFsSzi5XzJNwAOR0clI1NztT1QhJUrSdGClH7qxalzJTQVp8yMwPVxGEw1r32fEpM_LVDZV1puDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یه جام از منیریه پرت کنید جلوی این کصخل تا خودشو نگاییده
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139822" target="_blank">📅 21:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0EeoR7opOjeBUFBalvBcNjqDqmjGEDU-XvGiINV4oKK9GHMWqqBNx93EVODndkEuTBpGEks9U8qc-GWAaXCY2cMhSIrwJDgXpP0ndp_VDVfNqMh2MeRhpNyVGiBlIWcYI91Y6a9NeH1666GHvIBdNEK8liqEQbFNiJJWDYgOMEC5wAFL8bq3RS5aWe7sI5Yms4ApWKCX-JYEzOyqsYHx44_kp7VxM6vO_r9_wABqdsXch8xuNOVeRtk7TCiNQl136n8Bl0-gj_kN5H-Jk3KDo2kWRfQeZo5L5XaZWYkrHSXmnmzyy8J57w5oHvmeU73T2BPTBP1ICCLU5_aqP2ugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دوئل سنگین امشب؛ لیورپول در برابر اتلتیکوی سرسخت!
⚽️
تقابل فوتبال هجومی قرمزها با ساختار دفاعی و ضدحملات خطرناک اتلتیکو، نوید یک نبرد نزدیک و پُرتنش را می‌دهد.
[
لیورپول
🔴
🆚
🔴
اتلتیکومادرید
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139821" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚡️
⚡️
ترامپ:
⚡️
از نحوه مذاکره آن‌ها راضی نیستم من هنوز درباره ایران تصمیمی نگرفته‌ام، آنها نمیتوانند سلاح هسته ای داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139820" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKXx1kUCNUzHnjD4rreQO4___MQYxk6UrlAgGWWD2F5YxKY7E4h3xYt2GRn4fxaGRyJDkgAjToGftc3xjTylScMQaCgDpTBDM7n4hjMcr21T4QXEereBv-Q8d9dDjIn7T6Y2b7xdnjBMGRyyK2u1W4Xki-7ZykZhbrH5iy-ox6CFLt1J2r0kczdX6bjKR39TmhpdX0tYHyQi22ITwtUMdiYM1r0CB-pdkTM1NQNgJBLu2Owweb8sdqnuBjewJ51mcW4do9eYmBrkRjBNKGLv7Z3bKQGIRD4uUUZgFaFvUNZOK2FkQFDquLmPWd2tYVaAff17hyszGDJ01rYnhbX4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس مدل دهه شصت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139819" target="_blank">📅 20:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139817" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139816" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139814" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAsVpwKayNUQDG8NqRT6ho3Ce2zpfyBf0VI_qi3I0ynXy83qhDp1HF19lO3bg8IR_60aHzg7-CyngpMTxZ2TqTQ3yRN4ucbE2IJdpqh8HV77WdJ7PYgQqT6664koUm8Uf9cfyEM_Mx0H8UTRHbSXUNmHcONGRq3c2g2I8jqfyaaBYE-7z6YmPDXp5xzDIGfLq3-F2-B70SkY6GCcrpFxrSvZMEQEuzLH-_tXY4DAZeHHwzhzQuOYdUwGK1Yuk3EIPoidDNw74eIr1WJWED-Of1Eze2WPQ-7A50bGbYPt2yDlUiPtYr1BYxOWIYlhtzY_V0b0yz3O6qcsCBIMgNyjDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رسمی باشگاه پرسپولیس؛ اردوبادی کناره‌گیری کرد، صابری معرفی شد
‌
❌
سیدعلیرضا اردوبادی، رئیس پیشین هیأت‌مدیره باشگاه پرسپولیس، از عضویت در هیأت‌مدیره این باشگاه کناره‌گیری کرد.
❌
در پی این تغییر، حسین صابری به‌عنوان عضو جدید معرفی و با انتخاب اعضا، رئیس هیأت‌مدیره باشگاه پرسپولیس شد. مراسم معارفه وی نیز در نشست هیأت‌مدیره برگزار شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139813" target="_blank">📅 19:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139812" target="_blank">📅 17:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139811" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139810" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139809" target="_blank">📅 17:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139808">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139808" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
فوری؛ سردار آزمون پس از یک دوره غیبت به تیم ملی بازگشت و اسمش در لیست اولیه جدید تیم ملی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139807" target="_blank">📅 16:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139806" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139805" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
